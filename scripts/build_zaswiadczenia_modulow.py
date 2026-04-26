#!/usr/bin/env python3
"""
Generator zaświadczeń ukończenia modułów M1/M2/M3 × 4 jęz (12 plików).

Czyta szablon z `podprojekt-b/B1/_szablony/zaswiadczenie-ukonczenia-modulu/{lang}.md`
z placeholderami {{MODUL}}, {{ROLA}}, {{TYGODNIE}}, {{GODZINY}}, {{KOMPETENCJE_OPIS}}
i podstawia wartości z tabeli DATA per (jezyk, modul).

Wynik: `podprojekt-b/B1/zaswiadczenie-ukonczenia-modulu-m{1,2,3}/{lang}.md` (12 plików).

Domyślnie dry-run; --apply żeby zapisać.
"""
import argparse
import os
import sys
from pathlib import Path

if sys.platform == "win32":
    os.environ["PYTHONUTF8"] = "1"
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent.parent
TPL_DIR = ROOT / "podprojekt-b" / "B1" / "_szablony" / "zaswiadczenie-ukonczenia-modulu"
OUT_BASE = ROOT / "podprojekt-b" / "B1"

LANGS = ["pl", "en", "es", "uk"]
MODULES = ["M1", "M2", "M3"]

# Wszystkie wartości muszą być spójne z umową kursu (Part 35) i zaświadczeniem odbywania (Part 36):
# M1=4 tyg/72h pomocnik, M2=4 tyg/112h operator pod nadzorem, M3=4 tyg/132h operator samodzielny.
DATA = {
    "pl": {
        "M1": {
            "ROLA": "Pracownik pomocniczy w tartaku",
            "TYGODNIE": "4",
            "GODZINY": "72",
            "GODZINY_DECL": "godziny dydaktyczne",
            "KOMPETENCJE_OPIS": (
                "rozpoznawanie surowca drzewnego, podstawy BHP w zakładzie tartacznym, "
                "znakowanie i przemieszczanie materiału, obsługa pomocnicza prostych operacji "
                "manipulacyjno-magazynowych, podstawy komunikacji zawodowej w środowisku polskojęzycznym"
            ),
        },
        "M2": {
            "ROLA": "Operator urządzeń tartacznych pod nadzorem",
            "TYGODNIE": "4",
            "GODZINY": "112",
            "GODZINY_DECL": "godzin dydaktycznych",
            "KOMPETENCJE_OPIS": (
                "obsługa pod nadzorem podstawowych maszyn tartacznych (traki taśmowe, traki ramowe, "
                "gatry, piły tarczowe), kontrola parametrów cięcia, znajomość sortymentów wyrobu, "
                "identyfikacja zagrożeń mechanicznych i procedur awaryjnych, prowadzenie elementarnej "
                "dokumentacji technicznej procesu obróbki"
            ),
        },
        "M3": {
            "ROLA": "Operator samodzielny",
            "TYGODNIE": "4",
            "GODZINY": "132",
            "GODZINY_DECL": "godziny dydaktyczne",
            "KOMPETENCJE_OPIS": (
                "samodzielna obsługa kompletu maszyn tartacznych w trybie produkcyjnym, optymalizacja "
                "cięcia pod kątem wydajności surowcowej, planowanie sortymentowe, kontrola jakości "
                "wyrobu (klasy, wady, sortowanie), współpraca z innymi stanowiskami w łańcuchu "
                "produkcyjnym, podstawy obsługi systemów rejestracji produkcji oraz przepisów "
                "dotyczących eksploatacji maszyn (UDT, BHP)"
            ),
        },
    },
    "en": {
        "M1": {
            "ROLA": "Sawmill assistant worker",
            "TYGODNIE": "4",
            "GODZINY": "72",
            "GODZINY_DECL": "teaching hours",
            "KOMPETENCJE_OPIS": (
                "wood raw material recognition, basics of occupational health and safety in the "
                "sawmill, marking and moving of material, auxiliary handling of simple manipulation "
                "and warehousing operations, basics of vocational communication in a Polish-speaking "
                "environment"
            ),
        },
        "M2": {
            "ROLA": "Operator of sawmill machines under supervision",
            "TYGODNIE": "4",
            "GODZINY": "112",
            "GODZINY_DECL": "teaching hours",
            "KOMPETENCJE_OPIS": (
                "supervised operation of basic sawmill machines (band saws, frame saws, gang saws, "
                "circular saws), control of cutting parameters, knowledge of product assortments, "
                "identification of mechanical hazards and emergency procedures, keeping basic "
                "technical documentation of the processing operations"
            ),
        },
        "M3": {
            "ROLA": "Independent operator",
            "TYGODNIE": "4",
            "GODZINY": "132",
            "GODZINY_DECL": "teaching hours",
            "KOMPETENCJE_OPIS": (
                "independent operation of a complete set of sawmill machines in production mode, "
                "cutting optimization for raw material yield, assortment planning, quality control "
                "of products (grades, defects, sorting), cooperation with other stations in the "
                "production chain, basics of production registration systems and regulations on "
                "machine operation (UDT, occupational health and safety)"
            ),
        },
    },
    "es": {
        "M1": {
            "ROLA": "Trabajador auxiliar de aserradero",
            "TYGODNIE": "4",
            "GODZINY": "72",
            "GODZINY_DECL": "horas didácticas",
            "KOMPETENCJE_OPIS": (
                "reconocimiento de la materia prima de madera, fundamentos de seguridad e higiene "
                "laboral en el aserradero, marcado y traslado del material, manejo auxiliar de "
                "operaciones simples de manipulación y almacenamiento, fundamentos de comunicación "
                "profesional en un entorno de habla polaca"
            ),
        },
        "M2": {
            "ROLA": "Operador de máquinas de aserradero bajo supervisión",
            "TYGODNIE": "4",
            "GODZINY": "112",
            "GODZINY_DECL": "horas didácticas",
            "KOMPETENCJE_OPIS": (
                "operación bajo supervisión de las máquinas básicas de aserradero (sierras de cinta, "
                "sierras de marco, sierras múltiples, sierras circulares), control de los parámetros "
                "de corte, conocimiento de los surtidos del producto, identificación de los riesgos "
                "mecánicos y de los procedimientos de emergencia, llevanza de la documentación "
                "técnica básica del proceso de transformación"
            ),
        },
        "M3": {
            "ROLA": "Operador independiente",
            "TYGODNIE": "4",
            "GODZINY": "132",
            "GODZINY_DECL": "horas didácticas",
            "KOMPETENCJE_OPIS": (
                "operación independiente de un conjunto completo de máquinas de aserradero en modo "
                "de producción, optimización del corte en función del rendimiento de la materia "
                "prima, planificación de surtidos, control de calidad del producto (clases, defectos, "
                "clasificación), cooperación con otras estaciones en la cadena de producción, "
                "fundamentos de los sistemas de registro de la producción y de las normas sobre el "
                "funcionamiento de las máquinas (UDT, seguridad e higiene laboral)"
            ),
        },
    },
    "uk": {
        "M1": {
            "ROLA": "Допоміжний працівник тартака",
            "TYGODNIE": "4",
            "GODZINY": "72",
            "GODZINY_DECL": "дидактичні години",
            "KOMPETENCJE_OPIS": (
                "розпізнавання деревної сировини, основи охорони праці на тартаку, маркування та "
                "переміщення матеріалу, допоміжне виконання простих маніпуляційно-складських "
                "операцій, основи професійної комунікації в польськомовному середовищі"
            ),
        },
        "M2": {
            "ROLA": "Оператор тартацьких машин під наглядом",
            "TYGODNIE": "4",
            "GODZINY": "112",
            "GODZINY_DECL": "дидактичних годин",
            "KOMPETENCJE_OPIS": (
                "робота під наглядом з основними тартацькими машинами (стрічкові пили, рамні пили, "
                "гатери, дискові пили), контроль параметрів пиляння, знання сортиментів виробу, "
                "ідентифікація механічних небезпек та аварійних процедур, ведення елементарної "
                "технічної документації процесу обробки"
            ),
        },
        "M3": {
            "ROLA": "Самостійний оператор",
            "TYGODNIE": "4",
            "GODZINY": "132",
            "GODZINY_DECL": "дидактичні години",
            "KOMPETENCJE_OPIS": (
                "самостійна робота з повним комплектом тартацьких машин у виробничому режимі, "
                "оптимізація пиляння з огляду на сировинну продуктивність, планування сортиментів, "
                "контроль якості виробу (класи, вади, сортування), співпраця з іншими ділянками у "
                "виробничому ланцюгу, основи роботи з системами реєстрації виробництва та норм "
                "щодо експлуатації машин (UDT, охорона праці)"
            ),
        },
    },
}

