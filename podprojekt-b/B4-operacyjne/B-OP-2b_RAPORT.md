# RAPORT B-OP-2b - Ocena cz.2 (test końcowy + sprawdziany cząstkowe + protokół + karta postępów)

**Data zamknięcia:** 2026-04-27
**Zakres:** Podprojekt B / B4-operacyjne / O3-ocena (5 typów nowych dokumentów)
**Stan walidacji:** PASS na pełnej linii (validate_b4_op.py: 94/94 OK, B-OP-1 + B-OP-2a + B-OP-2b)

---

## Co dostarczamy

Sprint B-OP-2b uzupełnia rdzeń dokumentacji operacyjnej Kursu o drugą warstwę narzędzi oceny: **test końcowy Kursu** (warunek dopuszczenia do egzaminu praktycznego), **sprawdziany cząstkowe Modułu 1** (śródsemestralna diagnostyka postępu), **protokół z testu końcowego** (dokument akt operacyjnych) oraz **kartę postępów Kursanta** (zbiorcze narzędzie informacji zwrotnej). Po B-OP-2b operacyjna ocena drugiego rzędu (test podsumowujący Kursu, dokumentacja decyzji o zaliczeniu, monitoring postępów Kursanta) jest zaopatrzona w komplet narzędzi.

**Pięć filarów B-OP-2b:**

- **Filar I - test końcowy Kursu (4 jęz, REUSE z aplikacji A):** 4 pliki TKK × 4 jęz (PL/EN/ES/UK) eksportowane 1:1 z lekcji `content/M3/lessons/m3-w4-l8/{lang}.md` (lekcja jest jednocześnie testem końcowym Kursu, 108 pkt, próg 76, proporcja 20/30/50). Klucz odpowiedzi (PL only) wycięty do osobnego pliku KOD-TKK klasy 3.
- **Filar II - sprawdziany cząstkowe M1 (4 jęz, REUSE z aplikacji A):** 8 plików SPC-M1 × 4 jęz dla 2 sprawdzianów cząstkowych (T1+T2 po W2 i T3+T4 po W3) eksportowane z bloków testu modułowego M1 (lekcja `content/M1/lessons/m1-w4-l8/`). Każdy sprawdzian: 15 pytań zamkniętych, 30 pkt, próg 70% = 21 pkt. Plus 2 klucze odpowiedzi (PL only) z odpowiednimi wycinkami z tabeli klucza.
- **Filar III - protokół z testu końcowego (klasa 2 PL only, parametryzowany):** 1 plik PTK + 1 DOCX template. Generator CSV→DOCX wstawia 16 placeholderów (Kursant, instruktor, koordynator, wyniki części, decyzja, uwagi). PL only zgodnie z decyzją D4=A (dokument akt operacyjnych w języku polskim, art. 94 pkt 9a Kodeksu pracy).
- **Filar IV - karta postępów Kursanta (klasa 2 4-jęz, parametryzowana):** 4 pliki KP × 4 jęz + 4 DOCX templates. Sumator wyników wszystkich narzędzi oceny: sprawdziany cząstkowe, quizy uzupełniające, testy modułowe, test końcowy. 23 placeholdery (wyniki + tryby + komentarz instruktora + ewidencja).
- **Filar V - decyzje produktowe i pipeline:** rozszerzenie pipeline'u o 2 nowe typy klasy 2 (protokol-testu-koncowego, karta-postepow-kursanta), uogólnienie regex placeholderów na `[A-Z0-9_]+` (wcześniej tylko `[A-Z_]+` co blokowało nazwy z cyframi typu WYNIK_TKK, WYNIK_SPC_M1_T12).

---

## Liczbowo

