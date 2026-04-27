"""
b4_op_generate.py

Fills DOCX templates from B4-operacyjne klasa 2 with values from a CSV data file.
Each CSV row produces one filled DOCX (e.g., one Karta Uczestnika per Kursant).

Placeholders in the template are matched against CSV column headers by uppercase
name. Example: column header `IMIE_KURSANTA` in CSV substitutes `{{IMIE_KURSANTA}}`
in template.

Usage:
    python scripts/b4_op_generate.py --typ karta-uczestnika --lang pl \\
        --csv data/edycja_C1_2026_kursanci.csv --output-dir dist/edycja_C1_2026/

    python scripts/b4_op_generate.py --list-types

Output:
    <output-dir>/<typ>_<row-id>_<lang>.docx (per CSV row)
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
B4_ROOT = REPO_ROOT / "podprojekt-b" / "B4-operacyjne"


@dataclass(frozen=True)
class TypeConfig:
    slug: str
    typ_path: str
    languages: tuple[str, ...]
    row_id_field: str
    expected_placeholders: tuple[str, ...] = field(default=())

    def template_path(self, lang: str) -> Path:
        return B4_ROOT / self.typ_path / "templates" / f"template_{lang}.docx"


TYPE_CONFIGS: dict[str, TypeConfig] = {
    "karta-uczestnika": TypeConfig(
        slug="karta-uczestnika",
        typ_path="O1-wejscie/04-karta-uczestnika",
        languages=("pl", "en", "es", "uk"),
        row_id_field="NR_KARTY",
        expected_placeholders=(
            "IMIE_KURSANTA", "NAZWISKO_KURSANTA", "DATA_URODZENIA", "OBYWATELSTWO",
            "JEZYK_PIERWSZY", "NR_FORMULARZA", "NR_OSWIADCZENIA_KWALIFIKOWALNOSCI",
            "NR_TESTU_WEJSCIOWEGO", "NR_ANKIETY_WSTEPNEJ", "NR_UMOWY_KURSU",
            "CYKL_KURSU", "MODUL_GLOWNY", "DATA_OTWARCIA_KARTY",
            "KOORDYNATOR_KURSU", "NR_KARTY",
        ),
    ),
    "lista-kwalifikowanych": TypeConfig(
        slug="lista-kwalifikowanych",
        typ_path="O1-wejscie/05-lista-kwalifikowanych",
        languages=("pl",),
        row_id_field="NR_LISTY",
        expected_placeholders=(
            "CYKL_KURSU", "DATA_OTWARCIA_LISTY", "DATA_ZAMKNIECIA_LISTY",
            "LIMIT_MIEJSC_CYKLU", "KOORDYNATOR_KURSU", "NR_LISTY",
        ),
    ),
    "harmonogram-szczegolowy": TypeConfig(
        slug="harmonogram-szczegolowy",
        typ_path="O2-realizacja/01-harmonogram-szczegolowy",
        languages=("pl",),
        row_id_field="NR_HARMONOGRAMU",
        expected_placeholders=(
            "CYKL_KURSU", "DATA_ROZPOCZECIA_CYKLU", "DATA_ZAKONCZENIA_CYKLU",
            "LICZBA_SESJI_M1", "LICZBA_SESJI_M2", "LICZBA_SESJI_M3",
            "LACZNA_LICZBA_GODZIN", "KOORDYNATOR_KURSU", "GLOWNE_MIEJSCE_ZAJEC",
            "NR_HARMONOGRAMU",
        ),
    ),
    "zbiorcza-karta-obecnosci": TypeConfig(
        slug="zbiorcza-karta-obecnosci",
        typ_path="O2-realizacja/04-zbiorcza-karta-obecnosci",
        languages=("pl", "en", "es", "uk"),
        row_id_field="NR_KARTY_OBECNOSCI",
        expected_placeholders=(
            "IMIE_KURSANTA", "NAZWISKO_KURSANTA", "NR_KARTY_UCZESTNIKA",
            "NR_FORMULARZA", "CYKL_KURSU", "MODUL_GLOWNY",
            "DATA_OTWARCIA_KARTY", "DATA_ZAMKNIECIA_KARTY",
            "LACZNA_LICZBA_SESJI", "LICZBA_SESJI_OBECNYCH",
            "FREKWENCJA_PROCENTOWA", "PROG_FREKWENCJI_REGULAMIN",
            "DECYZJA_DOPUSZCZENIA", "KOORDYNATOR_KURSU", "NR_KARTY_OBECNOSCI",
        ),
    ),
    "karta-odpowiedzi": TypeConfig(
        slug="karta-odpowiedzi",
        typ_path="O3-ocena/07-karta-odpowiedzi",
        languages=("pl", "en", "es", "uk"),
        row_id_field="NR_KARTY",
        expected_placeholders=(
            "IMIE_KURSANTA", "NAZWISKO_KURSANTA", "NR_KARTY",
            "KOD_QUIZU", "NUMER_MODULU", "TRYB_QUIZU", "DATA_QUIZU",
            "CYKL_KURSU", "KOORDYNATOR_KURSU",
            "LICZBA_ZAMKNIETYCH", "LICZBA_OTWARTYCH", "LICZBA_CASEOW",
            "CZAS_TRWANIA_MIN",
        ),
    ),
    "protokol-testu-koncowego": TypeConfig(
        slug="protokol-testu-koncowego",
        typ_path="O3-ocena/14-protokol-testu-koncowego",
        languages=("pl",),
        row_id_field="NR_PROTOKOLU",
        expected_placeholders=(
            "IMIE_KURSANTA", "NAZWISKO_KURSANTA", "NR_KARTY_UCZESTNIKA",
            "CYKL_KURSU", "DATA_TESTU", "NR_TESTU", "INSTRUKTOR",
            "KOORDYNATOR_KURSU", "WYNIK_CZESC_1", "WYNIK_CZESC_2",
            "WYNIK_CZESC_3", "WYNIK_LACZNY", "PROCENT_LACZNY", "DECYZJA",
            "UWAGI_INSTRUKTORA", "NR_PROTOKOLU",
        ),
    ),
    "karta-postepow-kursanta": TypeConfig(
        slug="karta-postepow-kursanta",
        typ_path="O3-ocena/15-karta-postepow-kursanta",
        languages=("pl", "en", "es", "uk"),
        row_id_field="NR_KARTY_POSTEPOW",
        expected_placeholders=(
            "IMIE_KURSANTA", "NAZWISKO_KURSANTA", "NR_KARTY_UCZESTNIKA",
            "CYKL_KURSU", "DATA_GENERACJI",
            "WYNIK_SPC_M1_T12", "WYNIK_SPC_M1_T34",
            "WYNIK_QUM_M1", "TRYB_QUM_M1",
            "WYNIK_QUM_M2", "TRYB_QUM_M2",
            "WYNIK_QUM_M3", "TRYB_QUM_M3",
            "WYNIK_TEST_M1", "WYNIK_TEST_M2", "WYNIK_TEST_M3",
            "WYNIK_TKK", "DECYZJA_TKK",
            "KOMENTARZ_INSTRUKTORA", "INSTRUKTOR", "KOORDYNATOR_KURSU",
            "NR_KARTY_POSTEPOW",
        ),
    ),
}


def replace_placeholders_in_paragraph(paragraph, mapping: dict[str, str]) -> None:
    """Replace {{KEY}} occurrences in a python-docx paragraph, preserving runs.

    The naive approach (replace in run.text) loses formatting if a placeholder
    spans multiple runs. We rebuild the paragraph text first, then check if any
    placeholder is present, and if so, do the replacement in concatenated runs.
    """
    full_text = paragraph.text
    if "{{" not in full_text:
        return

    new_text = full_text
    for key, value in mapping.items():
        token = "{{" + key + "}}"
        if token in new_text:
            new_text = new_text.replace(token, value)

    if new_text == full_text:
        return

    # Replace by clearing all runs except the first, then setting the first run text.
    # This loses inline formatting (bold/italic per run), but our templates have
    # uniform formatting per cell so this is acceptable for v1.
    if not paragraph.runs:
        return
    first_run = paragraph.runs[0]
    first_run.text = new_text
    for run in paragraph.runs[1:]:
        run.text = ""


def replace_placeholders_in_doc(doc, mapping: dict[str, str]) -> None:
    for paragraph in doc.paragraphs:
        replace_placeholders_in_paragraph(paragraph, mapping)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    replace_placeholders_in_paragraph(paragraph, mapping)


def load_csv_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return [{k: (v or "").strip() for k, v in row.items()} for row in reader]


def find_remaining_placeholders(doc) -> set[str]:
    text_blob: list[str] = []
    for paragraph in doc.paragraphs:
        text_blob.append(paragraph.text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    text_blob.append(paragraph.text)
    return set(re.findall(r"\{\{[A-Z0-9_]+\}\}", "\n".join(text_blob)))


def generate_for_type(
    typ_slug: str,
    lang: str,
    csv_path: Path,
    output_dir: Path,
    strict: bool,
) -> tuple[int, list[str]]:
    from docx import Document  # type: ignore[import-untyped]

    config = TYPE_CONFIGS[typ_slug]
    if lang not in config.languages:
        raise ValueError(
            f"Type '{typ_slug}' does not support language '{lang}'. "
            f"Supported: {config.languages}"
        )

    template_path = config.template_path(lang)
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    rows = load_csv_rows(csv_path)
    if not rows:
        return 0, [f"CSV {csv_path} contains no data rows"]

    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files: list[str] = []
    issues: list[str] = []

    for index, row in enumerate(rows, start=1):
        row_id_raw = row.get(config.row_id_field, "")
        row_id = re.sub(r"[^A-Za-z0-9_-]", "-", row_id_raw) or f"row{index:03d}"

        document = Document(str(template_path))
        replace_placeholders_in_doc(document, row)

        remaining = find_remaining_placeholders(document)
        if remaining and strict:
            issues.append(
                f"Row {index} ({row_id}): unfilled placeholders {remaining}"
            )
            continue

        output_filename = f"{config.slug}_{row_id}_{lang}.docx"
        output_path = output_dir / output_filename
        document.save(str(output_path))
        generated_files.append(str(output_path.name))

    return len(generated_files), issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--typ", choices=sorted(TYPE_CONFIGS.keys()), help="Document type slug")
    parser.add_argument("--lang", help="Language code (pl, en, es, uk)")
    parser.add_argument("--csv", type=Path, help="Path to CSV with data rows")
    parser.add_argument("--output-dir", type=Path, help="Output directory for filled DOCX")
    parser.add_argument("--list-types", action="store_true", help="List supported types and exit")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any placeholder remains unfilled after substitution",
    )

    args = parser.parse_args(argv)

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    if args.list_types:
        print("Supported types:")
        for slug, config in sorted(TYPE_CONFIGS.items()):
            print(
                f"  {slug:<28} languages={','.join(config.languages):<14} "
                f"row-id={config.row_id_field}"
            )
        return 0

    missing_args = [name for name in ("typ", "lang", "csv", "output_dir") if getattr(args, name) is None]
    if missing_args:
        parser.error(f"Missing required arguments: {', '.join(missing_args)}")

    try:
        count, issues = generate_for_type(args.typ, args.lang, args.csv, args.output_dir, args.strict)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Generated {count} DOCX file(s) in {args.output_dir}")
    if issues:
        print(f"ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"  {issue}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
