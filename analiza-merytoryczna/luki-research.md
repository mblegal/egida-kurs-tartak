# Luki merytoryczne do uzupełnienia przez web research

**Zadanie:** Task 1.3 — Part 1 (Analiza merytoryczna)
**Data analizy:** 2026-04-16
**Input:** `analiza-pdf.md` (5 luk zidentyfikowanych w Task 1.1) + `analiza-wniosku-efs.md` (uzupełnienie LUKA 3)
**Cel:** Operacyjna checklist do Task 1.4 (pierwszy przebieg researchu luk krytycznych) i do późniejszych iteracji w Częściach 5–7 (produkcja treści).

> Szczegółowy opis każdej luki (zakres tematyczny, podejście do pokrycia) zob. `analiza-pdf.md`,
> sekcja „Zidentyfikowane luki tematyczne" (linie 344–383). Niniejszy plik zawiera
> **operacyjne queries i ocenę źródeł** — nie duplikuje tamtej analizy.

---

## Priorytetyzacja (kolejność researchu)

| # | Luka | Priorytet | Moduł(y) | Blok(i) | Kiedy zrobić |
|---|------|-----------|----------|---------|--------------|
| 1 | Suszenie drewna | 🔴 KRYTYCZNY | M2, M3 | M, P | **Task 1.4** (teraz) |
| 2 | Maszyny tartaczne — obsługa operatora | 🔴 KRYTYCZNY | M1, M2 | P | **Task 1.4** (teraz) |
| 3 | Prawo pracy + prawa migranta | 🟡 WAŻNY | M1, M3 | B, O | Przed produkcją M1 tydz. 4 (blok O) |
| 4 | Stolarka meblowa i wykończeniowa | 🟢 MAŁY | M3 | P | Przed produkcją M3 tydz. 3 |
| 5 | Certyfikaty i normy PN-EN / FSC | 🟢 MAŁY | M2, M3 | O | Przed produkcją M2 tydz. 4 |

---

## LUKA 1 — Suszenie drewna

**Priorytet:** 🔴 KRYTYCZNY (M3 blok P bez suszenia nie powstanie; suszarnia jest kluczową operacją tartaku przemysłowego)

**Moduły i bloki dotknięte:**
- M2 blok P (tydz. 3) — wprowadzenie do procesu suszenia pod nadzorem operatora
- M3 blok M (tydz. 2) — teoria wilgotności i jej wpływ na właściwości mechaniczne drewna
- M3 blok P (tydz. 3) — samodzielna obsługa suszarni komorowej

**Czego konkretnie szukamy:**
- Typy suszarni (komorowa, tunelowa, próżniowa, mikrofalowa) — różnice konstrukcyjne, zastosowania, skala produkcji
- Parametry procesu: temperatura (°C), wilgotność względna powietrza (%), prędkość nawiewu (m/s), ciśnienie (dla próżniowych), czas cyklu
- Krzywe suszenia dla gatunków iglastych (sosna, świerk) i liściastych (dąb, buk, brzoza) — tabele lub wykresy
- Wady suszenia: pęknięcia suszarnicze (czołowe, powierzchniowe, wewnętrzne), deformacje (paczenie, łukowatość, skręt), zabarwienia (sinienie, czernienie)
- Kontrola wilgotności w trakcie procesu — wilgotnościomierz oporowy vs. kontaktowy vs. pojemnościowy
- Obsługa sterownika suszarni: interfejs operatora, wybór programu, alarmy, zapis danych

### Sugerowane zapytania webowe

**Polskie (urzędowe i branżowe):**
1. `"suszarnia komorowa" drewno parametry temperatura wilgotność "krzywa suszenia"`
2. `suszenie drewna tartacznego gatunki iglaste liściaste czas temperatura tabela`
3. `wady suszenia drewna "pęknięcia suszarnicze" deformacje przyczyny zapobieganie`
4. `obsługa sterownika suszarni drewna instrukcja użytkownika`
5. `wilgotnościomierz drewna oporowy kontaktowy kalibracja pomiar`

**Angielskie (szersze źródła techniczne i normatywne):**
1. `wood kiln drying schedule pine oak beech temperature humidity table`
2. `lumber drying defects checks warp blue stain causes prevention`
3. `wood moisture meter pin pinless accuracy calibration industrial`
4. `industrial wood dryer control panel HMI operation manual`
5. `wood drying kiln types chamber tunnel vacuum comparison`

### Sugerowane źródła

