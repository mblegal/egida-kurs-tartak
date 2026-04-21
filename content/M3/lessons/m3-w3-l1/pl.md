---
id: m3-w3-l1
blok: procesy
czas: 120
---

## Wprowadzenie

Poniedziałek, 2026-05-26, godzina 6:58. Rustam wchodzi do hali pilarek. Za nim Wahan. Po weekendzie, po domkniętej w czwartek kampanii dębowej, po serwisie Pana Krzysztofa w czwartek rano (l8, cylinder podnoszenia głowicy LT70 wymieniony, olej Shell TTF-SB dolany, test szczelności 30 minut zaliczony), P3 od czwartku po południu pracuje bez wycieku. W piątek pracował na niej Damian (drugi operator samodzielny EGIDA, kończył resztki sosny). W poniedziałek rano maszyna stoi ciepła od weekendowego wstępnego rozgrzania z soboty rana (z m3-w1-l7), gotowa na nowe zlecenie.

W kieszeni kombinezonu Rustama leży **dyspozycja produkcyjna** w papierze, format A5, wydrukowana w piątek 16:00 przez Marka Kowalskiego. Zlecenie **ZLE-2026-05-077**, odebrane w biurze EGIDA przy wejściu o 6:55. Marek pokazał krótko, pytając „*Rustam, weźmiesz to na P3 dziś?*", na co Rustam potwierdził ruchem głowy, sprawdził surowiec na magazynie, wrócił do hali. Dyspozycja wygląda tak:

```
EGIDA TARTAK STRZAŁOWO
Dyspozycja produkcyjna nr ZLE-2026-05-077
Data wystawienia: 2026-05-22 (piątek)
Data realizacji: 2026-05-26 (poniedziałek), zmiana 7:00-15:00

Surowiec: sosna zwyczajna (Pinus sylvestris), magazyn SO-SOS-12,
          4 pnie, dłużyca 4,1 m, średnia średnica 32 cm,
          wilgotność bieżąca 32% (świeża, cięta 2026-05-18),
          klasa C (bez wad krytycznych, zakwalifikowana przez Panią Anię 23.05)

Sortyment docelowy: deski podłogowe surowe
                    28 × 155 × 4050 mm (naddatek +3 mm grubość, +5 mm szerokość, +50 mm długość)
                    Klasa wytrzymałościowa: C24 (wymóg klienta)
                    Cel po suszeniu i obróbce: 25 × 150 × 4000 mm, wilg. 12%

Ilość docelowa: około 0,55 m³ tarcicy surowej (odpowiada ~0,48 m³ po suszeniu i obróbce)

Maszyna: P3 Wood-Mizer LT70 (priorytet) lub P1 Serra SM40 (zastępcza)
Operator: R. Nazarov
Pomocnik: W. Petrosjan (M1 stacjonarny P3)

Dobór parametrów cięcia: decyzja operatora samodzielnego (M3)
  - Wpisać wybrane parametry w kartę KDP-001 przed pierwszym cięciem
  - W razie wątpliwości konsultacja z brygadzistą (M. Kowalski, tel. 501 ***)

Podpis wystawiającego: M. Kowalski, brygadzista EGIDA, 2026-05-22
```

Trzy linie w dyspozycji są kluczowe: **surowiec**, **sortyment docelowy**, **dobór parametrów decyzja operatora**. Do marca 2026 (M2, pod nadzorem) parametry dobierał brygadzista i wpisywał w dyspozycji. Od kwietnia, odkąd Rustam zdał egzamin M3 i przeszedł na „samodzielnego", to **operator** wybiera: jaką taśmę zakłada, jakie napięcie ustawia, z jaką prędkością posuwu rusza, jaki schemat cięcia stosuje i w jakiej kolejności tnie pień. Brygadzista widzi wybór po fakcie (karta KDP-001 w kopercie kurierskiej do biura, koniec zmiany).

Rustam kładzie dyspozycję na panelu P3, bierze z biurka w kącie hali świeżą **kartę KDP-001** (karta doboru parametrów, format A4, wprowadzona w EGIDA w marcu 2026 po sugestii audytora zewnętrznego jako narzędzie dowodowe: kto co i kiedy ustawił). Wahan patrzy zza ramienia, kalendarzyk otwarty. „*Wahan, dziś uczymy się, jak się decyduje parametry. Patrz, jak myślę, bo będziesz kiedyś myślał tak sam.*"

### 7:02, analiza surowca i sortymentu

Rustam idzie do magazynu SO-SOS-12, półka 4, gdzie leżą cztery pnie przygotowane w piątek. Metr stalowy, wilgotnościomierz Tanel ET-6 (ten sam z lekcji M2 o wilgotności), latarka LED. Każdy pień sprawdza:

- **Pień 1** (SO-SOS-12-P1): dł. 4,12 m, śr. czołowa 34 cm, śr. odziomkowa 36 cm, zbieżystość 0,5 cm/m (dobra). Wilgotność w cieńszym końcu, 5 cm od czoła, 8 mm głębokości: **33,2%**. Drugi pomiar 1 m od czoła: 31,8%. Trzeci 2 m od czoła: 32,5%. **Średnia 32,5%** (świeża, klasyczna sosna po 7 dniach od zrębu). Wady widoczne: sęk żywiczny w cieńszym końcu na 80 cm długości, średnica sęka 3 cm (dopuszczalny dla C24 wg PN-EN 1611-1, zobacz l2 M3 T2). Bez pęknięć rdzeniowych widocznych czołowo.
- **Pień 2** (SO-SOS-12-P2): dł. 4,09 m, śr. 31 cm, wilg. 31,9%, bez wad widocznych czołowo. Najlepszy z czwórki.
- **Pień 3** (SO-SOS-12-P3): dł. 4,15 m, śr. 33 cm, wilg. 33,5%, na odziomku czoła drobne pęknięcie promieniowe 8 cm długości, dopuszczalne dla C24 (limit 1/3 średnicy, czyli 11 cm). Pień do cięcia ostrożnie, pęknięcie pójdzie w dół.
- **Pień 4** (SO-SOS-12-P4): dł. 4,11 m, śr. 30 cm (najsmuklejszy), wilg. 32,1%, bez wad. Z niego wyjdzie mniej desek niż z innych, ale wszystkie równej jakości.

Sumaryczna objętość netto (kalkulacja uproszczona, średnia cylindra): **~1,32 m³ dłużycy**. Spodziewany uzysk dla sosny zwyczajnej na deski podłogowe 28 mm: **55-60%** (to znaczy z 1,32 m³ dłużycy wyjdzie 0,73-0,79 m³ tarcicy surowej). Zlecenie wymaga 0,55 m³, czyli jest **bufor 25-30%** na odrzuty, wady wewnętrzne wykryte po cięciu, niezgodność klasy wytrzymałościowej. Bufor komfortowy, ale nie nadmiarowy.

Rustam notuje te dane w karcie KDP-001 w sekcji „Surowiec wejściowy". Wahan przepisuje do kalendarzyka, Rustam go nie poprawia, niech się uczy notowania.

### 7:15, decyzja o taśmie

Rustam wraca do hali, staje przed szafą z taśmami (regał metalowy przy P3, 8 półek, każda z taśmą zapasową na rolce w papierze ochronnym). Pamięta z l6 i l7: **pilarka taśmowa LT70 EGIDA używa taśm 38 × 1,07 mm**. Typ stali, kąt natarcia (hook angle), podziałka zębów (tooth pitch) i rodzaj ostrzenia (stellite, stop, hartowanie) są zmienne.

Możliwe taśmy w szafie:

1. **Stellite 38/7-9** (stal stellitowa, podziałka zmienna 7 i 9 TPI, kąt natarcia 9°), nr magazynowy ST-38-7/9-S12. **Typowa do dębu i buku twardego**. Cena 380 zł netto.
2. **Stopowa 38/7/8** (stal stopowa, podziałka 7/8 TPI stała, kąt natarcia 10°), nr ST-38-7/8-A12. **Uniwersalna sosna-świerk**. Cena 145 zł netto.
3. **Stopowa 38/10** (stal stopowa, podziałka 10 TPI stała, kąt 10°), nr ST-38-10-A12. Dla **cienkich desek** (poniżej 20 mm grubości), drobniejsze wióry. Cena 165 zł netto.
4. **Stopowa 38/22 rzadka** (podziałka 22 TPI, kąt 13°, do **przecinania kłód o dużej średnicy** i do drewna zamrożonego). Cena 175 zł netto. Z l6, używana do dębu w awaryjnej sytuacji.
5. **Stellite 38/10** (stal stellitowa, podziałka 10 TPI, kąt 9°), nr ST-38-10-S12. Dębina grubszych desek. Cena 405 zł netto.
6. **Zużyte do kilkukrotnego ostrzenia** (odłożone w osobnym miejscu, do końca życia)

Rustam myśli głośno po polsku, Wahan słucha:

*„Zlecenie to sosna świeża, 32% wilgotności, grubość docelowa 28 mm mokre. Do sosny świeżej wybieramy stal **stopową**, nie stellite. Stellite kosztuje 2,5 raza więcej i trzyma ostrość dłużej, ale na sośnie świeżej żywica szybko zalepia stellit, tępienie jest szybsze niż na dębie. W sosnie lepiej taśma tańsza stopowa, ostrzona częściej."*

