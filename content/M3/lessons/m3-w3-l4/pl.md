---
id: m3-w3-l4
blok: procesy
czas: 120
---

## Wprowadzenie

Piątek, 2026-05-30, godzina 9:25. Jedenaście dni po naradzie planistycznej z l3, jedenaście dni w cyklu dębu szypułkowego w komorze BH-50. Mykoła idzie przez plac magazynowy w kierunku hali suszarni, w ręku notatnik, w kieszeni kombinezonu telefon służbowy (Nokia starego typu, bateria trzyma tydzień, zasięg w całym tartaku). Marek zaplanował mu dziś od 9:30 do 11:30 **szkoleniową obecność w suszarni** jako część bloku procesowego M3. Wasyl dziś nie jest z Mykołą, ma zmianę konserwacyjną na P1 z Jurim (młodszym mechanikiem UR).

Mykoła wchodzi do hali suszarni (12 × 8 × 4,5 m, ta sama hala co w l3), potem do **hali sterowania** (pomieszczenie 2 × 3 m z szafą sterowniczą, oknami obserwacyjnymi na komorę i małym biurkiem w kącie). Pan Henryk jest już tam, pije kawę z termosu, Maciek Wiśniewski (pomocnik suszarni, 19 lat, technikum drzewne Ostróda, z l3) stoi przed panelem z **dziennikiem weekendowym** w ręku. Dziennik to zeszyt A4 w twardej oprawie, wypełniany dwa razy dziennie w weekendy (sobota 10:00 i 16:00, niedziela 10:00 i 16:00), czasem częściej jeśli Maciek ma ochotę sprawdzić komorę w sobotę wieczorem.

### 9:30, odczyt rutynowy

Pan Henryk, do Mykoły: *„Dzień dobry. Usiądź, patrz, pisz. Dzisiaj pokażę ci, jak się czyta panel podczas cyklu. Dębu bieżącego czwartek otrzymaliśmy dzień czternasty, jutro dzień piętnasty, w niedzielę dzień szesnasty. Faza główna kończy się w niedzielę, poniedziałek przechodzimy w kondycjonowanie."*

Mykoła siada na krzesełku przy biurku, otwiera notatnik, zapisuje datę i godzinę. Panel BH-50 pokazuje:

```
Komora: BH-50 (Brunner-Hildebrand)
Program: DUB-STAND-28 (dąb szypułkowy 28 mm, 22 dni do 14%)
Wsadka: dąb 2,5 m³, deski 30 mm, start 2026-05-17
Dzień cyklu: 14 z 22
Aktualna faza: suszenie główne, dzień 12 z 14 (kończy się 2026-06-01)

Temperatura powietrza:        58°C  (cel 60°C, tolerancja ±3)
Wilgotność względna (RH):     47%   (cel 45%, tolerancja ±5)
Wilgotność drewna próba 1:    24,8% (start 38%, dzisiaj wczoraj 25,3%)
Wilgotność drewna próba 2:    24,1% (start 37,6%, wczoraj 24,6%)
Wilgotność drewna próba 3:    25,7% (start 38,5%, wczoraj 26,2%, wolniej schnie)
EMC (wilgotność równowagowa): 8,4%
Rozrzut sond wilgotności:     1,6% (OK, poniżej progu 3%)
Stan wentylatorów:            1450 RPM, prąd 6,2 A  (nominalne 1500/6,5)
Stan grzałek:                 45% mocy (nominalne 40-60% w fazie głównej)
```

Pan Henryk wskazuje paznokciem na trzy linijki: *„Patrz. Wilgotność drewna spada każdego dnia o 0,5-0,6%. To jest dobra dynamika dla dębu dzień czternasty. Do czternastego, cel 14%, zostało nam 10-11% do zrzucenia w ośmiu dniach. To jest **1,25% dziennie**. Wzrost tempa w kondycjonowaniu, potem spowolnienie w końcówce. Plan trzyma."*

Mykoła zapisuje: *„dąb d.14, wilg. 24-26%, EMC 8,4%, rozrzut 1,6% OK, wentylatory ok."*

Pan Henryk: *„**Rozrzut** to najważniejszy wskaźnik jednorodności w trakcie cyklu. Jeżeli sonda trzecia idzie wolniej o 1-2%, to znaczy, że tam gdzie jest zamocowana (tylna część komory), przepływ powietrza jest trochę słabszy. Normalne. Jak różnica rośnie do 3-4%, robi się problem. Dziś 1,6%, spokojnie."*

### 9:40, Pan Henryk pokazuje alarmy historyczne

Pan Henryk klika na panelu zakładkę „Historia alarmów". Na ekranie lista ostatnich 30 dni:

```
2026-05-19 03:47  INFO       Przepływ powietrza RPM 1400 (cel 1500, marża)
2026-05-22 16:23  OSTRZEŻENIE Wentylator 2 prąd 7,1 A (cel 6,5, +10%)  → auto-korekta
2026-05-27 08:15  INFO       Start programu, dzień 1 nagrzewania
[pozostałe pozycje z poprzednich cykli suszarniczych]
```

*„Widzisz, Mykoła, **INFO** to notowanie, nie alarm, nie wymaga reakcji. **OSTRZEŻENIE** to poziom drugi, sterownik sam koryguje, operator obserwuje. **ALARM** to poziom trzeci, sterownik nie koryguje, wymaga reakcji człowieka. Alarmów w ostatnim miesiącu nie było, to jest dobry znak."*

Maciek wraca do hali pilarek z własnym zadaniem (załadunek tartaku dla klienta popołudniowego), drzwi do hali sterowania zamyka za sobą.

### 9:45, alarm wyskakuje

Pan Henryk dolewa kawy z termosu, Mykoła patrzy na panel, nagle **dioda czerwona** na rogu ekranu zaczyna pulsować. Sterownik wydaje krótki sygnał dźwiękowy (trzy piknięcia, 1 sekunda, potem przerwa 2 sekundy, potem znów). Na ekranie komunikat:

```
ALARM: Temperatura powietrza przekroczona
Wartość aktualna: 62,3°C
Cel programu:      58,0°C
Odchylenie:        +4,3°C (próg alarmu +4)
Wykryto:           2026-05-30, 09:43:12
Rekomendacja:      Zmniejsz moc grzałek lub zwiększ wentylację
```

Mykoła drgnął, kawa w kubku Pana Henryka lekko zachybotała. Pan Henryk mówi spokojnie, ale precyzyjnie: *„Mykoła, widzisz czerwoną diodę. Co robisz teraz?"*

Mykoła myśli dwie sekundy. Lekcja z l3: operator M3 w przypadku alarmu **sygnalizuje mistrzowi natychmiast, nie próbuje rozwiązywać samodzielnie**. Pan Henryk jest obok, nie trzeba dzwonić, wystarczy się odwrócić. Mykoła mówi: *„Alarm temperaturowy, 62,3 zamiast 58, odchylenie +4,3. Zgłaszam panu, co mam robić?"*

Pan Henryk potakuje: *„Dobrze. Pierwsza rzecz, **nie resetujesz alarmu**, bo nie wiemy jeszcze, co jest przyczyną. Druga, **nie wchodzisz do komory**. Trzecia, **nie zmieniasz ustawień programu**. Ja teraz diagnozuję, ty obserwujesz i uczysz się. **Niewielki alarm** to dobry trening, bo nie ma pośpiechu."*

Pan Henryk otwiera zakładkę „Sensorów aktualne":

```
Czujnik T1 (roginik A, przód-lewo):  62,1°C
Czujnik T2 (roginik B, przód-prawo): 62,5°C
Czujnik T3 (roginik C, tył-lewo):    61,8°C
Czujnik T4 (roginik D, tył-prawo):   62,8°C
Średnia:                              62,3°C
Rozrzut między sondami:              1,0°C  (nominalne <1,5°C)
```

*„Wszystkie cztery sondy temperatury pokazują podobnie, między 61,8 a 62,8. Rozrzut jest normalny. **To znaczy, że cała komora jest gorętsza**, nie jedna strefa. Jeżeli byłaby jedna sonda 62 a trzy inne 58, podejrzewałbym uszkodzony czujnik w jednym rogu. Tutaj cała komora. Diagnoza pierwsza: **nie jest to błąd sensora**."*

Mykoła zapisuje notatkę: *„4 sondy blisko siebie = cała komora gorąca, nie jeden czujnik. Pierwsza diagnoza."*

### 9:50, Pan Henryk sprawdza grzałki i zawór gazu

