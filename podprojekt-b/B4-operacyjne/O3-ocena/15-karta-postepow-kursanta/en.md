---
typ: progress card
dokument: Trainee progress card (consolidated summary of results from all assessment tools throughout the Course cycle, parameterised for an individual Trainee)
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
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (Act of 24 April 2003 on public benefit activity and voluntary work, consolidated text Dz.U. 2024 item 1491 as amended) with respect to the statutory activity of the Foundation
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016, GDPR), in particular Article 6 (1) (f) with respect to diagnosing the Trainee's learning outcomes and providing feedback to the learner
charakter: parameterised consolidated document presenting to the Trainee and the instructor a complete picture of progress throughout the Course cycle (partial check tests, supplementary quizzes, modular tests, final Course test); a feedback tool for the Trainee and a basis for the instructor's methodological decisions; issued to the Trainee in the Trainee's language and in Polish for the Course records
strony: Trainee (the person to whom the card relates and the recipient of progress information), Course instructor (author of methodological decisions based on the card), Course coordinator (person keeping the register of progress cards for the cycle), Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation, owner of the tool)
parametry:
  - IMIE_KURSANTA - first name (names) of the Trainee
  - NAZWISKO_KURSANTA - surname of the Trainee
  - NR_KARTY_UCZESTNIKA - registration number of the Trainee's participant card (e.g., 2026/C1/001/KU)
  - CYKL_KURSU - identifier of the Course cycle (e.g., C1/2026)
  - DATA_GENERACJI - date of generation of the progress card in the format DD-MM-YYYY
  - WYNIK_SPC_M1_T12 - result of the partial check test of Module 1, block T1+T2, in the form X/30 or the special value not attempted
  - WYNIK_SPC_M1_T34 - result of the partial check test of Module 1, block T3+T4, in the form X/30 or the special value not attempted
  - WYNIK_QUM_M1 - result of the supplementary quiz of Module 1 in the form X/30 or the special value not attempted (self-assessment or remedial mode marked in the column alongside)
  - TRYB_QUM_M1 - mode in which the supplementary quiz of Module 1 was conducted (self-assessment or remedial or not applicable)
  - WYNIK_QUM_M2 - result of the supplementary quiz of Module 2 in the form X/110 or the special value not attempted
  - TRYB_QUM_M2 - mode in which the supplementary quiz of Module 2 was conducted (self-assessment or remedial or not applicable)
  - WYNIK_QUM_M3 - result of the supplementary quiz of Module 3 in the form X/45 or the special value not attempted
  - TRYB_QUM_M3 - mode in which the supplementary quiz of Module 3 was conducted (self-assessment or remedial or not applicable)
  - WYNIK_TEST_M1 - result of the modular test of Module 1 (lesson l8 of week 4) in the form X/110 or the special value not attempted
  - WYNIK_TEST_M2 - result of the modular test of Module 2 (lesson l8 of week 4) in the form X/40 or the special value not attempted
  - WYNIK_TEST_M3 - result of the modular test of Module 3 (lesson l8 of week 4, equivalent to the final Course test) in the form X/108 or the special value not attempted
  - WYNIK_TKK - result of the final Course test in the form X/108 or the special value not attempted
  - DECYZJA_TKK - decision following the final Course test (passed or failed or not attempted)
  - KOMENTARZ_INSTRUKTORA - brief comment from the instructor to the Trainee regarding the overall picture of progress (optional)
  - INSTRUKTOR - first name and surname of the instructor leading the Trainee
  - KOORDYNATOR_KURSU - first name and surname of the Course coordinator
  - NR_KARTY_POSTEPOW - registration number of the progress card (e.g., 2026/001/KP)
---

# TRAINEE PROGRESS CARD

**Practical Course "Praca w tartaku" (Work in a sawmill)**: a vocational course for foreign nationals legally residing in the territory of the Republic of Poland, organised free of charge by Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation).

---

## Introductory note

This progress card documents **the complete picture of the Trainee's results throughout the Course cycle** with respect to all assessment tools: partial check tests, supplementary quizzes, modular tests (lessons l8 of week 4 of each Module) and the final Course test. The card serves as a **feedback tool** for the Trainee and a **basis for methodological decisions** of the instructor (planning of revisions, decisions on self-assessment or remedial mode, evaluation of the Trainee's readiness for the practical examination).

The card is issued to the Trainee in the Trainee's native language (Polish, English, Spanish or Ukrainian) and, regardless of the Trainee's language, in a Polish-language version for the Course records.

The card is a parameterised document: the actual card for a specific Trainee at a specific moment of the cycle is created by replacing the `{{NAZWA_POLA}}` fields with values from the Course-edition data sheet (CSV) by means of a generator script. The list of data field identifiers is provided in the YAML header of this document under the `parametry` field.

| Template identifier[^1] | Registration number of the progress card[^2] | Date of card generation (DD-MM-YYYY) |
|---|---|---|
| KP-1.0/2026 | {{NR_KARTY_POSTEPOW}} | {{DATA_GENERACJI}} |

---

## Part A. Identification of the Trainee

