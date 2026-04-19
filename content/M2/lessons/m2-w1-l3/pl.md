---
id: m2-w1-l3
blok: bezpieczenstwo
czas: 120
---

## Wprowadzenie

Trzeci dzień Haia jako operatora. Wchodzi do hali ubrany jak operator (lekcja 2 została w głowie), podchodzi do pilarki taśmowej i kładzie rękę na zielonym przycisku START. Brygadzista zatrzymuje go jednym słowem: **„Najpierw STOP."**

Hai patrzy zdezorientowany. Przecież chce **uruchomić** maszynę, nie zatrzymać ją. Brygadzista odwraca jego dłoń i pokazuje czerwony grzybek na żółtym tle, 30 centymetrów na lewo od zielonego START-u. **„Zanim naciśniesz START, sprawdź, czy STOP jest sprawny i w twoim zasięgu. Jeśli nie wiesz, gdzie jest STOP, nie dotykaj START-u."**

Ta lekcja tłumaczy, dlaczego w każdej maszynie do drewna układ zatrzymania **ma pierwszeństwo** nad układem uruchamiania. Dlaczego grzybek ma kolor czerwony na żółtym tle. Dlaczego w zakładzie z trzema stanowiskami pilarki widzisz **sześć grzybków**, a nie trzy. I dlaczego codzienny test STOP-u to nie paranoja brygadzisty, tylko wymóg Rozp. MG 2000.

Pierwsza zasada tej lekcji: **twoja ręka wraca do STOP-u zanim druga dotknie START-u**. Tak samo będziesz pracował w 2026, w 2036 i w ostatni dzień przed emeryturą.

## Cele

Po tej lekcji:

1. Rozumiesz zasadę fail-safe: w każdej maszynie do drewna układ zatrzymania (STOP) ma pierwszeństwo nad układem uruchamiania (START). Ta hierarchia wynika z konstrukcji, normy i prawa, nie z wyboru operatora.
2. Rozpoznajesz grzybek wyłącznika awaryjnego wg normy PN-EN ISO 13850: kolor czerwony, tło żółte, kształt grzyba (łatwy do uderzenia dłonią lub łokciem), samozatrzaśnięty po naciśnięciu.
3. Znasz trzy kategorie zatrzymania (0, 1, 2) i wiesz, która z nich odpowiada pilarce taśmowej, tarczowej i frezarce.
4. Lokalizujesz wszystkie wyłączniki awaryjne stanowiska z każdej pozycji roboczej (zasięg <1 metra) i umiesz wskazać cztery rodzaje pułapek, które unieważniają E-stop.
5. Wykonujesz codzienny test funkcjonalny wyłącznika awaryjnego przed rozpoczęciem pracy i wiesz, jak go zgłosić brygadziście.

## Treść

### Zasada fail-safe: STOP > START

**Fail-safe** to zasada konstrukcji maszyn, w której uszkodzenie systemu **zatrzymuje** maszynę, nie uruchamia. Stosowana od lat 60 XX wieku w lotnictwie, od lat 80 w przemyśle drzewnym. Zapisana w polskim prawie w **Rozporządzeniu Ministra Gospodarki z 14 kwietnia 2000 r.**, § 7 ust. 1:

> *„Obrabiarki do drewna powinny być wyposażone w urządzenia sterujące zapewniające ich natychmiastowe zatrzymanie w sytuacji zagrożenia. Urządzenia te powinny być łatwo dostępne z każdego stanowiska obsługi."*

W praktyce oznacza to trzy reguły konstrukcyjne:

- **STOP jest silniejszy niż START**. Jeśli naciśniesz oba jednocześnie, maszyna się zatrzymuje.
- **STOP działa nawet przy uszkodzeniu zasilania**. Grzybek rozłącza obwód mechanicznie, niezależnie od sterownika PLC.
- **STOP jest pasywny w spoczynku**. Trzeba go nacisnąć raz (zatrzymanie), potem **obrócić i wyciągnąć** (reset). Samoczynne odblokowanie jest wykluczone.

