#!/usr/bin/env python3
"""Walidator wygenerowanych zaświadczeń ukończenia modułów (Part 37 cz.1, 12 plików)."""
import sys
import re
import os
from pathlib import Path

if sys.platform == "win32":
    os.environ["PYTHONUTF8"] = "1"
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent.parent
B1 = ROOT / "podprojekt-b" / "B1"

LANGS = ["pl", "en", "es", "uk"]
MODULES = ["m1", "m2", "m3"]

EFS_MARKERS = {
    "pl": "Budowa fundamentów pod lokalną politykę migracyjną i integracyjną",
    "en": "Building foundations",
    "es": "Construcción de fundamentos",
    "uk": "Розбудова",
}

REGISTRY_KEYS = ["0000957190", "7543348716", "521360040"]
PLACEHOLDERS = ["{{MODUL}}", "{{ROLA}}", "{{TYGODNIE}}", "{{GODZINY}}", "{{GODZINY_DECL}}", "{{KOMPETENCJE_OPIS}}"]

# Per-module hours (M1=72, M2=112, M3=132) musza wystapic w wygenerowanym pliku
MODULE_HOURS = {"m1": "72", "m2": "112", "m3": "132"}


def check(path: Path, lang: str, module: str) -> list[str]:
    raw = path.read_bytes()
    txt = raw.decode("utf-8")
    problems = []

    em = raw.count(b"\xe2\x80\x94")
    if em > 0:
        problems.append(f"em-dash={em}")

    leftover = [p for p in PLACEHOLDERS if p in txt]
    if leftover:
        problems.append(f"placeholdery niepodmienione: {leftover}")

    if EFS_MARKERS[lang] not in txt:
        problems.append(f"brak markera EFS+ ({EFS_MARKERS[lang]!r})")

    for k in REGISTRY_KEYS:
        if k not in txt:
            problems.append(f"brak {k}")

    if not txt.startswith("---"):
        problems.append("brak YAML frontmatter")

    # Modul-specific: liczba godzin musi wystapic
    hours = MODULE_HOURS[module]
    if hours not in txt:
        problems.append(f"brak liczby godzin {hours}")

    # Modul-specific: kod modulu w gornej regularnej wartosci
    module_upper = module.upper()
    if module_upper not in txt:
        problems.append(f"brak kodu modulu {module_upper}")

    # UK: cyrylicowa zl jako waluta = blad
    if lang == "uk":
        bad_zl = len(re.findall(r"\d+\s*зл\b", txt))
        if bad_zl > 0:
            problems.append(f"cyryliczna zl jako waluta: {bad_zl}")

    return problems


def main():
    failures = []
    total = 0
    word_totals = {}
    for lang in LANGS:
        for module in MODULES:
            p = B1 / f"zaswiadczenie-ukonczenia-modulu-{module}" / f"{lang}.md"
            total += 1
            if not p.exists():
                print(f"[MISSING] {p}")
                failures.append((str(p), ["plik nie istnieje"]))
                continue
            probs = check(p, lang, module)
            words = len(re.findall(r"\w+", p.read_text(encoding="utf-8")))
            word_totals.setdefault(lang, []).append(words)
            status = "OK" if not probs else "FAIL"
            print(f"[{status}] {lang}/{module}: words={words}")
            if probs:
                for pr in probs:
                    print(f"        -> {pr}")
                failures.append((f"{lang}/{module}", probs))

    print("\n=== SUMMARY ===")
    for lang, ws in word_totals.items():
        print(f"  {lang}: words {ws} (avg {sum(ws)//len(ws)})")
    print(f"  total files: {total}, failures: {len(failures)}")
    if failures:
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
