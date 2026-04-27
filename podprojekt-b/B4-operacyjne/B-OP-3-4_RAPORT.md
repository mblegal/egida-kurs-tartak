# RAPORT B-OP-3 + B-OP-4 - Zamknięcie cyklu + dokumenty incydentalne

**Data zamknięcia:** 2026-04-27
**Zakres:** Podprojekt B / B4-operacyjne / O3-ocena (3 nowe typy ewaluacji) + O4-zamkniecie (6 typów) + O5-incydenty (4 typy)
**Stan walidacji:** PASS na pełnej linii (validate_b4_op.py: 126/126 OK, B-OP-1 + B-OP-2a + B-OP-2b + B-OP-3 + B-OP-4)

---

## Co dostarczamy

Sprint B-OP-3+4 zamyka warstwę dokumentacji operacyjnej Kursu o **trzecią warstwę narzędzi oceny** (ankieta uczestnika, ankieta instruktora, indywidualny arkusz oceny, zestawienie zbiorcze ocen), **dokumenty zamknięcia cyklu** (protokół zakończenia, lista absolwentów, rejestr zaświadczeń, raport końcowy edycji, karta edycji, spis dokumentacji) oraz **dokumenty incydentalne** (usprawiedliwienia nieobecności, wnioski o powtórzenie, skreślenia z listy, protokoły wypadków BHP). Po B-OP-3+4 cała dokumentacja operacyjna Kursu jest **kompletna** dla pełnego cyklu Kursu od rekrutacji po archiwizację akt.

**Podstawowe filary B-OP-3+4:**

- **Filar I - rozszerzona ocena (3 typy w O3-ocena):** ankieta ewaluacyjna uczestnika (AEU, klasa 1 4-jęz, anonimowa), ankieta ewaluacyjna instruktora (AEI, klasa 3 PL), indywidualny arkusz oceny instruktora (AOI, klasa 3 PL); plus zestawienie zbiorcze ocen cyklu (ZZO, klasa 2 PL parametryzowana).
- **Filar II - zamknięcie cyklu (6 typów w O4-zamkniecie):** protokół zakończenia (PZK), lista absolwentów (LA), rejestr wydanych zaświadczeń (RWZ), raport końcowy edycji (RKE), karta edycji kursu (KEK, master record), spis dokumentacji edycji (SDE, manifest archiwalny). Wszystkie klasa 2 PL parametryzowana CSV→DOCX.
- **Filar III - incydenty (4 typy w O5-incydenty):** usprawiedliwienie nieobecności (UN, klasa 1 4-jęz), wniosek o powtórzenie (WP, klasa 1 4-jęz), skreślenie z listy (SL, klasa 2 PL), protokół wypadku BHP (PW, klasa 2 PL).

---

## Liczbowo

| Klasa funkcjonalna | Charakterystyka | Typów | Plików MD | Bytes MD |
|---|---|---|---|---|
| Klasa 1 (kursant 4-jęz) - AEU + UN + WP | Kursant wypełnia ręcznie | 3 | 12 | ~115 KB |
| Klasa 2 (parametryzowana PL) - ZZO + 6 zamknięcie + SL + PW | Generator CSV→DOCX | 9 | 9 | ~106 KB |
| Klasa 3 (instruktor PL) - AOI + AEI | Instruktor wypełnia ręcznie | 2 | 2 | ~10 KB |
| **Razem MD** | | **14** | **23** | **~231 KB** |
| DOCX templates klasy 2 (Pandoc) | 9 typów PL | - | 9 | ~119 KB |
| Sample CSV | sample_zamkniecie_cyklu + sample_incydenty + sample_wypadki | - | 3 | ~3 KB |
| E2E demo | 9 wypełnionych DOCX (1 per typ klasy 2 PL) | - | 9 | ~120 KB |
| **Razem artefakty B-OP-3+4** | | - | **44** | **~473 KB** |

---

## Inwentarz typów

