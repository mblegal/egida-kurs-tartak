"""
sync_heroes.py — synchronizacja bohaterów narracyjnych w content/ kursu tartakowego.

Zamienia stare imiona (Hai/Maricel/Emeka/Rustam/Wahan/Bekzod/Oleksii/Wacław)
na profile ukr+kolumbijskie zgodnie z rzeczywistym profilem beneficjentów
Fundacji EGIDA (Ukraińcy 45-55%, Kolumbijczycy 15-25%).

Użycie:
    python scripts/sync_heroes.py             # dry-run, tylko raport
    python scripts/sync_heroes.py --apply     # apply + raport

Raport: scripts/sync_heroes_report.md
"""
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
REPORT = Path(__file__).resolve().parent / "sync_heroes_report.md"

# Kolejność ma znaczenie: pełne nazwiska PRZED skrótowymi, deklinacje PRZED mianownikiem.
MAPPING = [
    (r"\bHai Nguyen\b",         "Andrij Tkaczenko"),
    (r"\bOleksij Tarasenko\b",  "Bohdan Szewczenko"),
    (r"\bRustam Karimov\b",     "Mykoła Hrycenko"),
    (r"\bWahan Petrosjan\b",    "Wasyl Melnyk"),
    # Hai + polskie deklinacje → Andrij + deklinacje
    (r"\bHaiowi\b",             "Andrijowi"),
    (r"\bHaiem\b",              "Andrijem"),
    (r"\bHaiu\b",               "Andriju"),
    (r"\bHaia\b",               "Andrija"),
    (r"\bHai\b",                "Andrij"),
    (r"\bMaricel\b",            "Sofía"),
    (r"\bEmeka\b",              "Carlos"),
    # Rustam + deklinacje → Mykoła + deklinacje (Mykoła odmienia się jak rzecz. żeński -a)
    (r"\bRustamowi\b",          "Mykole"),
    (r"\bRustamem\b",           "Mykołą"),
    (r"\bRustamie\b",           "Mykole"),
    (r"\bRustama\b",            "Mykoły"),
    (r"\bRustam\b",             "Mykoła"),
    # Wahan + deklinacje → Wasyl + deklinacje
    (r"\bWahanowi\b",           "Wasylowi"),
    (r"\bWahanem\b",            "Wasylem"),
    (r"\bWahanie\b",            "Wasylu"),
    (r"\bWahana\b",             "Wasyla"),
    (r"\bWahan\b",              "Wasyl"),
    # Bekzod → Diego (hiszp. nieodmienne: wszystkie przypadki → "Diego")
    (r"\bBekzodowi\b",          "Diego"),
    (r"\bBekzodem\b",           "Diego"),
    (r"\bBekzodzie\b",          "Diego"),
    (r"\bBekzoda\b",            "Diego"),
    (r"\bBekzod\b",             "Diego"),
    # Oleksii (EN translit.) + odmiany PL → Oleksij + odmiany PL
    (r"\bOleksiiemu\b",         "Oleksijowi"),
    (r"\bOleksiiego\b",         "Oleksija"),
    (r"\bOleksiim\b",           "Oleksijem"),
    (r"\bOleksiia\b",            "Oleksija"),
    (r"\bOleksii\b",            "Oleksij"),
    (r"\bWacław\b",             "Mychajło"),
]

# Drugi przebieg: poprawki biernikowe dla Mykoły (PL deklinacja żeńska -a
# ma rozróżnienie dop. `Mykoły` vs bier. `Mykołę`, podczas gdy źródłowy Rustam
# je zrównywał). Zamieniamy tylko w jednoznacznych kontekstach akuzatywnych.
MAPPING_ACCUSATIVE = [
    (r"\b(na|przez|za|pod|nad|poprzez|w) Mykoły\b",                                  r"\1 Mykołę"),
    (r"\b(widzi|widzial|widział|zobaczył|zobaczyła|patrzy na|patrzyl na|patrzył na|spogląda na|spojrzał na|zerka na|zerknął na|zaprasza|zaprosił|chwali|chwalił|pochwalił|atakuje|zaatakował|obserwuje|obserwował|sprawdza|sprawdzał|zauważa|zauważył|uczy|egzaminuje|ocenia|ocenił|krytykuje|skrytykował|prowadzi|prowadził|wspiera|wspierał|zabezpiecza|zabezpieczał|lubi|lubił|woła|zawołał|wzywa|wezwał|zna|znał|pyta|zapyta|zapytał|mianuje|mianował|wybiera|wybrał|szuka|znajduje|znalazł) Mykoły\b", r"\1 Mykołę"),
]

def apply_accusative(text: str) -> tuple[str, Counter]:
    counts = Counter()
    for pattern, replacement in MAPPING_ACCUSATIVE:
        new_text, n = re.subn(pattern, replacement, text)
        if n:
            counts[pattern] = n
        text = new_text
    return text, counts

