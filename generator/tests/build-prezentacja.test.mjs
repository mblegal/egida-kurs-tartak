// build-prezentacja.test.mjs — E2E test dla generatora Reveal.js
// Uruchamia build-prezentacja.mjs jako child process, potem waliduje wygenerowane HTML.

import { describe, it, expect, beforeAll } from 'vitest';
import { execSync } from 'node:child_process';
import { readFileSync, existsSync, statSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  buildSlides,
  buildLessonStack,
  buildSlideTitle,
  buildSlideEnd,
  loadInlineCss,
} from '../build-prezentacja.mjs';
import { loadConfig } from '../lib/config.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');
const DIST = join(PROJECT_ROOT, 'dist');
const BUILD_SCRIPT = join(PROJECT_ROOT, 'generator/build-prezentacja.mjs');

describe('build-prezentacja.mjs E2E', () => {
  let m1Html, m2Html, m3Html;

  beforeAll(() => {
    // Uruchom build raz (shared setup)
    execSync(`node "${BUILD_SCRIPT}"`, { cwd: PROJECT_ROOT, stdio: 'pipe' });
    m1Html = readFileSync(join(DIST, 'prezentacja_M1.html'), 'utf8');
    m2Html = readFileSync(join(DIST, 'prezentacja_M2.html'), 'utf8');
    m3Html = readFileSync(join(DIST, 'prezentacja_M3.html'), 'utf8');
  });

  it('generuje 3 pliki dist/prezentacja_M{1,2,3}.html', () => {
    expect(existsSync(join(DIST, 'prezentacja_M1.html'))).toBe(true);
    expect(existsSync(join(DIST, 'prezentacja_M2.html'))).toBe(true);
    expect(existsSync(join(DIST, 'prezentacja_M3.html'))).toBe(true);
  });

  it('każdy plik ma > 50 KB', () => {
    expect(statSync(join(DIST, 'prezentacja_M1.html')).size).toBeGreaterThan(50_000);
    expect(statSync(join(DIST, 'prezentacja_M2.html')).size).toBeGreaterThan(50_000);
    expect(statSync(join(DIST, 'prezentacja_M3.html')).size).toBeGreaterThan(50_000);
  });

  it('nie zawiera nierozwiązanych placeholderów {{...}}', () => {
    expect(m1Html).not.toMatch(/\{\{[A-Z_]+\}\}/);
    expect(m2Html).not.toMatch(/\{\{[A-Z_]+\}\}/);
    expect(m3Html).not.toMatch(/\{\{[A-Z_]+\}\}/);
  });

  it('CSS został inline\'owany (brak <link> do ../styles/)', () => {
    expect(m1Html).not.toContain('href="../styles/design-tokens.css"');
    expect(m1Html).not.toContain('href="../styles/cards.css"');
    expect(m1Html).not.toContain('href="../styles/prezentacja.css"');
    expect(m1Html).toMatch(/<style>[\s\S]+?--accent-primary/);
  });

  it('zachowuje Reveal.js CDN linki (z cdn.jsdelivr.net)', () => {
    expect(m1Html).toContain('cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/reveal.css');
    expect(m1Html).toContain('cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/reveal.js');
    expect(m1Html).toContain('cdn.jsdelivr.net/npm/reveal.js@5.2.1/plugin/notes/notes.js');
  });

  it('ma strukturę Reveal.js <div class="reveal"><div class="slides">', () => {
    expect(m1Html).toContain('<div class="reveal">');
    expect(m1Html).toContain('<div class="slides">');
  });

  it('ma Reveal.initialize z plugin RevealNotes', () => {
    expect(m1Html).toMatch(/Reveal\.initialize\s*\(/);
    expect(m1Html).toContain('plugins: [RevealNotes]');
    expect(m1Html).toContain('width: 1920');
    expect(m1Html).toContain('height: 1080');
  });

  it('ma slajdy ramowe: slide-title + slide-toc + slide-end', () => {
    expect(m1Html).toContain('class="slide-title"');
    expect(m1Html).toContain('class="slide-toc"');
    expect(m1Html).toContain('class="slide-end"');
  });

  it('ma 32 lekcje placeholder (każda z data-lesson-id pasującym do modułu)', () => {
    const m1Ids = m1Html.match(/data-lesson-id="m1-w[1-4]-l[1-8]"/g) || [];
    const m2Ids = m2Html.match(/data-lesson-id="m2-w[1-4]-l[1-8]"/g) || [];
    const m3Ids = m3Html.match(/data-lesson-id="m3-w[1-4]-l[1-8]"/g) || [];
    expect(m1Ids.length).toBe(32);
    expect(m2Ids.length).toBe(32);
    expect(m3Ids.length).toBe(32);
  });

  it('każda lekcja ma <aside class="notes"> (speaker notes)', () => {
    const m1Notes = m1Html.match(/<aside class="notes">/g) || [];
    expect(m1Notes.length).toBe(32);
  });

  it('zawiera wszystkie 4 języki w data-lang (każdy co najmniej 50×)', () => {
    for (const lang of ['es', 'uk', 'en', 'pl']) {
      const re = new RegExp(`data-lang="${lang}"`, 'g');
      const matches = m1Html.match(re) || [];
      expect(matches.length).toBeGreaterThan(50);
    }
  });

  it('ES jest widoczny domyślnie (bez hidden), inne języki hidden', () => {
    // ES spans i divs — bez hidden
    expect(m1Html).toMatch(/data-lang="es">/);
    // UK/EN/PL z hidden
    expect(m1Html).toMatch(/data-lang="uk" hidden>/);
    expect(m1Html).toMatch(/data-lang="en" hidden>/);
    expect(m1Html).toMatch(/data-lang="pl" hidden>/);
  });

  it('M1 ma nazwę modułu "Pracownik pomocniczy" (PL) z diakrytykami', () => {
    expect(m1Html).toContain('Moduł 1: Pracownik pomocniczy');
    expect(m1Html).toContain('Módulo 1: Trabajador auxiliar');
  });

  it('M3 ma ukraińską cyrylicę (Модуль, Самостійний)', () => {
    expect(m3Html).toContain('Модуль 3');
    expect(m3Html).toContain('Самостійний');
  });

  it('placeholder lekcji ma tag "Lección por preparar" + tytuł z structure.json', () => {
    // M1 po Bloku 3 T4 ma 32/32 lekcji z treścią (0 placeholder), więc placeholder sprawdzamy na M2
    expect(m2Html).toContain('class="placeholder-tag"');
    expect(m2Html).toContain('Lección por preparar');
    expect(m2Html).toContain('Lekcja w przygotowaniu'); // PL w ukrytym spanie
    // Tytuł pierwszej lekcji M1 (z structure.json) — nadal obecny, już nie w placeholderze bo lekcja ma treść
    expect(m1Html).toContain('Por qué un aserradero es diferente');
    expect(m1Html).toContain('Dlaczego tartak jest inny');
  });

  it('lang-switcher jest obecny z 4 przyciskami', () => {
    expect(m1Html).toContain('lang-switcher--presentation');
    expect(m1Html).toMatch(/data-lang-target="es"/);
    expect(m1Html).toMatch(/data-lang-target="uk"/);
    expect(m1Html).toMatch(/data-lang-target="en"/);
    expect(m1Html).toMatch(/data-lang-target="pl"/);
  });
});

describe('build-prezentacja — unit tests', () => {
  it('loadInlineCss() zwraca skonkatenowany CSS (design-tokens + cards + prezentacja)', () => {
    const css = loadInlineCss();
    expect(css).toContain('--accent-primary'); // z design-tokens
    expect(css).toContain('.info-card'); // z cards
    expect(css).toContain('.reveal'); // z prezentacja
    expect(css.length).toBeGreaterThan(3000);
  });

  it('buildSlideTitle() produkuje <section class="slide-title"> z 4 językami', () => {
    const config = loadConfig();
    const html = buildSlideTitle(config.modules[0], config);
    expect(html).toContain('class="slide-title"');
    expect(html).toContain('data-lang="es"');
    expect(html).toContain('data-lang="pl"');
    expect(html).toContain('Moduł 1: Pracownik pomocniczy');
    expect(html).toContain('Módulo 1: Trabajador auxiliar');
  });

  it('buildSlideEnd() zawiera "¡Gracias!" i nazwę kursu', () => {
    const config = loadConfig();
    const html = buildSlideEnd(config);
    expect(html).toContain('class="slide-end"');
    expect(html).toContain('¡Gracias!');
    expect(html).toContain('Dziękujemy!');
    expect(html).toContain('Fundación EGIDA');
  });

  it('buildLessonStack() w trybie placeholder ma slide-placeholder + <aside.notes>', () => {
    const week = {
      week: 1,
      blockId: 'bezpieczenstwo',
      lessons: [],
    };
    const lesson = {
      id: 'm1-w1-l1',
      czas: 120,
      tytul: { es: 'Test ES', uk: 'Тест UK', en: 'Test EN', pl: 'Test PL' },
      opis: { es: 'Opis ES', uk: 'Опис UK', en: 'Desc EN', pl: 'Opis PL' },
    };
    week.lessons = [lesson];

    const html = buildLessonStack('M1', week, lesson, null); // null = placeholder
    expect(html).toContain('slide-placeholder');
    expect(html).toContain('data-lesson-id="m1-w1-l1"');
    expect(html).toContain('<aside class="notes">');
    expect(html).toContain('Lekcja w przygotowaniu'); // PL placeholder tag
  });
});
