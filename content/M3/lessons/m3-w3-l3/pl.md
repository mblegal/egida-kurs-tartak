---
id: m3-w3-l3
blok: procesy
czas: 120
---

## Wprowadzenie

Czwartek, 2026-05-29, godzina 14:00. Rustam stoi w **hali suszarni** EGIDA, osobnym budynku 12 × 8 × 4,5 m, oddzielonym od hali pilarek 30-metrowym placem magazynowym. Wnętrze jest gorące (28-30°C, choć komora pracuje, hala dostaje ciepło przez izolację), powietrze ma charakterystyczny zapach mokrego dębu (od 12 dni w cyklu), hałas wentylatorów wyciągowych równy, 55-60 dB. Dzisiejsze zadanie, **narada planistyczna** nad kolejną wsadką komory: kiedy, co, w jakim programie, na jak długo.

W hali są trzy osoby: **Pan Henryk** (62 l., mistrz suszarni EGIDA, emeryt sezonowy, od marca do listopada pracuje w EGIDA, od grudnia do lutego zimuje w domu pod Ełkiem; 38 lat doświadczenia w suszarnictwie, w tym 22 w mazurskich tartakach), **Marek Kowalski** (brygadzista) i **Rustam Nazarov** (operator samodzielny M3, obecność w tej naradzie jest planową częścią jego szkolenia M3, ostatnia część bloku procesowego). Wahana nie ma (M1 ma dziś zmianę konserwacyjną w hali pilarek, nie zaplanowane szkolenie suszarnicze).

Planowanie kampanii suszarniczej nie jest kompetencją operatora M3 w sensie „decydującym". **Mistrz suszarni decyduje**. Operator M3 **uczestniczy, dostarcza informacje, dokumentuje**. To jest różnica, którą Rustam dziś uczy się przeżywać: **nie każda decyzja produkcyjna, w której uczestniczy operator samodzielny, jest decyzją operatora samodzielnego**. W niektórych obszarach (suszenie, regulacja elektryczna, zmiana programu sterownika) operator **asystuje specjaliście**, a nie prowadzi.

### 14:05, stan komory obecny

Pan Henryk otwiera drzwi do **hali sterowania suszarni** (pomieszczenie 2 × 3 m z szafą sterowniczą i oknami obserwacyjnymi na komorę). Panel sterowania z ekranem LCD pokazuje stan:

```
Komora: BH-50 (Brunner-Hildebrand, 50 m³ brutto, 38 m³ netto tarcicy)
Wsadka bieżąca: dąb szypułkowy 2,5 m³, deski 30 mm, start 2026-05-17
Dzień cyklu: 13 z 22 (fazy: nagrzewanie 2d, główne 14d, kondycjonowanie 4d, chłodzenie 2d)
Aktualna faza: główne suszenie, dzień 11 z 14

Temperatura powietrza:        58°C  (cel 60°C, tolerancja ±3)
Wilgotność względna (RH):     42%   (cel 40%, tolerancja ±5)
Wilgotność drewna próba 1:    28,4% (start 38%)
Wilgotność drewna próba 2:    27,9% (start 37,6%)
Wilgotność drewna próba 3:    29,1% (start 38,5%, wolniej schnie)
EMC (wilgotność równowagowa): 7,1%  (target końcowy dębu: 14%)

Planowane zakończenie: sobota 2026-06-07, wyjście tarcicy w poniedziałek 2026-06-09.
```

Pan Henryk komentuje na głos, pół do Marka, pół do Rustama:

*„Dąb idzie normalnie. Wilgotność spada, jak powinna. 28% dzień 11 to w planie, do 14% dojdziemy za 9 dni. Weekend nie ingeruje, komora pracuje sama, sterownik na automatyce. Sobotę-niedzielę Maciek przyjdzie odczytać i zapisać w dzienniku, jak każdy weekend."*

Maciek to pomocnik suszarni, M1 w EGIDA, uczy się pod Panem Henrykiem (nie Maciek Petrosjan, inny Maciek, Maciej Wiśniewski, 19 l., druga klasa technikum drzewnego Ostróda, praktyki w EGIDA).

*„Poniedziałek 9-go wypuszczamy dąb, stos na dzielnicy chłodzenia, potem klasyfikacja. Wtorek 10-go komora **pusta**. Od wtorku nowy program."*

Marek potakuje. Rustam patrzy na panel i notuje dane w kalendarzyku kieszonkowym (dla siebie, nie w KDP-001, bo nie jest dokument produkcyjny lecz planowanie).

### 14:15, co jest do wsadki

Marek wyjmuje notatnik brygadzisty, czyta listę tarcicy świeżej w magazynie tartaku, oczekującej na suszenie:

```
Stan świeżej tarcicy oczekującej w magazynie suszenia (z Kart WZ od klasyfikatorów):

A. Sosna zwyczajna, deski 28 × 155 × 4050 mm, świeża 28-32%:
   - ZLE-2026-05-077 (Rustam, ZLE wewn. ZLE-077): 0,58 m³
   - ZLE-2026-05-079 (Damian, piątek 23.05): 0,72 m³
   - Nadwyżki magazynu (materiał cięty wiosną do klasyfikacji): 1,12 m³
   Razem sosna: 2,42 m³

B. Dąb szypułkowy, deski 28 × 155 × 4050 mm, świeży 35-38%:
   - ZLE-2026-05-081 (Rustam, poniedziałek 26.05 kampania nowa dębowa): 0,38 m³
   - ZLE-2026-05-075 (Rustam, 12-14.05 z Part 25, tarcica w magazynie od 15.05): 1,84 m³
   Razem dąb: 2,22 m³

C. Buk zwyczajny, deski 25 × 130 × 4000 mm, świeży 32%:
   - Klient Stolarz Meblowy z Mrągowa, zlecenie ZLE-2026-05-082: 0,68 m³
   Razem buk: 0,68 m³

D. Brzoza (resztki z zimy, niska priorytet): 0,42 m³

SUMA WSZYSTKIEGO: 5,74 m³ w magazynie tartaku do suszenia.
```

Pan Henryk krzyczy krótko: *„Pięć i trzy czwarte metra sześciennego. Komora ma 38 metrów netto. To jest **15% wypełnienia**, za mało do cyklu."*

Tu zaczyna się główny problem narady. Komora suszarnicza BH-50 jest zaprojektowana do pracy przy **80-100% wypełnienia** (30-38 m³ netto). Przy 15% wypełnienia:

- Przepływ powietrza jest zbyt szybki (brak oporu, wentylatory tylko „przewiewają")
- Temperatura nie stabilizuje się równomiernie w komorze (konwencja konwekcyjna nierównomierna)
- Zużycie energii na metr sześcienny jest 3-4 razy wyższe (prądu, gazu na grzejniki, serwisu)
- Program suszarniczy (kalibrowany dla pełnej wsadki) daje wyniki niestandardowe, ryzyko pęknięć rdzeniowych w desce rośnie

Pan Henryk kontynuuje: *„Mamy trzy opcje. Słuchaj, Rustam, bo to jest dokładnie to, co kiedyś sam będziesz musiał oceniać jako przyszły mistrz, jeżeli pójdziesz tą ścieżką."*

### 14:25, trzy opcje i kompromisy

**Opcja A, czekać na pełną wsadkę.** Nie uruchamiać komory dopóki nie mamy 30+ m³ tarcicy w magazynie. EGIDA przerabia **~3 m³/zmianę** (jedna osoba na jednej maszynie), przy 5 dniach roboczych i 2 pilarkach to **30 m³/tydzień teoretycznie**, w praktyce (sortowanie, klasyfikacja, awarie, weekendy) **~22 m³/tydzień**. Od dziś do pełnej wsadki 30 m³: dzisiaj 5,74 m³, trzeba 24 m³ więcej, czyli **8-10 dni roboczych**, czyli ~**13 dni kalendarzowych**. Wsadka gotowa około **2026-06-11 środa**.

Zalety: ekonomia optymalna, cykl program trzyma, jakość suszenia najlepsza.
Wady: **ZLE-077 klient oczekuje odbioru 2026-06-20** (od dziś 22 dni). Cykl suszenia 8-9 dni plus obróbka końcowa plus wydanie 3 dni = 11-12 dni od startu suszenia. Czyli start najpóźniej **2026-06-08 poniedziałek**. Z opcją A start byłby 11-go, za późno o 3 dni.

**Opcja B, zlecenie zewnętrzne dla części tarcicy.** EGIDA ma umowę z suszarnią **„Drew-Sus"** w Mrągowie (40 km od Strzałowa), stawki 2026:

- Suszenie sosny deski 25-30 mm: **180 zł/m³**, cykl 7-9 dni u nich
- Transport tam-z-powrotem dla ciężarówki kontenerowej (3-5 m³ wsadki): **350 zł za kurs**
- Razem dla partii 3 m³: 540 zł suszenie + 350 zł transport = **890 zł / 3 m³ = 297 zł/m³**

Dla ZLE-077 (0,58 m³) partia osobna: za mała dla osobnego kursu. Trzeba by scalić z ZLE-079 sosna 0,72 m³ i Damian sosna 1,12 m³ = 2,42 m³ łącznie. Plus dąb jeżeli ta sama suszarnia akceptuje (nie, dąb i sosna różne programy, osobno). Więc **2,42 m³ sosna za 719 zł = 297 zł/m³** (bez dębu, dąb zostaje do następnej wsadki EGIDA).

Zalety: ZLE-077 zakończony w terminie (start zewnętrzny ~2 czerwca, koniec ~12 czerwca, transport 13 czerwca, klient odbiera 20 czerwca, bufor 7 dni). Dąb EGIDA czeka do pełnej wsadki następnej, nie blokuje ZLE-077.
Wady: koszt 297 zł/m³ vs **~85 zł/m³ suszenia własnego** (prąd, gaz, amortyzacja komory), czyli **212 zł różnicy na m³, 512 zł dla 2,42 m³**. Klient płaci za deski gotowe wilgotność 12%, nie za sposób suszenia, więc **EGIDA kupuje sobie terminowość za 512 zł**.

**Opcja C, hybryda**. Zlecenie zewnętrzne dla sosny (2,42 m³, termin krytyczny), komora własna dla dębu (2,22 m³, termin luźny, klient jeszcze nie odbiera, może poczekać). Ale z dębu samego (2,22 m³) do pełnej wsadki EGIDA brakuje dalszych **28 m³**, czyli **12 dni roboczych cięcia tylko dębu** (~2 m³/zmiana × 6 zmian × 2 pilarki = 24 m³), nie realne (kampania dębowa ograniczona dostępnym surowcem z Nadleśnictwa Strzałowo, kontyngent czerwcowy ~4-5 m³).

Realistycznie hybryda oznacza: zewnętrzne dla sosny, **czekanie 3-4 tygodni** dla dębu (następna wsadka dębu byłaby dopiero około **2026-07-01** gdy zbierzemy kolejne pnie).

### 14:45, decyzja

Pan Henryk, po chwili namysłu, mówi do Marka:

*„Marek, ja bym wziął opcję B. Sosna wychodzi na zewnątrz, 512 zł ekstra na marży, ale klient dostaje w terminie i nikt nie rozmawia o spóźnieniu. Dąb własnej komory uruchamiam, jak będzie 30 m³, pewnie do połowy czerwca, wtedy nowa wsadka."*

Marek: *„A ile nam to zepsuje ekonomię ZLE-077?"*

Pan Henryk szybko w głowie: *„Cena sprzedaży tarcicy sosna C24 deski 25 × 150 po suszeniu i obróbce: **1700 zł/m³** klient ZLE-077. Koszt produkcji EGIDA dla sosny: **~1100 zł/m³** (surowiec z lasu 380, praca tartaczna 220, suszenie własne 85, obróbka 200, amortyzacja 180, pozostałe 35). Marża 600 zł/m³. Przy 0,58 m³ = **348 zł marży**. Suszenie zewnętrzne plus 212 zł/m³ = plus 123 zł, marża spada do **225 zł**. Pozostaje zyskowne, klient niewiedzący."*

*„Akceptuję,*" mówi Marek. *„Opcja B. Jutro rano dzwonię do Drew-Sus, umawiam wtorek 3 czerwca załadunek, zlecenie całej sosny z magazynu 2,42 m³. Naszą komorę zostawiamy pustą do połowy czerwca, potem startujemy pełną wsadkę dębu."*

Pan Henryk potakuje, idzie do biurka w kącie hali sterowania, wypełnia **kartę KS-001** (karta suszarni, format A4, dedykowana dla każdej decyzji wsadkowej). Rustam patrzy przez ramię.

### 14:55, karta KS-001 wypełniana

Pan Henryk wpisuje w sekcjach:

**Sekcja 1, Wsadka planowana (jeżeli dotyczy)**:
```
Typ wsadki: sosna zwyczajna, deski 28 × 155 × 4050 mm surowe
Objętość planowana: 2,42 m³ (ZLE-077 0,58 + ZLE-079 0,72 + nadwyżka magazyn 1,12)
Wilgotność początkowa (średnia z 4 punktów pomiarowych): 30-32%
Wilgotność docelowa: 12% ±1%
Program suszarniczy wybrany: NIE DOTYCZY (wsadka zewnętrzna Drew-Sus)
Uzasadnienie: mała objętość, komora własna nieekonomiczna,
             klient ZLE-077 termin wymaga suszenia do 12.06,
             zlecenie zewnętrzne pozwala trzymać terminowość.
```

**Sekcja 2, Wsadka następna planowana (dla komory własnej)**:
```
Planowany start: ~2026-06-15 (po zebraniu 30+ m³)
Typ planowany: dąb szypułkowy, deski 28 × 155 × 4050 mm
Objętość zakładana: 30-38 m³ (pełna wsadka, wymaga zbierania 17 dni)
Program planowany: DUB-STAND-28 (dąb standard deski 28 mm, cykl 22 dni)
Wilgotność początkowa zakładana: 35-38%
Wilgotność docelowa: 14%
```

**Sekcja 3, Notatki i obserwacje**:
```
Wsadka bieżąca (dąb od 17.05) idzie normalnie, plan wyjście 07.06.
Następna kampania dębowa z Nadleśnictwa Strzałowo planowana 08-15.06.
Pan Henryk urlop 2 tygodnie 20.06-04.07, Maciek sam z komorą,
   w razie problemu eskalacja Marek → BTM (serwis polski suszarni).
Rustam Nazarov uczestniczy w naradzie (szkolenie M3 blok procesy, l3).
```

**Podpis**: Pan Henryk, data, godzina.

Retencja: **3 lata papier** w biurze suszarni, **5 lat skan** OneDrive EGIDA.

### 15:05, zlecenie zewnętrzne, telefon

Marek wychodzi z hali sterowania do własnego biura (5 minut marsz przez plac), wykonuje telefon do Drew-Sus. Wraca po 20 minutach z potwierdzeniem:

- Drew-Sus przyjmuje 2,42 m³ sosny we wtorek **2 czerwca 8:00-10:00** (załadunek ich ciężarówką u EGIDA).
- Cykl suszenia **8 dni** (start wtorek wieczór, koniec środa 10 czerwca).
- Transport tam-z-powrotem **350 zł netto** ryczałtowo.
- Suszenie **180 zł/m³ netto** × 2,42 = **435,60 zł netto**.
- Razem **785,60 zł netto, 966,30 zł brutto**. Faktura po odbiorze tarcicy suchej (12.06).

Marek informuje Pana Henryka o terminie. Pan Henryk w KS-001 dopisuje w sekcji 3:
```
Aktualizacja 14:55: zlecenie Drew-Sus potwierdzone.
Załadunek wtorek 02.06 8:00-10:00 (Marek koordynuje).
Wyjście 10.06, transport powrót 11.06, obróbka końcowa i wydanie klientowi 13-20.06.
Koszt: 785,60 zł netto.
```

## Cele

Po tej lekcji:

1. Znasz **strukturę komory suszarniczej EGIDA**: Brunner-Hildebrand BH-50 (austriacki producent z niemiecką tradycją, dystrybucja Polska od 2005), pojemność brutto **50 m³**, netto **38 m³** tarcicy. Typ konwencjonalny (grzanie gorącym powietrzem plus wentylatory osiowe plus wyciąg wilgoci na zewnątrz), nie kondensacyjna, nie vacuum. Rok produkcji EGIDA 2011, serwis BTM Polska (polski dystrybutor). Komora jedna na cały tartak.
2. Znasz **pięć faz typowego cyklu suszenia w komorze konwencjonalnej**: 1) **nagrzewanie** (2-3 dni, temperatura rośnie z 20 do 30-40°C, wilgotność RH 95% żeby drewno nie traciło wody nadmiernie), 2) **suszenie wstępne** (4-7 dni, temperatura 40-50°C, RH 85% → 65%, pierwsze 10-15% wilgotności oddaje drewno), 3) **suszenie główne** (5-14 dni, temperatura szczyt 60-70°C, RH 40-50%, wilgotność drewna z 25% do targetu), 4) **kondycjonowanie** (2-4 dni, temperatura 55-65°C, RH 70-80%, wyrównywanie naprężeń wewnętrznych), 5) **chłodzenie** (1-2 dni, temperatura spada do 25-30°C, drewno gotowe do wyjścia).
3. Znasz **typowe czasy cykli** dla głównych gatunków EGIDA (programy sterownika BH-50): **sosna świeża 25-32 mm**: 7-9 dni, target wilgotność 12% (stolarka budowlana) lub 8-10% (stolarka meblowa); **dąb świeży 28-30 mm**: 20-24 dni, target 14%; **buk świeży 25-28 mm**: 14-18 dni, target 10%; **brzoza 20-25 mm**: 12-15 dni, target 12%. Rozumiesz, że czas zależy od grubości deski kwadratowo (dwukrotnie grubsza deska = ok. cztery razy dłuższy cykl) i że gatunki twardsze (dąb) suszą się znacznie wolniej niż miękkie (sosna).
4. Znasz **EMC (wilgotność równowagową drewna)** jako wartość sterującą programu: dla temperatury 25°C i RH powietrza 60% EMC drewna wynosi ~10%. Sterownik BH-50 utrzymuje tę relację (dla sosny target 12% wymaga temperatury 60°C i RH ~50% pod koniec cyklu), nie „bezpośrednio suszy", lecz **tworzy warunki, w których drewno dąży do ~12%**. Rozumiesz, że za szybkie obniżanie wilgotności (ekspozycja na RH < 30% w fazie początkowej) powoduje pęknięcia na czole deski (*end checks*), a za wolne (RH > 60% w fazie głównej) powoduje pleśń wewnętrzną.
5. Znasz **problem jednorodności wsadki i dolną granicę ekonomiczną**. Komora BH-50 jest zaprojektowana dla 80-100% wypełnienia (30-38 m³ netto). Wypełnienie poniżej 60% (23 m³) daje nierównomierność temperatury (rogi komory są chłodniejsze niż środek) i nieprzewidywalny rezultat. **W praktyce EGIDA minimum 30 m³ na wsadkę**, co oznacza że tarcica w magazynie suszenia jest zbierana **10-17 dni** (typowa produkcja EGIDA ~22 m³/tydzień, z czego 60% idzie do suszenia, 40% sprzedawane surowe lub odkładane).
6. Znasz **kryteria wyboru suszenia zewnętrznego** (Drew-Sus w Mrągowie dla EGIDA): 1) termin klienta krytyczny, mniej niż 20 dni do wydania; 2) partia specyficzna, której nie można zmieszać z planowaną wsadką własną (np. sosna vs dąb); 3) pojedyncza partia 0,5-3 m³ bez szans na dołożenie w najbliższym tygodniu. Znasz stawki 2026: **180 zł/m³ suszenie plus 350 zł ryczałt transportu tam-z-powrotem**, przekłada się na **~260-300 zł/m³ dla partii 2-3 m³**, wobec **~85 zł/m³ suszenia własnego**.
7. Rozumiesz **granicę kompetencji operatora M3 w suszarnictwie**. Operator M3: uczestniczy w naradach planistycznych, dostarcza informacje o tarcicy świeżej w magazynie suszenia, rozumie program sterownika, czyta i interpretuje wskaźniki panelu, w razie alarmu może **wstępnie zdiagnozować** (alarm temperatury, alarm przepływu powietrza) i zgłosić mistrzowi suszarni. Mistrz suszarni (Pan Henryk w EGIDA): **decyduje** o programie, wsadce, czasie startu, korektach w trakcie, kondycjonowaniu. Operator M3 **nie uruchamia programu samodzielnie** (wymaga przeszkolenia fabrycznego BTM, którego operator M3 nie ma), **nie zmienia parametrów** w trakcie cyklu, **nie klasyfikuje tarcicy po suszeniu** (to klasyfikator, Pani Ania).
8. Znasz **kartę KS-001** (karta suszarni): format A4, cztery sekcje (wsadka planowana, wsadka następna, notatki i obserwacje, podpis), wypełniana **przez mistrza suszarni** dla każdej decyzji wsadkowej (planowanie, wsadka bieżąca obserwacje, zakończenie wsadki, decyzje zewnętrzne). Retencja **3 lata papier** plus **5 lat skan OneDrive**. Operator M3 **nie wypełnia KS-001 samodzielnie**, ale uczestniczy w wypełnianiu podczas narad planistycznych (rozumie strukturę dokumentu).

