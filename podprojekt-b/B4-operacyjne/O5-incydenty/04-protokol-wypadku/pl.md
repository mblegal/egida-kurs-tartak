---
typ: protokol
dokument: protokół wypadku w trakcie zajęć Kursu (BHP) (formalny dokument dokumentujący wypadek przy pracy szkoleniowej)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O5-incydenty
klasa: 2
parametryzacja: CSV-DOCX
język: pl
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie działalności statutowej Fundacji
  - Ustawa z dnia 26 czerwca 1974 r. Kodeks pracy (tekst jednolity Dz.U. z 2025 r. poz. 277), w szczególności dział X (BHP) art. 234-237
  - Rozporządzenie Rady Ministrów z dnia 1 lipca 2009 r. w sprawie ustalania okoliczności i przyczyn wypadków przy pracy (Dz.U. nr 105 poz. 870)
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO)
charakter: formalny dokument dokumentujący wypadek (Kursanta, instruktora albo innej osoby) w trakcie zajęć Kursu praktycznego; podstawa zgłoszenia wypadku do PIP/ZUS w przypadku wymagań prawnych oraz dokumentacji ubezpieczeniowej Fundacji
strony: poszkodowany (osoba dotknięta wypadkiem), świadkowie (osoby obecne przy zdarzeniu), instruktor / brygadzista (osoba pierwszej linii), koordynator Kursu (osoba sporządzająca protokół), inspektor BHP Fundacji albo zewnętrzny (osoba weryfikująca okoliczności), zarząd Fundacji pomocy prawnej EGIDA (osoba zatwierdzająca)
parametry:
  - IMIE_POSZKODOWANEGO - imię (imiona) osoby poszkodowanej
  - NAZWISKO_POSZKODOWANEGO - nazwisko osoby poszkodowanej
  - ROLA_POSZKODOWANEGO - rola osoby (Kursant / instruktor / inny)
  - DATA_WYPADKU - data wypadku (DD-MM-RRRR)
  - GODZINA_WYPADKU - godzina wypadku (HH:MM)
  - MIEJSCE_WYPADKU - dokładne miejsce wypadku (sala szkoleniowa albo konkretne stanowisko w tartaku)
  - OPIS_ZDARZENIA - krótki opis przebiegu zdarzenia (3-5 zdań)
  - RODZAJ_OBRAZEN - rodzaj i miejsce obrażeń (jeżeli wystąpiły)
  - PIERWSZA_POMOC - kto i jaką pierwszą pomoc udzielił
  - WEZWANE_SLUZBY - czy wezwano służby (pogotowie, straż pożarna, policja) i o której godzinie
  - SWIADKOWIE_LISTA - lista świadków zdarzenia (imiona i nazwiska, oddzielone przecinkami)
  - INSTRUKTOR_PIERWSZEJ_LINII - instruktor albo brygadzista obecny przy zdarzeniu
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora Kursu
  - DATA_PROTOKOLU - data sporządzenia protokołu
  - NR_PROTOKOLU - numer ewidencyjny protokołu wypadku (np. 2026/001/PW)
---

# PROTOKÓŁ WYPADKU W TRAKCIE ZAJĘĆ KURSU

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejszy protokół dokumentuje **wypadek w trakcie zajęć Kursu** dotyczący Kursanta, instruktora albo innej osoby obecnej na zajęciach. Protokół jest sporządzany niezwłocznie po zdarzeniu (najpóźniej w ciągu 24 godzin) przez koordynatora Kursu na podstawie informacji od poszkodowanego, świadków i instruktora pierwszej linii. Protokół jest podstawą zgłoszenia wypadku do PIP albo ZUS w przypadku wymagań prawnych oraz dokumentacji ubezpieczeniowej Fundacji.

| Identyfikator wzoru[^1] | Numer ewidencyjny protokołu[^2] | Data sporządzenia (DD-MM-RRRR) |
|---|---|---|
| PW-1.0/2026 | {{NR_PROTOKOLU}} | {{DATA_PROTOKOLU}} |

---

## Część A. Identyfikacja poszkodowanego

| Pole | Wartość |
|---|---|
| Imię i nazwisko poszkodowanego: | {{IMIE_POSZKODOWANEGO}} {{NAZWISKO_POSZKODOWANEGO}} |
| Rola w cyklu: | {{ROLA_POSZKODOWANEGO}} |

---

## Część B. Okoliczności wypadku

| Pole | Wartość |
|---|---|
| Data wypadku: | {{DATA_WYPADKU}} |
| Godzina wypadku: | {{GODZINA_WYPADKU}} |
| Miejsce wypadku: | {{MIEJSCE_WYPADKU}} |
| Instruktor pierwszej linii: | {{INSTRUKTOR_PIERWSZEJ_LINII}} |
| Świadkowie zdarzenia: | {{SWIADKOWIE_LISTA}} |

---

## Część C. Przebieg zdarzenia

{{OPIS_ZDARZENIA}}

---

## Część D. Skutki wypadku

| Pole | Wartość |
|---|---|
| Rodzaj i miejsce obrażeń: | {{RODZAJ_OBRAZEN}} |
| Pierwsza pomoc (kto, jaka): | {{PIERWSZA_POMOC}} |
| Wezwane służby (pogotowie, straż, policja, godzina): | {{WEZWANE_SLUZBY}} |

---

## Część E. Środki zaradcze (wypełnia koordynator po zdarzeniu)

**1. Co zostało zrobione bezpośrednio po wypadku?**



**2. Jakie środki zapobiegawcze zostaną wprowadzone, aby zapobiec podobnym zdarzeniom?**



**3. Czy konieczna jest aktualizacja procedur BHP, programu Kursu albo materiałów dydaktycznych?**



---

## Część F. Zgłoszenia zewnętrzne (wypełnia koordynator)

| Pole | Wartość |
|---|---|
| Czy wypadek zgłoszony do PIP? (tak/nie/nie dotyczy): | |
| Numer zgłoszenia PIP (jeżeli dotyczy): | |
| Czy wypadek zgłoszony do ZUS? (tak/nie/nie dotyczy): | |
| Numer zgłoszenia ZUS (jeżeli dotyczy): | |
| Czy wypadek zgłoszony ubezpieczycielowi Fundacji? (tak/nie): | |
| Data zgłoszenia ubezpieczycielowi: | |

---

## Część G. Podpisy

| Strona | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Poszkodowany (jeżeli zdolny do podpisu) | {{IMIE_POSZKODOWANEGO}} {{NAZWISKO_POSZKODOWANEGO}} | {{DATA_PROTOKOLU}} | _________________ |
| Instruktor pierwszej linii | {{INSTRUKTOR_PIERWSZEJ_LINII}} | {{DATA_PROTOKOLU}} | _________________ |
| Koordynator Kursu | {{KOORDYNATOR_KURSU}} | {{DATA_PROTOKOLU}} | _________________ |
| Inspektor BHP (Fundacji albo zewnętrzny) | _________________ | _________________ | _________________ |
| Zatwierdzający (zarząd Fundacji) | _________________ | _________________ | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru: PW (skrót od „Protokół Wypadku") - numer wersji - rok obowiązywania.

[^2]: Numer ewidencyjny protokołu nadaje koordynator Kursu w chwili sporządzenia dokumentu. Numer ma postać: rok / kolejny numer w roku / PW (np. 2026/001/PW). Każdy wypadek ma osobny numer ewidencyjny niezależnie od skutków.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji.*
