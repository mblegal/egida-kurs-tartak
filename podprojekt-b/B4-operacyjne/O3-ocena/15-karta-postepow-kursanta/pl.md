---
typ: karta postępów
dokument: karta postępów Kursanta (zbiorcze zestawienie wyników wszystkich narzędzi oceny w trakcie cyklu Kursu, parametryzowana na pojedynczego Kursanta)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O3-ocena
klasa: 2
parametryzacja: CSV-DOCX
język: pl
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie diagnozy efektów uczenia się Kursanta i informacji zwrotnej dla osoby uczącej się
charakter: dokument zbiorczy parametryzowany przedstawiający Kursantowi i instruktorowi pełny obraz postępów w trakcie cyklu Kursu (sprawdziany cząstkowe, quizy uzupełniające, testy modułowe, test końcowy); narzędzie informacji zwrotnej dla Kursanta i podstawa decyzji metodycznych instruktora; wydawany Kursantowi w jego języku oraz w języku polskim do akt
strony: Kursant (osoba, której dotyczy karta i odbiorca informacji o postępach), instruktor Kursu (autor decyzji metodycznych w oparciu o kartę), koordynator Kursu (osoba prowadząca ewidencję kart postępów cyklu), Fundacja pomocy prawnej EGIDA (właściciel narzędzia)
parametry:
  - IMIE_KURSANTA - imię (imiona) Kursanta
  - NAZWISKO_KURSANTA - nazwisko Kursanta
  - NR_KARTY_UCZESTNIKA - numer ewidencyjny karty uczestnika Kursanta (np. 2026/C1/001/KU)
  - CYKL_KURSU - oznaczenie cyklu Kursu (np. C1/2026)
  - DATA_GENERACJI - data wygenerowania karty postępów w formacie DD-MM-RRRR
  - WYNIK_SPC_M1_T12 - wynik sprawdzianu cząstkowego Modułu 1 blok T1+T2 w postaci X/30 albo wartość specjalna nie podejmował
  - WYNIK_SPC_M1_T34 - wynik sprawdzianu cząstkowego Modułu 1 blok T3+T4 w postaci X/30 albo wartość specjalna nie podejmował
  - WYNIK_QUM_M1 - wynik quizu uzupełniającego Modułu 1 w postaci X/30 albo wartość specjalna nie podejmował (samoocena albo poprawkowy zaznaczone w kolumnie obok)
  - TRYB_QUM_M1 - tryb przeprowadzenia quizu uzupełniającego Modułu 1 (samoocena albo poprawkowy albo nie dotyczy)
  - WYNIK_QUM_M2 - wynik quizu uzupełniającego Modułu 2 w postaci X/110 albo wartość specjalna nie podejmował
  - TRYB_QUM_M2 - tryb przeprowadzenia quizu uzupełniającego Modułu 2 (samoocena albo poprawkowy albo nie dotyczy)
  - WYNIK_QUM_M3 - wynik quizu uzupełniającego Modułu 3 w postaci X/45 albo wartość specjalna nie podejmował
  - TRYB_QUM_M3 - tryb przeprowadzenia quizu uzupełniającego Modułu 3 (samoocena albo poprawkowy albo nie dotyczy)
  - WYNIK_TEST_M1 - wynik testu modułowego Modułu 1 (lekcja l8 tygodnia 4) w postaci X/110 albo wartość specjalna nie podejmował
  - WYNIK_TEST_M2 - wynik testu modułowego Modułu 2 (lekcja l8 tygodnia 4) w postaci X/40 albo wartość specjalna nie podejmował
  - WYNIK_TEST_M3 - wynik testu modułowego Modułu 3 (lekcja l8 tygodnia 4, równoznaczna z testem końcowym Kursu) w postaci X/108 albo wartość specjalna nie podejmował
  - WYNIK_TKK - wynik testu końcowego Kursu w postaci X/108 albo wartość specjalna nie podejmował
  - DECYZJA_TKK - decyzja po teście końcowym Kursu (zaliczony albo niezaliczony albo nie podejmował)
  - KOMENTARZ_INSTRUKTORA - krótki komentarz instruktora dla Kursanta dotyczący ogólnego obrazu postępów (opcjonalny)
  - INSTRUKTOR - imię i nazwisko instruktora prowadzącego Kursanta
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora Kursu
  - NR_KARTY_POSTEPOW - numer ewidencyjny karty postępów (np. 2026/001/KP)
