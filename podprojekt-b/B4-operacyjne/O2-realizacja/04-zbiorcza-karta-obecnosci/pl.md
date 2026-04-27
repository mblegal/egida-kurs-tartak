---
typ: karta
dokument: zbiorcza karta obecności Kursanta (kumulatywne podsumowanie obecności na wszystkich sesjach cyklu)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O2-realizacja
klasa: 2
parametryzacja: CSV-DOCX
język: pl
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie dokumentowania działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. b oraz lit. f w zakresie informacji zwrotnej Kursantowi o jego frekwencji
charakter: dokument indywidualny per Kursant; kumulatywne zestawienie obecności na wszystkich sesjach cyklu Kursu; pełni rolę informacji zwrotnej dla Kursanta i podstawy decyzji o dopuszczeniu do testu końcowego
strony: Kursant (adresat informacji o frekwencji), Fundacja pomocy prawnej EGIDA (sporządzający i właściciel rejestru)
parametry:
  - IMIE_KURSANTA - imię (imiona) Kursanta
  - NAZWISKO_KURSANTA - nazwisko Kursanta
  - NR_KARTY_UCZESTNIKA - numer ewidencyjny powiązanej Karty uczestnika (KU)
  - NR_FORMULARZA - numer ewidencyjny Formularza rekrutacyjnego
  - CYKL_KURSU - oznaczenie cyklu Kursu
  - MODUL_GLOWNY - moduł, w którym Kursant uczestniczy (M1, M2, M3)
  - DATA_OTWARCIA_KARTY - data otwarcia karty (zazwyczaj data pierwszej sesji)
  - DATA_ZAMKNIECIA_KARTY - data zamknięcia karty (zazwyczaj data ostatniej sesji)
  - LACZNA_LICZBA_SESJI - łączna liczba sesji w cyklu na dzień zamknięcia karty
  - LICZBA_SESJI_OBECNYCH - liczba sesji, na których Kursant był obecny
  - FREKWENCJA_PROCENTOWA - frekwencja Kursanta w procentach
  - PROG_FREKWENCJI_REGULAMIN - próg frekwencji wymagany Regulaminem Kursu (np. 80%)
  - DECYZJA_DOPUSZCZENIA - decyzja o dopuszczeniu Kursanta do testu końcowego (tak / nie / warunkowo)
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora podpisującego kartę
  - NR_KARTY_OBECNOSCI - numer ewidencyjny zbiorczej karty obecności (np. 2026/C1/001/ZKO)
---

# ZBIORCZA KARTA OBECNOŚCI KURSANTA

**Kumulatywne zestawienie obecności Kursanta na wszystkich sesjach cyklu Kursu praktycznego „Praca w tartaku".** Karta sporządzana jest indywidualnie dla każdego Kursanta przez koordynatora Kursu na podstawie list obecności dziennych. Karta wydawana jest Kursantowi w odpisie po zamknięciu cyklu jako informacja zwrotna o jego frekwencji oraz dołączana do akt Kursanta.

---

## Informacja wstępna

Zbiorcza karta obecności pełni dwie funkcje:

a) **wewnętrzną** - stanowi podstawę decyzji koordynatora Kursu o dopuszczeniu Kursanta do testu końcowego oraz, dalej, do wystawienia zaświadczenia o ukończeniu Kursu, zgodnie z progiem frekwencji określonym w Regulaminie Kursu;

b) **zewnętrzną** - stanowi informację zwrotną dla Kursanta o jego rzeczywistej frekwencji, wydawaną mu w odpisie zgodnie z prawem dostępu Kursanta do własnych danych osobowych przetwarzanych przez Fundację.

Karta sporządzana jest po każdej sesji aktualizacją siatki frekwencji oraz na zakończenie cyklu sumarycznym podsumowaniem.

| Identyfikator wzoru[^1] | Numer ewidencyjny karty[^2] | Cykl Kursu | Powiązana Karta uczestnika |
|--------------------------|------------------------------|------------|------------------------------|
| ZKO-1.0/2026             | {{NR_KARTY_OBECNOSCI}}       | {{CYKL_KURSU}} | {{NR_KARTY_UCZESTNIKA}}   |

---

## Część A. Identyfikacja Kursanta

| Pole | Wartość |
|------|---------|
| Imię (imiona): | {{IMIE_KURSANTA}} |
| Nazwisko: | {{NAZWISKO_KURSANTA}} |
| Numer ewidencyjny Formularza rekrutacyjnego: | {{NR_FORMULARZA}} |
| Numer ewidencyjny powiązanej Karty uczestnika: | {{NR_KARTY_UCZESTNIKA}} |
| Cykl Kursu: | {{CYKL_KURSU}} |
| Moduł, w którym Kursant uczestniczy: | {{MODUL_GLOWNY}} |
| Data otwarcia karty (DD-MM-RRRR): | {{DATA_OTWARCIA_KARTY}} |

---

## Część B. Siatka frekwencji per sesja

