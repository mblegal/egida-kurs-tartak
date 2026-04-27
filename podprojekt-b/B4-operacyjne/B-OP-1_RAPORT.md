# RAPORT B-OP-1 - Rdzeń dokumentacji operacyjnej Kursu

**Data zamknięcia:** 2026-04-27
**Zakres:** Podprojekt B / B4-operacyjne / rdzeń (klasy 1, 2, 3)
**Stan walidacji:** PASS na pełnej linii (validate_b4_op.py: 46/46 OK)

---

## Co dostarczamy

Sprint B-OP-1 zamyka rdzeń dokumentacji operacyjnej Kursu „Praca w tartaku" Fundacji pomocy prawnej EGIDA: 12 typów dokumentów potwierdzających, że Kurs się odbył i konkretny Kursant w nim uczestniczył. Dokumentacja wypełnia trzy filary szczelnej konstrukcji audytowej (kto, co i kiedy, z jakim efektem) zgodnie ze standardami EFS+/POWER/FERS.

**Filar I - Kto (kwalifikacja i identyfikacja):** Oświadczenie kwalifikowalności, Test wejściowy, Ankieta wstępna, Karta uczestnika, Lista kwalifikowanych.

**Filar II - Co i kiedy (realizacja godzin):** Harmonogram szczegółowy, Dziennik zajęć, Lista obecności dzienna, Konspekt lekcji, Protokół z instruktażu BHP, Rejestr wydanych materiałów.

**Filar III - Z jakim efektem (przyrost kompetencji):** Zbiorcza karta obecności (z decyzją o dopuszczeniu do testu końcowego). Pełniejsza warstwa oceny dydaktycznej (testy modułowe, sprawdziany cząstkowe, indywidualne arkusze) zaplanowana do sprintu B-OP-2.

---

## Liczbowo

| Klasa funkcjonalna | Charakterystyka | Typów | Plików MD | Bytes MD |
|---|---|---|---|---|
| Klasa 1 - kursant wypełnia ręcznie | dokumenty czytane i podpisywane przez Kursanta | 5 | 20 | 256.2 KB |
| Klasa 3 - instruktor wypełnia ręcznie | dokumenty wewnętrzne instruktorskie | 3 | 6 | 78.1 KB |
| Klasa 2 - parametryzowana CSV→DOCX | dokumenty koordynatorskie wypełniane danymi edycji | 4 | 10 | 112.4 KB |
| **Razem MD** | - | **12** | **36** | **446.7 KB** |
| DOCX templates klasy 2 | wygenerowane z MD przez Pandoc, z placeholderami | - | 10 | 150.3 KB |
| Skrypty pipeline | 4 narzędzia Python | - | 4 | ~28 KB |
| **Razem artefakty** | - | - | **50** | **~625 KB** |

---

## Inwentarz typów

### O1 Wejście do Kursu

| # | Typ | Identyfikator | Klasa | Języki |
|---|---|---|---|---|
| 1 | Oświadczenie kwalifikowalności | OSK-1.0/2026 | 1 | PL/EN/ES/UK |
| 2 | Test wejściowy (pre-test) | TW-1.0/2026 | 1 | PL/EN/ES/UK |
| 3 | Ankieta wstępna | AW-1.0/2026 | 1 | PL/EN/ES/UK |
| 4 | Karta uczestnika | KU-1.0/2026 | 2 | PL/EN/ES/UK |
| 5 | Lista zakwalifikowanych | LK-1.0/2026 | 2 | PL only |

### O2 Realizacja Kursu

| # | Typ | Identyfikator | Klasa | Języki |
|---|---|---|---|---|
| 6 | Harmonogram szczegółowy | HSZ-1.0/2026 | 2 | PL only |
| 7 | Dziennik zajęć | DZ-1.0/2026 | 3 | PL only |
| 8 | Lista obecności dzienna | LO-1.0/2026 | 3 | PL+druga (hybryda) |
| 9 | Zbiorcza karta obecności | ZKO-1.0/2026 | 2 | PL/EN/ES/UK |
| 10 | Konspekt lekcji | KL-1.0/2026 | 3 | PL only |
| 11 | Protokół z instruktażu BHP | PIB-1.0/2026 | 1 | PL/EN/ES/UK |
| 12 | Rejestr wydanych materiałów | RM-1.0/2026 | 1 | PL/EN/ES/UK |

Dokumenty wejściowe pomijają **Formularz rekrutacyjny** (FRK-1.0/2026), bo ten istnieje w B2 (warstwa prawna domknięta 2026-04-26) i jest używany jako dokument wejściowy do B4-OP bez duplikacji.

