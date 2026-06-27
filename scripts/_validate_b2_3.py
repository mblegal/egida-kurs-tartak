#!/usr/bin/env python3
"""
Walidator globalny B2 #3 (formularz rekrutacyjny) x 4 jezyki.

Reusable szablon dla dokumentu B z polami checkbox/oswiadczeniami/zgodami.
Analogiczny do _validate_b2_2.py (RODO) i _validate_b3_1.py (polityka reklamacji).

Uruchamiac z roota kurs_tartak/:
    python scripts/_validate_b2_3.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = ROOT / "podprojekt-b" / "B2" / "formularz-rekrutacyjny"

LANGS = ("pl", "en", "es", "uk")


def load(path: Path) -> tuple[bytes, str]:
    raw = path.read_bytes()
    return raw, raw.decode("utf-8")


def common_checks(raw: bytes, txt: str, lang: str) -> dict[str, bool]:
    em = raw.count(b"\xe2\x80\x94")
    return {
        "em_dash_zero": em == 0,
        "frontmatter_typ": "typ:" in txt,
        "frontmatter_jezyk": f"język: {lang}" in txt,
        "frontmatter_charakter": "charakter:" in txt,
        "frontmatter_strony": "strony:" in txt,
        "KRS_0000957190": txt.count("0000957190") >= 1,
        "NIP_7543348716": txt.count("7543348716") >= 1,
        "REGON_521360040": txt.count("521360040") >= 1,
        "Opole_present": (
            txt.count("Opole") >= 1
            or txt.count("Ополе") >= 1
            or txt.count("Ополі") >= 1
        ),
        "FRK_id": "FRK-1.0/2026" in txt,
        "M1_present": txt.count("M1") >= 5,
        "M2_present": txt.count("M2") >= 5,
        "M3_present": txt.count("M3") >= 3,
        "316_h": txt.count("316") >= 2,
        "70_pct": "70%" in txt,
        "75_pct": "75%" in txt,
        "checkbox_30": txt.count("☐") >= 30,
        "sekretariat_email_x2": txt.count("sekretariat@fundacjaegida.eu") >= 2,
        "EFS_wzmianka": (
            "EFS+" in txt or "ESF+" in txt or "FSE+" in txt or "ЄСФ" in txt
        ),
        "project_name": "Budowa fundamentów" in txt,
        "CEFR_levels_all": all(
            lev in txt for lev in ("A1", "A2", "B1", "B2", "C1", "C2")
        ),
    }


def pl_checks(raw: bytes, txt: str) -> dict[str, bool]:
    return {
        "art_6_1_b_PL": txt.count("art. 6 ust. 1 lit. b") >= 2,
        "art_6_1_f_PL": txt.count("art. 6 ust. 1 lit. f") >= 1,
        "art_71_KC_PL": txt.count("art. 71") >= 1,
        "art_84_KC_PL": txt.count("art. 84") >= 1,
        "art_415_KC_PL": txt.count("art. 415") >= 1,
        "art_233_KK_PL": txt.count("art. 233") >= 1,
        "Oswiadczam_3plus": txt.count("Oświadczam") >= 3,
        "Wyrazam_3plus": txt.count("Wyrażam") >= 3,
        "12_tygodni_PL": txt.count("12 tygodni") >= 2,
        "trzy_sposoby_PL": (
            "osobiście" in txt
            and "pocztą elektroniczną" in txt
            and "pocztą tradycyjną" in txt
        ),
    }


def en_checks(raw: bytes, txt: str) -> dict[str, bool]:
    return {
        "GDPR_6_1_b_EN": (
            txt.count("Article 6(1)(b)") >= 2 or txt.count("art. 6(1)(b)") >= 2
        ),
        "GDPR_6_1_f_EN": (
            txt.count("Article 6(1)(f)") >= 1 or txt.count("art. 6(1)(f)") >= 1
        ),
        "Article_71_EN": txt.count("Article 71") >= 1,
        "Article_84_EN": txt.count("Article 84") >= 1,
        "Article_415_EN": txt.count("Article 415") >= 1,
        "Article_233_EN": txt.count("Article 233") >= 1,
        "Foundation_10plus": txt.count("Foundation") >= 10,
        "Candidate_5plus": (
            txt.count("Candidate") >= 5 or txt.count("candidate") >= 5
        ),
        "12_weeks_EN": (
            txt.count("12 weeks") >= 2 or txt.count("twelve weeks") >= 2
        ),
        "no_pl_residue_EN": (
            txt.count("Wyrażam") == 0 and txt.count("Oświadczam") == 0
        ),
        "recruitment_EN": "recruitment" in txt.lower(),
    }


def es_checks(raw: bytes, txt: str) -> dict[str, bool]:
    return {
        "RGPD_6_1_b_ES": (
            txt.count("art. 6, apartado 1, letra b)") >= 1
            or txt.count("artículo 6, apartado 1, letra b)") >= 1
            or txt.count("letra b) del RGPD") >= 1
        ),
        "RGPD_6_1_f_ES": (
            txt.count("letra f)") >= 1 or txt.count("apartado 1, letra f)") >= 1
        ),
        "art_71_ES": txt.count("art. 71") >= 1 or txt.count("artículo 71") >= 1,
        "art_84_ES": txt.count("art. 84") >= 1 or txt.count("artículo 84") >= 1,
        "art_415_ES": txt.count("art. 415") >= 1 or txt.count("artículo 415") >= 1,
        "art_233_ES": txt.count("art. 233") >= 1 or txt.count("artículo 233") >= 1,
        "Fundacion_10plus": txt.count("Fundación") >= 10,
        "12_semanas_ES": txt.count("12 semanas") >= 2,
        "no_pl_residue_ES": (
            txt.count("Wyrażam") == 0 and txt.count("Oświadczam") == 0
        ),
        "seleccion_or_reclutamiento_ES": (
            "selección" in txt.lower()
            or "reclutamiento" in txt.lower()
            or "admisión" in txt.lower()
        ),
    }


def uk_checks(raw: bytes, txt: str) -> dict[str, bool]:
    cyr_zl = len(re.findall(r"\d+\s*зл\b", txt))
    return {
        "Fundacja_dominantna_UK": (
            txt.count("Фундація") >= 5
            or txt.count("Фундації") >= 5
            or txt.count("Фундацію") >= 1
        ),
        "Fond_zakaz_UK": txt.count("Фонд") == 0,
        "Kursant_UK": txt.count("Курсант") >= 3,
        "Kandydat_UK": (
            txt.count("Кандидат") >= 3 or txt.count("кандидат") >= 5
        ),
        "GDPR_6_1_b_UK": (
            txt.count("ст. 6 ч. 1 літ. b)") >= 2
            or txt.count("ст. 6, ч. 1, літ. b)") >= 2
            or txt.count("літ. b)") >= 2
        ),
        "GDPR_6_1_f_UK": txt.count("літ. f)") >= 1,
        "art_71_UK": (
            txt.count("ст. 71") >= 1 or txt.count("статті 71") >= 1
        ),
        "art_84_UK": (
            txt.count("ст. 84") >= 1 or txt.count("статті 84") >= 1
        ),
        "art_415_UK": (
            txt.count("ст. 415") >= 1 or txt.count("статті 415") >= 1
        ),
        "art_233_UK": (
            txt.count("ст. 233") >= 1 or txt.count("статті 233") >= 1
        ),
        "12_tyzhniv_UK": txt.count("12 тижнів") >= 2,
        "cyr_zl_zero_UK": cyr_zl == 0,
        "no_pl_residue_UK": (
            txt.count("Wyrażam") == 0 and txt.count("Oświadczam") == 0
        ),
    }


def words(txt: str) -> int:
    return len(re.findall(r"\w+", txt, re.UNICODE))


def main() -> int:
    print("=" * 64)
    print(f"Walidator B2 #3 (formularz rekrutacyjny) — {DOC_DIR.relative_to(ROOT)}")
    print("=" * 64)

    total_failed = 0
    for lang in LANGS:
        path = DOC_DIR / f"{lang}.md"
        if not path.exists():
            print(f"\n[{lang.upper()}] BRAK PLIKU: {path}")
            total_failed += 1
            continue

        raw, txt = load(path)
        checks = common_checks(raw, txt, lang)
        if lang == "pl":
            checks.update(pl_checks(raw, txt))
        elif lang == "en":
            checks.update(en_checks(raw, txt))
        elif lang == "es":
            checks.update(es_checks(raw, txt))
        elif lang == "uk":
            checks.update(uk_checks(raw, txt))

        failed = [k for k, v in checks.items() if not v]
        status = "ALL CHECKS PASSED" if not failed else f"FAILED: {failed}"
        print(f"\n[{lang.upper()}] {path.name}  ({words(txt)} słów)")
        print(f"  checks: {len(checks)} total, {len(failed)} failed")
        print(f"  {status}")
        total_failed += len(failed)

    print("\n" + "=" * 64)
    if total_failed == 0:
        print("WALIDACJA GLOBALNA: ALL CHECKS PASSED 4/4 plików")
        return 0
    print(f"WALIDACJA GLOBALNA: {total_failed} czeków FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
