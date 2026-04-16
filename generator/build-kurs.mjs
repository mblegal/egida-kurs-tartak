#!/usr/bin/env node
// build-kurs.mjs — generator self-study SPA dla kursu tartakowego.
// Czyta course.config.json + content/{Mx}/structure.json (+ opcjonalnie
// content/{Mx}/lessons/{lessonId}/{lang}.md oraz content/{Mx}/quizzes.json),
// łączy z szablonem templates/kurs.html.hbs i CSS-ami (inline),
// zapisuje dist/kurs_M1.html, dist/kurs_M2.html, dist/kurs_M3.html.
//
// Gdy treść lekcji .md nie istnieje — generuje <article> z placeholder.
// Gdy quizzes.json nie istnieje — generuje placeholder final quiz (5 pytań).

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadConfig } from './lib/config.mjs';
import { loadLesson } from './lib/content-loader.mjs';
import { mdToHtml } from './lib/md-to-html.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '..');
const DIST = resolve(PROJECT_ROOT, 'dist');
const TEMPLATE_PATH = resolve(__dirname, 'lib/templates/kurs.html.hbs');
const STYLES_DIR = resolve(__dirname, 'lib/styles');
const CONTENT_DIR = resolve(PROJECT_ROOT, 'content');

const LANGS = ['es', 'uk', 'en', 'pl'];

// ===================================================================
// HTML escaping — tytuły z structure.json trafiają do atrybutów/treści;
// treść lekcji z .md jest już zrenderowana przez mdToHtml (HTML OK).
// ===================================================================
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ===================================================================
// Generator: 4-językowy span-set (ES widoczny, reszta hidden)
// ===================================================================
function langSpans(textMap, klass = '') {
  const classAttr = klass ? ` class="${klass}"` : '';
  return LANGS.map((lang) => {
    const hidden = lang === 'es' ? '' : ' hidden';
    const text = escapeHtml(textMap[lang] ?? textMap.es ?? '');
    return `          <span${classAttr} data-lang="${lang}"${hidden}>${text}</span>`;
  }).join('\n');
}

// ===================================================================
// SIDEBAR — 4 tygodnie × 8 lekcji, każda lekcja w 4 językach
// ===================================================================
function buildSidebar(structure, config) {
  const weekLabels = {
    es: (n) => `Semana ${n}`,
    uk: (n) => `Тиждень ${n}`,
    en: (n) => `Week ${n}`,
    pl: (n) => `Tydzień ${n}`,
  };

  const blockByWeek = Object.fromEntries(config.blocks.map((b) => [b.week, b]));

  const weeksHtml = structure.weeks.map((week) => {
    const block = blockByWeek[week.week] ?? config.blocks.find((b) => b.id === week.blockId);
    const weekLabelMap = Object.fromEntries(LANGS.map((l) => [l, weekLabels[l](week.week)]));

    const weekLabelSpans = LANGS.map((l) => {
      const hidden = l === 'es' ? '' : ' hidden';
      return `              <span data-lang="${l}"${hidden}>${escapeHtml(weekLabelMap[l])}</span>`;
    }).join('\n');

    const weekTitleSpans = LANGS.map((l) => {
      const hidden = l === 'es' ? '' : ' hidden';
      return `              <span data-lang="${l}"${hidden}>${escapeHtml(block.name[l])}</span>`;
    }).join('\n');

    const lessonsHtml = week.lessons
      .map((lesson, idx) => {
        // Pierwsza lekcja w module (week 1, pozycja 0) jest aktywna
        const isFirst = week.week === 1 && idx === 0;
        const activeClass = isFirst ? ' lesson-item--active' : '';
        const ariaCurrent = isFirst ? ' aria-current="page"' : '';

        const spans = LANGS.map((l) => {
          const hidden = l === 'es' ? '' : ' hidden';
          return `              <span data-lang="${l}"${hidden}>${escapeHtml(lesson.tytul[l])}</span>`;
        }).join('\n');

        return `            <li class="lesson-item${activeClass}" data-lesson-id="${lesson.id}"${ariaCurrent}>
${spans}
            </li>`;
      })
      .join('\n');

    return `        <section class="week">
          <header class="week__header">
            <span class="week__label">
${weekLabelSpans}
            </span>
            <span class="week__title">
${weekTitleSpans}
            </span>
          </header>
          <ol class="lessons">
${lessonsHtml}
          </ol>
        </section>`;
  }).join('\n\n');

  return weeksHtml;
}

