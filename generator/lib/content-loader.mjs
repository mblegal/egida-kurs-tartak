import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import matter from 'gray-matter';

const SECTION_MAPPING = {
  'Wprowadzenie': 'wprowadzenie',
  'Introducción': 'wprowadzenie',
  'Introduction': 'wprowadzenie',
  'Вступ': 'wprowadzenie',
  'Cele': 'cele',
  'Objetivos': 'cele',
  'Objectives': 'cele',
  'Цілі': 'cele',
  'Treść': 'tresc',
  'Contenido': 'tresc',
  'Content': 'tresc',
  'Зміст': 'tresc',
  'Kluczowe terminy': 'kluczowe_terminy',
  'Términos clave': 'kluczowe_terminy',
  'Key terms': 'kluczowe_terminy',
  'Ключові терміни': 'kluczowe_terminy',
  'Sprawdź siebie': 'sprawdz_siebie',
  'Autoevaluación': 'sprawdz_siebie',
  'Check yourself': 'sprawdz_siebie',
  'Перевір себе': 'sprawdz_siebie',
  'Link do praktyki': 'link_do_praktyki',
  'Vínculo con la práctica': 'link_do_praktyki',
  'Link to practice': 'link_do_praktyki',
  "Зв'язок з практикою": 'link_do_praktyki',
  'Notatki dla trenera': 'notatki_dla_trenera',
  'Notas para el formador': 'notatki_dla_trenera',
  'Trainer notes': 'notatki_dla_trenera',
  'Нотатки для тренера': 'notatki_dla_trenera',
};

function parseSections(markdown) {
  const sections = {};
  const parts = markdown.split(/^## /gm).slice(1);  // first split is empty/preamble
  for (const part of parts) {
    const [heading, ...rest] = part.split('\n');
    const key = SECTION_MAPPING[heading.trim()];
    if (key) {
      sections[key] = rest.join('\n').trim();
    }
  }
  return sections;
}

export function loadLesson(baseDir, lessonId, lang) {
  if (lang) {
    const file = join(baseDir, lessonId, `${lang}.md`);
    const raw = readFileSync(file, 'utf8');
    const { data, content } = matter(raw);
    return {
      ...data,
      lang,
      sections: parseSections(content),
    };
  }
  // No lang → load all 4, skip missing
  const result = {};
  for (const l of ['pl', 'en', 'es', 'uk']) {
    try {
      result[l] = loadLesson(baseDir, lessonId, l);
    } catch (err) {
      // Missing language file — skip (validator catches it later)
    }
  }
  return result;
}
