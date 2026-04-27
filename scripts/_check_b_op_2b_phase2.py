"""Walidacja Fazy 2 sprintu B-OP-2b: 8 + 2 plików sprawdzianów cząstkowych M1."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

REPO_ROOT = Path(__file__).resolve().parent.parent

FILES_KURSANT = [
    ("T12", "pl", "podprojekt-b/B4-operacyjne/O3-ocena/10-sprawdzian-czastkowy-M1-T12/pl.md"),
    ("T12", "en", "podprojekt-b/B4-operacyjne/O3-ocena/10-sprawdzian-czastkowy-M1-T12/en.md"),
    ("T12", "es", "podprojekt-b/B4-operacyjne/O3-ocena/10-sprawdzian-czastkowy-M1-T12/es.md"),
    ("T12", "uk", "podprojekt-b/B4-operacyjne/O3-ocena/10-sprawdzian-czastkowy-M1-T12/uk.md"),
    ("T34", "pl", "podprojekt-b/B4-operacyjne/O3-ocena/11-sprawdzian-czastkowy-M1-T34/pl.md"),
    ("T34", "en", "podprojekt-b/B4-operacyjne/O3-ocena/11-sprawdzian-czastkowy-M1-T34/en.md"),
    ("T34", "es", "podprojekt-b/B4-operacyjne/O3-ocena/11-sprawdzian-czastkowy-M1-T34/es.md"),
    ("T34", "uk", "podprojekt-b/B4-operacyjne/O3-ocena/11-sprawdzian-czastkowy-M1-T34/uk.md"),
]
FILES_KLUCZ = [
    ("T12", "podprojekt-b/B4-operacyjne/O3-ocena/12-klucz-sprawdzianu-M1-T12/pl.md"),
    ("T34", "podprojekt-b/B4-operacyjne/O3-ocena/13-klucz-sprawdzianu-M1-T34/pl.md"),
]

all_ok = True
print(f"{'plik':70s} {'em':>4} {'CRLF?':>5} {'YAML?':>5} {'ID?':>5}")
for block, lang, f in FILES_KURSANT:
    p = REPO_ROOT / f
    raw = p.read_bytes()
    em = raw.count(b"\xe2\x80\x94")
    crlf = b"\r\n" in raw[:200]
    yaml_ok = raw.startswith(b"---\n") and (b"\n---\n" in raw)
    txt = raw.decode("utf-8")
    id_ok = f"SPC-M1-{block}-1.0/2026" in txt
    fl = em == 0 and not crlf and yaml_ok and id_ok
    if not fl:
        all_ok = False
    print(f"{p.name + ' (' + block + '/' + lang + ')':70s} {em:>4} {str(crlf):>5} {str(yaml_ok):>5} {str(id_ok):>5}")

for block, f in FILES_KLUCZ:
    p = REPO_ROOT / f
    raw = p.read_bytes()
    em = raw.count(b"\xe2\x80\x94")
    crlf = b"\r\n" in raw[:200]
    yaml_ok = raw.startswith(b"---\n") and (b"\n---\n" in raw)
    txt = raw.decode("utf-8")
    id_ok = f"KOD-SPC-M1-{block}-1.0/2026" in txt
    fl = em == 0 and not crlf and yaml_ok and id_ok
    if not fl:
        all_ok = False
    print(f"{p.name + ' (klucz/' + block + ')':70s} {em:>4} {str(crlf):>5} {str(yaml_ok):>5} {str(id_ok):>5}")

print("\n=== Sprawdzian PL T12 - 15 pytan ===")
t12_pl = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/10-sprawdzian-czastkowy-M1-T12/pl.md").read_text(encoding="utf-8")
q_count_t12 = len(re.findall(r"^\*\*\d+\.", t12_pl, re.MULTILINE))
print(f"  pytania PL T12: {q_count_t12} (oczekuje 15)")
if q_count_t12 != 15:
    all_ok = False

t34_pl = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/11-sprawdzian-czastkowy-M1-T34/pl.md").read_text(encoding="utf-8")
q_count_t34 = len(re.findall(r"^\*\*\d+\.", t34_pl, re.MULTILINE))
print(f"  pytania PL T34: {q_count_t34} (oczekuje 15)")
if q_count_t34 != 15:
    all_ok = False

# Sprawdz ze T12 ma pytania 1-15 a T34 ma 16-30
nums_t12 = sorted(int(m.group(1)) for m in re.finditer(r"^\*\*(\d+)\.", t12_pl, re.MULTILINE))
nums_t34 = sorted(int(m.group(1)) for m in re.finditer(r"^\*\*(\d+)\.", t34_pl, re.MULTILINE))
print(f"  numery T12: {nums_t12} (oczekuje [1..15])")
print(f"  numery T34: {nums_t34} (oczekuje [16..30])")
if nums_t12 != list(range(1, 16)):
    all_ok = False
if nums_t34 != list(range(16, 31)):
    all_ok = False

print("\n=== Klucz T12 - 15 wierszy tabeli ===")
key_t12 = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/12-klucz-sprawdzianu-M1-T12/pl.md").read_text(encoding="utf-8")
key_rows_t12 = re.findall(r"^\| (\d+) \|", key_t12, re.MULTILINE)
print(f"  wiersze klucz T12: {[int(r) for r in key_rows_t12]} (oczekuje [1..15])")
if [int(r) for r in key_rows_t12] != list(range(1, 16)):
    all_ok = False

key_t34 = (REPO_ROOT / "podprojekt-b/B4-operacyjne/O3-ocena/13-klucz-sprawdzianu-M1-T34/pl.md").read_text(encoding="utf-8")
key_rows_t34 = re.findall(r"^\| (\d+) \|", key_t34, re.MULTILINE)
print(f"  wiersze klucz T34: {[int(r) for r in key_rows_t34]} (oczekuje [16..30])")
if [int(r) for r in key_rows_t34] != list(range(16, 31)):
    all_ok = False

print("\n=== UK kirylica ===")
for block in ("T12", "T34"):
    folder = "10-sprawdzian-czastkowy-M1-T12" if block == "T12" else "11-sprawdzian-czastkowy-M1-T34"
    uk = (REPO_ROOT / f"podprojekt-b/B4-operacyjne/O3-ocena/{folder}/uk.md").read_text(encoding="utf-8")
    cyr = sum(1 for c in uk if "Ѐ" <= c <= "ӿ")
    total = sum(1 for c in uk if c.isalpha())
    ratio = 100 * cyr / total if total else 0
    yi = uk.count("ї")
    ok = ratio > 60 and yi > 0
    if not ok:
        all_ok = False
    print(f"  {block} UK kirylica: {ratio:.1f}% (>60% wymagane), yi={yi}")

print("\n=== ES diakrytyki + ano-bug ===")
for block in ("T12", "T34"):
    folder = "10-sprawdzian-czastkowy-M1-T12" if block == "T12" else "11-sprawdzian-czastkowy-M1-T34"
    es = (REPO_ROOT / f"podprojekt-b/B4-operacyjne/O3-ocena/{folder}/es.md").read_text(encoding="utf-8")
    n_t = es.count("ñ")
    ano = re.findall(r"\bano\b", es)
    ok = n_t > 0 and not ano
    if not ok:
        all_ok = False
    print(f"  {block} ES: ñ={n_t}, ano-bug={len(ano)}")

print("\n=== PL diakrytyki ===")
for block in ("T12", "T34"):
    folder = "10-sprawdzian-czastkowy-M1-T12" if block == "T12" else "11-sprawdzian-czastkowy-M1-T34"
    pl = (REPO_ROOT / f"podprojekt-b/B4-operacyjne/O3-ocena/{folder}/pl.md").read_text(encoding="utf-8")
    diac = "ąćęłńóśźż"
    ok = all(pl.count(c) > 0 for c in diac)
    if not ok:
        all_ok = False
    counts = ", ".join(f"{c}={pl.count(c)}" for c in diac)
    print(f"  {block} PL: {counts}")

print("\n=== Niezmienniki tematyczne ===")
checks = [
    ("T12 PL: 30 pkt obecne", "30 punktów" in t12_pl, True),
    ("T12 PL: 21 prog obecne", "21 punkt" in t12_pl, True),
    ("T12 PL: 30 min obecne", "30 minut" in t12_pl, True),
    ("T34 PL: 30 pkt obecne", "30 punktów" in t34_pl, True),
    ("T34 PL: 21 prog obecne", "21 punkt" in t34_pl, True),
    ("T12 PL: EFS+ wzmianka", "Wzmianka o projekcie" in t12_pl, True),
    ("T34 PL: EFS+ wzmianka", "Wzmianka o projekcie" in t34_pl, True),
    ("Klucz T12: kolumna Zrodlo", "Źródło" in key_t12, True),
    ("Klucz T12: notatki interpretacyjne", "Notatki interpretacyjne" in key_t12, True),
    ("Klucz T12: BRAK EFS+ wzmianki (klasa 3)", "Wzmianka o projekcie" not in key_t12, True),
    ("Klucz T34: BRAK EFS+ wzmianki (klasa 3)", "Wzmianka o projekcie" not in key_t34, True),
]
for name, value, expected in checks:
    ok = value == expected
    if not ok:
        all_ok = False
    print(f"  [{'OK' if ok else 'FAIL'}] {name}")

total_em = sum((REPO_ROOT / f).read_bytes().count(b"\xe2\x80\x94") for _, _, f in FILES_KURSANT)
total_em += sum((REPO_ROOT / f).read_bytes().count(b"\xe2\x80\x94") for _, f in FILES_KLUCZ)
print(f"\n  em-dashy total: {total_em}")
if total_em > 0:
    all_ok = False

print(f"\n=== {'ALL PASSED' if all_ok else 'FAILED'} ===")
sys.exit(0 if all_ok else 1)