*„Grubość 28 mm to średnia, nie cienka. Dla desek powyżej 22 mm podziałka **7/8 TPI** jest optymalna. Drobniejsze (10 TPI) tnie wolniej i robi za dużo wiórów. Dobieram **stopową 38/7/8**, taśmę numer ST-38-7/8-A12."*

*„Kąt natarcia 10° to standardowy dla sosny. Dla dębu byłby 9° (twardsze drewno, mniejszy kąt żeby nie zrywało się zębów). Dla mrożonej sosny 13° (większy kąt, lepsze wprowadzenie w drewno). Dziś majowa świeża sosna, 10° dobrze."*

Wyjmuje taśmę z szafy, sprawdza nalepkę: ST-38-7/8-A12, dostawca Wood-Mizer Polska, data ostrzenia ostatniego **2026-05-20** (rozgrzewka ostrzarni w zakładach WM przed sezonem), licznik cięć od ostrzenia **0** (świeża). Idealna.

W KDP-001, sekcja „Wybór taśmy":
```
Taśma: stopowa 38 × 1,07 mm, podziałka 7/8 TPI, kąt natarcia 10°
Nr magazynowy: ST-38-7/8-A12
Licznik po ostrzeniu: 0 (świeża od 2026-05-20)
Uzasadnienie: sosna świeża 32%, deski 28 mm, optymalna stopowa 7/8 TPI
```

### 7:22, napięcie i prowadniki

Rustam otwiera osłonę boczną P3, podnosi dźwignię naprężacza do pozycji LUZ, zdejmuje poprzednią taśmę (ta od Damiana z piątku, stopowa 38/7/8 z nalepką zużycia 140 cięć, wraca do rotacji do ostrzenia), zakłada świeżą. Prowadzenie taśmy między kołami: napięcie, regulacja prowadników, alignment (wyrównanie w pionie).

**Napięcie taśmy** jest parametrem **operatora-zależnym** (z l6 M3 T2). Manometr Wood-Mizer LT70 pokazuje wartość w PSI (funty na cal kwadratowy). Zakres bezpieczny dla taśm 38 mm: **2200-2400 PSI**. Wybór wewnątrz zakresu:

- Twarde drewno (dąb, buk, jesion), taśma stellite: **2400 PSI** (maksimum w zakresie). Większe napięcie trzyma taśmę sztywniej w pionie, mniej drgań w cięciu, czystszy rzaz, ale większe obciążenie spoiny (ryzyko zerwania) i kół taśmowych.
- Miękkie drewno (sosna, świerk), taśma stopowa: **2200 PSI** (dolna granica zakresu). Taśma „oddycha", mniej ryzyko zerwania, mniejsze obciążenie kół. Rzaz minimalnie bardziej wrażliwy na sęki ale akceptowalnie.
- Drewno mrożone albo bardzo twarde (dąb mrożony, egzotyczne): **2400 PSI** plus ostrożna obserwacja manometru pierwszych 5 minut cięcia.

Dzisiaj sosna świeża, stopowa 7/8. Rustam ustawia **2200 PSI** (obraca pokrętło naprężacza pięć i pół obrotu w prawo, obserwuje manometr rosnący). Manometr zatrzymuje się na 2200, lekko drga, ale nie spada. Temperatura hali 18°C, bez dryfu napięcia. **OK**.

