---
typ: karta
dokument: karta uczestnika Kursu (zbiorczy rekord administracyjny per Kursant)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O1-wejście
klasa: 2
parametryzacja: CSV-DOCX
język: pl
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie dokumentowania działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. b oraz lit. f w zakresie prowadzenia ewidencji uczestnictwa Kursanta w Kursie
charakter: zbiorczy rekord administracyjny pojedynczego Kursanta, wiążący odsyłaczami wszystkie dokumenty operacyjne Kursu dotyczące tego Kursanta; karta otwierana w chwili kwalifikacji kandydata, zamykana w chwili ukończenia Kursu albo skreślenia z listy
strony: Kursant (podmiot ewidencji), Fundacja pomocy prawnej EGIDA (właściciel rejestru, koordynator Kursu)
parametry:
  - IMIE_KURSANTA - imię (imiona) Kursanta
  - NAZWISKO_KURSANTA - nazwisko Kursanta
  - DATA_URODZENIA - data urodzenia Kursanta w formacie DD-MM-RRRR
  - OBYWATELSTWO - obywatelstwo Kursanta
  - JEZYK_PIERWSZY - pierwszy język Kursanta (PL, EN, ES, UK)
  - NR_FORMULARZA - numer ewidencyjny Formularza rekrutacyjnego
  - NR_OSWIADCZENIA_KWALIFIKOWALNOSCI - numer ewidencyjny oświadczenia kwalifikowalności
  - NR_TESTU_WEJSCIOWEGO - numer ewidencyjny testu wejściowego
  - NR_ANKIETY_WSTEPNEJ - numer ewidencyjny ankiety wstępnej
  - NR_UMOWY_KURSU - numer ewidencyjny umowy kursu
  - CYKL_KURSU - oznaczenie cyklu Kursu (np. C1/2026)
  - MODUL_GLOWNY - moduł, w którym Kursant uczestniczy (M1, M2, M3)
  - DATA_OTWARCIA_KARTY - data otwarcia karty w formacie DD-MM-RRRR
  - KOORDYNATOR_KURSU - imię i nazwisko koordynatora Kursu otwierającego kartę
  - NR_KARTY - numer ewidencyjny karty (np. 2026/C1/001/KU)
---

# KARTA UCZESTNIKA KURSU

**Zbiorczy rekord administracyjny Kursanta uczestniczącego w Kursie praktycznym „Praca w tartaku".** Karta otwierana w chwili pozytywnej decyzji o kwalifikacji kandydata; pełni rolę indeksu wszystkich dokumentów operacyjnych Kursu dotyczących Kursanta. Karta jest dokumentem wewnętrznym Fundacji pomocy prawnej EGIDA i nie podlega wydawaniu Kursantowi (Kursant ma prawo wglądu w trybie RODO na zasadach klauzuli informacyjnej).

---

## Informacja wstępna

Karta uczestnika spełnia funkcję podstawowego rekordu administracyjnego Kursu w kontekście pojedynczego Kursanta. Każdy Kursant kwalifikowany do cyklu Kursu otrzymuje własną kartę. Karta zawiera dane identyfikacyjne, odsyłacze do wszystkich dokumentów operacyjnych dotyczących Kursanta, podsumowanie statusu uczestnictwa oraz wynik końcowy Kursu (jeżeli Kurs został ukończony).

Karta otwierana jest niezwłocznie po przyjęciu kandydata do Kursu i zamykana niezwłocznie po:

a) wystawieniu zaświadczenia o ukończeniu Kursu Kursantowi, który Kurs ukończył; albo

b) wystawieniu protokołu skreślenia Kursanta z listy uczestników, jeżeli Kursant został skreślony.

Karta jest dokumentem parametryzowanym: wzór poniżej zawiera oznaczenia pól danych w postaci `{{NAZWA_POLA}}`. Faktyczna karta konkretnego Kursanta powstaje przez zastąpienie oznaczeń wartościami z arkusza danych edycji Kursu (CSV) za pomocą skryptu generatora. Lista oznaczeń pól danych znajduje się w nagłówku YAML tego dokumentu w polu `parametry`.

| Identyfikator wzoru[^1] | Numer ewidencyjny karty[^2] | Data otwarcia karty (DD-MM-RRRR) |
|--------------------------|------------------------------|-----------------------------------|
| KU-1.0/2026              | {{NR_KARTY}}                 | {{DATA_OTWARCIA_KARTY}}           |

---

## Część A. Dane identyfikacyjne Kursanta

