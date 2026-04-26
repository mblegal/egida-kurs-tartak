"""
Walidator regulaminu kursu B2 #1 dla 4 plików językowych.

Sprawdza:
  - em-dash count = 0
  - KRS / NIP / REGON obecne (1 wystąpienie każdy)
  - EFS+ marker (per język) + nazwa projektu „Budowa fundamentów..."
  - Liczby Kursu: 316, 72, 112, 132, 76, 108, 70%, 75%
  - Frekwencja per modul: 54, 84, 99
  - M1, M2, M3 obecne >= 8 razy każdy
  - Frontmatter YAML klucz `język: <kod>`
  - Brak cyrylicznej waluty `зл`
  - Brak PLN (tu nie potrzebne)
  - Art. 384 KC obecne >= 2 razy (preambuła + pkt II.1)
  - Per-jęz: terminologia (Foundation/Fundación/Фундація)
  - UK: Фонд = 0 (lekcja Part 38)

Reusable szablon dla pojedynczego dokumentu B2 × 4 jęz.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "podprojekt-b" / "B2" / "regulamin-kursu"

LANGS = ["pl", "en", "es", "uk"]

EFS_MARKERS = {
    "pl": "EFS+",
    "en": "ESF+",
    "es": "FSE+",
    "uk": "ЄСФ",
}

LANG_TERMS = {
    "pl": [("Fundacja", 5), ("Przedsiębiorca", 5), ("Kursant", 10)],
    "en": [("Foundation", 10), ("Entrepreneur", 10), ("Participant", 10)],
    "es": [("Fundación", 10), ("Empresario", 10), ("Cursista", 10)],
    "uk": [("Фундаці", 15), ("Підприємц", 5), ("Курсант", 10)],
}


def check_file(lang: str) -> tuple[bool, list[str]]:
    path = ROOT / f"{lang}.md"
    errors: list[str] = []

    if not path.exists():
        return False, [f"file missing: {path}"]

    data = path.read_bytes()
    em_dash = data.count(b"\xe2\x80\x94")
    txt = data.decode("utf-8")

    # em-dash absolutny zakaz
    if em_dash != 0:
        errors.append(f"em_dash count = {em_dash} (oczekiwane 0)")

    # KRS / NIP / REGON
    if txt.count("0000957190") < 1:
        errors.append("brak KRS 0000957190")
    if txt.count("7543348716") < 1:
        errors.append("brak NIP 7543348716")
    if txt.count("521360040") < 1:
        errors.append("brak REGON 521360040")

    # EFS+ marker + nazwa projektu
    marker = EFS_MARKERS[lang]
    if marker not in txt:
        errors.append(f"brak markera EFS+ dla {lang} ({marker})")
    if "Budowa fundamentów" not in txt:
        errors.append("brak nazwy projektu „Budowa fundamentów..." )

    # Liczby Kursu
    if txt.count("316") < 1:
        errors.append("brak 316 (łączny wymiar)")
    if txt.count("76") < 3:
        errors.append(f"za mało wystąpień '76' ({txt.count('76')}, oczekiwane >=3)")
    if txt.count("108") < 3:
        errors.append(f"za mało wystąpień '108' ({txt.count('108')}, oczekiwane >=3)")
    if "70%" not in txt:
        errors.append("brak '70%'")
    if "75%" not in txt:
        errors.append("brak '75%'")

    # Frekwencja per modul (54 / 84 / 99)
    if "54" not in txt:
        errors.append("brak '54' (frekwencja M1)")
    if "84" not in txt:
        errors.append("brak '84' (frekwencja M2)")
    if "99" not in txt:
        errors.append("brak '99' (frekwencja M3)")

    # M1 / M2 / M3
    for m in ("M1", "M2", "M3"):
        c = txt.count(m)
        if c < 8:
            errors.append(f"za mało {m} ({c}, oczekiwane >=8)")

    # YAML lang
    if f"język: {lang}" not in txt:
        errors.append(f"brak frontmatter 'język: {lang}'")

    # Brak cyrylicznej waluty
    cyr_zl = len(re.findall(r"\d+\s*зл\b", txt))
    if cyr_zl != 0:
        errors.append(f"cyryliczna waluta 'зл' = {cyr_zl} (oczekiwane 0)")

    # Brak PLN (regulamin nie ma kwot)
    if txt.count("PLN") > 0:
        errors.append(f"PLN obecny {txt.count('PLN')}× (nieoczekiwane)")

    # Art. 384 KC
    if txt.count("384") < 2:
        errors.append(f"art. 384 KC za mało wystąpień ({txt.count('384')}, oczekiwane >=2)")

    # Terminologia per jęz
    for term, min_count in LANG_TERMS[lang]:
        c = txt.count(term)
        if c < min_count:
            errors.append(f"za mało wystąpień '{term}' ({c}, oczekiwane >={min_count})")

    # UK: Фонд = 0 (lekcja Part 38)
    if lang == "uk":
        fond_count = txt.count("Фонд")
        if fond_count > 0:
            errors.append(f"BŁĄD UK terminologii: 'Фонд' = {fond_count} (oczekiwane 0, używać 'Фундація')")

    # Liczba słów (sanity)
    words = len(txt.split())
    if words < 3500:
        errors.append(f"za mało słów ({words}, oczekiwane >=3500)")

    return len(errors) == 0, errors


def main() -> int:
    print("=" * 72)
    print("Walidator B2 #1 regulamin kursu — 4 pliki językowe")
    print("=" * 72)

    all_ok = True
    summary: list[tuple[str, int]] = []

    for lang in LANGS:
        path = ROOT / f"{lang}.md"
        ok, errors = check_file(lang)
        words = len(path.read_text(encoding="utf-8").split()) if path.exists() else 0
        summary.append((lang, words))

        status = "[OK]" if ok else "[FAIL]"
        print(f"\n{status} {lang}.md ({words} słów)")
        if not ok:
            all_ok = False
            for err in errors:
                print(f"   - {err}")

    print("\n" + "=" * 72)
    print("Podsumowanie:")
    for lang, words in summary:
        print(f"  {lang}: {words} słów")
    print("=" * 72)

    if all_ok:
        print("\n*** ALL CHECKS PASSED — 4/4 plików zwalidowanych ***")
        return 0
    else:
        print("\n*** WALIDACJA NIEUDANA — popraw błędy powyżej ***")
        return 1


if __name__ == "__main__":
    sys.exit(main())
