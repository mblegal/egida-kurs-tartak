---
typ: karta odpowiedzi
dokument: karta odpowiedzi do quizu uzupełniającego Modułu Kursu (uniwersalna karta wypełniana przez Kursanta)
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
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie diagnozy efektów uczenia się Kursanta
charakter: uniwersalny formularz odpowiedzi wypełniany ręcznie przez Kursanta podczas quizu uzupełniającego dowolnego z trzech Modułów Kursu; karta wypełniana w obecności instruktora albo koordynatora i przekazywana do oceny
strony: Kursant (wypełniający kartę), instruktor Kursu (oceniający arkusz), Fundacja pomocy prawnej EGIDA (autor i właściciel wzoru)
parametry:
  - IMIE_KURSANTA - imię (imiona) Kursanta
  - NAZWISKO_KURSANTA - nazwisko Kursanta
  - NR_KARTY - numer ewidencyjny karty odpowiedzi (np. 2026/C1/001/KO)
  - KOD_QUIZU - identyfikator quizu, do którego karta jest dołączana (np. QUM-M1-1.0/2026)
  - NUMER_MODULU - numer Modułu, którego dotyczy quiz (1, 2 albo 3)
  - TRYB_QUIZU - tryb przeprowadzenia quizu (samoocena albo poprawkowy)
  - DATA_QUIZU - data wypełnienia karty w formacie DD-MM-RRRR
  - CYKL_KURSU - oznaczenie cyklu Kursu, w którym Kursant uczestniczy (np. C1/2026)
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora albo instruktora przyjmującego kartę
  - LICZBA_ZAMKNIETYCH - liczba pytań zamkniętych w quizie (np. 15 dla M1, 30 dla M2, 15 dla M3)
  - LICZBA_OTWARTYCH - liczba pytań otwartych w quizie (np. 0 dla M1, 15 dla M2, 0 dla M3)
  - LICZBA_CASEOW - liczba pytań typu case w quizie (np. 0 dla M1, 10 dla M2, 0 dla M3)
  - CZAS_TRWANIA_MIN - przewidywany czas wypełniania karty w minutach (np. 30 dla M1, 120 dla M2, 60 dla M3)
---

