"""Walidator B2 #2 — RODO klauzula informacyjna i zgody, 4 jezyki.

Reusable szablon dla pojedynczego dokumentu B × 4 jezyki (analogiczny do _validate_b2_1.py).
Sprawdza niezmienniki: em-dash=0, dane Fundacji, podstawy prawne RODO, terminologia per
jezyk, ☐ checkboxy zgod, brak polskich zdan w narracji EN/ES/UK (z wylaczeniem oficjalnych
nazw entities zaczynajacych sie od "Fundacja pomocy prawnej EGIDA" lub
"Fundacja na rzecz edukacji SMART").

Wymaga PYTHONUTF8=1 na Windows.
"""
from __future__ import annotations
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), "..", "podprojekt-b", "B2", "rodo-klauzula-zgody")
LANGS = ("pl", "en", "es", "uk")


def read(lang: str) -> str:
    path = os.path.join(BASE, f"{lang}.md")
    with open(path, "rb") as fh:
        data = fh.read()
    return data.decode("utf-8")


def find_pl_residue_in_translation(txt: str, lang: str) -> list[str]:
    """Wykryj polskie slowa pozostawione w tlumaczeniu (poza oficjalnymi nazwami)."""
    if lang == "pl":
        return []
    residues = []
    # Whitelist oficjalne nazwy entities, ktore zostaja w polskim brzmieniu
    whitelist = ("Fundacja pomocy prawnej EGIDA", "Fundacja na rzecz edukacji SMART")
    masked = txt
    for w in whitelist:
        masked = masked.replace(w, "X" * len(w))
    # Frontmatter YAML kluczy zostaje (np. typ: klauzula) - usun caly frontmatter
    masked = re.sub(r"^---\n.*?\n---\n", "", masked, count=1, flags=re.DOTALL)
    # Szukaj polskich autonomicznych slow w narracji
    polish_markers = ["Kursant", "Przedsiębiorca", "klauzula informacyjna",
                       "wizerunek", "pochodzenia etnicznego", "Wyrażam zgodę",
                       "wyrażam zgody"]
    for m in polish_markers:
        if m in masked:
            residues.append(f"{m} found in {lang}")
    return residues


