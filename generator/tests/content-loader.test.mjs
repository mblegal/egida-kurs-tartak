import { describe, it, expect } from 'vitest';
import { loadLesson } from '../lib/content-loader.mjs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const FIXTURE_DIR = resolve(__dirname, 'fixtures');

describe('loadLesson', () => {
  it('parses frontmatter', () => {
    const lesson = loadLesson(FIXTURE_DIR, 'm1-w1-l1', 'pl');
    expect(lesson.id).toBe('m1-w1-l1');
    expect(lesson.blok).toBe('bezpieczenstwo');
    expect(lesson.czas).toBe(120);
  });

  it('extracts all 8 sections', () => {
    const lesson = loadLesson(FIXTURE_DIR, 'm1-w1-l1', 'pl');
    expect(lesson.sections).toHaveProperty('wprowadzenie');
    expect(lesson.sections).toHaveProperty('cele');
    expect(lesson.sections).toHaveProperty('tresc');
    expect(lesson.sections).toHaveProperty('kluczowe_terminy');
    expect(lesson.sections).toHaveProperty('sprawdz_siebie');
    expect(lesson.sections).toHaveProperty('link_do_praktyki');
    expect(lesson.sections).toHaveProperty('notatki_dla_trenera');
  });

  it('loads all 4 language versions', () => {
    const versions = loadLesson(FIXTURE_DIR, 'm1-w1-l1');
    expect(Object.keys(versions)).toEqual(expect.arrayContaining(['pl', 'en', 'es', 'uk']));
  });
});