# Scope M3-only: w tych plikach każdy Oleksij* odnosi się do Oleksija Tarasenki
# (epizodyczny bohater M3 w4), który został zmieniony na Bohdana Szewczenkę.
# W M2 Oleksij = Oleksij Bondarenko/Charków — zostaje.
M3_OLEKSIJ_FILES = {
    "M3/lessons/m3-w4-l4/en.md", "M3/lessons/m3-w4-l4/es.md", "M3/lessons/m3-w4-l4/pl.md",
    "M3/lessons/m3-w4-l5/en.md", "M3/lessons/m3-w4-l5/es.md", "M3/lessons/m3-w4-l5/pl.md", "M3/lessons/m3-w4-l5/uk.md",
    "M3/artifacts/quiz-uzupelniajacy/en.md", "M3/artifacts/quiz-uzupelniajacy/es.md", "M3/artifacts/quiz-uzupelniajacy/pl.md",
    "M3/artifacts/scenariusze-praktyczne/pl.md",
}

MAPPING_M3_OLEKSIJ = [
    # Pełne nazwisko w deklinacji (najpierw, dłuższe patterny)
    (r"\bOleksija Tarasenki\b",     "Bohdana Szewczenki"),
    (r"\bOleksijem Tarasenką\b",    "Bohdanem Szewczenką"),
    (r"\bOleksijowi Tarasence\b",   "Bohdanowi Szewczence"),
    (r"\bOleksiju Tarasence\b",     "Bohdanie Szewczence"),
    # Samo imię (epizod M3 w4: Oleksij = Tarasenko = Bohdan)
    (r"\bOleksijowi\b",             "Bohdanowi"),
    (r"\bOleksijem\b",              "Bohdanem"),
    (r"\bOleksija\b",               "Bohdana"),
    (r"\bOleksiju\b",               "Bohdanie"),
    (r"\bOleksij\b",                "Bohdan"),
]

def apply_m3_scope(path: Path, text: str) -> tuple[str, Counter]:
    counts = Counter()
    rel = path.relative_to(CONTENT.parent / "content").as_posix()
    if rel not in M3_OLEKSIJ_FILES:
        return text, counts
    for pattern, replacement in MAPPING_M3_OLEKSIJ:
        new_text, n = re.subn(pattern, replacement, text)
        if n:
            counts[pattern] = n
        text = new_text
    return text, counts

def apply_mapping(text: str) -> tuple[str, Counter]:
    counts = Counter()
    for pattern, replacement in MAPPING:
        new_text, n = re.subn(pattern, replacement, text)
        if n:
            counts[pattern] = n
        text = new_text
    return text, counts

def main():
    apply = "--apply" in sys.argv
    files = sorted(CONTENT.rglob("*.md"))
    per_file: list[tuple[Path, Counter]] = []
    global_counts: Counter = Counter()
    touched = 0

    for path in files:
        original = path.read_text(encoding="utf-8")
        new_text, counts = apply_mapping(original)
        new_text, acc_counts = apply_accusative(new_text)
        counts.update(acc_counts)
        new_text, m3_counts = apply_m3_scope(path, new_text)
        counts.update(m3_counts)
        if counts:
            touched += 1
            per_file.append((path, counts))
            global_counts.update(counts)
            if apply:
                path.write_text(new_text, encoding="utf-8")

    lines = []
    mode = "APPLY" if apply else "DRY-RUN"
    lines.append(f"# sync_heroes report — {mode}")
    lines.append("")
    lines.append(f"Scan: {len(files)} plików w `content/`")
    lines.append(f"Touched: **{touched} plików**")
    lines.append(f"Total replacements: **{sum(global_counts.values())}**")
    lines.append("")
    lines.append("## Summary per pattern")
    lines.append("")
    lines.append("| # | Pattern | → | Count |")
    lines.append("|---|---------|---|-------|")
    for i, (pattern, replacement) in enumerate(MAPPING, 1):
        n = global_counts.get(pattern, 0)
        lines.append(f"| {i} | `{pattern}` | `{replacement}` | {n} |")
    lines.append("")
    lines.append("## Per-file breakdown")
    lines.append("")
    lines.append("| Plik | Zamiany |")
    lines.append("|------|---------|")
    for path, counts in per_file:
        rel = path.relative_to(ROOT).as_posix()
        summary = ", ".join(f"{p}:{n}" for p, n in counts.items())
        lines.append(f"| `{rel}` | {summary} |")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[{mode}] touched={touched}/{len(files)} total_replacements={sum(global_counts.values())}")
    print(f"Report: {REPORT.relative_to(ROOT).as_posix()}")

if __name__ == "__main__":
    main()