---

# KARTA POSTĘPÓW KURSANTA

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejsza karta postępów dokumentuje **pełny obraz wyników Kursanta w trakcie cyklu Kursu** w odniesieniu do wszystkich narzędzi oceny: sprawdzianów cząstkowych, quizów uzupełniających, testów modułowych (lekcje l8 tygodnia 4 każdego Modułu) i testu końcowego Kursu. Karta jest **narzędziem informacji zwrotnej** dla Kursanta i **podstawą decyzji metodycznych** instruktora (planowanie powtórek, decyzje o trybie samooceny albo poprawkowym, ocena gotowości Kursanta do egzaminu praktycznego).

Karta jest wydawana Kursantowi w jego języku ojczystym (polski, angielski, hiszpański albo ukraiński) oraz, niezależnie od języka Kursanta, w wersji polskiej do akt Kursu.

Karta jest dokumentem parametryzowanym: faktyczna karta dla konkretnego Kursanta i konkretnego momentu cyklu powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu (CSV) za pomocą skryptu generatora. Lista oznaczeń pól danych znajduje się w nagłówku YAML tego dokumentu w polu `parametry`.

| Identyfikator wzoru[^1] | Numer ewidencyjny karty postępów[^2] | Data wygenerowania karty (DD-MM-RRRR) |
|---|---|---|
| KP-1.0/2026 | {{NR_KARTY_POSTEPOW}} | {{DATA_GENERACJI}} |

---

## Część A. Identyfikacja Kursanta

| Pole | Wartość |
|---|---|
| Imię (imiona) Kursanta: | {{IMIE_KURSANTA}} |
| Nazwisko Kursanta: | {{NAZWISKO_KURSANTA}} |
| Numer karty uczestnika Kursanta: | {{NR_KARTY_UCZESTNIKA}} |
| Cykl Kursu: | {{CYKL_KURSU}} |
| Instruktor prowadzący: | {{INSTRUKTOR}} |

---

## Część B. Wyniki narzędzi oceny

### Sprawdziany cząstkowe Modułu 1

Sprawdziany cząstkowe są narzędziem śródsemestralnej diagnostyki postępu Kursanta po drugim i trzecim tygodniu Modułu 1. Każdy sprawdzian to 15 pytań zamkniętych po 2 punkty (razem 30 punktów), próg pomyślnego rozwiązania 70% = 21 punktów. Sprawdziany dla Modułu 2 i Modułu 3 nie są przewidziane w aktualnej wersji programu Kursu.

| Narzędzie | Identyfikator wzoru | Maksimum | Wynik Kursanta |
|---|---|---|---|
| Sprawdzian cząstkowy M1 (T1+T2) | SPC-M1-T12-1.0/2026 | 30 punktów | {{WYNIK_SPC_M1_T12}} |
| Sprawdzian cząstkowy M1 (T3+T4) | SPC-M1-T34-1.0/2026 | 30 punktów | {{WYNIK_SPC_M1_T34}} |

### Quizy uzupełniające Modułów

Quizy uzupełniające są narzędziem samooceny po teście modułowym (gdy zdany) albo trybu poprawkowego (gdy test modułowy nie zdany). Tryb przeprowadzenia quizu wskazany jest w kolumnie „Tryb".