Pan Henryk otwiera zakładkę „Grzałki i media":

```
Grzałka 1 (wlot komory):    moc aktualna 68%  (cel 45%, powyżej o 23%)
Grzałka 2 (wylot komory):   moc aktualna 64%  (cel 45%, powyżej o 19%)
Zawór gazu główny:          otwarcie 72%      (cel 50%, powyżej o 22%)
Wymiennik ciepła temp. wlot: 78°C              (cel 65°C, powyżej o 13°C)
Regulacja proporcjonalna:   AUTO               (normalna praca)
```

*„A. **Grzałki grzeją za mocno**. Zawór gazu otwarty na 72% zamiast 50%. Wymiennik ciepła ma 78°C zamiast 65°C. To znaczy system **grzeje więcej gazu niż program zadaje**. Sterownik to zauważył, ale nie kompensuje, bo grzałki są w trybie AUTO proporcjonalnym i ktoś albo coś zwiększył sygnał referencyjny."*

Pan Henryk bierze telefon, wybiera numer do Marka (brygadzisty, na telefonie komórkowym Marek pracuje od 7:00):

*„Marek, Henryk z suszarni. Mam alarm temperaturowy w komorze dębu, plus cztery stopnie, grzałki otwarte na 68%, zawór gazu 72%. Podejrzewam **termostat wymiennika ciepła**, który każe systemowi grzać więcej niż trzeba. Wiesz, co słyszałem wczoraj od BTM, że planują nam wymianę tego termostatu w lipcu podczas przeglądu rocznego, ale to już teraz jest zbyt wcześnie. Możesz zadzwonić do BTM serwisu? Numer masz w folderze."*

Marek potwierdza, że zadzwoni. Pan Henryk odwiesza telefon.

### 9:55, pierwsza korekta ręczna

Pan Henryk do Mykoły: *„Teraz zrobię **ręczną korektę zaworu gazu**, żeby obniżyć temperaturę w komorze z 62 z powrotem na 58. To jest decyzja **mistrza suszarni**, nie operatora M3. Operator M3 nawet nie ma hasła dostępu do tego panelu, widzi tylko informacyjnie."*

Pan Henryk wpisuje hasło (6-cyfrowe, zmieniane co kwartał przez BTM), otwiera okno sterowania ręcznego:

```
Sterowanie ręczne grzałek:
Grzałka 1: aktualnie 68%, zmień na: 40% [potwierdź]
Grzałka 2: aktualnie 64%, zmień na: 40% [potwierdź]
Zawór gazu: aktualnie 72%, zmień na: 45% [potwierdź]

Uwaga: zmiana ręczna wyłączy tryb AUTO na 30 minut.
Po 30 minutach sterownik wraca do AUTO z nowymi wartościami.
Jeżeli chcesz, by tryb AUTO pozostał wyłączony dłużej, wprowadź
w „Opcje specjalne, blokada AUTO na N minut".
```

Pan Henryk obniża grzałkę 1 z 68% do 40%, grzałkę 2 z 64% do 40%, zawór gazu z 72% do 45%. Potwierdza trzy razy, sterownik wyłącza tryb AUTO na 30 minut (od 9:55 do 10:25).

*„Mykoła, **zasada maksymalnego tempa zmiany temperatury** to **6°C na godzinę**. Dębu nie wolno schładzać szybciej niż 6°C/h, bo powoduje to **pęknięcia rdzeniowe**. Skok z 62 na 58 to spadek 4°C, powinno się dokonać w 40 minutach, nie w 5. Sterownik będzie obniżał stopniowo. Obserwujemy."*

### 10:00, obserwacja trendu

Pan Henryk i Mykoła patrzą na panel, odświeżanie co 15 sekund. Temperatura w ciągu 5 minut spada z 62,3 na 61,1 (spadek 1,2°C za 5 minut, czyli **14,4°C/h**, za szybko). Pan Henryk komentuje: *„Za szybko, ale oczekiwane w pierwszych minutach po redukcji gazu. Gorący wymiennik ciepła oddaje ciepło do komory nawet gdy grzałki dostają mniej prądu. Poczekamy, w ciągu 20 minut spadek powinien się ustabilizować."*

Mykoła zapisuje obserwacje co 2 minuty:
- 09:55 62,3°C (start)
- 09:57 61,9°C (spadek 0,4)
- 10:00 61,1°C (spadek 0,8)
- 10:03 60,6°C (spadek 0,5)
- 10:05 60,2°C (spadek 0,4)
- 10:10 59,5°C (spadek 0,7 za 5 min)
- 10:15 58,8°C (spadek 0,7 za 5 min, stabilizacja)

*„10:15, temperatura 58,8, prawie na celu 58. Od 9:55 spadek 3,5°C w 20 minut, czyli **10,5°C/h średnio**. To jest powyżej limitu 6°C/h przez pierwsze 10 minut, potem się uspokoiło. Za szybki, ale nie katastrofalny dla dębu dzień czternasty (drewno już częściowo wysuszone, mniej wrażliwe niż na początku cyklu). Pozostawiamy tak jak jest, monitorujemy."*

### 10:20, telefon Marka z informacjami BTM

Telefon Pana Henryka wibruje. Marek: *„Henryk, dzwoniłem do BTM. Termostat wymiennika ciepła, model GH-67, znany problem u nich od 2024 roku, sprzężenie zwrotne pcha sygnał w kierunku grzania ponad wymaganie przy wilgotności otoczenia 65%+ (poza komorą, w hali suszarni). Dzisiaj hala ma 68% (mamy deszczowy ranek). To tłumaczy zachowanie. BTM przyjedzie w poniedziałek rano, wymieni termostat za darmo z gwarancji. Do poniedziałku **sterowanie ręczne**, korekty co 4-6 godzin, ja cię zmienię w sobotę rano na 2 godziny, żebyś nie siedział tutaj w weekend cały czas. Maciek weekendowy plan aktualny, tylko dodatkowo co 4 godziny obserwacja, nie co 8."*

Pan Henryk potwierdza, zapisuje w notatniku: *„Do pon 02.06 sterowanie ręczne, korekty co 4-6 h. BTM serwis pon rano."*

### 10:30, sterownik wraca do AUTO z nowymi wartościami

O 10:25 sterownik automatycznie wraca do trybu AUTO. Temperatura stabilizuje się na 58,2°C (blisko celu 58), grzałki schodzą do 43% (blisko celu 45%), zawór gazu 48% (blisko celu 50%). Rozrzut między sondami 0,8°C. Rozrzut sond wilgotności drewna 1,6% (niezmieniony). Alarm zniknął, czerwona dioda zgasła o 10:24.

Pan Henryk resetuje historię alarmów (zatwierdza w dzienniku komory), wpisuje w notatkę:
```
2026-05-30 09:43  ALARM Temp +4,3°C  → korekta ręczna 9:55
2026-05-30 10:15  ALARM rozwiązany, temp 58,2°C
```

*„Mykoła, **teraz karta KS-001**. Każdy alarm musi być udokumentowany, niezależnie od tego czy skutki były dla drewna, czy nie. To jest wymóg ISO 9001 i BTM dla gwarancji komory."*

### 10:40, wpis w KS-001

Pan Henryk bierze z szuflady biurka kartę suszarni wsadki bieżącej (KS-001 dla wsadki dębu ZLE-075 start 17.05, którą wypełnił przy starcie cyklu). Dopisuje w sekcji 3 (Notatki i obserwacje):

```
2026-05-30 09:43-10:24 ALARM temperaturowy +4,3°C
Przyczyna (wg BTM, telefon M.Kowalski): termostat GH-67
  wymiennika ciepła, sprzężenie zwrotne przy wysokiej
  wilgotności atmosferycznej.
Korekta: ręczne obniżenie zaworu gazu z 72% na 45%,
  grzałek z 68/64% na 40/40%. Temperatura wróciła na 58°C
  w 32 minuty (spadek średni 10°C/h, powyżej limitu 6°C/h
  przez 10 min, akceptowalne dla dębu dzień 14).
Stan drewna: wilgotność bez zmian, rozrzut sond 1,6%.
Plan: sterowanie ręczne do pon 02.06, serwis BTM.
Obecni: Pan Henryk (mistrz), Mykoła Hrycenko (M3 szkolenie).
Podpis: H. Nowak, 10:45.
```

