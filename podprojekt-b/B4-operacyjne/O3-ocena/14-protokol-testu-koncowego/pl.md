---
typ: protokol
dokument: protokół z przeprowadzenia testu końcowego Kursu (dokument operacyjny dokumentujący wynik testu końcowego pojedynczego Kursanta)
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
  - Ustawa z dnia 26 czerwca 1974 r. Kodeks pracy (tekst jednolity Dz.U. z 2025 r. poz. 277), w szczególności art. 94 pkt 9a w zakresie prowadzenia akt osobowych pracownika i dokumentacji szkoleniowej
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie diagnozy efektów uczenia się Kursanta
charakter: protokół operacyjny dokumentujący wynik testu końcowego Kursu pojedynczego Kursanta; podstawa decyzji o dopuszczeniu do egzaminu praktycznego i wydaniu zaświadczenia ukończenia Kursu; dokument prowadzony w języku polskim jako aktach osobowych Kursanta i archiwum Fundacji
strony: instruktor Kursu (oceniający arkusz testu), koordynator Kursu (przyjmujący protokół do akt), Kursant (osoba, której dotyczy wynik), Fundacja pomocy prawnej EGIDA (właściciel dokumentacji)
parametry:
  - IMIE_KURSANTA - imię (imiona) Kursanta
  - NAZWISKO_KURSANTA - nazwisko Kursanta
  - NR_KARTY_UCZESTNIKA - numer ewidencyjny karty uczestnika Kursanta (np. 2026/C1/001/KU)
  - CYKL_KURSU - oznaczenie cyklu Kursu (np. C1/2026)
  - DATA_TESTU - data przeprowadzenia testu końcowego w formacie DD-MM-RRRR
  - NR_TESTU - numer ewidencyjny ocenionego arkusza testu (np. 2026/001/TKK)
  - INSTRUKTOR - imię i nazwisko instruktora oceniającego arkusz testu
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora Kursu przyjmującego protokół
  - WYNIK_CZESC_1 - liczba punktów uzyskanych w Części 1 testu (pytania zamknięte, maksimum 60 punktów)
  - WYNIK_CZESC_2 - liczba punktów uzyskanych w Części 2 testu (scenariusze decyzyjne, maksimum 30 punktów)
  - WYNIK_CZESC_3 - liczba punktów uzyskanych w Części 3 testu (zadania praktyczne, maksimum 18 punktów)
  - WYNIK_LACZNY - łączna liczba punktów (maksimum 108 punktów)
  - PROCENT_LACZNY - procent uzyskanych punktów względem maksimum (np. 78%)
  - DECYZJA - decyzja o zaliczeniu testu (zaliczony albo niezaliczony)
  - UWAGI_INSTRUKTORA - uwagi instruktora dotyczące wyniku Kursanta i zaleceń (krótki tekst, opcjonalny)
  - NR_PROTOKOLU - numer ewidencyjny protokołu (np. 2026/001/PTK)
---

# PROTOKÓŁ Z PRZEPROWADZENIA TESTU KOŃCOWEGO KURSU

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejszy protokół dokumentuje wynik **testu końcowego Kursu** pojedynczego Kursanta. Test końcowy obejmuje treść wszystkich trzech Modułów Kursu (M1 Pomocnik, M2 Operator pod nadzorem, M3 Operator samodzielny) w proporcji 20% / 30% / 50% i jest warunkiem dopuszczenia do egzaminu praktycznego oraz wydania zaświadczenia ukończenia Kursu. Test składa się z trzech części: **pytania zamknięte (60 punktów)**, **scenariusze decyzyjne (30 punktów)** i **zadania praktyczne (18 punktów)**, łącznie **108 punktów** przy progu zaliczenia **70% = 76 punktów**.

Protokół jest dokumentem parametryzowanym: faktyczny protokół dla konkretnego Kursanta i konkretnego cyklu Kursu powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu (CSV) za pomocą skryptu generatora. Lista oznaczeń pól danych znajduje się w nagłówku YAML tego dokumentu w polu `parametry`.

Protokół prowadzony jest **w języku polskim**, ponieważ stanowi dokument akt osobowych Kursanta i archiwum Fundacji (zgodnie z Kodeksem pracy art. 94 pkt 9a w zakresie dokumentacji szkoleniowej).

