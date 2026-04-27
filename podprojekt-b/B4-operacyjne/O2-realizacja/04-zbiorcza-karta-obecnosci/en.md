---
typ: karta
dokument: Course Participant's cumulative attendance card (cumulative summary of attendance at all sessions of the cycle)
kurs: Praca w tartaku (Work in a sawmill)
podprojekt: B
faza: B4-operacyjne
grupa: O2-realizacja
klasa: 2
parametryzacja: CSV-DOCX
język: en
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie dokumentowania działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. b oraz lit. f w zakresie informacji zwrotnej Kursantowi o jego frekwencji
charakter: individual document per Course Participant; cumulative summary of attendance at all sessions of the Course cycle; serves as feedback for the Course Participant and as the basis for the decision on admission to the final test
strony: Course Participant (addressee of the attendance information), Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation) (preparing party and owner of the register)
parametry:
  - IMIE_KURSANTA - first name(s) of the Course Participant
  - NAZWISKO_KURSANTA - surname of the Course Participant
  - NR_KARTY_UCZESTNIKA - registration number of the linked Participant Card (KU)
  - NR_FORMULARZA - registration number of the Recruitment Form
  - CYKL_KURSU - designation of the Course cycle
  - MODUL_GLOWNY - module in which the Course Participant takes part (M1, M2, M3)
  - DATA_OTWARCIA_KARTY - card opening date (usually the date of the first session)
  - DATA_ZAMKNIECIA_KARTY - card closing date (usually the date of the last session)
  - LACZNA_LICZBA_SESJI - total number of sessions in the cycle as of the card closing date
  - LICZBA_SESJI_OBECNYCH - number of sessions at which the Course Participant was present
  - FREKWENCJA_PROCENTOWA - attendance of the Course Participant as a percentage
  - PROG_FREKWENCJI_REGULAMIN - attendance threshold required by the Course Regulations (e.g. 80%)
  - DECYZJA_DOPUSZCZENIA - decision on admission of the Course Participant to the final test (yes / no / conditionally)
  - KOORDYNATOR_KURSU - first name and surname of the coordinator signing the card
  - NR_KARTY_OBECNOSCI - registration number of the cumulative attendance card (e.g. 2026/C1/001/ZKO)
---

# COURSE PARTICIPANT'S CUMULATIVE ATTENDANCE CARD

**Cumulative summary of the Course Participant's attendance at all sessions of the cycle of the practical Course "Praca w tartaku" (Work in a sawmill).** The card is prepared individually for each Course Participant by the Course coordinator on the basis of daily attendance lists. The card is issued to the Course Participant in a copy after the closing of the cycle as feedback on attendance and is attached to the Course Participant's file.

---

## Introductory information

The cumulative attendance card serves two functions:

a) **internal** - it constitutes the basis for the Course coordinator's decision on admission of the Course Participant to the final test and, further, on issuing the certificate of completion of the Course, in accordance with the attendance threshold specified in the Course Regulations;

b) **external** - it constitutes feedback for the Course Participant on actual attendance, provided as a copy in accordance with the right of the Course Participant to access personal data processed by the Foundation.

The card is prepared after each session by updating the attendance grid and at the end of the cycle by way of a summary recapitulation.

| Template identifier[^1] | Card registration number[^2] | Course cycle | Linked Participant Card |
|--------------------------|------------------------------|------------|------------------------------|
| ZKO-1.0/2026             | {{NR_KARTY_OBECNOSCI}}       | {{CYKL_KURSU}} | {{NR_KARTY_UCZESTNIKA}}   |

---

## Section A. Identification of the Course Participant

| Field | Value |
|------|---------|
| First name(s): | {{IMIE_KURSANTA}} |
| Surname: | {{NAZWISKO_KURSANTA}} |
| Registration number of the Recruitment Form: | {{NR_FORMULARZA}} |
| Registration number of the linked Participant Card: | {{NR_KARTY_UCZESTNIKA}} |
| Course cycle: | {{CYKL_KURSU}} |
| Module in which the Course Participant takes part: | {{MODUL_GLOWNY}} |
| Card opening date (DD-MM-YYYY): | {{DATA_OTWARCIA_KARTY}} |

