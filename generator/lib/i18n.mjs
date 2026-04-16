export function pickLang(langMap, preferred, fallback = 'pl') {
  if (langMap[preferred]) return langMap[preferred];
  if (langMap[fallback]) return langMap[fallback];
  return '';
}

export function renderMultilingual(langMap) {
  return Object.entries(langMap)
    .map(([lang, html]) => `<div class="lang-${lang}" data-lang="${lang}">${html}</div>`)
    .join('\n');
}