**Prowadniki taśmy** (rolki z obu stron taśmy, dolna i górna, regulują boczne położenie taśmy i zapobiegają „pływaniu" taśmy w cięciu). Każdy prowadnik ma regulację **odległości od taśmy**. Zakres: **3-4 mm** (z l6). Za ciasno (poniżej 3 mm): prowadnik dotyka taśmy, grzeje się, szybko się zużywa, generuje drgania. Za luźno (powyżej 4 mm): taśma „pływa", rzaz falisty.

Rustam regulacja szczelinomierzem 3,5 mm (standard EGIDA, środek zakresu). Cztery punkty regulacji (dolne i górne, lewy i prawy). Każdy po kolei: szczelinomierz wsuwa się luźno, ale nie z luzem. Jeżeli wsuwa się za luźno, pokrętło regulacji obraca w prawo o 1/8 obrotu. Jeżeli w ogóle nie wchodzi, obraca w lewo o 1/4 obrotu. **Kalibracja 3 minuty, cztery punkty OK**.

W KDP-001, sekcja „Ustawienia maszyny":
```
Napięcie taśmy: 2200 PSI (dolna granica zakresu dla sosny i stopowej)
Prowadniki taśmy: 3,5 mm szczelina, cztery punkty skalibrowane
Temperatura hali start: 18°C
```

### 7:30, prędkość posuwu i schemat cięcia

**Prędkość posuwu** (feed rate) to prędkość, z jaką głowica pilarki przesuwa się po szynie podczas cięcia. Mierzona w stopach na minutę (imperial Wood-Mizer) albo metrach na minutę. Panel LT70 EGIDA pokazuje w stopach/min, Rustam w głowie przelicza na m/min (1 stopa = 0,305 m, czyli 30 stóp/min ≈ 9 m/min).

Zakres dla LT70: **0-80 stóp/min** (0-24 m/min). Wybór zależny od czterech czynników:

1. **Gatunek drewna**. Sosna miękka → szybko (30-40 st/min). Dąb twardy → wolno (10-20 st/min). Buk → średnio (15-25 st/min).
2. **Wilgotność**. Świeże drewno → szybciej (opór cięcia mniejszy). Suche → wolniej (większy opór, większe grzanie taśmy).
3. **Grubość rzazu**. Grube deski (50+ mm) → wolniej (dłużej w drewnie, więcej wiórów). Cienkie (poniżej 25 mm) → szybciej (mniej materiału usuwanego).
4. **Średnica pnia**. Duży pień → wolniej w pierwszym przetarciu (cięcie przez sam rdzeń najtrudniejsze). Mały pień → szybciej.

Dzisiejsze warunki: sosna świeża, 28 mm grubość, średnica 32 cm. Rekomendacja Wood-Mizer w DTR LT70, tabela 3.5: **30-35 stóp/min** (9-10,5 m/min). Rustam wybiera **32 stopy/min** jako start (środek zakresu). Możliwa korekta po pierwszym cięciu (obserwacja rzazu, prostość deski, dźwięk silnika).

**Schemat cięcia** (sawing pattern) to kolejność cięć i sposób obracania pnia. Dwa podstawowe schematy dla desek podłogowych z sosny:

**Schemat A: przeciąganie pierwszego blatu (cant sawing).** Pień leży płasko na łóżku maszyny. Pierwsze cięcie zdejmuje **oblinę** (zaokrąglony brzeg z korą). Obrót 180°, drugie cięcie zdejmuje drugą oblinę. Obrót 90°, trzecie cięcie zdejmuje trzecią oblinę. Obrót 180°, czwarte cięcie zdejmuje czwartą oblinę. Teraz mamy kwadratowy blat (**cant**). Z blatu tniemy równolegle deski 28 mm grubości. **Zalety**: prosty, szybki (operator nie rotuje pnia często), dobry uzysk dla średnich i dużych pni (30 cm +). **Wady**: w każdej desce jest rdzeń drewna w środku długości, co obniża klasę wytrzymałościową (C24 wymaga max 25% rdzenia).

**Schemat B: czwartowanie z obrotem (quarter sawing).** Pień cięty pionowo przez rdzeń na dwie połowy. Każda połowa obrócona o 90°, cięta pionowo przez oś rdzenia na ćwiartki. Ćwiartki cięte równolegle na deski. **Zalety**: słoje roczne w desce prostopadłe do powierzchni (wytrzymałość mechaniczna wyższa, stabilność wymiarowa lepsza, klasa C24 + pewniejsza, czasem C30). **Wady**: więcej operacji, wolniej, mniejszy uzysk dla wąskich pni (poniżej 30 cm strata duża), wymaga obracania pnia.

Rustam myśli: *„Zlecenie wymaga C24. Klasa pewna, nie C30 ani nie C16. Schemat A jest szybszy i daje C24 dla sosny zwyczajnej 32% wilgotności bez problemu. Schemat B byłby lepszy dla C30 ale zlecenie tego nie wymaga, wkład pracy operatora byłby dwa razy większy, uzysk o 5% gorszy. **Wybieram A**, standardowy cant sawing."*

W KDP-001, sekcja „Parametry cięcia":
```
Prędkość posuwu: 32 stopy/min (środek zakresu 30-35 dla sosny świeżej 28 mm)
Schemat cięcia: A (cant sawing, obrót 4 razy, pierwsze cięcie zdejmuje oblinę)
Grubość deski: 28 mm (+3 mm naddatek suszenia i obróbki do 25 mm docelowo)
Szerokość deski: 155 mm (+5 mm naddatek do 150 mm docelowo)
Długość deski: 4050 mm (+50 mm naddatek odcięcia końców do 4000 mm)
Strategia pasów: 4 oblin + 8-10 desek z blatu (planowane 8 desek z P1 i P2, po 9-10 z P3 i P4)
```

### 7:38, ostatnie sprawdzenie, start

Karta KDP-001 wypełniona, Rustam składa po formacie A4 (jedno złożenie), wkłada do papierowej koperty z adnotacją „**ZLE-2026-05-077 P3 26.05 Rustam**", kładzie na biurku brygadzisty w kącie hali. Marek odbierze po zmianie.

Na panelu P3: ustawienie prędkości posuwu **32 stopy/min** (potencjometr na panelu, skala 0-80, obrót do pozycji środkowej między 30 a 35). Wysokość głowicy ustawiona: pierwsze cięcie zdejmie oblinę o grubości 3-5 cm (zależy od zbieżystości pnia, ocena wzrokowa Rustama).

Wahan stoi przy podajniku pomocniczym, ma za zadanie odbierać oblinę i deski z platformy odbiorczej (operator LT70 jest sam na platformie głównej). Między nimi komunikacja wzrokowa i krótkie gesty (z M1 l1: „STOP" = płasko dłoń w pionie, „dalej" = okrągły ruch, „wolniej" = dłoń w dół).

**7:40 silnik włączony**, 37 kW elektryczny, zielona LED, pomarańczowa LED w trybie ready, taśma rozruch obrotów. 10 sekund rozbiegu do pełnej prędkości. 7:41 pierwsze cięcie, pień 1, zdjęcie pierwszej obliny. Deski idą.

## Cele

Po tej lekcji:

1. Znasz **pięć parametrów cięcia**, które operator samodzielny dobiera przed rozpoczęciem zlecenia na pilarce taśmowej: 1) **dobór taśmy** (typ stali stellite vs stopowa, szerokość 38 mm stała dla LT70, podziałka zębów 7/8 vs 10 vs 22 TPI, kąt natarcia 9-13°); 2) **napięcie taśmy** (2200-2400 PSI wewnątrz zakresu bezpiecznego, wybór zależny od gatunku i typu stali); 3) **prowadniki taśmy** (szczelina 3-4 mm, cztery punkty regulacji); 4) **prędkość posuwu** (0-80 stóp/min, wybór 10-40 w praktyce, zależny od gatunku, wilgotności, grubości rzazu, średnicy pnia); 5) **schemat cięcia** (cant sawing A standardowy lub quarter sawing B dla wyższych klas wytrzymałościowych). Rozumiesz, że żaden z tych parametrów nie jest podany w dyspozycji, wszystkie są **decyzją operatora**.
2. Rozumiesz **jak gatunek i wilgotność wpływają na dobór taśmy i napięcia**. Sosna i świerk świeże (wilg. 25-35%) → stopowa, napięcie 2200 PSI. Sosna i świerk suche (poniżej 20%) → stopowa z większym kątem natarcia lub stellite, napięcie 2300 PSI. Dąb, buk, jesion twarde → stellite, napięcie 2400 PSI. Drewno mrożone (zimą, grudzień-luty) → stopowa z kątem 22 TPI, napięcie 2400 PSI. Rozumiesz, że **żywica** w sośnie szybciej zalepia stellit niż stopową, dlatego stopowa jest preferowana dla świeżej sosny pomimo szybszego tępienia.
3. Znasz **zasadę doboru prędkości posuwu** na podstawie zmiennych: gatunek (sosna 30-40, buk 15-25, dąb 10-20 stóp/min jako punkty startowe), wilgotność (korekta do 10% szybciej dla świeżego, do 10% wolniej dla suchego), grubość rzazu (deski powyżej 50 mm wolniej), średnica pnia (duży pień wolniej w pierwszym przetarciu). Rozumiesz, że wybór to **start**, nie docel, i wymaga **korekty po pierwszym cięciu** na podstawie obserwacji rzazu, prostości deski i dźwięku silnika.
4. Rozumiesz **różnicę między schematem A (cant sawing) i schematem B (quarter sawing)**. Schemat A: obrót pnia 4 razy, zdjęcie 4 oblin do kwadratu, potem równolegle deski z blatu. Szybki, uniwersalny, dobry dla C24. Schemat B: rozcięcie pnia na połowy przez rdzeń, potem na ćwiartki, potem deski równolegle. Wolniejszy, droższy w pracy, lepsza klasa wytrzymałościowa (C30+), lepsza stabilność wymiarowa. Rozumiesz, że **wybór schematu zależy od wymagań klasy z zlecenia**, nie od preferencji operatora, i że próba „wyjścia wyżej" poza wymaganie klienta to marnowanie pracy operatora.
5. Znasz **kartę doboru parametrów KDP-001** wprowadzoną w EGIDA w marcu 2026. Format A4, cztery sekcje: „Surowiec wejściowy" (wymiary, wilgotność, wady pni), „Wybór taśmy" (typ, nr magazynowy, licznik po ostrzeniu), „Ustawienia maszyny" (napięcie, prowadniki, temperatura hali), „Parametry cięcia" (prędkość posuwu, schemat, grubości, długości). Wypełniana **przed pierwszym cięciem**, kopia do brygadzisty po zmianie, retencja 2 lata w papierze plus 5 lat w skan do OneDrive. Podstawa prawna udokumentowania: audyt jakości ISO 9001 (EGIDA jest certyfikowana), śledzenie zlecenia wstecz w razie reklamacji (l2 m3-w4), oraz **art. 211 pkt 7 Kodeksu pracy** (pracownik obowiązany współdziałać z pracodawcą w realizacji obowiązków BHP).
6. Potrafisz **przeprowadzić decyzję parametryczną** w ciągu **30-40 minut** przed rozpoczęciem zmiany na konkretnym zleceniu. Etapy: 1) odczytanie dyspozycji (5 min); 2) inspekcja surowca na magazynie (10 min, pomiary wilgotności, oględziny wad); 3) decyzja o taśmie (5 min, wybór z szafy na podstawie gatunku i sortymentu); 4) montaż taśmy, napięcia, prowadników (10 min); 5) decyzja o prędkości posuwu i schemacie (5 min, wpis w KDP-001); 6) start. Rozumiesz, że **pospiech w tym 30-40 minutowym oknie generuje błędy kosztujące 2-4 godziny** późniejszej korekty lub w skrajnym przypadku zerwaną taśmę i koszt 150 zł plus 40 minut wymiany awaryjnej.

## Treść

### 1. Które parametry wybiera operator, a które są stałe

W pilarce taśmowej Wood-Mizer LT70 (ani w Serra SM40, ani w żadnej innej stacjonarnej pilarce taśmowej w EGIDA) nie wszystkie parametry są do wyboru. Część jest ustawiona raz przy instalacji maszyny i nigdy nie zmieniana, część jest wymuszona przez konstrukcję maszyny (szerokość taśmy np.), a część jest stała dla zlecenia (wymiar docelowy deski jest podany w dyspozycji, nie wynika z decyzji operatora).

**Parametry stałe konstrukcyjne** (operator nie zmienia):
- Szerokość taśmy: **38 mm** (LT70 używa tej szerokości, Serra też, P1-P3 wszystkie 38 mm)
- Grubość taśmy: **1,07 mm** (standard Wood-Mizer, inne grubości wymagałyby zmiany kół prowadzących)
- Moc silnika: **37 kW** elektryczna dla EGIDA, LT70 ma też wersję 48 kW spalinową, ale to decyzja zakupowa, nie operatora
- Zakres prędkości posuwu: **0-80 stóp/min** (fizyczny limit szyny masztu pionowego i silnika posuwu)
- Zakres napięcia taśmy: **2200-2400 PSI** bezpieczny (manometr ma zakres 0-3000, ale powyżej 2400 PSI ryzyko zerwania spoiny rośnie wykładniczo)

**Parametry wymuszone przez dyspozycję** (operator wykonuje, nie decyduje):
- Gatunek drewna (z magazynu, wybiera brygadzista przy zakupie od leśnictwa)
- Klasa wytrzymałościowa docelowa (C24, C30, C16, podaje klient)
- Wymiar deski docelowy po suszeniu i obróbce (zlecenie klienta)
- Ilość desek (ze zlecenia)

**Parametry decyzyjne operatora**:
1. Wybór taśmy z szafy (typ stali, podziałka zębów, kąt natarcia)
2. Napięcie taśmy w zakresie 2200-2400 PSI
3. Regulacja prowadników (3-4 mm szczelina)
4. Prędkość posuwu (10-40 stóp/min typowo)
5. Schemat cięcia (A cant vs B quarter)
6. Kolejność pni w zleceniu (który pień pierwszy, dlaczego)
7. Naddatki na grubość deski (plus 2-4 mm ponad wymiar docelowy)
8. Moment korekty parametrów (po pierwszym cięciu, po pierwszych 10 cm, po pierwszej desce)

To osiem decyzji, które operator M3 podejmuje co zmianę. Operator M2 (pod nadzorem) wykonuje parametry podane przez brygadzistę w dyspozycji, operator M1 (pomocnik) wykonuje czynności pomocnicze bez decyzji parametrycznej. **Samodzielność parametryczna** jest kluczową różnicą M3.

### 2. Dobór taśmy pod gatunek i sortyment

Z l6 M3 T2 wiemy: taśma pilarki taśmowej ma cztery zmienne:

