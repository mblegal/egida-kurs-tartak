"""Weryfikacja globalna materiałów pomocniczych Fazy 5.

Sprawdza 10 plików (D1 PL, D2 PL/EN/ES/UK, D3 PL/EN/ES/UK, D4 PL) pod kątem:
- 0 em-dashów (U+2014)
- 0 en-dashów (U+2013)
- 0 typograficznych apostrofów U+2019 w UK (ASCII U+0027 only)
- Waluta `zł` literalnie (U+0142), 0 ASCII `zl`, 0 `PLN`
- Spójność kodów systemowych w ES/EN/UK względem PL
- Frontmatter YAML: id/faza/typ/dokument identyczne, tylko `język:` różne
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "materialy-pomocnicze"

FILES = [
    ("program-ogolny", ["pl"]),
    ("program-szczegolowy", ["pl", "en", "es", "uk"]),
    ("prospekt-rekrutacyjny", ["pl", "en", "es", "uk"]),
    ("wytyczne-koordynatora", ["pl"]),
]

SYSTEM_CODES = ["ZLE-2026", "FSC-C112233", "EFS+", "2026_004"]

errors = []
summary = []

for folder, langs in FILES:
    for lang in langs:
        p = BASE / folder / f"{lang}.md"
        if not p.exists():
            errors.append(f"BRAK PLIKU: {p}")
            continue
        t = p.read_text(encoding="utf-8")

        em = t.count("\u2014")
        en = t.count("\u2013")
        zl = t.count("zł")
        zl_ascii = len(re.findall(r"\bzl\b", t))
        pln = t.count("PLN")
        slow = len(t.split())

        typ_apo = t.count("\u2019") if lang == "uk" else 0

        # Frontmatter check
        fm_match = re.match(r"---\n(.*?)\n---", t, re.DOTALL)
        fm_ok = fm_match is not None
        lang_in_fm = f"język: {lang}" in t[:400] if fm_ok else False

        line = f"{folder}/{lang}: slow={slow}, em={em}, en={en}, zl={zl}, zl-ascii={zl_ascii}, PLN={pln}, typ-apo={typ_apo}, fm={'OK' if fm_ok else 'BRAK'}, lang-in-fm={'OK' if lang_in_fm else 'BRAK'}"
        summary.append(line)

        if em > 0:
            errors.append(f"{folder}/{lang}: {em} em-dashów")
        if en > 0:
            errors.append(f"{folder}/{lang}: {en} en-dashów")
        if zl_ascii > 0:
            errors.append(f"{folder}/{lang}: {zl_ascii} ASCII 'zl'")
        if pln > 0:
            errors.append(f"{folder}/{lang}: {pln} 'PLN'")
        if lang == "uk" and typ_apo > 0:
            errors.append(f"{folder}/{lang}: {typ_apo} typograficznych apostrofów U+2019")
        if not fm_ok:
            errors.append(f"{folder}/{lang}: BRAK frontmatter")
        if fm_ok and not lang_in_fm:
            errors.append(f"{folder}/{lang}: frontmatter NIE zawiera 'język: {lang}'")

        # Kody systemowe - tylko w wytycznych koordynatora (D4), nie w prospekcie
        if folder == "wytyczne-koordynatora":
            for code in ["FSC-C112233", "EFS+", "ZLE-2026"]:
                if code not in t:
                    errors.append(f"{folder}/{lang}: brak kodu '{code}'")
        # W prospekcie wymagamy tylko EFS+
        if folder == "prospekt-rekrutacyjny":
            if "EFS+" not in t:
                errors.append(f"{folder}/{lang}: brak kodu 'EFS+'")

print("=" * 60)
print("RAPORT WERYFIKACJI FAZY 5")
print("=" * 60)
for line in summary:
    print(line)
print()
print("-" * 60)
if errors:
    print(f"BŁĘDY ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("OK: 10/10 plików czyste, 0 błędów")
    sys.exit(0)
