"""Walidacja Fazy 1 sprintu B-OP-2b: 4 + 1 plików testu końcowego + klucza."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

REPO_ROOT = Path(__file__).resolve().parent.parent

FILES = [
    "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/pl.md",
    "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/en.md",
    "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/es.md",
    "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/uk.md",
    "podprojekt-b/B4-operacyjne/O3-ocena/09-klucz-testu-koncowego/pl.md",
]

print(f"{'plik':70s} {'em':>4} {'CRLF?':>5} {'YAML?':>5} {'TKK?':>5}")
all_ok = True
for f in FILES:
    p = REPO_ROOT / f
    raw = p.read_bytes()
    em = raw.count(b"\xe2\x80\x94")
    crlf_in_yaml = b"\r\n" in raw[:200]
    yaml_ok = raw.startswith(b"---\n") and (b"\n---\n" in raw)
    txt = raw.decode("utf-8")
    tkk_ok = ("TKK-1.0/2026" in txt) or ("KOD-TKK-1.0/2026" in txt)
    flag = em == 0 and not crlf_in_yaml and yaml_ok and tkk_ok
    if not flag:
        all_ok = False
    print(f"{p.name:70s} {em:>4} {str(crlf_in_yaml):>5} {str(yaml_ok):>5} {str(tkk_ok):>5}")

print("\n=== Klucz pl.md - co zostalo wyciete ===")
key = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/09-klucz-testu-koncowego/pl.md").read_text(encoding="utf-8")
checks_key = [
    ("Klucz odpowiedzi (h3) w kluczu", "### Klucz odpowiedzi" in key, True),
    ("Ocena testu (kryteria) w kluczu", "Ocena testu" in key, True),
    ("Kluczowe terminy WYCIETE", "## Kluczowe terminy" not in key, True),
    ("Sprawdz siebie WYCIETE", "## Sprawd" not in key.replace("ź", "z"), True),
]
for name, value, expected in checks_key:
    ok = value == expected
    print(f"  [{'OK' if ok else 'FAIL'}] {name}: {value}")
    if not ok:
        all_ok = False

print("\n=== Test pl.md - bez klucza, z czesciami ===")
test_pl = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/pl.md").read_text(encoding="utf-8")
checks_test = [
    ("BRAK Klucz odpowiedzi", "### Klucz odpowiedzi" not in test_pl, True),
    ("Czesc 1 obecna", "Cz" in test_pl and " 1" in test_pl, True),
    ("EFS+ wzmianka", "Wzmianka o projekcie" in test_pl, True),
    ("108 punktow", "108" in test_pl, True),
    ("76 prog", "76" in test_pl, True),
]
for name, value, expected in checks_test:
    ok = value == expected
    print(f"  [{'OK' if ok else 'FAIL'}] {name}: {value}")
    if not ok:
        all_ok = False

print("\n=== UK kirylica ===")
uk = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/uk.md").read_text(encoding="utf-8")
cyr = sum(1 for c in uk if "Ѐ" <= c <= "ӿ")
total = sum(1 for c in uk if c.isalpha())
ratio = 100 * cyr / total if total else 0
ok = ratio > 60
print(f"  [{'OK' if ok else 'FAIL'}] kirylica/litery = {cyr}/{total} = {ratio:.1f}% (prog 60%)")
if not ok:
    all_ok = False
yi_count = uk.count("ї")  # ї
print(f"  [{'OK' if yi_count > 0 else 'FAIL'}] yi (i z dwoma kropkami) count: {yi_count} (rozni od ros)")
if yi_count == 0:
    all_ok = False

print("\n=== ES diakrytyki ===")
es = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/es.md").read_text(encoding="utf-8")
n_tilde = es.count("ñ")  # ñ
print(f"  [{'OK' if n_tilde > 0 else 'FAIL'}] n-tilde count: {n_tilde}")
ano_bug = re.findall(r"\bano\b", es)
print(f"  [{'OK' if len(ano_bug) == 0 else 'FAIL'}] 'ano' bug count: {len(ano_bug)} (oczekuje 0)")
if n_tilde == 0 or ano_bug:
    all_ok = False

print("\n=== PL diakrytyki ===")
pl = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/08-test-koncowy-kursu/pl.md").read_text(encoding="utf-8")
diac_chars = "ąćęłńóśźż"  # ąćęłńóśźż
counts = {ch: pl.count(ch) for ch in diac_chars}
all_diac = all(c > 0 for c in counts.values())
print(f"  [{'OK' if all_diac else 'FAIL'}] wszystkie diakrytyki obecne: {[(k, v) for k, v in counts.items()]}")
if not all_diac:
    all_ok = False

print("\n=== Em-dash global w body ===")
total_em = sum((REPO_ROOT / f).read_bytes().count(b"\xe2\x80\x94") for f in FILES)
print(f"  [{'OK' if total_em == 0 else 'FAIL'}] em-dashy total: {total_em}")
if total_em > 0:
    all_ok = False

print(f"\n=== {'ALL PASSED' if all_ok else 'FAILED'} ===")
sys.exit(0 if all_ok else 1)