def main() -> int:
    failures: list[str] = []
    print(f"=== Walidator B2 #2 (RODO klauzula informacyjna + zgody) ===")
    print(f"BASE: {os.path.abspath(BASE)}")
    print()

    for lang in LANGS:
        path = os.path.join(BASE, f"{lang}.md")
        if not os.path.isfile(path):
            failures.append(f"[{lang}] missing file {path}")
            continue
        with open(path, "rb") as fh:
            data = fh.read()
        txt = data.decode("utf-8")
        em = data.count(b"\xe2\x80\x94")
        words = len(txt.split())

        checks: dict[str, bool] = {
            "em_dash_zero": em == 0,
            "KRS": txt.count("0000957190") >= 1,
            "NIP": txt.count("7543348716") >= 1,
            "REGON": txt.count("521360040") >= 1,
            "Ozimska_addr": (txt.count("Ozimska 14-16/314A") + txt.count("Озимська 14-16/314A")) >= 1,
            "sekretariat_email_x2": txt.count("sekretariat@fundacjaegida.eu") >= 2,
            "SMART": txt.count("SMART") >= 1,
            "consent_checkboxes_ge_6": txt.count("☐") >= 6,
        }

        if lang == "pl":
            checks.update({
                "lang_yaml_pl": txt.count("język: pl") >= 1,
                "art_6_lit_a": txt.count("art. 6 ust. 1 lit. a") >= 2,
                "art_6_lit_b": txt.count("art. 6 ust. 1 lit. b") >= 1,
                "art_6_lit_c": txt.count("art. 6 ust. 1 lit. c") >= 1,
                "art_6_lit_f": txt.count("art. 6 ust. 1 lit. f") >= 1,
                "art_9_lit_a": txt.count("art. 9 ust. 2 lit. a") >= 2,
                "art_9_lit_h": txt.count("art. 9 ust. 2 lit. h") >= 1,
                "art_13_RODO": txt.count("art. 13 RODO") >= 2,
                "art_15_to_22_present": all(f"art. {n} RODO" in txt for n in (15, 16, 17, 18, 20, 21, 22)),
                "Prezes_UODO": txt.count("Prezes Urzędu Ochrony Danych Osobowych") >= 1,
                "Fundacja_x_ge_5": txt.count("Fundacja") >= 5,
                "Przedsiebiorca_x_ge_3": txt.count("Przedsiębiorc") >= 3,
                "Kursant_x_ge_5": txt.count("Kursant") >= 5,
                "EFS_marker": txt.count("EFS+") >= 1,
                "retention_5_lat": txt.count("5 lat") >= 1,
                "retention_10_lat": txt.count("10 lat") >= 1,
                "retention_bezterminowo": txt.count("bezterminowo") >= 1,
                "newsletter": txt.lower().count("newsletter") >= 3,
                "wizerunek": txt.count("wizerune") >= 3,
                "pochodzenie_etniczne": (txt.count("pochodzenia etnicznego") + txt.count("pochodzenie etniczne") + txt.count("pochodzeniu etnicznym")) >= 3,
            })
        elif lang == "en":
            checks.update({
                "lang_yaml_en": txt.count("język: en") >= 1,
                "no_jezyk_pl": txt.count("język: pl") == 0,
                "art_6_a_b_c_f_present": all(s in txt for s in ("Article 6(1)(a)", "Article 6(1)(b)", "Article 6(1)(c)", "Article 6(1)(f)")),
                "art_9_a_h_present": all(s in txt for s in ("Article 9(2)(a)", "Article 9(2)(h)")),
                "art_13_GDPR_x2": txt.count("Article 13") >= 2,
                "art_15_to_22": all(f"Article {n}" in txt for n in (15, 16, 17, 18, 20, 21, 22)),
                "GDPR_x_ge_5": txt.count("GDPR") >= 5,
                "Foundation_x_ge_5": txt.count("Foundation") >= 5,
                "Entrepreneur_x_ge_5": txt.count("Entrepreneur") >= 5,
                "Participant_x_ge_5": txt.count("Participant") >= 5,
                "ESF_marker": txt.count("ESF+") >= 1,
                "ethnic_origin": txt.lower().count("ethnic origin") >= 3,
                "newsletter": txt.lower().count("newsletter") >= 3,
                "image_or_likeness": (txt.lower().count("image") + txt.lower().count("likeness")) >= 3,
                "UODO": txt.count("UODO") >= 2,
            })
        elif lang == "es":
            checks.update({
                "lang_yaml_es": txt.count("język: es") >= 1,
                "no_jezyk_pl": txt.count("język: pl") == 0,
                "RGPD_x_ge_5": txt.count("RGPD") >= 5,
                "Fundacion_x_ge_5": txt.count("Fundación") >= 5,
                "Empresario_x_ge_5": txt.count("Empresario") >= 5,
                "Cursante_or_Participante": (txt.count("Cursante") + txt.count("Participante")) >= 5,
                "FSE_marker": txt.count("FSE+") >= 1,
                "origen_etnico": txt.lower().count("origen étnico") >= 3,
                "imagen": txt.lower().count("imagen") >= 3,
                "salud_o_BHP": any(s in txt.lower() for s in ("seguridad y salud", "salud laboral", "seguridad e higiene")),
                "UODO": txt.count("UODO") >= 2,
            })
        elif lang == "uk":
            apo = data.count(b"\xe2\x80\x99")
            fond_count = len(re.findall(r"\bФонд\b", txt))
            fundacia_count = len(re.findall(r"Фундаці[яії]|Фундацією", txt))
            checks.update({
                "lang_yaml_uk": txt.count("język: uk") >= 1,
                "no_jezyk_pl": txt.count("język: pl") == 0,
                "apostrophes_typographic": apo >= 1,
                "Fundacia_dominant": fundacia_count >= 5,
                "no_Fond_lone": fond_count == 0,
                "Pidpryiemets_x_ge_3": (txt.count("Підприємец") + txt.count("Підприємц")) >= 3,
                "Kursant_or_Uchasnyk_x_ge_5": (txt.count("Курсант") + txt.count("Учасник Курсу")) >= 5,
                "EFS_marker_cyr": txt.count("ЄСФ") >= 1,
                "ethnic_etnich": txt.lower().count("етнічн") >= 3,
                "TAK_NI_consent": txt.count("ТАК") >= 3 and txt.count("НІ") >= 3,
                "UODO": txt.count("UODO") >= 2,
            })

        residues = find_pl_residue_in_translation(txt, lang)
        if residues:
            checks["no_pl_residue"] = False
        else:
            checks["no_pl_residue"] = True

        bad = [k for k, v in checks.items() if not v]
        status = "OK" if not bad else "FAIL"
        print(f"[{lang}] words={words} em-dash={em} status={status}")
        if bad:
            print(f"   FAILED checks: {bad}")
            if residues:
                print(f"   PL residues: {residues}")
            failures.append(f"{lang}: {bad}")
        else:
            print(f"   all {len(checks)} checks pass")

    print()
    if failures:
        print(f"GLOBAL: FAIL ({len(failures)} languages)")
        for f in failures:
            print(f"  {f}")
        return 1
    print("GLOBAL: ALL 4 LANGUAGES PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