// ===================================================================
// PLACEHOLDER lekcji — gdy brak .md dla żadnego języka
// ===================================================================
function buildPlaceholderLesson(lesson, isFirst) {
  const hiddenAttr = isFirst ? '' : ' hidden';

  const titleSpans = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    return `          <span data-lang="${l}"${hidden}>${escapeHtml(lesson.tytul[l])}</span>`;
  }).join('\n');

  const placeholderTexts = {
    es: 'Esta lección aún no tiene contenido. Se generará cuando se añada el archivo de la lección.',
    uk: 'Цей урок ще не має змісту. Буде згенеровано, коли додамо файл уроку.',
    en: 'This lesson has no content yet. It will be generated when the lesson file is added.',
    pl: 'Ta lekcja nie ma jeszcze treści. Zostanie wygenerowana gdy dodamy plik lekcji.',
  };

  const bodyParagraphs = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    return `          <p data-lang="${l}"${hidden}>${escapeHtml(placeholderTexts[l])}</p>`;
  }).join('\n');

  return `      <article class="lesson lesson--placeholder" data-lesson-id="${lesson.id}"${hiddenAttr}>
        <h1 class="lesson-title">
${titleSpans}
        </h1>
        <div class="lesson-meta">
          <span class="lesson-meta__item" data-lang="es">Duración: ${lesson.czas} min</span>
          <span class="lesson-meta__item" data-lang="uk" hidden>Тривалість: ${lesson.czas} хв</span>
          <span class="lesson-meta__item" data-lang="en" hidden>Duration: ${lesson.czas} min</span>
          <span class="lesson-meta__item" data-lang="pl" hidden>Czas: ${lesson.czas} min</span>
        </div>
        <div class="lesson__body lesson--placeholder__body">
${bodyParagraphs}
        </div>
      </article>`;
}

// ===================================================================
// Pełna lekcja z treścią — render 7 sekcji × 4 języki
// notatki_dla_trenera trafiają do .trainer-notes-only (ukryte w self-study)
// ===================================================================
const SECTION_TITLES = {
  wprowadzenie:        { pl: '1. Wprowadzenie',      en: '1. Introduction',            es: '1. Introducción',       uk: '1. Вступ' },
  cele:                { pl: '2. Cele',              en: '2. Objectives',              es: '2. Objetivos',          uk: '2. Цілі' },
  tresc:               { pl: '3. Treść',             en: '3. Content',                 es: '3. Contenido',          uk: '3. Зміст' },
  kluczowe_terminy:    { pl: '4. Kluczowe terminy',  en: '4. Key Terms',               es: '4. Términos clave',     uk: '4. Ключові терміни' },
  sprawdz_siebie:      { pl: '5. Sprawdź siebie',    en: '5. Check Your Knowledge',    es: '5. Comprueba tu conocimiento', uk: '5. Перевір свої знання' },
  link_do_praktyki:    { pl: '6. Link do praktyki',  en: '6. Link to Practice',        es: '6. Enlace con la práctica', uk: "6. Зв'язок з практикою" },
  notatki_dla_trenera: { pl: '7. Notatki dla trenera', en: '7. Notes for the Trainer', es: '7. Notas para el formador', uk: '7. Нотатки для викладача' },
};

const SECTION_ORDER = [
  'wprowadzenie', 'cele', 'tresc', 'kluczowe_terminy',
  'sprawdz_siebie', 'link_do_praktyki', 'notatki_dla_trenera',
];