## Treść

### 1. Co to jest suszenie drewna i po co

**Świeżo ścięte drewno** (sosna, dąb, buk, brzoza) zawiera typowo **35-55% wilgotności** (odsetek masy wody w całkowitej masie drewna). Ta woda jest w dwóch postaciach: 1) **woda wolna** w świetle komórek rurek naczyniowych, 2) **woda związana** w ścianach komórkowych (chemicznie wiązana celulozą i hemicelulozą). Woda wolna wychodzi szybciej (pierwsze 8-20 dni suszenia), woda związana wolniej (kolejne tygodnie).

**Po co suszymy**:

1. **Stabilność wymiarowa**. Drewno świeże kurczy się po ścięciu, w miarę utraty wody. Skurcz jest nierównomierny: promieniowy (12-20% w maksimum dla dębu), tangencjalny (8-12% dla dębu), wzdłużny (<1%). Jeżeli deska nie jest wysuszona przed użyciem w budynku, **kurczy się w konstrukcji** (pęknięcia, szczeliny między deskami, sufity obwisłe).

2. **Wytrzymałość mechaniczna**. Drewno wysuszone do 12% ma **wytrzymałość zginania wyższa o 40-60%** niż drewno świeże. Klasy wytrzymałościowe (C16, C24, C30) są **kalibrowane dla wilgotności 12%**. Drewno suszone do innego target (np. 18%) daje wytrzymałość inną, trzeba przelicznik.

