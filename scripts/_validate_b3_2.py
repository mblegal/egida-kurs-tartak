"""
Walidator B3 #2 umowa współorganizacji kursu (PL + EN).

Reusable szablon dla dokumentów B × 2 jęz (umowy B2B, kursant nie czyta).
Wzorowany na _validate_b3_1.py z Part 42; różnica: tylko 2 języki, bez ES/UK.

Sprawdza niezmienniki systemowe oddzielnie per język:
- em-dashy (zakaz absolutny)
- KRS/NIP/REGON Fundacji
- artykuły prawne (KC 471, KP 207, RODO/GDPR 4 pkt 7, 26, 13, 32, 33)
- struktura: M1/M2/M3, 316h, 12 tygodni, 70%, 75%, 76/108
- terminologia per jęz
- decyzja 5 (model hierarchiczny: F. kieruje + P. organizuje + F. konsultuje)
- decyzja 1A (gratis), 2A (F. zawsze NNW), 3A (P. wyłącznie odpowiada),
  4A (RODO odrębni admin), 6C (ramowa + załączniki + 3-mies wypowiedzenie),
  7A (brak klauzuli poufności)
"""

import sys
from pathlib import Path

DOC_DIR = Path(__file__).resolve().parent.parent / 'podprojekt-b' / 'B3' / 'umowa-wspolorganizacji'

# Niezmienniki ogólne (per plik, wszystkie języki)
COMMON_DATA = {
    'KRS': '0000957190',
    'NIP': '7543348716',
    'REGON': '521360040',
    'address': 'Ozimska',
    '316_hours_marker': '316',
    'M_modules': ['M1', 'M2', 'M3'],
    'percentages': ['70%', '75%'],
}

PL_CHECKS = {
    'em_dash_zero':                  lambda d, t: d.count(b'\xe2\x80\x94') == 0,
    'KRS_present':                   lambda d, t: 'KRS: 0000957190' in t,
    'NIP_present':                   lambda d, t: '7543348716' in t,
    'REGON_present':                 lambda d, t: '521360040' in t,
    'Ozimska_present':               lambda d, t: 'Ozimska' in t,
    'art_471_KC':                    lambda d, t: t.count('art. 471') >= 2,
    'art_207_KP':                    lambda d, t: t.count('art. 207') >= 2,
    'RODO_art_4_pkt_7':              lambda d, t: 'art. 4 pkt 7 RODO' in t,
    'RODO_art_26':                   lambda d, t: 'art. 26 RODO' in t,
    'RODO_art_13':                   lambda d, t: 'art. 13 RODO' in t,
    'RODO_art_32':                   lambda d, t: 'art. 32 RODO' in t,
    'RODO_art_33':                   lambda d, t: 'art. 33 RODO' in t,
    'OPP_art_3_ust_1':               lambda d, t: 'art. 3 ust. 1' in t,
    'OPP_art_4_ust_1_pkt_2':         lambda d, t: 'art. 4 ust. 1 pkt 2' in t,
    '316_godzin':                    lambda d, t: '316 godzin' in t,
    'M1_M2_M3_present':              lambda d, t: t.count('M1') >= 3 and t.count('M2') >= 3 and t.count('M3') >= 5,
    '12_tygodniach':                 lambda d, t: '12 tygodniach' in t,
    'prog_70':                       lambda d, t: '70%' in t,
    'prog_75':                       lambda d, t: '75%' in t,
    '76_z_108':                      lambda d, t: ('76 punktów ze 108' in t) or ('76 punktów z 108' in t),
    'NNW_3x':                        lambda d, t: t.count('NNW') >= 3,
    'EFS_marker':                    lambda d, t: 'EFS+' in t,
    'projekt_nazwa':                 lambda d, t: 'Budowa fundamentów' in t,
    'fundacja_kieruje_2x':           lambda d, t: t.count('Fundacja kieruje') >= 2,
    'przedsiebiorca_organizuje_2x':  lambda d, t: t.count('Przedsiębiorca organizuje') >= 2,
    'pomaga_konsultuje':             lambda d, t: 'pomaga i konsultuje' in t,
    'klasyfikator_decyduje':         lambda d, t: 'wyłącznie klasyfikator Fundacji' in t,
    'gratis_wzajemne_dec1A':         lambda d, t: 'wzajemnie nieodpłatny' in t,
    'NNW_F_zawsze_dec2A':            lambda d, t: ('zawsze i niezależnie' in t) or ('Fundacja zapewnia Kursantowi ubezpieczenie' in t),
    'P_wylacznie_BHP_dec3A':         lambda d, t: 'odpowiada wyłącznie Przedsiębiorca' in t,
    'odrebny_admin_dec4A':           lambda d, t: 'odrębnymi administratorami' in t or 'odrębnym administratorem' in t,
    'umowa_ramowa_dec6C':            lambda d, t: 'czas nieokreślony' in t and ('załącznik per cykl' in t.lower()),
    'wypowiedzenie_3_mies':          lambda d, t: 'trzymiesięcznego okresu wypowiedzenia' in t,
    'naruszenie_14_dni':             lambda d, t: 'w terminie 14 dni' in t,
    'breach_24_godz':                lambda d, t: '24 godzin' in t,
    'sygnal_60_dni':                 lambda d, t: '60 dni' in t,
    'opinia_7_dni':                  lambda d, t: '7 dni' in t,
    'klauzula_salwatoryjna':         lambda d, t: 'pozostałe postanowienia Umowy zachowują moc' in t,
    'sad_F_siedziby':                lambda d, t: 'sąd powszechny właściwy dla siedziby Fundacji' in t,
    'dwa_egzemplarze':               lambda d, t: 'dwóch jednobrzmiących egzemplarzach' in t,
    'tytul_umowa_ramowa_naglowek':   lambda d, t: 'UMOWA RAMOWA O WSPÓŁORGANIZACJI' in t,
    'preambla_section':              lambda d, t: '## Preambuła' in t,
    'wzmianka_section':              lambda d, t: '## Wzmianka' in t,
    'frontmatter_jezyk_pl':          lambda d, t: 'język: pl' in t,
    'frontmatter_charakter':         lambda d, t: 'charakter:' in t,
    'frontmatter_typ_B2B':           lambda d, t: 'typ: umowa ramowa B2B' in t,
    'definicje_glosariusz_polpauza': lambda d, t: t.count('** – ') >= 8,
}

