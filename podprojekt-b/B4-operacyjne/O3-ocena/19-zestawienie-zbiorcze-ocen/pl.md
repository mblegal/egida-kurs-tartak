---
typ: zestawienie
dokument: zestawienie zbiorcze ocen cyklu Kursu (sumator wyników wszystkich Kursantów cyklu w jednym dokumencie)
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
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie ewaluacji efektów uczenia się
charakter: dokument zbiorczy parametryzowany przedstawiający wyniki wszystkich Kursantów cyklu w jednym dokumencie; podstawa decyzji koordynatora i zarządu Fundacji w zakresie statystyki cyklu, sukcesów i niepowodzeń edukacyjnych; podstawa raportu końcowego edycji
strony: koordynator Kursu (osoba zestawiająca dane), instruktor Kursu (osoba weryfikująca poprawność), Fundacja pomocy prawnej EGIDA (właściciel ewidencji)
parametry:
  - CYKL_KURSU - oznaczenie cyklu Kursu (np. C1/2026)
  - DATA_GENERACJI - data wygenerowania zestawienia w formacie DD-MM-RRRR
  - LICZBA_KURSANTOW - łączna liczba Kursantów cyklu
  - LICZBA_ZALICZONYCH - liczba Kursantów, którzy zaliczyli test końcowy
  - LICZBA_NIEZALICZONYCH - liczba Kursantów, którzy nie zaliczyli testu końcowego
  - LICZBA_PRZERWANYCH - liczba Kursantów, którzy przerwali Kurs przed końcem
  - SREDNI_WYNIK_TEST_M1 - średni wynik testu modułowego M1 (X/110)
  - SREDNI_WYNIK_TEST_M2 - średni wynik testu modułowego M2 (X/40)
  - SREDNI_WYNIK_TEST_M3 - średni wynik testu modułowego M3 (X/108)
  - SREDNI_WYNIK_TKK - średni wynik testu końcowego Kursu (X/108)
  - PROCENT_ZDAWALNOSCI - procent Kursantów zaliczających test końcowy (X%)
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora Kursu
  - INSTRUKTOR_GLOWNY - imię i nazwisko głównego instruktora cyklu
  - NR_ZESTAWIENIA - numer ewidencyjny zestawienia (np. 2026/001/ZZO)
---

# ZESTAWIENIE ZBIORCZE OCEN CYKLU KURSU

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejsze zestawienie zbiorcze prezentuje **statystykę wyników wszystkich Kursantów cyklu** w jednym dokumencie. Zestawienie służy koordynatorowi i zarządowi Fundacji do oceny jakości cyklu, identyfikacji sukcesów oraz niepowodzeń edukacyjnych, a także stanowi podstawę raportu końcowego edycji (RKE-1.0/2026).

Zestawienie jest dokumentem parametryzowanym: faktyczne zestawienie dla konkretnego cyklu powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu (CSV) za pomocą skryptu generatora.

| Identyfikator wzoru[^1] | Numer ewidencyjny zestawienia[^2] | Data wygenerowania (DD-MM-RRRR) |
|---|---|---|
| ZZO-1.0/2026 | {{NR_ZESTAWIENIA}} | {{DATA_GENERACJI}} |

---

## Część A. Identyfikacja cyklu

| Pole | Wartość |
|---|---|
| Cykl Kursu: | {{CYKL_KURSU}} |
| Koordynator Kursu: | {{KOORDYNATOR_KURSU}} |
| Główny instruktor cyklu: | {{INSTRUKTOR_GLOWNY}} |

---

## Część B. Statystyka uczestnictwa

| Wskaźnik | Wartość |
|---|---|
| Łączna liczba Kursantów cyklu: | {{LICZBA_KURSANTOW}} |
| Liczba Kursantów zaliczających test końcowy: | {{LICZBA_ZALICZONYCH}} |
| Liczba Kursantów niezaliczających testu końcowego: | {{LICZBA_NIEZALICZONYCH}} |
| Liczba Kursantów, którzy przerwali Kurs: | {{LICZBA_PRZERWANYCH}} |
| **Procent zdawalności:** | **{{PROCENT_ZDAWALNOSCI}}** |

---

## Część C. Średnie wyniki narzędzi oceny

| Narzędzie | Maksimum | Średni wynik cyklu |
|---|---|---|
| Test modułowy M1 (l8 tygodnia 4 Modułu 1) | 110 punktów | {{SREDNI_WYNIK_TEST_M1}} |
| Test modułowy M2 (l8 tygodnia 4 Modułu 2) | 40 punktów | {{SREDNI_WYNIK_TEST_M2}} |
| Test modułowy M3 (l8 tygodnia 4 Modułu 3) | 108 punktów | {{SREDNI_WYNIK_TEST_M3}} |
| Test końcowy Kursu (TKK) | 108 punktów | {{SREDNI_WYNIK_TKK}} |

---

## Część D. Tabela szczegółowa wyników (wypełnia koordynator ręcznie albo przez external script)

| Lp. | Imię i nazwisko Kursanta | Test M1 | Test M2 | Test M3 | TKK | Decyzja TKK |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

(Tabela rozszerzana o dodatkowe wiersze w razie większej liczby Kursantów cyklu.)

---

## Część E. Podpisy

| Pole | Wartość |
|---|---|
| Imię i nazwisko koordynatora: | {{KOORDYNATOR_KURSU}} |
| Imię i nazwisko głównego instruktora: | {{INSTRUKTOR_GLOWNY}} |
| Data sporządzenia zestawienia: | {{DATA_GENERACJI}} |
| Podpis koordynatora: | _________________ |
| Podpis instruktora: | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru określa wersję wzoru zestawienia w postaci: ZZO (skrót od „Zestawienie Zbiorcze Ocen") - numer wersji - rok obowiązywania.

[^2]: Numer ewidencyjny zestawienia nadaje koordynator Kursu w chwili wygenerowania. Numer ma postać: rok / kolejny numer w roku / ZZO (np. 2026/001/ZZO). Każdy cykl Kursu ma osobne zestawienie zbiorcze.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji.*