::: info
**Historia zasady**: w latach 70 XX wieku w zakładach drzewnych używano pojedynczego przycisku START-STOP (jeden włącznik, dwie pozycje). Po serii amputacji w NRD i Finlandii norma EN 418 (1993) wymusiła **oddzielenie obwodów**. Polska implementacja: PN-EN 418 (1999), następnie PN-EN ISO 13850 (2015).
:::

### Grzybek: czerwony na żółtym tle

Norma **PN-EN ISO 13850:2015** opisuje wyłącznik awaryjny (E-stop) precyzyjnie:

- **Kolor przycisku**: czerwony.
- **Kolor tła pod przyciskiem**: żółty.
- **Kształt**: grzybowaty (head of a mushroom), średnica 40-60 mm, wystający o 15-20 mm nad płaszczyznę.
- **Mechanizm**: naciśnięcie zatrzaskuje, odblokowanie przez **obrót w prawo** (klucz, rygiel, czasem pociągnięcie).

Dlaczego kolor czerwony na żółtym tle, a nie czerwony na szarym pulpicie? Kontrast. Oko operatora w warunkach tartaku (oświetlenie 300-500 lux, zapylenie 2-10 mg/m³) rozpoznaje czerwony na żółtym **w 0,2 sekundy**, czerwony na szarym **w 0,5-0,8 sekundy**. Trzy razy szybciej. To jest różnica między „ręka na STOP zanim deska uderzy" a „deska uderzyła, ręka w drodze".

::: warning
**Uwaga na podróbki**: tanie pilarki z marketów importowe mają czasem „e-stop" w kolorze czerwonym na czarnym pulpicie, bez żółtego tła, bez samozatrzasku (sprężyna odbija po puszczeniu). **To nie jest E-stop w sensie PN-EN ISO 13850**. Zgłoś taki przycisk brygadziście, nie uruchamiaj maszyny.
:::

### Trzy kategorie zatrzymania

Norma **PN-EN 60204-1** (bezpieczeństwo maszyn, wyposażenie elektryczne) definiuje trzy kategorie zatrzymania:

**Kategoria 0**: natychmiastowe odcięcie zasilania silnika. Maszyna **zatrzymuje się wybiegiem** (tzn. kręci się dalej dzięki bezwładności, aż tarcie ją zatrzyma). Pilarka tarczowa z silnikiem 4 kW ma wybieg **8-15 sekund**. Pilarka taśmowa z kołem zamachowym: **20-30 sekund**. W tym czasie ostrze jest **dalej niebezpieczne**.

**Kategoria 1**: sterowane zatrzymanie z hamulcem. Silnik dostaje sygnał hamowania, ostrze zatrzymuje się w **3-8 sekund**. Standard dla nowych pilarek tarczowych w UE (wymóg od 2006 r., dyrektywa maszynowa 2006/42/WE).