EN_CHECKS = {
    'em_dash_zero':                  lambda d, t: d.count(b'\xe2\x80\x94') == 0,
    'KRS_present':                   lambda d, t: '0000957190' in t,
    'NIP_present':                   lambda d, t: '7543348716' in t,
    'REGON_present':                 lambda d, t: '521360040' in t,
    'Ozimska_present':               lambda d, t: 'Ozimska' in t,
    'art_471_CC':                    lambda d, t: t.count('Article 471') >= 2,
    'art_207_LC':                    lambda d, t: t.count('Article 207') >= 2,
    'GDPR_art_4_7':                  lambda d, t: ('Article 4(7)' in t) or ('Article 4 point 7' in t) or ('Art. 4(7)' in t),
    'GDPR_art_26':                   lambda d, t: 'Article 26' in t,
    'GDPR_art_13':                   lambda d, t: 'Article 13' in t,
    'GDPR_art_32':                   lambda d, t: 'Article 32' in t,
    'GDPR_art_33':                   lambda d, t: 'Article 33' in t,
    'GDPR_5x':                       lambda d, t: t.count('GDPR') >= 5,
    'no_RODO_polish':                lambda d, t: t.count('RODO') == 0,
    '316_hours':                     lambda d, t: '316' in t and 'hour' in t.lower(),
    'M1_M2_M3':                      lambda d, t: t.count('M1') >= 3 and t.count('M2') >= 3 and t.count('M3') >= 5,
    '12_weeks':                      lambda d, t: '12 week' in t or 'twelve week' in t.lower(),
    'pct_70':                        lambda d, t: '70%' in t,
    'pct_75':                        lambda d, t: '75%' in t,
    '76_of_108':                     lambda d, t: ('76 point' in t) or ('76 of 108' in t) or ('76/108' in t),
    'ESF_plus':                      lambda d, t: t.count('ESF+') >= 1,
    'no_EFS_polish':                 lambda d, t: t.count('EFS+') == 0,
    'Building_Foundations':          lambda d, t: 'Building Foundations' in t,
    'three_month_notice':            lambda d, t: ('three-month' in t) or ('3-month' in t) or ('three month' in t),
    'days_14':                       lambda d, t: '14 days' in t or '14 day' in t,
    'hours_24_breach':               lambda d, t: '24 hour' in t,
    'days_60_program':               lambda d, t: '60 day' in t,
    'days_7_opinion':                lambda d, t: '7 day' in t,
    'Foundation_directs':            lambda d, t: ('Foundation directs' in t) or ('Foundation manages' in t) or ('Foundation supervises' in t),
    'Entrepreneur_organises':        lambda d, t: ('Entrepreneur organis' in t) or ('Entrepreneur arranges' in t),
    'Foundation_supports':           lambda d, t: ('assists' in t) or ('supports' in t) or ('consults' in t),
    'Foundation_term_30x':           lambda d, t: t.count('Foundation') >= 30,
    'Entrepreneur_term_30x':         lambda d, t: t.count('Entrepreneur') >= 30,
    'Course_term_30x':               lambda d, t: t.count('Course') >= 30,
    'Participant_term':              lambda d, t: t.count('Participant') >= 5,
    'Supervisor_term':               lambda d, t: t.count('Supervisor') >= 5,
    'Classifier_term':               lambda d, t: 'Classifier' in t,
    'Coordinator_term':              lambda d, t: 'Coordinator' in t,
    'Cycle_term':                    lambda d, t: t.count('Cycle') >= 5,
    'Annex_per_cycle':               lambda d, t: 'annex' in t.lower() and 'Cycle' in t,
    'two_counterparts':              lambda d, t: ('two ident' in t) or ('two counter' in t),
    'court_for_Foundation':          lambda d, t: 'court' in t.lower() and 'Foundation' in t,
    'severability_clause':           lambda d, t: ('remaining provisions' in t.lower()) or ('shall remain in force' in t.lower()),
    'preamble_section':              lambda d, t: 'Preamble' in t or 'PREAMBLE' in t,
    'acknowledgement_section':       lambda d, t: 'Acknowledg' in t,
    'frontmatter_jezyk_en':          lambda d, t: 'język: en' in t,
    'glossary_polpauza':             lambda d, t: t.count('** – ') >= 8,
    'civil_code_label':              lambda d, t: 'Civil Code' in t,
    'labour_code_label':             lambda d, t: 'Labour Code' in t,
}