| Źródło | Typ | Wiarygodność | Uwagi |
|--------|-----|--------------|-------|
| PKN — pkn.pl | standardy | 🟢 urzędowe | PN-EN 13183-1/2 (wilgotność tarcicy), PN-EN 14298 (ocena drewna) |
| CIOP-PIB — ciop.pl | naukowo-branżowe | 🟢 wysokie | publikacje o procesach technologicznych w przemyśle drzewnym |
| Nardi Impianti (nardi.it) | producent | 🟢 wysokie | dokumentacje techniczne suszarni komorowych; perspektywa dostawcy — weryfikować niezależnie |
| Mühlböck (muehlboeck.com) | producent | 🟢 wysokie | szczegółowe materiały techniczne (krzywe suszenia, sterowniki) |
| Brunner Hildebrand (b-h.de) | producent | 🟢 wysokie | literatura techniczna dostępna do pobrania |
| Instytut Technologii Drewna — ithd.pl | badawcze | 🟢 wysokie | raporty naukowe w języku polskim |
| „Przemysł Drzewny" — przemysldrzewny.pl | branżowe | 🟢 wysokie | artykuły praktyczne dla branży; dostępne archiwum |
| Wood Drying — USDA Forest Service (fpl.fs.usda.gov) | rządowe USA | 🟢 wysokie | Handbook of drying, angielski, bezpłatny PDF |
| Wikipedia PL: „Suszenie drewna" | ogólne | 🟡 orientacyjne | wyłącznie do wstępnego rozpoznania pojęć; NIE cytować jako źródło |
| YouTube (producenci suszarni) | wideo | 🟡 zmienna | wizualizacja procesu i obsługi sterownika; uważać na treści nieautoryzowane |

**Wyniki zapisywać w:** `web-research/suszenie-drewna.md`

---

## LUKA 2 — Maszyny tartaczne (obsługa z perspektywy operatora)

**Priorytet:** 🔴 KRYTYCZNY (M1 blok P i M2 blok P wymagają procedur operacyjnych, nie tylko teorii konstrukcji maszyn)

**Moduły i bloki dotknięte:**
- M1 blok P (tydz. 2–3) — praca pod nadzorem przy obsłudze podstawowych maszyn
- M2 blok P (tydz. 2–3) — obsługa samodzielna pilarki taśmowej i pomocniczych maszyn

**Czego konkretnie szukamy:**
- Pilarka taśmowa pionowa: uruchamianie, regulacja prowadnic, napięcie taśmy, wymiana taśmy tnącej, zatrzymanie awaryjne
- Pilarka wielopiłowa (trakownica): nastawianie szerokości cięcia, wymiana pił, czyszczenie, procedura rozruchu
- Okrawiarka (edger): ustawianie szerokości, obsługa w ciągu technologicznym
- Strugarko-wyrównarka przemysłowa: głębokość skrawania, wymiana noży, kierunek podawania, blokady
- Sytuacje awaryjne: zakleszczenie materiału, zerwanie taśmy/piły, zadziałanie wyłącznika awaryjnego
- Oznaczenia na maszynach: tabliczki BHP, strefy zagrożenia, wymagany PPE

### Sugerowane zapytania webowe

**Polskie:**
1. `pilarka taśmowa pionowa obsługa operatora instrukcja uruchamianie zatrzymanie`
2. `"pilarka wielopiłowa" trakownica regulacja nastawianie obsługa`
3. `okrawiarka drewno obsługa ustawianie szerokości cięcia instrukcja`
4. `strugarko-wyrównarka przemysłowa wymiana noży obsługa BHP`
5. `maszyny tartaczne BHP sytuacje awaryjne wyłącznik bezpieczeństwa`

**Angielskie:**
1. `band saw vertical mill operator guide blade tension tracking adjustment`
2. `multi-blade gang saw lumber setup operation manual`
3. `edger sawmill width setting operation procedure`
4. `industrial planer jointer blade change safety procedure`
5. `sawmill emergency stop jammed lumber blade breakage procedure`

### Sugerowane źródła