# KARTA ODPOWIEDZI DO QUIZU UZUPEŁNIAJĄCEGO

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejsza karta odpowiedzi służy do udokumentowania odpowiedzi Kursanta na pytania quizu uzupełniającego dowolnego z trzech Modułów Kursu. Karta jest **uniwersalna**: zawiera trzy części odpowiadające trzem typom pytań występujących w quizach Modułów (zamknięte, otwarte, case'y). Kursant wypełnia tylko te części, które odpowiadają strukturze quizu, do którego karta jest dołączana - liczba pytań w każdej części jest podana w nagłówku karty (pole „Liczba pytań w quizie"). Pozostałe wiersze albo pola zostawia się niewypełnione.

Karta wypełniana jest **samodzielnie**, długopisem albo ołówkiem, w obecności koordynatora albo instruktora Kursu. Korzystanie z notatek, podręczników, telefonu, komputera albo z pomocy innych osób jest niedozwolone. Czas wypełniania karty wskazany jest w nagłówku karty (pole „Czas trwania quizu"). Po upływie czasu Kursant kończy wypełnianie i oddaje kartę.

Karta jest dokumentem parametryzowanym: faktyczna karta dla konkretnego Kursanta i konkretnego cyklu Kursu powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu (CSV) za pomocą skryptu generatora. Lista oznaczeń pól danych znajduje się w nagłówku YAML tego dokumentu w polu `parametry`.

| Identyfikator wzoru[^1] | Numer ewidencyjny karty[^2] | Data wypełnienia karty (DD-MM-RRRR) |
|--------------------------|------------------------------|--------------------------------------|
| KO-1.0/2026              | {{NR_KARTY}}                 | {{DATA_QUIZU}}                       |

---

## Część A. Identyfikacja Kursanta i quizu

| Pole | Wartość |
|------|---------|
| Imię (imiona) Kursanta: | {{IMIE_KURSANTA}} |
| Nazwisko Kursanta: | {{NAZWISKO_KURSANTA}} |
| Cykl Kursu: | {{CYKL_KURSU}} |
| Numer Modułu, którego dotyczy quiz: | {{NUMER_MODULU}} |
| Identyfikator quizu (kod wzoru): | {{KOD_QUIZU}} |
| Tryb quizu: | {{TRYB_QUIZU}} |
| Czas trwania quizu (w minutach): | {{CZAS_TRWANIA_MIN}} |

### Liczba pytań w quizie (informacja dla Kursanta)

| Część karty | Typ pytań | Liczba pytań w tym quizie |
|-------------|-----------|----------------------------|
| Część B | pytania zamknięte (A/B/C/D, jedna poprawna) | {{LICZBA_ZAMKNIETYCH}} |
| Część C | pytania otwarte (odpowiedź 1-3 zdania) | {{LICZBA_OTWARTYCH}} |
| Część D | pytania typu case (analiza 4-6 zdań) | {{LICZBA_CASEOW}} |

Wypełniaj tylko wiersze odpowiadające faktycznej liczbie pytań w quizie. Wiersze ponad tę liczbę zostaw niewypełnione albo przekreśl ukośnikiem.

---

## Część B. Odpowiedzi na pytania zamknięte

W każdym wierszu zaznacz **jedną** odpowiedź (A, B, C albo D) przez postawienie znaku × w odpowiedniej kratce. Jeżeli nie znasz odpowiedzi, zaznacz „nie wiem". Jeżeli quiz wymaga uzasadnienia odpowiedzi (Moduł 3), uzasadnienie wpisz w kolumnie „Uzasadnienie" w 2-3 zdaniach.

| Numer pytania | A | B | C | D | nie wiem | Uzasadnienie (jeżeli wymagane) |
|---------------|---|---|---|---|----------|--------------------------------|
| 1  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 2  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 3  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 4  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 5  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 6  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 7  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 8  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 9  | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 10 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 11 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 12 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 13 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 14 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 15 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 16 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 17 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 18 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 19 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 20 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 21 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 22 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 23 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 24 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 25 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 26 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 27 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 28 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 29 | ☐ | ☐ | ☐ | ☐ | ☐ |  |
| 30 | ☐ | ☐ | ☐ | ☐ | ☐ |  |

---

## Część C. Odpowiedzi na pytania otwarte

W każdym polu wpisz odpowiedź na pytanie o numerze wskazanym po lewej stronie. Odpowiedź powinna mieć **1-3 zdania**. Jeżeli nie znasz odpowiedzi, wpisz „nie wiem".

**Pytanie otwarte 1**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 2**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 3**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 4**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 5**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 6**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 7**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 8**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 9**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 10**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 11**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 12**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 13**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 14**

|  |
|--|
|  |
|  |
|  |

**Pytanie otwarte 15**

|  |
|--|
|  |
|  |
|  |

---

## Część D. Odpowiedzi na pytania typu case

W każdym polu wpisz analizę sytuacji opisanej w pytaniu o numerze wskazanym po lewej stronie. Analiza powinna mieć **4-6 zdań** i zawierać: opis problemu z perspektywy Kursanta, wskazanie zastosowanych zasad albo przepisów, propozycję działania.

**Case 1**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 2**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 3**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 4**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 5**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 6**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 7**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 8**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 9**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Case 10**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

---

## Część E. Oświadczenie Kursanta

Niniejszym oświadczam, że kartę odpowiedzi wypełniłem (wypełniłam) samodzielnie, bez korzystania z notatek, podręczników, telefonu, komputera ani z pomocy innych osób. Wpisane odpowiedzi są moimi własnymi odpowiedziami. Rozumiem, że karta zostanie przekazana do oceny przez instruktora Kursu na podstawie klucza odpowiedzi obowiązującego dla danego quizu.

| Pole | Wartość |
|------|---------|
| Data wypełnienia karty (DD-MM-RRRR): | {{DATA_QUIZU}} |
| Własnoręczny podpis Kursanta: |  |

---

## Część F. Przyjęcie karty przez koordynatora albo instruktora

| Pole | Wartość |
|------|---------|
| Data odbioru karty (DD-MM-RRRR): | {{DATA_QUIZU}} |
| Imię i nazwisko koordynatora albo instruktora przyjmującego kartę: | {{KOORDYNATOR_KURSU}} |
| Własnoręczny podpis koordynatora albo instruktora: |  |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru określa wersję wzoru karty odpowiedzi w postaci: KO (skrót od „karta odpowiedzi") - numer wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji wzoru przez Fundację. Karta jest uniwersalna dla wszystkich trzech Modułów Kursu i wszystkich trybów quizu (samoocena, poprawkowy).

[^2]: Numer ewidencyjny karty nadaje koordynator Kursu w chwili odbioru wypełnionej karty od Kursanta. Numer ma postać: rok / oznaczenie cyklu / numer kolejny w cyklu / KO (np. 2026/C1/001/KO). Numer powiązany jest jednoznacznie z numerem Karty uczestnika Kursanta i z identyfikatorem quizu.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór parametryzowany; faktyczna karta odpowiedzi powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu. Karta po wypełnieniu i przekazaniu do oceny stanowi dokument operacyjny Kursu i podlega archiwizacji wraz z pozostałą dokumentacją cyklu.*