### O3 Ocena Kursanta (cz.3 - rozszerzona ewaluacja)

| # | Typ | Identyfikator | Klasa | Języki | Liczba plików |
|---|---|---|---|---|---|
| 1 | Indywidualny Arkusz Oceny Instruktora | AOI-1.0/2026 | 3 | PL only | 1 |
| 2 | Ankieta Ewaluacyjna Instruktora | AEI-1.0/2026 | 3 | PL only | 1 |
| 3 | Ankieta Ewaluacyjna Uczestnika | AEU-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 4 | Zestawienie Zbiorcze Ocen | ZZO-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |

### O4 Zamknięcie cyklu

| # | Typ | Identyfikator | Klasa | Języki | Liczba plików |
|---|---|---|---|---|---|
| 5 | Protokół Zakończenia Kursu | PZK-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 6 | Lista Absolwentów | LA-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 7 | Rejestr Wydanych Zaświadczeń | RWZ-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 8 | Raport Końcowy Edycji | RKE-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 9 | Karta Edycji Kursu | KEK-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 10 | Spis Dokumentacji Edycji | SDE-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |

### O5 Incydenty

| # | Typ | Identyfikator | Klasa | Języki | Liczba plików |
|---|---|---|---|---|---|
| 11 | Usprawiedliwienie Nieobecności | UN-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 12 | Wniosek o Powtórzenie | WP-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 13 | Skreślenie z Listy | SL-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |
| 14 | Protokół Wypadku | PW-1.0/2026 | 2 | PL only + 1 DOCX | 1 + 1 DOCX |

---

## Architektura

### Konwencja plików (rozszerzona o 2 nowe grupy)

```
podprojekt-b/B4-operacyjne/
├── O1-wejscie/                   (B-OP-1, 5 typów)
├── O2-realizacja/                (B-OP-1, 7 typów)
├── O3-ocena/                     (B-OP-2a + 2b + 3, łącznie 13 typów)
│   ├── 16-arkusz-oceny-instruktora/      pl.md
│   ├── 17-ankieta-ewaluacyjna-instruktora/ pl.md
│   ├── 18-ankieta-ewaluacyjna-uczestnika/  pl.md en.md es.md uk.md
│   └── 19-zestawienie-zbiorcze-ocen/       pl.md + DOCX template
├── O4-zamkniecie/                NOWA grupa, 6 typów (PZK, LA, RWZ, RKE, KEK, SDE)
│   ├── 01-protokol-zakonczenia-kursu/      pl.md + DOCX
│   ├── 02-lista-absolwentow/               pl.md + DOCX
│   ├── 03-rejestr-wydanych-zaswiadczen/    pl.md + DOCX
│   ├── 04-raport-koncowy-edycji/           pl.md + DOCX
│   ├── 05-karta-edycji-kursu/              pl.md + DOCX
│   └── 06-spis-dokumentacji-edycji/        pl.md + DOCX
└── O5-incydenty/                 NOWA grupa, 4 typy (UN, WP, SL, PW)
    ├── 01-usprawiedliwienie-nieobecnosci/  pl.md en.md es.md uk.md
    ├── 02-wniosek-o-powtorzenie/           pl.md en.md es.md uk.md
    ├── 03-skreslenie-z-listy/              pl.md + DOCX
    └── 04-protokol-wypadku/                pl.md + DOCX
```

### Pipeline narzędziowy (rozszerzony)

| Skrypt | Funkcja | Status |
|---|---|---|
| `b4_op_build_templates.py` | Rozszerzony o 9 nowych typów klasy 2 PL only (ZZO, PZK, LA, RWZ, RKE, KEK, SDE, SL, PW) | rozszerzony |
| `b4_op_generate.py` | Rozszerzony o 9 nowych TypeConfig (z polami i placeholderami specyficznymi per typ) | rozszerzony |
| `validate_b4_op.py` | Rozszerzony o 14 wpisów: 3 klasa 1 (AEU, UN, WP × 4 jęz), 9 klasa 2 PL, 2 klasa 3 (AOI, AEI) | rozszerzony |
| `build_b4_op.py` | Bez zmian | bez zmian |