| Pole | Wartość |
|------|---------|
| Imię (imiona): | {{IMIE_KURSANTA}} |
| Nazwisko: | {{NAZWISKO_KURSANTA}} |
| Data urodzenia (DD-MM-RRRR): | {{DATA_URODZENIA}} |
| Obywatelstwo: | {{OBYWATELSTWO}} |
| Pierwszy język Kursanta: | {{JEZYK_PIERWSZY}} |
| Numer ewidencyjny Formularza rekrutacyjnego: | {{NR_FORMULARZA}} |

Szczegółowe dane osobowe (adres do korespondencji, dokumenty pobytowe, kontakt awaryjny) znajdują się w Formularzu rekrutacyjnym o numerze ewidencyjnym wskazanym powyżej i nie są powtarzane w niniejszej karcie ze względu na zasadę minimalizacji danych z art. 5 ust. 1 lit. c RODO.

---

## Część B. Powiązane dokumenty operacyjne

Karta indeksuje wszystkie dokumenty operacyjne Kursu dotyczące Kursanta. W kolumnie „Numer ewidencyjny" wpisuje się numer wskazanej pozycji albo wpis „nie dotyczy", jeżeli dokument nie został (jeszcze) wystawiony.

### B.1. Dokumenty wejściowe

| Dokument | Numer ewidencyjny | Stan na dzień otwarcia karty |
|----------|--------------------|-------------------------------|
| Formularz rekrutacyjny (FRK) | {{NR_FORMULARZA}} | wystawiony |
| Oświadczenie kwalifikowalności (OSK) | {{NR_OSWIADCZENIA_KWALIFIKOWALNOSCI}} | wystawione |
| Test wejściowy (TW) | {{NR_TESTU_WEJSCIOWEGO}} | wystawiony albo nie dotyczy |
| Ankieta wstępna (AW) | {{NR_ANKIETY_WSTEPNEJ}} | wystawiona albo nie dotyczy |
| Umowa kursu (UK) | {{NR_UMOWY_KURSU}} | wystawiona albo do podpisania |

### B.2. Dokumenty realizacyjne (uzupełniane w trakcie Kursu)

| Dokument | Częstotliwość | Sposób ewidencji w karcie |
|----------|---------------|----------------------------|
| Listy obecności dziennej (LO) | per sesja | sumarycznie w części D.1 |
| Protokół z instruktażu BHP (PIB) | per moduł albo per stanowisko | wpis w części D.2 |
| Rejestr wydanych materiałów (RM) | otwarty na początku, zamykany na końcu | wpis w części D.3 |

### B.3. Dokumenty zamykające (uzupełniane na zakończenie Kursu)

| Dokument | Numer ewidencyjny | Stan |
|----------|--------------------|------|
| Wynik testu końcowego | wpis w części E.2 | wystawiony albo nie dotyczy |
| Zaświadczenie o ukończeniu Kursu (Z-UK) | wpis w części F.1 | wystawione albo nie dotyczy |
| Protokół skreślenia z listy (jeżeli dotyczy) | wpis w części F.2 | wystawiony albo nie dotyczy |

---

## Część C. Status uczestnictwa Kursanta

| Pole | Wartość |
|------|---------|
| Cykl Kursu: | {{CYKL_KURSU}} |
| Moduł, w którym Kursant uczestniczy: | {{MODUL_GLOWNY}} |
| Data otwarcia karty: | {{DATA_OTWARCIA_KARTY}} |

### C.1. Aktualny status (zaznaczyć jeden)

☐ kwalifikowany, oczekuje na rozpoczęcie cyklu  
☐ uczestnik aktywny, w trakcie modułu  
☐ uczestnik zawieszony tymczasowo (z powodu opisanego w D.4)  
☐ uczestnik, który ukończył Kurs (zaświadczenie wystawione)  
☐ uczestnik skreślony z listy (protokół skreślenia wystawiony)  
☐ inny status (opisać niżej)

Opis innego statusu (jeżeli dotyczy):

|  |
|--|
|  |

---

## Część D. Realizacja Kursu - frekwencja i przebieg

### D.1. Frekwencja kumulowana (uzupełnia koordynator po każdej sesji)

| Moduł | Liczba sesji w module | Liczba sesji obecnych | Frekwencja procentowa |
|-------|------------------------|------------------------|------------------------|
| M1 |  |  |  |
| M2 |  |  |  |
| M3 |  |  |  |
| Razem |  |  |  |

### D.2. Instruktaże BHP

