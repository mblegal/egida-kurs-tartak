# RAPORT B-OP-2a - Ocena cz.1 (quizy uzupełniające + karta odpowiedzi + klucze)

**Data zamknięcia:** 2026-04-27
**Zakres:** Podprojekt B / B4-operacyjne / O3-ocena (3 typy nowych dokumentów)
**Stan walidacji:** PASS na pełnej linii (validate_b4_op.py: 69/69 OK, B-OP-1 + B-OP-2a)

---

## Co dostarczamy

Sprint B-OP-2a uzupełnia rdzeń dokumentacji operacyjnej Kursu o pierwszą warstwę narzędzi oceny dydaktycznej: **quizy uzupełniające** dla każdego z trzech Modułów (M1, M2, M3), uniwersalną **kartę odpowiedzi** wypełnianą przez Kursanta oraz **klucze odpowiedzi** dla instruktora. Dokumenty domykają lukę z B-OP-1, gdzie warstwa oceny była reprezentowana wyłącznie przez zbiorczą kartę obecności (decyzja o dopuszczeniu do testu końcowego). Po B-OP-2a operacyjna ocena pierwszego rzędu (per Moduł, w trybie samooceny i poprawkowym) jest zaopatrzona w komplet narzędzi.

**Trzy filary B-OP-2a:**

- **Filar I - narzędzie oceny dla Kursanta (4 jęz):** 12 plików Quiz Uzupełniający Modułu × 4 jęz (PL/EN/ES/UK). Treść 1:1 z aplikacji A (`content/M{1,2,3}/artifacts/quiz-uzupelniajacy/`), wycięte sekcje klucza/punktacji/notatek (kursant nie może otrzymać klucza).
- **Filar II - karta wypełniana ręcznie (4 jęz, parametryzowana):** 4 pliki MD + 4 DOCX templates uniwersalnej karty odpowiedzi z maksymalną siatką 30 zamkniętych + 15 otwartych + 10 case'ów. Generator CSV→DOCX wstawia parametry edycji.
- **Filar III - narzędzie oceny dla instruktora (PL only):** 3 pliki Klucz Odpowiedzi × Moduł, klasa 3 dokument wewnętrzny zawierający klucz + uzasadnienia + punktację + interpretację wyników + notatki metodyczne.

---

## Liczbowo

| Klasa funkcjonalna | Charakterystyka | Typów | Plików MD | Bytes MD |
|---|---|---|---|---|
| Klasa 1 (kursant) - Quiz Uzupełniający Modułu | Kursant czyta i wpisuje odpowiedzi w karcie odpowiedzi | 3 (M1/M2/M3) | 12 | 230,9 KB |
| Klasa 2 (parametryzowana) - Karta Odpowiedzi | Koordynator generuje DOCX per cykl z CSV; Kursant wypełnia ręcznie | 1 (uniwersalna) | 4 | 51,6 KB |
| Klasa 3 (instruktor) - Klucz Odpowiedzi | Dokument wewnętrzny do oceny arkuszy Kursantów | 3 (M1/M2/M3) | 3 | 24,0 KB |
| **Razem MD** | | **7** | **19** | **306,5 KB** |
| DOCX templates klasy 2 (Pandoc) | Karta odpowiedzi × 4 jęz | - | 4 | 62,5 KB |
| Skrypt eksportera | b4_op_export_quiz.py | - | 1 | ~14 KB |
| Sample CSV | sample_karty_odpowiedzi.csv | - | 1 | ~0,4 KB |
| **Razem artefakty B-OP-2a** | | - | **25** | **~383 KB** |

---

## Inwentarz typów

### O3 Ocena Kursanta (cz.1)

| # | Typ | Identyfikator | Klasa | Języki | Liczba plików |
|---|---|---|---|---|---|
| 1 | Quiz Uzupełniający Modułu 1 | QUM-M1-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 2 | Quiz Uzupełniający Modułu 2 | QUM-M2-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 3 | Quiz Uzupełniający Modułu 3 | QUM-M3-1.0/2026 | 1 | PL/EN/ES/UK | 4 |
| 4 | Klucz Odpowiedzi do QUM Modułu 1 | KOD-QUM-M1-1.0/2026 | 3 | PL only | 1 |
| 5 | Klucz Odpowiedzi do QUM Modułu 2 | KOD-QUM-M2-1.0/2026 | 3 | PL only | 1 |
| 6 | Klucz Odpowiedzi do QUM Modułu 3 | KOD-QUM-M3-1.0/2026 | 3 | PL only | 1 |
| 7 | Karta Odpowiedzi (uniwersalna) | KO-1.0/2026 | 2 | PL/EN/ES/UK + 4 DOCX | 4 + 4 DOCX |

