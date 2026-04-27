---
typ: karta
dokument: participant card of the Course (consolidated administrative record per Course Participant)
kurs: Praca w tartaku (Work in a sawmill)
podprojekt: B
faza: B4-operacyjne
grupa: O1-wejście
klasa: 2
parametryzacja: CSV-DOCX
język: en
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) [Act of 24 April 2003 on public benefit activity and voluntary work, consolidated text Journal of Laws of 2024, item 1491, as amended] in the scope of documenting the statutory activity of the Foundation
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO) [Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (GDPR)], in particular Article 6(1)(b) and (f), in the scope of maintaining the record of the Course Participant's participation in the Course
charakter: consolidated administrative record of an individual Course Participant, binding by cross-references all operational documents of the Course concerning that Course Participant; the card is opened at the moment of the candidate's qualification and closed at the moment of completion of the Course or removal from the list
strony: Course Participant (subject of the record), Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation) (owner of the register, Course coordinator)
parametry:
  - IMIE_KURSANTA - first name (names) of the Course Participant
  - NAZWISKO_KURSANTA - surname of the Course Participant
  - DATA_URODZENIA - date of birth of the Course Participant in the format DD-MM-YYYY
  - OBYWATELSTWO - citizenship of the Course Participant
  - JEZYK_PIERWSZY - first language of the Course Participant (PL, EN, ES, UK)
  - NR_FORMULARZA - registration number of the Recruitment Form
  - NR_OSWIADCZENIA_KWALIFIKOWALNOSCI - registration number of the eligibility declaration
  - NR_TESTU_WEJSCIOWEGO - registration number of the entry test
  - NR_ANKIETY_WSTEPNEJ - registration number of the preliminary survey
  - NR_UMOWY_KURSU - registration number of the course agreement
  - CYKL_KURSU - designation of the Course cycle (e.g. C1/2026)
  - MODUL_GLOWNY - module in which the Course Participant takes part (M1, M2, M3)
  - DATA_OTWARCIA_KARTY - date of opening the card in the format DD-MM-YYYY
  - KOORDYNATOR_KURSU - first name and surname of the Course coordinator opening the card
  - NR_KARTY - registration number of the card (e.g. 2026/C1/001/KU)
---

# COURSE PARTICIPANT CARD

**Consolidated administrative record of a Course Participant taking part in the practical Course "Praca w tartaku" (Work in a sawmill).** The card is opened at the moment of a positive decision on the candidate's qualification; it serves as an index of all operational documents of the Course concerning the Course Participant. The card is an internal document of the Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation) and is not subject to issuance to the Course Participant (the Course Participant has the right of access under the GDPR procedure on the terms set out in the information clause).

---

## Preliminary information

The participant card serves as the basic administrative record of the Course in the context of an individual Course Participant. Each Course Participant qualified for a Course cycle receives their own card. The card contains identification data, cross-references to all operational documents concerning the Course Participant, a summary of participation status, and the final result of the Course (if the Course has been completed).

The card is opened immediately after the candidate is admitted to the Course and closed immediately after:

a) the issuance of a certificate of completion of the Course to the Course Participant who has completed the Course; or

b) the issuance of a removal protocol of the Course Participant from the list of participants, if the Course Participant has been removed.

The card is a parametrised document: the template below contains data field markers in the form `{{FIELD_NAME}}`. The actual card of a specific Course Participant is created by replacing the markers with values from the Course edition data sheet (CSV) using a generator script. The list of data field markers is provided in the YAML header of this document in the `parametry` field.

| Template identifier[^1] | Card registration number[^2] | Date of opening the card (DD-MM-YYYY) |
|--------------------------|------------------------------|-----------------------------------------|
| KU-1.0/2026              | {{NR_KARTY}}                 | {{DATA_OTWARCIA_KARTY}}                 |

---

## Part A. Identification data of the Course Participant

| Field | Value |
|-------|-------|
| First name (names): | {{IMIE_KURSANTA}} |
| Surname: | {{NAZWISKO_KURSANTA}} |
| Date of birth (DD-MM-YYYY): | {{DATA_URODZENIA}} |
| Citizenship: | {{OBYWATELSTWO}} |
| First language of the Course Participant: | {{JEZYK_PIERWSZY}} |
| Registration number of the Recruitment Form: | {{NR_FORMULARZA}} |

Detailed personal data (correspondence address, residence documents, emergency contact) are kept in the Recruitment Form with the registration number indicated above and are not repeated in this card due to the principle of data minimisation under Article 5(1)(c) GDPR.

---

## Part B. Related operational documents

The card indexes all operational documents of the Course concerning the Course Participant. In the "Registration number" column, the number of the indicated item is entered, or the entry "not applicable", if the document has not (yet) been issued.

### B.1. Entry documents

| Document | Registration number | Status as at the date of opening the card |
|----------|---------------------|--------------------------------------------|
| Recruitment Form (FRK) | {{NR_FORMULARZA}} | issued |
| Eligibility declaration (OSK) | {{NR_OSWIADCZENIA_KWALIFIKOWALNOSCI}} | issued |
| Entry test (TW) | {{NR_TESTU_WEJSCIOWEGO}} | issued or not applicable |
| Preliminary survey (AW) | {{NR_ANKIETY_WSTEPNEJ}} | issued or not applicable |
| Course agreement (UK) | {{NR_UMOWY_KURSU}} | issued or to be signed |

### B.2. Implementation documents (completed during the Course)

| Document | Frequency | Method of recording in the card |
|----------|-----------|-----------------------------------|
| Daily attendance lists (LO) | per session | summarised in part D.1 |
| OHS instruction protocol (PIB) | per module or per workstation | entry in part D.2 |
| Register of issued materials (RM) | opened at the start, closed at the end | entry in part D.3 |