| Narzędzie | Identyfikator wzoru | Maksimum | Wynik Kursanta | Tryb |
|---|---|---|---|---|
| Quiz uzupełniający M1 | QUM-M1-1.0/2026 | 30 punktów | {{WYNIK_QUM_M1}} | {{TRYB_QUM_M1}} |
| Quiz uzupełniający M2 | QUM-M2-1.0/2026 | 110 punktów | {{WYNIK_QUM_M2}} | {{TRYB_QUM_M2}} |
| Quiz uzupełniający M3 | QUM-M3-1.0/2026 | 45 punktów | {{WYNIK_QUM_M3}} | {{TRYB_QUM_M3}} |

### Testy modułowe (lekcja l8 tygodnia 4)

Testy modułowe są podstawowymi narzędziami zaliczenia każdego Modułu Kursu. Są przeprowadzane jako lekcja l8 tygodnia 4 każdego Modułu. Próg zaliczenia testu modułowego wynosi 70% punktów; nie zaliczenie skutkuje powtórzeniem wybranych lekcji i poprawką.

| Narzędzie | Maksimum | Próg zaliczenia (70%) | Wynik Kursanta |
|---|---|---|---|
| Test modułowy M1 (l8 tygodnia 4 Modułu 1) | 110 punktów | 77 punktów | {{WYNIK_TEST_M1}} |
| Test modułowy M2 (l8 tygodnia 4 Modułu 2) | 40 punktów | 28 punktów | {{WYNIK_TEST_M2}} |
| Test modułowy M3 (l8 tygodnia 4 Modułu 3, równoznaczny z testem końcowym Kursu) | 108 punktów | 76 punktów | {{WYNIK_TEST_M3}} |

### Test końcowy Kursu

Test końcowy Kursu obejmuje treść wszystkich trzech Modułów w proporcji 20% / 30% / 50% i jest warunkiem dopuszczenia do egzaminu praktycznego oraz wydania zaświadczenia ukończenia Kursu. W praktyce test końcowy Kursu jest tożsamy z testem modułowym Modułu 3 (lekcja l8 tygodnia 4 Modułu 3), zatem wynik testu końcowego jest powtórzeniem wyniku z wiersza „Test modułowy M3" powyżej. Pole pozostaje w karcie jako oddzielny wpis, ponieważ niektóre cykle Kursu mogą wprowadzać dodatkowy oddzielny test końcowy z odmiennym numerem ewidencyjnym.

| Narzędzie | Identyfikator wzoru | Maksimum | Próg zaliczenia (70%) | Wynik Kursanta | Decyzja |
|---|---|---|---|---|---|
| Test końcowy Kursu | TKK-1.0/2026 | 108 punktów | 76 punktów | {{WYNIK_TKK}} | {{DECYZJA_TKK}} |

---

## Część C. Komentarz instruktora

{{KOMENTARZ_INSTRUKTORA}}

---

## Część D. Podpisy

| Strona | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Kursant (potwierdzenie odbioru karty) | {{IMIE_KURSANTA}} {{NAZWISKO_KURSANTA}} | {{DATA_GENERACJI}} | _________________ |
| Instruktor prowadzący | {{INSTRUKTOR}} | {{DATA_GENERACJI}} | _________________ |
| Koordynator Kursu | {{KOORDYNATOR_KURSU}} | {{DATA_GENERACJI}} | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru określa wersję wzoru karty postępów w postaci: KP (skrót od „Karta Postępów") - numer wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji wzoru przez Fundację.

[^2]: Numer ewidencyjny karty postępów nadaje koordynator Kursu w chwili wygenerowania karty. Numer ma postać: rok / kolejny numer w roku / KP (np. 2026/001/KP). Każdy Kursant może otrzymać kolejne karty postępów w trakcie cyklu (np. po teście modułowym M1, M2, M3 i po teście końcowym), z osobnymi numerami ewidencyjnymi i datami generacji.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji. Egzemplarz Kursanta i egzemplarz Fundacji są tożsame co do treści.*
