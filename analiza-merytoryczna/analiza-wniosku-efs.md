# Analiza wniosku EFS+ 2026-2027 — kurs tartakowy EGIDA

**Zadanie:** Task 1.2 — Part 1 (Analiza merytoryczna)
**Data analizy:** 2026-04-16
**Plik źródłowy:** `2026_004 - Smart_Egida - projekt EFS+2026-2027 - WNIOSEK.pdf` (333 KB, 75 stron)
**Program:** Fundusze Europejskie dla Opolskiego 2021-2027 / EFS+ (Priorytet 06.03)

---

> **KONTEKST PROJEKTU I DECYZJA (2026-04-16):**
> Wniosek dotyczy projektu pn. „Budowa fundamentów pod lokalną politykę migracyjną
> i integracyjną" realizowanego przez **Fundację na rzecz Edukacji SMART** (lider) +
> **Fundację pomocy prawnej EGIDA** (partner) — projekt wzmocnienia potencjału
> organizacyjnego obu fundacji (500 000 zł, 2026-01-01 → 2027-12-31). Kurs tartakowy
> nie jest explicite wskaźnikiem projektowym, ale jest **efektem docelowym** budowania
> potencjału: wniosek finansuje wzmocnienie, **po to żeby** organizacja realizowała
> swój cel statutowy — a działaniami statutowymi są m.in. kursy integracyjne dla migrantów.
>
> **DECYZJA (podjęta przez koordynatora EGIDA, 2026-04-16) — OPCJA C „HYBRYDA":**
> Kurs tartakowy jest traktowany jako działanie projektowe (łańcuch przyczynowy
> wniosek → potencjał → kursy jest ciągły). Oznaczenia UE (3 logotypy: FE Opolskie
> + barwy RP + UE) oraz klauzula informacyjna SĄ obowiązkowe. Implementacja przez
> **placeholdery** parametryzowane w `course.config.json` — zgodnie z D14 (Architektura 3
> „deferred split"), żeby w fazie C (plugin Claude Code) inna organizacja mogła podmienić
> wartości bez modyfikacji kodu.
>
> Konsekwencje praktyczne: logotypy + klauzula w stopce `kurs.html`, slajdzie tytułowym
> `prezentacja.html`, nagłówku zaświadczeń DOCX (faza B), naklejkach na sprzęt (jeśli
> dotyczy). Wskaźniki projektu (11 osób personelu) NIE są zmartwieniem kursu —
> to sprawa SMART+EGIDA jako beneficjentów. Pre-test/post-test: opcjonalny dla kursu
> migrantów, mechanizm karty postępu (Opcja R ze speca) wystarczający.

---

## 1. Cel projektu

Celem projektu jest rozbudowa potencjałów Fundacji SMART i Fundacji EGIDA w ramach ich
dążenia do wyspecjalizowania się w kompleksowych działaniach na rzecz integracji oraz
aktywizacji społecznej i zawodowej cudzoziemców przebywających legalnie na terytorium RP
(s. 11). Wg wniosku celem jest „rozbudowa potencjałów organizacji w ramach dążenia przez
nich do wyspecjalizowania się w kierunku kompleksowych działań na rzecz włączania migrantów
do społeczeństwa przyjmującego" (s. 11).

Organizacje zamierzają utworzyć lokalny ośrodek integracji cudzoziemców w modelu
**one-stop-shop** w Opolu (docelowo też Kluczbork), oferujący:
- nauczanie i promocję języka polskiego (kursy stacjonarne, e-learning, social media),
- nauczanie „życia w Polsce" (kultura, obyczaje, e-administracja, ekologia, zasady bezpieczeństwa),
- promocję zatrudnienia (doradztwo zawodowe, pośrednictwo pracy, praktyki, szkolenia kompetencyjne).

Projekt trwa 2026-01-01 — 2027-12-31 (24 miesiące). Budżet: 500 000 zł (dofinansowanie EFS+
425 000 zł = 85%, budżet państwa 50 000 zł = 10%, wkład własny 25 000 zł = 5%).

### Implikacje dla kursu

- E-learning tartakowy mieści się w kategorii „nauczanie życia w Polsce / szkolenia
  kompetencyjne" — jest zgodny z wizją ośrodka one-stop-shop.
- **Kurs jest sygnowany jako działanie realizowane w ramach projektu EFS+** (logo + klauzula
  obowiązkowe) — zgodnie z decyzją koordynatora z 2026-04-16, zob. nota na górze dokumentu.
- Implementacja przez placeholdery w `course.config.json` (`{{UE_LOGO_BLOCK}}`,
  `{{CO_FUNDED_CLAUSE}}`, `{{PROJEKT_NAZWA}}`, `{{PROJEKT_NUMER}}`) — Architektura 3.

---

## 2. Grupy docelowe

### Bezpośrednia grupa docelowa (s. 12)

Projekt kierowany jest do **pracowników i osób związanych umowami z obiema organizacjami**
— nie do migrantów bezpośrednio. Łącznie 11 osób (8 kobiet + 3 mężczyzn), w tym:
- 8 osób już związanych z organizacjami (wolontariusze, zleceniobiorcy, pracownicy),
- 3 nowo zatrudnione osoby (pracownicy biurowi z kompetencjami językowymi).

### Pośrednia grupa docelowa — migranci (s. 12–13)

Docelowi odbiorcy usług ośrodka (nie wskaźniki projektu):
- **Obywatele Ukrainy** zamieszkali lub pracujący w woj. opolskim — osoby, które komunikują
  się po polsku, ale oceniają swoją znajomość jako niewystarczającą do prawidłowego wykonywania
  ról społecznych; kurs języka polskiego na poziomie wyższym niż podstawowy.
- **Imigranci hiszpańskojęzyczni, ze szczególnym uwzględnieniem obywateli Kolumbii** —
  nowa, dynamicznie rosnąca grupa (wzrost zezwoleń na pracę o 352,1% w I półroczu 2024 r.
  względem 2023 r.); brak dotychczas zorganizowanych działań integracyjnych dla tej grupy.
- Wiek: pełnoletni.
- Lokalizacja: Opole i Kluczbork (woj. opolskie).
- Status: przebywający legalnie na terytorium RP.

Wniosek wskazuje, że organizacje „obecnie obejmują wsparciem 80-osobową grupę cudzoziemców"
(s. 13) i planują zwielokrotnienie zasięgu po wzmocnieniu potencjału.

### Implikacje dla treści kursu tartakowego

- Kurs BHP/tartak trafia do **migrantów poszukujących zatrudnienia** — głównie Ukraińcy
  i Kolumbijczycy w woj. opolskim. Uzasadnienie językowe (UA, ES, PL) jest więc zgodne
  z profilowaną grupą docelową wniosku.
- **Kryteria kwalifikowalności uczestnika** (zgodnie z decyzją C — kurs w ramach projektu):
  pełnoletność + legalny pobyt w RP. Weryfikujemy przy zapisie; odzwierciedlenie w umowie
  o kurs (Podprojekt B) — pole `{{UCZESTNIK_STATUS_POBYTOWY}}`.
- Poziom języka polskiego uczestników: wyższy niż podstawowy (A2+/B1) — kurs PL
  pisany dla A2+ jest bezpieczny.
- Wniosek **nie precyzuje** wymagań formalnych co do poziomu wykształcenia uczestników
  kursów zawodowych — luka do uzupełnienia u koordynatora.

---

## 3. Wskaźniki produktu i rezultatu

### Wskaźniki produktu (output — co dostarczamy)

| Wskaźnik | Wartość docelowa (ogółem) | K / M | Sposób pomiaru |
|----------|--------------------------|-------|----------------|
| Liczba przedstawicieli OSP (w tym wolontariuszy) objętych wsparciem | **11** | 8K / 3M | umowy o pracę, umowy cywilnoprawne, listy obecności, zaświadczenia |
| Liczba osób z krajów trzecich objętych wsparciem (wskaźnik horyzontalny nr 4) | **1** | — | umowa o pracę, listy obecności, listy płac |

Pozostałe wskaźniki horyzontalne (osoby z niepełnosprawnościami, bezdomni, mniejszości
etniczne, obcego pochodzenia) mają wartość 0 — projekt ich nie realizuje.

### Wskaźniki rezultatu (outcome — efekt)

| Wskaźnik | Wartość bazowa | Wartość docelowa (ogółem) | Sposób pomiaru |
|----------|----------------|--------------------------|----------------|
| Liczba OSP, które zwiększyły potencjał organizacyjny (zarządzanie, RODO, jakość usług, współpraca) | 0 | **2** (obydwie fundacje) | ilość opracowanych i wdrożonych procedur RODO, audytów |
| Liczba przedstawicieli OSP, którzy zdobyli nowe umiejętności/wiedzę/kwalifikacje | 0 | **8** (SMART: 6, EGIDA: 2) | listy obecności, zaświadczenia ukończenia, pre-test/post-test, pomiar w ciągu 4 tygodni od zakończenia |

**Podział na realizatorów (s. 20–21):**
- SMART (Wnioskodawca): 6 osób zdobywa kwalifikacje (arkusz kalkulacyjny + prawo cudzoziemców),
  1 organizacja zwiększa potencjał.
- EGIDA (Partner): 2 osoby zdobywają kwalifikacje (arkusz kalkulacyjny), 1 organizacja
  zwiększa potencjał.

### Implikacje dla kursu / dokumentów

- **Zaświadczenia o ukończeniu szkolenia** muszą być wystawiane dla każdego uczestnika —
  są dowodem wskaźnika rezultatu nr 2 (s. 18). Wzór zaświadczenia MUSI zawierać: imię,
  nazwisko, zakres szkolenia, datę, podpis organizacji.
- **Pre-test i post-test** są wymagane przy wskaźniku rezultatu nr 2 — muszą być
  zaprojektowane w systemie e-learningowym jako moduły ewaluacyjne.
- Karta postępu / wynik quizu końcowego w systemie kursowym MUSI rejestrować:
  wynik procentowy, datę ukończenia, identyfikator uczestnika.
- **Koszt przypadający na 1 uczestnika projektu: 45 454,55 zł** (s. 49) — to kwota
  projektu organizacyjnego, nie koszt kursu e-learningowego (kurs jest efektem, nie kosztem
  kwalifikowanym w tym projekcie).

---

## 4. Wymogi oznaczeń wizualnych

### Obligatoryjne elementy wizualne (s. 71–73, sekcja 11)

Wg Podręcznika wnioskodawcy i beneficjenta Funduszy Europejskich 2021–2027 (s. 71),
na wszystkich dokumentach i materiałach projektu muszą się pojawić:

1. **Znak Funduszy Europejskich** (logo programu „Fundusze Europejskie dla Opolskiego")
2. **Znak barw Rzeczypospolitej Polskiej** (flaga/herb RP)
3. **Znak Unii Europejskiej** (flaga UE z napisem „Dofinansowane przez Unię Europejską")

Kolejność i proporcje według Księgi Identyfikacji Wizualnej FE 2021–2027.

### Gdzie muszą się pojawić (s. 71–73)

| Nośnik | Obowiązek |
|--------|-----------|
| Strony internetowe obu organizacji | opis projektu + logotypy (styczeń–luty 2026) |
| Media społecznościowe (FB SMART, FB EGIDA, Instagram SMART) | informacje + logotypy (styczeń–marzec 2026) |
| Plakat/tablica w siedzibie (wejście do budynku, drzwi biura) | trwały, widoczny (styczeń–luty 2026) |
| Naklejki na zakupionym sprzęcie i wyposażeniu | nazwa projektu, źródło finansowania, logotypy (styczeń–kwiecień 2026) |
| Wszystkie dokumenty związane z projektem | logotypy UE, styczeń 2026 – grudzień 2027 |

### Obligatoryjna klauzula informacyjna

Wniosek nie cytuje pełnej klauzuli (s. nieokr.) — odsyła do *Podręcznika wnioskodawcy
i beneficjenta Funduszy Europejskich na lata 2021–2027 w zakresie informacji i promocji*.
Standardowa klauzula brzmi mniej więcej:
„Projekt finansowany ze środków Europejskiego Funduszu Społecznego Plus w ramach
programu Fundusze Europejskie dla Opolskiego 2021–2027."

> Do weryfikacji: pełna, oficjalna wersja klauzuli u koordynatora projektu lub
> w dokumentach IZ (Urząd Marszałkowski Województwa Opolskiego).

### Implikacje dla generatora (Faza 6)

- Template `kurs.html` — stopka musi zawierać placeholder `{{CO_FUNDED_CLAUSE}}`
  i `{{UE_LOGO_BLOCK}}` (trzy znaki: FE Opolskie + barwy RP + UE).
- Template `prezentacja.html` — slajd tytułowy musi zawierać `{{UE_LOGO_BLOCK}}`.
- Template zaświadczenia DOCX — nagłówek lub stopka: `{{UE_LOGO_BLOCK}}`,
  `{{CO_FUNDED_CLAUSE}}`, `{{PROJEKT_NUMER}}`.
- Naklejki na sprzęt: `{{PROJEKT_NAZWA}}`, `{{PROJEKT_NUMER}}`, `{{UE_LOGO_BLOCK}}`.

---

## 5. Wymogi RODO i zgód uczestnika

### Kontekst — Zadanie 6 projektu (s. 44–46)

Jednym z 6 zadań projektu jest wprost: „Wprowadzenie systemu ochrony danych osobowych
w organizacjach (audyt, compliance, governance, risk management, training)". Budżet:
14 000 zł (po 7 000 zł na każdą organizację), realizacja 2026-01-01 – 2026-04-15.
Wskaźnik rezultatu nr 1 (potencjał organizacyjny) mierzony jest m.in. przez:
„ilość opracowanych i wdrożonych procedur związanych z ochroną danych osobowych,
ilość przeprowadzonych audytów dotyczących ochrony danych osobowych" (s. 17).

Oznacza to, że **EGIDA musi mieć wdrożone procedury RODO przed 2026-04-15** — i te
procedury będą podstawą dla dokumentów kursowych.

### Co trzeba zbierać od uczestników kursów zawodowych (parafraza z wniosku)

Wniosek nie specyfikuje szczegółowo formularzy dla uczestników kursów migrantów, ale
ze wskaźników i opisu zadań wynika konieczność zbierania:

- **Dane identyfikacyjne** (imię, nazwisko, data urodzenia) — niezbędne do wystawienia
  zaświadczenia ukończenia szkolenia.
- **Dane kontaktowe** (e-mail, ewentualnie telefon) — do ankiety follow-up i monitorowania
  wskaźników rezultatu.
- **Status pobytowy / obywatelstwo** — weryfikacja kryterium kwalifikowalności
  (legalne przebywanie w Polsce), wymagana dla wskaźnika horyzontalnego nr 4
  (osoba z krajów trzecich).
- **Dane o sytuacji zawodowej** (poszukujący pracy / pracujący) — dla wskaźników
  aktywizacji zawodowej.
- **Dane o wyniku szkolenia** (pre-test, post-test, wynik quizu końcowego) — dokumentacja
  wskaźnika rezultatu nr 2.

### Wymagane zgody (parafraza)

| Zgoda | Charakter | Podstawa |
|-------|-----------|---------|
| Przetwarzanie danych osobowych w celu realizacji projektu EFS+ | Obligatoryjna | RODO art. 6 ust. 1 lit. b/c (realizacja umowy / obowiązek prawny) |
| Przetwarzanie danych w celu monitorowania wskaźników przez IZ (Urząd Marszałkowski) | Obligatoryjna | przepisy o Funduszach Europejskich |
| Ankieta follow-up po zakończeniu kursu (do 12 miesięcy) | Osobna, opcjonalna | RODO art. 6 ust. 1 lit. a (zgoda) |
| Publikacja wizerunku (np. zdjęcia z zajęć stacjonarnych) | Osobna, opcjonalna | RODO art. 6 ust. 1 lit. a |

### Klauzula RODO obowiązkowa

Administrator danych: Fundacja na rzecz Edukacji SMART (lider projektu) lub Fundacja
pomocy prawnej EGIDA (zależnie od roli w kursie). Cel przetwarzania: realizacja
projektu dofinansowanego z EFS+ FEO 2021–2027. Dane przekazywane do IZ (Urzędu
Marszałkowskiego) w ramach obowiązków sprawozdawczych.

> Pełna treść klauzuli: do opracowania po zakończeniu Zadania 6 projektu (audyt RODO,
> termin: do 2026-04-15). Placeholder w dokumentach kursowych: `{{KLAUZULA_RODO_PELNA}}`.

### Implikacje dla fazy B (dokumenty)

- **Umowa o kurs**: pełna klauzula RODO (`{{KLAUZULA_RODO_PELNA}}`), zgoda na
  przetwarzanie danych w celach projektowych (obligatoryjna) + zgoda follow-up (opcjonalna).
- **Zaświadczenie**: brak danych wrażliwych w jawnym tekście — tylko imię, nazwisko,
  zakres szkolenia, data, godziny. Numer dokumentu (do ewidencji wewnętrznej EGIDY).
- **Formularz rekrutacyjny / karta uczestnika**: imię, nazwisko, data urodzenia,
  obywatelstwo, status pobytowy (dokument do wglądu, nie kserokopia), e-mail, status
  zawodowy — to WEWNĘTRZNY dokument, przechowywany zgodnie z procedurami RODO.
- **Pre-test i post-test**: wyniki przechowywane w systemie e-learningowym — anonimizacja
  po upływie okresu przechowywania wymaganego przez IZ.

---

## 6. Ograniczenia harmonogramowe

### Daty kluczowe projektu

| Etap | Data |
|------|------|
| Start projektu | 2026-01-01 |
| Zakończenie rzeczowe (ostatnie działanie) | 2027-12-31 |
| Zakończenie finansowe (ostatnie płatności) | 2027-12-31 |

### Kamienie milowe z harmonogramu rzeczowo-finansowego (s. 22–49)

| Zadanie | Zakres | Termin realizacji |
|---------|--------|-------------------|
| Zadanie 1: Dodatkowe zatrudnienie i onboarding | Zatrudnienie 3 osób (specjalista marketingu, 2 pracowników biurowych) | 2026-01-01 – 2027-12-31 (cały projekt) |
| Zadanie 2: Zakup sprzętu biurowego i oprogramowania | Laptopy, komputery, drukarki, monitor interaktywny, oprogramowanie biurowe, ERP | 2026-01-01 – **2026-03-31** |
| Zadanie 3: Wyposażenie sal szkoleniowych | Stół konferencyjny, 20 krzeseł (sala w Opolu) | 2026-01-01 – **2026-05-09** |
| Zadanie 4: Szkolenie — arkusz kalkulacyjny | 4-stopniowy kurs dla 4 osób (SMART) | 2026-01-01 – **2026-02-28** |
| Zadanie 5: Szkolenie — prawo cudzoziemców | 12 godzin, 6 osób (SMART) | **2026-05-01** – 2026-05-31 |
| Zadanie 6: Audyt i wdrożenie RODO | Audyt + procedury + szkolenie w obu organizacjach | 2026-01-01 – **2026-04-15** |

### Ważne: koordynator projektu

Zatrudniony w wymiarze:
- 1/2 etatu: 2026-01-01 – 2026-04-30 (intensywna faza startowa: zakupy, rekrutacja, promocja)
- 1/8 etatu: 2026-05-01 – 2027-11-30 (bieżące zarządzanie)
- 1/2 etatu: 2027-12-01 – 2027-12-31 (zamknięcie projektu, sprawozdanie)

### Implikacje dla planu implementacji kursu

- Zadanie 6 (RODO) kończy się **do 2026-04-15** — procedury RODO MUSZĄ być gotowe
  zanim kurs tartakowy zacznie zbierać dane uczestników. Jeśli kurs startuje przed
  tą datą, ryzyko niezgodności. Bezpieczna data startu zbierania danych: **po 2026-04-15**.
- Monitor interaktywny (tablica multimedialna w sali Opole) gotowy **do 2026-03-31** —
  kurs może być prezentowany stacjonarnie w tej sali od Q2 2026.
- Sala szkoleniowa w Opolu (20 krzeseł, stół konferencyjny) gotowa **do 2026-05-09** —
  ewentualne szkolenia stacjonarne z wykorzystaniem sali możliwe od maja 2026.
- Wskaźniki rezultatu mierzone **w ciągu 4 tygodni od zakończenia udziału w projekcie**
  (s. 18) — kurs e-learningowy musi generować automatyczne potwierdzenia (zaświadczenia)
  niezwłocznie po ukończeniu, nie „przy następnej okazji".

---

## 7. Placeholdery do prospektu (Faza 8)

Elementy, które muszą być w prospekcie — wynikające z wniosku EFS+:

- `{{PROJEKT_NAZWA}}` — „Budowa fundamentów pod lokalną politykę migracyjną i integracyjną"
- `{{PROJEKT_NUMER}}` — FEOP.06.03-IZ.00-0006/25
- `{{PROJEKT_OKRES}}` — 2026-01-01 – 2027-12-31
- `{{PROJEKT_WARTOSC_OGOLEM}}` — 500 000,00 zł
- `{{PROJEKT_DOFINANSOWANIE}}` — 475 000,00 zł (95%)
- `{{PROJEKT_DOFINANSOWANIE_EFS}}` — 425 000,00 zł (85%)
- `{{BENEFICJENT_LIDER}}` — Fundacja na rzecz Edukacji SMART, ul. Ozimska 14-16/314A, 45-057 Opole
- `{{BENEFICJENT_PARTNER}}` — Fundacja pomocy prawnej EGIDA, ul. Ozimska 14-16/314A, 45-057 Opole
- `{{PROGRAM}}` — Fundusze Europejskie dla Opolskiego 2021-2027, Działanie 06.03
- `{{CO_FUNDED_CLAUSE}}` — „Projekt finansowany ze środków Europejskiego Funduszu
  Społecznego Plus w ramach programu Fundusze Europejskie dla Opolskiego 2021–2027"
  *(pełna treść — do weryfikacji w dokumentach IZ)*
- `{{UE_LOGO_BLOCK}}` — trzy znaki: logo FE dla Opolskiego + barwy RP + flaga UE
  *(pliki graficzne — do pobrania z portalu Funduszy Europejskich)*
- `{{GRUPY_DOCELOWE}}` — „pełnoletni migranci zamieszkali lub pracujący w woj. opolskim,
  ze szczególnym uwzględnieniem obywateli Ukrainy i Kolumbii"
- `{{CEL_PROJEKTU}}` — krótki opis one-stop-shop (patrz sekcja 1 powyżej)
- `{{LOKALIZACJA}}` — Opole (docelowo też Kluczbork), woj. opolskie
- `{{STRONA_SMART}}` — https://fundacjasmart.pl/
- `{{STRONA_EGIDA}}` — https://fundacjaegida.eu/

---

## 8. Placeholdery do umów/zaświadczeń (Podprojekt B)

Elementy, które muszą być w dokumentach administracyjnych:

### Zaświadczenie o ukończeniu szkolenia/kursu

- `{{UCZESTNIK_IMIE_NAZWISKO}}` — imię i nazwisko uczestnika
- `{{UCZESTNIK_DATA_UR}}` — data urodzenia (opcjonalnie — do uzgodnienia z prawnikiem EGIDY)
- `{{KURS_NAZWA}}` — nazwa kursu (np. „BHP w zakładach tartacznych i stolarni")
- `{{KURS_GODZINY_OGOLEM}}` — łączna liczba godzin kursu
- `{{KURS_DATA_UKONCZENIA}}` — data ukończenia kursu
- `{{KURS_WYNIK}}` — wynik procentowy (opcjonalnie)
- `{{ORGANIZACJA_NAZWA}}` — Fundacja pomocy prawnej EGIDA
- `{{ORGANIZACJA_NIP}}` — 7543348716
- `{{ORGANIZACJA_KRS}}` — 0000957190
- `{{PODPISUJACY_IMIE_NAZWISKO}}` — osoba uprawniona do podpisu
- `{{PODPISUJACY_STANOWISKO}}` — stanowisko
- `{{PROJEKT_NUMER}}` — FEOP.06.03-IZ.00-0006/25
- `{{CO_FUNDED_CLAUSE}}` — klauzula EFS+
- `{{UE_LOGO_BLOCK}}` — blok logotypów UE

### Umowa o uczestnictwo w kursie

- `{{UCZESTNIK_IMIE_NAZWISKO}}`
- `{{UCZESTNIK_ADRES}}`
- `{{UCZESTNIK_NR_DOKUMENTU}}` — nr paszportu lub karty pobytu (do weryfikacji kwalifikowalności)
- `{{UCZESTNIK_OBYWATELSTWO}}`
- `{{KURS_NAZWA}}`
- `{{KURS_DATA_START}}`
- `{{KURS_DATA_KONIEC}}`
- `{{KURS_GODZINY_OGOLEM}}`
- `{{KURS_FORMA}}` — e-learning / stacjonarny / mieszany
- `{{ZGODA_RODO_PROJEKT}}` — zgoda na przetwarzanie danych w celach realizacji projektu EFS+ (obligatoryjna)
- `{{ZGODA_RODO_MONITORING}}` — zgoda na udostępnienie danych do IZ (obligatoryjna)
- `{{ZGODA_FOLLOWUP}}` — zgoda na kontakt follow-up po zakończeniu kursu (opcjonalna)
- `{{ZGODA_WIZERUNEK}}` — zgoda na publikację wizerunku (opcjonalna)
- `{{KLAUZULA_RODO_PELNA}}` — pełna klauzula informacyjna RODO
- `{{CO_FUNDED_CLAUSE}}`
- `{{UE_LOGO_BLOCK}}`
- `{{ORGANIZACJA_NAZWA}}`
- `{{DATA_ZAWARCIA_UMOWY}}`
- `{{MIEJSCE_ZAWARCIA_UMOWY}}`

### Karta uczestnika (wewnętrzna)

- `{{UCZESTNIK_IMIE_NAZWISKO}}`
- `{{UCZESTNIK_EMAIL}}`
- `{{UCZESTNIK_STATUS_ZAWODOWY}}` — poszukujący pracy / pracujący / inne
- `{{UCZESTNIK_STATUS_POBYTOWY}}` — obywatel / karta pobytu / inne (nie kopiujemy dokumentu)
- `{{KURS_WYNIK_PRETEST}}`
- `{{KURS_WYNIK_POSTTEST}}`
- `{{KURS_DATA_UKONCZENIA}}`
- `{{DATA_WYPELNIENIA}}`

---

## Uwagi końcowe — braki i luki do uzupełnienia

1. ~~**Kurs tartakowy nie jest explicite wymieniony w wniosku** — jest efektem docelowym
   budowania potencjału, nie zadaniem projektowym. Czy kurs będzie formalnie powiązany
   z projektem (i tym samym objęty wymogami EFS+) — **do decyzji koordynatora projektu**.~~
   **ROZSTRZYGNIĘTE 2026-04-16:** kurs traktowany jako działanie projektowe (opcja C „hybryda"),
   oznaczenia UE obowiązkowe, implementacja przez placeholdery. Zob. nota na górze dokumentu.

2. **Pełna klauzula oznakowania EFS+** (dokładna treść i kolejność logotypów) — brak
   w tekście wniosku, odsyła do *Podręcznika wnioskodawcy*. Pobrać z portalu:
   https://www.funduszeeuropejskie.gov.pl lub od IZ (Urząd Marszałkowski Woj. Opolskiego).

3. **Wymogi dotyczące certyfikacji kursów zawodowych** (np. czy ukończenie kursu e-learningowego
   może być podstawą do wystawienia zaświadczenia uznawanego przez pracodawców lub PUP) —
   **nie wynika wprost z wniosku**. Sprawdzić u koordynatora lub prawnika EGIDY.

4. **Wskaźnik godzin teorii vs. praktyki** — wniosek wymienia 12-godzinne szkolenie
   z prawa cudzoziemców (Zadanie 5, s. 43), ale nie określa wymaganego podziału godzin
   dla kursów zawodowych. **Sprawdzić w wytycznych programu i u koordynatora**.

5. **Ankieta follow-up** — wniosek wspomina o ewaluacji (pre-test, post-test), ale nie
   definiuje dokładnego narzędzia. Projekt formularza ankiety follow-up: **do opracowania
   w fazie B** (Podprojekt B: dokumenty administracyjne).

---

*Plik wygenerowany automatycznie w ramach Task 1.2. Wchodzi do `analiza-merytoryczna/`, nie do `dist/`.*
*Następny krok: Task 1.3 — lista luk do web researchu.*