---

## Architektura

### Konwencja plików (zgodna z B-OP-1)

```
podprojekt-b/B4-operacyjne/
└── O3-ocena/
    ├── 01-quiz-uzupelniajacy-M1/      pl.md  en.md  es.md  uk.md
    ├── 02-quiz-uzupelniajacy-M2/      pl.md  en.md  es.md  uk.md
    ├── 03-quiz-uzupelniajacy-M3/      pl.md  en.md  es.md  uk.md
    ├── 04-klucz-quizu-M1/             pl.md
    ├── 05-klucz-quizu-M2/             pl.md
    ├── 06-klucz-quizu-M3/             pl.md
    └── 07-karta-odpowiedzi/           pl.md  en.md  es.md  uk.md
        └── templates/                 template_{pl,en,es,uk}.docx
```

### Pipeline narzędziowy (rozszerzony)

| Skrypt | Funkcja | Status |
|---|---|---|
| `b4_op_export_quiz.py` | NOWY: czyta `content/Mn/artifacts/quiz-uzupelniajacy/{lang}.md` aplikacji A, dzieli na quiz dla kursanta (bez klucza) i klucz dla instruktora (PL only); generuje YAML B-OP, identyfikatory, EFS+ wzmiankę, przypisy | nowy |
| `b4_op_build_templates.py` | Rozszerzony o 1 nowy typ klasy 2 (KO × 4 jęz) | rozszerzony |
| `b4_op_generate.py` | Rozszerzony o typ `karta-odpowiedzi` z 13 placeholderami substytuowanymi z CSV | rozszerzony |
| `validate_b4_op.py` | Rozszerzony o 7 wpisów (3 QUM klasy 1, 3 KOD klasy 3, 1 KO klasy 2) | rozszerzony |
| `build_b4_op.py` | Bez zmian, działa z rozszerzonym walidatorem i build templates | bez zmian |

### Kluczowa decyzja produktowa: rozdzielenie klucz↔quiz

W aplikacji A pliki źródłowe `content/M{1,2,3}/artifacts/quiz-uzupelniajacy/{lang}.md` zawierają **zarówno pytania, jak i klucz odpowiedzi inline** (kursant czyta plik na ekranie aplikacji, klucz jest dla niego widoczny po teście). W B-OP-2a, gdzie quiz przechodzi do trybu druku i wypełniania ręcznego, ta inline'owa struktura jest niedopuszczalna: **kursant nie może otrzymać dokumentu z kluczem odpowiedzi w tej samej kartce**.

Eksporter `b4_op_export_quiz.py` rozwiązuje ten problem przez parsowanie struktury markdown i lokalizowanie nagłówka „Klucz odpowiedzi" (lub jego ekwiwalentu w EN/ES/UK). Sekcje od tego nagłówka do końca pliku trafiają do osobnego pliku `klucz-quizu-Mn/pl.md` (klasa 3, PL only, dokument wewnętrzny). Sekcje przed tym nagłówkiem (Przeznaczenie, Instrukcja, Klucz rozkładu w M2, Pytania) trafiają do pliku quizu kursanta. Eksporter ponadto dodaje YAML B-OP, identyfikator wzoru, wzmiankę EFS+ (tylko w pliku kursanta - klucz jest dokumentem wewnętrznym), oraz znormalizowane przypisy.

### Karta odpowiedzi: max-rows zamiast dynamic-resize

Quizy uzupełniające mają różną strukturę per Moduł:
- M1: 15 zamkniętych A/B/C/D
- M2: 30 zamkniętych + 15 otwartych + 10 case'ów = 55 pozycji
- M3: 15 mieszanych (A/B/C/D + uzasadnienie pisemne 2-3 zdań)

Karta odpowiedzi rozwiązuje tę zmienność przez **maksymalną stałą siatkę** dopasowaną do M2 (największy moduł): 30 wierszy zamkniętych z kolumnami A/B/C/D/„nie wiem"/uzasadnienie + 15 boxów odpowiedzi otwartych po 4 linie + 10 boxów case'ów po 7 linii. Generator nie modyfikuje struktury DOCX; parametry CSV (`LICZBA_ZAMKNIETYCH`, `LICZBA_OTWARTYCH`, `LICZBA_CASEOW`) trafiają do nagłówka karty informując Kursanta ile pól ma faktycznie wypełnić. Niewykorzystane wiersze pozostają puste albo są przekreślone ukośnikiem.