**Kategoria 2**: sterowane zatrzymanie z zachowaniem zasilania (maszyna „czuwa", gotowa do wznowienia). Stosowana rzadko, głównie w automatycznych liniach przemysłowych.

**Co to znaczy dla operatora**: kategoria 0 to **stara maszyna**. Kategoria 1 to **nowa maszyna z hamulcem**. Przy kategorii 0 **nie podchodź do ostrza przez 30 sekund** po naciśnięciu STOP. Zliczanie na głos („tysiąc jeden, tysiąc dwa…") to nie dziwactwo brygadzisty, to **ochrona palców**.

::: example
**Przypadek z polskiego tartaku (Opolskie, 2022)**: operator pilarki taśmowej z 2001 r. (kategoria 0) nacisnął STOP, zobaczył klocek między prowadnicami, sięgnął po niego **po 12 sekundach**. Koło zamachowe jeszcze się kręciło. Amputacja palca wskazującego. Wniosek PIP: maszyna sprawna, operator pominął czas wybiegu. Rekomendacja: **modernizacja do kategorii 1 z hamulcem**.
:::

### Lokalizacja i rytuał „ręka na STOP"

Rozp. MG 2000 § 7 ust. 2 wymaga, aby wyłącznik awaryjny był **„łatwo dostępny z każdego stanowiska obsługi"**. Przy pilarce taśmowej z dwoma operatorami (podawacz + odbiorca) to oznacza **dwa grzybki**: po jednym na każdym stanowisku, każdy w zasięgu jednej ręki (<1 metra).

Rytuał, który wchodzi w nawyk po miesiącu pracy:

1. **Podchodząc do maszyny**: zlokalizuj grzybek wzrokowo. Sprawdź kolor (czerwony na żółtym), kształt (wystający), stan (bez śladów uderzenia, bez przyklejonych wiórów).
2. **Przed uruchomieniem**: połóż lewą dłoń na grzybku. Dopiero teraz prawa dłoń idzie na START.
3. **W trakcie cięcia**: lewa dłoń **nie zdejmuje się z zasięgu grzybka**. Przesuwa drewno, ale wraca do pozycji nad grzybkiem między cięciami.
4. **W sytuacji zagrożenia**: uderzasz dłonią, łokciem albo biodrem. Nie szukasz palcem. Grzybek jest na tyle duży, że trafisz nawet w półmroku albo z zamkniętymi oczami.

### Cztery pułapki, które unieważniają E-stop

::: warning
Grzybek może **fizycznie istnieć** i **prawnie nie istnieć**. Cztery sytuacje, w których E-stop nie zadziała:

1. **Nieosiągalny**: zastawiony stosem desek, skrzynką narzędzi, workiem trocin. Widzisz, nie dosięgniesz.
2. **Zablokowany**: klin, nakrętka, kawałek drewna wciśnięty pod grzybek. Wciśniesz, wróci sam.
3. **Niesprawny mechanicznie**: rdza, uszkodzony samozatrzask, poluzowane mocowanie. Wciśniesz, nie zatrzyma.
4. **Nieprzetestowany**: działa w teorii, nikt nie sprawdzał od miesięcy. Wciśniesz, może zadziała, może nie.
:::

Trzy pierwsze pułapki widzi operator z szafki ŚOI. Czwarta pułapka wymaga **codziennego testu funkcjonalnego**.

### Test funkcjonalny E-stop (codziennie, przed zmianą)

Rozp. MG 2000 § 7 ust. 4 nakłada na operatora obowiązek **sprawdzenia działania urządzeń zabezpieczających przed rozpoczęciem pracy**. Test E-stop wygląda tak:

1. **Uruchomienie maszyny bez obciążenia** (tylko silnik, bez drewna). Taśma/tarcza na obrotach jałowych.
2. **Naciśnięcie grzybka**. Maszyna musi zatrzymać się natychmiast (kategoria 1: hamulec w 3-8 s) albo zacząć wybieg (kategoria 0: 15-30 s).
3. **Obrót grzybka** do odblokowania. Przycisk musi wyskoczyć sam po obrocie.
4. **Ponowne uruchomienie**. Maszyna musi startować od zera, bez pamięci poprzedniego stanu.
5. **Zapis w dzienniku**: „E-stop stanowisko X, OK, [podpis, godzina]". W kilku zakładach zapis to jeden „+" na tablicy kredą, ale zapis musi być.

::: tip
**Jeśli którykolwiek z pięciu kroków nie przebiegł prawidłowo: zatrzymaj maszynę fizycznie (wyłącznik główny), zgłoś brygadziście, nie rozpoczynaj pracy. Art. 210 § 1 KP daje ci prawo do powstrzymania się od pracy, gdy warunki zagrażają życiu lub zdrowiu.**
:::

## Kluczowe terminy

- **STOP awaryjny (E-stop)** – Emergency STOP (E-stop) – Parada de emergencia (E-stop) – Аварійний STOP (E-stop)
- **Grzybek STOP** – Mushroom STOP button – Pulsador tipo seta – Грибоподібна кнопка STOP
- **PN-EN ISO 13850** – PN-EN ISO 13850 – PN-EN ISO 13850 – PN-EN ISO 13850
- **Wybieg maszyny** – Run-down time – Tiempo de inercia – Час вибігу машини
- **Reset grzybka** – Mushroom reset – Reinicio del pulsador – Скидання грибоподібної кнопки
- **Kategoria zatrzymania 0/1/2** – Stop category 0/1/2 – Categoría de parada 0/1/2 – Категорія зупинки 0/1/2
- **Test funkcjonalny E-stop** – E-stop functional test – Prueba funcional del E-stop – Функціональний тест аварійного STOP

## Sprawdź siebie

**Pytanie 1.** Pracujesz przy pilarce tarczowej z 2001 r. (kategoria 0, bez hamulca). Naciskasz E-stop. Po ilu sekundach możesz bezpiecznie podejść do ostrza?

A) Od razu, bo E-stop zatrzymuje silnik natychmiast.
B) Po 3-8 sekundach.
C) **Po 15-30 sekundach (czas wybiegu koła zamachowego), najlepiej po pełnym zatrzymaniu wizualnym.**
D) Po godzinie, bo tarcza się grzeje.