const MISSING_LANG_TEXTS = {
  es: 'Esta sección aún no está traducida al español.',
  uk: 'Цей розділ ще не перекладено українською.',
  en: 'This section is not yet translated to English.',
  pl: 'Ta sekcja nie jest jeszcze przetłumaczona na język polski.',
};

function buildFullLesson(lesson, languageData, isFirst) {
  // languageData = { pl: {sections: {...}, czas, blok}, en: {...}, ... }
  // — wynik loadLesson(baseDir, lessonId) bez lang argumentu.
  // Nie każdy język musi być obecny (graceful degradation).
  const hiddenAttr = isFirst ? '' : ' hidden';

  const titleSpans = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    return `          <span data-lang="${l}"${hidden}>${escapeHtml(lesson.tytul[l])}</span>`;
  }).join('\n');

  // Meta info — duration + block
  const metaHtml = `        <div class="lesson-meta">
          <span class="lesson-meta__item">
            <span data-lang="es">Duración: ${lesson.czas} min</span>
            <span data-lang="uk" hidden>Тривалість: ${lesson.czas} хв</span>
            <span data-lang="en" hidden>Duration: ${lesson.czas} min</span>
            <span data-lang="pl" hidden>Czas: ${lesson.czas} min</span>
          </span>
        </div>`;

  // 7 sekcji — dla każdej 4 języki
  const sectionsHtml = SECTION_ORDER.map((sectionKey) => {
    const titleMap = SECTION_TITLES[sectionKey];
    const titleSpans = LANGS.map((l) => {
      const hidden = l === 'es' ? '' : ' hidden';
      return `            <span data-lang="${l}"${hidden}>${escapeHtml(titleMap[l])}</span>`;
    }).join('\n');

    // Dla każdego języka: jeśli są sekcje, weź sekcję i renderuj mdToHtml.
    // Jeśli brak → placeholder text.
    const bodyDivs = LANGS.map((l) => {
      const hidden = l === 'es' ? '' : ' hidden';
      const langData = languageData[l];
      const md = langData && langData.sections && langData.sections[sectionKey];
      const html = md ? mdToHtml(md) : `<p>${escapeHtml(MISSING_LANG_TEXTS[l])}</p>`;
      return `          <div data-lang="${l}"${hidden}>${html}</div>`;
    }).join('\n');

    const isTrainer = sectionKey === 'notatki_dla_trenera';
    const sectionClass = isTrainer ? 'lesson-section trainer-notes-only' : 'lesson-section';
    const ariaHidden = isTrainer ? ' aria-hidden="true"' : '';

    return `        <section class="${sectionClass}"${ariaHidden}>
          <h2 class="lesson-section__title">
${titleSpans}
          </h2>
${bodyDivs}
        </section>`;
  }).join('\n\n');

  return `      <article class="lesson" data-lesson-id="${lesson.id}"${hiddenAttr}>
        <h1 class="lesson-title">
${titleSpans}
        </h1>
${metaHtml}

${sectionsHtml}
      </article>`;
}

// ===================================================================
// LESSONS — cała kolekcja <article> dla modułu (32 lekcje)
// ===================================================================
function buildLessons(moduleId, structure) {
  const moduleBase = join(CONTENT_DIR, moduleId, 'lessons');

  const counts = { rendered: 0, placeholder: 0 };
  const articles = [];

  structure.weeks.forEach((week) => {
    week.lessons.forEach((lesson, idx) => {
      const isFirst = week.week === 1 && idx === 0;

      // Spróbuj załadować wszystkie 4 języki; jeśli wszystkie puste → placeholder.
      let languageData = {};
      if (existsSync(join(moduleBase, lesson.id))) {
        try {
          languageData = loadLesson(moduleBase, lesson.id); // zwraca { pl?, en?, es?, uk? }
        } catch (err) {
          languageData = {};
        }
      }

      const hasAnyContent = LANGS.some((l) => languageData[l] && languageData[l].sections);
      if (hasAnyContent) {
        articles.push(buildFullLesson(lesson, languageData, isFirst));
        counts.rendered++;
      } else {
        articles.push(buildPlaceholderLesson(lesson, isFirst));
        counts.placeholder++;
      }
    });
  });

  return { html: articles.join('\n\n'), counts };
}

