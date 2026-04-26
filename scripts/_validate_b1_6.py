"""Walidator B1 #6 zaswiadczenie ukonczenia kursu (4 jezyki)."""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent / "podprojekt-b" / "B1" / "zaswiadczenie-ukonczenia-kursu"
LANGS = ["pl", "en", "es", "uk"]

results = {}
errors = []

for lang in LANGS:
    p = BASE / f"{lang}.md"
    with open(p, "rb") as f:
        data = f.read()
    txt = data.decode("utf-8")

    em = data.count(b"\xe2\x80\x94")
    cyr_zl = len(re.findall(r"\d+\s*зл\b", txt))
    has_krs = "0000957190" in txt
    has_nip = "7543348716" in txt
    has_regon = "521360040" in txt
    has_efs = "Budowa fundamentów pod lokalną politykę" in txt
    has_316 = "316" in txt
    has_76 = "76" in txt
    has_108 = "108" in txt
    has_70pct = "70%" in txt
    has_m1 = txt.count("M1") >= 6
    has_m2 = txt.count("M2") >= 5
    has_m3 = txt.count("M3") >= 6
    lang_yaml = f"język: {lang}" in txt
    words = len(txt.split())

    row_errors = []
    if em > 0: row_errors.append(f"em-dash={em}")
    if cyr_zl > 0: row_errors.append(f"cyr_zl={cyr_zl}")
    if not has_krs: row_errors.append("KRS missing")
    if not has_nip: row_errors.append("NIP missing")
    if not has_regon: row_errors.append("REGON missing")
    if not has_efs: row_errors.append("EFS+ marker missing")
    if not has_316: row_errors.append("316 missing")
    if not has_76: row_errors.append("76 missing")
    if not has_108: row_errors.append("108 missing")
    if not has_70pct: row_errors.append("70% missing")
    if not has_m1: row_errors.append("M1 not enough")
    if not has_m2: row_errors.append("M2 not enough")
    if not has_m3: row_errors.append("M3 not enough")
    if not lang_yaml: row_errors.append(f"lang YAML wrong (expected język: {lang})")

    results[lang] = {
        "em": em, "cyr_zl": cyr_zl,
        "krs": has_krs, "nip": has_nip, "regon": has_regon,
        "efs": has_efs, "316": has_316, "76": has_76, "108": has_108,
        "70%": has_70pct,
        "m1": txt.count("M1"), "m2": txt.count("M2"), "m3": txt.count("M3"),
        "lang_yaml": lang_yaml, "words": words,
        "errors": row_errors,
    }
    if row_errors:
        errors.extend([f"[{lang}] {e}" for e in row_errors])

print("=" * 80)
print(f"{'LANG':<6}{'EM':<4}{'CYR_ZL':<8}{'KRS':<5}{'NIP':<5}{'REGON':<7}{'EFS+':<6}{'316':<5}{'76':<4}{'108':<5}{'70%':<5}{'M1':<4}{'M2':<4}{'M3':<4}{'LANG_Y':<8}{'WORDS':<6}")
print("=" * 80)
for lang in LANGS:
    r = results[lang]
    print(f"{lang:<6}{r['em']:<4}{r['cyr_zl']:<8}{str(r['krs']):<5}{str(r['nip']):<5}{str(r['regon']):<7}{str(r['efs']):<6}{str(r['316']):<5}{str(r['76']):<4}{str(r['108']):<5}{str(r['70%']):<5}{r['m1']:<4}{r['m2']:<4}{r['m3']:<4}{str(r['lang_yaml']):<8}{r['words']:<6}")
print("=" * 80)
if errors:
    print("\nERRORS:")
    for e in errors:
        print(f"  - {e}")
    raise SystemExit(1)
else:
    print("\nALL CHECKS PASSED (4/4 plikow)")