*„Mykoła, **nie byłeś tu 9:55**. W dokumencie piszę 'obecni Mykoła Hrycenko', bo byłeś, i to jest fakt dla audytu. Jeśli ktoś cię zapyta kiedyś 'byłeś przy alarmie komory 30 maja', powiesz 'tak, uczyłem się', nie będziesz się wstydził."*

Mykoła zapisuje w notatniku: *„Alarm zdarzył się. Udokumentowaliśmy. Bez ukrywania. **Dokumenty są ochroną, nie problemem**."*

### 10:50, rozmowa o granicy kompetencji

Pan Henryk dolewa Mykole kawy z termosu (cukier z osobnej torebki), siedzą obok siebie przed panelem, temperatura stabilizuje się 58,2°C.

*„Mykoła, chciałbym, żebyś zrozumiał dzisiaj jedną rzecz. Alarm wyskoczył, ja go rozwiązałem, ale **gdyby mnie tu nie było**? Co ty jako operator M3 zrobiłbyś?"*

Mykoła myśli: *„Zgłosiłbym Markowi telefonem. Marek jest na hali pilarek, doszedłby tutaj za 2-3 minuty."*

*„Dobrze. A jeżeli Marek nie odbiera, bo jest pod prysznicem po zapyleniu odpychania trocin?"*

*„Zadzwoniłbym na numer serwisowy BTM. Który znajdę w folderze w szafie sterowania suszarni."*

*„Dobrze. A jeżeli BTM nie odbiera, bo jest weekend? Co robisz?"*

Mykoła myśli. *„W przeciwieństwie do pilarki, nie mogę wyłączyć komory sam, bo drewno wtedy się schłodzi za szybko albo rozgrzeje. Jeśli nie mogę wezwać mistrza ani BTM, to... **obserwuję i zapisuję**, do momentu aż jeden z nich się odzyska. Chyba że widzę dymu albo słyszę trzask."*

*„Dokładnie. **Ostatni ratunek** to nie wyłączenie komory przez operatora M3, bo każda próba ręcznej ingerencji bez uprawnień może pogorszyć sytuację. Ratunkiem jest **obserwacja, dokumentacja, eskalacja**. Tak jak w pilarce jest **STOP, zabezpiecz, zgłoś, udokumentuj**. Tutaj jest **OBSERWUJ, ZAPISUJ, ZGŁOŚ, ZGŁOŚ WYŻEJ**. Pierwsze trzy kroki są te same, czwarty inny, bo komory nie da się 'zabezpieczyć' w jednej minucie jak maszyny."*

Mykoła zapisuje w notatniku: *„Komora, procedura alarmu operator M3: **OBSERWUJ, ZAPISUJ, ZGŁOŚ, ZGŁOŚ WYŻEJ**. Nie wolno ingerować ręcznie."*

### 11:00, normalizacja komory i plan weekendowy

O 11:00 komora jest całkowicie ustabilizowana: temperatura 58,1°C, RH 46%, wilgotność drewna średnia 24,7%, EMC 8,5%. Pan Henryk przeprowadza odczyt, Mykoła zapisuje równolegle.

Pan Henryk: *„Do poniedziałku sterowanie ręczne. Ja dziś zostaję do 16:00. Maciek wrócił do pilarek, powiem mu po powrocie, że weekend będzie obserwował komorę **co 4 godziny** zamiast co 8. Sobota 8:00, 12:00, 16:00, 20:00. Niedziela podobnie. Jeśli cokolwiek się dzieje, dzwoni do mnie, nie do ciebie, nie do Marka."*

*„Ty jutro (sobota) masz wolne, prawda?"*

Mykoła: *„Tak, niedziela wolna też."*

*„Dobrze. Poniedziałek przyjdziesz normalnie na pilarkę, BTM wymieni termostat, może ci się przyda zobaczyć jak serwis się ludzi dokonuje ale to nie twoja rola. Wtorek 02.06 załadunek Drew-Sus, pamiętasz, sosna 2,42 m³, ty Wasyl i Anton z brygady placowej. Od wtorku wieczorem komora pusta do 08.06 kiedy zbieramy dąb."*

Mykoła potwierdza, zamyka notatnik. *„Dziękuję, Panie Henryku."*

*„Poradziłeś sobie. **Sygnalizacja zamiast ingerencji, obserwacja zamiast paniki**. To jest standardy mistrza, które ty jako operator M3 już wiesz i stosujesz. Za pół roku, jeśli zrobisz szkolenie suszarnicze pomocnicze, będziesz mógł rozwiązywać takie alarmy sam. Dziś się uczyłeś patrząc."*

## Cele

Po tej lekcji:

1. Znasz **trzy poziomy sygnałów sterownika BH-50**: 1) **INFO** (notowanie w historii, bez reakcji wymaganej, np. krótkotrwałe odchylenie RPM wentylatora); 2) **OSTRZEŻENIE** (sterownik sam koryguje, operator obserwuje, np. prąd wentylatora powyżej 10% nominalnej); 3) **ALARM** (sterownik nie koryguje, wymaga reakcji człowieka, np. odchylenie temperatury +4°C lub więcej). Rozumiesz, że ALARM uruchamia czerwoną diodę na panelu i sygnał dźwiękowy (trzy piknięcia z przerwami 2 s), i że **operator M3 w przypadku ALARMU natychmiast sygnalizuje mistrzowi suszarni**, nie próbuje rozwiązywać samodzielnie.
2. Znasz **czterokrokową procedurę operatora M3 przy alarmie komory**: **OBSERWUJ** (odczyt wskazań wszystkich sensorów, bez dotykania panelu), **ZAPISUJ** (data, godzina, wartości aktualne vs cel, typ alarmu), **ZGŁOŚ** (telefon lub osobisty kontakt z mistrzem suszarni), **ZGŁOŚ WYŻEJ** (jeśli mistrz nieosiągalny, brygadzista, potem serwis BTM). Rozumiesz, że to procedura **różna od pilarki** (gdzie jest STOP-zabezpiecz-zgłoś-udokumentuj), bo komory nie da się „zabezpieczyć" w minutę, szybkie wyłączenie generuje szok termiczny dla drewna i kosztuje więcej niż spokojna obserwacja.
3. Rozumiesz **typowe alarmy komory** (temperaturowy, przepływu powietrza, wilgotności, sensor, stan gazu) i ich różne priorytety. Alarm temperaturowy +4°C w fazie głównej cyklu dębu dzień 14 to **drobny alarm** (drewno częściowo wysuszone, mniej wrażliwe), alarm temperaturowy +6°C na dzień 3 nagrzewania to **poważny alarm** (drewno na początku, wrażliwe na szok). Rozumiesz, że operator M3 nie klasyfikuje priorytetu alarmu (to robi mistrz), tylko zgłasza wszystkie alarmy na równi.
4. Znasz **zasadę maksymalnego tempa zmiany temperatury 6°C/h** w komorach suszarniczych dla gatunków twardych (dąb, buk, jesion). Przekraczanie tej zasady przez okresy dłuższe niż 10-15 minut powoduje **pęknięcia rdzeniowe wewnętrzne** (internal checker) w deskach, niewidoczne z zewnątrz, ujawniające się po obróbce u klienta. Dla gatunków miękkich (sosna, świerk) zasada jest mniej rygorystyczna (dopuszczalne 8-10°C/h), ale mistrz EGIDA i tak trzyma 6°C/h dla wszystkich gatunków jako standard bezpieczeństwa.
5. Znasz **interpretację rozrzutu sond** na panelu BH-50. Rozrzut temperaturowy między czterema czujnikami rogów komory: **<1,5°C** (OK, jednorodność normalna), **1,5-2,5°C** (obserwacja, może oznaczać nierównomierny przepływ), **>2,5°C** (problem z przepływem, mistrz diagnozuje). Rozrzut sond wilgotności drewna: **<2%** (OK, wsadka jednorodna), **2-3%** (obserwacja, pewne deski schną wolniej), **>3%** (problem, wsadka była niejednorodna lub sonda uszkodzona). Rozumiesz, że **jedna sonda odstająca** sygnalizuje problem czujnika, **wszystkie sondy odstające równolegle** sygnalizuje problem całej komory.
6. Rozumiesz **granicę kompetencji operatora M3 w sterowaniu komorą**. Operator M3: **nie ma hasła dostępu** do trybu ręcznego sterowania grzałek, zaworów, programów. Operator M3 **nie resetuje alarmu** samodzielnie, nawet gdy wydaje się, że alarm był fałszywy. Operator M3 **nie otwiera drzwi komory** w trakcie cyklu (szok termiczny dla drewna, utrata godziny cyklu). Operator M3 **nie zmienia tempa zadań programu** (temperatura cel, RH cel, grubość deski). Mistrz suszarni (Pan Henryk): ma hasło, wpisuje korekty ręczne, wyłącza tryb AUTO na 30 minut lub dłużej, dokumentuje w KS-001.
7. Znasz **sposób dokumentacji alarmu w karcie KS-001** sekcja 3 (Notatki i obserwacje). Wymagane pola: **data i godzina początku alarmu**, **wartość zmierzona vs cel** (np. „62,3°C vs 58°C, odchylenie +4,3"), **prawdopodobna przyczyna** (np. „termostat GH-67 sprzężenie zwrotne, potwierdzone BTM telefonicznie"), **podjęte działania** (np. „ręczna korekta zaworu gazu z 72% na 45%"), **rezultat** (np. „temperatura wróciła na 58°C w 32 minuty, spadek średni 10°C/h"), **stan drewna po alarmie** (np. „wilgotność bez zmian, rozrzut sond 1,6%"), **plan do normalizacji** (np. „sterowanie ręczne do pon 02.06, serwis BTM"), **osoby obecne** (mistrz, operator M3 w trakcie szkolenia), **podpis i godzina wypisania**.
8. Znasz **rolę Maćka Wiśniewskiego** (pomocnika suszarni M1) w monitoringu komory. Maciek **codziennie** odczytuje panel i wpisuje w dzienniku (co najmniej 2 razy dziennie w dni robocze plus 4 razy w weekendy standardowo, 6-8 razy w weekendy po alarmie). Maciek **sygnalizuje Panu Henrykowi** przy każdym odchyleniu wychodzącym poza rutynę. Maciek **nie ma hasła** do sterowania ręcznego, tak jak operator M3. Rozumiesz, że **Maciek i operator M3 mają podobny zakres kompetencji** w stosunku do komory (obserwują, zapisują, sygnalizują, nie ingerują), ale Maciek ma większą wprawę wzrokową (widzi komorę co dzień, operator M3 raz w tygodniu).

