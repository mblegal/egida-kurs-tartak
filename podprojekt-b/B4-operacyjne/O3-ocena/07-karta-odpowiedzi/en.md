---
typ: karta odpowiedzi
dokument: karta odpowiedzi do quizu uzupełniającego Modułu Kursu (uniwersalna karta wypełniana przez Kursanta)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O3-ocena
klasa: 2
parametryzacja: CSV-DOCX
język: en
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie diagnozy efektów uczenia się Kursanta
charakter: universal answer form filled in manually by the Trainee during the supplementary quiz of any of the three Course Modules; the form is completed in the presence of the instructor or the coordinator and submitted for evaluation
strony: Trainee (filling in the form), Course instructor (evaluating the form), Fundacja pomocy prawnej EGIDA (author and owner of the template)
parametry:
  - IMIE_KURSANTA - Trainee's first name (or first names)
  - NAZWISKO_KURSANTA - Trainee's last name
  - NR_KARTY - registration number of the answer sheet (e.g. 2026/C1/001/KO)
  - KOD_QUIZU - identifier of the quiz to which the sheet is attached (e.g. QUM-M1-1.0/2026)
  - NUMER_MODULU - number of the Module to which the quiz refers (1, 2 or 3)
  - TRYB_QUIZU - mode in which the quiz is conducted (self-assessment or remedial)
  - DATA_QUIZU - date of completion of the sheet in the format DD-MM-YYYY
  - CYKL_KURSU - designation of the Course cycle in which the Trainee participates (e.g. C1/2026)
  - KOORDYNATOR_KURSU - first and last name of the coordinator or instructor receiving the sheet
  - LICZBA_ZAMKNIETYCH - number of closed-ended questions in the quiz (e.g. 15 for M1, 30 for M2, 15 for M3)
  - LICZBA_OTWARTYCH - number of open-ended questions in the quiz (e.g. 0 for M1, 15 for M2, 0 for M3)
  - LICZBA_CASEOW - number of case-type questions in the quiz (e.g. 0 for M1, 10 for M2, 0 for M3)
  - CZAS_TRWANIA_MIN - expected time for completing the sheet in minutes (e.g. 30 for M1, 120 for M2, 60 for M3)
---

# QUIZ ANSWER SHEET FOR THE MODULE SUPPLEMENTARY QUIZ

**Practical course „Praca w tartaku" (Work in a sawmill)**: a vocational course for foreigners legally residing in the territory of the Republic of Poland, organised free of charge by Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation).

---

## Preliminary information

This answer sheet is used to document the Trainee's answers to the questions of the supplementary quiz of any of the three Course Modules. The sheet is **universal**: it contains three sections corresponding to the three types of questions occurring in the Module quizzes (closed-ended, open-ended, cases). The Trainee fills in only those sections that correspond to the structure of the quiz to which the sheet is attached, the number of questions in each section is given in the header of the sheet (the field "Number of questions in the quiz"). The remaining rows or fields are left blank.

The sheet is filled in **independently**, in pen or pencil, in the presence of the Course coordinator or instructor. The use of notes, textbooks, a telephone, a computer or assistance from other persons is not permitted. The time available for completing the sheet is given in the header of the sheet (the field "Quiz duration"). When the time runs out, the Trainee finishes filling in the sheet and hands it over.

The sheet is a parameterised document: the actual sheet for a specific Trainee and a specific Course cycle is produced by replacing the fields `{{NAZWA_POLA}}` with values from the data sheet of the Course edition (CSV) using a generator script. The list of data field designations can be found in the YAML header of this document, in the field `parametry`.

| Template identifier[^1] | Sheet registration number[^2] | Date of completion (DD-MM-YYYY) |
|--------------------------|-------------------------------|---------------------------------|
| KO-1.0/2026              | {{NR_KARTY}}                  | {{DATA_QUIZU}}                  |

---

## Section A. Identification of the Trainee and of the quiz

| Field | Value |
|-------|-------|
| Trainee's first name (or first names): | {{IMIE_KURSANTA}} |
| Trainee's last name: | {{NAZWISKO_KURSANTA}} |
| Course cycle: | {{CYKL_KURSU}} |
| Number of the Module to which the quiz refers: | {{NUMER_MODULU}} |
| Quiz identifier (template code): | {{KOD_QUIZU}} |
| Quiz mode: | {{TRYB_QUIZU}} |
| Quiz duration (in minutes): | {{CZAS_TRWANIA_MIN}} |