### Klasa 1 4-jęz - dyscyplina językowa

3 typy klasy 1 4-jęz wymagały tłumaczenia (master PL napisany przez głównego agenta, EN/ES/UK przez 9 subagentów równoległych z inline-verification):

- **AEU** (ankieta ewaluacyjna uczestnika): anonimowa, 3 sekcje pytań ze skalą 1-5 i pytania otwarte; bez identyfikacji Kursanta (RODO art. 6 ust. 1 lit. f).
- **UN** (usprawiedliwienie nieobecności): formularz incydentalny z miejscem na załączniki (zaświadczenia lekarskie, pisma urzędowe).
- **WP** (wniosek o powtórzenie testu albo Modułu): formularz z opinią instruktora i decyzją koordynatora; eskalacja do zarządu Fundacji w przypadku powtórzenia całego Modułu.

### Klasa 2 PL only - parametryzacja CSV→DOCX

9 typów klasy 2 PL only ma identyczny pipeline jak B-OP-1+2a+2b: MD master z YAML zawierającym placeholdery + DOCX template generowany przez Pandoc + generator CSV→DOCX podstawiający wartości.

Specyficzne dla B-OP-3+4:
- **ZZO** (zestawienie zbiorcze ocen): 14 placeholderów cyklu (statystyka, średnie wyniki, koordynator).
- **PZK** (protokół zakończenia): 13 placeholderów cyklu (kadra, harmonogram, statystyki).
- **LA** (lista absolwentów): 7 placeholderów cyklu + tabela do wypełnienia ręcznego (każdy absolwent jest osobnym wierszem).
- **RWZ** (rejestr zaświadczeń): 7 placeholderów cyklu + tabela ewidencyjna do wypełnienia.
- **RKE** (raport końcowy): 13 placeholderów + 3 sekcje narracyjne (osiągnięcia, problemy, rekomendacje).
- **KEK** (karta edycji): 15 placeholderów (master record cyklu w pigułce).
- **SDE** (spis dokumentacji): 6 placeholderów + tabela inwentarzowa rozdzielona per grupa O1-O5.
- **SL** (skreślenie z listy): 11 placeholderów per Kursant (rezygnacja albo decyzja Fundacji).
- **PW** (protokół wypadku BHP): 15 placeholderów per zdarzenie (poszkodowany, świadkowie, opis, służby).

Wszystkie 9 typów klasy 2 PL passes E2E demo z sample CSV (1 wiersz reprezentatywny per typ): 9 wypełnionych DOCX z 100% placeholderów podstawionych poprawnie, 0 em-dashów, 0 leftover.

### Klasa 3 PL only - dokumenty wewnętrzne instruktora

2 typy klasy 3:
- **AOI** (indywidualny arkusz oceny Kursanta przez instruktora): 5 obszarów kompetencji twardych + 6 obszarów kompetencji miękkich + mocne strony + obszary rozwoju + rekomendacje.
- **AEI** (ankieta ewaluacyjna instruktora): refleksja instruktora po cyklu (mocne strony, problemy, rekomendacje); wykorzystywana w RKE.

Oba PL only zgodnie z konwencją B-OP (dokumenty wewnętrzne nie są tłumaczone, język akt = polski).

---

## Dyscyplina jakościowa

Wszystkie 23 plików MD i 9 DOCX templates (łącznie 32 nowe artefakty B-OP-3+4) przeszły walidację:

- **0 em-dashów** wszędzie;
- **YAML frontmatter** kompletny w każdym pliku z polskimi kluczami i tłumaczonymi wartościami;
- **Identyfikator wzoru** obecny w każdym pliku (AOI, AEI, AEU, ZZO, PZK, LA, RWZ, RKE, KEK, SDE, UN, WP, SL, PW);
- **Język-specific** (klasa 1 4-jęz):
  - PL: pełne diakrytyki ąćęłńóśźż;
  - UK: kirylica >83% (max 84.8% w AEU UK, min 83.4% w WP UK), ї obecne w każdym pliku, brak ы/ё (rosyjskich);
  - ES: ñ obecne w każdym pliku, ano-bug = 0;
  - EN: bez polskich naleciałości w treści;
