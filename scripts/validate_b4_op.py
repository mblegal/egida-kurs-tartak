"""
validate_b4_op.py

Comprehensive validator for podprojekt-b/B4-operacyjne (operational documentation).
Checks every MD file and every DOCX template against the B-OP convention:

- YAML frontmatter present and parseable
- Mandatory frontmatter keys
- Identifier (e.g. OSK-1.0/2026) present in body
- No em-dash (U+2014) anywhere
- Polish ogonki sanity (when language is `pl`)
- Cyrillic majority for `uk` files
- Spanish ñ presence and absence of "ano" bug for `es`
- Klasa 2 placeholder consistency between MD and DOCX templates

Usage:
    python scripts/validate_b4_op.py
    python scripts/validate_b4_op.py --strict      # nonzero exit if any warning
    python scripts/validate_b4_op.py --json        # machine-readable output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
B4_ROOT = REPO_ROOT / "podprojekt-b" / "B4-operacyjne"

EM_DASH = b"\xe2\x80\x94"
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


@dataclass
class FileSpec:
    relpath: str
    languages: tuple[str, ...]
    expected_id: str
    klasa: int


@dataclass
class CheckResult:
    file: str
    ok: bool
    warnings: list[str] = field(default_factory=list)
    info: dict[str, object] = field(default_factory=dict)


KLASA_1: tuple[FileSpec, ...] = (
    FileSpec("O1-wejscie/01-oswiadczenie-kwalifikowalnosci", ("pl", "en", "es", "uk"), "OSK-1.0/2026", 1),
    FileSpec("O1-wejscie/02-test-wejsciowy", ("pl", "en", "es", "uk"), "TW-1.0/2026", 1),
    FileSpec("O1-wejscie/03-ankieta-wstepna", ("pl", "en", "es", "uk"), "AW-1.0/2026", 1),
    FileSpec("O2-realizacja/06-protokol-bhp", ("pl", "en", "es", "uk"), "PIB-1.0/2026", 1),
    FileSpec("O2-realizacja/07-rejestr-materialow", ("pl", "en", "es", "uk"), "RM-1.0/2026", 1),
    FileSpec("O3-ocena/01-quiz-uzupelniajacy-M1", ("pl", "en", "es", "uk"), "QUM-M1-1.0/2026", 1),
    FileSpec("O3-ocena/02-quiz-uzupelniajacy-M2", ("pl", "en", "es", "uk"), "QUM-M2-1.0/2026", 1),
    FileSpec("O3-ocena/03-quiz-uzupelniajacy-M3", ("pl", "en", "es", "uk"), "QUM-M3-1.0/2026", 1),
    FileSpec("O3-ocena/08-test-koncowy-kursu", ("pl", "en", "es", "uk"), "TKK-1.0/2026", 1),
    FileSpec("O3-ocena/10-sprawdzian-czastkowy-M1-T12", ("pl", "en", "es", "uk"), "SPC-M1-T12-1.0/2026", 1),
    FileSpec("O3-ocena/11-sprawdzian-czastkowy-M1-T34", ("pl", "en", "es", "uk"), "SPC-M1-T34-1.0/2026", 1),
    FileSpec("O3-ocena/18-ankieta-ewaluacyjna-uczestnika", ("pl", "en", "es", "uk"), "AEU-1.0/2026", 1),
    FileSpec("O5-incydenty/01-usprawiedliwienie-nieobecnosci", ("pl", "en", "es", "uk"), "UN-1.0/2026", 1),
    FileSpec("O5-incydenty/02-wniosek-o-powtorzenie", ("pl", "en", "es", "uk"), "WP-1.0/2026", 1),
)

KLASA_3: tuple[FileSpec, ...] = (
    FileSpec("O2-realizacja/02-dziennik-zajec", ("pl",), "DZ-1.0/2026", 3),
    FileSpec("O2-realizacja/05-konspekt-lekcji", ("pl",), "KL-1.0/2026", 3),
    FileSpec("O2-realizacja/03-lista-obecnosci-dzienna", ("pl", "en", "es", "uk"), "LO-1.0/2026", 3),
    FileSpec("O3-ocena/04-klucz-quizu-M1", ("pl",), "KOD-QUM-M1-1.0/2026", 3),
    FileSpec("O3-ocena/05-klucz-quizu-M2", ("pl",), "KOD-QUM-M2-1.0/2026", 3),
    FileSpec("O3-ocena/06-klucz-quizu-M3", ("pl",), "KOD-QUM-M3-1.0/2026", 3),
    FileSpec("O3-ocena/09-klucz-testu-koncowego", ("pl",), "KOD-TKK-1.0/2026", 3),
    FileSpec("O3-ocena/12-klucz-sprawdzianu-M1-T12", ("pl",), "KOD-SPC-M1-T12-1.0/2026", 3),
    FileSpec("O3-ocena/13-klucz-sprawdzianu-M1-T34", ("pl",), "KOD-SPC-M1-T34-1.0/2026", 3),
    FileSpec("O3-ocena/16-arkusz-oceny-instruktora", ("pl",), "AOI-1.0/2026", 3),
    FileSpec("O3-ocena/17-ankieta-ewaluacyjna-instruktora", ("pl",), "AEI-1.0/2026", 3),
)

KLASA_2: tuple[FileSpec, ...] = (
    FileSpec("O1-wejscie/04-karta-uczestnika", ("pl", "en", "es", "uk"), "KU-1.0/2026", 2),
    FileSpec("O1-wejscie/05-lista-kwalifikowanych", ("pl",), "LK-1.0/2026", 2),
    FileSpec("O2-realizacja/01-harmonogram-szczegolowy", ("pl",), "HSZ-1.0/2026", 2),
    FileSpec("O2-realizacja/04-zbiorcza-karta-obecnosci", ("pl", "en", "es", "uk"), "ZKO-1.0/2026", 2),
    FileSpec("O3-ocena/07-karta-odpowiedzi", ("pl", "en", "es", "uk"), "KO-1.0/2026", 2),
    FileSpec("O3-ocena/14-protokol-testu-koncowego", ("pl",), "PTK-1.0/2026", 2),
    FileSpec("O3-ocena/15-karta-postepow-kursanta", ("pl", "en", "es", "uk"), "KP-1.0/2026", 2),
    FileSpec("O3-ocena/19-zestawienie-zbiorcze-ocen", ("pl",), "ZZO-1.0/2026", 2),
    FileSpec("O4-zamkniecie/01-protokol-zakonczenia-kursu", ("pl",), "PZK-1.0/2026", 2),
    FileSpec("O4-zamkniecie/02-lista-absolwentow", ("pl",), "LA-1.0/2026", 2),
    FileSpec("O4-zamkniecie/03-rejestr-wydanych-zaswiadczen", ("pl",), "RWZ-1.0/2026", 2),
    FileSpec("O4-zamkniecie/04-raport-koncowy-edycji", ("pl",), "RKE-1.0/2026", 2),
    FileSpec("O4-zamkniecie/05-karta-edycji-kursu", ("pl",), "KEK-1.0/2026", 2),
    FileSpec("O4-zamkniecie/06-spis-dokumentacji-edycji", ("pl",), "SDE-1.0/2026", 2),
    FileSpec("O5-incydenty/03-skreslenie-z-listy", ("pl",), "SL-1.0/2026", 2),
    FileSpec("O5-incydenty/04-protokol-wypadku", ("pl",), "PW-1.0/2026", 2),
)

ALL_TYPES: tuple[FileSpec, ...] = KLASA_1 + KLASA_3 + KLASA_2

REQUIRED_YAML_KEYS = ("typ", "dokument", "kurs", "podprojekt", "faza", "język", "wersja", "stan-na")


def parse_yaml_frontmatter(text: str) -> tuple[dict[str, str] | None, int]:
    """Return (parsed dict of top-level keys, body_start_offset). None if no frontmatter."""
    if not text.startswith("---\n"):
        return None, 0
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, 0
    yaml_block = text[4:end]
    parsed: dict[str, str] = {}
    for line in yaml_block.split("\n"):
        match = re.match(r"^([\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ_-]+):\s*(.*)$", line)
        if match:
            parsed[match.group(1)] = match.group(2).strip()
    return parsed, end + 5


def check_md_file(path: Path, spec: FileSpec, lang: str) -> CheckResult:
    result = CheckResult(file=str(path.relative_to(B4_ROOT)), ok=True)

    if not path.exists():
        result.ok = False
        result.warnings.append("FILE MISSING")
        return result

    raw = path.read_bytes()
    text = raw.decode("utf-8")
    result.info["bytes"] = len(raw)

    em_count = raw.count(EM_DASH)
    result.info["em_dash"] = em_count
    if em_count > 0:
        result.ok = False
        result.warnings.append(f"em-dash count {em_count}")

    yaml, _ = parse_yaml_frontmatter(text)
    if yaml is None:
        result.ok = False
        result.warnings.append("YAML frontmatter missing or unparseable")
    else:
        for key in REQUIRED_YAML_KEYS:
            if key not in yaml:
                result.warnings.append(f"YAML missing key: {key}")
                result.ok = False
        if yaml.get("język") != lang:
            result.warnings.append(f"YAML język={yaml.get('język')!r} but file is {lang}")
            result.ok = False

    if spec.expected_id not in text:
        result.ok = False
        result.warnings.append(f"identifier {spec.expected_id} not found in body")

    placeholders = set(PLACEHOLDER_RE.findall(text))
    result.info["placeholders_unique"] = len(placeholders)

    if lang == "uk":
        cyrillic = sum(1 for ch in text if "Ѐ" <= ch <= "ӿ")
        latin_letters = sum(1 for ch in text if ch.isalpha() and ord(ch) < 128)
        ratio = cyrillic / max(1, cyrillic + latin_letters)
        result.info["cyrillic_ratio"] = round(ratio, 3)
        result.info["cyrillic_count"] = cyrillic
        # Hybrid lista-obecnosci-dzienna has mostly PL admin content; check
        # absolute cyrillic count instead of ratio for that specific type.
        if "lista-obecnosci-dzienna" in spec.relpath:
            if cyrillic < 200:
                result.warnings.append(
                    f"Cyrillic count {cyrillic} below minimum 200 (hybrid file)"
                )
                result.ok = False
        else:
            if ratio < 0.6:
                result.warnings.append(
                    f"Cyrillic ratio {ratio:.1%} below threshold 60%"
                )
                result.ok = False
        if "ї" not in text and "Ї" not in text:
            result.warnings.append("Ukrainian ї not found (might be Russian)")
            result.ok = False

    if lang == "es":
        if " ano " in text or " anos " in text:
            result.warnings.append("'ano' bug detected (missing tilde on año)")
            result.ok = False

    return result


def check_klasa_2_template(spec: FileSpec, lang: str, md_placeholders: set[str]) -> CheckResult:
    """Verify DOCX template exists and contains all placeholders found in MD source."""
    template_path = B4_ROOT / spec.relpath / "templates" / f"template_{lang}.docx"
    rel = str(template_path.relative_to(B4_ROOT))
    result = CheckResult(file=rel, ok=True)

    if not template_path.exists():
        result.ok = False
        result.warnings.append("DOCX template missing")
        return result

    from docx import Document  # type: ignore[import-untyped]

    doc = Document(str(template_path))
    text_blob: list[str] = []
    for paragraph in doc.paragraphs:
        text_blob.append(paragraph.text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    text_blob.append(paragraph.text)
    body = "\n".join(text_blob)
    docx_placeholders = set(PLACEHOLDER_RE.findall(body))

    missing = md_placeholders - docx_placeholders
    extra = docx_placeholders - md_placeholders

    result.info["bytes"] = template_path.stat().st_size
    result.info["placeholders_in_docx"] = len(docx_placeholders)
    result.info["placeholders_in_md"] = len(md_placeholders)

    if missing:
        result.ok = False
        result.warnings.append(f"DOCX missing placeholders from MD: {sorted(missing)}")
    if extra:
        result.warnings.append(f"DOCX has placeholders not in MD: {sorted(extra)}")

    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Nonzero exit if any warning")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args(argv)

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    results: list[CheckResult] = []

    for spec in ALL_TYPES:
        for lang in spec.languages:
            md_path = B4_ROOT / spec.relpath / f"{lang}.md"
            md_result = check_md_file(md_path, spec, lang)
            results.append(md_result)

            if spec.klasa == 2 and md_result.ok:
                md_text = md_path.read_text(encoding="utf-8")
                md_placeholders = set(PLACEHOLDER_RE.findall(md_text))
                docx_result = check_klasa_2_template(spec, lang, md_placeholders)
                results.append(docx_result)

    if args.json:
        print(
            json.dumps(
                [
                    {
                        "file": r.file,
                        "ok": r.ok,
                        "warnings": r.warnings,
                        "info": r.info,
                    }
                    for r in results
                ],
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        ok_count = sum(1 for r in results if r.ok)
        warn_count = sum(1 for r in results if not r.ok)
        print(f"validate_b4_op.py - {len(results)} checks, {ok_count} OK, {warn_count} with issues")
        print("=" * 80)
        for r in results:
            status = "OK" if r.ok else "FAIL"
            print(f"[{status}] {r.file}")
            for w in r.warnings:
                print(f"    {w}")
        print("=" * 80)
        if warn_count > 0:
            print(f"FAIL: {warn_count} files have issues")
        else:
            print("PASS: all files OK")

    return 1 if (args.strict and any(not r.ok for r in results)) else (0 if all(r.ok for r in results) else 1)


if __name__ == "__main__":
    raise SystemExit(main())