3. **Ochrona przed grzybami i pleśniami**. Drewno o wilgotności poniżej 20% **nie jest medium wzrostu** dla grzybów pleśniowych. Drewno świeże jest idealne dla pleśni (woda + celuloza + rzeczywista temperatura pokojowa).

4. **Możliwość obróbki**. Drewno świeże **nie obrabia się dobrze** planerem (ślizga się, hebluje nierówno), **nie klei się dobrze** (kleje wymagają wilgotności 8-12%), **nie lakieruje się** (lakier nie trzyma na mokrym drewnie). Dla **stolarki meblowej** wymóg 8-10%, dla **stolarki budowlanej i podłogi** 12%, dla **więźby dachowej** 18%.

5. **Redukcja masy i kosztów transportu**. 1 m³ sosny świeżej 35% wilg. waży **~720 kg**. Ta sama sosna 12% wilg. waży **~520 kg**. Różnica 200 kg/m³, dla 10 m³ to 2000 kg mniej do transportu. Koszt transportu EGIDA → klient Warszawa średnio 35-45 zł/km, ciężarówka 15 t: oszczędność realna.

### 2. Dwa podstawowe sposoby suszenia

**Suszenie naturalne (sezonowanie)**: drewno składowane na zadaszonym placu bez izolacji z ogrzewania, woda odparowuje do atmosfery zimnym powietrzem. Czas: **6-12 miesięcy dla deski 25 mm sosny**, **24-36 miesięcy dla deski 28 mm dębu**. Zalety: taniość (brak energii, tylko czas), naturalna jakość suszenia (wolne, bez naprężeń). Wady: **bardzo wolne** (przepustowość EGIDA gdyby tylko sezonowała, ~30% obecnej), **sezonowe** (zimą wilgotność spada bardzo wolno, wiosną ryzyko pleśni), **brak kontroli targetu** (wilgotność końcowa zależy od klimatu, nie od wymogu).

EGIDA używa sezonowania dla **niskich priorytetów** (brzoza, resztki dębu, partie bez klienta konkretnego), **plac magazynowy 800 m²** na tyłach hali, 4-6 stosów (każdy 15-25 m³), rotacja ciągła.

**Suszenie komorowe**: drewno w zamkniętej komorze, grzanie kontrolowane, wilgotność powietrza regulowana, wentylacja wymuszona. Czas: **7-30 dni** zależnie od gatunku i grubości. Zalety: **szybkie, kontrolowane, powtarzalne** (program 5x ten sam daje 5x ten sam rezultat), target wilgotności dokładny (±1%). Wady: **kosztowne w energii** (BH-50 EGIDA zużywa 800-1200 kWh na cykl 20-dniowy plus gaz ~400 kg), wymaga **specjalisty** (mistrz suszarni), ryzyko pęknięć przy błędnym programie.

EGIDA używa komory dla **głównej produkcji** (sosna C24, dąb podłogowy, buk meblowy), planowanych zamówień klientów, każdej partii z terminem.

### 3. Kiedy suszenie kombinowane

W praktyce EGIDA trzy strategie kombinowane:

