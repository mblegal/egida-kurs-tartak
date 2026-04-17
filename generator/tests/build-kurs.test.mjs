import { describe, it, expect, beforeAll } from 'vitest';
import { execSync } from 'node:child_process';
import { readFileSync, existsSync, statSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  buildSidebar, buildLessons, buildFinalQuiz,
} from '../build-kurs.mjs';
import { loadConfig } from '../lib/config.mjs';
import { loadLesson } from '../lib/content-loader.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');
const DIST = resolve(PROJECT_ROOT, 'dist');
const BUILD_SCRIPT = resolve(__dirname, '../build-kurs.mjs');
const CONTENT_DIR = resolve(PROJECT_ROOT, 'content');
const FIXTURE_DIR = resolve(__dirname, 'fixtures');

describe('build-kurs.mjs — E2E', () => {
  let config;

  beforeAll(() => {
    // Uruchom generator jako child process — pełny E2E.
    execSync(`node "${BUILD_SCRIPT}"`, { cwd: PROJECT_ROOT, stdio: 'pipe' });
    config = loadConfig();
  });

  it('produkuje dist/kurs_M1.html, M2.html, M3.html', () => {
    for (const id of ['M1', 'M2', 'M3']) {
      const path = join(DIST, `kurs_${id}.html`);
      expect(existsSync(path), `${path} nie istnieje`).toBe(true);
      const size = statSync(path).size;
      expect(size, `${id} ma tylko ${size} B — za mało (oczekiwane >100 KB)`).toBeGreaterThan(100_000);
    }
  });

  it('dist/kurs_M1.html nie zawiera niepodmienionych {{...}}', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    const unresolved = html.match(/\{\{[A-Z_]+\}\}/g);
    expect(unresolved, `Niepodmienione placeholdery: ${unresolved?.join(', ')}`).toBeNull();
  });

  it('dist/kurs_M1.html ma CSS inline (brak linków do ../styles/)', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    expect(html).not.toMatch(/<link rel="stylesheet" href="\.\.\/styles\//);
    expect(html).toMatch(/<style>[\s\S]+\.sidebar/); // styles kurs.css zostały wklejone
  });

  it('dist/kurs_M1.html zawiera wszystkie 4 języki co najmniej 10×', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    for (const lang of ['es', 'uk', 'en', 'pl']) {
      const count = (html.match(new RegExp(`data-lang="${lang}"`, 'g')) || []).length;
      expect(count, `${lang} występuje tylko ${count}×, oczekiwano ≥ 10`).toBeGreaterThanOrEqual(10);
    }
  });

  it('dist/kurs_M1.html zawiera 32 unikalne data-lesson-id lekcji', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    const matches = html.match(/data-lesson-id="(m1-w\d-l\d)"/g) || [];
    const unique = new Set(matches.map((m) => m.match(/"(.+)"/)[1]));
    expect(unique.size, 'Oczekiwano 32 unikalnych data-lesson-id').toBe(32);
    expect(unique.has('m1-w1-l1')).toBe(true);
    expect(unique.has('m1-w4-l8')).toBe(true);
  });

  it('dist/kurs_M1.html: placeholder + rendered = 32 lekcji (niezmiennik modułu)', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    // Każda lekcja placeholderowa ma 2 wystąpienia "lesson--placeholder"
    // (class na <article> i class na div-body). Liczba placeholderów = matches/2.
    const placeholderMatches = html.match(/lesson--placeholder/g) || [];
    const placeholderCount = Math.floor(placeholderMatches.length / 2);
    // Liczba unikalnych lesson-id (wszystkie 32) MUSI być stała.
    const lessonIds = html.match(/data-lesson-id="(m1-w\d-l\d)"/g) || [];
    const unique = new Set(lessonIds.map((m) => m.match(/"(.+)"/)[1]));
    expect(unique.size, 'Moduł M1 zawsze ma 32 lekcje').toBe(32);
    // Rendered = wszystkie − placeholder
    const renderedCount = 32 - placeholderCount;
    expect(renderedCount, `Rendered: ${renderedCount}, Placeholder: ${placeholderCount}, Suma: 32`).toBeGreaterThan(0);
  });

  it('dist/kurs_M1.html ma klucze localStorage dla M1, nie dla M2', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    expect(html).toContain("'egida_tartak_M1_progress'");
    expect(html).not.toContain("'egida_tartak_M2_progress'");
  });

  it('dist/kurs_M2.html ma klucze localStorage dla M2', () => {
    const html = readFileSync(join(DIST, 'kurs_M2.html'), 'utf8');
    expect(html).toContain("'egida_tartak_M2_progress'");
    expect(html).not.toContain("'egida_tartak_M1_progress'");
  });

  it('dist/kurs_M1.html ma Google Fonts link (CDN pozostał)', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    expect(html).toMatch(/fonts\.googleapis\.com/);
  });

  it('dist/kurs_M1.html zawiera breadcrumb z numerem modułu', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    expect(html).toContain('Módulo 1 / Semana 1 / Lección 1');
  });

  it('dist/kurs_M3.html zawiera breadcrumb z „Módulo 3"', () => {
    const html = readFileSync(join(DIST, 'kurs_M3.html'), 'utf8');
    expect(html).toContain('Módulo 3');
    expect(html).toContain('Moduł 3');
    expect(html).toContain('Модуль 3');
  });

  it('dist/kurs_M1.html ma tytuł ES z nazwą modułu', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    expect(html).toMatch(/<title>.*Módulo 1: Trabajador auxiliar<\/title>/);
  });
});