### B.3. Closing documents (completed at the end of the Course)

| Document | Registration number | Status |
|----------|---------------------|--------|
| Final test result | entry in part E.2 | issued or not applicable |
| Certificate of completion of the Course (Z-UK) | entry in part F.1 | issued or not applicable |
| Removal protocol from the list (if applicable) | entry in part F.2 | issued or not applicable |

---

## Part C. Course Participant's participation status

| Field | Value |
|-------|-------|
| Course cycle: | {{CYKL_KURSU}} |
| Module in which the Course Participant takes part: | {{MODUL_GLOWNY}} |
| Date of opening the card: | {{DATA_OTWARCIA_KARTY}} |

### C.1. Current status (mark one)

☐ qualified, awaiting the start of the cycle  
☐ active participant, during the module  
☐ participant temporarily suspended (for the reason described in D.4)  
☐ participant who has completed the Course (certificate issued)  
☐ participant removed from the list (removal protocol issued)  
☐ other status (describe below)

Description of other status (if applicable):

|  |
|--|
|  |

---

## Part D. Implementation of the Course, attendance and progress

### D.1. Cumulative attendance (completed by the coordinator after each session)

| Module | Number of sessions in the module | Number of sessions attended | Attendance percentage |
|--------|----------------------------------|------------------------------|------------------------|
| M1 |  |  |  |
| M2 |  |  |  |
| M3 |  |  |  |
| Total |  |  |  |

### D.2. OHS instructions

| Stage | Date of instruction (DD-MM-YYYY) | PIB protocol number | Comments |
|-------|------------------------------------|----------------------|----------|
| Before M1 |  |  |  |
| Before M2 |  |  |  |
| Before M3 |  |  |  |
| Other |  |  |  |

### D.3. Register of issued materials

| Field | Value |
|-------|-------|
| Registration number of the materials register (RM): |  |
| Date of opening the register: |  |
| Date of closing the register: |  |
| Status of loan settlement: | ☐ fully settled ☐ settled with comments ☐ not settled |

### D.4. Significant events during the Course

|  |
|--|
|  |

---

## Part E. Educational results

### E.1. Module test results

| Module | Date of test (DD-MM-YYYY) | Points obtained | Maximum points | Percentage result | Passed |
|--------|----------------------------|-----------------|-----------------|--------------------|--------|
| M1 |  |  |  |  | ☐ yes ☐ no |
| M2 |  |  |  |  | ☐ yes ☐ no |
| M3 |  |  |  |  | ☐ yes ☐ no |

### E.2. Final test of the Course

| Field | Value |
|-------|-------|
| Date of the final test (DD-MM-YYYY): |  |
| Points obtained: |  |
| Maximum points: |  |
| Percentage result: |  |
| Final test result: | ☐ passed ☐ failed ☐ did not take |

### E.3. Individual instructor evaluation sheet (qualitative)

|  |
|--|
|  |

---

## Part F. Closing the card

### F.1. Issuance of the certificate of completion of the Course

| Field | Value |
|-------|-------|
| Date of issuance of the certificate (DD-MM-YYYY): |  |
| Registration number of the certificate: |  |
| Method of issuing the certificate: | ☐ in person against receipt ☐ by postal delivery ☐ electronically |
| Date of delivery of the certificate to the Course Participant: |  |

### F.2. Removal from the list of participants (if applicable)

| Field | Value |
|-------|-------|
| Date of removal (DD-MM-YYYY): |  |
| Registration number of the removal protocol: |  |
| Reason for removal: | ☐ resignation of the Course Participant ☐ low attendance below the threshold of the Course Regulations ☐ failure of the final test ☐ gross violation of OHS rules ☐ other reason (describe below) |
| Description of other reason for removal (if applicable): |  |

### F.3. Closing the card

| Field | Value |
|-------|-------|
| Date of closing the card (DD-MM-YYYY): |  |
| First name and surname of the coordinator closing the card: |  |
| Handwritten signature of the coordinator closing the card: |  |

---

## Part G. Coordinator's notes

In this part, the coordinator records administrative notes concerning the Course Participant, such as significant contacts with the Course Participant, changes in data, signals from instructors, decisions of the coordinator.

|  |
|--|
|  |

---

## Part H. Opening the card

| Field | Value |
|-------|-------|
| Date of opening the card (DD-MM-YYYY): | {{DATA_OTWARCIA_KARTY}} |
| First name and surname of the coordinator opening the card: | {{KOORDYNATOR_KURSU}} |
| Handwritten signature of the coordinator opening the card: |  |

---

## Note on the project

The Course "Praca w tartaku" (Work in a sawmill) was created as a result of the potential developed within the project "Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Building the foundations of support for foreigners on the labour market in the Opolskie Voivodeship), implemented by Stowarzyszenie SMART (SMART Association) (lead partner) in cooperation with Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation) (partner) in the years 2026-2027 from the funds of the European Social Fund Plus. The Course itself is not financed from the project funds and does not constitute a project activity; it is an independent statutory undertaking of the Foundation, conducted free of charge for the benefit of foreigners.

---

## Footnotes

[^1]: The template identifier specifies the version of the card template in the form: KU (abbreviation of "karta uczestnika", participant card), version number, year of validity. The version number is raised at each update of the template by the Foundation.

[^2]: The registration number of the card is assigned by the Course coordinator at the moment of opening the card. The number has the form: year / cycle designation / sequential number in the cycle / KU (e.g. 2026/C1/001/KU). The number is unambiguously linked to the registration number of the Course Participant's Recruitment Form.

---

*Document drawn up by the Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation). Parametrised template; the actual card is created by replacing the `{{FIELD_NAME}}` fields with values from the Course edition data sheet. The participant card constitutes an internal document of the Foundation.*