| Klasa funkcjonalna | Charakterystyka | Typów | Plików MD | Bytes MD |
|---|---|---|---|---|
| Klasa 1 - Test Końcowy Kursu (TKK) | Kursant rozwiązuje, instruktor ocenia | 1 | 4 | 125,3 KB |
| Klasa 1 - Sprawdziany cząstkowe M1 (SPC) | Kursant rozwiązuje, instruktor ocenia | 2 (T12 + T34) | 8 | 78,1 KB |
| Klasa 2 - Protokół z testu końcowego (PTK) | Generator CSV→DOCX, PL only | 1 | 1 | 7,9 KB |
| Klasa 2 - Karta postępów Kursanta (KP) | Generator CSV→DOCX, 4 jęz | 1 | 4 | 38,0 KB |
| Klasa 3 - Klucze odpowiedzi (KOD) | Dokument wewnętrzny instruktora | 3 (TKK + SPC×2) | 3 | 26,0 KB |
| **Razem MD** | | **8** | **20** | **275,3 KB** |
| DOCX templates klasy 2 (Pandoc) | PTK PL + KP × 4 jęz | - | 5 | 71,0 KB |
| Skrypty eksporterów | b4_op_export_test_koncowy + b4_op_export_sprawdzian | - | 2 | ~36 KB |
| Sample CSV | sample_protokoly + sample_karty_postepow | - | 2 | ~3 KB |
| **Razem artefakty B-OP-2b** | | - | **29** | **~385 KB** |

---

## Inwentarz typów

### O3 Ocena Kursanta (cz.2)

| # | Typ | Identyfikator | Klasa | Języki | Liczba plików |
|---|---|---|---|---|---|
| 1 | Test Końcowy Kursu | TKK-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 2 | Klucz Odpowiedzi do Testu Końcowego | KOD-TKK-1.0/2026 | 3 | PL only | 1 |
| 3 | Sprawdzian Cząstkowy M1 (T1+T2) | SPC-M1-T12-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 4 | Sprawdzian Cząstkowy M1 (T3+T4) | SPC-M1-T34-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 5 | Klucz Odpowiedzi do SPC M1 (T1+T2) | KOD-SPC-M1-T12-1.0/2026 | 3 | PL only | 1 |
| 6 | Klucz Odpowiedzi do SPC M1 (T3+T4) | KOD-SPC-M1-T34-1.0/2026 | 3 | PL only | 1 |
| 7 | Protokół z Testu Końcowego | PTK-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 8 | Karta Postępów Kursanta | KP-1.0/2026 | 2 | PL/EN/ES/UK + 4 DOCX | 4 + 4 DOCX |

---

## Architektura

### Konwencja plików (zgodna z B-OP-1 i B-OP-2a)

```
podprojekt-b/B4-operacyjne/
└── O3-ocena/
    ├── 08-test-koncowy-kursu/        pl.md  en.md  es.md  uk.md
    ├── 09-klucz-testu-koncowego/     pl.md
    ├── 10-sprawdzian-czastkowy-M1-T12/   pl.md  en.md  es.md  uk.md
    ├── 11-sprawdzian-czastkowy-M1-T34/   pl.md  en.md  es.md  uk.md
    ├── 12-klucz-sprawdzianu-M1-T12/  pl.md
    ├── 13-klucz-sprawdzianu-M1-T34/  pl.md
    ├── 14-protokol-testu-koncowego/  pl.md
    │   └── templates/                template_pl.docx
    └── 15-karta-postepow-kursanta/   pl.md  en.md  es.md  uk.md
        └── templates/                template_{pl,en,es,uk}.docx
```

### Pipeline narzędziowy (rozszerzony)

| Skrypt | Funkcja | Status |
|---|---|---|
| `b4_op_export_test_koncowy.py` | NOWY: czyta `content/M3/lessons/m3-w4-l8/{lang}.md` aplikacji A, dzieli na test dla kursanta (BEZ klucza i sekcji „Kluczowe terminy"/„Sprawdź siebie") oraz klucz dla instruktora (PL only); generuje YAML B-OP, identyfikator TKK-1.0/2026, wzmiankę EFS+, przypisy | nowy |
| `b4_op_export_sprawdzian.py` | NOWY: czyta `content/M1/lessons/m1-w4-l8/{lang}.md` aplikacji A, parsuje pogrubione nagłówki bloków T1/T2/T3/T4, generuje 2 sprawdziany cząstkowe (T12 = pytania 1-15, T34 = pytania 16-30) × 4 jęz; klucz odpowiedzi PL only z wycinkiem 15 wierszy tabeli per blok plus notatki interpretacyjne dla instruktora | nowy |
| `b4_op_build_templates.py` | Rozszerzony o 2 nowe typy klasy 2 (PTK PL + KP × 4 jęz). Regex placeholderów uogólniony na `[A-Z0-9_]+` | rozszerzony |
| `b4_op_generate.py` | Rozszerzony o 2 nowe TypeConfig: `protokol-testu-koncowego` (16 placeholderów PL) i `karta-postepow-kursanta` (22 placeholdery × 4 jęz). Regex placeholderów uogólniony na `[A-Z0-9_]+` | rozszerzony |
| `validate_b4_op.py` | Rozszerzony o 8 wpisów: 1 TKK klasy 1 (4 jęz), 1 KOD-TKK klasy 3, 2 SPC klasy 1 (4 jęz każdy), 2 KOD-SPC klasy 3, 1 PTK klasy 2 PL, 1 KP klasy 2 (4 jęz). Regex placeholderów uogólniony | rozszerzony |
| `build_b4_op.py` | Bez zmian, działa z rozszerzonym walidatorem | bez zmian |