**Pytanie 2.** Dlaczego grzybek E-stop ma kolor czerwony na żółtym tle, a nie na szarym?

A) Bo żółty to kolor przemysłowy.
B) **Bo kontrast czerwony-żółty pozwala oku operatora rozpoznać E-stop w 0,2 sekundy, trzy razy szybciej niż czerwony na szarym.**
C) Bo taka jest moda w Niemczech i Polska skopiowała.
D) Bo żółty odstrasza owady.

**Pytanie 3.** Podchodzisz do pilarki taśmowej i widzisz, że pod grzybkiem leży kawałek listwy, pozornie przypadkowo. Co robisz?

A) Zdejmuję listwę, uruchamiam maszynę, pracuję normalnie.
B) Zostawiam listwę, testuję, czy grzybek działa mimo przeszkody.
C) **Nie uruchamiam maszyny. Grzybek jest zablokowany (pułapka 2 z czterech), zgłaszam brygadziście, czekam na naprawę albo potwierdzenie.**
D) Naciskam grzybek razem z listwą, żeby „wytrenować mechanizm".

**Refleksja**: Jutro, zanim naciśniesz jakikolwiek przycisk START w całym zakładzie, **znajdź grzybek**. Jeśli nie widzisz go w zasięgu 1 metra, znajdź brygadzistę, nie maszynę. Operator, który uruchamia maszynę bez zlokalizowanego STOP-u, łamie Rozp. MG 2000 § 7 ust. 1 i ryzykuje własne palce. Obie konsekwencje są realne.

## Link do praktyki

**Jutro rano w tartaku:**

1. **Mapa STOP-ów**: obejdź swoje stanowisko i narysuj na kartce, gdzie są wszystkie wyłączniki awaryjne (grzybki, linki STOP na osłonach, stopki nożne). Przy pilarce taśmowej z dwoma operatorami powinno być minimum dwa grzybki. Policz, ile jest naprawdę.
2. **Codzienny test**: wykonaj pięciokrokowy test E-stop opisany w lekcji. Przy pierwszym teście poproś brygadzistę o asystę, żeby zobaczył i potwierdził. Zapisz w dzienniku albo na tablicy.
3. **Rytuał rąk**: przez pierwszy tydzień pracy wyłącznie **lewa dłoń na grzybku zanim prawa dotknie START-u**. Po tygodniu to wchodzi w nawyk mięśniowy i nie wymaga świadomego skupienia. Brygadzista sprawdzi cię wzrokiem z odległości 3 metrów.

## Notatki dla trenera

**Akcenty lekcji:**