---

## Section B. Attendance grid per session

Each row of the table corresponds to a single session of the cycle, in chronological order consistent with the Detailed Schedule. In the "Attendance" column, one of the following marks is entered: **+** (present), **-** (absent unjustified), **U** (justified absence), **S** (significant tardiness above 15 minutes), **W** (left before the end of the session).

| Session No. | Session date (DD-MM-YYYY) | Module | Session title | Attendance | Attendance List number (LO) |
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

## Section C. Numerical summary (completed by the coordinator after closing the cycle)

### C.1. Attendance per module

| Module | Number of sessions in module | Number of sessions present | Number of justified absences | Number of unjustified absences | Attendance percentage |
|-------|------------------------|------------------------|----------------------------------------------|------------------------------------------------|------------------------|
| M1 |  |  |  |  |  |
| M2 |  |  |  |  |  |
| M3 |  |  |  |  |  |
| **Total** | {{LACZNA_LICZBA_SESJI}} | {{LICZBA_SESJI_OBECNYCH}} |  |  | {{FREKWENCJA_PROCENTOWA}} |

### C.2. Attendance threshold required by the Course Regulations

| Field | Value |
|------|---------|
| Attendance threshold specified in section VII of the Course Regulations (percentage): | {{PROG_FREKWENCJI_REGULAMIN}} |
| Whether the Course Participant's attendance reached the threshold: | ☐ yes ☐ no ☐ special circumstances apply (described below) |
| Description of special circumstances (if applicable): |  |

---

## Section D. Decision on admission to the final test

| Field | Value |
|------|---------|
| Coordinator's decision: | {{DECYZJA_DOPUSZCZENIA}} |
| Brief justification of the decision: |  |
| Date of the decision (DD-MM-YYYY): |  |
| First name and surname of the coordinator issuing the decision: | {{KOORDYNATOR_KURSU}} |
| Handwritten signature of the coordinator: |  |

---

## Section E. Issuance of a copy to the Course Participant

| Field | Value |
|------|---------|
| Card closing date (DD-MM-YYYY): | {{DATA_ZAMKNIECIA_KARTY}} |
| Date of issuance of the copy to the Course Participant (DD-MM-YYYY): |  |
| Method of issuance of the copy: | ☐ personally against acknowledgement of receipt ☐ by postal mail ☐ electronically in accordance with the Course Agreement |
| Course Participant's annotation on receipt of the copy (if issued personally): |  |
| Handwritten signature of the Course Participant upon receipt of the copy (if issued personally): |  |

---

## Note on the project

The Course "Praca w tartaku" (Work in a sawmill) was created as a result of the potential developed under the project "Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Building the foundations of support for foreigners on the labour market in the Opolskie voivodeship), implemented by the SMART Association (leader) in cooperation with Fundacja pomocy prawnej EGIDA (partner) in 2026-2027 from the resources of the European Social Fund Plus. The Course itself is not financed from the project funds and does not constitute a project activity; it is an independent statutory undertaking of the Foundation, conducted free of charge for the benefit of foreigners.

---

## Footnotes

[^1]: The template identifier specifies the version of the cumulative attendance card template in the form: ZKO (abbreviation for "zbiorcza karta obecności", cumulative attendance card) - version number - year of validity. The version number is increased upon each update of the template by the Foundation.

[^2]: The registration number of the cumulative attendance card is assigned by the Course coordinator at the moment of opening the card (usually on the date of the first session of the cycle). The number takes the form: year / cycle designation / sequential number in the cycle / ZKO (e.g. 2026/C1/001/ZKO). The number should correspond to the number of the linked Participant Card (preserving the different suffix KU or ZKO).

---

*Document prepared by Fundacja pomocy prawnej EGIDA. Parameterised template; the actual card is created by replacing the `{{FIELD_NAME}}` fields with values from the Course edition data sheet and entering attendance in section B. The cumulative attendance card is issued to the Course Participant in a copy after the closing of the cycle.*
