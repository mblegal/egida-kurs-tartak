"""Naprawa em-dashów w M1 (PL i EN) — heurystyka 2-stopniowa.

Pass 1: nagłówek Markdown z em-dashem  '### Tytuł — podtytuł'  → '### Tytuł: podtytuł'
Pass 2: po bold + em-dash               '**Foo** — bar'         → '**Foo**: bar'
Pass 3: zwykły em-dash w zdaniu         'tekst — kontynuacja'   → 'tekst, kontynuacja'
Pass 4: em-dash bez spacji wokół        'a—b'                   → 'a, b'

Domyślnie dry-run. --apply zapisuje zmiany. --file ogranicza do 1 pliku.

Używa tylko stdlib. Czyta UTF-8, zapisuje UTF-8 z LF endings (preserve original).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
M1_LESSONS = ROOT / "content" / "M1" / "lessons"

# Regex per pass — kolejność krytyczna (od bardziej specyficznego do ogólnego)
EM = "\u2014"

# Pass 1: nagłówek Markdown — pierwszy em-dash w linii zaczynającej się od #
# Łapie '### Foo bar — baz qux' (nagłówek, em-dash poprzedzony spacją)
PASS1_RE = re.compile(r"^(#{1,6} [^\n]*?) " + EM + r" ", re.MULTILINE)
PASS1_SUB = r"\1: "

# Pass 2: po bold (`**...**`) + spacja + em-dash + spacja → bold + ': '
# Łapie '**Foo** — bar' (typowy listowy element definiujący)
PASS2_RE = re.compile(r"(\*\*[^*\n]+\*\*) " + EM + r" ")
PASS2_SUB = r"\1: "

# Pass 3: zwykły em-dash otoczony spacjami → przecinek + spacja
PASS3_RE = re.compile(r" " + EM + r" ")
PASS3_SUB = ", "

# Pass 4: em-dash bez spacji wokół (rzadki, np. liczba—liczba albo skrót)
# Wstawiamy ", " bo to bezpieczniejsze niż "-" (które samo jest złe w MD)
PASS4_RE = re.compile(EM)
PASS4_SUB = ", "


def fix_text(text: str) -> tuple[str, dict]:
    counters = {"pass1_heading": 0, "pass2_bold": 0, "pass3_inline": 0, "pass4_bare": 0}
    new_text, n1 = PASS1_RE.subn(PASS1_SUB, text)
    counters["pass1_heading"] = n1
    new_text, n2 = PASS2_RE.subn(PASS2_SUB, new_text)
    counters["pass2_bold"] = n2
    new_text, n3 = PASS3_RE.subn(PASS3_SUB, new_text)
    counters["pass3_inline"] = n3
    new_text, n4 = PASS4_RE.subn(PASS4_SUB, new_text)
    counters["pass4_bare"] = n4
    return new_text, counters


def show_diff_samples(orig: str, new: str, n: int = 8) -> None:
    """Znajdź pozycje zmian w originale (em-dash) i pokaż kontekst przed/po."""
    em_positions = [m.start() for m in re.finditer(EM, orig)]
    if not em_positions:
        return
    step = max(1, len(em_positions) // n)
    print(f"\n  Próbka {min(n, len(em_positions))} zmian (z {len(em_positions)}):\n")
    for i in range(0, len(em_positions), step):
        if i // step >= n:
            break
        pos = em_positions[i]
        s, e = max(0, pos - 50), min(len(orig), pos + 50)
        before = orig[s:e].replace("\n", " / ")

        # Zmapuj pozycję w orig na pozycję w new — przybliżenie (em → 1 char ", ")
        # Korekta: każdy poprzedni em zamienił się na 1-2 chars; szacujemy delta
        # Bezpieczniej: znajdź najbliższe odpowiadające miejsce po keywordach
        keyword_len = 20
        keyword = orig[max(0, pos - keyword_len):pos].split("\n")[-1]
        new_pos = new.find(keyword) if len(keyword) >= 8 else -1
        if new_pos >= 0:
            new_pos += len(keyword)
            s2, e2 = max(0, new_pos - 50), min(len(new), new_pos + 50)
            after = new[s2:e2].replace("\n", " / ")
        else:
            after = "(nie udało się zlokalizować)"

        print(f"  [{i+1:>3}] PRZED: ...{before}...")
        print(f"        PO:    ...{after}...")
        print()


def process_file(path: Path, apply: bool, verbose: bool = True) -> dict:
    text = path.read_text(encoding="utf-8")
    em_count_before = text.count(EM)
    new_text, counters = fix_text(text)
    em_count_after = new_text.count(EM)

    if verbose:
        rel = path.relative_to(ROOT)
        print(f"\n{'=' * 78}")
        print(f"PLIK: {rel}")
        print(f"  em-dash przed: {em_count_before}, po: {em_count_after}")
        print(f"  pass1 (nagłówek):  {counters['pass1_heading']}")
        print(f"  pass2 (po bold):   {counters['pass2_bold']}")
        print(f"  pass3 (inline):    {counters['pass3_inline']}")
        print(f"  pass4 (bez spacji):{counters['pass4_bare']}")

    if apply:
        if em_count_before > 0:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            if verbose:
                print(f"  ZAPISANO ({em_count_before} → {em_count_after} em-dashów)")
    elif verbose and em_count_before > 0:
        show_diff_samples(text, new_text, n=8)

    return {
        "path": str(path.relative_to(ROOT)),
        "em_before": em_count_before,
        "em_after": em_count_after,
        **counters,
    }


def main():
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="Faktycznie zapisz zmiany (domyślnie dry-run).")
    ap.add_argument("--file", type=str, default=None,
                    help="Pojedynczy plik (relatywnie do kurs_tartak/), np. content/M1/lessons/m1-w3-l3/pl.md")
    ap.add_argument("--langs", type=str, default="pl,en",
                    help="Języki do przetworzenia (CSV), domyślnie 'pl,en'")
    args = ap.parse_args()

    langs = args.langs.split(",")

    if args.file:
        path = ROOT / args.file
        if not path.exists():
            print(f"BRAK PLIKU: {path}", file=sys.stderr)
            sys.exit(2)
        process_file(path, apply=args.apply, verbose=True)
        return

    # Pełny przejście: wszystkie pliki M1/lessons/*/{lang}.md
    targets = []
    for lesson_dir in sorted(M1_LESSONS.iterdir()):
        if not lesson_dir.is_dir():
            continue
        for lang in langs:
            p = lesson_dir / f"{lang}.md"
            if p.exists():
                targets.append((lang, p))

    print(f"Znaleziono {len(targets)} plików M1 ({', '.join(langs)})")
    print(f"Tryb: {'APPLY (zapis)' if args.apply else 'DRY-RUN (bez zapisu)'}\n")

    totals = {"em_before": 0, "em_after": 0,
              "pass1_heading": 0, "pass2_bold": 0,
              "pass3_inline": 0, "pass4_bare": 0}
    files_with_changes = 0

    for lang, p in targets:
        result = process_file(p, apply=args.apply, verbose=False)
        if result["em_before"] > 0:
            files_with_changes += 1
            print(f"  {result['path']}  em: {result['em_before']:>4} -> {result['em_after']:>2}  "
                  f"(p1={result['pass1_heading']:>2} p2={result['pass2_bold']:>2} "
                  f"p3={result['pass3_inline']:>3} p4={result['pass4_bare']:>2})")
        for k in totals:
            totals[k] += result[k]

    print(f"\n{'=' * 78}")
    print(f"PODSUMOWANIE ({files_with_changes}/{len(targets)} plików ze zmianami):")
    print(f"  em-dash przed: {totals['em_before']}")
    print(f"  em-dash po:    {totals['em_after']}")
    print(f"  pass1 (nagłówki):       {totals['pass1_heading']}")
    print(f"  pass2 (po bold):        {totals['pass2_bold']}")
    print(f"  pass3 (inline w spacji):{totals['pass3_inline']}")
    print(f"  pass4 (bez spacji):     {totals['pass4_bare']}")

    if totals["em_after"] > 0:
        print(f"\n  UWAGA: pozostało {totals['em_after']} em-dashów po zamianach.")
        sys.exit(1)
    else:
        print(f"\n  OK: 0 em-dashów po zamianach.")


if __name__ == "__main__":
    main()