- **Tytuły polskich ustaw** zachowane w PL z tłumaczeniem w nawiasie przy pierwszym wystąpieniu;
- **Wzmianka EFS+** obecna w plikach klasy 1 (kursant) i klasa 2 (parametryzowane); pominięta w plikach klasy 3 (AOI, AEI - dokumenty wewnętrzne);
- **Klasa 2 placeholdery**: wszystkie unikalne w nazwach (regex `[A-Z0-9_]+`), 100% podstawienia w E2E demo.

### Workflow tłumaczeniowy (dziewiąta sesja z 0 ręcznymi korektami)

- **9 dispatchów subagentów** (3 typy klasy 1 4-jęz × 3 jęz EN/ES/UK) uruchomione równolegle w tle z inline-verification w prompcie. Wszystkie wróciły „PASSED" w pierwszym uruchomieniu:
  - AEU EN/ES/UK: PASSED
  - UN EN/ES/UK: PASSED
  - WP EN/ES/UK: PASSED
- **0 ręcznych korekt głównego agenta** dla wszystkich 9 plików tłumaczonych. **Dziewiąta sesja z rzędu z taką dyscypliną** (Parts 27-32, 47, 48, 49).

### Optymalizacja kontekstowa

- Klasa 2 PL only typowo 4-7 KB per plik (parametryzowane tabele zamiast pełnej narracji), co pozwoliło zmieścić 9 nowych typów bez wybuchu kontekstu.
- 9 dispatchów asynchronicznych równolegle minimalizuje wall-time (każdy agent stand-alone, brak interferencji).
- Wszystkie 14 typów dostarczone w jednej sesji (B-OP-3 + B-OP-4 łącznie).

---

## Workflow koordynatora po B-OP-3+4

Pełny cykl Kursu od rekrutacji do archiwizacji jest teraz wspierany komplete dokumentacją operacyjną:

1. **Rekrutacja (B-OP-1)**: lista zakwalifikowanych, karta uczestnika, oświadczenia kwalifikowalności, test wejściowy, ankieta wstępna.
2. **Realizacja (B-OP-1)**: harmonogram szczegółowy, dziennik zajęć, konspekt, lista obecności, zbiorcza karta obecności, protokół BHP, rejestr materiałów. **Incydenty (B-OP-4)**: usprawiedliwienia nieobecności, skreślenia z listy, protokoły wypadków BHP.
3. **Ocena (B-OP-2a + 2b + 3)**: quizy uzupełniające + karta odpowiedzi + klucze; sprawdziany cząstkowe M1 + klucze; test końcowy + klucz; protokół z testu końcowego; karta postępów; ankieta ewaluacyjna uczestnika (anonimowa); ankieta i arkusz oceny instruktora; zestawienie zbiorcze ocen cyklu.
4. **Zamknięcie (B-OP-3)**: protokół zakończenia cyklu, lista absolwentów, rejestr wydanych zaświadczeń, raport końcowy edycji, karta edycji kursu, spis dokumentacji edycji.
5. **Archiwizacja**: akta cyklu (wszystkie dokumenty z punktów 1-4 plus formularze incydentalne) trafiają do archiwum Fundacji wraz ze spisem dokumentacji edycji.

Polecenia generatora dla typów B-OP-3+4 (CSV→DOCX):

```
python scripts/b4_op_generate.py --typ <slug> --lang pl --csv data/<file>.csv --output-dir dist/edycja_C1_2026/

slugs B-OP-3+4: zestawienie-zbiorcze-ocen, protokol-zakonczenia-kursu, lista-absolwentow,
rejestr-wydanych-zaswiadczen, raport-koncowy-edycji, karta-edycji-kursu,
spis-dokumentacji-edycji, skreslenie-z-listy, protokol-wypadku
```