| Źródło | Typ | Wiarygodność | Uwagi |
|--------|-----|--------------|-------|
| Wood-Mizer (woodmizer.pl / woodmizer.com) | producent | 🟢 wysokie | instrukcje obsługi pił taśmowych; wersje PL i EN dostępne online |
| Ustrojczuk (ustrojczuk.pl) | producent PL | 🟢 wysokie | maszyny tartaczne i stolarskie; materiały techniczne w języku polskim |
| ISAP — legislacja.gov.pl | urzędowe | 🟢 urzędowe | Rozporządzenie MG 2002 (BHP przy obróbce drewna) — przepisy dot. maszyn |
| PIP — pip.gov.pl | urzędowe | 🟢 urzędowe | poradniki BHP dla tartaków, karty BHP maszyn |
| CIOP-PIB — ciop.pl | naukowo-branżowe | 🟢 wysokie | baza danych maszyn, karty oceny ryzyka |
| YouTube: kanały producentów (Wood-Mizer, Ustrojczuk) | wideo | 🟡 zmienna | filmy instruktażowe operatorów; weryfikować daty i model maszyny |
| Serwisy aukcyjne (maszyny.pl, mascus.pl) | handlowe | 🔴 orientacyjne | tylko dla zdjęć i nazw modeli; NIE jako źródło procedur obsługi |

**Wyniki zapisywać w:** `web-research/maszyny-tartaczne.md`

---

## LUKA 3 — Prawo pracy i prawa migranta

**Priorytet:** 🟡 WAŻNY (szczególnie istotne dla grupy docelowej — migrantów UA i ES w woj. opolskim)

**Moduły i bloki dotknięte:**
- M1 blok O (tydz. 4) — wprowadzenie do prawa pracy w Polsce dla nowego pracownika
- M3 blok B (tydz. 1) — przepisy BHP specyficzne dla tartaku (Rozp. MG 2002)
- M3 blok O (tydz. 4) — prawa i obowiązki pracownicze na poziomie samodzielnego pracownika

**Czego konkretnie szukamy:**

*Podtemat A — Prawo pracy ogólne (PL):*
- Rodzaje umów o pracę (o pracę, zlecenie, o dzieło) — różnice, co wybrać, jak czytać umowę
- Minimalne wynagrodzenie, termin wypłaty, pasek płacowy
- Urlop wypoczynkowy (wymiar, nabywanie prawa), choroba (zwolnienie L4, ZUS)
- Obowiązki pracodawcy: BHP, szkolenia, badania lekarskie

*Podtemat B — Prawa cudzoziemca w Polsce:*
- Zezwolenie na pracę typ A — kto wydaje (Urząd Wojewódzki), czas oczekiwania, wymagane dokumenty
- Oświadczenie o powierzeniu pracy (uproszczona ścieżka dla obywateli UA po 24.02.2022)
- Rejestracja w ZUS przez pracodawcę — co powinien dostać pracownik (zgłoszenie ZUA)
- PESEL dla cudzoziemca — jak uzyskać
- Gdzie szukać pomocy: PIP, PUP, UdSC (Urząd do Spraw Cudzoziemców)

*Podtemat C — Przepisy BHP specyficzne dla tartaków:*
- Rozporządzenie Ministra Gospodarki z dnia 19.08.2002 r. w sprawie BHP przy obróbce drewna (Dz. U. 2002 nr 148 poz. 1247) — kluczowe paragrafy (§12–§40: maszyny, §5–§11: ogólne)

### Sugerowane zapytania webowe

**Polskie:**
1. `"zezwolenie na pracę typ A" cudzoziemiec Polska wymagane dokumenty procedura 2024`
2. `oświadczenie o powierzeniu pracy Ukrainiec PUP rejestracja 2024`
3. `prawa pracownicze cudzoziemca Polska umowa o pracę urlop wynagrodzenie PIP`
4. `"Rozporządzenie Ministra Gospodarki" 2002 BHP obróbka drewna tartak pełny tekst`
5. `PESEL cudzoziemiec Polska jak uzyskać wniosek urząd gminy`