// ===================================================================
// FINAL QUIZ — placeholder (5 sample pytań) gdy brak quizzes.json
// ===================================================================
function buildFinalQuiz(moduleId, moduleNames) {
  const quizzesPath = join(CONTENT_DIR, moduleId, 'quizzes.json');

  // TODO: gdy quizzes.json istnieje — render z niego (Task 5.5).
  // Na razie wszystkie 3 moduły mają placeholder.
  if (existsSync(quizzesPath)) {
    // Zabezpieczenie na przyszłość — na razie nie osiągalne.
    console.warn(`[build-kurs] ${quizzesPath} istnieje, ale renderer quizów z JSON nie jest jeszcze zaimplementowany (Task 5.5). Używam placeholdera.`);
  }

  const titleSpans = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    const text = { es: 'Examen final', uk: 'Підсумковий іспит', en: 'Final exam', pl: 'Egzamin końcowy' }[l];
    return `            <span data-lang="${l}"${hidden}>${escapeHtml(text)} — ${escapeHtml(moduleNames[l])}</span>`;
  }).join('\n');

  const infoSpans = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    const text = {
      es: '20 preguntas · Aprobado ≥ 70%',
      uk: '20 питань · Прохідний бал ≥ 70%',
      en: '20 questions · Pass ≥ 70%',
      pl: '20 pytań · Zaliczenie ≥ 70%',
    }[l];
    return `            <span data-lang="${l}"${hidden}>${escapeHtml(text)}</span>`;
  }).join('\n');

  // 5 sample pytań — klonują strukturę, ale generyczne. Task 5.5 doda realne.
  const sampleQuestions = [
    {
      q: {
        es: '¿Cuál es el riesgo principal en un aserradero?',
        uk: 'Який головний ризик на лісопилці?',
        en: 'What is the main hazard in a sawmill?',
        pl: 'Jakie jest główne zagrożenie w tartaku?',
      },
      options: [
        {
          text: { es: 'Rechazo (kickback)', uk: 'Віддача (kickback)', en: 'Kickback', pl: 'Odrzut (kickback)' },
          correct: true,
        },
        {
          text: { es: 'Cortes con papel', uk: 'Порізи папером', en: 'Paper cuts', pl: 'Skaleczenia papierem' },
          correct: false,
        },
        {
          text: { es: 'Fatiga visual', uk: 'Втома очей', en: 'Eye strain', pl: 'Zmęczenie oczu' },
          correct: false,
        },
        {
          text: { es: 'Electricidad estática', uk: 'Статична електрика', en: 'Static electricity', pl: 'Elektryczność statyczna' },
          correct: false,
        },
      ],
    },
    {
      q: {
        es: '¿A partir de qué nivel de ruido diario se daña el oído de forma permanente?',
        uk: 'З якого рівня щоденного шуму слух пошкоджується назавжди?',
        en: 'Above what daily noise level is hearing damage permanent?',
        pl: 'Od jakiego poziomu codziennego hałasu słuch jest uszkadzany trwale?',
      },
      options: [
        { text: { es: '60 dB', uk: '60 дБ', en: '60 dB', pl: '60 dB' }, correct: false },
        { text: { es: '70 dB', uk: '70 дБ', en: '70 dB', pl: '70 dB' }, correct: false },
        { text: { es: '85 dB', uk: '85 дБ', en: '85 dB', pl: '85 dB' }, correct: true },
        { text: { es: '120 dB', uk: '120 дБ', en: '120 dB', pl: '120 dB' }, correct: false },
      ],
    },
    {
      q: {
        es: '¿Qué mascarilla es adecuada frente al polvo fino de madera?',
        uk: 'Яка маска підходить проти дрібного деревного пилу?',
        en: 'Which mask is suitable against fine wood dust?',
        pl: 'Która maska nadaje się przeciw drobnemu pyłowi drzewnemu?',
      },
      options: [
        { text: { es: 'Mascarilla quirúrgica', uk: 'Хірургічна маска', en: 'Surgical mask', pl: 'Maska chirurgiczna' }, correct: false },
        { text: { es: 'Bufanda de tela', uk: 'Тканинний шарф', en: 'Fabric scarf', pl: 'Szalik z tkaniny' }, correct: false },
        { text: { es: 'Mascarilla FFP3 ajustada', uk: 'Маска FFP3, щільно припасована', en: 'FFP3 mask sealed', pl: 'Maska FFP3 szczelnie dopasowana' }, correct: true },
        { text: { es: 'Ninguna', uk: 'Жодна', en: 'None', pl: 'Żadna' }, correct: false },
      ],
    },
    {
      q: {
        es: '¿Dónde NO debes colocarte cuando el operador está cortando?',
        uk: 'Де НЕ можна стояти, коли оператор ріже?',
        en: 'Where must you NOT stand while the operator is cutting?',
        pl: 'Gdzie NIE wolno stawać, gdy operator tnie?',
      },
      options: [
        { text: { es: 'A un lado de la máquina', uk: 'Збоку від машини', en: 'Beside the machine', pl: 'Z boku maszyny' }, correct: false },
        { text: { es: 'En la línea de corte', uk: 'У лінії різу', en: 'In the line of cut', pl: 'W linii cięcia' }, correct: true },
        { text: { es: 'En la ruta peatonal', uk: 'На пішохідній доріжці', en: 'On the pedestrian route', pl: 'Na trasie dla pieszych' }, correct: false },
        { text: { es: 'Fuera del taller', uk: 'Поза цехом', en: 'Outside the workshop', pl: 'Poza halą' }, correct: false },
      ],
    },
    {
      q: {
        es: '¿Por qué el curso empieza por seguridad?',
        uk: 'Чому курс починається з безпеки?',
        en: 'Why does the course start with safety?',
        pl: 'Dlaczego kurs zaczyna się od BHP?',
      },
      options: [
        { text: { es: 'Porque lo exige la ley', uk: 'Бо того вимагає закон', en: 'Because the law requires it', pl: 'Bo wymaga tego prawo' }, correct: false },
        {
          text: {
            es: 'Para poder estar en el taller sin ser un peligro antes de tocar una máquina',
            uk: 'Щоб перебувати в цеху, не створюючи небезпеки, перш ніж торкнешся машини',
            en: 'So you can be in the workshop without being a danger before touching a machine',
            pl: 'Aby móc być w hali nie stanowiąc zagrożenia, zanim dotkniesz maszyny',
          },
          correct: true,
        },
        { text: { es: 'Porque las máquinas son complicadas', uk: 'Бо машини складні', en: 'Because machines are complicated', pl: 'Bo maszyny są skomplikowane' }, correct: false },
        { text: { es: 'Porque es más barato', uk: 'Бо це дешевше', en: "Because it's cheaper", pl: 'Bo jest taniej' }, correct: false },
      ],
    },
  ];

  const questionsHtml = sampleQuestions.map((q, qIdx) => {
    const qNum = qIdx + 1;
    const promptSpans = LANGS.map((l) => {
      const hidden = l === 'es' ? '' : ' hidden';
      return `                <span data-lang="${l}"${hidden}><strong>${qNum}.</strong> ${escapeHtml(q.q[l])}</span>`;
    }).join('\n');

    const optionsHtml = q.options.map((opt, optIdx) => {
      const value = ['a', 'b', 'c', 'd'][optIdx];
      const correctAttr = opt.correct ? ' data-correct="true"' : '';
      const optSpans = LANGS.map((l) => {
        const hidden = l === 'es' ? '' : ' hidden';
        return `                  <span data-lang="${l}"${hidden}>${escapeHtml(opt.text[l])}</span>`;
      }).join('\n');
      return `                <li><label><input type="radio" name="q${qNum}" value="${value}"${correctAttr}>
${optSpans}
                </label></li>`;
    }).join('\n');

    return `            <li class="final-quiz-question">
              <p class="final-quiz-question__prompt">
${promptSpans}
              </p>
              <ul class="final-quiz-options">
${optionsHtml}
              </ul>
            </li>`;
  }).join('\n\n');

  const submitSpans = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    const text = { es: 'Enviar', uk: 'Надіслати', en: 'Submit', pl: 'Wyślij' }[l];
    return `            <span data-lang="${l}"${hidden}>${escapeHtml(text)}</span>`;
  }).join('\n');

  const backSpans = LANGS.map((l) => {
    const hidden = l === 'es' ? '' : ' hidden';
    const text = { es: 'Volver al curso', uk: 'Повернутися до курсу', en: 'Back to course', pl: 'Powrót do kursu' }[l];
    return `            <span data-lang="${l}"${hidden}>${escapeHtml(text)}</span>`;
  }).join('\n');

  return `      <section class="final-quiz-view" hidden aria-label="Examen final">
        <header class="final-quiz-header">
          <h1 class="final-quiz-title">
${titleSpans}
          </h1>
          <p class="final-quiz-info">
${infoSpans}
          </p>
        </header>

        <!-- TODO: gdy content/${moduleId}/quizzes.json istnieje — render z niego (Task 5.5).
             Na razie 5 sample pytań — pass ≥ 70% (min 4/5). -->
        <form class="final-quiz-form" novalidate>
          <ol class="final-quiz-questions">
${questionsHtml}
          </ol>
          <div class="final-quiz-actions">
            <button type="submit" class="final-quiz-submit">
${submitSpans}
            </button>
            <button type="button" class="final-quiz-back">
${backSpans}
            </button>
          </div>
        </form>

        <div class="final-quiz-result" hidden aria-live="polite"></div>
      </section>`;
}