### Number of questions in the quiz (information for the Trainee)

| Section of the sheet | Type of questions | Number of questions in this quiz |
|----------------------|-------------------|----------------------------------|
| Section B | closed-ended questions (A/B/C/D, one correct answer) | {{LICZBA_ZAMKNIETYCH}} |
| Section C | open-ended questions (answer of 1-3 sentences) | {{LICZBA_OTWARTYCH}} |
| Section D | case-type questions (analysis of 4-6 sentences) | {{LICZBA_CASEOW}} |

Fill in only the rows that correspond to the actual number of questions in the quiz. Leave the rows beyond that number blank or cross them out with a slash.

---

## Section B. Answers to closed-ended questions

In each row, mark **one** answer (A, B, C or D) by placing a × in the appropriate box. If you do not know the answer, mark "I don't know". If the quiz requires a justification of the answer (Module 3), enter the justification in the column "Justification" in 2-3 sentences.

| Question number | A | B | C | D | I don't know | Justification (if required) |
|-----------------|---|---|---|---|--------------|------------------------------|
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

## Section C. Answers to open-ended questions

In each field, write your answer to the question with the number indicated on the left. The answer should consist of **1-3 sentences**. If you do not know the answer, write "I don't know".

**Open-ended question 1**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 2**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 3**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 4**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 5**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 6**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 7**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 8**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 9**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 10**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 11**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 12**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 13**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 14**

|  |
|--|
|  |
|  |
|  |

**Open-ended question 15**

|  |
|--|
|  |
|  |
|  |

---

## Section D. Answers to case-type questions

In each field, write an analysis of the situation described in the question with the number indicated on the left. The analysis should consist of **4-6 sentences** and should include: a description of the problem from the Trainee's perspective, an indication of the applicable rules or provisions, a proposed course of action.

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

## Section E. Trainee's declaration

I hereby declare that I have completed this answer sheet independently, without using any notes, textbooks, telephone, computer, or assistance from other persons. The answers entered are my own. I understand that the sheet will be submitted for evaluation by the Course instructor on the basis of the answer key in force for the given quiz.

| Field | Value |
|-------|-------|
| Date of completion of the sheet (DD-MM-YYYY): | {{DATA_QUIZU}} |
| Trainee's handwritten signature: |  |

---

## Section F. Receipt of the sheet by the coordinator or instructor

| Field | Value |
|-------|-------|
| Date of receipt of the sheet (DD-MM-YYYY): | {{DATA_QUIZU}} |
| First and last name of the coordinator or instructor receiving the sheet: | {{KOORDYNATOR_KURSU}} |
| Handwritten signature of the coordinator or instructor: |  |

---

## Note on the project

The course „Praca w tartaku" (Work in a sawmill) was created as a result of the potential developed within the project „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Building foundations for supporting foreigners in the labour market in the Opole Voivodeship), implemented by Stowarzyszenie SMART (leader) in cooperation with Fundacja pomocy prawnej EGIDA (partner) in the years 2026-2027 from the resources of the European Social Fund Plus. The Course itself is not financed from project resources and does not constitute a project activity; it is an independent statutory undertaking of the Foundation, conducted free of charge for foreigners.

---

## Footnotes

[^1]: The template identifier indicates the version of the answer sheet template in the format: KO (abbreviation for „karta odpowiedzi", answer sheet), version number, year of effect. The version number is increased with each update of the template by the Foundation. The sheet is universal for all three Course Modules and all quiz modes (self-assessment, remedial).

[^2]: The sheet registration number is assigned by the Course coordinator at the moment the completed sheet is received from the Trainee. The number takes the form: year / cycle designation / consecutive number in the cycle / KO (e.g. 2026/C1/001/KO). The number is uniquely linked to the Trainee's Course participant Card number and to the quiz identifier.

---

*Document prepared by Fundacja pomocy prawnej EGIDA. Parameterised template; the actual answer sheet is produced by replacing the fields `{{NAZWA_POLA}}` with values from the data sheet of the Course edition. After being filled in and submitted for evaluation, the sheet constitutes an operational document of the Course and is subject to archiving together with the remaining documentation of the cycle.*