**Angielskie / ukraińskie (materiały dla migrantów):**
1. `work permit type A Poland foreigner application procedure 2024 English`
2. `employee rights Poland migrant labor law English guide`
3. `"prawa pracownika" ukraiński język PIP poradnik` *(cyrylicą: „права працівника Польща")*

### Sugerowane źródła

| Źródło | Typ | Wiarygodność | Uwagi |
|--------|-----|--------------|-------|
| ISAP — legislacja.gov.pl | urzędowe | 🟢 urzędowe | pełny tekst Rozp. MG 2002 (Dz. U. 2002 nr 148 poz. 1247) |
| PIP — pip.gov.pl | urzędowe | 🟢 urzędowe | poradniki wielojęzyczne (PL/UA/EN/ES), w tym „Pracownik z zagranicy w Polsce" |
| ZUS — zus.pl | urzędowe | 🟢 urzędowe | informacje o zgłoszeniu do ubezpieczeń, formularz ZUA |
| Urząd Wojewódzki Opolski — opolskie.uw.gov.pl | urzędowe | 🟢 urzędowe | procedury zezwoleń na pracę dla woj. opolskiego |
| UdSC — udsc.gov.pl | urzędowe | 🟢 urzędowe | Urząd do Spraw Cudzoziemców; informacje o statusie pobytu, PESEL |
| PUP Opole — pupopole.pl | urzędowe | 🟢 urzędowe | rejestracja oświadczeń o powierzeniu pracy dla Ukraińców |
| Infor.pl / kadry.infor.pl | prawno-branżowe | 🟡 orientacyjne | artykuły komentarzowe do przepisów; pomocne do zrozumienia, ale NIE cytować zamiast urzędowego źródła |
| Wikipedia PL: „Umowa o pracę" | ogólne | 🟡 orientacyjne | wyłącznie orientacja; weryfikować z Kodeksem pracy |

**Wyniki zapisywać w:** `web-research/prawo-pracy-migrant.md`

---

## LUKA 4 — Stolarka meblowa i wykończeniowa

**Priorytet:** 🟢 MAŁY (dotyczy tylko M3 blok P, tydz. 3; kurs może ten temat potraktować skrótowo)

**Moduły i bloki dotknięte:**
- M3 blok P (tydz. 3) — produkty końcowe z tarcicy: stolarka, meble, elementy budowlane

**Czego konkretnie szukamy:**
- Typy wyrobów z tarcicy tartakowej: stolarka okienna i drzwiowa, więźba dachowa, podłogi, meble surowe
- Podstawowe połączenia stolarskie: czop i gniazdo, wpust i pióro, kołek drewniany, złącze na wkręty
- Obróbka powierzchniowa: lakierowanie, bejcowanie, impregnacja (ciśnieniowa vs. powłokowa), olejowanie
- Wymagania jakościowe dla wyrobów końcowych (klasy wilgotności, tolerancje wymiarowe)

### Sugerowane zapytania webowe

**Polskie:**
1. `stolarka okienna drzwiowa drewniana produkcja wymagania jakościowe tarcica`
2. `"połączenia stolarskie" czop wpust kołek rodzaje zastosowanie stolarz`
3. `impregnacja drewna ciśnieniowa powłokowa rodzaje środków preparaty`
4. `lakierowanie drewna tartacznego rodzaje lakierów technologia wykończenie`
5. `więźba dachowa elementy nazwy tarcica tartakowa wymiary sortyment`

**Angielskie:**
1. `woodworking joints mortise tenon dowel applications furniture`
2. `wood surface treatment staining lacquering varnishing pressure impregnation`
3. `sawn timber products end use windows doors flooring furniture`

### Sugerowane źródła

| Źródło | Typ | Wiarygodność | Uwagi |
|--------|-----|--------------|-------|
| PKN — pkn.pl | standardy | 🟢 urzędowe | PN-EN 942 (drewno w stolarce), PN-EN 14915 (okładziny drewniane) |
| Instytut Technologii Drewna — ithd.pl | badawcze | 🟢 wysokie | artykuły o impregnacji i ochronie drewna |
| Stowarzyszenie Przemysłu Drzewnego | branżowe | 🟢 wysokie | materiały o wyrobach drzewnych; sprawdzić aktualność |
| Poradniki DYI / szkolne ZSZ | edukacyjne | 🟡 orientacyjne | do ogólnego oglądu połączeń stolarskich; weryfikować dokładność terminologii |
| Wikipedia PL: „Stolarka budowlana" | ogólne | 🟡 orientacyjne | wstępna orientacja w typach wyrobów |

**Wyniki zapisywać w:** `web-research/stolarka-meblowa.md`

---

## LUKA 5 — Certyfikaty i normy PN-EN / FSC / PEFC

**Priorytet:** 🟢 MAŁY (M2–M3 blok O; wystarczy jedna lekcja na moduł — przegląd, nie egzamin z norm)

**Moduły i bloki dotknięte:**
- M2 blok O (tydz. 4) — co to jest certyfikat jakości, po co pracodawca go wymaga
- M3 blok O (tydz. 4) — sortowanie tarcicy wg norm, dokumentacja jakościowa

**Czego konkretnie szukamy:**
- Normy sortowania tarcicy: PN-EN 1611-1 (tarcica iglasta wizualnie), PN-EN 14081 (wytrzymałościowo) — klasy C16/C24/C35
- FSC i PEFC: co to jest, certyfikat łańcucha dostaw (CoC), dlaczego klient/eksporter wymaga
- Klasy jakości tarcicy tartakowej w praktyce: A/B/C/D lub I/II/III — oznaczenia na sztaplach
- Znakowanie tarcicy (CE, klasa, producent) — jak czytać oznaczenia na desce

### Sugerowane zapytania webowe

**Polskie:**
1. `"PN-EN 14081" tarcica sortowanie wytrzymałościowe klasy C16 C24 C35 Polska`
2. `certyfikat FSC PEFC tartak Polska "łańcuch dostaw" CoC wymagania`
3. `klasy jakości tarcicy wizualnej oznaczenia A B C D Polska norma`
4. `"PN-EN 1611" tarcica iglasta sortowanie wizualne klasy`
5. `znakowanie tarcicy CE oznaczenie co oznacza klasa wytrzymałości`

**Angielskie:**
1. `EN 14081 structural timber grading classes C16 C24 C35 explained`
2. `FSC PEFC chain of custody certification sawmill requirements`
3. `sawn timber grading visual strength marking CE explained`

### Sugerowane źródła

| Źródło | Typ | Wiarygodność | Uwagi |
|--------|-----|--------------|-------|
| PKN — pkn.pl | standardy | 🟢 urzędowe | PN-EN 1611-1, PN-EN 14081, PN-EN 336 (wymiary) — kupno lub biblioteka |
| FSC Polska — pl.fsc.org | urzędowe/branżowe | 🟢 wysokie | opis certyfikatu FSC CoC po polsku, darmowe materiały informacyjne |
| PEFC Polska — pefc.pl | urzędowe/branżowe | 🟢 wysokie | analogicznie do FSC |
| Procons / TKDK — certyfikatory | branżowe | 🟡 orientacyjne | artykuły wyjaśniające normy; komercyjne, ale merytorycznie poprawne |
| European Organisation for Technical Assessment — eota.eu | europejskie | 🟢 wysokie | dokumenty dot. znakowania CE dla wyrobów drzewnych |
| Wikipedia PL: „FSC" / „Tarcica" | ogólne | 🟡 orientacyjne | orientacja wstępna |

**Wyniki zapisywać w:** `web-research/certyfikaty-normy.md`

---

## Uwagi końcowe

### Co NIE jest zadaniem web researchu (tory osobne)

- **Pełna klauzula widoczności UE i Księga Identyfikacji Wizualnej FE Opolskie 2021–2027** —
  kontakt z koordynatorem projektu SMART+EGIDA lub Urzędem Marszałkowskim Woj. Opolskiego.
  Zob. `analiza-wniosku-efs.md`, punkt 2 sekcji „Uwagi końcowe". NIE szukamy tego w Google.
- **Wymogi certyfikacji e-learningu przez PUP / Ministerstwo** (czy zaświadczenie będzie uznawane
  przez pracodawców) — pytanie do prawnika EGIDY lub koordynatora, nie do researchu.
  Zob. `analiza-wniosku-efs.md`, punkt 3 sekcji „Uwagi końcowe".
- **Konkretne parametry BHP dla konkretnych maszyn w konkretnym tartaku partnerskim** —
  wymaga wywiadu bezpośredniego z tartakiem partnerskim, nie web researchu.

### Zasady pracy z web researchem (dla Task 1.4 i późniejszych)

1. **Zawsze notuj URL, datę pobrania i parafrazę kluczowej informacji** — nie kopiuj całych akapitów.
2. **Oznaczaj wiarygodność źródła:** 🟢 urzędowe/branżowe, 🟡 orientacyjne, 🔴 nieautoryzowane.
3. **Cytat dosłowny tylko krótki (do 15 słów), w cudzysłowie, z URL i datą.**
4. **Jeśli źródło jest komercyjne (producent maszyny, suszarni)** — zaznacz perspektywę dostawcy;
   dla równowagi szukaj alternatywnego źródła niezależnego (CIOP, ITD, urzędowego).
5. **Wyniki każdej luki zapisuj w osobnym pliku** `web-research/<nazwa-tematu>.md`,
   nie bezpośrednio w tym dokumencie.
6. **Kolejność pracy:** zob. tabela priorytetyzacji na początku. Task 1.4 obejmuje wyłącznie LUKA 1 i LUKA 2.

---

*Plik wygenerowany automatycznie w ramach Task 1.3. Input do Task 1.4.*