- **Typ stali**: stopowa (alloy steel) vs stellite (stal z warstewką stellite na zębach). Stopowa tańsza, ostrzy się łatwo, szybciej tępi się na twardym drewnie. Stellite trzyma ostrość 3-5 razy dłużej, ale kosztuje 2,5 raza więcej i nie znosi żywic sosnowych.
- **Podziałka zębów** (tooth pitch, TPI, teeth per inch): 7 TPI = rzadka (grube deski), 10 TPI = średnia (cienkie deski), 22 TPI = bardzo rzadka (duże średnice, mrożone drewno). Liczba zębów na cal. Rzadsza podziałka = większe wióry = szybsze cięcie, grubsze deski. Gęstsza podziałka = mniejsze wióry = gładszy rzaz, cienkie deski.
- **Kąt natarcia** (hook angle): 9°, 10°, 13°. Mniejszy kąt (9°) = mniej agresywne wcinanie, dobre dla twardego drewna, mniej ryzyka zerwania zęba. Większy kąt (13°) = bardziej agresywne, dobre dla miękkiego lub mrożonego, większa wydajność ale większe obciążenie taśmy.
- **Typ ostrzenia zębów**: zwykłe szlifowanie stali, szlifowanie plus nakładka stellite, indukcyjne utwardzenie. Dla EGIDA dwa pierwsze typy w rotacji.

**Tabela doboru taśmy dla typowych sytuacji w EGIDA** (kompilacja Wood-Mizer DTR plus doświadczenie brygadzistów):

| Gatunek i stan | Sortyment | Taśma typ | Podziałka | Kąt | Przykładowa nalepka |
|---|---|---|---|---|---|
| Sosna świeża 25-35% | Deski 22-32 mm | Stopowa | 7/8 | 10° | ST-38-7/8-A12 |
| Sosna świeża | Deski 15-20 mm (cienkie) | Stopowa | 10 | 10° | ST-38-10-A12 |
| Sosna sucha < 20% | Deski 22-32 mm | Stellite | 9 | 9° | ST-38-9-S12 (zużyta żywicą wolniej) |
| Dąb świeży 30-40% | Deski 22-32 mm | Stellite | 7/9 | 9° | ST-38-7/9-S12 (skuteczna na świeżym dębie) |
| Dąb suchy 20-25% | Deski 22-32 mm | Stellite | 9 | 9° | ST-38-9-S12 |
| Buk / jesion | Deski 22-32 mm | Stellite | 7/9 | 9° | ST-38-7/9-S12 |
| Mrożone (grudzień-luty) | każde | Stopowa | 22 | 13° | ST-38-22-A12 |
| Duża średnica (45+ cm) | Deski grube 40+ mm | Stopowa | 22 | 13° | ST-38-22-A12 |

Dla dzisiejszego zlecenia (sosna świeża 32%, deski 28 mm) pierwszy wiersz: **stopowa 7/8, kąt 10°**. Rustam wybrał ST-38-7/8-A12 z magazynu. Prawidłowo.

### 3. Napięcie taśmy, głębokie wpłynięcie na cięcie

Napięcie taśmy w pilarce taśmowej to siła, z jaką koła pilarki ciągną taśmę w pionie. Manometr LT70 pokazuje w PSI (funty na cal kwadratowy, 1 PSI ≈ 0,0069 MPa, 2200 PSI ≈ 15 MPa). Fizycznie: taśma jest sznurem tnącym między dwoma kołami, napięcie utrzymuje ją prostą w płaszczyźnie cięcia. Za mało napięcia, taśma „oddycha", płynie w cięciu, rzaz falisty. Za dużo napięcia, spoina taśmy (miejsce gdzie taśma została zgrzana w zamkniętą pętlę) jest przeciążona, rośnie ryzyko zerwania, typowy koszt 145-200 zł za taśmę plus 40 minut wymiany.

**Zakres bezpieczny LT70**: **2200-2400 PSI**. Dolna granica 2200 to minimum dla akceptowalnego rzazu prostego. Górna 2400 to granica, powyżej której producent (Wood-Mizer) nie gwarantuje trwałości spoin. W praktyce EGIDA wybór wewnątrz zakresu:

- **2200 PSI**: sosna i świerk (miękkie, żywicowe), stopowa taśma, zwykłe cięcie letnie.
- **2300 PSI**: drewno mieszane w zmianie (połowa sosny, połowa dębu), kompromis.
- **2400 PSI**: dąb, buk, jesion (twarde), stellite taśma, albo drewno mrożone. Maksimum.

**Co się zmienia z każdym 100 PSI w górę**:

- Rzaz bardziej prosty (mniej „fali"), szczególnie na sękach i wadach wewnętrznych
- Deska wychodzi bardziej równomierna grubości (mniej +/-0,5 mm na 4 m długości)
- Wibracje taśmy mniejsze, dźwięk cięcia wyższy i równomierniejszy
- Zużycie spoiny taśmy rośnie (średnia żywotność taśmy 140-180 cięć przy 2200 PSI, 110-140 cięć przy 2400 PSI)
- Obciążenie łożysk kół rośnie (ale niewielkie, poniżej 1% skrócenia żywotności na każde 100 PSI)

Dla dzisiejszego zlecenia (sosna świeża, stopowa, komfortowo w pracy) **2200 PSI** jest wyborem standardowym. Rustam tak ustawił. Dla sosny suchej lub mieszanki sosny z modrzewiem (który jest twardszy) rozważałby 2300.

**Pułapka częsta początkujących**: „wystarczy napiąć bardziej, rzaz będzie lepszy". Nie zawsze, bo czasem lepszy rzaz daje korekta prędkości posuwu (wolniej), a nie napięcie. I napięcie powyżej 2400 PSI kosztuje taśmą częściej niż daje jakością rzazu.

::: info
**Manometr LT70 nie mierzy bezpośrednio PSI w taśmie**, mierzy ciśnienie oleju hydraulicznego w cylindrze naprężacza. Skala jest skalibrowana przy produkcji maszyny (tabela konwersji ciśnienie hydrauliczne → PSI taśmy). Skalibrowanie jest trwałe, ale **uszczelka cylindra** (ta sama co w l8) jeżeli przecieka, manometr pokazuje zaniżoną wartość. Dlatego w KDP-001 wpisujemy wartość z manometru razem z datą kalibracji ostatniej. Serwis Wood-Mizer Polska sprawdza kalibrację raz w roku (przegląd B z l8).
:::

### 4. Prowadniki taśmy, drobne ale krytyczne

Prowadniki taśmy to cztery rolki (dolne i górne, lewa i prawa), między którymi taśma przechodzi przed cięciem. Rola: **trzymają taśmę w jednej płaszczyźnie**, nie pozwalają jej odchylać się w bok pod naporem cięcia w drewno.

Każdy prowadnik jest regulowany śrubą. Oddalenie rolki od taśmy mierzone jest szczelinomierzem (uniwersalny przyrząd stalowy z zestawem łopatek o różnych grubościach, w EGIDA 0,05 do 1,00 mm). Standardowa szczelina w LT70: **3-4 mm**.

- **3 mm** (dolna granica): dla twardego drewna, dla taśmy stellite, lepsze prowadzenie, lekka strata na zużycie prowadników (o ~20% szybsze tępienie)
- **4 mm** (górna granica): dla miękkiego drewna, stopowej, mniejsze tarcie, dłuższa żywotność prowadników
- **3,5 mm**: standard EGIDA dla typowej pracy, kompromis

**Cztery punkty regulacji**: lewy górny, prawy górny, lewy dolny, prawy dolny. Każdy regulowany osobno. W teorii wszystkie cztery powinny być identyczne. W praktyce dopuszczalne odchylenie **0,1 mm** (szczelinomierz 0,1 mm wchodzi w jednym punkcie, nie wchodzi w sąsiednim).

**Kalibracja jako procedura operatora przed każdą zmianą** (jeżeli nie jest to wymiana taśmy):
1. Wyciągnij szczelinomierz na grubość rekomendowaną (np. 3,5 mm).
2. Wsuń między rolkę prowadnika a taśmę. Powinien wchodzić z lekkim oporem, ale bez siłowania.
3. Jeżeli wchodzi za łatwo (luźno) → pokrętło regulacji w prawo o 1/8 obrotu, ponowna próba.
4. Jeżeli nie wchodzi w ogóle → pokrętło w lewo o 1/4 obrotu, ponowna próba.
5. Cztery punkty po kolei, czas łączny 3-5 minut.

Brak kalibracji prowadników to jeden z trzech najczęstszych powodów falistego rzazu (pozostałe dwa: zbyt niskie napięcie taśmy, zbyt wysoka prędkość posuwu). Operator M1 i M2 nie sprawdza prowadników (robi to operator samodzielny), ale patrzy przez ramię operatorowi M3 jak to robi.

### 5. Prędkość posuwu, parametr najbardziej dynamiczny

Prędkość posuwu jest jedynym parametrem, który **zmienia się w trakcie zmiany**. Taśma jest taka sama, napięcie jest takie samo, prowadniki są takie same. Ale prędkość **korygujesz** na podstawie obserwacji cięcia.

**Start**: rekomendacja Wood-Mizer z DTR (tabela 3.5 LT70) albo doświadczenie EGIDA. Dla sosny świeżej 28 mm deska, jak Rustam dzisiaj: **32 stopy/min** (środek zakresu 30-35 rekomendowanego).

**Korekta po pierwszym cięciu** (pierwsza oblina zdjęta, Rustam patrzy na powierzchnię cięcia):

- Powierzchnia **gładka i prosta** (rzaz jak kartka papieru, bez fali) → prędkość OK, zostaw 32.
- Powierzchnia **z delikatnym „łuskowaniem"** w kierunku cięcia (małe piki co 5-10 cm na długości) → prędkość **za szybka**, zmniejsz do 28-30 stóp/min.
- Powierzchnia **falista** (fala o amplitudzie 1-2 mm co 20-30 cm) → prędkość **dużo za szybka**, ale częściej przyczyną jest **tępa taśma** albo **niewłaściwe napięcie**. Zwolnij do 22-25 stóp/min, ale w pierwszej kolejności sprawdź taśmę.
- Deska **grubsza z jednego końca**, cieńsza z drugiego (klin) → prędkość nie jest przyczyną, to **alignment taśmy** (regulacja wyrówności taśmy względem łóżka), zadanie serwisowe, zgłoś do brygadzisty.
- Dźwięk silnika **nie równy**, „falujący" → prędkość **za szybka**, silnik dochodzi do przeciążenia, zwolnij o 3-5 stóp/min.
- Dźwięk silnika **bardzo wysoki, świszczący** → prędkość **za wolna** (silnik pracuje „luźno", taśma nie gryzie w drewno, marnowana energia), zwiększ o 3-5 stóp/min.

Rustam uczy tej korekty Wahana poprzez **nazwane przykłady**. Każdy kolejny pień ma okazję do zmiany prędkości i Wahan uczy się słuchać silnika.

**Zapis w KDP-001** końcowy (po zmianie, wieczór), w polu „Parametry rzeczywiste zastosowane":
```
Start zmiany: 32 stopy/min (sosna świeża, stopowa 7/8)
Pień 1: 32 st/min całość, rzaz prosty, OK
Pień 2: 32 st/min start, po pierwszych 2 m zmniejszone do 30 (delikatne łuskowanie), OK
Pień 3: 30 st/min start (pamięć z P2), całość 30, OK
Pień 4: 30 st/min całość, ostatnia deska lekko „szorstka" bo taśma już 140 cięć, w normie
```

To jest dokument mocy brygadzisty: widzi, że operator nie tylko ustawił parametr, ale go **śledził**.

### 6. Schemat cięcia A (cant sawing), standardowy

Schemat A, cant sawing (cięcie do kwadratu, potem równolegle):

**Etap 1**. Pień leży poziomo na łóżku, przekrój czołowy okrągły widoczny z przodu maszyny. Rustam uruchamia posuw, głowica idzie po szynie, taśma zdejmuje **pierwszą oblinę** (zaokrąglona wypukłość z górnej strony pnia, zwykle 3-5 cm grubości w środku, węższa na końcach). Grubość obliny szacuje wzrokowo przed startem ustawieniem wysokości głowicy. Efekt: pień z płaską górą.

**Etap 2**. Obrót pnia 180° (z pomocą obracarki hydraulicznej, log turner). Poprzednia góra jest teraz dołem, poprzedni dół góra. Rustam zdejmuje **drugą oblinę**. Efekt: pień z dwiema płaskimi bokami przeciwległymi, dwie obliny oryginalne po stronach lewo i prawo.

**Etap 3**. Obrót pnia 90° (ta sama obracarka). Jedna z dwóch bocznych oblin jest teraz na górze. Rustam zdejmuje **trzecią oblinę**. Efekt: pień z trzema płaskimi stronami.

**Etap 4**. Obrót pnia 180°. Ostatnia oblina (czwarta) na górze. Zdjęcie. Efekt: **kwadratowy blat (cant)**, wymiary zbliżone do kwadratu. Dla sosny Ø 32 cm średnica, kwadrat wychodzi około 23 × 23 cm (boki z poślizgiem, straty 20-25% w 4 oblinach).

**Etap 5 i dalsze**. Z cantu Rustam tnie równolegle deski o grubości 28 mm. Licząc: 23 cm / 28 mm = 8,2, czyli **8 desek** czystych plus 9. jest „pół-deska" (resztka 15-20 mm), która idzie na opał lub do obróbki jako listwa. Ośmiu desek o wymiarach 28 × 155 mm (szerokość ograniczona przekrojem cantu) i długości 4050 mm.

**Czas całego schematu A dla jednego pnia 32 cm i 4 m**: 4 obliny po ~35 sekund = 2 min 20 s, plus 8 desek po ~30 sekund (deska jest krótsza niż pień, tak samo dług) = 4 min, plus 4 obroty po ~15 s = 1 min. Łącznie **~7-8 minut** od pierwszego cięcia do ostatniej deski.

**Uzysk typowy** ze schematu A dla sosny Ø 32 cm i 4 m: **8 desek × 28 × 155 × 4050 mm = 0,141 m³** z pnia o objętości **1,04 m³** (surowa dłużyca cylinder π × 0,16² × 4 = 0,322 m³, z zapasem na zbieżność liczymy 1,04, ale czasem mniej precyzyjnie). Współczynnik uzysku: 40% przy niskiej objętości, 60% przy pełnej metryce z obliną wliczoną. Wzory są różne w literaturze, EGIDA używa uproszczonego „uzysk = objętość tarcicy surowej / objętość dłużycy" i dla sosny zwyczajnej deski 28 mm oczekuje **55-65%**.

### 7. Schemat cięcia B (quarter sawing), dla wyższej klasy

Schemat B, quarter sawing (czwartowanie):

**Etap 1**. Pień leży poziomo, Rustam ustawia pierwsze cięcie tak, że taśma idzie przez środek pnia, przez rdzeń. Cięcie trwa całą długość pnia. Efekt: **pień na dwie półkole** (bogate w kształt litery D).

**Etap 2**. Jedna półkola odkłada się (wózek pomocnika), druga obrócona o 90° względem pierwotnego ułożenia (płaski bok teraz na dole, zaokrąglenie do góry). Cięcie przez środek tej półkoli, prostopadle do pierwotnego cięcia. Efekt: **ćwiartka pnia** (kształt litery Y nieregularny).

**Etap 3**. Każda ćwiartka cięta równolegle na deski, począwszy od prostej strony wewnętrznej (tam gdzie był rdzeń). Deski pierwszych dwóch-trzech są **najlepsze**: słoje roczne prostopadłe do powierzchni deski („kwarterowe deski"), wytrzymałość mechaniczna maksymalna, stabilność wymiarowa przy zmianach wilgotności najwyższa. Deski z ćwiartki bliskiej korze są słabsze (słoje ukośne), ale wciąż lepsze niż w schemacie A.

**Etap 4**. Powtórz etapy 2-3 dla drugiej półkoli.

**Czas dla jednego pnia 32 cm i 4 m**: 1 cięcie dzielące + 2 cięcia ćwiartujące + 8-10 desek z 4 ćwiartek = **~12-15 minut** (ok. 2 razy więcej niż schemat A).

**Uzysk typowy**: **45-55%** (gorszy niż A bo więcej strat geometrycznych w kształcie ćwiartki).

**Klasa wytrzymałościowa**: **C24 pewne, C30 prawdopodobne** (na 3-4 deskach z 10 z każdego pnia).

**Kiedy wybrać B**:
- Zlecenie wymaga C30 lub C35 (klient: „muszę mieć pewną klasę C30 na elementy konstrukcyjne")
- Zlecenie wymaga wysokiej stabilności wymiarowej (meble, parkiety drogie, stolarka okienna)
- Cena sortymentu uzasadnia pracę dodatkową (dębowa podłoga parkietowa za 180 zł/m², warto)

**Kiedy nie**:
- Zlecenie C24 standardowe (dzisiejsze ZLE-077)
- Taśmy mało pozostało życia (schemat B zużywa taśmę szybciej, 15-20% skrócenie żywotności na pień)
- Presja czasowa (zlecenie na jutro, nie ma 2 razy więcej czasu)

Rustam dziś wybrał A. Wahan zapisał w kalendarzyku pytanie: „*Kiedy B?*" na rozmowę po zmianie.

### 8. Dokumentacja decyzji, karta KDP-001

KDP-001 (Karta Doboru Parametrów) to formularz A4 wprowadzony w EGIDA w marcu 2026 po audycie jakości ISO 9001 w lutym (audytor wskazał, że **brak śladu dowodowego** kto jakie parametry ustawił na zleceniu to ryzyko w razie reklamacji klienta). Struktura karty:

**Nagłówek**: nr zlecenia, data, operator, maszyna, pomocnik (jeśli jest).

**Sekcja 1, Surowiec wejściowy**:
- Lista pni z magazynu (nr magazynowy, wymiary, wilgotność, wady widoczne)
- Suma objętości szacowana
- Komentarz dot. wad krytycznych (jeżeli są, np. „P3 pęknięcie promieniowe 8 cm, ostrożność")

**Sekcja 2, Wybór taśmy**:
- Typ, szerokość, grubość, podziałka, kąt, nr magazynowy
- Data ostatniego ostrzenia
- Licznik cięć od ostrzenia (zeru dla świeżej)
- Uzasadnienie wyboru (1-2 zdania, dlaczego ta taśma)

**Sekcja 3, Ustawienia maszyny**:
- Napięcie taśmy (PSI, z manometru)
- Prowadniki (szczelina mm, czy skalibrowane)
- Temperatura hali (wpływa na dryf napięcia w ciągu zmiany)

**Sekcja 4, Parametry cięcia**:
- Prędkość posuwu startowa (stopy/min)
- Schemat cięcia (A lub B)
- Grubość deski (naddatek podany)
- Szerokość, długość (naddatki podane)
- Strategia (ile desek z pnia zakładane)

**Sekcja 5, Parametry zastosowane rzeczywiście** (wypełniana na koniec zmiany):
- Zmiana prędkości (z czego na co, kiedy, dlaczego)
- Zmiana napięcia (jeżeli była)
- Wymiana taśmy w trakcie (jeżeli była, dlaczego)
- Obserwacje wad wewnętrznych wykrytych

**Sekcja 6, Podpis**:
- Imię i nazwisko operatora, data, godzina końca zmiany

**Retencja**: **2 lata papier** w biurze tartaku, **5 lat skan elektroniczny** na OneDrive EGIDA (folder zlecenia, dostęp brygadzista + kierownik). Po 2 latach papier do niszczarki, skan dalej.

**Użycie dokumentu**:
1. **Reklamacja klienta** (deska za miękka, za krótka, pęknięta po 6 miesiącach): brygadzista otwiera KDP, sprawdza czy operator dał dobre parametry. Jeżeli tak, wina jest po stronie surowca (dostawca Nadleśnictwo Strzałowo) albo suszenia. Jeżeli nie, wina operatora (rozmowa naprawcza, ewentualnie szkolenie).
2. **Audyt FSC/PEFC** (m3-w4-l3): audytor chce widzieć ślad jakościowy zlecenia, KDP-001 jest pierwszym dokumentem w łańcuchu.
3. **Szkolenie nowego operatora**: kierownik pokazuje dobre KDP („tak się wypełnia"), złe KDP („tak się nie wypełnia, brakuje uzasadnienia wyboru taśmy").
4. **Samoocena operatora**: po 6 miesiącach operator ma pliczek 100-150 własnych KDP, widzi wzorce swoich decyzji, uczy się z własnej pracy.

::: warning
**Wpis nieprawdziwy w KDP-001** jest traktowany jak wpis nieprawdziwy w dzienniku pracy. Wraca do **art. 52 § 1 pkt 1 Kodeksu pracy** (ciężkie naruszenie obowiązków), podstawa do rozwiązania stosunku pracy bez wypowiedzenia. EGIDA nie miała takiego zdarzenia, ale kierownik raz w miesiącu wyrywkowo konfrontuje KDP z rzeczywistością (pyta operatora o detale zlecenia, patrzy na wynik cięcia). Zasada działa po obu stronach: uczciwy zapis jest dowodem dla operatora, że pracował dobrze, zły zapis jest dowodem przeciwko.
:::

### 9. Błędy częste początkujących operatorów M3

Kompilacja z raportów brygadzistów EGIDA za 2024-2025, wady doboru parametrów u operatorów, którzy przeszli na M3 w pierwszym półroczu pracy samodzielnej:

**Błąd 1. Dobór taśmy z pamięci z poprzedniej zmiany**. „Wczoraj był dąb, wzięłam stellit 7/9. Dziś jest sosna, biorę ten sam stellit, bo leży na miejscu.". Skutek: stellit na sośnie zalepia się żywicą w 40 cięciach (zamiast 140 stopową), taśma idzie do ostrzenia po jednej zmianie, koszt 120 zł niepotrzebnie plus czas. **Prawidłowo**: każda zmiana jest nowym wyborem, nie automatycznym przenoszeniem. KDP-001 wymusza tę refleksję.

**Błąd 2. Maksymalizacja napięcia „dla bezpieczeństwa"**. „Ustawiam 2400 zawsze, bo rzaz jest najlepszy". Skutek: taśma żyje 110-140 cięć zamiast 140-180, koszty taśm w rocznym budżecie 25% wyższe, spoina pęka częściej w cięciu (przerwane cięcie, odbiór za 145-200 zł dodatkowo). **Prawidłowo**: napięcie dobrane do gatunku i typu taśmy, zakres optymalny 2200-2300 PSI dla większości zleceń.

**Błąd 3. Prędkość posuwu „od razu szybko"**. „Szybciej znaczy więcej zrobię, 40 st/min od startu". Skutek: pierwsza deska lekko falista (korekta na 32 po pierwszym pniu to strata 20 minut i 2 deski do C16 zamiast C24), zużycie taśmy szybsze o 15%, silnik grzeje się ponadnormatywnie. **Prawidłowo**: start rekomendacja Wood-Mizer DTR, korekta tylko po pierwszym cięciu i tylko w oparciu o obserwację.

**Błąd 4. Schemat B „na wszelki wypadek"**. „C24 jest ok, ale zrobię B, bo wyższe klasy to lepsze, klient się ucieszy". Skutek: praca 2 razy dłuższa, uzysk 10% gorszy, klient i tak płaci za C24 nie za C30 (bo nie zamawiał C30), ekonomia zmiany gorsza o 30%. **Prawidłowo**: dokładnie to co zamawia klient, nie więcej. Brygadzista może autoryzować schemat B tylko w ustalonych przypadkach.

**Błąd 5. Brak wpisu w KDP-001 „bo mało czasu"**. „Wypełnię wieczorem". Skutek: wieczorem operator pamięta o połowie, szczegóły taśmy i prowadników mylą się z poprzednią zmianą, KDP jest nieprecyzyjny. Audytor ISO wskaże to jako niezgodność. **Prawidłowo**: KDP wypełniany jest **przed pierwszym cięciem** (sekcje 1-4), sekcja 5 po zmianie.

**Błąd 6. Kopia rozwiązania kolegi bez zrozumienia**. „Damian ustawił 30 st/min wczoraj, biorę to samo". Skutek: Damian miał sosnę suchą 18% (gatunek i wilgotność inne), 30 st/min było za wolne dla świeżej sosny 32%, taśma ślizga się, efekt nieoptymalny. **Prawidłowo**: każde zlecenie ma swoje parametry, parametrem porównawczym jest KDP poprzednie **z zbliżonych warunków**, nie ostatnie wpisane.

### 10. Gdy decyzja parametryczna wymyka się operatorowi

Nie każde zlecenie jest w polu komfortu operatora M3. Są sytuacje, gdy operator powinien **zapytać brygadzistę** przed decyzją. Trzy scenariusze:

**Scenariusz A, gatunek nieznany**. Zlecenie na „drewno egzotyczne" (jatoba, meranti, iroko), które operator widzi pierwszy raz. Charakterystyka cięcia, opór, żywice, wilgotność końcowa są nieznane z doświadczenia. **Procedura**: operator pyta brygadzistę, który konsultuje z serwisem Wood-Mizer (infolinia Polska, czas reakcji 15-30 minut), uzyskuje rekomendację taśmy i napięcia, decyzja do KDP wpisana z adnotacją „na podstawie konsultacji WM Polska, 2026-05-... godz ...".

**Scenariusz B, średnica pnia poza zakresem LT70**. LT70 ma maksymalną średnicę cięcia **67 cm**, minimalną **10 cm**. Pień Ø 72 cm (rzadko, ale zdarzało się, że nadleśnictwo wyróżnia duży sosnowy) jest poza zakresem, operator odsyła do innego stanowiska (Serra SM40 ma max 80 cm) albo pień idzie do dystanczowania (cięcie ręczne piłą łańcuchową na mniejsze kawałki przed LT70). Nie próbuje „na sztukę" zmieścić, bo grozi to uszkodzeniem maszyny, zerwaniem taśmy, a nawet kontuzją.

**Scenariusz C, wilgotność pnia skrajna**. Pień „suchy jak kość" (poniżej 15%, rzadko w magazynie EGIDA, ale raz zdarzyła się zapomniana półka z 2024) albo „po powodzi" (45%+, napuchnięty, waży 2 razy więcej niż powinien). Normalne parametry cięcia są nieskalibrowane, rekomendacja Wood-Mizer DTR nie obejmuje. **Procedura**: operator pyta, brygadzista decyduje, dokumenty wpisane.

**Reguła EGIDA**: w przypadkach niestandardowych operator samodzielny **zawsze może zadzwonić do brygadzisty przed startem**. Brygadzista nie jest rozdrażniony pytaniami, wręcz preferuje je nad wypadki i reklamacje. W KDP-001 jest pole „Konsultacja brygadzisty (tak/nie, data, godzina, osoba)", więc jawnie zapisujemy, że operator pytał.

### 11. Dzień pierwszy na P3 po serwisie, obserwacje pokażywcze

Zwróć uwagę, że dziś jest **pierwszy dzień P3 po serwisie Pana Krzysztofa z czwartku**. Cylinder podnoszenia głowicy wymieniona uszczelka, dolane 400 ml oleju hydraulicznego, wszystko przetestowane pod nadzorem. Rustam ma dwa powody dodatkowej czujności:

**Powód 1. Manometr**. Manometr napięcia taśmy jest związany z cylindrem naprężacza, nie podnoszenia. Ale oba cylindry w tym samym systemie hydraulicznym (wspólny zbiornik oleju Shell TTF-SB, wspólna pompa). Jeżeli system hydrauliczny po serwisie ma minimalne inne ciśnienie robocze niż przed, manometr naprężacza może pokazywać trochę inne wartości. Rustam **sprawdza kalibrację manometru** przez obracanie pokrętłem naprężacza od LUZ do pełnego zakresu, obserwując narastanie od 0 do 2200 PSI płynnie, bez skoków. **OK**, manometr płynny, kalibracja pozornie trzymana.

**Powód 2. Wyciek**. Wczoraj (piątek) Damian pracował na P3 po serwisie, bez incydentu. W sobotę maszyna była zimna, kondensat mógł się pojawić (zmiana temperatury dnia i nocy). Rustam **przed startem sprawdza podłogę pod cylindrem podnoszenia**: żadnej plamki, żadnej wilgotności, sucho. **OK**, serwis trzyma.

Wpis w KDP-001, sekcja „Ustawienia maszyny", adnotacja:
```
P3 pierwszy dzień po serwisie WM Polska z 21.05 (Pan Krzysztof).
Manometr naprężacza kalibrację zachował, rozruch 0-2200 PSI płynny.
Pod cylindrem podnoszenia sucho, bez wycieku od soboty.
Start zlecenia ZLE-077, 7:40.
```

To nie wymóg formalny, to **dobry nawyk operatora samodzielnego**. W razie wykrycia usterki w ciągu zmiany Rustam będzie miał ślad „po starcie było OK" jako punkt odniesienia.

## Scena domykająca, 14:30, pierwsze trzy pnie zakończone

Poniedziałek 2026-05-26, godzina 14:30. Rustam i Wahan mają za sobą **trzy pnie z czterech**: P1, P2, P3. Pień P4 w kolejce do cięcia, rozpoczęcie 14:35, szacowany koniec 15:10, czyli 10 minut po formalnej godzinie końca zmiany (15:00). Brygadzista (Marek) widzi to i nie ma problemu, zapłaci 10 minut nadgodziny wg stawki standard.

### Bilans trzech pni

**Pień 1**: zdjęto 4 obliny (3 min 40 s), zdjęto 8 desek 28 × 155 mm (4 min 30 s), plus 1 listwa resztkowa 18 × 155 mm (do opału). Total 8 desek, **0,1412 m³** tarcicy surowej. Pierwsza i ostatnia deska z cantu zawierały część obliny (sęk żywiczny na 80 cm, Rustam oznaczył dla klasyfikatora). Uzysk pnia P1: **57%**.

**Pień 2**: Pień najlepszy (bez wad). Obliny 3 min 50 s, 9 desek 28 × 155 mm (5 min), resztka 12 × 155 mm (do opału). **9 desek, 0,158 m³**. Uzysk: **64%**. Najlepszy.

**Pień 3**: Pień z pęknięciem promieniowym 8 cm na odziomku. Rustam orientował pęknięcie **w dół** w pierwszym ustawieniu (nie do góry, bo wtedy byłoby w oblinie, marnotrawstwo). Po zdjęciu czwartej obliny pęknięcie ujawniło się w cancie jako 8 cm długi ślad w górnym rogu. Rustam tnie 8 desek, z których **7** jest czystych, 8. zawiera pęknięcie (zostaje zaklasyfikowana jako C16 zamiast C24, spadek jakości, ale akceptowalne dla sortymentu podłogowego). Total 8 desek, **0,141 m³**. Uzysk: **56%**.

**Suma po trzech pniach**: 25 desek **dobrej jakości** (sortyment docelowy), 0,441 m³ tarcicy surowej. Plus 1 deska C16 z pęknięciem z P3 (może idzie do listwy boazeryjnej zamiast podłogi).

### Obserwacje parametrów

Prędkość posuwu:
- Pień 1, start 32 st/min, bez korekty, OK (rzaz prosty).
- Pień 2, start 32, po pierwszych 2 m głowicy delikatne łuskowanie na powierzchni, Rustam zmniejsza na 30 st/min, reszta cięć OK. Decyzja na bazie obserwacji powierzchni.
- Pień 3, start 30 (pamięć z P2, sosna świeża zachowuje się podobnie), całość 30, OK. Lekka obniżka klasy P3 deski 8. to wada surowca, nie parametru.

Napięcie taśmy:
- 2200 PSI przez całe trzy pnie, bez korekty. Manometr drgał w zakresie 2180-2220 (dopuszczalne odchylenie), nie było konieczności dolewania.

Prowadniki:
- Skalibrowane rano 3,5 mm, na koniec P2 Rustam sprawdził szybki test szczelinomierzem, szczelina trzyma (3,5-3,6 mm, dryf minimalny).

Taśma:
- Stopowa 38/7/8 ST-38-7/8-A12, licznik po 3 pniach = **~90 cięć** (obliny + deski + obroty pojedynczego pnia ~30 cięć, 3 pnie = 90). Taśma jeszcze świeża, na dzisiejszą zmianę wystarczy, wymiana najwcześniej po 140-180 cięciach, czyli za 2 pnie więcej niż dziś (jutro wtorek pień 4 plus kolejne 4 jeśli będzie zlecenie kontynuowane).

### Wpis w KDP-001, sekcja 5 (parametry rzeczywiste)

Rustam dopisuje w sekcji 5 karty:

```
Parametry rzeczywiste zastosowane:
Pień 1: 32 st/min, bez korekty, 8 desek C24, 0 wady.
Pień 2: 32→30 st/min (po 2 m cięcia, łuskowanie), 9 desek C24, 0 wady.
Pień 3: 30 st/min, 7 desek C24 + 1 deska C16 (pęknięcie surowca),
        oznaczenie dla klasyfikatora.
Napięcie: 2200 PSI stabilne, bez korekty.
Taśma: 38/7/8 stopowa, po 3 pniach licznik ~90 cięć, stan dobry.
Strategia kolejności pni: P2 (najlepszy) na drugi,
        żeby parametry ustabilizować przed P3 (z pęknięciem).
```

### Refleksja Rustama

Rustam rozmawia z Wahanem przy kawie w przerwie 14:35 przed rozpoczęciem P4:

*„Wahan, zauważyłeś, że na P2 zmieniłem prędkość po 2 metrach? Pierwsze 2 metry szły dobrze, potem zacząłem widzieć małe piki na powierzchni cięcia, co 10 cm. Znasz to? To znaczy prędkość za duża, taśma nie nadąża gryźć. Zwolniłem, małe piki zniknęły. Szybsza korekta, tańsza niż zepsuta deska."*

Wahan potakuje. W kalendarzyku ma notatkę: „*32 start sosna → jeśli piki, zwolnić do 30. Tylko jak same piki, nie fala, bo fala to taśma albo napięcie.*"

*„Jak myślisz, dlaczego zacząłem od P1, nie od P2?"*

Wahan myśli chwilę: *„Bo... P1 był pierwszy w magazynie?"*

*„Nie. Bo P1 ma sęk żywiczny, a ja chciałem pierwsze cięcie ze sękiem, żeby sprawdzić jak parametry działają na trudniejszym wariancie. Jak działają na trudnym, będą działać na łatwym. Odwrotnie nie. **Od trudnego do łatwego w pierwszym cięciu zmiany**, potem do łatwego na koniec. To się zapamiętuje."*

Wahan zapisuje: „*Pierwszy pień = najtrudniejszy albo typowy. Nie ten najłatwiejszy, bo parametry złudzą.*"

*„I jeszcze jedno. W KDP-001 zobaczysz, że w sekcji 5 wpisałem, dlaczego zmieniłem prędkość na P2. Nie tylko 'zmieniłem', ale 'zmieniłem bo łuskowanie'. Jak ktoś przyjdzie za rok albo dwa i popatrzy, zobaczy nie tylko co, ale i dlaczego. **Parametr bez uzasadnienia to magia. Parametr z uzasadnieniem to wiedza.**"*

### 15:10, pień 4 zakończony, zmiana zamknięta

Pień 4 (najsmuklejszy, bez wad): 4 obliny 3 min 30 s, 8 desek 28 × 155 mm, resztka 6 × 155 mm do opału. **8 desek, 0,141 m³**. Uzysk: **61%**.

**Suma czterech pni**: 33 deski sortyment docelowy (32 C24 + 1 C16 pęknięta), **0,582 m³** tarcicy surowej. Zlecenie wymagało 0,55 m³, więc **nadwyżka 5%**, dobra dla buforu suszenia (z tego 0,58 m³ po suszeniu i obróbce zostanie ~0,49 m³, zamówienie klienta 0,48 m³, nadwyżka 2%). **Zlecenie zrealizowane zgodnie z oczekiwaniami**.

Rustam zdejmuje taśmę (będzie na jutro, w magazynie pod folią), sprząta stanowisko z Wahanem (10 minut), wypełnia KDP-001 końcowo (sekcja 5 plus podpis plus godzina 15:18), składa kartę w kopercie, kładzie na biurku brygadzisty.

Marek przyjdzie wieczorem, przeczyta, wpisze swoje uwagi do akt osobowych Rustama (jeżeli są), KDP pójdzie do skanowania jutro rano do OneDrive.

## Kluczowe terminy

**Dobór parametrów cięcia** (*dobór parametrów cięcia*, EN *cutting parameter selection*, ES *selección de parámetros de corte*, UK *підбір параметрів різання*): proces decyzyjny operatora samodzielnego przed rozpoczęciem zlecenia, obejmujący wybór taśmy, napięcia, prowadników, prędkości posuwu i schematu cięcia na podstawie surowca i sortymentu docelowego.

**Karta KDP-001** (*karta doboru parametrów*, EN *cutting parameter selection card*, ES *ficha de selección de parámetros de corte*, UK *картка підбору параметрів різання*): formularz EGIDA A4 wypełniany przez operatora przed pierwszym cięciem zlecenia, dokumentuje wszystkie parametry decyzyjne plus parametry rzeczywiście zastosowane po zmianie.

**Prędkość posuwu** (*prędkość posuwu*, EN *feed rate*, ES *velocidad de avance*, UK *швидкість подачі*): prędkość, z jaką głowica pilarki przesuwa się po szynie podczas cięcia, mierzona w stopach na minutę (Wood-Mizer DTR) lub metrach na minutę, zakres LT70 0-80 stóp/min.

**Napięcie taśmy** (*napięcie taśmy*, EN *blade tension*, ES *tensión de la cinta*, UK *натяг стрічки*): siła, z jaką koła pilarki rozciągają taśmę w pionie, mierzona w PSI (funty/cal²), zakres bezpieczny LT70 2200-2400 PSI.

**Prowadniki taśmy** (*prowadniki taśmy*, EN *blade guides*, ES *guías de la cinta*, UK *напрямні стрічки*): cztery rolki (dolne i górne, lewa i prawa) utrzymujące taśmę w pionie podczas cięcia, regulowane szczelinomierzem w zakresie 3-4 mm.

**Schemat cięcia A cant sawing** (*schemat cięcia do kwadratu*, EN *cant sawing pattern*, ES *corte por pieza cuadrada*, UK *схема різання до квадрата*): obrót pnia 4 razy, zdjęcie 4 oblin do kwadratowego blatu, cięcie równoległe desek z blatu. Szybki, uniwersalny, dobry uzysk.

**Schemat cięcia B quarter sawing** (*schemat czwartowania*, EN *quarter sawing pattern*, ES *corte por cuarterones*, UK *схема четвертного різання*): rozcięcie pnia przez rdzeń na połowy, każdej na ćwiartki, cięcie desek z ćwiartek. Wolniejszy, lepsza klasa wytrzymałościowa (C30+) i stabilność.

**Podziałka zębów TPI** (*podziałka zębów*, EN *tooth pitch TPI teeth per inch*, ES *paso de los dientes TPI*, UK *крок зубів TPI*): liczba zębów taśmy na cal, typowo 7/8 TPI dla sosny, 7/9 TPI dla dębu, 10 TPI dla cienkich desek, 22 TPI dla mrożonych lub dużych średnic.

**Kąt natarcia** (*kąt natarcia*, EN *hook angle*, ES *ángulo de ataque*, UK *передній кут*): kąt, pod jakim ząb taśmy „wprowadza się" w drewno, typowo 9° dla twardego drewna, 10° dla standardu, 13° dla mrożonego.

**Stellite vs stopowa** (*stal stellitowa vs stopowa*, EN *stellite vs alloy steel*, ES *acero estelita vs aleación*, UK *стелітова сталь vs сплавна*): dwa typy ostrzenia taśmy, stellite trzyma ostrość 3-5× dłużej, ale kosztuje 2,5× więcej i nie znosi żywic sosnowych.

**Dyspozycja produkcyjna** (*dyspozycja produkcyjna*, EN *production work order*, ES *orden de producción*, UK *виробничий наряд*): dokument A5 wystawiany przez brygadzistę, zawierający surowiec, sortyment docelowy, ilość i termin realizacji, bez parametrów cięcia (te wybiera operator).

**Naddatek** (*naddatek*, EN *allowance / oversize*, ES *sobredimensión / margen*, UK *припуск*): różnica między wymiarem cięcia surowym a docelowym po suszeniu i obróbce, typowo 3 mm grubości, 5 mm szerokości, 50 mm długości dla desek podłogowych 25×150×4000.

**Uzysk** (*uzysk / wydajność surowca*, EN *yield / lumber recovery*, ES *rendimiento / aprovechamiento*, UK *вихід / коефіцієнт виходу*): stosunek objętości tarcicy surowej do objętości dłużycy, dla sosny zwyczajnej deski 28 mm typowo 55-65%.

**Operator samodzielny M3** (*operator samodzielny*, EN *independent operator*, ES *operador independiente*, UK *самостійний оператор*): operator po ukończeniu modułu 3 kursu EGIDA, podejmuje decyzje parametryczne na zleceniu bez bezpośredniego nadzoru brygadzisty.

**Cant** (*blat prostokątny*, EN *cant*, ES *pieza cuadrada*, UK *брус / чотиригранний блок*): prostokątny lub kwadratowy blat drewna powstały po zdjęciu 4 oblin w schemacie A, z którego tnie się równolegle deski.

## Sprawdź siebie

### A. Parametry operatora (pytania rozpoznawcze)

1. Wymień **pięć parametrów decyzyjnych operatora** na pilarce taśmowej LT70, które nie są podane w dyspozycji produkcyjnej.

2. Operator M1 (pomocnik) widzi taśmę stellite 7/9 na pilarce. Czy jest to parametr operatora M3 (samodzielnego), czy parametr wymuszony konstrukcyjnie? Uzasadnij odpowiedź.

3. Co oznacza skrót **KDP-001** w dokumentacji EGIDA? Jaki jest cel wypełnienia tej karty przed cięciem?

### B. Dobór taśmy

4. Zlecenie: buk świeży 30% wilgotności, deski 30 mm grubość, klasa C24. Dobierz taśmę z opcji: a) stopowa 7/8 kąt 10°, b) stellite 9 kąt 9°, c) stellite 7/9 kąt 9°, d) stopowa 22 kąt 13°. Uzasadnij wybór 2 zdaniami.

5. Dlaczego stellite **nie** jest dobrą taśmą dla sosny świeżej, pomimo że trzyma ostrość dłużej niż stopowa? Podaj przyczynę fizyczną.

6. Po zmianie widzisz, że taśma, której użyłeś na sośnie suchej 18% wilgotności, ma po 80 cięciach powierzchnię zębów zapchaną brązowymi osadami. Co to za osady i czy są problemem?

### C. Napięcie i prędkość

7. Napięcie taśmy ustawiasz na 2400 PSI dla sosny świeżej z przyzwyczajenia. Jakie trzy skutki tego widzisz w ciągu 2-3 zmian pracy?

8. Prędkość posuwu w trakcie cięcia pierwszego pnia zacząłeś na 32 stopy/min. Po 2 metrach widzisz drobne „łuskowanie" na powierzchni cięcia. Co robisz:
   a) zwiększasz prędkość o 5 st/min
   b) zmniejszasz prędkość o 5 st/min
   c) zmniejszasz napięcie
   d) wymieniasz taśmę
   