To rozwiązanie kompromisowe: kosztem nieco zbyt obszernej karty dla M1 (15 zamkniętych z 30 dostępnych) zachowuje **jeden uniwersalny szablon** zamiast trzech osobnych per Moduł. Generator pozostaje prosty (substytucja placeholderów bez modyfikacji struktury DOCX).

---

## Dyscyplina jakościowa

Wszystkie 19 plików MD i 4 DOCX templates (łącznie 23 artefakty B-OP-2a) przeszły walidację:

- **0 em-dashów** (znak `—` zakazany regułą feedback);
- **YAML frontmatter** kompletny w każdym pliku (typ, dokument, kurs, podprojekt, faza, grupa, język, wersja, stan-na, podstawa-prawna, charakter, strony, plus dla klasy 2: parametry);
- **Identyfikator wzoru** (np. QUM-M1-1.0/2026, KOD-QUM-M1-1.0/2026, KO-1.0/2026) obecny w każdym pliku;
- **Język-specific:**
  - PL pełne diakrytyki (ą/ć/ę/ł/ń/ó/ś/ź/ż);
  - UK kirylica >60% w plikach pełnych (81% w karcie odpowiedzi UK, 5211 znaków cyrylicy); ї obecne (różnicowanie od rosyjskiego);
  - ES brak bug-a „ano" (zawsze „año"), ñ obecne (7 wystąpień w karcie odpowiedzi ES);
  - EN bez polskich naleciałości w treści (ale PL nazwy własne i tytuły ustaw zachowane);
- **Tytuły polskich ustaw** zachowane w PL z tłumaczeniem w nawiasie przy pierwszym wystąpieniu;
- **Wzmianka EFS+** obecna w plikach klasy 1 (kursant) i klasy 2 (parametryzowane); pominięta w plikach klasy 3 (klucze, dokumenty wewnętrzne) zgodnie z regułą Part 45.

Klasa 2 dodatkowo:
- **14 unique placeholderów `{{PLACEHOLDER}}`** (13 substytuowanych z CSV + 1 dokumentacyjny `{{NAZWA_POLA}}`) zachowanych jednoznacznie między PL/EN/ES/UK i DOCX templates;
- **End-to-end test:** sample_karty_odpowiedzi.csv (3 wiersze: Iryna M1 samoocena, Carlos M2 samoocena, Iryna M3 poprawkowy) → generator → 3 wypełnione DOCX z poprawnym podstawieniem wszystkich 13 placeholderów (Iryna Kowalenko, QUM-M1-1.0/2026, 2026/C1/001/KO, 22-09-2026, Anna Nowak, samoocena), 0 em-dashów.

### Workflow tłumaczeniowy (siódma sesja z 0 ręcznymi korektami)

Klasa 1 i klasa 3: brak subagentów - eksporter Python robi 1:1 transfer treści 4-językowej z aplikacji A do B-OP. Treść quizów istnieje już w 4 językach (Parts 27-32 dyscyplina). To zgodne z feedback `generator-vs-subagent`: dane strukturyzowane → Python skrypt.

Klasa 2 (karta odpowiedzi): tradycyjny workflow tłumaczeniowy z trzema agentami EN/ES/UK równolegle, każdy z **inline weryfikacją Python** (feedback `subagent-inline-verification`). Wyniki: wszystkie trzy agenty zwróciły „ALL CHECKS PASSED" w pierwszym uruchomieniu (em-dash=0, 14/14 placeholderów, ID wzoru zachowany, kirylica/ñ/diakrytyki w niezmiennikach), 0 ręcznych korekt głównego agenta. **Siódma sesja z rzędu z taką dyscypliną** (Parts 27-32, 47).

---

## Workflow koordynatora po B-OP-2a

1. **Po teście l8 Modułu** (gdy zdany): drukuje arkusz Quiz Uzupełniający Modułu (PL + język Kursanta) i przekazuje Kursantowi do trybu samooceny. Wraz z arkuszem przekazuje wygenerowaną kartę odpowiedzi DOCX (z parametrów CSV cyklu).
2. **Po teście l8 Modułu** (gdy nie zdany): drukuje quiz w trybie poprawkowym, dolicza wynik do testu l8 do progu 70% z sumy.
3. **Po wypełnieniu**: zbiera kartę odpowiedzi od Kursanta. Instruktor ocenia z użyciem Klucza Odpowiedzi (KOD-QUM-Mn-1.0/2026, PL only, dokument wewnętrzny).
4. **Generowanie kart**: `python scripts/b4_op_generate.py --typ karta-odpowiedzi --lang pl --csv data/edycja_C1_2026_quizy.csv --output-dir dist/edycja_C1_2026/karty/`
5. **Aktualizacja quizów**: gdy zmienia się treść quizu w aplikacji A (`content/M{1,2,3}/artifacts/quiz-uzupelniajacy/`), uruchom `python scripts/b4_op_export_quiz.py` aby zregenerować pliki w `O3-ocena/`. Walidator weryfikuje spójność.

