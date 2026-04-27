---
typ: karta edycji
dokument: karta edycji cyklu Kursu (master record cyklu, jeden dokument zbiorczy zawierający wszystkie kluczowe parametry edycji)
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
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO)
charakter: master record cyklu Kursu; jeden dokument zbiorczy zawierający kluczowe parametry edycji w pigułce (kadra, harmonogram, miejsce, statystyki); pierwszy dokument otwierany przy zapytaniach zewnętrznych o cykl Kursu i przy archiwizacji
strony: koordynator Kursu (osoba prowadząca kartę), zarząd Fundacji pomocy prawnej EGIDA (osoba zatwierdzająca), Fundacja pomocy prawnej EGIDA (właściciel dokumentu)
parametry:
  - CYKL_KURSU - oznaczenie cyklu (np. C1/2026)
  - DATA_OTWARCIA_KARTY - data otwarcia karty (DD-MM-RRRR)
  - DATA_ZAMKNIECIA_KARTY - data zamknięcia karty
  - DATA_ROZPOCZECIA_CYKLU - data pierwszej lekcji cyklu
  - DATA_ZAKONCZENIA_CYKLU - data ostatniej lekcji cyklu
  - MIEJSCE_GLOWNE - główne miejsce zajęć (adres)
  - MIEJSCE_PRAKTYK - miejsce zajęć praktycznych (tartak partnerski)
  - LICZBA_KURSANTOW_REKRUTOWANYCH - liczba Kursantów zrekrutowanych
  - LICZBA_KURSANTOW_KONCZACYCH - liczba Kursantów ukończywszych cykl (zaliczonych albo nie)
  - LICZBA_ABSOLWENTOW - liczba absolwentów cyklu
  - LICZNA_GODZIN - łączna liczba godzin zajęć cyklu
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora
  - INSTRUKTOR_GLOWNY - imię i nazwisko głównego instruktora
  - INSTRUKTORZY_LISTA - lista pozostałych instruktorów
  - NR_KARTY_EDYCJI - numer ewidencyjny karty edycji (np. 2026/001/KEK)
---

# KARTA EDYCJI CYKLU KURSU

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejsza karta edycji jest **master recordem cyklu Kursu**: jednym dokumentem zbiorczym zawierającym kluczowe parametry edycji w pigułce. Karta jest pierwszym dokumentem otwieranym przy zapytaniach zewnętrznych o cykl Kursu (np. od pracodawców, organów kontrolnych, sponsora, członków zarządu Fundacji) oraz przy archiwizacji akt cyklu.

| Identyfikator wzoru[^1] | Numer ewidencyjny karty edycji[^2] | Data wygenerowania (DD-MM-RRRR) |
|---|---|---|
| KEK-1.0/2026 | {{NR_KARTY_EDYCJI}} | {{DATA_ZAMKNIECIA_KARTY}} |

---

## Część A. Cykl Kursu

| Pole | Wartość |
|---|---|
| Cykl Kursu: | {{CYKL_KURSU}} |
| Data otwarcia karty: | {{DATA_OTWARCIA_KARTY}} |
| Data zamknięcia karty: | {{DATA_ZAMKNIECIA_KARTY}} |
| Data rozpoczęcia cyklu (pierwsza lekcja): | {{DATA_ROZPOCZECIA_CYKLU}} |
| Data zakończenia cyklu (ostatnia lekcja): | {{DATA_ZAKONCZENIA_CYKLU}} |
| Łączna liczba godzin zajęć: | {{LICZNA_GODZIN}} |

---

## Część B. Miejsce realizacji

| Pole | Wartość |
|---|---|
| Główne miejsce zajęć teoretycznych: | {{MIEJSCE_GLOWNE}} |
| Miejsce zajęć praktycznych: | {{MIEJSCE_PRAKTYK}} |

---

## Część C. Kadra cyklu

| Pole | Wartość |
|---|---|
| Koordynator Kursu: | {{KOORDYNATOR_KURSU}} |
| Główny instruktor cyklu: | {{INSTRUKTOR_GLOWNY}} |
| Pozostali instruktorzy: | {{INSTRUKTORZY_LISTA}} |

---

## Część D. Statystyka uczestnictwa

| Wskaźnik | Wartość |
|---|---|
| Liczba Kursantów zrekrutowanych do cyklu: | {{LICZBA_KURSANTOW_REKRUTOWANYCH}} |
| Liczba Kursantów kończących cykl: | {{LICZBA_KURSANTOW_KONCZACYCH}} |
| Liczba absolwentów cyklu (zaliczających TKK): | {{LICZBA_ABSOLWENTOW}} |

---

## Część E. Linki do dokumentów cyklu

(Wypełnia koordynator po zamknięciu cyklu - lista numerów ewidencyjnych dokumentów archiwizowanych dla cyklu.)

| Dokument | Numer ewidencyjny |
|---|---|
| Harmonogram szczegółowy cyklu (HSZ) | |
| Lista zakwalifikowanych (LK) | |
| Protokół zakończenia cyklu (PZK) | |
| Zestawienie zbiorcze ocen (ZZO) | |
| Lista absolwentów (LA) | |
| Rejestr wydanych zaświadczeń (RWZ) | |
| Raport końcowy edycji (RKE) | |
| Spis dokumentacji edycji (SDE) | |

---

## Część F. Podpisy

| Pole | Wartość |
|---|---|
| Koordynator Kursu: | {{KOORDYNATOR_KURSU}} |
| Data zamknięcia karty: | {{DATA_ZAMKNIECIA_KARTY}} |
| Podpis koordynatora: | _________________ |
| Zatwierdzający (zarząd Fundacji): | _________________ |
| Podpis zatwierdzającego: | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru: KEK (skrót od „Karta Edycji Kursu") - numer wersji - rok obowiązywania.

[^2]: Numer ewidencyjny karty edycji nadaje koordynator Kursu w chwili otwarcia cyklu (przed pierwszą lekcją). Numer ma postać: rok / kolejny numer w roku / KEK (np. 2026/001/KEK). Każdy cykl Kursu ma osobną kartę edycji.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji.*
