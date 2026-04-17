#!/usr/bin/env node
// build-prezentacja.mjs — generator prezentacji Reveal.js dla trenera
// Output: dist/prezentacja_Mx.html per moduł (standalone, Reveal.js z CDN, CSS inline)
//
// Analog do build-kurs.mjs, ale dla innego formatu wyjściowego:
// - Reveal.js 5.2.1 slajdy 1920x1080 (bez sidebar/progress/quiz)
// - Stack pionowy per lekcja (section/section...)
// - Sekcja "Notatki dla trenera" → <aside class="notes"> (plugin RevealNotes, klawisz S)
// - Przełącznik języka ES/UK/EN/PL (wspólny localStorage z kursem)

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadConfig } from './lib/config.mjs';
import { loadLesson } from './lib/content-loader.mjs';
import { mdToHtml } from './lib/md-to-html.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '..');
const TEMPLATE_PATH = resolve(__dirname, 'lib/templates/prezentacja.html.hbs');
const STYLES_DIR = resolve(__dirname, 'lib/styles');
const CONTENT_DIR = resolve(PROJECT_ROOT, 'content');
const DIST = resolve(PROJECT_ROOT, 'dist');

const LANGS = ['es', 'uk', 'en', 'pl'];

// ============================================================================
// Helpers
// ============================================================================

/**
 * Escape HTML special characters.
 */