- Drugi krok rytuału **sprawdź – uruchom – zgłoś**. Po „sprawdź siebie" z lekcji 2 przychodzi **„sprawdź maszynę"**, zaczynający się od STOP-u. Podkreśl: **uruchomienie to nie pierwsza czynność, tylko trzecia (po sprawdzeniu ŚOI i sprawdzeniu E-stop).**
- Hai kontynuacja łuku: w pilocie „pierwszy raz sam", w l2 „ubiera się jak operator", tutaj „kładzie lewą dłoń na STOP-ie". Cielesny gest ukotwiczony w nawyku. W l4 wykona pięciopunktowy checklist, zamykający rytuał tygodnia.
- Fail-safe principle nie jest „bezpieczniej = drożej". To jest **prawny standard** wynikający z Rozp. MG 2000 i normy PN-EN ISO 13850. Maszyny bez tego standardu są **nielegalne w eksploatacji** po 2006 r. (dyrektywa maszynowa 2006/42/WE).

**Pułapki migranckie:**

- W wielu krajach (Wietnam, Mołdawia, Gruzja, częściowo Ukraina) stare maszyny bez E-stop są w użyciu. Operator przenosi odruch „jedyny przycisk to START, w razie czego wyłącz zasilanie główne". W Polsce to skrót, który kosztuje palce (wybieg koła zamachowego 15-30 s bez hamulca).
- Pokaż fizycznie różnicę: czerwony grzybek na żółtym tle vs. czerwony przycisk na szarym pulpicie. Zadaj pytanie migrantom: „ile taśm potrzebujesz, żeby przyciemnić halę tak, żeby czerwony na szarym zniknął?". Odpowiedź: jedna (zapylenie po 2 h cięcia dębu).
- Czwarta pułapka (nieprzetestowany) jest najtrudniejsza pedagogicznie. Operator myśli „brygadzista testował w zeszłym tygodniu, to wystarczy". Rozp. MG 2000 wymaga **codziennego testu**. Pokaż zapis w dzienniku jako dowód, nie biurokrację.

**Link do M1:**

- Tydzień 1 l8 M1: rytuał STOP brygady ewakuacyjny. Ten sam znak (czerwony grzybek na żółtym tle) wraca tu jako STOP operatorski. W M1 STOP był na ścianie (ewakuacja), w M2 STOP jest na pulpicie (maszyna).
- Tydzień 4 l6 M1: zgłaszanie zdarzeń 5W1H. Test E-stop i niesprawność STOP-u są klasycznym „near-miss" do zgłoszenia przed wypadkiem.

**Trudne pytania:**

- „Ile razy dziennie mam testować STOP?" Raz, przed rozpoczęciem zmiany, na maszynie bez obciążenia. Ponadto po każdej awarii, po każdej wymianie taśmy/tarczy, po każdym dłuższym postoju (>4 h).
- „Co jeśli STOP wyskakuje sam podczas pracy?" Uszkodzony samozatrzask. Wyłącz maszynę wyłącznikiem głównym, zgłoś brygadziście, nie próbuj „docisnąć mocniej". Wymagana wymiana przez uprawnioną osobę.
- „Czy mogę nacisnąć STOP dla wygody (zamiast używać normalnego STOP-u cyklu)?" Nie. E-stop jest zaprojektowany na **sytuacje zagrożenia**, nie na zatrzymania rutynowe. Częste używanie zużywa samozatrzask i skraca żywotność o 5-10 razy. Do rutynowego zatrzymania służy czarny przycisk STOP cyklu.

**Materiały pomocnicze:**

- Pokaz fizyczny grzybka E-stop zdemontowanego z maszyny (stary element z wymiany): rozkręcony, widać samozatrzask i mechaniczne rozłączenie obwodu.
- Wydruk § 7 Rozp. MG 2000 w 4 językach (PL/EN/ES/UK) na ścianie przy stanowisku.
- Stoper albo telefon z sekundnikiem do testu wybiegu pilarki: uczeń mierzy faktyczny czas wybiegu swojej maszyny, zapisuje w dzienniku.
- Wideo 30 s amputacji palca na pilarce kategorii 0 (rekonstrukcja PIP, 2022) do omówienia etycznie: „nie dla szoku, dla zrozumienia dlaczego 30 s czekania".