### Kluczowa decyzja produktowa: REUSE z aplikacji A jako pierwsza linia obrony

W B-OP-2b kontynuujemy strategię B-OP-2a (eksport content z aplikacji A 1:1 zamiast tłumaczenia od nowa). Powtarza udany pattern dyscypliny:

1. **TKK**: lekcja `m3-w4-l8` jest **literalnie testem końcowym Kursu** (108 pkt, próg 76, proporcja 20/30/50 zgodnie z propozycją B-OP-2b). Strukturalna zgodność potwierdzona przed implementacją - zatem REUSE eliminuje 4-6 sesji tłumaczeniowych.
2. **SPC-M1**: lekcja `m1-w4-l8` ma jasne bloki tematyczne T1/T2/T3/T4 z numerowanymi pytaniami (1-8 BHP, 9-15 Materiał, 16-23 Procesy, 24-30 Organizacja). Eksporter parsuje pogrubione nagłówki bloków per jęz i wycina dwa sprawdziany cząstkowe (T12 = pytania 1-15 z bloków BHP+Materiał, T34 = pytania 16-30 z bloków Procesy+Organizacja). Klucz odpowiedzi: tabela 30 wierszy z m1-w4-l8 dzielona na dwie tabele po 15 wierszy.

Ograniczenia REUSE:
- **M2 i M3 sprawdzianów cząstkowych nie produkujemy** (decyzja D1=D1.1 zrewidowana w trakcie sprintu). Powód materiałowy: m2-w4-l8 zawiera metodykę testu i próbkę 8 pytań (po 2 na obszar), nie pełną pulę 25 pytań - brak źródła do REUSE; m3-w4-l8 jest testem końcowym Kursu (TKK), zatem sprawdzian cząstkowy z części M1+M2 dublowałby TKK. Quizy uzupełniające M2 i M3 (B-OP-2a) pełnią funkcję post-l8.

### Klasa 2 - parametryzacja: dwa różne reżimy językowe

- **PTK PL only**: protokół jest dokumentem akt operacyjnych Kursanta (Kodeks pracy art. 94 pkt 9a). Język akt = polski. Kursant cudzoziemiec dostaje zaświadczenie B1 z protokołu po teście (B1 ma 4 jęz), nie potrzebuje protokołu we własnym języku.
- **KP 4 jęz**: karta postępów jest narzędziem informacji zwrotnej dla Kursanta. Transparentność wyniku wymaga wydania w języku kursanta (analogicznie do certyfikatów B1). Plus wersja PL do akt.

---

## Dyscyplina jakościowa

Wszystkie 20 plików MD i 5 DOCX templates (łącznie 25 artefaktów B-OP-2b) przeszły walidację:

- **0 em-dashów** (znak U+2014 zakazany regułą feedback);
- **YAML frontmatter** kompletny w każdym pliku;
- **Identyfikator wzoru** obecny w każdym pliku;
- **Język-specific:**
  - PL pełne diakrytyki (ą/ć/ę/ł/ń/ó/ś/ź/ż);
  - UK kirylica >85% w wszystkich plikach (90% w TKK UK, 85% w SPC UK, 85% w KP UK), ї obecne, brak ы/ё (rosyjskich);
  - ES brak bug-a „ano" (zawsze „año"), ñ obecne;
  - EN bez polskich naleciałości w treści;
- **Tytuły polskich ustaw** zachowane w PL z tłumaczeniem w nawiasie;
- **Wzmianka EFS+** obecna w plikach klasy 1 (kursant) i klasy 2 (parametryzowane); pominięta w plikach klasy 3 (klucze, dokumenty wewnętrzne) zgodnie z regułą Part 45.