## Treść

### 1. Jak operator M3 czyta panel sterowania BH-50

Panel sterowania komory BH-50 jest **dostępny wzrokowo dla każdego pracownika** hali suszarni, w tym operatora M3 obecnego tutaj sporadycznie (np. podczas narady planistycznej z l3 lub szkoleniowej obecności). Widoczne są: temperatura, wilgotność powietrza, wilgotność drewna w trzech sondach, EMC, stan wentylatorów, stan grzałek, numer programu, dzień cyklu, faza cyklu, historia alarmów.

**Nie widoczne bez hasła** (dostęp mistrza suszarni i serwisu BTM): sterowanie ręczne grzałek, ręczne otwarcie zaworu gazu, ręczne dostrojenie RH przez wstrzyknięcie pary, pełny log alarmów z ostatnich 2 lat, parametry kalibracji czujników.

**Operator M3 obserwuje, nie zmienia.** Zrozumienie panelu jest pedagogicznie ważne, bo operator M3 uczy się widzieć **dynamikę cyklu suszarniczego**: jak wilgotność drewna spada stopniowo (0,3-0,6% dziennie w fazie głównej), jak temperatura oscyluje w wąskim zakresie ±2°C wokół celu, jak wentylatory utrzymują stały przepływ 1400-1500 RPM, jak grzałki schodzą z 60% w nagrzewaniu do 40% w fazie głównej do 30% w kondycjonowaniu. Widząc to, operator M3 **wyczuwa normalny rytm cyklu**, i kiedy coś odbiega od rytmu, widzi szybciej niż osoba bez doświadczenia.

**Trzy typowe wartości na panelu dla cyklu dębu dzień 14 z 22** (dziś, 2026-05-30):

1. **Temperatura**: cel 58-60°C (faza główna), tolerancja ±3°C. Jeżeli poza tolerancją o 2-3°C, obserwacja. Jeżeli +4°C lub więcej, alarm.
2. **Wilgotność względna (RH)**: cel 45-50% (faza główna), tolerancja ±5%. Jeżeli poza tolerancją o 2-5%, obserwacja. Jeżeli +8% lub więcej, alarm.
3. **Wilgotność drewna**: cel dynamiczny (spada 0,3-0,6%/dzień w fazie głównej). Jeżeli tempo jest 0, sterownik szuka przyczyny (grzałki, wentylacja). Jeżeli tempo jest 1%+/dzień, może oznaczać za szybkie suszenie (ryzyko pęknięć), obserwacja.

### 2. Jak działa sterownik BH-50 w cyklu dębu

Sterownik **Brunner-Hildebrand Omega 7** (model używany w BH-50 od 2011) to przemysłowy sterownik PLC (Programmable Logic Controller) z oprogramowaniem specyficznym dla komór suszarniczych. Ma pamięć **20 programów fabrycznych** (sosna, świerk, dąb, buk, brzoza, klon i inne) plus **10 programów użytkownika** (EGIDA ma obecnie 4: SOS-STAND-28 sosna, DUB-STAND-28 dąb, BUK-STAND-25 buk, BRZ-STAND-25 brzoza).

**Cykl programowy** to zestaw **około 150 parametrów** opisujących jak komora ma się zachować przez 9-25 dni cyklu: **na każdą godzinę** cyklu sterownik ma zadane **temperatura cel, RH cel, tempo zmiany temperatury, tempo zmiany RH**. Program automatycznie **wylicza z aktualnej wilgotności drewna**, w której fazie jest (nagrzewanie, suszenie wstępne, suszenie główne, kondycjonowanie, chłodzenie), i dostosowuje parametry. Przełączenie fazy jest automatyczne (np. sterownik sam wykrywa, że wilgotność drewna doszła do 16% i przełącza cykl z suszenia głównego na kondycjonowanie).

**W fazie głównej dębu dzień 14**:
- Cel temperatura: 58-60°C (stopniowo rośnie z 52°C dnia 10 do 62°C dnia 15, potem spada)
- Cel RH: 45-50% (spada z 60% na początku fazy głównej do 40% pod koniec)
- Tempo schodzenia RH: ok. 0,8% dziennie
- Tempo spadku wilgotności drewna: 0,5-0,6% dziennie

**Regulacja proporcjonalna PID** (Proportional-Integral-Derivative, standard sterowników przemysłowych): sterownik **nie włącza grzałek na 100% gdy za zimno, nie wyłącza na 0% gdy za gorąco**. Wyliczenia na bieżąco: jak daleko jesteśmy od celu (P), jak długo odchylenie trwa (I), jak szybko odchylenie rośnie (D). Grzałki są włączane **procentowo** (np. 45% mocy) dla płynnej regulacji.

**Dlatego alarm 62°C zamiast 58°C nie był wynikiem „ktoś włączył grzałki na 100%"**, tylko wynikiem **utknięcia sprzężenia zwrotnego na termostacie**: sterownik myślał, że trzeba jeszcze grzać, bo dostawał fałszywy sygnał od termostatu GH-67 wymiennika ciepła (że temperatura wlotu jest niższa niż w rzeczywistości była).

### 3. Rozpoznawanie typów alarmów komory

**Alarm temperaturowy** (najczęstszy):
- Cel +3°C tolerancja, **+4°C = alarm**
- Cel -3°C tolerancja, **-4°C = alarm** (za zimna komora, też problem, ale rzadszy)
- Typowe przyczyny: termostat uszkodzony (patrz dziś), zawór gazu zaklejony, wymiennik ciepła zabrudzony, sensor temperatury uszkodzony (wtedy jedna sonda odstająca), drzwi komory niedomknięte (wszystkie cztery sondy niżej)

**Alarm wilgotności względnej (RH)**:
- Cel ±5% tolerancja, **±8% = alarm**
- Za wysoka RH w fazie głównej: problem z wyciągiem, drewno nie schnie, ryzyko pleśni wewnątrz
- Za niska RH w fazie początkowej: ryzyko pęknięć powierzchniowych (end checks) na czołach desek

**Alarm przepływu powietrza (wentylatory)**:
- Jeden z dwóch wentylatorów **poniżej 80% RPM** = alarm
- Oba wentylatory poniżej 80% = alarm krytyczny, komora grozi natychmiastowe wyłączenie
- Typowe przyczyny: zatkany filtr, uszkodzony silnik wentylatora, zwarcie prądu