describe('buildSidebar — unit', () => {
  it('produkuje HTML z 4 tygodniami × 8 lekcji = 32 pozycji', () => {
    const config = loadConfig();
    const structure = JSON.parse(readFileSync(join(CONTENT_DIR, 'M1', 'structure.json'), 'utf8'));
    const html = buildSidebar(structure, config);
    const lessonItems = html.match(/<li class="lesson-item/g) || [];
    expect(lessonItems.length).toBe(32);
    expect(html).toContain('lesson-item--active'); // pierwsza lekcja aktywna
    expect(html).toContain('data-lesson-id="m1-w1-l1"');
    expect(html).toContain('aria-current="page"');
  });

  it('tytuły tygodni w 4 językach (Semana 1 / Тиждень 1 / Week 1 / Tydzień 1)', () => {
    const config = loadConfig();
    const structure = JSON.parse(readFileSync(join(CONTENT_DIR, 'M1', 'structure.json'), 'utf8'));
    const html = buildSidebar(structure, config);
    expect(html).toContain('Semana 1');
    expect(html).toContain('Тиждень 1');
    expect(html).toContain('Week 1');
    expect(html).toContain('Tydzień 1');
  });
});

describe('buildLessons — placeholder fallback', () => {
  it('gdy brak .md dla lekcji → lesson--placeholder z polskimi diakrytykami', () => {
    // Używamy M2, który nadal jest 0/32 placeholderów (M1 ma już realną lekcję m1-w1-l1 od Part 4)
    const structure = JSON.parse(readFileSync(join(CONTENT_DIR, 'M2', 'structure.json'), 'utf8'));
    const { html, counts } = buildLessons('M2', structure);
    expect(counts.rendered).toBe(0);
    expect(counts.placeholder).toBe(32);
    expect(html).toContain('lesson--placeholder');
    // Polskie diakrytyki w tekście placeholdera
    expect(html).toContain('Ta lekcja nie ma jeszcze treści');
  });

  it('M1 po Part 4: co najmniej 1 realna lekcja + reszta jako placeholder, suma 32', () => {
    const structure = JSON.parse(readFileSync(join(CONTENT_DIR, 'M1', 'structure.json'), 'utf8'));
    const { counts } = buildLessons('M1', structure);
    expect(counts.rendered).toBeGreaterThanOrEqual(1);
    expect(counts.placeholder).toBeGreaterThanOrEqual(1);
    expect(counts.rendered + counts.placeholder).toBe(32);
  });
});

describe('buildFinalQuiz — placeholder', () => {
  it('produkuje nagłówek + 5 pytań × 4 języki', () => {
    const quiz = buildFinalQuiz('M1', {
      pl: 'Moduł 1: Pracownik pomocniczy',
      en: 'Module 1: Assistant Worker',
      es: 'Módulo 1: Trabajador auxiliar',
      uk: 'Модуль 1: Помічник робітника',
    });
    expect(quiz).toContain('final-quiz-view');
    expect(quiz).toContain('Examen final');
    expect(quiz).toContain('Egzamin końcowy');
    expect(quiz).toContain('Підсумковий іспит');
    expect(quiz).toContain('Final exam');
    // 5 pytań
    const questions = quiz.match(/final-quiz-question"/g) || [];
    expect(questions.length).toBe(5);
    // Każde pytanie ma 4 opcje → łącznie 20 radio
    const radios = quiz.match(/type="radio"/g) || [];
    expect(radios.length).toBe(20);
    // Każde pytanie ma dokładnie 1 odpowiedź poprawną
    const corrects = quiz.match(/data-correct="true"/g) || [];
    expect(corrects.length).toBe(5);
  });
});