| Field | Value |
|---|---|
| First name (names) of the Trainee: | {{IMIE_KURSANTA}} |
| Surname of the Trainee: | {{NAZWISKO_KURSANTA}} |
| Trainee's participant card number: | {{NR_KARTY_UCZESTNIKA}} |
| Course cycle: | {{CYKL_KURSU}} |
| Leading instructor: | {{INSTRUKTOR}} |

---

## Part B. Results of assessment tools

### Partial check tests of Module 1

The partial check tests are tools for mid-term diagnosis of the Trainee's progress after the second and third weeks of Module 1. Each check test consists of 15 closed-ended questions worth 2 points each (30 points in total), with a passing threshold of 70% = 21 points. Partial check tests for Module 2 and Module 3 are not provided in the current version of the Course programme.

| Tool | Template identifier | Maximum | Trainee's result |
|---|---|---|---|
| Partial check test M1 (T1+T2) | SPC-M1-T12-1.0/2026 | 30 points | {{WYNIK_SPC_M1_T12}} |
| Partial check test M1 (T3+T4) | SPC-M1-T34-1.0/2026 | 30 points | {{WYNIK_SPC_M1_T34}} |

### Supplementary quizzes of the Modules

The supplementary quizzes are a self-assessment tool following the modular test (where passed) or a remedial-mode tool (where the modular test was not passed). The mode in which the quiz was conducted is indicated in the "Mode" column.

| Tool | Template identifier | Maximum | Trainee's result | Mode |
|---|---|---|---|---|
| Supplementary quiz M1 | QUM-M1-1.0/2026 | 30 points | {{WYNIK_QUM_M1}} | {{TRYB_QUM_M1}} |
| Supplementary quiz M2 | QUM-M2-1.0/2026 | 110 points | {{WYNIK_QUM_M2}} | {{TRYB_QUM_M2}} |
| Supplementary quiz M3 | QUM-M3-1.0/2026 | 45 points | {{WYNIK_QUM_M3}} | {{TRYB_QUM_M3}} |

### Modular tests (lesson l8 of week 4)

The modular tests are the basic tools for completing each Module of the Course. They are conducted as lesson l8 of week 4 of each Module. The passing threshold for the modular test is 70% of points; failure to pass results in repeating selected lessons and a retake.

| Tool | Maximum | Passing threshold (70%) | Trainee's result |
|---|---|---|---|
| Modular test M1 (l8 of week 4 of Module 1) | 110 points | 77 points | {{WYNIK_TEST_M1}} |
| Modular test M2 (l8 of week 4 of Module 2) | 40 points | 28 points | {{WYNIK_TEST_M2}} |
| Modular test M3 (l8 of week 4 of Module 3, equivalent to the final Course test) | 108 points | 76 points | {{WYNIK_TEST_M3}} |

### Final Course test

The final Course test covers the content of all three Modules in the proportion 20% / 30% / 50% and is a condition of admission to the practical examination and of issuance of the certificate of completion of the Course. In practice the final Course test is identical to the modular test of Module 3 (lesson l8 of week 4 of Module 3), so the result of the final test is a repetition of the result from the "Modular test M3" row above. The field remains in the card as a separate entry because some Course cycles may introduce an additional separate final test with a different registration number.

| Tool | Template identifier | Maximum | Passing threshold (70%) | Trainee's result | Decision |
|---|---|---|---|---|---|
| Final Course test | TKK-1.0/2026 | 108 points | 76 points | {{WYNIK_TKK}} | {{DECYZJA_TKK}} |

---

## Part C. Instructor's comment

{{KOMENTARZ_INSTRUKTORA}}

---

## Part D. Signatures

| Party | First name and surname | Date | Signature |
|---|---|---|---|
| Trainee (confirmation of receipt of the card) | {{IMIE_KURSANTA}} {{NAZWISKO_KURSANTA}} | {{DATA_GENERACJI}} | _________________ |
| Leading instructor | {{INSTRUKTOR}} | {{DATA_GENERACJI}} | _________________ |
| Course coordinator | {{KOORDYNATOR_KURSU}} | {{DATA_GENERACJI}} | _________________ |

---

## Project notice

The Course "Praca w tartaku" (Work in a sawmill) was created as a result of the potential developed within the project "Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Building the foundations of support for foreign nationals in the labour market of the Opolskie Voivodeship), implemented by Stowarzyszenie SMART (the SMART Association, leader) in cooperation with Fundacja pomocy prawnej EGIDA (the EGIDA Legal Aid Foundation, partner) in 2026-2027 with funding from the European Social Fund Plus. The Course itself is not financed from project funds and does not constitute a project activity; it is an independent statutory undertaking of the Foundation, conducted free of charge for the benefit of foreign nationals.

---

## Footnotes

[^1]: The template identifier specifies the version of the progress card template in the form: KP (abbreviation of "Karta Postępów", Progress Card) - version number - year of validity. The version number is incremented at each update of the template by the Foundation.

[^2]: The registration number of the progress card is assigned by the Course coordinator at the moment of card generation. The number has the form: year / sequential number within the year / KP (e.g., 2026/001/KP). Each Trainee may receive successive progress cards during the cycle (e.g., after the modular test of M1, M2, M3 and after the final test), with separate registration numbers and dates of generation.

---

*Document drawn up by Fundacja pomocy prawnej EGIDA (the EGIDA Legal Aid Foundation). Template under internal version control. The Trainee's copy and the Foundation's copy are identical in content.*