---

## Architektura

### Konwencja plików (zgodna z B)

```
podprojekt-b/B4-operacyjne/
├── O1-wejscie/
│   ├── 01-oswiadczenie-kwalifikowalnosci/  pl.md  en.md  es.md  uk.md
│   ├── 02-test-wejsciowy/                   pl.md  en.md  es.md  uk.md
│   ├── 03-ankieta-wstepna/                  pl.md  en.md  es.md  uk.md
│   ├── 04-karta-uczestnika/                 pl.md  en.md  es.md  uk.md
│   │   └── templates/                       template_{pl,en,es,uk}.docx
│   └── 05-lista-kwalifikowanych/            pl.md
│       └── templates/                       template_pl.docx
├── O2-realizacja/
│   ├── 01-harmonogram-szczegolowy/          pl.md
│   │   └── templates/                       template_pl.docx
│   ├── 02-dziennik-zajec/                   pl.md
│   ├── 03-lista-obecnosci-dzienna/          pl.md  en.md  es.md  uk.md
│   ├── 04-zbiorcza-karta-obecnosci/         pl.md  en.md  es.md  uk.md
│   │   └── templates/                       template_{pl,en,es,uk}.docx
│   ├── 05-konspekt-lekcji/                  pl.md
│   ├── 06-protokol-bhp/                     pl.md  en.md  es.md  uk.md
│   └── 07-rejestr-materialow/               pl.md  en.md  es.md  uk.md
├── _test_data/
│   └── sample_kursanci.csv
├── dist/                                    # output filled DOCX (gitignore)
└── B-OP-1_RAPORT.md
```

### Hybryda klas funkcjonalnych

Trzy klasy funkcjonalne dokumentów uzasadniają różne wymogi językowe i parametryzacji:

- **Klasa 1** (kursant wypełnia ręcznie po wydruku) - 4 jęz, MD-only, identyczna struktura między językami, kursant czyta i podpisuje swoją wersję;
- **Klasa 2** (koordynator wypełnia danymi edycji) - 4 jęz lub PL only, MD + DOCX template + generator CSV→DOCX, parametryzacja przez `{{PLACEHOLDER}}`;
- **Klasa 3** (instruktor wypełnia ręcznie) - PL only (instrukcyjne), z hybrydą dla list obecności dziennej (PL+drugi w sekcjach widzianych przez Kursanta).

### Pipeline narzędziowy (`scripts/`)

| Skrypt | Funkcja |
|---|---|
| `b4_op_build_templates.py` | MD → DOCX template (Pandoc 3.9, strip YAML, zachowanie placeholderów) |
| `b4_op_generate.py` | CSV + DOCX template → wypełnione DOCX per wiersz (python-docx 1.2) |
| `validate_b4_op.py` | walidacja em-dash, YAML, identyfikatorów, diakrytyków, cyrylicy, placeholderów |
| `build_b4_op.py` | orchestrator (validate-md → build-templates → validate-strict → optional demo) |

Uruchomienie pełnej linii:
```
python scripts/build_b4_op.py
```

Z demo end-to-end:
```
python scripts/build_b4_op.py --demo-csv podprojekt-b/B4-operacyjne/_test_data/sample_kursanci.csv
```

Aktualizacja jednego typu po zmianie MD:
```
python scripts/b4_op_build_templates.py
python scripts/validate_b4_op.py --strict
```

---

## Dyscyplina jakościowa

Wszystkie 36 plików MD przeszły walidację:

- **0 em-dashów** (znak `—` zakazany regułą feedback);
- **YAML frontmatter** kompletny w każdym pliku (typ, dokument, kurs, podprojekt, faza, język, wersja, stan-na, podstawa-prawna, charakter, strony, plus dla klasy 2: parametry);
- **Identyfikator wzoru** (np. OSK-1.0/2026) obecny w każdym pliku;
- **Język-specific:**
  - PL pełne diakrytyki (ą/ć/ę/ł/ń/ó/ś/ź/ż);
  - UK kirylica >60% w plikach pełnych, >200 znaków cyrylicy w hybrydzie LO; ї i є obecne (różnicowanie od rosyjskiego);
  - ES brak bug-a "ano" (zawsze "año"), ñ obecne;
  - EN bez polskich naleciałości w treści (ale PL nazwy własne i tytuły ustaw zachowane);
