#!/usr/bin/env python3
"""Walidator szablonów zaswiadczenia-ukonczenia-modulu (Part 37 cz.1)."""
import sys
import re
import os
from pathlib import Path

if sys.platform == "win32":
    os.environ["PYTHONUTF8"] = "1"
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent.parent
TPL_DIR = ROOT / "podprojekt-b" / "B1" / "_szablony" / "zaswiadczenie-ukonczenia-modulu"

REQUIRED_PLACEHOLDERS = [
    "{{MODUL}}",
    "{{ROLA}}",
    "{{TYGODNIE}}",
    "{{GODZINY}}",
    "{{GODZINY_DECL}}",
    "{{KOMPETENCJE_OPIS}}",
]

# Markery wzmianki EFS+ per język (sprawdzamy obecność kluczowej frazy)
EFS_MARKERS = {
    "pl": "Budowa fundamentów pod lokalną politykę migracyjną i integracyjną",
    "en": "Building foundations",
    "es": "Construcción de fundamentos",
    "uk": "Розбудова",
}

# Klucze rejestrowe muszą wystąpić we wszystkich językach
REGISTRY_KEYS = ["0000957190", "7543348716", "521360040"]


def check_file(path: Path, lang: str) -> dict:
    raw = path.read_bytes()
    txt = raw.decode("utf-8")
    em = raw.count(b"\xe2\x80\x94")  # em-dash U+2014
    apo = raw.count(b"\xe2\x80\x99")  # typographic apostrophe (UK only OK)

    missing_ph = [p for p in REQUIRED_PLACEHOLDERS if p not in txt]
    placeholder_counts = {p: txt.count(p) for p in REQUIRED_PLACEHOLDERS}

    has_efs = EFS_MARKERS[lang] in txt
    registry_ok = all(k in txt for k in REGISTRY_KEYS)

    # YAML frontmatter musi mieć "język:" PL z ogonkami (lub equivalent in other langs)
    fm_match = re.match(r"^---\n(.*?)\n---", txt, re.DOTALL)
    fm_ok = bool(fm_match)
    lang_field_ok = False
    if fm_ok:
        fm = fm_match.group(1)
        if lang == "pl":
            lang_field_ok = "język: pl" in fm
        else:
            # other langs: any "language:" or "język:" or "idioma:" or "мова:"
            lang_field_ok = any(
                k in fm for k in ["język:", "language:", "idioma:", "мова:"]
            )

    # PL no-diacritics check (case-sensitive, common offenders)
    # Wytnij placeholdery {{...}} zeby nie laczylo sie z {{MODUL}} -> 'modul'
    no_diac = []
    if lang == "pl":
        txt_no_ph = re.sub(r"\{\{[A-Z_]+\}\}", "", txt)
        offenders = [
            r"\bjezyk\b", r"\bmodul\b", r"\bjezyka\b",
            r"\bukonczenia\b", r"\bzaswiadcza\b",
        ]
        for pat in offenders:
            if re.search(pat, txt_no_ph, re.IGNORECASE):
                no_diac.append(pat)

    word_count = len(re.findall(r"\w+", txt))

    return {
        "lang": lang,
        "em_dash": em,
        "apo": apo,
        "missing_placeholders": missing_ph,
        "placeholder_counts": placeholder_counts,
        "has_efs_marker": has_efs,
        "registry_ok": registry_ok,
        "fm_ok": fm_ok,
        "lang_field_ok": lang_field_ok,
        "no_diac": no_diac,
        "word_count": word_count,
    }


def main():
    failures = []
    for lang in ["pl", "en", "es", "uk"]:
        p = TPL_DIR / f"{lang}.md"
        if not p.exists():
            print(f"[SKIP] {lang}: brak pliku {p}")
            continue
        r = check_file(p, lang)
        problems = []
        if r["em_dash"] > 0:
            problems.append(f"em-dash={r['em_dash']}")
        if r["missing_placeholders"]:
            problems.append(f"missing PH={r['missing_placeholders']}")
        if not r["has_efs_marker"]:
            problems.append("brak wzmianki EFS+")
        if not r["registry_ok"]:
            problems.append("brak KRS/NIP/REGON")
        if not r["fm_ok"]:
            problems.append("brak YAML frontmatter")
        if not r["lang_field_ok"]:
            problems.append("brak/zly klucz jezyk w YAML")
        if r["no_diac"]:
            problems.append(f"PL bez diakrytyk: {r['no_diac']}")

        status = "OK" if not problems else "FAIL"
        print(f"[{status}] {lang}: words={r['word_count']} em={r['em_dash']} apo={r['apo']} PH={r['placeholder_counts']}")
        if problems:
            for pr in problems:
                print(f"       -> {pr}")
            failures.append((lang, problems))

    print("\n=== SUMMARY ===")
    if failures:
        print(f"FAILURES: {len(failures)}")
        for lang, probs in failures:
            print(f"  {lang}: {probs}")
        sys.exit(1)
    else:
        print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