**Alarm wilgotności drewna (sondy)**:
- Rozrzut między sondami **>3%** = alarm (wsadka niejednorodna lub sonda uszkodzona)
- Tempo spadku **0% przez 48h** = alarm stagnacji (drewno nie oddaje wody, problem z warunkami)
- Tempo spadku **>1,5% dziennie** = alarm szybkiego suszenia (ryzyko pęknięć)

**Alarm gazu głównego**:
- Ciśnienie zewnętrzne w zbiorniku gazu **poniżej 25% pełnego** = alarm, komora automatycznie przełącza na drugi zbiornik
- Poniżej 10% = alarm krytyczny, komora automatycznie wyłącza grzanie, sterownik wchodzi w tryb „chłodzenie awaryjne"

**Alarm sensora**:
- Sensor czujnika temperatury lub wilgotności pokazuje wartości **skrajne (niemożliwe fizycznie)** = alarm, sterownik odizolowuje sensor, korzysta z pozostałych (redundancja 4 sondy temperatury = 3 wystarczy do kontynuacji cyklu).

### 4. Maksymalne tempo zmiany temperatury i chłodzenia

Zasada **6°C na godzinę** dla komór suszarniczych konwencjonalnych stosujących się do gatunków twardych (dąb, buk, jesion, klon) wywodzi się z fizyki drewna. **Skurcz dębu** przy zmianie wilgotności wynosi **0,25% na 1% zmiany wilgotności** (wzdłużnie promieniowo). Przy szoku termicznym (nagła zmiana temperatury) powierzchnia deski traci wodę szybciej niż rdzeń, powstaje **gradient wilgotności** (5-10% różnicy), co w konsekwencji daje gradient wymiarowy i **naprężenia wewnętrzne**.

Naprężenia przekraczające **wytrzymałość dębu na rozciąganie w kierunku tangencjalnym** (ok. 5-6 MPa) powodują **pęknięcia rdzeniowe**, nie widoczne z zewnątrz, ujawniające się przy obróbce.

**Tempo 6°C/h** jest skonfigurowane w programie DUB-STAND-28 na dzień 14 jako limit: sterownik **sam nie zmieni temperatury szybciej**, jeśli program zadaje nową wartość. Jeżeli **ręczne sterowanie mistrza** generuje szybszą zmianę (jak dzisiaj, 10,5°C/h przez 10 minut), jest to **świadoma decyzja mistrza** na podstawie oceny ryzyka (np. dzień 14 drewno już mniej wrażliwe).

**Dla sosny (DUB-STAND-28 vs SOS-STAND-28)** zasada jest mniej rygorystyczna: **8-10°C/h** bo sosna ma bardziej jednorodną strukturę i mniejszy skurcz. Ale EGIDA trzyma **6°C/h** dla wszystkich gatunków jako standard bezpieczeństwa (Pan Henryk wyjaśnił to operatorom w 2014 roku, od tego czasu zasada w dokumentacji procedur).

**Dla chłodzenia na końcu cyklu** (faza 5, 1-2 dni) zasada jest jeszcze bardziej rygorystyczna: **4°C/h maksymalnie**, bo drewno wysuszone do 14% jest już wrażliwe na szok, a finał cyklu ma „wypełnić" wszystkie mikro-naprężenia, nie generować nowych.

### 5. Profilaktyka pęknięć i paczenia przez monitoring

Operator M3 obserwujący cykl **nie może zapobiec pęknięciom w trakcie cyklu** (to robią mistrz suszarni i serwis BTM przez prawidłowy program), ale **może wcześnie wykryć ryzyko** i zgłosić:

**Oznaki ryzyka pęknięć powierzchniowych (end checks)**:
- Rozrzut sond wilgotności **rośnie powyżej 2%** w fazie 1-3 dnia (drewno powierzchnia wysychana szybciej niż rdzeń)
- Temperatura **powyżej celu** w fazie nagrzewania (ponad +2°C przez godzinę)
- RH **poniżej celu** w fazie początkowej (ponad -5% przez 4 godziny)

**Oznaki ryzyka pęknięć rdzeniowych (internal checks)**:
- Tempo spadku wilgotności drewna **przekracza 1%/dzień** w fazie głównej
- Temperatura **skoki powyżej 3°C w ciągu godziny**
- Kondycjonowanie **skrócone lub pominięte** (decyzja mistrza, rzadka w EGIDA)

**Oznaki ryzyka paczenia (warping)**:
- Jedna sonda wilgotności **wyraźnie odstaje w górę** (sekcja wsadki schnie wolniej)
- Nierówne ułożenie stosów (widać przez okno obserwacyjne, widać że niektóre deski się już wyginają)
- RH **za niska** w fazie kondycjonowania (gradient nie wyrównuje się)

Operator M3 w szkoleniowej obecności w suszarni uczy się **rozpoznawać te oznaki i zgłaszać**. Dzisiaj Mykoła nie widział żadnej z nich poza sam alarmem temperaturowym, który Pan Henryk rozwiązał ręcznie. Ale za 6 miesięcy, po kursie suszarniczym pomocniczym, Mykoła będzie mógł samodzielnie interpretować te sygnały i decydować o korekcie.

### 6. Rola Maćka i monitoring weekendowy

**Maciek Wiśniewski** (pomocnik suszarni M1, 19 lat) ma zakres kompetencji **szerszy niż operator M3 w komorach**, ale **węższy niż mistrz**. Może:
- Odczytać panel i zapisać w dzienniku (samodzielnie)
- Wymienić papier w drukarce dziennika
- Uzupełnić olej smarujący w silnikach wentylatorów (rutyna serwisowa co 6 miesięcy, z listy BTM)
- Zamieść halę sterowania suszarni, umyć okna obserwacyjne komory

Nie może:
- Otworzyć drzwi komory w trakcie cyklu (tylko mistrz, tylko z powodów wyjątkowych)
- Wpisać korektę ręczną sterownika (hasło mistrza)
- Decydować o wsadce lub programie (to mistrz)
- Skasować alarmu lub wpisu w dzienniku alarmowym

**W rutynie weekendowej (bez alarmu)**:
- Sobota 10:00 i 16:00, niedziela 10:00 i 16:00 (4 odczyty w weekend)
- Dzienniki to zeszyt A4 na biurku, w jednym wierszu: data, godzina, temperatura, RH, wilgotność drewna (średnia), EMC, podpis
- Jeżeli odchylenie temperatury lub wilgotności **poza tolerancją** (>±3°C lub >±5% RH), Maciek dzwoni do Pana Henryka **natychmiast**, nie czeka do następnego odczytu
- Jeżeli alarm sterownika (czerwona dioda), Maciek dzwoni **natychmiast** i zostaje przy panelu do przybycia mistrza

**Po dzisiejszym alarmie**, rutyna zagęszczona do **co 4 godziny** (sobota 8:00, 12:00, 16:00, 20:00, niedziela analogicznie). Maciek dostaje dodatkowe wynagrodzenie (stawka weekendowa 150% zamiast 100%) za zagęszczoną obecność.

### 7. Dokumentacja alarmu w karcie KS-001

**Karta KS-001 wsadki bieżącej** (ta, którą Pan Henryk wypełnił przy starcie cyklu dębu 17.05) ma **4 sekcje**:
1. Wsadka planowana (wpisana 17.05, opis partii 2,5 m³ dębu)
2. Wsadka następna planowana (wpisana 29.05 w l3, opis planowanej sosny do Drew-Sus)
3. **Notatki i obserwacje** (wpisywana w ciągu cyklu, każde istotne zdarzenie)
4. Podpisy (17.05 start, potem po cyklu końcowym)

**Alarm dzisiejszy** wchodzi do sekcji 3. Pan Henryk wpisuje:
- Data i godzina początku alarmu (2026-05-30 09:43)
- Data i godzina rozwiązania alarmu (2026-05-30 10:15)
- Wartość zmierzona vs cel programu (62,3°C vs 58°C)
- Odchylenie (+4,3°C, próg alarmu +4°C)
- Prawdopodobna przyczyna (termostat GH-67 wymiennika ciepła, sprzężenie zwrotne, potwierdzone BTM)
- Podjęte działania (ręczna korekta zaworu gazu 72→45%, grzałek 68/64→40/40%)
- Rezultat (temperatura wróciła na 58°C w 32 minuty, spadek średni 10°C/h, powyżej limitu 6°C/h przez 10 min, akceptowalne dla dębu dzień 14)
- Stan drewna po alarmie (wilgotność bez zmian, rozrzut sond 1,6% niezmieniony)
- Plan (sterowanie ręczne do pon 02.06, serwis BTM, termostat do wymiany)
- Obecni (Pan Henryk mistrz, Mykoła Hrycenko M3 szkolenie)
- Podpis i godzina wypisania (H. Nowak, 10:45)