function escapeHtml(str) {
  if (str == null) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/**
 * Dla mapy { es, uk, en, pl } → zwraca 4 `<span data-lang="xx"...>` (ES widoczny, reszta hidden).
 * Używane dla inline tekstów typu tytuł, opis, label.
 */
function langSpans(langMap, tag = 'span', extraClass = '') {
  const cls = extraClass ? ` class="${escapeHtml(extraClass)}"` : '';
  return LANGS.map((lang) => {
    const content = escapeHtml(langMap[lang] || langMap['es'] || '');
    const hidden = lang === 'es' ? '' : ' hidden';
    return `<${tag} data-lang="${lang}"${hidden}${cls}>${content}</${tag}>`;
  }).join('');
}

/**
 * Dla mapy { es, uk, en, pl } HTML-ready (już zrenderowany) → zwraca 4 `<div data-lang="xx"...>`.
 * Używane dla blokowych treści HTML (np. render markdownem).
 */
function langDivs(langMap, extraClass = '') {
  const cls = extraClass ? ` ${escapeHtml(extraClass)}` : '';
  return LANGS.map((lang) => {
    const html = langMap[lang] || langMap['es'] || '';
    const hidden = lang === 'es' ? '' : ' hidden';
    return `<div class="lang-${lang}${cls}" data-lang="${lang}"${hidden}>${html}</div>`;
  }).join('\n');
}

/**
 * Labels per język dla etykiet typu "Semana", "Lección", "Minuto".
 */
const LABELS = {
  semana: { es: 'Semana', uk: 'Тиждень', en: 'Week', pl: 'Tydzień' },
  leccion: { es: 'Lección', uk: 'Урок', en: 'Lesson', pl: 'Lekcja' },
  min: { es: 'min', uk: 'хв', en: 'min', pl: 'min' },
  objetivos: { es: 'Objetivos', uk: 'Цілі', en: 'Objectives', pl: 'Cele' },
  contenido: { es: 'Contenido', uk: 'Зміст', en: 'Content', pl: 'Treść' },
  terminos: { es: 'Términos clave', uk: 'Ключові терміни', en: 'Key terms', pl: 'Kluczowe terminy' },
  contenidoModulo: { es: 'Contenido del módulo', uk: 'Зміст модуля', en: 'Module content', pl: 'Zawartość modułu' },
  gracias: { es: '¡Gracias!', uk: 'Дякуємо!', en: 'Thank you!', pl: 'Dziękujemy!' },
  leccionPorPreparar: {
    es: 'Lección por preparar — contenido en fase de producción (Parte 4+)',
    uk: 'Урок у підготовці — зміст ще не готовий (Частина 4+)',
    en: 'Lesson in preparation — content not yet produced (Part 4+)',
    pl: 'Lekcja w przygotowaniu — treść jeszcze nie powstała (Część 4+)',
  },
  notaTreninga: {
    es: '<!-- Notas del formador: se añadirán cuando se produzca el contenido de la lección (Parte 4+) -->',
    uk: "<!-- Нотатки тренера: будуть додані коли з'явиться зміст уроку (Частина 4+) -->",
    en: '<!-- Trainer notes: will be added when lesson content is produced (Part 4+) -->',
    pl: '<!-- Notatki trenera: zostaną dodane gdy powstanie treść lekcji (Część 4+) -->',
  },
};

// ============================================================================
// Builders — poszczególne typy slajdów
// ============================================================================

/**
 * Slajd tytułowy modułu (hero) — 4 języki.
 */
function buildSlideTitle(module, config) {
  const roleMap = {
    pomocniczy: { es: 'AUXILIAR', uk: 'ПОМІЧНИК', en: 'ASSISTANT', pl: 'POMOCNICZY' },
    'młodszy': { es: 'JUNIOR', uk: 'МОЛОДШИЙ', en: 'JUNIOR', pl: 'MŁODSZY' },
    samodzielny: { es: 'INDEPENDIENTE', uk: 'САМОСТІЙНИЙ', en: 'INDEPENDENT', pl: 'SAMODZIELNY' },
  };
  const role = roleMap[module.role] || { es: '', uk: '', en: '', pl: '' };

  return `      <section class="slide-title">
        <h1>${langSpans(module.name)}</h1>
        <p class="subtitle">${langSpans(config.courseName)}</p>
        <span class="module-role">${langSpans(role)}</span>
      </section>`;
}

/**
 * Slajd spisu treści modułu — 4 tygodnie z liczbą lekcji.
 */
function buildSlideTOC(structure, config) {
  const weekItems = structure.weeks.map((week) => {
    const block = config.blocks.find((b) => b.id === week.blockId);
    const blockName = block ? block.name : { es: week.blockId, uk: week.blockId, en: week.blockId, pl: week.blockId };
    // Składamy tekst: "Semana X — Nazwa · N lekcji" dla każdego języka
    const itemTexts = {};
    for (const lang of LANGS) {
      const semana = LABELS.semana[lang];
      const lessonsLabel = lang === 'pl' ? 'lekcji' : lang === 'uk' ? 'уроків' : lang === 'en' ? 'lessons' : 'lecciones';
      itemTexts[lang] = `${semana} ${week.week} — ${blockName[lang]} · ${week.lessons.length} ${lessonsLabel}`;
    }
    return `          <li>${langSpans(itemTexts)}</li>`;
  }).join('\n');

  return `      <section class="slide-toc">
        <h2>${langSpans(LABELS.contenidoModulo)}</h2>
        <ul>
${weekItems}
        </ul>
      </section>`;
}

/**
 * Stack pionowy lekcji (jedna <section> z zagnieżdżonymi <section>).
 * Jeśli contentMap (4 języki) jest obecny → full slides (intro + sekcje + notes).
 * Jeśli nie → placeholder slide + komentarz notes.
 */
function buildLessonStack(moduleId, week, lesson, contentMap = null) {
  // Meta per język: "Semana X · Lección Y · 120 min"
  const metaMap = {};
  for (const lang of LANGS) {
    metaMap[lang] = `${LABELS.semana[lang]} ${week.week} · ${LABELS.leccion[lang]} ${week.lessons.indexOf(lesson) + 1} · ${lesson.czas} ${LABELS.min[lang]}`;
  }

  // ===== PLACEHOLDER (brak .md) =====
  if (!contentMap) {
    const notesComment = LABELS.notaTreninga.es; // komentarz po ES wystarczy
    return `      <section>
        <section class="slide-lesson-intro slide-placeholder" data-lesson-id="${lesson.id}">
          <span class="lesson-meta">${langSpans(metaMap)}</span>
          <h2>${langSpans(lesson.tytul)}</h2>
          <p class="lesson-desc">${langSpans(lesson.opis)}</p>
          <span class="placeholder-tag">${langSpans(LABELS.leccionPorPreparar)}</span>
        </section>
        <aside class="notes">
          ${notesComment}
        </aside>
      </section>`;
  }

  // ===== FULL LESSON (z .md) =====
  // contentMap: { es: {sections: {...}}, uk: {...}, en: {...}, pl: {...} }
  const slides = [];

  // Slajd intro
  slides.push(`        <section class="slide-lesson-intro" data-lesson-id="${lesson.id}">
          <span class="lesson-meta">${langSpans(metaMap)}</span>
          <h2>${langSpans(lesson.tytul)}</h2>
          <p class="lesson-desc">${langSpans(lesson.opis)}</p>
        </section>`);

  // Slajd Objetivos (Cele) — jeśli istnieje
  const celeMap = {};
  for (const lang of LANGS) {
    const sec = contentMap[lang]?.sections?.cele;
    if (sec) celeMap[lang] = mdToHtml(sec);
  }
  if (Object.keys(celeMap).length > 0) {
    slides.push(`        <section class="slide-section slide-objectives">
          <h3>${langSpans(LABELS.objetivos)}</h3>
${langDivs(celeMap)}
        </section>`);
  }

  // Slajd Contenido (Treść)
  const tresMap = {};
  for (const lang of LANGS) {
    const sec = contentMap[lang]?.sections?.tresc;
    if (sec) tresMap[lang] = mdToHtml(sec);
  }
  if (Object.keys(tresMap).length > 0) {
    slides.push(`        <section class="slide-section slide-content">
          <h3>${langSpans(LABELS.contenido)}</h3>
${langDivs(tresMap)}
        </section>`);
  }

  // Slajd Términos clave
  const termMap = {};
  for (const lang of LANGS) {
    const sec = contentMap[lang]?.sections?.kluczowe_terminy;
    if (sec) termMap[lang] = mdToHtml(sec);
  }
  if (Object.keys(termMap).length > 0) {
    slides.push(`        <section class="slide-section slide-terms">
          <h3>${langSpans(LABELS.terminos)}</h3>
${langDivs(termMap)}
        </section>`);
  }

  // Aside notes — sekcja notatki_dla_trenera (dowolny język, ale bierzemy wszystkie dostępne)
  const notesBits = [];
  for (const lang of LANGS) {
    const sec = contentMap[lang]?.sections?.notatki_dla_trenera;
    if (sec) notesBits.push(`<div data-lang="${lang}"${lang === 'es' ? '' : ' hidden'}>\n${mdToHtml(sec)}\n</div>`);
  }
  const notesContent = notesBits.length > 0 ? notesBits.join('\n') : LABELS.notaTreninga.es;

  return `      <section>
${slides.join('\n')}
        <aside class="notes">
${notesContent}
        </aside>
      </section>`;
}

/**
 * Slajd końcowy (Gracias).
 */
function buildSlideEnd(config) {
  const subtitleMap = {};
  for (const lang of LANGS) {
    subtitleMap[lang] = `${config.courseName[lang]} · Fundación EGIDA`;
  }
  return `      <section class="slide-end">
        <h2>${langSpans(LABELS.gracias)}</h2>
        <p>${langSpans(subtitleMap)}</p>
      </section>`;
}

// ============================================================================
// Module builder — całość slajdów per moduł
// ============================================================================

/**
 * Zbuduj SLIDES_HTML dla modułu:
 *   slide-title → slide-toc → 32× lesson stack → slide-end
 */
function buildSlides(module, structure, config) {
  const slides = [];

  slides.push(buildSlideTitle(module, config));
  slides.push(buildSlideTOC(structure, config));

  const lessonBaseDir = join(CONTENT_DIR, module.id, 'lessons');
  for (const week of structure.weeks) {
    for (const lesson of week.lessons) {
      // Spróbuj załadować .md dla tej lekcji (wszystkie 4 języki)
      let contentMap = null;
      if (existsSync(join(lessonBaseDir, lesson.id))) {
        try {
          const loaded = loadLesson(lessonBaseDir, lesson.id); // bez lang → wszystkie
          if (Object.keys(loaded).length > 0) contentMap = loaded;
        } catch (e) {
          // brak plików — placeholder
        }
      }
      slides.push(buildLessonStack(module.id, week, lesson, contentMap));
    }
  }

  slides.push(buildSlideEnd(config));
  return slides.join('\n\n');
}

/**
 * Załaduj i skonkatenuj CSS dla prezentacji (design-tokens + cards + prezentacja).
 * NIE inline'uje Reveal.js CSS — to leci z CDN via <link>.
 */
function loadInlineCss() {
  const tokens = readFileSync(join(STYLES_DIR, 'design-tokens.css'), 'utf8');
  const cards = readFileSync(join(STYLES_DIR, 'cards.css'), 'utf8');
  const prezentacja = readFileSync(join(STYLES_DIR, 'prezentacja.css'), 'utf8');
  return `${tokens}\n${cards}\n${prezentacja}`;
}

/**
 * Zbuduj pełny HTML modułu — string substitution template + inline CSS.
 */
function buildModule(module, config, template, css) {
  const structurePath = join(CONTENT_DIR, module.id, 'structure.json');
  if (!existsSync(structurePath)) {
    throw new Error(`Brak pliku structure.json dla modułu ${module.id}: ${structurePath}`);
  }
  const structure = JSON.parse(readFileSync(structurePath, 'utf8'));

  const replacements = {
    MODULE_ID: module.id,
    MODULE_NAME_ES: module.name.es,
    MODULE_NAME_UK: module.name.uk,
    MODULE_NAME_EN: module.name.en,
    MODULE_NAME_PL: module.name.pl,
    COURSE_NAME_ES: config.courseName.es,
    COURSE_NAME_UK: config.courseName.uk,
    COURSE_NAME_EN: config.courseName.en,
    COURSE_NAME_PL: config.courseName.pl,
    SLIDES_HTML: buildSlides(module, structure, config),
  };

  let html = template;
  for (const [key, value] of Object.entries(replacements)) {
    html = html.replaceAll(`{{${key}}}`, value);
  }

  // Inline CSS — podmień 3 <link rel="stylesheet" href="../styles/*.css"> jednym <style>
  const linkRegex = /<link rel="stylesheet" href="\.\.\/styles\/design-tokens\.css">\s*<link rel="stylesheet" href="\.\.\/styles\/cards\.css">\s*<link rel="stylesheet" href="\.\.\/styles\/prezentacja\.css">/;
  if (!linkRegex.test(html)) {
    throw new Error('Nie znaleziono bloku 3 <link> do stylów lokalnych w template — format może się zmienił');
  }
  html = html.replace(linkRegex, `<style>\n${css}\n</style>`);

  // Walidacja — brak nierozwiązanych placeholderów
  const leftovers = html.match(/\{\{[A-Z_]+\}\}/g);
  if (leftovers) {
    throw new Error(`Template ma nierozwiązane placeholdery: ${[...new Set(leftovers)].join(', ')}`);
  }

  return html;
}

// ============================================================================
// Main — iteracja po modułach
// ============================================================================

export { buildModule, buildSlides, buildLessonStack, buildSlideTitle, buildSlideTOC, buildSlideEnd, loadInlineCss };

async function main() {
  const config = loadConfig();
  const template = readFileSync(TEMPLATE_PATH, 'utf8');
  const css = loadInlineCss();

  if (!existsSync(DIST)) mkdirSync(DIST, { recursive: true });

  console.log(`🎬 build-prezentacja — generowanie prezentacji Reveal.js dla trenera\n`);

  let totalSlides = 0;
  for (const module of config.modules) {
    const html = buildModule(module, config, template, css);
    const outPath = join(DIST, `prezentacja_${module.id}.html`);
    writeFileSync(outPath, html, 'utf8');

    const sizeKB = (html.length / 1024).toFixed(1);
    const slideCount = (html.match(/<section[\s>]/g) || []).length;
    totalSlides += slideCount;
    console.log(`✅ dist/prezentacja_${module.id}.html (${sizeKB} KB, ${slideCount} sekcji <section>)`);
  }

  console.log(`\n🎯 Zbudowano 3 prezentacje (łącznie ${totalSlides} <section>)`);
}

// Run if invoked directly
if (import.meta.url === `file://${process.argv[1].replace(/\\/g, '/')}` || process.argv[1].endsWith('build-prezentacja.mjs')) {
  main().catch((err) => {
    console.error('❌ Błąd generowania prezentacji:', err.message);
    console.error(err.stack);
    process.exit(1);
  });
}