9. Na panelu LT70 widzisz, że prędkość posuwu jest ustawiona na 45 stóp/min. Cięcie trwa, słyszysz silnik pracujący „falująco" (dźwięk zmienia tonację co 2-3 sekundy). Co to znaczy i co robisz?

10. W tabeli DTR Wood-Mizer dla sosny świeżej i deski 28 mm rekomendacja to 30-35 stóp/min. Dlaczego rekomendacja jest **zakresem**, nie pojedynczą wartością?

### D. Schemat cięcia

11. Zlecenie wymaga klasy C24. Operator planuje schemat B (quarter sawing) „dla pewności klasy". Brygadzista odwołuje to i ustala schemat A. Dlaczego brygadzista ma rację?

12. Zlecenie wymaga klasy **C30** na elementy konstrukcyjne (krokwie dachowe). Surowiec: sosna zwyczajna 30% wilgotności. Który schemat wybierasz i dlaczego?

13. Pień Ø 22 cm (smuklejszy niż typowy). Operator chce użyć schematu B. Dlaczego to zły wybór pod względem ekonomii zlecenia?

### E. KDP-001 i dokumentacja

14. W KDP-001 sekcja 5 „Parametry rzeczywiste zastosowane" wypełniasz po zmianie wieczorem. Jaką informację operator **musi** tam wpisać, jeżeli zmienił prędkość posuwu w trakcie zmiany?

15. Brygadzista znajduje w KDP-001 operatora dwa wpisy identyczne (prędkość 32, napięcie 2200, schemat A) na zleceniach, z których jedno to sosna świeża 32% a drugie dąb świeży 35%. Co myśli brygadzista i dlaczego?

16. Podczas audytu ISO 9001 audytor pyta o KDP-001 sprzed 6 miesięcy. Gdzie szuka: a) biurko operatora, b) szafa brygadzisty w biurze, c) OneDrive EGIDA skan, d) nie ma, po 6 miesiącach wyrzucane? Wybierz i uzasadnij.

### F. Scenariusze decyzyjne

17. Scenariusz A z lekcji: gatunek nieznany (jatoba). Jak postępujesz jako operator M3 samodzielny? Trzy kroki.

18. Scenariusz B z lekcji: średnica pnia 72 cm, poza zakresem LT70 (max 67 cm). Jakie masz trzy opcje, i którą wybierasz i dlaczego?