Klasa 2 dodatkowo:
- **PTK**: 16 unique placeholderów + 1 dokumentacyjny `{{NAZWA_POLA}}`. End-to-end test: sample_protokoly.csv (Iryna zaliczona 91/108 = 84%, Carlos niezaliczony 68/108 = 63%) → generator → 2 wypełnione DOCX z poprawnym podstawieniem 16 placeholderów, 0 em-dashów, 0 leftover.
- **KP**: 22 unique placeholderów + 1 dokumentacyjny `{{NAZWA_POLA}}`. End-to-end test: sample_karty_postepow.csv (3 wiersze: Iryna po M1 - tylko M1 wypełniony, Iryna po M3 zaliczony, Carlos po M3 niezaliczony) → generator × 4 jęz → 12 wypełnionych DOCX z 22/22 placeholderów, 0 em-dashów, 0 leftover.

### Workflow tłumaczeniowy (ósma sesja z 0 ręcznymi korektami)

- **TKK i SPC-M1**: brak subagentów - eksportery Python robią 1:1 transfer treści 4-językowej z aplikacji A do B-OP. Treść istnieje już w 4 językach (Parts 27-32 dyscyplina). Zgodne z feedback `generator-vs-subagent`: dane strukturyzowane → Python skrypt.
- **PTK**: PL only, napisane przez głównego agenta z auto-weryfikacją Python po Write (em-dash=0, placeholdery=16, ID present).
- **KP master PL**: napisane przez głównego agenta z auto-weryfikacją.
- **KP EN/ES/UK**: trzy subagenty równolegle z **inline weryfikacją Python** (feedback `subagent-inline-verification`). Wyniki: wszystkie trzy agenty zwróciły „PASSED" w pierwszym uruchomieniu (em-dash=0, 23/23 placeholderów, ID wzoru zachowany, kirylica/ñ/diakrytyki w niezmiennikach). 0 ręcznych korekt głównego agenta. **Ósma sesja z rzędu z taką dyscypliną** (Parts 27-32, 47, B-OP-2b).

---

## Workflow koordynatora po B-OP-2b