| Identyfikator wzoru[^1] | Numer ewidencyjny protokołu[^2] | Data sporządzenia protokołu (DD-MM-RRRR) |
|---|---|---|
| PTK-1.0/2026 | {{NR_PROTOKOLU}} | {{DATA_TESTU}} |

---

## Część A. Identyfikacja Kursanta i testu

| Pole | Wartość |
|---|---|
| Imię (imiona) Kursanta: | {{IMIE_KURSANTA}} |
| Nazwisko Kursanta: | {{NAZWISKO_KURSANTA}} |
| Numer karty uczestnika Kursanta: | {{NR_KARTY_UCZESTNIKA}} |
| Cykl Kursu: | {{CYKL_KURSU}} |
| Data przeprowadzenia testu: | {{DATA_TESTU}} |
| Numer ewidencyjny ocenionego arkusza: | {{NR_TESTU}} |
| Identyfikator wzoru testu: | TKK-1.0/2026 |

---

## Część B. Rozkład punktów

| Część testu | Maksimum | Wynik Kursanta |
|---|---|---|
| Część 1 - Pytania zamknięte (30 pytań × 2 pkt) | 60 punktów | {{WYNIK_CZESC_1}} punktów |
| Część 2 - Scenariusze decyzyjne (3 scenariusze × 10 pkt) | 30 punktów | {{WYNIK_CZESC_2}} punktów |
| Część 3 - Zadania praktyczne (6 zadań × 3 pkt) | 18 punktów | {{WYNIK_CZESC_3}} punktów |
| **Razem** | **108 punktów** | **{{WYNIK_LACZNY}} punktów** |
| **Procent uzyskanych punktów** | 100% | **{{PROCENT_LACZNY}}** |
| Próg zaliczenia | 70% (76 punktów) | - |

---

## Część C. Decyzja

| Pole | Wartość |
|---|---|
| Decyzja o zaliczeniu testu końcowego: | **{{DECYZJA}}** |
| Imię i nazwisko instruktora oceniającego: | {{INSTRUKTOR}} |
| Imię i nazwisko koordynatora przyjmującego protokół: | {{KOORDYNATOR_KURSU}} |

**Skutki decyzji:**

- **W przypadku decyzji „zaliczony"**: Kursant zostaje **dopuszczony do egzaminu praktycznego** (samodzielna zmiana 8 godzin pod nadzorem komisji EGIDA, termin nie później niż 14 dni od daty testu) oraz wpisany na listę kandydatów do **wydania zaświadczenia ukończenia Kursu** (po pozytywnym wyniku egzaminu praktycznego).
- **W przypadku decyzji „niezaliczony"**: Kursant **powtarza wybrane lekcje** wskazane przez instruktora w polu „Uwagi instruktora" i **zdaje test poprawkowy** w terminie nie wcześniejszym niż 21 dni od daty testu. W okresie do testu poprawkowego Kursant pracuje w trybie M2 rozszerzonym (samodzielnie pod nadzorem M3, bez wykonywania zadań na maszynach kategorii LT70 i bez zadań nadzorczych).

---

## Część D. Uwagi instruktora

{{UWAGI_INSTRUKTORA}}

---

## Część E. Podpisy

| Strona | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Kursant | {{IMIE_KURSANTA}} {{NAZWISKO_KURSANTA}} | {{DATA_TESTU}} | _________________ |
| Instruktor oceniający | {{INSTRUKTOR}} | {{DATA_TESTU}} | _________________ |
| Koordynator przyjmujący protokół | {{KOORDYNATOR_KURSU}} | {{DATA_TESTU}} | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru określa wersję wzoru protokołu w postaci: PTK (skrót od „Protokół z Testu Końcowego") - numer wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji wzoru przez Fundację.

[^2]: Numer ewidencyjny protokołu nadaje koordynator Kursu w chwili przyjęcia protokołu do akt. Numer ma postać: rok / kolejny numer w roku / PTK (np. 2026/001/PTK). Każdy Kursant ma osobny protokół z osobnym numerem ewidencyjnym, niezależnie od decyzji o zaliczeniu albo niezaliczeniu testu.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji. Egzemplarz Kursanta i egzemplarz Fundacji są tożsame co do treści.*