**Karta KS-001 wsadki bieżącej pozostaje w biurku suszarni do zamknięcia cyklu** (rozładunek 08.06). Wtedy wsadka jest „zamykana", karta podpisana przez mistrza i brygadzistę, skanowana do OneDrive EGIDA, papier do archiwum (retencja 3 lata papier + 5 lat skan).

**Audytor ISO 9001** może w dowolnym momencie zobaczyć kartę i powiedzieć: „pokażcie mi KS-001 dla wsadki dębu z maja 2026". Karta musi być do dyspozycji w ciągu 15 minut (ISO 9001 sekcja 7.5 „informacja udokumentowana"). Dlatego sekcja 3 jest wypełniana **na bieżąco, nie po cyklu**.

### 8. EMC w praktyce monitorowania dębu

**EMC (wilgotność równowagowa)** jest **wartością sterującą w czasie rzeczywistym**. Na panelu BH-50 widnieje jako „EMC: 8,4%" (dzisiaj). Oznacza to: **jeśli drewno pozostanie w aktualnym środowisku (58°C temperatura, 47% RH) dostatecznie długo, osiągnie wilgotność 8,4%**.

**Faktyczna wilgotność drewna wynosi 24,7% (średnia z 3 sond)**. Zatem **różnica** to 24,7 - 8,4 = **16,3%**. Drewno dąży do spadku, ponieważ jest „mokrzejsze" niż otoczenie pozwala.

**Tempo spadku** zależy od:
- Różnicy „aktualne - EMC" (im większa, tym szybsze oddawanie wody)
- Przepuszczalności drewna (dąb mniej przepuszczalny niż sosna, wolniej oddaje)
- Grubości deski (grubsza deska wolniej oddaje, bo woda musi się „przedrzeć" do powierzchni)

**Dla dębu 28 mm**: tempo 0,5% dziennie w fazie głównej jest normalne przy różnicy 16%. Jeśli różnica byłaby 20% (np. przez obniżenie RH do 35%), tempo mogłoby wzrosnąć do 0,8-1% dziennie, **ryzyko pęknięć rosłoby**.

**Dlatego sterownik nie obniża RH do skrajnie niskiej** w fazie głównej. Cel 45-50% RH + temperatura 58-60°C daje EMC 8-9%. Drewno schnie stopniowo, różnica „aktualne - EMC" jest umiarkowana (ok. 16%), tempo spokojne (0,5%/dzień), pęknięcia unikane.

**Operator M3 rozumie ten mechanizm intuicyjnie**. Widzi EMC 8,4, wilgotność drewna 24,7, różnicę 16%, tempo 0,5/dzień. **To jest normalne**. Gdyby zobaczył EMC 5%, różnicę 20%, tempo 1%/dzień, pomyślałby: „sterownik za mocno obniża RH, za ostro". Zgłosiłby mistrzowi.

### 9. Błędy typowe monitoringu początkującego

**Błąd 1. Ignorowanie drobnego odchylenia**. Operator początkujący widzi temperaturę 61°C zamiast 58°C, myśli „to tylko 3°C, jest w tolerancji". Tolerancja to ±3°C, 61°C faktycznie jest w granicy. Ale **trend** rośnie 0,5°C w ostatnich 20 minutach, za godzinę będzie 64°C, **wtedy alarm**. **Prawidłowo**: widząc trend rosnący ku granicy, operator **sygnalizuje wcześniej**, nie czeka na alarm.

**Błąd 2. Reset alarmu „żeby zniknął"**. Operator widzi czerwoną diodę, chce, żeby nie świeciła. Szuka przycisku „reset" na panelu, niektóre modele sterowników mają taki przycisk dostępny bez hasła. **To błąd**: alarm **pojawia się znów po chwili**, bo przyczyna nie została rozwiązana. Gorsze, sterownik traci historię alarmu (reset kasuje wpis), audyt ISO ma dziurę. **Prawidłowo**: **nie resetuj alarmu**, obserwuj, zgłoś mistrzowi, mistrz diagnozuje i dopiero potem resetuje po rozwiązaniu.

**Błąd 3. Otwieranie drzwi komory „żeby sprawdzić drewno"**. Operator myśli „zobaczę jak wygląda wsadka, czy coś się nie poszło". **To poważny błąd**: drzwi otwarte na 10 sekund w fazie głównej cyklu dębu generuje **spadek temperatury o 15-20°C w komorze** (powietrze gorące wychodzi, zimne wchodzi), sterownik reaguje alarmem, cykl może być „poślizgnięty" o 8-12 godzin, jakość drewna może ucierpieć. **Prawidłowo**: **drzwi komory otwierają się tylko na końcu cyklu** (faza chłodzenia zakończona), na polecenie mistrza. W trakcie cyklu wszystkie informacje są **z panelu i sond**, nie z bezpośredniego oka.

**Błąd 4. Mylenie RH powietrza z wilgotnością drewna**. Panel pokazuje „wilgotność 47%" (RH powietrza) i „wilgotność drewna 24,7%" (dwa różne parametry). Operator początkujący myśli: „drewno ma 47%, dużo, jeszcze dużo do schnięcia". Ale 47% to nie drewno, to powietrze. Drewno ma 24,7%, do celu 14% zostało 10,7%. **Prawidłowo**: rozróżniać na panelu **RH powietrza** (procent wilgotności powietrza w komorze) od **wilgotność drewna** (procent wody w drewnie). Są to dwa niezależne parametry, sterownik reguluje RH, drewno dostosowuje się samodzielnie.

**Błąd 5. Interpretacja rozrzutu sond jako „wszystko w porządku"**. Trzy sondy pokazują 22%, 24%, 28%. Średnia 24,7%. Operator myśli: „średnia dobra". Ale rozrzut 6% (28-22) jest **poważny**: jedna deska (sonda 3) schnie wolniej niż pozostałe. Może to być sonda uszkodzona, może deska z defektem wewnętrznym, może nierówne ułożenie stosu. **Prawidłowo**: patrzeć na **rozrzut, nie średnią**. Rozrzut >3% to sygnał do zgłoszenia mistrzowi.

**Błąd 6. „Sam naprawię, Panu Henrykowi nie będę zawracał głowy"**. Operator widzi alarm, myśli: „Pan Henryk jest zmęczony, ja sam spróbuję". **Absolutny błąd**: operator M3 nie ma hasła, nie ma wprawy, jego ingerencja **pogorszy sytuację**. Pan Henryk ma numer telefonu, ma uprawnienia, ma wprawę. **Prawidłowo**: **zawsze dzwoń do mistrza przy alarmie**, nawet jeśli alarm wydaje się drobny. Pan Henryk wolałby zostać wybudzony o 23:30 w niedzielę na fałszywy alarm, niż rano zobaczyć komorę z pękniętym drewnem po „samodzielnej naprawie" przez operatora bez uprawnień.

### 10. Szkolenie pomocnicze suszarnicze – następny krok Mykoły

Moduł szkoleniowy suszarnictwa pomocniczego (opisany w l3 pkt 11) jest opcjonalnym rozszerzeniem M3. Wymaga **zgody mistrza suszarni** (dziś Pana Henryka) i **ukończonego M3** (dla Mykoły planowanego na październik 2026). Zakres: 5 dni intensywnego szkolenia + egzamin.

**Dzisiejsza obecność Mykoły** (2026-05-30, 2 godziny) **liczy się** jako **wstępna praktyka** w kierunku szkolenia. Pan Henryk pod koniec dnia wpisze do akt osobowych Mykoły:

```
2026-05-30, 9:30-11:00
R. Hrycenko, operator M3, obecność szkoleniowa w suszarni.
Obserwacja cyklu dębu (dzień 14), alarm temperaturowy,
diagnoza i ręczna korekta mistrza.
Mykoła zrozumiał: granica kompetencji, procedura alarmu
(OBSERWUJ, ZAPISUJ, ZGŁOŚ, ZGŁOŚ WYŻEJ), dokumentacja
w KS-001.
Ocena: gotowy do dalszych obecności szkoleniowych.
Następna obecność planowana: rozładunek dębu 2026-06-08,
jako asysta przy pomiarach końcowych i pakowaniu.
Podpis: H. Nowak, mistrz suszarni.
```

Akta osobowe Mykoły są w biurze kierownika tartaku, w folderze „Szkolenia wewnętrzne". Ich zawartość wpływa na **kwalifikację Mykoły** do szkolenia suszarniczego pomocniczego w październiku 2026 (minimum 3 obecności szkoleniowe jako warunek dopuszczenia).

### 11. Co dzieje się dalej w cyklu dębu po alarmie

**Dziś (piątek 30.05)**: sterowanie ręczne od 10:25, stabilizacja przy 58°C, monitoring ciągły przez Pana Henryka do 16:00. Stan drewna: wilgotność 24,7% (bez zmian po alarmie, drewno odporne na tak krótkie odchylenie), rozrzut sond 1,6% (bez zmian).

**Sobota (31.05) i niedziela (01.06)**: Maciek monitoring co 4 godziny. Pan Henryk w sobotę rano (8:00-10:00) przyjdzie sprawdzić osobiście (brygadzista Marek zgodził się zapłacić nadgodziny sobotnie). Temperatura powinna trzymać się 58-60°C, wilgotność drewna spadać 0,5-0,6% dziennie.

**Poniedziałek (02.06)**: BTM przyjedzie rano (9:00) wymienić termostat GH-67 wymiennika ciepła. Komora w tym czasie **pracuje** (nie zatrzymują cyklu dla jednej godziny wymiany), BTM robi wymianę „na gorąco" (wyłącza tylko ten jeden komponent, sterownik kompensuje ręcznie na czas wymiany).

**Wtorek (03.06) – sobota (07.06)**: cykl kończy się fazą kondycjonowania (niedziela 31.05 rozpoczyna kondycjonowanie zgodnie z programem, choć alarm dzisiaj nie wpływa na kalendarz fazy). Temperatura stopniowo spada z 60°C do 55°C, RH rośnie z 45% do 75% (kondycjonowanie). Wilgotność drewna spada z 24% do 14%.

**Niedziela (07.06)**: faza chłodzenia, temperatura 55°C → 25°C (spadek powolny 4°C/h maks), RH 75% stabilne. Wilgotność drewna 14% docelowo.

**Poniedziałek (08.06)**: koniec cyklu 22 dni. **Otwieranie komory, rozładunek** (to jest l5 M3 T3, następna lekcja Mykoły).

## Scena domykająca, 11:00, wyjście Mykoły

Pan Henryk zostaje w hali sterowania (dziennik do zamknięcia, telefon do kolejnego operatora BTM potwierdzający wizytę poniedziałkową), Mykoła wychodzi z notatnikiem pełnym nowych zapisów. Przez okno hali sterowania widzi Maćka wracającego z hali pilarek z dziennikiem weekendowym w dłoni, Maciek patrzy pytająco. Mykoła pokazuje mu krótko: *„Alarm był, temperatura +4, Pan Henryk naprawił. Sterowanie ręczne do poniedziałku, ty co 4 godziny w weekend."*

Maciek kiwa głową, wchodzi do hali sterowania porozmawiać z Panem Henrykiem o weekendowym harmonogramie.

### 11:05, przejście do hali pilarek

Mykoła idzie przez plac magazynowy do hali pilarek. Dziś jest piątek, zmiana produkcyjna normalna. Jego zmiana na P3 rozpoczyna się od 12:00, do 12:00 ma 50 minut wolnego. Idzie do szafki pracowniczej, bierze kanapkę z torebki, siada na ławce przed halą, otwiera notatnik i **spisuje na czysto** to, co zobaczył dziś rano.

**Pięć wniosków**:

1. **Komora suszarnicza nie jest maszyną „do włączenia i wyłączenia"**. Cykl trwa 22 dni, operator obserwuje go, mistrz prowadzi, w ciągu tych 22 dni może się zdarzyć wszystko (alarmy, korekty, serwis). Operator M3 uczestniczy w tej złożoności **bez decyzji**, uczy się widzieć rytm.

2. **Alarm +4°C jest „drobny" dla dębu dzień 14**. To samo +4°C na dzień 3 nagrzewania byłoby poważniejsze. Pan Henryk widział to od razu („nie ma pośpiechu, niewielki alarm dobry trening"). Operator M3 nie ocenia priorytetu alarmu, **zgłasza wszystkie alarmy na równi**.