---

## Co poza zakresem B-OP-2a (kolejne sprinty)

**Sprint B-OP-2b** - sprawdziany cząstkowe + test końcowy + arkusze:
- 6 sprawdzianów cząstkowych × 4 jęz (podzbiory quizu modułowego, np. T1, T2, T3, T4 per Moduł)
- 1 test końcowy Kursu × 4 jęz (proporcja 20% M1 / 30% M2 / 50% M3)
- Protokół z testu końcowego
- Karta postępów Kursanta (sumator wyników)
- Zestawienie zbiorcze ocen cyklu
- Indywidualny arkusz oceny instruktora (jakościowy)

**Sprint B-OP-3** - zamknięcie i archiwizacja edycji:
- Protokół zakończenia kursu
- Lista absolwentów
- Rejestr wydanych zaświadczeń (łączy się z B1 zaświadczeniami modułowymi)
- Ankieta ewaluacyjna uczestnika (4 jęz)
- Ankieta ewaluacyjna instruktora (PL)
- Raport końcowy edycji
- Karta edycji kursu (master record edycji)
- Spis dokumentacji edycji (manifest archiwalny)

**Sprint B-OP-4 (opcja)** - dokumenty incydentalne.

**Hub kursu (`prezentacje.m-b.legal/kurs-tartak/dokumenty/operacyjne/`):** sekcja na hubie do wdrożenia po zamknięciu B-OP-3, obejmująca wszystkie grupy O1-O4.

---

## Lekcje techniczne

W trakcie sprintu wykryto i naprawiono dwa Windows-specific bugi (oba zaktualizowane w pamięci projektu):

1. **`Path.write_text` na Windows daje CRLF**: początkowo eksporter pisał pliki z line endings `\r\n`, walidator szukający `\n---\n` (nagłówka YAML) zawodził. Naprawione przez `write_bytes(s.encode('utf-8'))`. Memo: `feedback-python-write-text-windows-crlf.md`.
2. **`python -c "..."` z polskimi stringami w bash-Windows niszczy diakrytyki**: próba edycji eksportera przez `python -c` zaśmieciła polskie znaki (`„Praca` → `�Praca`) bo bash przekazuje argumenty w cp1250. Reguła rozszerzona: do edycji plików z polskim tekstem na Windows używać Edit/Write tool, nigdy `python -c`. Memo: `feedback-curl-pipe-python-windows-encoding.md` (rozszerzony).

---

## Ślad commitów

Sprint B-OP-2a: jeden commit Part 47 z całością artefaktów (19 MD + 4 DOCX + 1 nowy skrypt + 3 zmodyfikowane skrypty + sample CSV + raport).

---

## Sygnały do następnej iteracji

Brak dostrzeżonych technical debt-ów wewnątrz B-OP-2a. Walidator oznaczył wszystkie 23 artefakty B-OP-2a jako OK; pełna walidacja (B-OP-1 + B-OP-2a) - 69/69 OK. End-to-end test wypełnia 13 placeholderów 100%. Brak sygnałów wymagających poprawek przed sprintem B-OP-2b.

Jedna kwestia do potwierdzenia z koordynatorem rzeczowym przed B-OP-2b: **czy struktura testu końcowego l8** (108 pkt, próg 76 pkt, proporcja 20% M1 / 30% M2 / 50% M3 zgodnie z M3 quiz uzupełniającym) **jest zatwierdzonym wzorem**, czy podlega rewizji. Test końcowy będzie głównym artefaktem B-OP-2b i zmiana jego struktury wymusiłaby aktualizację wzorów MD oraz prawdopodobnie protokołu z testu końcowego.

Druga kwestia: **czy karta odpowiedzi z stałą siatką 30+15+10** sprawdzi się w praktycznej eksploatacji, czy koordynator zażąda osobnych wzorów per Moduł (D2=B z propozycji architektury). Decyzja oparta na empirii pierwszej edycji cyklu.