Każdy wiersz tabeli odpowiada pojedynczej sesji cyklu, w kolejności chronologicznej zgodnej z Harmonogramem szczegółowym. W kolumnie „Obecność" zaznacza się jedno z oznaczeń: **+** (obecny), **-** (nieobecny nieusprawiedliwiony), **U** (nieobecny usprawiedliwiony), **S** (spóźnienie istotne powyżej 15 minut), **W** (wyjście przed końcem sesji).

| Lp. sesji | Data sesji (DD-MM-RRRR) | Moduł | Tytuł sesji | Obecność | Numer Listy obecności (LO) |
|-----------|--------------------------|-------|--------------|-----------|------------------------------|
| 1   |  |  |  |  |  |
| 2   |  |  |  |  |  |
| 3   |  |  |  |  |  |
| 4   |  |  |  |  |  |
| 5   |  |  |  |  |  |
| 6   |  |  |  |  |  |
| 7   |  |  |  |  |  |
| 8   |  |  |  |  |  |
| 9   |  |  |  |  |  |
| 10  |  |  |  |  |  |
| 11  |  |  |  |  |  |
| 12  |  |  |  |  |  |
| 13  |  |  |  |  |  |
| 14  |  |  |  |  |  |
| 15  |  |  |  |  |  |
| 16  |  |  |  |  |  |
| 17  |  |  |  |  |  |
| 18  |  |  |  |  |  |
| 19  |  |  |  |  |  |
| 20  |  |  |  |  |  |
| 21  |  |  |  |  |  |
| 22  |  |  |  |  |  |
| 23  |  |  |  |  |  |
| 24  |  |  |  |  |  |

---

## Część C. Podsumowanie liczbowe (wypełnia koordynator po zamknięciu cyklu)

### C.1. Frekwencja per moduł

| Moduł | Liczba sesji w module | Liczba sesji obecnych | Liczba sesji nieobecnych usprawiedliwionych | Liczba sesji nieobecnych nieusprawiedliwionych | Frekwencja procentowa |
|-------|------------------------|------------------------|----------------------------------------------|------------------------------------------------|------------------------|
| M1 |  |  |  |  |  |
| M2 |  |  |  |  |  |
| M3 |  |  |  |  |  |
| **Razem** | {{LACZNA_LICZBA_SESJI}} | {{LICZBA_SESJI_OBECNYCH}} |  |  | {{FREKWENCJA_PROCENTOWA}} |

### C.2. Próg frekwencji wymagany Regulaminem Kursu

| Pole | Wartość |
|------|---------|
| Próg frekwencji określony w pkt VII Regulaminu Kursu (procentowo): | {{PROG_FREKWENCJI_REGULAMIN}} |
| Czy frekwencja Kursanta osiągnęła próg: | ☐ tak ☐ nie ☐ zachodzą okoliczności szczególne (opisać niżej) |
| Opis okoliczności szczególnych (jeżeli dotyczy): |  |

---

## Część D. Decyzja o dopuszczeniu do testu końcowego

| Pole | Wartość |
|------|---------|
| Decyzja koordynatora: | {{DECYZJA_DOPUSZCZENIA}} |
| Krótkie uzasadnienie decyzji: |  |
| Data wydania decyzji (DD-MM-RRRR): |  |
| Imię i nazwisko koordynatora wydającego decyzję: | {{KOORDYNATOR_KURSU}} |
| Własnoręczny podpis koordynatora: |  |

---

## Część E. Wydanie odpisu Kursantowi

| Pole | Wartość |
|------|---------|
| Data zamknięcia karty (DD-MM-RRRR): | {{DATA_ZAMKNIECIA_KARTY}} |
| Data wydania odpisu Kursantowi (DD-MM-RRRR): |  |
| Sposób wydania odpisu: | ☐ osobiście za pokwitowaniem ☐ przesyłką pocztową ☐ drogą elektroniczną zgodnie z Umową kursu |
| Adnotacja Kursanta o odbiorze odpisu (jeżeli wydano osobiście): |  |
| Własnoręczny podpis Kursanta przy odbiorze odpisu (jeżeli wydano osobiście): |  |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru określa wersję wzoru zbiorczej karty obecności w postaci: ZKO (skrót od „zbiorcza karta obecności") - numer wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji wzoru przez Fundację.

[^2]: Numer ewidencyjny zbiorczej karty obecności nadaje koordynator Kursu w chwili otwarcia karty (zazwyczaj w dniu pierwszej sesji cyklu). Numer ma postać: rok / oznaczenie cyklu / numer kolejny w cyklu / ZKO (np. 2026/C1/001/ZKO). Numer powinien odpowiadać numerowi powiązanej Karty uczestnika (z zachowaniem różnego sufiksu KU albo ZKO).

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór parametryzowany; faktyczna karta powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu i wpisanie obecności w części B. Zbiorcza karta obecności wydawana jest Kursantowi w odpisie po zamknięciu cyklu.*