1. **Sprawdziany cząstkowe M1**: drukuje arkusz SPC-M1-T12 (PL + język Kursanta) po W2 modułu, SPC-M1-T34 po W3. Instruktor ocenia z użyciem KOD-SPC-M1-T12 albo T34. W trybie kart papierowych Kursant pisze odpowiedzi bezpośrednio na arkuszu (każde pytanie ma A/B/C/D do zakreślenia).
2. **Test końcowy Kursu**: drukuje TKK (PL + język Kursanta) jako lekcję l8 tygodnia 4 Modułu 3. Czas 120 min, 108 pkt, próg 76. Instruktor ocenia z użyciem KOD-TKK (zawiera klucz + kryteria oceny scenariuszy + zadań + interpretację wyniku + ścieżki rozwoju).
3. **Protokół z testu końcowego**: po ocenie testu instruktor i koordynator wypełniają CSV (sample_protokoly.csv jako wzór) i generują DOCX: `python scripts/b4_op_generate.py --typ protokol-testu-koncowego --lang pl --csv data.csv --output-dir dist/`. Protokół trafia do akt Kursanta i archiwum cyklu.
4. **Karta postępów Kursanta**: po teście modułowym (M1, M2, M3) albo po teście końcowym koordynator generuje karty postępów: `python scripts/b4_op_generate.py --typ karta-postepow-kursanta --lang {pl,en,es,uk} --csv data.csv --output-dir dist/`. Każdy Kursant dostaje kartę w swoim języku + PL do akt. Wcześniejsze karty mogą mieć niewypełnione pola („nie podejmował") jeśli Kursant nie podszedł jeszcze do testu.
5. **Aktualizacja testu końcowego**: gdy zmienia się treść m3-w4-l8 w aplikacji A, koordynator uruchamia `python scripts/b4_op_export_test_koncowy.py` aby zregenerować TKK i KOD-TKK.
6. **Aktualizacja sprawdzianów**: gdy zmienia się treść m1-w4-l8, uruchamia `python scripts/b4_op_export_sprawdzian.py`.

---

## Co poza zakresem B-OP-2b (kolejne sprinty)

**Sprint B-OP-3** - zamknięcie i archiwizacja edycji:
- Protokół zakończenia kursu
- Lista absolwentów (klasa 2 PL)
- Rejestr wydanych zaświadczeń (łączy się z B1)
- Ankieta ewaluacyjna uczestnika (4 jęz)
- Ankieta ewaluacyjna instruktora (PL)
- Raport końcowy edycji (PL)
- Karta edycji kursu (master record edycji)
- Spis dokumentacji edycji (manifest archiwalny)
- **Zestawienie zbiorcze ocen cyklu** (klasa 2 PL only) - przeniesione z B-OP-2b
- **Indywidualny arkusz oceny instruktora** (klasa 3 PL) - przeniesione z B-OP-2b

**Sprint B-OP-4 (opcja)** - dokumenty incydentalne:
- Usprawiedliwienia nieobecności
- Wnioski o powtórzenie modułu/testu
- Skreślenia z listy
- Protokoły wypadków (BHP)

**Hub kursu (`prezentacje.m-b.legal/kurs-tartak/dokumenty/operacyjne/`):** sekcja na hubie do wdrożenia po zamknięciu B-OP-3, obejmująca wszystkie grupy O1-O4.

---

## Lekcje techniczne

W trakcie sprintu wykryto i naprawiono następujące zagadnienia:

1. **Regex `[A-Z_]+` blokował nazwy placeholderów z cyframi**: poprzednia wersja nie łapała `WYNIK_TKK`, `WYNIK_SPC_M1_T12`, `WYNIK_TEST_M3` itp. ze względu na cyfry w nazwach. Naprawione przez uogólnienie do `[A-Z0-9_]+` w trzech miejscach: `b4_op_build_templates.py`, `b4_op_generate.py`, `validate_b4_op.py`. Zmiana niełamiąca dla istniejących 5 typów klasy 2 (sprawdzone - żaden istniejący placeholder nie miał cyfr w nazwie).

2. **Stringi Python z polskimi cudzysłowami `„...."` w stringu `"..."`**: `"...kolumna „Źródło"...."` - cudzysłów zamykający `"` w `Źródło"` zamykał string Pythona przed końcem. Naprawione przez konsekwentne użycie `'...'` jako delimitera Pythona dla wszystkich stringów zawierających polskie cudzysłowy `„...."`. Lekcja: zawsze używaj single-quote delimiterów dla stringów z polskimi cudzysłowami typograficznymi.

3. **Dyscyplina write_bytes vs write_text potwierdzona**: oba nowe eksportery używają `write_bytes(text.encode('utf-8'))` zgodnie z feedback `feedback-python-write-text-windows-crlf`. Brak regresji CRLF na Windows, walidator parsuje YAML bez problemu.

---

## Ślad commitów

Sprint B-OP-2b: jeden commit Part 48 z całością artefaktów (20 MD + 5 DOCX templates + 2 nowe skrypty + 4 zmodyfikowane skrypty + 2 sample CSV + 12 demo DOCX + raport).

---

## Sygnały do następnej iteracji

Brak dostrzeżonych technical debt-ów wewnątrz B-OP-2b. Walidator oznaczył wszystkie 25 artefaktów B-OP-2b jako OK; pełna walidacja (B-OP-1 + B-OP-2a + B-OP-2b) - 94/94 OK. End-to-end test wypełnia wszystkie placeholdery 100% w 14 wygenerowanych DOCX (2 PTK PL + 12 KP × 4 jęz × 3 wiersze). Brak sygnałów wymagających poprawek przed sprintem B-OP-3.

Kwestie do potwierdzenia z koordynatorem rzeczowym przed B-OP-3:
1. **Czy struktura sprawdzianów cząstkowych M1 (T12 + T34, 15 pytań po 2 pkt każdy)** sprawdzi się w empirii pierwszego cyklu, czy koordynator zechce dodatkowych blokad (np. T1 osobno + T2 osobno = 4 sprawdziany cząstkowe M1 zamiast 2).
2. **Czy karta postępów ma być wydawana po każdym Module** (3 razy w trakcie cyklu + 1 raz po teście końcowym = 4 karty), czy raz na końcu cyklu (tylko po teście końcowym). Decyzja oparta na pierwszej empirii cyklu.
3. **Czy protokół z testu końcowego ma być wydawany Kursantowi** (egzemplarz + akta), czy tylko do akt (Kursant dostaje zaświadczenie B1 ze skrótem informacji). Aktualnie wzór zakłada egzemplarz Kursanta i egzemplarz Fundacji.