**Sezonowanie wstępne plus komora**. Dla dębu świeżego (35-38% wilg.) stosujemy **2-3 tygodnie sezonowania na placu** (spada do ~28-30% wilg.), potem **komora 20-24 dni** (z 28% do 14%). Razem 5-6 tygodni. Zalety: oszczędność energii komory (pierwsze 10% wilgotności drewno oddaje „za darmo" na placu), komora pracuje w zakresie, w którym jest efektywna.

**Komora plus sezonowanie końcowe** (rzadko, dla specjalnych klientów). Komora do 14%, potem sezonowanie 2-3 miesiące, drewno „dojrzewa" w stabilnym klimacie, naprężenia dochodzą do równowagi. Używane dla eksportu do regionów z innym klimatem (Niemcy, Niderlandy), gdzie drewno „osiadło" i nie pęka w transportach.

**Dwuetapowa w komorze**. Drewno bardzo świeże (sosna świeża 32%+), komora program fazy nagrzewania i suszenia wstępnego (7 dni), potem **pauza w hali klimatyzowanej** (3-5 dni, drewno stabilizuje się), następnie **komora drugi program** suszenia głównego i kondycjonowania (5-8 dni). Razem 15-20 dni. Używane dla dużych partii gdzie skrócenie cyklu nie jest krytyczne.

### 4. Program suszarniczy dla sosny świeżej 28 mm

Przykład programu **SOS-STAND-28** (sosna standardowa deski 28 mm świeża do 12%), używanego przez EGIDA w komorze BH-50 (i używanego też przez Drew-Sus, bo podobny sterownik Brunner):

```
DZIEŃ 1 (nagrzewanie):
  Temperatura: 20 → 35°C (powoli, ~0,5°C/godz)
  Wilgotność RH: 95% (bardzo wysoka, drewno nie suszy się)
  Cel: wyrównać temperaturę całej masy drewna
  Koniec dnia 1: drewno 35°C, wilgotność drewna bez zmian (32%)

DZIEŃ 2-3 (suszenie wstępne):
  Temperatura: 35 → 50°C
  Wilgotność RH: 95% → 70%
  Cel: usunąć wodę wolną (najłatwiejszą)
  Koniec dnia 3: wilgotność drewna ~20-22% (z 32%, spadek 10-12%)

DZIEŃ 4-7 (suszenie główne):
  Temperatura: 50 → 70°C (szczyt)
  Wilgotność RH: 70% → 40%
  Cel: wilgotność drewna do 14-15%
  Koniec dnia 7: drewno 70°C, wilg. drewna 14%

DZIEŃ 8 (kondycjonowanie):
  Temperatura: 70 → 60°C
  Wilgotność RH: 40% → 70%
  Cel: wyrównanie naprężeń wewnętrznych, brak pęknięć wewn.
  Koniec dnia 8: drewno 60°C, wilg. 12-13%

DZIEŃ 9 (chłodzenie):
  Temperatura: 60 → 25°C (naturalnie, wentylatory bez grzania)
  Wilgotność RH: 70% (stabilna)
  Cel: drewno gotowe do wyjścia bez szoku termicznego
  Koniec dnia 9: drewno 25°C, wilg. 12%, WYJŚCIE Z KOMORY.
```

**Całkowity czas**: 9 dni (cykl nominalny). W praktyce ±1-2 dni zależnie od wilgotności początkowej i parametrów komory.

**Parametry sterownika**:
- Czujniki temperatury: 4 (rogi komory plus środek)
- Czujniki wilgotności względnej powietrza: 2 (wlot wentylatora plus wylot)
- Czujniki wilgotności drewna: 3 (sondy wbite w deski w 3 różnych stosach: przód, środek, tył komory)
- Odchylenie dopuszczalne: temperatura ±2°C od zadania, RH ±5% od zadania
- Alarm sterownika: przekroczenie dopuszczalnego odchylenia o 50% (4°C temp, 8% RH)

**Zużycie energii**: ~180 kWh/dzień (prąd wentylatorów), ~25 kg gazu/dzień (grzanie), razem **~85 zł/m³ na cykl** dla pełnej wsadki 38 m³.

### 5. Program suszarniczy dla dębu świeżego 28 mm

Dąb wymaga **znacznie wolniejszego cyklu**, bo ma wyższe ryzyko pęknięć (struktura tangencjalna-promieniowa duża różnica skurczu, rdzeń drewna wrażliwy na szok termiczny):

```
DZIEŃ 1-2 (nagrzewanie powolne):
  Temperatura: 20 → 30°C (bardzo wolno, 0,2°C/godz)
  Wilgotność RH: 95%
  Cel: temperatura masy drewna bez szoku

DZIEŃ 3-10 (suszenie wstępne):
  Temperatura: 30 → 40°C (powoli)
  Wilgotność RH: 90% → 75%
  Cel: wilgotność drewna 38% → 28%

DZIEŃ 11-18 (suszenie główne):
  Temperatura: 40 → 60°C (szczyt dębu, nie wyżej!)
  Wilgotność RH: 75% → 45%
  Cel: wilgotność drewna 28% → 16%

DZIEŃ 19-21 (kondycjonowanie długie):
  Temperatura: 60 → 55°C
  Wilgotność RH: 45% → 75%
  Cel: wyrównanie naprężeń (dąb szczególnie wrażliwy, ryzyko pęknięć rdzeniowych)

DZIEŃ 22 (chłodzenie):
  Temperatura: 55 → 25°C
  Wilgotność RH: 75% stabilne
  Koniec: drewno 25°C, wilg. 14%, WYJŚCIE.
```

**Całkowity czas**: **22 dni nominalne**, często 24-25 dni w praktyce dla dużych partii.

**Różnice kluczowe vs sosna**:
- Temperatura szczyt **60°C** (vs 70°C sosna), wyżej dąb popęka
- Kondycjonowanie **3 dni** (vs 1 dzień sosna), dąb wymaga długiego wyrównania
- Wilgotność docelowa **14%** (vs 12% sosna), dąb nie osiąga 12% bez kruchości

**Zużycie energii**: ~180 kWh/dzień × 22 dni = 3960 kWh plus ~400 kg gazu = ~**80-90 zł/m³** (podobnie jak sosna, bo wolniejszy ale z niższymi temperaturami).

### 6. Co operator M3 widzi na panelu sterownika

Panel sterowania BH-50 w hali sterowania suszarni pokazuje **w czasie rzeczywistym**:

**Ekran główny**:
- Nr programu (np. SOS-STAND-28)
- Dzień cyklu (np. 5 z 9) i faza (np. „Suszenie główne")
- Temperatura powietrza komory (w °C, z czterech czujników plus średnia)
- Wilgotność względna powietrza (RH w %, z dwóch czujników plus średnia)
- Wilgotność drewna (z trzech sond, plus średnia, plus rozrzut)
- EMC (wyliczona z temperatury i RH powietrza, porównanie z aktualną wilgotnością drewna)
- Stan wentylatorów (obroty RPM, prąd A)
- Stan grzałek (moc kW aktualnie, procent maksimum)

**Ekran alarmy** (jeżeli jakikolwiek z sensorów poza zakresem):
- Typ alarmu (temperatura, wilgotność, przepływ, sensor)
- Czas wykrycia (godzina, minuta)
- Wartość odczytana vs oczekiwana
- Rekomendacja automatyczna (np. „zwiększ wentylację", „zatrzymaj cykl")

**Co operator M3 rozumie** (bez ingerencji):
- Jeżeli temperatura ±2°C od zadania, **OK**, program trzyma.
- Jeżeli wilgotność drewna spada monotonnie (każdy dzień o 1-2%), **OK**, suszenie idzie.
- Jeżeli rozrzut między trzema sondami wilgotności drewna jest <2%, **OK**, wsadka jednorodna.
- Jeżeli rozrzut >3%, coś jest nie tak (problem z ułożeniem stosów, nierównomierny przepływ, zgłoś mistrzowi).
- Jeżeli alarm czerwony na ekranie, **zgłoś mistrzowi natychmiast** (nie próbuj rozwiązać samodzielnie).

**Co operator M3 NIE robi**:
- Nie zmienia parametrów programu (temperatura, RH, czas fazy)
- Nie przełącza programu na inny w trakcie
- Nie otwiera drzwi komory podczas cyklu (wypuszcza ciepło, szok termiczny drewna)
- Nie wyłącza wentylatorów ani grzałek
- Nie resetuje alarmu bez zgody mistrza

### 7. Jednorodność wsadki, dlaczego krytyczna

Komora suszarnicza suszy **całą wsadkę jednocześnie pod tym samym programem**. Jeżeli wsadka jest **niejednorodna** (różne gatunki, różne grubości, różne wilgotności), program optymalny dla części wsadki jest **błędny dla reszty**. Przykłady:

**A. Sosna 25 mm plus dąb 25 mm razem**. Program sosny 9 dni do 12%. Dąb po 9 dniach w tym programie: temperatura 70°C (za wysoka dla dębu, pęka), wilgotność dębu wciąż 22% (nie wysuszony). Program dębu 22 dni do 14%. Sosna po 22 dniach: wilgotność 8% (za niska, drewno łamliwe), temperatura 60°C (OK), ale czas 2,5 razy dłuższy niż potrzebny (strata energii). **Nie mieszaj gatunków w jednej wsadce.**

**B. Sosna 25 mm i sosna 45 mm razem**. Ten sam gatunek, ale różna grubość. Program 25 mm 9 dni. 45 mm w 9 dni: wilgotność 20% (nie dosuszony), cykl trzeba przedłużyć 3-5 dni. Program 45 mm 15 dni. 25 mm w 15 dni: wilgotność 9% (przesuszony), kruchy. **Grubości różne to kompromis lub dwie wsadki.**

**C. Sosna świeża 32% plus sosna sezonowana 22% razem**. Ten sam gatunek, ta sama grubość, ale inna wilgotność startowa. Różne zachowanie w fazach początkowych: świeża oddaje dużo wody (nasyca powietrze), sezonowana oddaje mało (nie nasyca). W fazie głównej świeża jeszcze wilgotna, sezonowana już przesuszona. **Mieszanie wilgotności startowych dopuszczalne tylko w zakresie ±5% (np. 28-33% razem, 20-25% razem)**.

**Ocena jednorodności przed wsadką** (procedura mistrza suszarni):
1. Pomiar wilgotności **w co najmniej 10 deskach** różnych partii planowanej wsadki.
2. Obliczenie rozrzutu. Jeżeli <±5% od średniej, wsadka jednorodna.
3. Rejestracja w KS-001 sekcja „Wsadka planowana" (średnia, minimum, maksimum).
4. Jeżeli rozrzut większy, dzielenie na dwie wsadki albo odrzucenie części do innej wsadki.

### 8. Kondycjonowanie i naprężenia wewnętrzne

**Kondycjonowanie** (faza 4 cyklu, po głównym suszeniu) to **kluczowa faza jakości**, często niedoceniana przez operatora początkującego. Fizycznie: drewno po suszeniu głównym ma **gradient wilgotności wewnętrzny**. Zewnętrzna warstwa deski (powierzchnia) jest wysuszona (8-10%), rdzeń deski jest wilgotniejszy (14-15%). Gradient generuje **naprężenia wewnętrzne** (kompresja warstw zewnętrznych, rozciąganie rdzenia).

Jeżeli deska wychodzi z komory w tym stanie i idzie do obróbki (planer, piła formatyzerka), **naprężenia ujawniają się**: deska po cięciu „trzaska" (mikro-pęknięcia wewnętrzne), po zheblowaniu wygina się (warping), po kilku tygodniach w budynku klient widzi **pęknięcia rdzeniowe** (internal checks).

Kondycjonowanie **odwraca częściowo gradient**: podwyższając wilgotność powietrza (RH z 40% do 70%) przy temperaturze nieco niższej (60°C z 70°C), warstwy zewnętrzne deski **wchłaniają trochę wilgoci** z powietrza (wilgotność powierzchni rośnie z 8% do 11%), rdzeń wciąż wyrównuje się w dół (15% → 13%). Po 2-3 dniach gradient **spada do 2-3%** (z 6-7%), naprężenia rozpuszczone.

**Testo w praktyce**: operator M3 patrzy na wskaźnik rozrzutu między sondami wilgotności po kondycjonowaniu. Jeżeli trzy sondy pokazują 11,8 / 12,0 / 12,3% (rozrzut 0,5%), kondycjonowanie udane. Jeżeli 10,5 / 12,0 / 13,8% (rozrzut 3,3%), kondycjonowanie niedopełnione, mistrz wydłuża fazę o dzień.

::: info
**Pomijanie kondycjonowania** to najczęstszy skrót suszarniczy „dla oszczędności". Operator nieprzeszkolony widzi, że drewno „już jest suche" po fazie głównej (wilg. 12% na sondach), chce wyjąć. Mistrz odpowiada: **„widzisz średnią, nie widzisz naprężeń". Drewno bez kondycjonowania wygląda identycznie z zewnątrz, ale pęka w ciągu 2-4 tygodni u klienta**, reklamacja jest nieuchronna. Koszt reklamacji (wymiana tarcicy plus koszty transportu plus wizyta klienta) zawsze przekroczy oszczędność z 2 dni kondycjonowania (40-60 zł prądu).
:::

### 9. Wilgotność równowagowa EMC i program

**EMC (Equilibrium Moisture Content, wilgotność równowagowa)** to wilgotność, do której **drewno dąży** w danym środowisku (temperatura, RH powietrza). Jest to fundamentalne pojęcie suszarnictwa. EMC zależy od temperatury i RH, nie od gatunku drewna (drobne różnice między gatunkami istnieją, ale w praktyce EGIDA tabele uproszczone).

**Tabela EMC** (uproszczona, dla sosny i dębu w temperaturze 20-70°C):

| Temperatura | RH 30% | RH 50% | RH 70% | RH 90% |
|---|---|---|---|---|
| 20°C | 6,3% | 9,2% | 13,1% | 20,5% |
| 40°C | 5,8% | 8,5% | 12,2% | 19,3% |
| 60°C | 5,2% | 7,7% | 11,2% | 18,0% |
| 70°C | 5,0% | 7,4% | 10,8% | 17,5% |

**Jak sterownik używa EMC**: w każdej fazie cyklu sterownik zna zadaną temperaturę i RH, oblicza aktualną EMC, porównuje z celem dla danej fazy. Jeżeli drewno jest powyżej celu EMC dla danej chwili, **suszenie trwa** (woda paruje). Jeżeli drewno jest poniżej EMC (za szybko wysuszono), sterownik **zwiększa RH** (wstrzykuje parę lub wyłącza wentylację) żeby drewno zwolniło suszenie.

**Klucz do zrozumienia sosny 28 mm do 12%**: końcowy program wymaga **temperatura 60°C i RH 50%**, bo wtedy EMC ≈ 7,7% (tabela). Drewno dąży do 7,7%, ale ze względu na grubość deski i dyfuzję, w czasie 2-3 dni ostatniej fazy nie dosięgnie 7,7%, zatrzyma się na ~12%. **Tu sterownik wyłącza cykl** (target osiągnięty). Gdyby cykl trwał jeszcze 5 dni, drewno spadłoby do 8%, byłoby za suche.

**Mistrz suszarni** rozumie tę dynamikę intuicyjnie. **Operator M3** rozumie zasadę (EMC, dlaczego 60°C i 50% RH daje 12% w 28 mm). Nie musi wyliczać EMC w głowie, ale widzi na panelu „aktualna EMC 7,7% vs wilg. drewna 12%" i wie co to znaczy.

### 10. Problemy typowe w cyklu i jak operator M3 sygnalizuje

**Problem 1. Temperatura nie dochodzi do zadania**. Program zadaje 70°C, sterownik pokazuje 62°C. Powody:
- Grzałka uszkodzona (serwis)
- Termostat zabrudzony (serwis)
- Wsadka za duża, grzałka nie daje rady (operator zgłasza, mistrz zmniejsza cel)
- Drzwi nieuszczelnione (mistrz sprawdza, ewentualnie wymienia uszczelki)

**Sygnalizacja operatora M3**: zgłoszenie Pani Henryku po 2 godzinach odchylenia. „Komora 62 zamiast 70, od 2 godzin."

**Problem 2. Wilgotność drewna spada nierówno w sondach**. Sondy 1/2/3 pokazują 18/14/21%. Rozrzut 7%. Powody:
- Sondy zamocowane w różnych gatunkach (błąd załadunku, mistrz koryguje)
- Wsadka nierówno ułożona, przepływ powietrza nierównomierny (mistrz decyduje o korekcie)
- Sonda uszkodzona (mistrz sprawdza po cyklu)

**Sygnalizacja operatora M3**: zgłoszenie rozrzutu >3%. „Sondy 18/14/21, rozrzut 7%, od rana."

**Problem 3. Alarm wentylacji**. Sterownik pokazuje „alarm: przepływ powietrza poniżej 80%". Powody:
- Wentylator uszkodzony (mistrz wyłącza cykl, wzywa serwis)
- Zator w kanałach wentylacyjnych (mistrz sprawdza)
- Sensor przepływu uszkodzony (mistrz przełącza na ręczną kontrolę)

**Sygnalizacja operatora M3**: **natychmiastowa**, telefon do mistrza. „Alarm wentylacji na komorze, LED czerwona."

**Problem 4. Zapach pleśni w hali sterowania**. Subtelny sygnał, że w komorze jest warunek sprzyjający pleśni (zbyt wysoka wilgotność w fazie suszenia wstępnego, zwykle przy niedopałceniu grzałek). Niemiejskie alarm sterownik, wymaga doświadczonego nosa.

**Sygnalizacja operatora M3**: zgłoszenie mistrzowi, „w hali pachnie zatęchło, pewnie w komorze coś jest". Mistrz sprawdza, decyduje.

### 11. Szkolenie suszarnicze operatora M3 po lekcji

EGIDA oferuje operatorom M3 **dodatkowy moduł szkoleniowy suszarnictwa** (opcjonalny, po zaliczeniu M3), który trwa 5 dni. Zakres:

1. **Dzień 1**: teoria suszarnictwa (dyfuzja, EMC, programy, kondycjonowanie), wykłady Pana Henryka.
2. **Dzień 2**: obserwacja pełnego cyklu z wnętrza komory (tylko w fazie chłodzenia, bo w gorącej fazie nie wchodzimy), pomiary sondami, obsługa panelu.
3. **Dzień 3**: planowanie wsadki (podobne do dzisiejszej narady, ale operator prowadzi, mistrz koryguje).
4. **Dzień 4**: diagnoza usterek (wprowadzone błędy, operator próbuje rozpoznać).
5. **Dzień 5**: egzamin (pisemny plus praktyczny, próg 80%). Zaliczenie daje uprawnienie **„operatora suszarniczego pomocniczego"** (może zastąpić mistrza na 1-2 dni, np. weekend), ale **nie jest mistrzem** (to wymaga 3-letniego stażu i kursu BTM).

Rustam sygnalizuje Panu Henrykowi zainteresowanie tym kursem. Pan Henryk: *„Skończ M3, potem pogadamy. Za wcześnie, masz jeszcze 13 lekcji w bloku procesowym i organizacyjnym. Jeżeli cię zainteresuje, w październiku ruszymy szkolenie."*

Rustam zapisuje w kalendarzyku: „*październik 2026, moduł suszarniczy pomocniczy, 5 dni.*"

## Scena domykająca, 15:30, wyjście z hali suszarni

Rustam, Marek i Pan Henryk wychodzą z hali sterowania. Pan Henryk zostaje przy komorze (sprawdzi sondy raz jeszcze, napije się wody, wróci do domu o 17:00), Marek i Rustam idą przez plac magazynowy do hali pilarek.

### 15:35, rozmowa Marek z Rustamem

Marek, idąc: *„Rustam, co zrozumiałeś z dzisiejszej narady?"*

Rustam: *„Trzy rzeczy. Po pierwsze, suszenie to **nie kwestia maszyny tylko czasu**. 22 dni dla dębu, 9 dni dla sosny, nic tego nie skróci poza przeskoczeniem na gorszą jakość. Po drugie, **wsadka jednorodna** to podstawa, mieszanie gatunków daje ryzyko. Po trzecie, **mistrz suszarni decyduje, operator M3 dokumentuje**. Nie jest tak jak na pilarce, gdzie ja decyduję sam."*

*„Dobrze. Co z czwartą rzeczą?"*

*„Czwartą?"*

*„Zlecenie zewnętrzne jako opcja. Dla klienta ZLE-077 Drew-Sus kosztuje nas 512 zł ekstra, ale ratuje termin. **Termin jest ważniejszy niż marża**, bo klient, który dostaje towar w terminie, zamawia następne zlecenie. Klient, który dostaje 3 dni spóźnienie, szuka innego tartaku. Zyski długoterminowe mierzy się ciągłością zamówień, nie marżą pojedynczego zlecenia."*

Rustam zapisuje w kalendarzyku: *„Termin > marża. Suszenie zewnętrzne jako opcja strategiczna, nie awaryjna."*

### 15:45, planowanie najbliższej przyszłości

Marek: *„Jutro piątek, dzień planowy bez nietypowych zadań. W poniedziałek 2 czerwca załadunek Drew-Sus 8:00-10:00, ty Wahan pomagacie z brygadzistą placu, trzeba przenieść stosy z magazynu suszenia do ciężarówki. Po załadunku normalna zmiana na P3 od 10:15. Tydzień za poniedziałkiem, 9 czerwca, wyjście dębu z komory, nowa klasyfikacja (Pani Ania), ty asystujesz z Wahanem przy sortowaniu. To blok l5 twojego kursu, rozładunek komory, wyjście z l3."*

Rustam potakuje. Zapisuje w kalendarzyku: *„02.06 załadunek Drew-Sus, 09.06 wyjście dębu z komory."*

### 15:50, powrót do hali pilarek

Marek wraca do biura brygadzisty, Rustam do P3. Na P3 jeszcze świeżo zgrzana taśma z wczoraj, zlecenie ZLE-2026-05-079 (Damian z rana, teraz Rustam dokończy popołudnie), sosna deski 25 × 130 mm. Inny sortyment niż wczoraj (węższe, cieńsze), ale parametrów nie trzeba zmieniać (sosna ta sama, grubość inna tylko o 3 mm), **prędkość posuwu 34 st/min** (sosna cieńsza tnie szybciej), **napięcie 2200 PSI**, bez zmiany taśmy.

Rustam wypełnia nowe KDP-001 dla ZLE-079 (pierwsza sekcja: surowiec, druga: taśma już na maszynie, nr znany, sekcje 3-4: parametry). 10 minut wypełniania. Startuje cięcie o 16:02. Dzień pracuje do końca zmiany 17:00. Wahan przy podajniku.

## Kluczowe terminy

**Komora suszarnicza konwencjonalna** (*komora suszarnicza konwencjonalna*, EN *conventional kiln dryer*, ES *cámara de secado convencional*, UK *конвенційна сушильна камера*): zamknięte pomieszczenie z grzaniem gorącym powietrzem, wentylatorami osiowymi i wyciągiem wilgoci, typowa pojemność 30-80 m³ netto tarcicy, cykl suszenia 7-25 dni zależnie od gatunku.

**Program suszarniczy** (*program suszarniczy*, EN *drying schedule / program*, ES *programa de secado*, UK *програма сушіння*): zaprogramowana sekwencja faz (nagrzewanie, suszenie wstępne, suszenie główne, kondycjonowanie, chłodzenie) z określonymi temperaturami i RH dla konkretnego gatunku i grubości, np. SOS-STAND-28 dla sosny 28 mm (9 dni), DUB-STAND-28 dla dębu 28 mm (22 dni).

**EMC (Equilibrium Moisture Content)** (*wilgotność równowagowa*, EN *equilibrium moisture content EMC*, ES *contenido de humedad de equilibrio*, UK *рівноважна вологість*): wilgotność, do której drewno dąży w danym środowisku, zależna od temperatury i wilgotności względnej powietrza, wartość teoretyczna sterowania programu suszarniczego.

**Kondycjonowanie** (*kondycjonowanie*, EN *conditioning*, ES *acondicionamiento*, UK *кондиціонування*): przedostatnia faza cyklu suszenia (2-4 dni), w której wilgotność powietrza podwyższana jest powtórnie (z 40-50% do 70-80%) przy obniżonej temperaturze, celem wyrównania gradientu wilgotności wewnętrznej deski i rozpuszczenia naprężeń.

**Wsadka suszarnicza** (*wsadka suszarnicza*, EN *kiln charge / load*, ES *carga del secadero*, UK *завантаження сушарні*): pełna zawartość komory suszarniczej podczas jednego cyklu, typowa wielkość 30-38 m³ netto dla BH-50, wymóg jednorodności gatunku, grubości i wilgotności startowej.

**Jednorodność wsadki** (*jednorodność wsadki*, EN *charge uniformity*, ES *homogeneidad de la carga*, UK *однорідність завантаження*): wymóg, że wszystkie deski wsadki mają ten sam gatunek, zbliżoną grubość (±3 mm) i zbliżoną wilgotność startową (±5%), warunek prawidłowego działania programu.

**Sondy wilgotności drewna** (*sondy wilgotności drewna*, EN *wood moisture probes*, ES *sondas de humedad de la madera*, UK *зонди вологості деревини*): elektryczne sensory (zwykle 2 elektrody wbijane w deskę), mierzą wilgotność drewna w trakcie cyklu, trzy sztuki w BH-50 (przód, środek, tył komory), rozrzut wskazań operacyjny <3%.

**BH-50** (*Brunner-Hildebrand BH-50*, EN *Brunner-Hildebrand BH-50*, ES *Brunner-Hildebrand BH-50*, UK *Brunner-Hildebrand BH-50*): model komory suszarniczej austriacko-niemieckiego producenta, pojemność 50 m³ brutto 38 m³ netto tarcicy, stosowany przez EGIDA od 2011, dystrybucja polska BTM.

**Sezonowanie** (*sezonowanie*, EN *air drying / seasoning*, ES *secado al aire / oreo*, UK *природне висихання / сезонування*): naturalne suszenie drewna na zadaszonym placu bez ogrzewania, czas 6-36 miesięcy, używane w EGIDA dla niskopriorytetowych partii lub jako wstępne suszenie przed komorą.

**Suszarnia zewnętrzna** (*suszarnia zewnętrzna*, EN *external drying service*, ES *secadero externo*, UK *зовнішня сушарня*): podmiot komercyjny świadczący usługę suszenia tarcicy dla innych tartaków, przykład EGIDA: Drew-Sus w Mrągowie, stawka 180 zł/m³ plus 350 zł transport ryczałt za kurs.

**Mistrz suszarni** (*mistrz suszarni*, EN *kiln master*, ES *maestro del secadero*, UK *майстер сушарні*): pracownik z uprawnieniami BTM lub równoważnymi do obsługi komory suszarniczej, decydujący o programie, wsadce, korektach w cyklu, w EGIDA Pan Henryk (emeryt sezonowy).

**Karta KS-001** (*karta suszarni*, EN *kiln log card*, ES *ficha del secadero*, UK *картка сушарні*): formularz A4 wypełniany przez mistrza suszarni dla każdej decyzji wsadkowej, cztery sekcje (planowanie, następna wsadka, notatki, podpis), retencja 3 lata papier + 5 lat skan.

**Target wilgotności** (*target wilgotności*, EN *target moisture content*, ES *humedad objetivo*, UK *цільова вологість*): docelowa wilgotność drewna po suszeniu, zależna od zastosowania: 8-10% stolarka meblowa, 12% stolarka budowlana i podłoga, 14% dąb konstrukcyjny, 18% więźba dachowa.

**Gradient wilgotności** (*gradient wilgotności*, EN *moisture gradient*, ES *gradiente de humedad*, UK *градієнт вологості*): różnica wilgotności między powierzchnią deski (suchsza) a jej rdzeniem (wilgotniejszym) po suszeniu głównym, rozpuszczana w fazie kondycjonowania, niedotrzymana powoduje pęknięcia wewnętrzne u klienta.

## Sprawdź siebie

### A. Fazy cyklu i programy

1. Wymień **pięć faz** typowego cyklu suszenia komorowego. Która z nich jest najdłuższa dla sosny 28 mm, a która dla dębu 28 mm?

2. Dla sosny 28 mm nominalny cykl to **9 dni**, dla dębu 28 mm to **22 dni**. Dlaczego dąb wymaga 2,5 razy dłuższego cyklu, choć grubość deski jest taka sama?

3. **Kondycjonowanie** to faza, którą operator początkujący chce pomijać „dla oszczędności". Dlaczego pomijanie jest błędem i po jakim czasie u klienta widać skutki?

### B. EMC i sterowanie

4. Sterownik BH-50 pokazuje: temperatura 60°C, RH powietrza 50%, wilgotność drewna 12%. Czy cykl powinien być kontynuowany, czy zakończony? Uzasadnij przez EMC.

5. Dla sosny target 12% sterownik dąży do temperatury **60°C** i RH **50%**. Dlaczego nie do RH 30% (EMC ~5%, szybsze suszenie)?

6. Trzy sondy wilgotności drewna pokazują: 11,8 / 12,0 / 12,3%. Rozrzut: 0,5%. Czy kondycjonowanie jest udane? Uzasadnij.

### C. Wsadka i jednorodność

7. Magazyn suszenia EGIDA ma: 2,42 m³ sosny + 2,22 m³ dębu + 0,68 m³ buku + 0,42 m³ brzozy = 5,74 m³. Komora BH-50 ma 38 m³ netto. Czy można uruchomić cykl? Uzasadnij.

8. Dlaczego mieszanie w jednej wsadce sosny 25 mm i sosny 45 mm jest **złe** (nawet jeśli gatunek ten sam)?

9. Wsadka ma 30 m³ sosny świeżej 30%, plus 2 m³ sosny sezonowanej 22% (chcą dosuszyć do 12%). Czy akceptujesz jednorodność? Uzasadnij.

### D. Decyzja zewnętrzna vs własna

10. Suszenie własne EGIDA: **~85 zł/m³**. Drew-Sus: **180 zł/m³ + 350 zł transport ryczałt**. Dla partii 2,42 m³ oblicz koszt Drew-Sus na m³.

11. Zlecenie ZLE-077 (0,58 m³ sosny) ma termin klienta 20.06. Suszenie własne wymaga pełnej wsadki 30 m³, zbieranie do 11.06, cykl 9 dni, wyjście 20.06 (bez buforu). Czy akceptujesz to planowanie, czy wybierasz Drew-Sus? Uzasadnij.

12. Marka „Termin > marża" Marek tłumaczył jako zasadę strategiczną. Co to oznacza dla relacji tartak-klient długofalowo?

### E. Rola operatora M3

13. Operator M3 uczestniczy w naradzie planistycznej wsadki. Czy **decyduje** o wyborze programu i wsadki? Kto ostatecznie decyduje?

14. Operator M3 widzi na panelu sterownika „alarm wentylacji, LED czerwona". Co robi: a) resetuje alarm, b) otwiera drzwi komory, c) zgłasza mistrzowi suszarni telefonem, d) wyłącza wentylator ręcznie? Wybierz i uzasadnij.

15. Operator M3 po zaliczeniu szkolenia suszarniczego pomocniczego (5 dni + egzamin) otrzymuje uprawnienie „operator suszarniczy pomocniczy". Co może, a czego nie może?

### F. Scenariusze planistyczne

16. EGIDA ma 28 m³ sosny świeżej w magazynie suszenia. Klient oczekuje odbioru tarcicy suchej za 18 dni. Cykl sosny 9 dni + transport 1 dzień + obróbka 4 dni + bufor 1 dzień = 15 dni. Zbieranie kolejnych 2 m³ do pełnej wsadki 30 m³ to 2 dni. Czy ruszasz komorę dzisiaj, czy czekasz 2 dni? Uzasadnij.

17. Pan Henryk urlop 2 tygodnie 20.06-04.07. W tym czasie komora ma zaplanowany cykl dębu 22 dni (start 15.06, wyjście 07.07). Kto odpowiada za komorę podczas urlopu Pana Henryka i co to oznacza dla operatora M3?

18. Suszarnia zewnętrzna Drew-Sus pracuje z tym samym sterownikiem Brunner co EGIDA, ma te same programy. Dlaczego nie zamawiać 100% suszenia tam i zamknąć własną komorę? Podaj dwa powody operacyjne i jeden ekonomiczny.
