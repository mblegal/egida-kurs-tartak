# CLAUDE.md — kurs_tartak

Ten katalog to root Podprojektu A (kurs tartakowy). Jest subkatalogiem workspace-u
`C:/Users/mbart/Documents/EGIDA/kurs/`. W fazie C (skill/plugin) będzie przeniesiony
do `EGIDA_academy/courses/tartak/` — stąd dyscyplina „bez hardcoded'ów" w kodzie.

## Dyscyplina Architektury 3 (D14 ze speca)

- **Generator** (w `generator/`) zawsze czyta `course.config.json`. NIE używaj słowa
  „tartak" w kodzie poza tym jednym miejscem.
- **Templates DOCX** (w przyszłym `templates/`) mają placeholdery: `{{COURSE_NAME}}`,
  `{{MODULE_NAME}}`, `{{IMIE_NAZWISKO}}`.
- **Design tokens** w osobnym pliku CSS — żeby łatwo wyciągnąć do `shared/` w fazie C.
- **Ścieżki** zawsze relatywne do `kurs_tartak/` (używaj `import.meta.url` + `path.resolve`).

## Reguły treści

- Polskie znaki diakrytyczne OBOWIĄZKOWE w każdym tekście PL (globalna reguła z
  `~/.claude/CLAUDE.md`). Ukraiński w cyrylicy.
- Znaki specjalne jako Unicode (°C, CO₂, ±), nie encje HTML.
- Dziesiętne: w PL/ES/UK przecinek (0,25%), w EN kropka (0.25%).
- Sekcja `## Kluczowe terminy` w KAŻDYM pliku językowym zawiera wszystkie 4 tłumaczenia
  polskiego terminu (misja integracyjna). Reszta sekcji — tylko język pliku.

## Spec

Źródło prawdy: `../docs/superpowers/specs/2026-04-16-kurs-tartak-design.md`.
Pamięć projektu: `~/.claude/projects/C--Users-mbart-Documents-EGIDA-kurs/memory/MEMORY.md`.