- **Tytuły polskich ustaw** zachowane w PL z tłumaczeniem w nawiasie przy pierwszym wystąpieniu - zgodnie z konwencją B i regułą Q2 sprintu;
- **Wzmianka EFS+** z poprawną informacją (kurs jako rezultat potencjału, nie działanie projektowe; SMART lider, EGIDA partner, lata 2026-2027) we wszystkich plikach klasy 1 i klasy 2 widzianych przez kursanta - zgodnie z regułą Part 45 / 04-26.

Klasa 2 dodatkowo:
- **39 unique placeholderów `{{PLACEHOLDER}}`** zachowanych jednoznacznie między PL/EN/ES/UK i DOCX templates (placeholder names stay PL CAPS Latin; descriptions in YAML translate);
- **End-to-end test:** sample_kursanci.csv (2 wiersze) → generator → 4 wypełnione DOCX (Iryna Kowalenko PL+UK, Carlos García PL+UK) z poprawnym podstawieniem wszystkich 16 placeholderów.

---

## Co poza zakresem B-OP-1 (kolejne sprinty)

**Sprint B-OP-2a** - quizy modułowe + reuse z aplikacji:
- 3 quizy modułowe × 4 jęz (eksport z `kurs_tartak/.../course_quizzes.js`)
- Karta odpowiedzi
- Klucz odpowiedzi (PL only)

**Sprint B-OP-2b** - sprawdziany cząstkowe + test końcowy + arkusze:
- 6 sprawdzianów cząstkowych × 4 jęz (podzbiory quizu modułowego)
- 1 test końcowy × 4 jęz
- Protokół z testu końcowego
- Karta postępów
- Zestawienie zbiorcze ocen
- Indywidualny arkusz oceny instruktora

**Sprint B-OP-3** - zamknięcie i archiwizacja:
- Protokół zakończenia kursu
- Lista absolwentów
- Rejestr wydanych zaświadczeń (łączy się z B1 zaświadczeniami modułowymi)
- Ankieta ewaluacyjna uczestnika (4 jęz)
- Ankieta ewaluacyjna instruktora (PL)
- Raport końcowy edycji
- Karta edycji kursu (master record edycji)
- Spis dokumentacji edycji (manifest archiwalny)

**Sprint B-OP-4 (opcja)** - incydentalne:
- Wniosek o usprawiedliwienie nieobecności
- Protokół skreślenia z listy
- Protokół wypadku/zdarzenia
- Wniosek o powtórzenie modułu

**Faza nadbudowy klasy 2** (poza B-OP):
- Rozszerzenie generatora o tryb wsadowy: jeden CSV cyklu → komplet kart, list, harmonogramów dla całej edycji jednym poleceniem.
- Plik docelowy: `scripts/b4_op_generate_edycja.py` z konwencją CSV-per-typ w `_test_data/edycja_<oznaczenie>/`.

**Hub kursu (`prezentacje.m-b.legal/kurs-tartak/dokumenty/operacyjne/`):**
- Sekcja na hubie nie została jeszcze wdrożona. Do wdrożenia po zamknięciu B-OP-3, łącznie z wszystkimi grupami O1-O4. Dziedziczyć styl z B `dokumenty/prawne/`.

---

## Ślad commitów

Sprint B-OP-1 jest gotowy do commit'a w repo `kurs_tartak`. Sugerowana struktura:

```
B-OP-1 part1: B4-operacyjne klasa 1 (5 typów × 4 jęz, 20 plików MD)
B-OP-1 part2: B4-operacyjne klasa 3 (3 typy, 6 plików MD)
B-OP-1 part3: B4-operacyjne klasa 2 MD (4 typy, 10 plików MD)
B-OP-1 part4: B4-operacyjne klasa 2 DOCX templates + generator CSV→DOCX
B-OP-1 part5: walidator + pipeline + raport
```

Albo jeden commit zbiorczy dla całego sprintu, jeśli preferowany.

---

## Sygnały do następnej iteracji

Brak dostrzeżonych technical debt-ów wewnątrz B-OP-1. Walidator oznaczył wszystkie 46 artefaktów jako OK. End-to-end test wypełnia placeholdery 100%. Brak sygnałów wymagających poprawek przed sprintem B-OP-2.

Jedna kwestia do potwierdzenia z koordynatorem rzeczowym przed B-OP-2: numeracja modułów Kursu (M1, M2, M3) i liczba sesji per moduł (parametry HSZ - LICZBA_SESJI_M1/M2/M3) są obecnie placeholderami parametryzującymi - zakładamy 8 lekcji × 3 moduły = 24 sesje cyklu zgodnie z analizą Podprojektu A. Każda zmiana w strukturze Kursu (np. dodanie modułu M4, zmiana liczby lekcji na moduł) wymusi aktualizację wzorców MD klasy 2.
