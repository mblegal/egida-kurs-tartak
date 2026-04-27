---
typ: protokol
dokument: protokół zakończenia cyklu Kursu (formalny dokument zamykający cykl Kursu, podstawa wydania zaświadczeń ukończenia)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O4-zamkniecie
klasa: 2
parametryzacja: CSV-DOCX
język: pl
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie działalności statutowej Fundacji
  - Ustawa z dnia 26 czerwca 1974 r. Kodeks pracy (tekst jednolity Dz.U. z 2025 r. poz. 277), w szczególności art. 94 pkt 9a w zakresie dokumentacji szkoleniowej
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO)
charakter: formalny dokument zamykający cykl Kursu; podstawa wydania zaświadczeń ukończenia Kursu (zgodnie z B1 dokumentacja kursanta) oraz przekazania akt cyklu do archiwum Fundacji
strony: koordynator Kursu (osoba sporządzająca protokół), instruktor Kursu (osoba potwierdzająca przeprowadzenie cyklu), zarząd Fundacji pomocy prawnej EGIDA (osoba zatwierdzająca protokół), Fundacja pomocy prawnej EGIDA (właściciel dokumentu)
parametry:
  - CYKL_KURSU - oznaczenie cyklu Kursu (np. C1/2026)
  - DATA_ROZPOCZECIA - data rozpoczęcia cyklu (DD-MM-RRRR)
  - DATA_ZAKONCZENIA - data zakończenia cyklu (DD-MM-RRRR)
  - LICZBA_KURSANTOW - łączna liczba Kursantów cyklu
  - LICZBA_ZALICZONYCH - liczba Kursantów zaliczających test końcowy
  - MIEJSCE_ZAJEC - główne miejsce prowadzenia zajęć (adres)
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora Kursu
  - INSTRUKTOR_GLOWNY - imię i nazwisko głównego instruktora cyklu
  - INSTRUKTORZY_LISTA - lista pozostałych instruktorów cyklu (oddzielona przecinkami)
  - LICZNA_GODZIN - łączna liczba godzin zajęć cyklu
  - UWAGI_KOORDYNATORA - uwagi koordynatora dotyczące cyklu (krótki tekst, opcjonalny)
  - NR_PROTOKOLU - numer ewidencyjny protokołu zakończenia (np. 2026/001/PZK)
  - DATA_PROTOKOLU - data sporządzenia protokołu
---

# PROTOKÓŁ ZAKOŃCZENIA CYKLU KURSU

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejszy protokół jest **formalnym dokumentem zamykającym cykl Kursu**. Podstawą sporządzenia protokołu jest zakończenie wszystkich zaplanowanych zajęć cyklu (3 Moduły × 4 tygodnie × 8 lekcji = 96 lekcji w pełnym cyklu), przeprowadzenie testu końcowego oraz wystawienie protokołów z testu końcowego (PTK) i kart postępów Kursantów (KP) wszystkim Kursantom cyklu. Protokół zakończenia jest podstawą wydania zaświadczeń ukończenia Kursu (zgodnie z dokumentacją kursanta B1) oraz przekazania akt cyklu do archiwum Fundacji.

| Identyfikator wzoru[^1] | Numer ewidencyjny protokołu[^2] | Data sporządzenia (DD-MM-RRRR) |
|---|---|---|
| PZK-1.0/2026 | {{NR_PROTOKOLU}} | {{DATA_PROTOKOLU}} |

---

## Część A. Identyfikacja cyklu

| Pole | Wartość |
|---|---|
| Cykl Kursu: | {{CYKL_KURSU}} |
| Data rozpoczęcia cyklu: | {{DATA_ROZPOCZECIA}} |
| Data zakończenia cyklu: | {{DATA_ZAKONCZENIA}} |
| Łączna liczba godzin zajęć: | {{LICZNA_GODZIN}} |
| Główne miejsce prowadzenia zajęć: | {{MIEJSCE_ZAJEC}} |

---

## Część B. Kadra cyklu

| Pole | Wartość |
|---|---|
| Koordynator Kursu: | {{KOORDYNATOR_KURSU}} |
| Główny instruktor cyklu: | {{INSTRUKTOR_GLOWNY}} |
| Pozostali instruktorzy: | {{INSTRUKTORZY_LISTA}} |

---

## Część C. Statystyka cyklu

| Wskaźnik | Wartość |
|---|---|
| Łączna liczba Kursantów cyklu: | {{LICZBA_KURSANTOW}} |
| Liczba Kursantów zaliczających test końcowy: | {{LICZBA_ZALICZONYCH}} |

---

## Część D. Potwierdzenia formalne

Niniejszym koordynator i główny instruktor cyklu **potwierdzają**, że:

1. Wszystkie zaplanowane zajęcia cyklu zostały **zrealizowane** zgodnie z harmonogramem szczegółowym (HSZ).
2. Test końcowy Kursu (TKK) został przeprowadzony i oceniony, a protokoły z testu końcowego (PTK) sporządzone dla wszystkich Kursantów cyklu.
3. Karty postępów Kursantów (KP) zostały wygenerowane i przekazane Kursantom oraz dołączone do akt cyklu.
4. Materiały operacyjne cyklu (zbiorcze karty obecności, dzienniki zajęć, listy obecności dziennej, formularze incydentalne) zostały zebrane i przygotowane do archiwizacji.
5. Wszystkie nieobecności Kursantów zostały rozliczone (usprawiedliwione albo nieusprawiedliwione) i odnotowane w zbiorczych kartach obecności.

---

## Część E. Uwagi koordynatora

{{UWAGI_KOORDYNATORA}}

---

## Część F. Podpisy

| Strona | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Koordynator Kursu | {{KOORDYNATOR_KURSU}} | {{DATA_PROTOKOLU}} | _________________ |
| Główny instruktor | {{INSTRUKTOR_GLOWNY}} | {{DATA_PROTOKOLU}} | _________________ |
| Zatwierdzający (zarząd Fundacji) | _________________ | _________________ | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru: PZK (skrót od „Protokół Zakończenia Kursu") - numer wersji - rok obowiązywania.

[^2]: Numer ewidencyjny protokołu nadaje koordynator Kursu w chwili sporządzenia. Numer ma postać: rok / kolejny numer w roku / PZK (np. 2026/001/PZK).

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji.*
