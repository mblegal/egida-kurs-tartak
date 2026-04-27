---
typ: skreslenie
dokument: skreślenie Kursanta z listy uczestników Kursu (formalny dokument zamykający uczestnictwo Kursanta przed zakończeniem cyklu)
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
  - Regulamin Kursu praktycznego „Praca w tartaku" Fundacji pomocy prawnej EGIDA (przesłanki skreślenia z listy)
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO)
charakter: formalny dokument zamykający uczestnictwo Kursanta przed zakończeniem cyklu Kursu z przyczyn rezygnacji Kursanta albo decyzji Fundacji (przekroczenie progu nieobecności, naruszenie regulaminu, niespełnienie warunków kwalifikacji)
strony: koordynator Kursu (osoba sporządzająca dokument), Kursant (osoba skreślona z listy), zarząd Fundacji pomocy prawnej EGIDA (osoba zatwierdzająca w przypadku skreślenia z inicjatywy Fundacji), Fundacja pomocy prawnej EGIDA (właściciel dokumentu)
parametry:
  - IMIE_KURSANTA - imię (imiona) Kursanta
  - NAZWISKO_KURSANTA - nazwisko Kursanta
  - NR_KARTY_UCZESTNIKA - numer karty uczestnika Kursanta
  - CYKL_KURSU - oznaczenie cyklu Kursu
  - DATA_SKRESLENIA - data skreślenia (DD-MM-RRRR)
  - PRZYCZYNA_SKRESLENIA - krótki opis przyczyny skreślenia (1-3 zdania)
  - INICJATOR_SKRESLENIA - kto zainicjował skreślenie (Kursant albo Fundacja)
  - PROCENT_UKONCZENIA - jaki procent cyklu Kursant ukończył (X%)
  - WYDANE_ZASWIADCZENIA - lista wydanych zaświadczeń modułowych (jeżeli ukończył M1 albo M2)
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora
  - NR_SKRESLENIA - numer ewidencyjny skreślenia (np. 2026/001/SL)
---

# SKREŚLENIE Z LISTY UCZESTNIKÓW KURSU

**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie przez Fundację pomocy prawnej EGIDA.

---

## Informacja wstępna

Niniejszy dokument formalizuje **skreślenie Kursanta z listy uczestników cyklu Kursu** przed jego zakończeniem. Skreślenie może mieć dwie przyczyny: (1) **z inicjatywy Kursanta** (rezygnacja z udziału), albo (2) **z inicjatywy Fundacji** (przekroczenie progu nieobecności określonego w Regulaminie, naruszenie zasad bezpieczeństwa, niespełnienie warunków kwalifikacji ujawnione w trakcie Kursu, naruszenie postanowień regulaminu Kursu). Skreślenie z inicjatywy Fundacji wymaga zatwierdzenia zarządu Fundacji.

Po skreśleniu Kursant otrzymuje wydane wcześniej zaświadczenia modułowe (jeżeli ukończył co najmniej Moduł 1 albo Moduł 2), nie otrzymuje natomiast zaświadczenia ukończenia Kursu.

| Identyfikator wzoru[^1] | Numer ewidencyjny skreślenia[^2] | Data sporządzenia (DD-MM-RRRR) |
|---|---|---|
| SL-1.0/2026 | {{NR_SKRESLENIA}} | {{DATA_SKRESLENIA}} |

---

## Część A. Identyfikacja Kursanta

| Pole | Wartość |
|---|---|
| Imię i nazwisko Kursanta: | {{IMIE_KURSANTA}} {{NAZWISKO_KURSANTA}} |
| Numer karty uczestnika: | {{NR_KARTY_UCZESTNIKA}} |
| Cykl Kursu: | {{CYKL_KURSU}} |
| Procent ukończonego cyklu: | {{PROCENT_UKONCZENIA}} |

---

## Część B. Przyczyna skreślenia

| Pole | Wartość |
|---|---|
| Inicjator skreślenia: | {{INICJATOR_SKRESLENIA}} |
| Data skreślenia: | {{DATA_SKRESLENIA}} |
| Przyczyna: | {{PRZYCZYNA_SKRESLENIA}} |

---

## Część C. Wydane zaświadczenia (zachowywane przez Kursanta)

| Pole | Wartość |
|---|---|
| Wydane zaświadczenia modułowe: | {{WYDANE_ZASWIADCZENIA}} |

---

## Część D. Skutki skreślenia

1. Kursant traci status uczestnika cyklu Kursu z datą skreślenia wskazaną w polu „Data skreślenia".
2. Kursant nie otrzymuje zaświadczenia ukończenia Kursu (B1) ze względu na przerwanie cyklu.
3. Wydane wcześniej zaświadczenia modułowe (jeżeli dotyczy) **zachowują ważność**: Kursant zachowuje je w swoich aktach jako dowód ukończenia konkretnego Modułu.
4. W przypadku ponownego ubiegania się Kursanta o udział w kolejnym cyklu Kursu Kursant przechodzi standardową procedurę rekrutacji z B-OP-1.
5. Akta Kursanta w cyklu są archiwizowane wraz z aktami całego cyklu zgodnie z Regulaminem Kursu i polityką archiwalną Fundacji.

---

## Część E. Podpisy

| Strona | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Kursant (potwierdzenie odbioru dokumentu) | {{IMIE_KURSANTA}} {{NAZWISKO_KURSANTA}} | {{DATA_SKRESLENIA}} | _________________ |
| Koordynator Kursu | {{KOORDYNATOR_KURSU}} | {{DATA_SKRESLENIA}} | _________________ |
| Zatwierdzający (zarząd Fundacji, jeżeli skreślenie z inicjatywy Fundacji) | _________________ | _________________ | _________________ |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru: SL (skrót od „Skreślenie z Listy") - numer wersji - rok obowiązywania.

[^2]: Numer ewidencyjny skreślenia nadaje koordynator Kursu w chwili sporządzenia dokumentu. Numer ma postać: rok / kolejny numer w roku / SL (np. 2026/001/SL). Każde skreślenie ma osobny numer ewidencyjny.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną kontrolą wersji.*