PLACEHOLDERS = ["MODUL", "ROLA", "TYGODNIE", "GODZINY", "GODZINY_DECL", "KOMPETENCJE_OPIS"]


def build(apply: bool) -> int:
    written = 0
    for lang in LANGS:
        tpl_path = TPL_DIR / f"{lang}.md"
        if not tpl_path.exists():
            print(f"[ERROR] Brak szablonu: {tpl_path}")
            return 1
        tpl = tpl_path.read_text(encoding="utf-8")

        for module in MODULES:
            data = DATA[lang][module]
            out = tpl
            substitutions = {"MODUL": module, **data}
            for key in PLACEHOLDERS:
                out = out.replace(f"{{{{{key}}}}}", substitutions[key])

            # Sanity check - zaden placeholder nie pozostal
            for key in PLACEHOLDERS:
                marker = f"{{{{{key}}}}}"
                if marker in out:
                    print(f"[ERROR] {lang}/{module}: placeholder {marker} nadal obecny po zamianie")
                    return 1

            out_dir = OUT_BASE / f"zaswiadczenie-ukonczenia-modulu-{module.lower()}"
            out_path = out_dir / f"{lang}.md"
            mode = "APPLY" if apply else "DRY-RUN"
            print(f"[{mode}] {out_path.relative_to(ROOT)}  ({len(out)} bytes)")
            if apply:
                out_dir.mkdir(parents=True, exist_ok=True)
                out_path.write_text(out, encoding="utf-8")
                written += 1

    print(f"\n=== {'WRITTEN' if apply else 'WOULD WRITE'}: {12 if apply else 12} plików ===")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Generator zaświadczeń ukończenia modułów M1/M2/M3.")
    parser.add_argument("--apply", action="store_true", help="Zapisz pliki (default: dry-run)")
    args = parser.parse_args()
    sys.exit(build(apply=args.apply))


if __name__ == "__main__":
    main()