| Etap | Data instruktażu (DD-MM-RRRR) | Numer protokołu PIB | Uwagi |
|------|--------------------------------|----------------------|-------|
| Przed M1 |  |  |  |
| Przed M2 |  |  |  |
| Przed M3 |  |  |  |
| Inny |  |  |  |

### D.3. Rejestr wydanych materiałów

| Pole | Wartość |
|------|---------|
| Numer ewidencyjny rejestru materiałów (RM): |  |
| Data otwarcia rejestru: |  |
| Data zamknięcia rejestru: |  |
| Stan rozliczenia wypożyczeń: | ☐ rozliczone w pełni ☐ rozliczone z uwagami ☐ nierozliczone |

### D.4. Istotne zdarzenia w trakcie Kursu

|  |
|--|
|  |

---

## Część E. Wyniki dydaktyczne

### E.1. Wyniki testów modułowych

| Moduł | Data testu (DD-MM-RRRR) | Liczba uzyskanych punktów | Liczba punktów maksymalnych | Wynik procentowy | Zaliczony |
|-------|--------------------------|----------------------------|------------------------------|------------------|-----------|
| M1 |  |  |  |  | ☐ tak ☐ nie |
| M2 |  |  |  |  | ☐ tak ☐ nie |
| M3 |  |  |  |  | ☐ tak ☐ nie |

### E.2. Test końcowy Kursu

| Pole | Wartość |
|------|---------|
| Data testu końcowego (DD-MM-RRRR): |  |
| Liczba uzyskanych punktów: |  |
| Liczba punktów maksymalnych: |  |
| Wynik procentowy: |  |
| Wynik testu końcowego: | ☐ zdany ☐ niezdany ☐ nie przystąpił |

### E.3. Indywidualny arkusz oceny instruktora (jakościowy)

|  |
|--|
|  |

---

## Część F. Zamknięcie karty

### F.1. Wystawienie zaświadczenia o ukończeniu Kursu

| Pole | Wartość |
|------|---------|
| Data wystawienia zaświadczenia (DD-MM-RRRR): |  |
| Numer ewidencyjny zaświadczenia: |  |
| Sposób wydania zaświadczenia: | ☐ osobiście za pokwitowaniem ☐ przesyłką pocztową ☐ drogą elektroniczną |
| Data wydania zaświadczenia Kursantowi: |  |

### F.2. Skreślenie z listy uczestników (jeżeli dotyczy)

| Pole | Wartość |
|------|---------|
| Data skreślenia (DD-MM-RRRR): |  |
| Numer ewidencyjny protokołu skreślenia: |  |
| Powód skreślenia: | ☐ rezygnacja Kursanta ☐ niska frekwencja poniżej progu Regulaminu Kursu ☐ niezdanie testu końcowego ☐ rażące naruszenie zasad BHP ☐ inny powód (opisać niżej) |
| Opis innego powodu skreślenia (jeżeli dotyczy): |  |

### F.3. Zamknięcie karty

| Pole | Wartość |
|------|---------|
| Data zamknięcia karty (DD-MM-RRRR): |  |
| Imię i nazwisko koordynatora zamykającego kartę: |  |
| Własnoręczny podpis koordynatora zamykającego kartę: |  |

---

## Część G. Notatki koordynatora

W tej części koordynator zapisuje notatki o charakterze administracyjnym dotyczące Kursanta, takie jak istotne kontakty z Kursantem, zmiany danych, sygnały od instruktorów, decyzje koordynatora.

|  |
|--|
|  |

---

## Część H. Otwarcie karty

| Pole | Wartość |
|------|---------|
| Data otwarcia karty (DD-MM-RRRR): | {{DATA_OTWARCIA_KARTY}} |
| Imię i nazwisko koordynatora otwierającego kartę: | {{KOORDYNATOR_KURSU}} |
| Własnoręczny podpis koordynatora otwierającego kartę: |  |

---

## Wzmianka o projekcie

Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców.

---

## Przypisy

[^1]: Identyfikator wzoru określa wersję wzoru karty w postaci: KU (skrót od „karta uczestnika") - numer wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji wzoru przez Fundację.

[^2]: Numer ewidencyjny karty nadaje koordynator Kursu w chwili otwarcia karty. Numer ma postać: rok / oznaczenie cyklu / numer kolejny w cyklu / KU (np. 2026/C1/001/KU). Numer powiązany jest jednoznacznie z numerem Formularza rekrutacyjnego Kursanta.

---

*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór parametryzowany; faktyczna karta powstaje przez zastąpienie pól `{{NAZWA_POLA}}` wartościami z arkusza danych edycji Kursu. Karta uczestnika stanowi dokument wewnętrzny Fundacji.*