def run_checks(file_path: Path, checks: dict) -> tuple[int, int, list[str]]:
    if not file_path.exists():
        return 0, 0, [f'FILE_MISSING: {file_path}']
    data = file_path.read_bytes()
    txt = data.decode('utf-8')
    failed = []
    for name, predicate in checks.items():
        try:
            ok = predicate(data, txt)
        except Exception as e:
            failed.append(f'{name} (exception: {e})')
            continue
        if not ok:
            failed.append(name)
    return len(checks) - len(failed), len(checks), failed


def main() -> int:
    print('=' * 70)
    print('WALIDATOR B3 #2 umowa współorganizacji kursu (PL + EN)')
    print('=' * 70)

    targets = [
        ('PL', DOC_DIR / 'pl.md', PL_CHECKS),
        ('EN', DOC_DIR / 'en.md', EN_CHECKS),
    ]

    overall_ok = True
    for lang, fp, checks in targets:
        passed, total, failed = run_checks(fp, checks)
        status = 'OK' if not failed else 'FAILED'
        em_count = fp.read_bytes().count(b'\xe2\x80\x94') if fp.exists() else -1
        words = len(fp.read_text(encoding='utf-8').split()) if fp.exists() else 0
        print(f'\n[{lang}] {fp.name}: {passed}/{total} {status}  '
              f'(em-dash={em_count}, words={words})')
        if failed:
            overall_ok = False
            for f in failed:
                print(f'  - {f}')

    print('\n' + '=' * 70)
    print('RESULT: ' + ('ALL PASSED' if overall_ok else 'FAILED'))
    print('=' * 70)
    return 0 if overall_ok else 1


if __name__ == '__main__':
    sys.exit(main())
