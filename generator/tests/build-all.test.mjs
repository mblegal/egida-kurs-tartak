// build-all.test.mjs — E2E smoke test Task 3.10
// Uruchamia `npm run build:all`, sprawdza że `dist/` zawiera 6 oczekiwanych plików HTML.

import { describe, it, expect, beforeAll } from 'vitest';
import { execSync } from 'node:child_process';
import { existsSync, statSync, readFileSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');
const DIST = join(PROJECT_ROOT, 'dist');

const EXPECTED_FILES = [
  'kurs_M1.html',
  'kurs_M2.html',
  'kurs_M3.html',
  'prezentacja_M1.html',
  'prezentacja_M2.html',
  'prezentacja_M3.html',
];

describe('build:all — E2E smoke test (Task 3.10)', () => {
  beforeAll(() => {
    execSync('npm run build:all', { cwd: PROJECT_ROOT, stdio: 'pipe' });
  });

  it('exit 0 dla npm run build:all', () => {
    // Jeśli beforeAll nie rzucił, build:all exited 0 — beforeAll rzuca dla non-zero
    expect(true).toBe(true);
  });

  it('dist/ zawiera 6 oczekiwanych plików HTML', () => {
    for (const file of EXPECTED_FILES) {
      expect(existsSync(join(DIST, file))).toBe(true);
    }
  });

  it('każdy z 6 plików ma > 50 KB (faktyczny content, nie stub)', () => {
    for (const file of EXPECTED_FILES) {
      const size = statSync(join(DIST, file)).size;
      expect(size).toBeGreaterThan(50_000);
    }
  });

  it('kurs_M1 ma sidebar + progress bar + final-quiz-open', () => {
    const html = readFileSync(join(DIST, 'kurs_M1.html'), 'utf8');
    expect(html).toContain('class="sidebar"');
    expect(html).toContain('class="progress__fill"');
    expect(html).toContain('class="final-quiz-open"');
  });

  it('prezentacja_M1 ma Reveal.js + plugin notes + 1920x1080', () => {
    const html = readFileSync(join(DIST, 'prezentacja_M1.html'), 'utf8');
    expect(html).toContain('<div class="reveal">');
    expect(html).toContain('plugins: [RevealNotes]');
    expect(html).toContain('width: 1920');
    expect(html).toContain('height: 1080');
  });

  it('kurs i prezentacja NIE zawierają placeholderów {{...}}', () => {
    for (const file of EXPECTED_FILES) {
      const html = readFileSync(join(DIST, file), 'utf8');
      expect(html).not.toMatch(/\{\{[A-Z_]+\}\}/);
    }
  });
});
