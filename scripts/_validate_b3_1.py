"""Walidator B3 #1 - Polityka reklamacji i odwolan, 4 jezyki.

Reusable szablon dla pojedynczego dokumentu B3 x 4 jezyki.
"""
from __future__ import annotations
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), "..", "podprojekt-b", "B3", "polityka-reklamacji")
LANGS = ("pl", "en", "es", "uk")


def main() -> int:
    failures: list[str] = []
    print(f"=== Walidator B3 #1 (Polityka reklamacji i odwolan) ===")
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
            "reklamacje_email": txt.count("reklamacje@fundacjaegida.eu") >= 1,
            "SMART": txt.count("SMART") >= 1,
            "Opole_or_decl": (txt.count("Opole") + txt.count("Opolu") + txt.count("Ополе") + txt.count("Ополі")) >= 2,
        }

        if lang == "pl":
            checks.update({
                "lang_yaml_pl": txt.count("język: pl") >= 1,
                "Fundacja_x_ge_5": txt.count("Fundacja") >= 5,
                "Przedsiebiorca_x_ge_3": txt.count("Przedsiębiorc") >= 3,
                "Kursant_x_ge_5": txt.count("Kursant") >= 5,
                "reklamacja_x_ge_5": txt.count("eklamacj") >= 5,
                "odwolanie_x_ge_3": txt.count("dwołani") >= 3,
                "term_14_dni": txt.count("14 dni") >= 2,
                "term_30_dni": txt.count("30 dni") >= 2,
                "RODO": txt.count("RODO") >= 2,
                "UODO": txt.count("UODO") >= 2,
                "EFS_marker": txt.count("EFS+") >= 1,
                "art_384_KC": txt.count("art. 384") >= 1,
            })
        elif lang == "en":
            checks.update({
                "lang_yaml_en": txt.count("język: en") >= 1,
                "no_jezyk_pl": txt.count("język: pl") == 0,
                "Foundation_x_ge_5": txt.count("Foundation") >= 5,
                "Entrepreneur_x_ge_3": txt.count("Entrepreneur") >= 3,
                "Participant_x_ge_5": txt.count("Participant") >= 5,
                "complaint_x_ge_5": txt.lower().count("complaint") >= 5,
                "appeal_x_ge_3": txt.lower().count("appeal") >= 3,
                "term_14_days": txt.count("14 days") >= 2,
                "term_30_days": txt.count("30 days") >= 2,
                "GDPR": txt.count("GDPR") >= 2,
                "UODO": txt.count("UODO") >= 2,
                "Civil_Code": txt.count("Civil Code") >= 1,
                "ESF_marker": txt.count("ESF+") >= 1,
            })
        elif lang == "es":
            checks.update({
                "lang_yaml_es": txt.count("język: es") >= 1,
                "no_jezyk_pl": txt.count("język: pl") == 0,
                "Fundacion_x_ge_5": txt.count("Fundación") >= 5,
                "Empresario_x_ge_3": txt.count("Empresario") >= 3,
                "Cursante_or_Participante": (txt.count("Cursante") + txt.count("Participante")) >= 5,
                "reclamacion_x_ge_5": txt.lower().count("reclamación") + txt.lower().count("reclamaciones") >= 5,
                "apelacion_x_ge_3": txt.lower().count("apelación") + txt.lower().count("apelaciones") >= 3,
                "term_14_dias": txt.count("14 días") >= 2,
                "term_30_dias": txt.count("30 días") >= 2,
                "RGPD": txt.count("RGPD") >= 2,
                "UODO": txt.count("UODO") >= 2,
                "Codigo_Civil": txt.count("Código Civil") >= 1,
                "FSE_marker": txt.count("FSE+") >= 1,
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
                "Pidpryiemets": (txt.count("Підприємец") + txt.count("Підприємц")) >= 3,
                "Kursant_or_Uchasnyk": (txt.count("Курсант") + txt.count("Учасник Курсу")) >= 5,
                "EFS_marker_cyr": txt.count("ЄСФ") >= 1,
                "UODO": txt.count("UODO") >= 2,
                "term_14_dni_uk": (txt.count("14 днів") + txt.count("14-денн")) >= 2,
                "term_30_dni_uk": (txt.count("30 днів") + txt.count("30-денн")) >= 2,
            })

        # No PL residue check (poza oficjalnymi nazwami)
        whitelist = ("Fundacja pomocy prawnej EGIDA", "Fundacja na rzecz edukacji SMART")
        masked = txt
        for w in whitelist:
            masked = masked.replace(w, "X" * len(w))
        masked = re.sub(r"^---\n.*?\n---\n", "", masked, count=1, flags=re.DOTALL)
        if lang != "pl":
            for marker in ("Kursant ", "Przedsiębiorca", "klauzula informacyjna"):
                if marker in masked:
                    checks[f"no_pl_residue_{marker.strip()}"] = False
                else:
                    checks[f"no_pl_residue_{marker.strip()}"] = True

        bad = [k for k, v in checks.items() if not v]
        status = "OK" if not bad else "FAIL"
        print(f"[{lang}] words={words} em-dash={em} status={status}")
        if bad:
            print(f"   FAILED: {bad}")
            failures.append(f"{lang}: {bad}")
        else:
            print(f"   all {len(checks)} checks pass")

    print()
    if failures:
        print(f"GLOBAL: FAIL ({len(failures)} languages)")
        return 1
    print("GLOBAL: ALL 4 LANGUAGES PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