// ===================================================================
// CSS inline — łączy 3 pliki styles/ w jeden <style> block
// ===================================================================
function loadInlineCss() {
  const tokens = readFileSync(join(STYLES_DIR, 'design-tokens.css'), 'utf8');
  const cards = readFileSync(join(STYLES_DIR, 'cards.css'), 'utf8');
  const kurs = readFileSync(join(STYLES_DIR, 'kurs.css'), 'utf8');
  return [
    '    /* === design-tokens.css === */',
    tokens,
    '    /* === cards.css === */',
    cards,
    '    /* === kurs.css === */',
    kurs,
  ].join('\n\n');
}

// ===================================================================
// BUILD MODULE — jednego modułu (M1/M2/M3)
// ===================================================================
function buildModule(moduleCfg, config, template, css) {
  const structurePath = join(CONTENT_DIR, moduleCfg.id, 'structure.json');
  if (!existsSync(structurePath)) {
    console.error(`[build-kurs] BŁĄD: ${structurePath} nie istnieje. Pomijam moduł ${moduleCfg.id}.`);
    process.exit(1);
  }
  const structure = JSON.parse(readFileSync(structurePath, 'utf8'));

  const sidebar = buildSidebar(structure, config);
  const { html: lessonsHtml, counts } = buildLessons(moduleCfg.id, structure);
  const finalQuiz = buildFinalQuiz(moduleCfg.id, moduleCfg.name);

  // Breadcrumb startowy — „Módulo N / Semana 1 / Lección 1"
  const moduleNum = moduleCfg.id.replace(/^M/, '');
  const breadcrumb = {
    es: `Módulo ${moduleNum} / Semana 1 / Lección 1`,
    uk: `Модуль ${moduleNum} / Тиждень 1 / Урок 1`,
    en: `Module ${moduleNum} / Week 1 / Lesson 1`,
    pl: `Moduł ${moduleNum} / Tydzień 1 / Lekcja 1`,
  };

  const replacements = {
    MODULE_ID: moduleCfg.id,
    MODULE_NAME_ES: moduleCfg.name.es,
    MODULE_NAME_UK: moduleCfg.name.uk,
    MODULE_NAME_EN: moduleCfg.name.en,
    MODULE_NAME_PL: moduleCfg.name.pl,
    MODULE_ROLE: moduleCfg.role ?? '',
    COURSE_NAME_ES: config.courseName.es,
    COURSE_NAME_UK: config.courseName.uk,
    COURSE_NAME_EN: config.courseName.en,
    COURSE_NAME_PL: config.courseName.pl,
    BREADCRUMB_ES: breadcrumb.es,
    BREADCRUMB_UK: breadcrumb.uk,
    BREADCRUMB_EN: breadcrumb.en,
    BREADCRUMB_PL: breadcrumb.pl,
    SIDEBAR_WEEKS_HTML: sidebar,
    LESSONS_HTML: lessonsHtml,
    FINAL_QUIZ_HTML: finalQuiz,
  };

  let html = template;
  for (const [key, value] of Object.entries(replacements)) {
    html = html.split(`{{${key}}}`).join(value);
  }

  // Inline CSS — wymień 3 <link rel="stylesheet" href="../styles/..."> na jeden <style>
  html = html.replace(
    /  <!-- CSS modułowo:[\s\S]*?<link rel="stylesheet" href="\.\.\/styles\/kurs\.css">/,
    `  <!-- CSS inline — standalone dla protokołu file:// -->\n  <style>\n${css}\n  </style>`
  );

  // Walidacja — żadnych niepodmienionych placeholderów
  const unresolvedMatches = html.match(/\{\{[A-Z_]+\}\}/g);
  if (unresolvedMatches) {
    console.error(`[build-kurs] BŁĄD: niepodmienione placeholdery w ${moduleCfg.id}: ${[...new Set(unresolvedMatches)].join(', ')}`);
    process.exit(1);
  }

  // Walidacja — nie zostały linki do styles/
  if (html.includes('<link rel="stylesheet" href="../styles/')) {
    console.error(`[build-kurs] BŁĄD: inline CSS nie zadziałał w ${moduleCfg.id}. Pozostały <link> do styles/.`);
    process.exit(1);
  }

  return { html, counts };
}