3. **Termostat GH-67** to komponent, który Mykoła wcześniej nie znał. Dzisiaj nauczył się, że sterownik komory ma wiele komponentów, **każdy może się zepsuć niezależnie**, i że serwis BTM ma wiedzę o typowych usterkach, której operator M3 nie ma i nie musi mieć.

4. **Procedura OBSERWUJ, ZAPISUJ, ZGŁOŚ, ZGŁOŚ WYŻEJ** jest **inna niż procedura pilarki** (STOP, zabezpiecz, zgłoś, udokumentuj). Komora nie ma „STOP" natychmiastowego. Operator musi zrozumieć tę różnicę, bo intuicja z pilarki podpowiada „zatrzymaj maszynę", ale w komorze **zatrzymanie cyklu** generuje więcej problemów niż rozwiązuje.

5. **Dokumentacja = ochrona**. Pan Henryk wpisuje w KS-001 nawet „drobne" alarmy, nawet „obecność szkoleniową Mykoły". W audycie ISO 9001 widać, że komora jest monitorowana, alarmy są rozwiązywane, personel jest szkolony. Bez tych wpisów nie można udowodnić nic. **Papiery są ochroną, nie przeszkodą**.

Mykoła zamyka notatnik, odkłada na ławkę, pije resztkę herbaty z termosu. O 11:35 wchodzi do hali pilarek, zaczyna przygotowanie P3 do zmiany (czyszczenie łóżka maszyny z trocin Damiana z porannej zmiany).

### 11:55, dyspozycja dnia

Marek przynosi dyspozycję dnia na P3 od 12:00 do 15:00. To jest **ZLE-2026-05-082**, klient Stolarz Meblowy Mrągowo (z l3), buk zwyczajny 25 × 130 × 4000 mm. Inny gatunek, inny sortyment, inna klasa (C24 meblowa, ale z warunkiem estetycznym). Mykoła wypełni nowe KDP-001.

Ale to jest następna lekcja, nie dzisiaj. Dzisiaj Mykoła kończy notatki suszarnicze i startuje produkcję bukową o 12:00. Wasyl dołączy o 12:15 po zakończeniu konserwacji z Jurim.

## Kluczowe terminy

**Alarm komory suszarniczej** (*alarm komory suszarniczej*, EN *kiln alarm*, ES *alarma de secadero*, UK *тривога сушильної камери*): sygnał sterownika sygnalizujący przekroczenie progu tolerancji parametru poza zakres, wymaga reakcji człowieka (mistrza suszarni), oznakowany czerwoną diodą i sygnałem dźwiękowym, dokumentowany w karcie KS-001.

**Sterownik Brunner-Hildebrand Omega 7** (*sterownik Omega 7*, EN *Omega 7 controller*, ES *controlador Omega 7*, UK *контролер Omega 7*): przemysłowy sterownik PLC stosowany w komorze BH-50, zawiera 20 programów fabrycznych plus 10 programów użytkownika, regulacja proporcjonalna PID, pamięć historii alarmów 24 miesiące.

**Regulacja proporcjonalna PID** (*regulacja PID*, EN *PID control*, ES *control PID*, UK *ПІД-регулювання*): algorytm sterowania wyliczający wyjście na podstawie odchylenia proporcjonalnego (P), całkowego (I) i różniczkowego (D), używany w sterowniku komory dla płynnej regulacji grzałek, zaworu gazu, wentylatorów bez skoków.

**Termostat wymiennika ciepła GH-67** (*termostat GH-67*, EN *GH-67 heat exchanger thermostat*, ES *termostato GH-67*, UK *термостат GH-67*): komponent instalacji gazowej komory BH-50 Brunner-Hildebrand, regulujący temperaturę wlotu wymiennika ciepła do komory, znany problem ze sprzężeniem zwrotnym przy wysokiej wilgotności otoczenia, seryjnie wymieniany podczas rocznego przeglądu BTM.

**Procedura OBSERWUJ-ZAPISUJ-ZGŁOŚ-ZGŁOŚ WYŻEJ** (*procedura alarmu komory dla M3*, EN *kiln alarm procedure for M3*, ES *procedimiento de alarma del secadero para M3*, UK *процедура тривоги сушарні для М3*): czterokrokowa procedura reakcji operatora M3 na alarm komory, różna od pilarkowej (STOP-zabezpiecz-zgłoś-udokumentuj), bo komory nie można szybko „zabezpieczyć".

