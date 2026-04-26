#!/usr/bin/env python3
"""
Walidator globalny B1 #7 (zaswiadczenie praktyki absolwenckiej):
- B1 #7a: zaswiadczenie o ODBYWANIU praktyki x 4 jezyki
- B1 #7b: zaswiadczenie o UKONCZENIU praktyki x 4 jezyki

Razem 8 plikow.

Uruchamiac z roota kurs_tartak/:
    python scripts/_validate_b1_7.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("pl", "en", "es", "uk")
DOCS = (
    ("zaswiadczenie-praktyki-odbywania", "ODBYWANIA"),
    ("zaswiadczenie-praktyki-ukonczenia", "UKONCZENIA"),
)


def common_checks(raw: bytes, txt: str, lang: str) -> dict[str, bool]:
    em = raw.count(b"\xe2\x80\x94")
    return {
        "em_dash_zero": em == 0,
        "frontmatter_typ": "typ:" in txt,
        "frontmatter_jezyk": f"język: {lang}" in txt,
        "frontmatter_strony": "strony:" in txt,
        "frontmatter_wystawia": "wystawia:" in txt,
        "KRS_0000957190": txt.count("0000957190") >= 1,
        "NIP_7543348716": txt.count("7543348716") >= 1,
        "REGON_521360040": txt.count("521360040") >= 1,
        "Opole_present": (
            txt.count("Opole") >= 1
            or txt.count("Ополе") >= 1
            or txt.count("Ополі") >= 1
        ),
        "M1_4plus": txt.count("M1") >= 4,
        "M2_4plus": txt.count("M2") >= 4,
        "M3_3plus": txt.count("M3") >= 3,
        "316_h": "316" in txt,
        "art_306": "306" in txt,
        "ustawa_2025": "2025" in txt and "620" in txt,
        "ustawa_praktyk_2009": (
            txt.count("17 lipca 2009") >= 2
            or txt.count("17 July 2009") >= 2
            or txt.count("17 de julio de 2009") >= 2
            or txt.count("17 липня 2009") >= 2
        ),
        "EFS_wzmianka": (
            "EFS+" in txt or "ESF+" in txt or "FSE+" in txt or "ЄСФ" in txt
        ),
        "project_name": "Budowa fundamentów" in txt,
    }


def pl_checks(raw: bytes, txt: str, doctype: str) -> dict[str, bool]:
    base = {
        "art_5_ust_1_PL": txt.count("art. 5 ust. 1") >= 1,
        "art_2_ust_1_PL": txt.count("art. 2 ust. 1") >= 1,
        "wiek_30_PL": "30. roku życia" in txt or "30 roku życia" in txt,
        "praktykant_5plus": txt.count("Praktykant") >= 5,
        "fundacja_5plus": txt.count("Fundacj") >= 5,
        "12_tygodni_PL": txt.count("12 tygodni") >= 1,
        "BHP_PL": "BHP" in txt,
    }
    if doctype == "ODBYWANIA":
        base["nie_zastepuje_ukonczenia"] = "ukończenia praktyki" in txt
    else:
        base["art_7_ust_1_PL"] = txt.count("art. 7 ust. 1") >= 2
        base["B1_6_ref"] = "B1 #6" in txt
        base["B1_7a_ref"] = "B1 #7a" in txt
        base["umiejetnosci_nabyte_PL"] = "umiejętności" in txt and "nabyt" in txt
    return base


def en_checks(raw: bytes, txt: str, doctype: str) -> dict[str, bool]:
    base = {
        "Foundation_8plus": txt.count("Foundation") >= 8,
        "Trainee_5plus": txt.count("Trainee") >= 5,
        "Article_5": "5(1)" in txt or "Article 5" in txt,
        "Article_2": "2(1)" in txt or "Article 2" in txt,
        "OHS_or_BHP": "OHS" in txt or "BHP" in txt,
        "no_pl_residue_EN": (
            txt.count("Oświadczam") == 0 and txt.count("Wyrażam") == 0
        ),
        "30_years_or_lat": "30" in txt,
        "12_weeks_EN": "12 weeks" in txt or "twelve weeks" in txt,
        "apprenticeship_EN": "apprenticeship" in txt.lower(),
    }
    if doctype == "UKONCZENIA":
        base["Article_7"] = "7(1)" in txt or "Article 7" in txt
        base["B1_6_ref_EN"] = "B1 #6" in txt
        base["B1_7a_ref_EN"] = "B1 #7a" in txt
    return base


def es_checks(raw: bytes, txt: str, doctype: str) -> dict[str, bool]:
    base = {
        "Fundacion_8plus": txt.count("Fundación") >= 8,
        "Practicante_5plus": (
            txt.count("Practicante") >= 5 or txt.count("practicante") >= 5
        ),
        "art_5": "art. 5" in txt or "artículo 5" in txt,
        "art_2": "art. 2" in txt or "artículo 2" in txt,
        "SST_or_BHP": (
            "SST" in txt or "BHP" in txt or "salud" in txt.lower()
        ),
        "no_pl_residue_ES": (
            txt.count("Oświadczam") == 0 and txt.count("Wyrażam") == 0
        ),
        "12_semanas_ES": "12 semanas" in txt,
        "practicas_ES": "prácticas" in txt.lower(),
    }
    if doctype == "UKONCZENIA":
        base["art_7"] = "art. 7" in txt or "artículo 7" in txt
        base["B1_6_ref_ES"] = "B1 #6" in txt
        base["B1_7a_ref_ES"] = "B1 #7a" in txt
    return base


def uk_checks(raw: bytes, txt: str, doctype: str) -> dict[str, bool]:
    cyr_zl = len(re.findall(r"\d+\s*зл\b", txt))
    base = {
        "Fundacja_dominantna_UK": (
            txt.count("Фундація") >= 4 or txt.count("Фундації") >= 4
        ),
        "Fond_zakaz_UK": txt.count("Фонд") == 0,
        "Praktykant_5plus_UK": txt.count("Практикант") >= 5,
        "Pidpryemets_UK": (
            txt.count("Підприємець") >= 3 or txt.count("Підприємця") >= 3
        ),
        "art_5_UK": "ст. 5" in txt or "статті 5" in txt,
        "art_2_UK": "ст. 2" in txt or "статті 2" in txt,
        "no_cyr_zl_UK": cyr_zl == 0,
        "no_pl_residue_UK": (
            txt.count("Oświadczam") == 0 and txt.count("Wyrażam") == 0
        ),
        "praktyka_UK": "практик" in txt.lower(),
        "12_tyzhniv_UK": "12 тижнів" in txt,
        "vipusknytska_UK": "випускниц" in txt,  # spojnosc terminologii
        "uchnivska_zakaz_UK": "учнівськ" not in txt,
    }
    if doctype == "UKONCZENIA":
        base["art_7_UK"] = "ст. 7" in txt or "статті 7" in txt
        base["B1_6_ref_UK"] = "B1 #6" in txt
        base["B1_7a_ref_UK"] = "B1 #7a" in txt
    return base


def words(txt: str) -> int:
    return len(re.findall(r"\w+", txt, re.UNICODE))


def main() -> int:
    print("=" * 64)
    print("Walidator B1 #7 (zaswiadczenia praktyki absolwenckiej): 8 plikow")
    print("=" * 64)

    total_failed = 0
    for doc_dir, doctype in DOCS:
        print(f"\n=== {doctype} ({doc_dir}) ===")
        for lang in LANGS:
            path = ROOT / "podprojekt-b" / "B1" / doc_dir / f"{lang}.md"
            if not path.exists():
                print(f"  [{lang.upper()}] BRAK PLIKU: {path}")
                total_failed += 1
                continue

            raw = path.read_bytes()
            txt = raw.decode("utf-8")
            checks = common_checks(raw, txt, lang)
            if lang == "pl":
                checks.update(pl_checks(raw, txt, doctype))
            elif lang == "en":
                checks.update(en_checks(raw, txt, doctype))
            elif lang == "es":
                checks.update(es_checks(raw, txt, doctype))
            elif lang == "uk":
                checks.update(uk_checks(raw, txt, doctype))

            failed = [k for k, v in checks.items() if not v]
            status = "ALL CHECKS PASSED" if not failed else f"FAILED: {failed}"
            print(
                f"  [{lang.upper()}] {path.name}  ({words(txt)} slow)  "
                f"{len(checks)} checks, {len(failed)} failed"
            )
            if failed:
                print(f"      {status}")
            total_failed += len(failed)

    print("\n" + "=" * 64)
    if total_failed == 0:
        print("WALIDACJA GLOBALNA: ALL CHECKS PASSED 8/8 plikow")
        return 0
    print(f"WALIDACJA GLOBALNA: {total_failed} czekow FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