// ===================================================================
// MAIN
// ===================================================================
function main() {
  const config = loadConfig();
  const template = readFileSync(TEMPLATE_PATH, 'utf8');
  const css = loadInlineCss();

  if (!existsSync(DIST)) mkdirSync(DIST, { recursive: true });

  const results = [];
  for (const mod of config.modules) {
    const { html, counts } = buildModule(mod, config, template, css);
    const outPath = join(DIST, `kurs_${mod.id}.html`);
    writeFileSync(outPath, html, 'utf8');

    const sizeKb = (html.length / 1024).toFixed(1);
    const totalLessons = counts.rendered + counts.placeholder;
    console.log(
      `  OK dist/kurs_${mod.id}.html (${sizeKb} KB, ${totalLessons} lekcji: ` +
      `${counts.rendered} z treścią + ${counts.placeholder} placeholder)`
    );
    results.push({ id: mod.id, sizeKb, ...counts });
  }

  console.log(`\nZbudowano ${results.length} modułów do ${DIST}`);
  return results;
}

// Uruchamiaj main tylko gdy plik jest wywołany jako CLI (nie importowany w testach)
const isMain = fileURLToPath(import.meta.url) === resolve(process.argv[1] ?? '');
if (isMain) {
  main();
}

export { buildModule, buildSidebar, buildLessons, buildFinalQuiz, main };