**Maksymalne tempo zmiany temperatury 6°C/h** (*maksymalne tempo 6°C/h*, EN *max temperature change rate 6°C/h*, ES *tasa máxima de cambio de temperatura 6°C/h*, UK *максимальний темп зміни температури 6°C/год*): standard EGIDA dla wszystkich gatunków w komorze BH-50, zapobiega pęknięciom rdzeniowym, może być przekroczony krótkotrwale (do 10-15 minut) na decyzję mistrza w przypadkach ograniczonego ryzyka.

**Rozrzut sond wilgotności** (*rozrzut sond*, EN *moisture probe spread*, ES *dispersión de sondas de humedad*, UK *розкид зондів вологості*): różnica między najwyższym a najniższym odczytem trzech sond wilgotności drewna w komorze, wskaźnik jednorodności wsadki, wartość <2% OK, 2-3% obserwacja, >3% problem.

**Dziennik weekendowy suszarni** (*dziennik weekendowy*, EN *weekend kiln log*, ES *diario de fin de semana del secadero*, UK *вихідний журнал сушарні*): zeszyt A4 w twardej oprawie, wypełniany przez pomocnika suszarni 2-4 razy na dobę w dni wolne od pracy normalnej, zawiera datę, godzinę, odczyty panelu i podpis.

**Faza kondycjonowania** (*faza kondycjonowania*, EN *conditioning phase*, ES *fase de acondicionamiento*, UK *фаза кондиціонування*): przedostatnia faza cyklu (2-4 dni dla dębu), podwyższenie RH do 70-80% przy obniżonej temperaturze, wyrównanie gradientu wilgotności i rozpuszczenie naprężeń wewnętrznych deski.

**Faza chłodzenia** (*faza chłodzenia*, EN *cooling phase*, ES *fase de enfriamiento*, UK *фаза охолодження*): ostatnia faza cyklu (1-2 dni), obniżanie temperatury z 55-60°C do 25°C, tempo maksymalnie 4°C/h, bez modyfikacji wilgotności powietrza, przygotowuje drewno do wyjścia z komory bez szoku termicznego.

**Sterowanie ręczne** (*sterowanie ręczne*, EN *manual control mode*, ES *control manual*, UK *ручне керування*): tryb sterownika BH-50 dostępny tylko pod hasłem mistrza suszarni, wyłącza regulację AUTO i pozwala na bezpośrednie ustawienie procentu mocy grzałek, otwarcia zaworu gazu, obrotów wentylatorów, używany podczas diagnozy lub korekty.

**Serwis BTM Polska** (*serwis BTM*, EN *BTM Poland service*, ES *servicio BTM Polonia*, UK *сервіс BTM Польща*): polski dystrybutor i serwis komór Brunner-Hildebrand, ma wiedzę o typowych usterkach sterowników Omega 7, wykonuje przeglądy roczne i wymiany części, dostępny pod numerem 24/7.

**INFO-OSTRZEŻENIE-ALARM** (*trzy poziomy sygnału sterownika*, EN *info-warning-alarm levels*, ES *niveles información-advertencia-alarma*, UK *рівні інформація-попередження-тривога*): hierarchia sygnałów sterownika BH-50, INFO to notowanie bez reakcji, OSTRZEŻENIE to auto-korekta sterownika z obserwacją operatora, ALARM to wymagana reakcja człowieka.

**Akta osobowe szkolenia** (*akta osobowe szkolenia*, EN *personnel training record*, ES *expediente de formación*, UK *особова справа навчання*): folder w biurze kierownika EGIDA zawierający wpisy o obecnościach szkoleniowych operatora, stanowi podstawę do decyzji o dopuszczeniu do szkoleń rozszerzonych (np. suszarnictwo pomocnicze wymaga min. 3 obecności).

## Sprawdź siebie

### A. Alarmy i ich rozpoznawanie

1. Jakie są **trzy poziomy sygnałów** sterownika BH-50, i która z nich wymaga reakcji człowieka?

2. Sterownik pokazuje „ALARM: Temperatura powietrza 62,3°C, cel 58°C, odchylenie +4,3°C". Operator M3 jest sam przy panelu (mistrz na innym odcinku). Co robi jako pierwsze, drugie, trzecie?

3. Jaka jest **czterokrokowa procedura** operatora M3 przy alarmie komory? Napisz po kolei.

### B. Granica kompetencji w komorze

4. Operator M3 widzi alarm temperaturowy. Kuszą go dwa przyciski na panelu: „Reset alarmu" (bez hasła) i „Sterowanie ręczne grzałek" (z hasłem). Które naciska? Wybierz i uzasadnij:
a) Reset alarmu, bo wydaje się prosty
b) Sterowanie ręczne grzałek, bo wyłączenie grzałek pomoże
c) Żaden, bo operator M3 nie resetuje ani nie zmienia parametrów
d) Oba, żeby pokazać uprawnienia

5. Operator M3 jest w komorze podczas cyklu dębu dzień 14, nudzi się, chce zobaczyć jak wygląda drewno w komorze. Czy może otworzyć drzwi komory na 10 sekund „tylko żeby zerknąć"? Uzasadnij.

6. Pan Henryk jest na urlopie przez 2 tygodnie. Komora pracuje pełny cykl 22 dni. Kto jest odpowiedzialny za komorę w tym czasie i co to oznacza dla operatora M3?

### C. Interpretacja parametrów

7. Panel pokazuje: temperatura 58°C, RH 47%, wilgotność drewna średnia 24,7%, EMC 8,4%. Jaka jest różnica między aktualną wilgotnością drewna a EMC, i co ta różnica oznacza dla tempa suszenia?

8. Trzy sondy wilgotności drewna pokazują: 22%, 24%, 28%. Średnia 24,7%. Operator początkujący chwali „dobra średnia". Co widzi mistrz i dlaczego zgłasza to jako problem?

9. Temperatura rośnie stopniowo: 58°C, potem 59°C, potem 60°C, potem 61°C (w ciągu godziny). Cel 58°C, tolerancja ±3°C. Alarm jeszcze nie, bo 61°C jest w granicy 58±3. Czy operator M3 już teraz sygnalizuje mistrzowi, czy czeka do alarmu?

### D. Maksymalne tempo i profilaktyka pęknięć

10. Zasada **maksymalnego tempa zmiany temperatury 6°C/h** dla komór konwencjonalnych. Co powoduje jej przekroczenie dla dębu, i jaki jest widoczny skutek u klienta?

11. Po alarmie dzisiejszym temperatura spadła z 62,3°C na 58,2°C w 32 minuty. Oblicz średnie tempo spadku i porównaj z limitem. Czy korekta była w granicach bezpieczeństwa dla dębu dzień 14?

12. Dlaczego dla **sosny** zasada może być 8-10°C/h, a dla **dębu** musi być 6°C/h? Podaj przyczynę strukturalną drewna.

### E. Dokumentacja alarmu

13. Karta KS-001 dla wsadki dębu bieżącego (start 17.05). Alarm w piątek 30.05. W której sekcji karty wpisuje się ten alarm, i jakie elementy wpisu są **wymagane**?

14. Audytor ISO 9001 przychodzi w czerwcu 2026 i mówi: „pokażcie mi KS-001 dla wsadki dębu z maja". W ciągu ilu minut karta musi być do dyspozycji? Gdzie jest przechowywana?

15. Pan Henryk wpisuje w KS-001 „obecni: Mykoła Hrycenko (M3 szkolenie)". Dlaczego jawnie zapisuje obecność Mykoły, nawet jeśli Mykoła niczego nie decydował?

### F. Rola Maćka i plany

16. Maciek jest pomocnikiem suszarni M1. Co może, a czego nie może robić z komorą w weekend, gdy Pana Henryka nie ma?

17. Zwykła rutyna weekendu: Maciek robi 4 odczyty na dobę (10:00 i 16:00 sobota i niedziela). Dlaczego po alarmie Pan Henryk zwiększa rutynę do co 4 godziny (8 odczytów), a nie utrzymuje standardową 4?

18. Mykoła dzisiaj zaliczył obecność szkoleniową w suszarni (2 godziny). To liczy się jako **wstęp** do czego, i jakie są wymagania formalne do uczestnictwa w tym kolejnym kroku?
