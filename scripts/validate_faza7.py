"""Walidacja Fazy 7 — read-only audyt typograficzny i merytoryczny.

Skanuje:
- 384 plików lekcji w content/M{1,2,3}/lessons/m{1,2,3}-w{1..4}-l{1..8}/{en,es,pl,uk}.md
- artefakty trenerskie w content/M{1,2,3}/artifacts/{cwiczenia,quiz,scenariusze,wytyczne}/*.md
- 10 plików materiały-pomocnicze (potwierdzenie Fazy 5)
- 6 plików dist/kurs_M{1,2,3}.html i dist/prezentacja_M{1,2,3}.html (sanity)

Wykrywa (per kategoria liczy znaleziska):
1. em-dash U+2014 (zakaz globalny)
2. en-dash U+2013 (z kontekstem — łapie typograficzne, ignoruje numeryczne zakresy
   typu '08:00–10:00', '15–20', '2026–2027' opcjonalnie)
3. apostrof typograficzny U+2019 w plikach UK
4. waluta: ASCII `zl`, `PLN` (wszędzie zakazane), `zł` (wymagane w PL)
5. halucynowane narodowości / imiona z prehistorii bohaterów
6. brak PL diakrytyków (heurystyka: standalone 'bedzie/moze/wiec/...' w pl.md)
7. frontmatter YAML + 'język: <lang>' (zgodnie z konwencją z verify_faza5)

Output: raport tekstowy z licznikami per moduł/jęz + lista znalezisk top-N + exit code.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"

LANGS = ["pl", "en", "es", "uk"]
MODULES = ["M1", "M2", "M3"]
WEEKS = [1, 2, 3, 4]
LESSONS = list(range(1, 9))

# 1. Halucynowane / wymienione narodowości i imiona (rezultat sync_heroes
#    Fazy 2A/2B). Wystąpienie któregokolwiek = regresja.
# UWAGA: zachowani nazwani bohaterowie (intencjonalnie pozostawieni przez
# user w P2#1): Siarhei (Białorusin z Grodna), Oleh, Andrei, Ion Popa,
# Murat Kaya. Ich obecność w lekcjach NIE jest błędem.
# Generyczne nazwy narodowości używamy z word-boundary regex, żeby
# 'Uzbek' nie łapało 'Uzbekistan' (kraj pochodzenia jest legalny w prospekcie).
FORBIDDEN_HEROES = [
    # Imiona-nazwiska z prehistorii (zamienione na ukr+kol)
    "Hai Nguyen", "Hai Nguyena", "Hai Nguyenowi", "Hai Nguyenem",
    "Maricel ", "Maricela",
    "Emeka ", "Emeki", "Emece",
    "Rustam Karimov", "Rustama Karimova", "Rustamem Karimovem",
    "Wahan Petrosjan", "Wahana Petrosjana", "Petrosjan", "Petrosyan",
    "Bekzod", "Bekzoda", "Bekzodem",
    "Mykoła Nazarov", "Nazarov",
    "Andrij Wietnamczyk", "Sofía Santos", "Sofia Santos",
    "Carlos Okonkwo", "Pangasinan", "Enugu",
    # Geografia spoza scope (zamieniona)
    "Tadżykistan", "Duszanbe", "Dagestan",
]

# Generyczne narodowości — z word-boundary, żeby nie łapać nazw krajów
# (Uzbekistan, Białoruś), oraz z wyjątkami nazwanych bohaterów obok.
FORBIDDEN_NATIONALITIES_WB = [
    r"Wietnamczyk\w*",
    r"Filip[iń]ńczyk\w*", r"Filipinczyk\w*",
    r"Nigeryjczyk\w*",
    r"Tadżyk\w*",
    r"Uzbek\w{0,3}\b(?!istan)",   # Uzbek/Uzbeka/Uzbeków, nie Uzbekistan
    r"Ormian[ai]n?\w*",
    r"Białorusin\w*(?!\s+(Siarhei|Oleh|Andrei))",  # nie Siarhei/Oleh/Andrei
    r"Senegalczyk\w*", r"Ghańczyk\w*", r"Irańczyk\w*", r"Gruzin\w*",
]
# Nazwani bohaterowie do WYKLUCZENIA z wszelkich match (intencjonalni)
NAMED_HEROES_OK = ["Siarhei", "Oleh", "Andrei", "Ion Popa", "Murat Kaya"]

# 2. Heurystyka: PL słowa bez diakrytyków (najczęstsze formy bezosobowe).
# Tylko w pl.md. \b zapewnia standalone. Case-sensitive (lowercase only),
# żeby uppercase-owe kody systemowe (ZLE-2026) nie były false-positive.
PL_NO_DIACRITICS = [
    r"\bbedzie\b", r"\bbedziesz\b", r"\bbedziemy\b", r"\bbedziecie\b",
    r"\bmoze\b", r"\bmozesz\b", r"\bmozemy\b", r"\bmozecie\b", r"\bmozliwe\b",
    r"\bwiec\b", r"\bwiekszy\b", r"\bwiecej\b",
    r"\bktory\b", r"\bktora\b", r"\bktore\b", r"\bktorego\b", r"\bktorym\b",
    r"\bbyc\b", r"\brobic\b", r"\bpisac\b", r"\bczytac\b",
    r"\bzeby\b", r"\bjuz\b", r"\bzrobic\b",
    r"\bczesto\b", r"\bczestosc\b",
    r"\browniez\b",
    r"\bzrodlo\b", r"\bzle\b", r"\bpozno\b",
    r"\bglowny\b", r"\bglowna\b", r"\bglowne\b",
]

# 3. en-dash kontekstowy: ignoruj zakresy numeryczne (godziny, lata, liczby).
# Wszystko inne = typograficzne i powinno być półpauzą lub przecinkiem.
EN_DASH_NUMERIC = re.compile(r"\d+(?::\d+)?\s*\u2013\s*\d+(?::\d+)?")


def find_en_dash_typographic(text: str) -> list[str]:
    """Zwraca listę kontekstów (±20 znaków) typograficznych en-dashów."""
    contexts = []
    for m in re.finditer(r"\u2013", text):
        start, end = max(0, m.start() - 20), min(len(text), m.end() + 20)
        ctx = text[start:end].replace("\n", " ")
        # Sprawdź czy to numeryczny zakres
        if EN_DASH_NUMERIC.search(text[max(0, m.start() - 6):min(len(text), m.end() + 6)]):
            continue
        contexts.append(ctx)
    return contexts


def find_em_dash(text: str) -> int:
    return text.count("\u2014")


def check_frontmatter(text: str, expected_lang: str) -> tuple[bool, bool]:
    fm_match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        return False, False
    head = text[:600]
    has_lang = (f"język: {expected_lang}" in head) or (f"language: {expected_lang}" in head)
    return True, has_lang


def scan_file(path: Path, lang: str, category: str) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": str(e), "path": str(path)}

    findings = {
        "path": str(path.relative_to(ROOT)),
        "lang": lang,
        "category": category,
        "words": len(text.split()),
        "em_dash": find_em_dash(text),
        "en_dash_typo": len(find_en_dash_typographic(text)),
        "en_dash_typo_examples": find_en_dash_typographic(text)[:3],
        "zl_ascii": len(re.findall(r"\bzl\b", text)),
        # PLN: tylko w pl.md zakazane. W EN/ES/UK kod ISO jest poprawny.
        "pln": (text.count("PLN") if lang == "pl" else 0),
        "zl_proper": text.count("zł"),
        "uk_apo": text.count("\u2019") if lang == "uk" else 0,
        "forbidden_heroes": [],
        "pl_no_diacritics": [],
    }

    # Forbidden heroes — sprawdzamy substringi, ale wykluczamy nazwanych bohaterów
    # i nazwy krajów (przez generic regex z word-boundary).
    for hero in FORBIDDEN_HEROES:
        cnt = text.count(hero)
        if cnt > 0:
            findings["forbidden_heroes"].append((hero, cnt))
    for pat in FORBIDDEN_NATIONALITIES_WB:
        for m in re.finditer(pat, text):
            # Wyklucz jeśli najbliższy kontekst zawiera nazwanego bohatera
            window = text[max(0, m.start()-30):min(len(text), m.end()+30)]
            if any(h in window for h in NAMED_HEROES_OK):
                continue
            findings["forbidden_heroes"].append((m.group(0), 1))

    # PL diacritics tylko w pl.md; case-sensitive (lowercase patterns)
    if lang == "pl":
        for pat in PL_NO_DIACRITICS:
            for m in re.finditer(pat, text):  # bez IGNORECASE
                findings["pl_no_diacritics"].append(m.group(0))

    # Frontmatter (tylko dla .md)
    if path.suffix == ".md":
        fm_ok, lang_ok = check_frontmatter(text, lang)
        findings["fm_ok"] = fm_ok
        findings["lang_in_fm"] = lang_ok

    return findings


def main():
    # Wymuś UTF-8 na stdout (Windows cp1250 wywala się na ×, ✓, etc.)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    all_findings = []
    counters = defaultdict(int)

    # 1. LEKCJE: content/M{1,2,3}/lessons/m{X}-w{Y}-l{Z}/{lang}.md
    print("Skanowanie lekcji...", file=sys.stderr)
    for mod in MODULES:
        mod_num = mod[1]
        for w in WEEKS:
            for l in LESSONS:
                lesson_dir = CONTENT / mod / "lessons" / f"m{mod_num}-w{w}-l{l}"
                if not lesson_dir.exists():
                    counters["missing_lessons"] += 1
                    all_findings.append({"category": "MISSING", "path": str(lesson_dir.relative_to(ROOT))})
                    continue
                for lang in LANGS:
                    p = lesson_dir / f"{lang}.md"
                    if not p.exists():
                        counters["missing_lang_files"] += 1
                        all_findings.append({"category": "MISSING_LANG", "path": str(p.relative_to(ROOT))})
                        continue
                    f = scan_file(p, lang, f"lesson-{mod}")
                    all_findings.append(f)
                    counters["scanned_lessons"] += 1

    # 2. ARTEFAKTY trenerskie
    print("Skanowanie artefaktów...", file=sys.stderr)
    for mod in MODULES:
        artifacts_dir = CONTENT / mod / "artifacts"
        if not artifacts_dir.exists():
            continue
        for art_type in ["cwiczenia-teoretyczne", "quiz-uzupelniajacy",
                         "scenariusze-praktyczne", "wytyczne-trenera"]:
            art_dir = artifacts_dir / art_type
            if not art_dir.exists():
                continue
            for md_file in sorted(art_dir.glob("*.md")):
                lang = md_file.stem  # 'pl', 'en', 'es', 'uk'
                if lang not in LANGS:
                    continue
                f = scan_file(md_file, lang, f"artifact-{mod}-{art_type}")
                all_findings.append(f)
                counters["scanned_artifacts"] += 1

    # 3. MATERIAŁY POMOCNICZE (powtórka Fazy 5)
    print("Skanowanie materiałów pomocniczych...", file=sys.stderr)
    pomoc_base = CONTENT / "materialy-pomocnicze"
    for folder in pomoc_base.iterdir():
        if not folder.is_dir():
            continue
        for md_file in sorted(folder.glob("*.md")):
            lang = md_file.stem
            if lang not in LANGS:
                continue
            f = scan_file(md_file, lang, f"pomocnicze-{folder.name}")
            all_findings.append(f)
            counters["scanned_pomocnicze"] += 1

    # 4. DIST (sanity)
    print("Skanowanie dist/...", file=sys.stderr)
    dist_findings = []
    for html in sorted(DIST.glob("*.html")):
        size = html.stat().st_size
        text = html.read_text(encoding="utf-8")
        # Podstawowe sanity: rozmiar, brak placeholderów typu '{{...}}', brak '[BRAK]'
        placeholders = len(re.findall(r"\{\{[A-Z_]+\}\}", text))
        brak = text.count("[BRAK]") + text.count("[TODO]") + text.count("[FIXME]")
        em = text.count("\u2014")
        en_typo = len(find_en_dash_typographic(text))
        dist_findings.append({
            "file": html.name, "size_kb": size // 1024,
            "placeholders": placeholders, "brak_markers": brak,
            "em_dash": em, "en_dash_typo": en_typo,
        })

    # ============= AGREGATY =============
    by_category = defaultdict(lambda: {
        "files": 0, "em": 0, "en_typo": 0, "zl_ascii": 0, "pln": 0,
        "uk_apo": 0, "heroes": 0, "no_diacr": 0, "fm_missing": 0,
    })

    issues_top = []  # lista (count, file, type, sample)

    for f in all_findings:
        cat = f.get("category", "UNKNOWN")
        if cat in ("MISSING", "MISSING_LANG"):
            continue
        if "error" in f:
            continue
        by_category[cat]["files"] += 1
        by_category[cat]["em"] += f.get("em_dash", 0)
        by_category[cat]["en_typo"] += f.get("en_dash_typo", 0)
        by_category[cat]["zl_ascii"] += f.get("zl_ascii", 0)
        by_category[cat]["pln"] += f.get("pln", 0)
        by_category[cat]["uk_apo"] += f.get("uk_apo", 0)
        by_category[cat]["heroes"] += sum(c for _, c in f.get("forbidden_heroes", []))
        by_category[cat]["no_diacr"] += len(f.get("pl_no_diacritics", []))
        if not f.get("fm_ok", True):
            by_category[cat]["fm_missing"] += 1

        if f.get("em_dash", 0) > 0:
            issues_top.append((f["em_dash"], f["path"], "em-dash", ""))
        if f.get("en_dash_typo", 0) > 0:
            ex = f.get("en_dash_typo_examples", [])
            issues_top.append((f["en_dash_typo"], f["path"], "en-dash-typo",
                               " | ".join(ex[:2])))
        if f.get("zl_ascii", 0) > 0:
            issues_top.append((f["zl_ascii"], f["path"], "zl-ascii", ""))
        if f.get("pln", 0) > 0:
            issues_top.append((f["pln"], f["path"], "PLN", ""))
        if f.get("uk_apo", 0) > 0:
            issues_top.append((f["uk_apo"], f["path"], "uk-apostrophe", ""))
        for hero, cnt in f.get("forbidden_heroes", []):
            issues_top.append((cnt, f["path"], f"hero:{hero}", ""))
        for word in f.get("pl_no_diacritics", []):
            issues_top.append((1, f["path"], f"no-diacr:{word}", ""))

    # ============= RAPORT =============
    print("=" * 78)
    print("RAPORT WALIDACJI FAZY 7 — KURS TARTAKOWY")
    print("=" * 78)
    print()
    print("STAN SKANU:")
    print(f"  Lekcje sklanowane: {counters['scanned_lessons']} / 384 oczekiwanych")
    print(f"  Artefakty: {counters['scanned_artifacts']}")
    print(f"  Materiały pomocnicze: {counters['scanned_pomocnicze']}")
    print(f"  Brakujące lekcje (folder): {counters['missing_lessons']}")
    print(f"  Brakujące pliki językowe: {counters['missing_lang_files']}")
    print()

    print("AGREGATY PER KATEGORIA:")
    print(f"  {'kategoria':<35} {'plików':>7} {'em':>5} {'en_typo':>8} {'zl_asc':>7} {'PLN':>5} {'uk_apo':>7} {'heroes':>7} {'no_dia':>7} {'fm_miss':>8}")
    for cat in sorted(by_category):
        c = by_category[cat]
        print(f"  {cat:<35} {c['files']:>7} {c['em']:>5} {c['en_typo']:>8} {c['zl_ascii']:>7} {c['pln']:>5} {c['uk_apo']:>7} {c['heroes']:>7} {c['no_diacr']:>7} {c['fm_missing']:>8}")
    print()

    print("DIST/ SANITY:")
    for d in dist_findings:
        flag = "OK" if (d["placeholders"] == 0 and d["brak_markers"] == 0 and d["size_kb"] > 50) else "WARN"
        print(f"  {d['file']:<28} {d['size_kb']:>6} KB  placeholders={d['placeholders']:>2}  brak={d['brak_markers']:>2}  em={d['em_dash']:>3}  en_typo={d['en_dash_typo']:>3}  [{flag}]")
    print()

    if issues_top:
        # Sort by count desc, top 30
        issues_top.sort(key=lambda x: -x[0])
        print(f"TOP {min(30, len(issues_top))} ZNALEZISK (z {len(issues_top)} łącznie):")
        for count, path, typ, sample in issues_top[:30]:
            sample_str = f"  [{sample[:40]}]" if sample else ""
            print(f"  {count:>4}x {typ:<28} {path}{sample_str}")
        print()

    # Verdict
    total_blocking = sum(
        c["em"] + c["zl_ascii"] + c["pln"] + c["uk_apo"] + c["heroes"]
        for c in by_category.values()
    )
    total_warnings = sum(
        c["en_typo"] + c["no_diacr"] + c["fm_missing"]
        for c in by_category.values()
    )

    print("-" * 78)
    print(f"BLOKUJĄCE  (em + zl_ascii + PLN + uk_apo + heroes): {total_blocking}")
    print(f"OSTRZEŻENIA (en_typo + no_diacr + fm_missing):       {total_warnings}")
    print()

    if total_blocking == 0:
        print("WERDYKT: BRAK BLOKUJĄCYCH ZNALEZISK ✓")
        if total_warnings == 0:
            print("Faza 7 (warstwa automatyczna): GREEN — można przejść do B-light spot-check.")
        else:
            print("Faza 7 (warstwa automatyczna): GREEN z ostrzeżeniami — przejrzyj listę top.")
        sys.exit(0)
    else:
        print(f"WERDYKT: {total_blocking} BLOKUJĄCYCH — wymaga naprawy przed zamknięciem Fazy 7.")
        sys.exit(1)


if __name__ == "__main__":
    main()