---

## Co poza zakresem B-OP-3+4

Po B-OP-3+4 dokumentacja operacyjna B4 jest **kompletna**. Pozostały elementy do wdrożenia:

- **Hub deployment**: sekcja `prezentacje.m-b.legal/kurs-tartak/dokumenty/operacyjne/` (wszystkie grupy O1-O5). Wymaga rozszerzenia generatora hubowego o sekcję dokumentów operacyjnych (na wzór B1, B2, B3).
- **Real-life walidacja w pierwszym cyklu**: wzory są zatwierdzone teoretycznie, ale realna eksploatacja w cyklu C1/2026 może ujawnić niedoskonałości (zbyt obszerne formularze, brakujące pola, niewygodne sekwencje wypełniania). Po pierwszym cyklu rekomendowana rewizja v1.0 → v1.1.

Sprint **B-OP-5 (opcja)** jeżeli pojawi się potrzeba: dodatkowe formularze incydentalne lub rozszerzenie ankiet ewaluacyjnych. Aktualnie nie planowane.

---

## Lekcje techniczne

W trakcie sprintu B-OP-3+4 wykryto i naprawiono następujące zagadnienia:

1. **Stringi Python z `'...'` zamiast `"..."` w stringach z polskimi cudzysłowami `„...."`**: lekcja powtórzona z B-OP-2b. Konsekwentne użycie `'...'` jako delimitera Pythona dla stringów zawierających polskie cudzysłowy typograficzne `„...."` zapobiega błędom składni.

2. **Asynchroniczne dispatchy subagentów minimalizują wall-time**: 9 agentów uruchomionych równolegle z inline-verification skończyło się w czasie zbliżonym do pojedynczego dispatcha (~5 minut dla najwolniejszego). Główny agent w międzyczasie pisał 9 plików klasy 2 PL only - efektywne wykorzystanie czasu oczekiwania.

3. **CSV z 47 kolumnami jako sample dla 7 typów**: jeden CSV `sample_zamkniecie_cyklu.csv` pokrywa 7 typów klasy 2 PL only (ZZO, PZK, LA, RWZ, RKE, KEK, SDE) bo każdy typ używa subsetu tych samych kolumn. Generator wyciąga tylko potrzebne placeholdery per typ. Upraszcza utrzymanie sample data.

---

## Ślad commitów

Sprint B-OP-3+4: jeden commit Part 49 z całością artefaktów (23 MD + 9 DOCX templates + 3 sample CSV + 9 demo DOCX + raport).

---

## Sygnały do następnej iteracji

Brak dostrzeżonych technical debt-ów wewnątrz B-OP-3+4. Walidator oznaczył wszystkie 32 nowe artefakty B-OP-3+4 jako OK; pełna walidacja (B-OP-1 + B-OP-2a + B-OP-2b + B-OP-3 + B-OP-4) - 126/126 OK. End-to-end test wypełnia wszystkie placeholdery w 9 wygenerowanych DOCX klasy 2 PL only.

Kwestie do potwierdzenia z koordynatorem rzeczowym przed kolejnym sprintem (hub deployment albo Podprojekt C):

1. **Czy harmonogram pierwszego cyklu C1/2026** ma stanowić podstawę real-life walidacji wzorów (planowana rewizja v1.0 → v1.1 po pierwszym cyklu).
2. **Czy hub deployment dokumentów operacyjnych** ma być realizowany przed pierwszym cyklem (wzory dostępne online dla koordynatora i instruktorów) czy po pierwszym cyklu (wzory zaktualizowane na podstawie realności).
3. **Czy AEU (anonimowa ankieta uczestnika) ma być rozdawana w 4 jęz** czy tylko w języku Kursanta plus PL (dla statystyki cyklu wystarczy jeden język per Kursant).
