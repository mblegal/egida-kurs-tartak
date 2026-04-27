"""
b4_op_export_sprawdzian.py

Eksporter Sprawdzianów Cząstkowych Modułu 1 z aplikacji A
(content/M1/lessons/m1-w4-l8/{lang}.md - bloki tematyczne T1/T2/T3/T4) do
Podprojektu B4-operacyjne (podprojekt-b/B4-operacyjne/O3-ocena/...).

Dla M1 generujemy 2 sprawdziany cząstkowe (po W2 i po W3) z wybranych bloków
testu modułowego:

1. SPC-M1-T12-1.0/2026 (klasa 1, 4 jęz): bloki T1 BHP + T2 Materiał drzewny
   (15 pytań, 30 pkt, 30 min, próg 70% = 21 pkt). Po W2 modułu, śródsemestralna
   diagnostyka postępu Kursanta przed wejściem w bloki proceduralne.

2. SPC-M1-T34-1.0/2026 (klasa 1, 4 jęz): bloki T3 Procesy + T4 Organizacja
   (15 pytań, 30 pkt, 30 min, próg 70% = 21 pkt). Po W3 modułu, sprawdzenie
   gotowości do testu modułowego l8.

Plus 2 klucze odpowiedzi (KOD-SPC-M1-T12 / KOD-SPC-M1-T34, klasa 3, PL only)
zawierające tabele odpowiedzi i notatki interpretacyjne dla instruktora.

Sprawdziany cząstkowe nie są generowane dla M2 i M3, ponieważ:
- m2-w4-l8 zawiera metodykę testu i próbkę 8 pytań (po 2 na obszar), nie pełną
  pulę 25 pytań - brak źródła do REUSE. Quizy uzupełniające M2 (B-OP-2a) pełnią
  funkcję post-l8.
- m3-w4-l8 jest testem końcowym Kursu (TKK-1.0/2026) - sprawdzian cząstkowy z
  części M1+M2 dublowałby TKK.

Użycie:
    python scripts/b4_op_export_sprawdzian.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE_DIR = REPO_ROOT / "content" / "M1" / "lessons" / "m1-w4-l8"
TARGET_ROOT = REPO_ROOT / "podprojekt-b" / "B4-operacyjne" / "O3-ocena"

LANGS: tuple[str, ...] = ("pl", "en", "es", "uk")
STAN_NA = "2026-04-27"

# Markery bloków pogrubionych w m1-w4-l8 per jezyk
T1_HEADERS: dict[str, str] = {
    "pl": "**T1 BHP (pytania 1-8)**",
    "en": "**T1 OHS (questions 1-8)**",
    "es": "**T1 SST (preguntas 1-8)**",
    "uk": "**T1 БЖД (питання 1-8)**",
}

T3_HEADERS: dict[str, str] = {
    "pl": "**T3 Procesy pracy (pytania 16-23)**",
    "en": "**T3 Work processes (questions 16-23)**",
    "es": "**T3 Procesos de trabajo (preguntas 16-23)**",
    "uk": "**T3 Робочі процеси (питання 16-23)**",
}

PART2_HEADERS: dict[str, str] = {
    "pl": "### Część 2: 3 scenariusze decyzyjne",
    "en": "### Part 2: 3 decision scenarios",
    "es": "### Parte 2: 3 escenarios de decisión",
    "uk": "### Частина 2: 3 сценарії рішень",
}

# Klucz odpowiedzi (PL only - dla instruktora)
KEY_TABLE_START_PL = "**Część 1 – pytania zamknięte**:"
KEY_TABLE_END_PL = "**Część 2 – scenariusze decyzyjne (kryteria oceny)**:"

# Tytuły H1
SPC_TITLE_H1: dict[tuple[str, str], str] = {
    ("pl", "T12"): "SPRAWDZIAN CZĄSTKOWY MODUŁU 1 - BLOK T1+T2 (BHP + MATERIAŁ DRZEWNY)",
    ("pl", "T34"): "SPRAWDZIAN CZĄSTKOWY MODUŁU 1 - BLOK T3+T4 (PROCESY PRACY + ORGANIZACJA)",
    ("en", "T12"): "MODULE 1 PARTIAL CHECK - BLOCK T1+T2 (OHS + WOOD MATERIAL)",
    ("en", "T34"): "MODULE 1 PARTIAL CHECK - BLOCK T3+T4 (WORK PROCESSES + ORGANIZATION)",
    ("es", "T12"): "PRUEBA PARCIAL DEL MÓDULO 1 - BLOQUE T1+T2 (SST + MATERIAL LEÑOSO)",
    ("es", "T34"): "PRUEBA PARCIAL DEL MÓDULO 1 - BLOQUE T3+T4 (PROCESOS DE TRABAJO + ORGANIZACIÓN)",
    ("uk", "T12"): "ПРОМІЖНА ПЕРЕВІРКА МОДУЛЯ 1 - БЛОК T1+T2 (БЖД + ДЕРЕВНИЙ МАТЕРІАЛ)",
    ("uk", "T34"): "ПРОМІЖНА ПЕРЕВІРКА МОДУЛЯ 1 - БЛОК T3+T4 (РОБОЧІ ПРОЦЕСИ + ОРГАНІЗАЦІЯ)",
}

KEY_TITLE_H1_PL: dict[str, str] = {
    "T12": "KLUCZ ODPOWIEDZI - SPRAWDZIAN CZĄSTKOWY MODUŁU 1 - BLOK T1+T2",
    "T34": "KLUCZ ODPOWIEDZI - SPRAWDZIAN CZĄSTKOWY MODUŁU 1 - BLOK T3+T4",
}

LEAD_SENTENCE: dict[str, str] = {
    "pl": (
        '**Kurs praktyczny „Praca w tartaku"**: kurs zawodowy dla cudzoziemców legalnie '
        "przebywających na terytorium Rzeczypospolitej Polskiej, organizowany nieodpłatnie "
        "przez Fundację pomocy prawnej EGIDA."
    ),
    "en": (
        '**Practical course "Praca w tartaku" (Work in a sawmill)**: a vocational course '
        "for foreigners legally residing in the territory of the Republic of Poland, organised "
        "free of charge by Fundacja pomocy prawnej EGIDA (EGIDA Legal Aid Foundation)."
    ),
    "es": (
        '**Curso práctico „Praca w tartaku" (Trabajo en aserradero)**: curso profesional '
        "para personas extranjeras que residen legalmente en el territorio de la República de "
        "Polonia, organizado de forma gratuita por la Fundacja pomocy prawnej EGIDA "
        "(Fundación de Asistencia Jurídica EGIDA)."
    ),
    "uk": (
        '**Практичний курс „Praca w tartaku" (Робота на лісопильні)**: професійний курс для '
        "іноземців, які легально перебувають на території Республіки Польща, що "
        "організовується безоплатно Фундацією Fundacja pomocy prawnej EGIDA (Фундація "
        "правової допомоги EGIDA)."
    ),
}

INTRO_PARA: dict[tuple[str, str], str] = {
    ("pl", "T12"): (
        "Niniejszy dokument zawiera **sprawdzian cząstkowy Modułu 1** obejmujący materiał z "
        "bloku **T1 (Bezpieczeństwo i higiena pracy)** oraz **T2 (Materiał drzewny)**. "
        "Sprawdzian jest narzędziem śródsemestralnej diagnostyki postępu Kursanta, "
        "przeprowadzanym po drugim tygodniu Modułu (przed wejściem w bloki proceduralne T3 "
        "i organizacyjne T4). Składa się z **15 pytań zamkniętych** A/B/C/D, każde po **2 "
        "punkty**, łącznie **30 punktów**, czas **30 minut**, próg pomyślnego rozwiązania "
        "**70% = 21 punktów**. Sprawdzian samodzielnie nie rozstrzyga o ukończeniu Modułu, "
        "lecz dostarcza Kursantowi i instruktorowi obrazu obszarów wymagających powtórki "
        "przed testem modułowym (lekcja l8 tygodnia 4)."
    ),
    ("pl", "T34"): (
        "Niniejszy dokument zawiera **sprawdzian cząstkowy Modułu 1** obejmujący materiał z "
        "bloku **T3 (Procesy pracy)** oraz **T4 (Organizacja)**. Sprawdzian jest narzędziem "
        "śródsemestralnej diagnostyki postępu Kursanta, przeprowadzanym po trzecim tygodniu "
        "Modułu (jako sprawdzenie gotowości do testu modułowego). Składa się z **15 pytań "
        "zamkniętych** A/B/C/D, każde po **2 punkty**, łącznie **30 punktów**, czas **30 "
        "minut**, próg pomyślnego rozwiązania **70% = 21 punktów**. Sprawdzian samodzielnie "
        "nie rozstrzyga o ukończeniu Modułu, lecz dostarcza Kursantowi i instruktorowi obrazu "
        "obszarów wymagających powtórki przed testem modułowym (lekcja l8 tygodnia 4)."
    ),
    ("en", "T12"): (
        "This document contains **the partial check of Module 1** covering the material from "
        "block **T1 (Occupational health and safety)** and **T2 (Wood material)**. The check "
        "is a tool of mid-semester diagnostics of the Trainee's progress, carried out after "
        "the second week of the Module (before entering the procedural blocks T3 and "
        "organisational T4). It consists of **15 multiple-choice questions** A/B/C/D, each "
        "worth **2 points**, totalling **30 points**, with a duration of **30 minutes** and a "
        "pass threshold of **70% = 21 points**. The check alone does not determine completion "
        "of the Module, but provides the Trainee and the instructor with a picture of the "
        "areas requiring review before the module test (lesson l8 of week 4)."
    ),
    ("en", "T34"): (
        "This document contains **the partial check of Module 1** covering the material from "
        "block **T3 (Work processes)** and **T4 (Organization)**. The check is a tool of "
        "mid-semester diagnostics of the Trainee's progress, carried out after the third week "
        "of the Module (as a readiness check before the module test). It consists of **15 "
        "multiple-choice questions** A/B/C/D, each worth **2 points**, totalling **30 "
        "points**, with a duration of **30 minutes** and a pass threshold of "
        "**70% = 21 points**. The check alone does not determine completion of the Module, "
        "but provides the Trainee and the instructor with a picture of the areas requiring "
        "review before the module test (lesson l8 of week 4)."
    ),
    ("es", "T12"): (
        "El presente documento contiene **la prueba parcial del Módulo 1** que abarca el "
        "material del bloque **T1 (Seguridad y salud en el trabajo)** y **T2 (Material "
        "leñoso)**. La prueba es una herramienta de diagnóstico de medio semestre del progreso "
        "del Kursant (cursante), realizada tras la segunda semana del Módulo (antes de entrar "
        "en los bloques procedimentales T3 y organizativos T4). Consta de **15 preguntas de "
        "opción múltiple** A/B/C/D, cada una de **2 puntos**, en total **30 puntos**, con una "
        "duración de **30 minutos** y un umbral de aprobación **70% = 21 puntos**. La prueba "
        "por sí sola no decide la finalización del Módulo, sino que proporciona al Kursant y "
        "al instructor una imagen de las áreas que requieren repaso antes del test del módulo "
        "(lección l8 de la semana 4)."
    ),
    ("es", "T34"): (
        "El presente documento contiene **la prueba parcial del Módulo 1** que abarca el "
        "material del bloque **T3 (Procesos de trabajo)** y **T4 (Organización)**. La prueba "
        "es una herramienta de diagnóstico de medio semestre del progreso del Kursant "
        "(cursante), realizada tras la tercera semana del Módulo (como verificación de "
        "preparación para el test del módulo). Consta de **15 preguntas de opción múltiple** "
        "A/B/C/D, cada una de **2 puntos**, en total **30 puntos**, con una duración de **30 "
        "minutos** y un umbral de aprobación **70% = 21 puntos**. La prueba por sí sola no "
        "decide la finalización del Módulo, sino que proporciona al Kursant y al instructor "
        "una imagen de las áreas que requieren repaso antes del test del módulo (lección l8 "
        "de la semana 4)."
    ),
    ("uk", "T12"): (
        "Цей документ містить **проміжну перевірку Модуля 1**, що охоплює матеріал блоку "
        "**T1 (Безпека життєдіяльності)** та **T2 (Деревний матеріал)**. Перевірка є "
        "інструментом діагностики прогресу Курсанта в середині семестру, що проводиться після "
        "другого тижня Модуля (перед входом у процедурні блоки T3 і організаційні T4). "
        "Складається з **15 тестових питань** A/B/C/D, кожне по **2 бали**, разом **30 "
        "балів**, тривалість **30 хвилин**, поріг успішного складання **70% = 21 бал**. "
        "Перевірка самостійно не вирішує про завершення Модуля, а надає Курсантові та "
        "інструкторові картину сфер, які потребують повторення перед тестом модуля (урок l8 "
        "тижня 4)."
    ),
    ("uk", "T34"): (
        "Цей документ містить **проміжну перевірку Модуля 1**, що охоплює матеріал блоку "
        "**T3 (Робочі процеси)** та **T4 (Організація)**. Перевірка є інструментом "
        "діагностики прогресу Курсанта в середині семестру, що проводиться після третього "
        "тижня Модуля (як перевірка готовності до тесту модуля). Складається з **15 тестових "
        "питань** A/B/C/D, кожне по **2 бали**, разом **30 балів**, тривалість **30 хвилин**, "
        "поріг успішного складання **70% = 21 бал**. Перевірка самостійно не вирішує про "
        "завершення Модуля, а надає Курсантові та інструкторові картину сфер, які потребують "
        "повторення перед тестом модуля (урок l8 тижня 4)."
    ),
}

INSTRUCTION_HEADER: dict[str, str] = {
    "pl": "## Instrukcja dla Kursanta",
    "en": "## Instructions for the Trainee",
    "es": "## Instrucciones para el Kursant (cursante)",
    "uk": "## Інструкція для Курсанта",
}

INSTRUCTION_BODY: dict[str, str] = {
    "pl": (
        "- Przeczytaj każde pytanie uważnie, **dwukrotnie** zanim zaznaczysz odpowiedź.\n"
        "- Zaznacz **jedną** odpowiedź spośród czterech (A, B, C, D).\n"
        "- Jeśli skorygujesz wybór, **przekreśl wyraźnie** poprzednią odpowiedź i zaznacz nową.\n"
        "- **Nie zostawiaj pustych pól** - puste pole liczy się jako odpowiedź błędna (0 pkt).\n"
        "- Sprawdzian wykonujesz **samodzielnie**, bez konsultacji z innymi Kursantami i bez "
        "korzystania z notatek lekcyjnych.\n"
        "- Każde pytanie warte jest **2 punkty**. Razem **30 punktów**. Próg pomyślnego "
        "rozwiązania **21 punktów (70%)**.\n"
        "- Czas trwania sprawdzianu: **30 minut**."
    ),
    "en": (
        "- Read each question carefully, **twice** before marking the answer.\n"
        "- Mark **one** answer out of four (A, B, C, D).\n"
        "- If you change your mind, **cross out clearly** the previous answer and mark the "
        "new one.\n"
        "- **Do not leave empty fields** - an empty field counts as a wrong answer (0 pts).\n"
        "- The check is performed **independently**, without consulting other Trainees and "
        "without using lesson notes.\n"
        "- Each question is worth **2 points**. Total **30 points**. Pass threshold "
        "**21 points (70%)**.\n"
        "- Duration of the check: **30 minutes**."
    ),
    "es": (
        "- Lee cada pregunta con atención, **dos veces** antes de marcar la respuesta.\n"
        "- Marca **una** respuesta entre cuatro (A, B, C, D).\n"
        "- Si cambias de opinión, **tacha claramente** la respuesta anterior y marca la nueva.\n"
        "- **No dejes campos en blanco** - un campo vacío cuenta como respuesta incorrecta "
        "(0 pts).\n"
        "- La prueba se realiza **de forma independiente**, sin consultar a otros Kursanci "
        "(cursantes) y sin usar apuntes de las lecciones.\n"
        "- Cada pregunta vale **2 puntos**. En total **30 puntos**. Umbral de aprobación "
        "**21 puntos (70%)**.\n"
        "- Duración de la prueba: **30 minutos**."
    ),
    "uk": (
        "- Прочитай кожне питання уважно, **двічі** перед позначенням відповіді.\n"
        "- Познач **одну** відповідь з чотирьох (A, B, C, D).\n"
        "- Якщо змінюєш думку, **закресли чітко** попередню відповідь і познач нову.\n"
        "- **Не залишай порожніх полів** - порожнє поле зараховується як неправильна відповідь "
        "(0 балів).\n"
        "- Перевірку виконуєш **самостійно**, без консультацій з іншими Курсантами і без "
        "використання конспектів уроків.\n"
        "- Кожне питання вартує **2 бали**. Разом **30 балів**. Поріг успішного складання "
        "**21 бал (70%)**.\n"
        "- Тривалість перевірки: **30 хвилин**."
    ),
}

QUESTIONS_HEADER: dict[str, str] = {
    "pl": "## Pytania",
    "en": "## Questions",
    "es": "## Preguntas",
    "uk": "## Питання",
}

ID_LABELS: dict[str, dict[str, str]] = {
    "pl": {
        "id_caption": "Identyfikator wzoru[^1]",
        "ev_caption": "Numer ewidencyjny sprawdzianu[^2]",
        "date_caption": "Data wypełnienia (DD-MM-RRRR)",
        "footnote_label": "Przypisy",
        "footer": (
            "*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty "
            "wewnętrzną kontrolą wersji. Egzemplarz Kursanta i egzemplarz Fundacji są "
            "tożsame co do treści.*"
        ),
    },
    "en": {
        "id_caption": "Template identifier[^1]",
        "ev_caption": "Check registration number[^2]",
        "date_caption": "Date completed (DD-MM-YYYY)",
        "footnote_label": "Footnotes",
        "footer": (
            "*Document prepared by Fundacja pomocy prawnej EGIDA. The template is subject "
            "to internal version control. The Trainee's copy and the Foundation's copy are "
            "identical in content.*"
        ),
    },
    "es": {
        "id_caption": "Identificador del modelo[^1]",
        "ev_caption": "Número de registro de la prueba[^2]",
        "date_caption": "Fecha de cumplimentación (DD-MM-AAAA)",
        "footnote_label": "Notas",
        "footer": (
            "*Documento elaborado por la Fundacja pomocy prawnej EGIDA (Fundación de "
            "Asistencia Jurídica EGIDA). Modelo sujeto a control interno de versiones. El "
            "ejemplar del Kursant (cursante) y el ejemplar de la Fundación son idénticos "
            "en cuanto a contenido.*"
        ),
    },
    "uk": {
        "id_caption": "Ідентифікатор зразка[^1]",
        "ev_caption": "Реєстраційний номер перевірки[^2]",
        "date_caption": "Дата заповнення (ДД-ММ-РРРР)",
        "footnote_label": "Виноски",
        "footer": (
            "*Документ складений Fundacją pomocy prawnej EGIDA (Фундацією правової допомоги "
            "EGIDA). Зразок підлягає внутрішньому контролю версій. Примірник Курсанта і "
            "примірник Фундації є тотожними щодо змісту.*"
        ),
    },
}

SPC_FOOTNOTE_1: dict[str, str] = {
    "pl": (
        'Identyfikator wzoru określa wersję wzoru sprawdzianu w postaci: SPC (skrót od '
        '„Sprawdzian Cząstkowy") - numer modułu - blok tematyczny (T12 albo T34) - numer '
        "wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji "
        "wzoru przez Fundację."
    ),
    "en": (
        'The template identifier specifies the version of the check template in the form: '
        'SPC (short for "Partial Check") - module number - thematic block (T12 or T34) - '
        "version number - year of validity. The version number is raised at every update of "
        "the template by the Foundation."
    ),
    "es": (
        'El identificador del modelo indica la versión del modelo de la prueba en la forma: '
        'SPC (abreviatura de „Sprawdzian Cząstkowy", prueba parcial) - número de módulo - '
        "bloque temático (T12 o T34) - número de versión - año de vigencia. El número de "
        "versión se eleva con cada actualización del modelo por parte de la Fundación."
    ),
    "uk": (
        'Ідентифікатор зразка визначає версію зразка перевірки у формі: SPC (скорочення від '
        '„Sprawdzian Cząstkowy", проміжна перевірка) - номер модуля - тематичний блок (T12 '
        "або T34) - номер версії - рік чинності. Номер версії підвищується при кожному "
        "оновленні зразка Фундацією."
    ),
}

SPC_FOOTNOTE_2: dict[str, str] = {
    "pl": (
        "Numer ewidencyjny sprawdzianu nadaje koordynator Kursu w chwili przyjęcia "
        "wypełnionego arkusza. Numer ma postać: rok / kolejny numer w roku / SPC-M1-{block} "
        "(np. 2026/001/SPC-M1-{block})."
    ),
    "en": (
        "The check registration number is assigned by the Course coordinator at the moment "
        "the completed sheet is received. The number takes the form: year / consecutive number "
        "in the year / SPC-M1-{block} (e.g. 2026/001/SPC-M1-{block})."
    ),
    "es": (
        "El número de registro de la prueba lo asigna el coordinador del Curso en el momento "
        "de la recepción de la hoja cumplimentada. El número tiene el formato: año / número "
        "correlativo en el año / SPC-M1-{block} (por ejemplo, 2026/001/SPC-M1-{block})."
    ),
    "uk": (
        "Реєстраційний номер перевірки присвоює координатор Курсу в момент прийняття "
        "заповненого аркуша. Номер має формат: рік / порядковий номер у році / SPC-M1-{block} "
        "(наприклад, 2026/001/SPC-M1-{block})."
    ),
}

PROJECT_NOTE_HEADER: dict[str, str] = {
    "pl": "Wzmianka o projekcie",
    "en": "Note on the project",
    "es": "Mención del proyecto",
    "uk": "Згадка про проєкт",
}

PROJECT_NOTE_BODY: dict[str, str] = {
    "pl": (
        'Kurs „Praca w tartaku" powstał jako rezultat potencjału wypracowanego w ramach '
        'projektu „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie '
        'opolskim", realizowanego przez Stowarzyszenie SMART (lider) we współpracy z '
        "Fundacją pomocy prawnej EGIDA (partner) w latach 2026-2027 ze środków Europejskiego "
        "Funduszu Społecznego Plus. Sam Kurs nie jest finansowany ze środków projektu i nie "
        "stanowi działania projektowego; jest niezależnym przedsięwzięciem statutowym "
        "Fundacji, prowadzonym nieodpłatnie na rzecz cudzoziemców."
    ),
    "en": (
        'The course "Praca w tartaku" (Work in a sawmill) was created as a result of the '
        'potential developed within the project "Budowa fundamentów wsparcia cudzoziemców na '
        'rynku pracy w województwie opolskim" (Building foundations for supporting foreigners '
        "in the labour market in the Opole Voivodeship), implemented by Stowarzyszenie SMART "
        "(leader) in cooperation with Fundacja pomocy prawnej EGIDA (partner) in the years "
        "2026-2027 from the resources of the European Social Fund Plus. The Course itself is "
        "not financed from project resources and does not constitute a project activity; it is "
        "an independent statutory undertaking of the Foundation, conducted free of charge for "
        "foreigners."
    ),
    "es": (
        'El Curso „Praca w tartaku" (Trabajo en aserradero) ha surgido como resultado del '
        'potencial desarrollado en el marco del proyecto „Budowa fundamentów wsparcia '
        'cudzoziemców na rynku pracy w województwie opolskim" (Construyendo los fundamentos '
        "para el apoyo a los extranjeros en el mercado laboral en el Voivodato de Opole), "
        "realizado por la Asociación SMART (líder) en colaboración con la Fundacja pomocy "
        "prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA, socio) en los años 2026-2027 "
        "con fondos del Fondo Social Europeo Plus. El Curso en sí no se financia con fondos "
        "del proyecto y no constituye una acción del proyecto; es una iniciativa estatutaria "
        "independiente de la Fundación, llevada a cabo de forma gratuita en favor de las "
        "personas extranjeras."
    ),
    "uk": (
        'Курс „Praca w tartaku" (Робота на лісопильні) виник як результат потенціалу, '
        'напрацьованого в межах проєкту „Budowa fundamentów wsparcia cudzoziemców na rynku '
        'pracy w województwie opolskim" (Розбудова основ підтримки іноземців на ринку праці '
        "в Опольському воєводстві), який реалізує Stowarzyszenie SMART (лідер) у співпраці з "
        "Fundacją pomocy prawnej EGIDA (партнер) у 2026-2027 роках із коштів Європейського "
        "соціального фонду плюс. Сам Курс не фінансується з коштів проєкту і не становить "
        "проєктного заходу; це самостійне статутне підприємство Фундації, що ведеться "
        "безоплатно на користь іноземців."
    ),
}

CHARAKTER: dict[tuple[str, str], str] = {
    ("pl", "T12"): (
        "narzędzie diagnostyczne sprawdzające postęp Kursanta po drugim tygodniu Modułu 1 "
        "Kursu w zakresie bloków T1 (Bezpieczeństwo i higiena pracy) i T2 (Materiał drzewny); "
        "wynik samodzielnie nie rozstrzyga o ukończeniu Modułu, lecz wspiera planowanie "
        "powtórek przed testem modułowym (l8)"
    ),
    ("pl", "T34"): (
        "narzędzie diagnostyczne sprawdzające postęp Kursanta po trzecim tygodniu Modułu 1 "
        "Kursu w zakresie bloków T3 (Procesy pracy) i T4 (Organizacja); wynik samodzielnie nie "
        "rozstrzyga o ukończeniu Modułu, lecz wspiera planowanie powtórek przed testem "
        "modułowym (l8)"
    ),
    ("en", "T12"): (
        "diagnostic instrument verifying the Trainee's progress after the second week of "
        "Module 1 of the Course in the scope of blocks T1 (Occupational health and safety) "
        "and T2 (Wood material); the result alone does not decide completion of the Module, "
        "but supports planning of revisions before the module test (l8)"
    ),
    ("en", "T34"): (
        "diagnostic instrument verifying the Trainee's progress after the third week of "
        "Module 1 of the Course in the scope of blocks T3 (Work processes) and T4 "
        "(Organization); the result alone does not decide completion of the Module, but "
        "supports planning of revisions before the module test (l8)"
    ),
    ("es", "T12"): (
        "instrumento diagnóstico que verifica el progreso del Kursant (cursante) tras la "
        "segunda semana del Módulo 1 del Curso en el ámbito de los bloques T1 (Seguridad y "
        "salud en el trabajo) y T2 (Material leñoso); el resultado por sí solo no decide la "
        "finalización del Módulo, sino que apoya la planificación de los repasos antes del "
        "test del módulo (l8)"
    ),
    ("es", "T34"): (
        "instrumento diagnóstico que verifica el progreso del Kursant (cursante) tras la "
        "tercera semana del Módulo 1 del Curso en el ámbito de los bloques T3 (Procesos de "
        "trabajo) y T4 (Organización); el resultado por sí solo no decide la finalización del "
        "Módulo, sino que apoya la planificación de los repasos antes del test del módulo (l8)"
    ),
    ("uk", "T12"): (
        "діагностичний інструмент перевірки прогресу Курсанта після другого тижня Модуля 1 "
        "Курсу у сфері блоків T1 (Безпека життєдіяльності) і T2 (Деревний матеріал); "
        "результат самостійно не вирішує про завершення Модуля, а підтримує планування "
        "повторень перед тестом модуля (l8)"
    ),
    ("uk", "T34"): (
        "діагностичний інструмент перевірки прогресу Курсанта після третього тижня Модуля 1 "
        "Курсу у сфері блоків T3 (Робочі процеси) і T4 (Організація); результат самостійно не "
        "вирішує про завершення Модуля, а підтримує планування повторень перед тестом модуля "
        "(l8)"
    ),
}

STRONY: dict[str, str] = {
    "pl": (
        "Kursant (rozwiązujący sprawdzian), instruktor Kursu (oceniający arkusz), Fundacja "
        "pomocy prawnej EGIDA (autor i właściciel narzędzia oceny)"
    ),
    "en": (
        "the Trainee (solving the check), the Course instructor (grading the sheet), "
        "Fundacja pomocy prawnej EGIDA (the author and owner of the assessment instrument)"
    ),
    "es": (
        "el Kursant (que resuelve la prueba), el instructor del Curso (que corrige la hoja), "
        "Fundacja pomocy prawnej EGIDA (autor y propietario del instrumento de evaluación)"
    ),
    "uk": (
        "Курсант (особа, яка проходить перевірку), інструктор Курсу (особа, яка оцінює "
        "аркуш), Fundacja pomocy prawnej EGIDA (автор і власник інструменту оцінювання)"
    ),
}

PODSTAWA_PRAWNA = (
    "  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o "
    "wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie "
    "działalności statutowej Fundacji\n"
    "  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia "
    "2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie diagnozy efektów "
    "uczenia się Kursanta"
)

EVALUATION_HEADER: dict[str, str] = {
    "pl": "## Punktacja i ocena",
    "en": "## Scoring and evaluation",
    "es": "## Puntuación y evaluación",
    "uk": "## Бали та оцінка",
}

EVALUATION_BODY: dict[str, str] = {
    "pl": (
        "- Każda poprawna odpowiedź: **2 punkty**\n"
        "- Odpowiedź błędna albo niezaznaczona: **0 punktów**\n"
        "- Suma punktów: **15 × 2 = 30 punktów**\n"
        "- Próg pomyślnego rozwiązania: **21 punktów (70%)**\n\n"
        "Po sprawdzianie instruktor zwraca Kursantowi ocenione arkusze i omawia obszary, w "
        "których Kursant uzyskał mniej niż 50% punktów w ramach pojedynczego bloku (T1, T2, "
        "T3 albo T4). Kursant otrzymuje rekomendację, do których lekcji wrócić, zanim "
        "podejdzie do testu modułowego (l8 tygodnia 4)."
    ),
    "en": (
        "- Each correct answer: **2 points**\n"
        "- Wrong or unmarked answer: **0 points**\n"
        "- Total points: **15 × 2 = 30 points**\n"
        "- Pass threshold: **21 points (70%)**\n\n"
        "After the check, the instructor returns the graded sheets to the Trainee and "
        "discusses the areas in which the Trainee obtained less than 50% of points within a "
        "single block (T1, T2, T3 or T4). The Trainee receives a recommendation as to which "
        "lessons to revisit before approaching the module test (l8 of week 4)."
    ),
    "es": (
        "- Cada respuesta correcta: **2 puntos**\n"
        "- Respuesta incorrecta o sin marcar: **0 puntos**\n"
        "- Total de puntos: **15 × 2 = 30 puntos**\n"
        "- Umbral de aprobación: **21 puntos (70%)**\n\n"
        "Tras la prueba, el instructor devuelve al Kursant las hojas corregidas y comenta las "
        "áreas en las que el Kursant ha obtenido menos del 50% de los puntos dentro de un "
        "solo bloque (T1, T2, T3 o T4). El Kursant recibe una recomendación sobre a qué "
        "lecciones volver antes de presentarse al test del módulo (l8 de la semana 4)."
    ),
    "uk": (
        "- Кожна правильна відповідь: **2 бали**\n"
        "- Неправильна або непозначена відповідь: **0 балів**\n"
        "- Сума балів: **15 × 2 = 30 балів**\n"
        "- Поріг успішного складання: **21 бал (70%)**\n\n"
        "Після перевірки інструктор повертає Курсантові оцінені аркуші та обговорює сфери, у "
        "яких Курсант отримав менше 50% балів у межах одного блоку (T1, T2, T3 або T4). "
        "Курсант отримує рекомендацію щодо того, до яких уроків повернутися перед тим, як "
        "приступити до тесту модуля (l8 тижня 4)."
    ),
}

KEY_INTRO_PL: dict[str, str] = {
    "T12": (
        "Niniejszy dokument zawiera **klucz odpowiedzi do sprawdzianu cząstkowego Modułu 1 "
        "(blok T1+T2)** wraz z punktacją i notatkami interpretacyjnymi dla instruktora. "
        "Dokument jest **wewnętrznym narzędziem instruktorskim** i **nie podlega wydawaniu "
        "Kursantom** ani podmiotom zewnętrznym. Klucz służy obiektywnej ocenie arkuszy "
        "odpowiedzi po przeprowadzeniu sprawdzianu po drugim tygodniu Modułu 1."
    ),
    "T34": (
        "Niniejszy dokument zawiera **klucz odpowiedzi do sprawdzianu cząstkowego Modułu 1 "
        "(blok T3+T4)** wraz z punktacją i notatkami interpretacyjnymi dla instruktora. "
        "Dokument jest **wewnętrznym narzędziem instruktorskim** i **nie podlega wydawaniu "
        "Kursantom** ani podmiotom zewnętrznym. Klucz służy obiektywnej ocenie arkuszy "
        "odpowiedzi po przeprowadzeniu sprawdzianu po trzecim tygodniu Modułu 1."
    ),
}

KEY_FOOTNOTE_1_PL_TEMPLATE = (
    'Identyfikator wzoru określa wersję wzoru klucza w postaci: KOD-SPC (skrót od „Klucz '
    'Odpowiedzi do Sprawdzianu Cząstkowego") - numer modułu - blok tematyczny ({block}) - '
    "numer wersji - rok obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji "
    "wzoru przez Fundację. Klucz odpowiada wzorowi sprawdzianu SPC-M1-{block}-1.0/2026."
)

KEY_FOOTNOTE_2_PL_TEMPLATE = (
    "Numer ewidencyjny ocenionego arkusza nadaje koordynator albo instruktor Kursu w "
    "chwili oceny. Numer ma postać: rok / kolejny numer w roku / SPC-M1-{block}-OCN (np. "
    "2026/001/SPC-M1-{block}-OCN)."
)

KEY_INTERPRETATION_PL: dict[str, str] = {
    "T12": (
        "## Notatki interpretacyjne dla instruktora\n\n"
        "**Skala interpretacji wyniku Kursanta po sprawdzianie T1+T2:**\n\n"
        "- **27-30 punktów (90-100%)**: bardzo dobre opanowanie bloków BHP i Materiał. "
        "Kursant gotowy do bloków proceduralnych T3 i organizacyjnych T4.\n"
        "- **21-26 punktów (70-86%)**: dobre opanowanie. Kontynuacja Modułu bez konieczności "
        "powtórek.\n"
        "- **15-20 punktów (50-66%)**: pozytywne tempo, ale luka. Instruktor wskazuje "
        "konkretne lekcje T1 albo T2 do powtórki w wieczornej sesji konsultacyjnej.\n"
        "- **0-14 punktów (poniżej 50%)**: poważny sygnał ostrzegawczy. Instruktor planuje "
        "indywidualną sesję powtórkową (1-2 godziny) przed wejściem w T3, oraz informuje "
        "koordynatora.\n\n"
        "**Reguła analizy bloków**: jeśli Kursant uzyskał poniżej 50% punktów w ramach "
        "pojedynczego bloku (T1 albo T2), instruktor wskazuje konkretną lekcję, której "
        'fragment dotyczy nieprawidłowych odpowiedzi (kolumna „Źródło" w kluczu).\n\n'
        "**Reguła rozmowy zwrotnej**: instruktor zwraca arkusze najpóźniej 24 godziny po "
        "sprawdzianie. Rozmowa zwrotna z Kursantem trwa 5-10 minut i koncentruje się na "
        "obszarach niedoboru, nie na liczbie punktów."
    ),
    "T34": (
        "## Notatki interpretacyjne dla instruktora\n\n"
        "**Skala interpretacji wyniku Kursanta po sprawdzianie T3+T4:**\n\n"
        "- **27-30 punktów (90-100%)**: bardzo dobre opanowanie bloków proceduralnego i "
        "organizacyjnego. Kursant gotowy do testu modułowego (l8) bez dodatkowych powtórek.\n"
        "- **21-26 punktów (70-86%)**: dobre opanowanie. Instruktor sygnalizuje pojedyncze "
        "luki do utrwalenia w piątym dniu Modułu (l1-l7 tygodnia 4).\n"
        "- **15-20 punktów (50-66%)**: ostrzeżenie. Instruktor planuje sesję powtórkową "
        "obejmującą zarówno blok T3, jak i T4, w przeddzień testu modułowego.\n"
        "- **0-14 punktów (poniżej 50%)**: krytyczny sygnał. Test modułowy (l8) możliwy do "
        "odroczenia o tydzień, jeśli zgodnie z decyzją koordynatora wymaga to dodatkowych "
        "lekcji powtórkowych. Informacja do koordynatora obowiązkowa.\n\n"
        "**Reguła analizy bloków**: jeśli Kursant uzyskał poniżej 50% punktów w ramach "
        "pojedynczego bloku (T3 albo T4), instruktor wskazuje konkretną lekcję, której "
        'fragment dotyczy nieprawidłowych odpowiedzi (kolumna „Źródło" w kluczu).\n\n'
        "**Reguła rozmowy zwrotnej**: instruktor zwraca arkusze najpóźniej 24 godziny po "
        "sprawdzianie. Rozmowa zwrotna z Kursantem trwa 5-10 minut i koncentruje się na "
        "obszarach niedoboru, nie na liczbie punktów."
    ),
}


def parse_questions(path: Path, lang: str, block: str) -> str:
    """Wytnij sekcję pytań dla danego bloku z m1-w4-l8/{lang}.md.

    block = 'T12' oznacza T1+T2 (pytania 1-15)
    block = 'T34' oznacza T3+T4 (pytania 16-30)
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: brak frontmattera")
    yaml_end = text.find("\n---\n", 4)
    if yaml_end == -1:
        raise ValueError(f"{path}: niezamknięty frontmatter")
    body = text[yaml_end + 5 :]

    t1 = T1_HEADERS[lang]
    t3 = T3_HEADERS[lang]
    part2 = PART2_HEADERS[lang]

    t1_offset = body.find(t1)
    t3_offset = body.find(t3)
    part2_offset = body.find(part2)

    if t1_offset == -1:
        raise ValueError(f"{path}: nie znaleziono '{t1}'")
    if t3_offset == -1:
        raise ValueError(f"{path}: nie znaleziono '{t3}'")
    if part2_offset == -1:
        raise ValueError(f"{path}: nie znaleziono '{part2}'")

    if block == "T12":
        section = body[t1_offset:t3_offset].rstrip()
    elif block == "T34":
        section = body[t3_offset:part2_offset].rstrip()
    else:
        raise ValueError(f"Nieznany blok {block}")

    return section + "\n"


def parse_key_pl(block: str) -> str:
    """Wytnij wiersze tabeli klucza odpowiedzi dla danego bloku z m1-w4-l8/pl.md.

    Tabela ma 30 wierszy (pytania 1-30). Dla T12 zostawiamy 1-15, dla T34 16-30.
    """
    src = SOURCE_FILE_DIR / "pl.md"
    text = src.read_text(encoding="utf-8")

    table_start = text.find(KEY_TABLE_START_PL)
    table_end = text.find(KEY_TABLE_END_PL)
    if table_start == -1 or table_end == -1:
        raise ValueError("PL: nie znaleziono granic tabeli klucza w m1-w4-l8")

    raw = text[table_start:table_end]
    lines = raw.split("\n")
    header_idx = None
    sep_idx = None
    rows: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        if line.startswith("| # |") and "Odpowiedź" in line:
            header_idx = i
        elif header_idx is not None and sep_idx is None and line.startswith("|---"):
            sep_idx = i
        elif sep_idx is not None and line.startswith("|") and not line.startswith("|---"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if parts and parts[0].isdigit():
                rows.append((int(parts[0]), line))
            elif parts and parts[0] == "":
                continue

    if header_idx is None or sep_idx is None or len(rows) < 30:
        raise ValueError(f"PL: nieprawidłowa tabela klucza (rows={len(rows)})")

    if block == "T12":
        wanted = [r for r in rows if 1 <= r[0] <= 15]
    elif block == "T34":
        wanted = [r for r in rows if 16 <= r[0] <= 30]
    else:
        raise ValueError(f"Nieznany blok {block}")

    out: list[str] = []
    out.append(lines[header_idx])
    out.append(lines[sep_idx])
    for _, line in wanted:
        out.append(line)
    return "\n".join(out) + "\n"


def build_yaml(lang: str, block: str) -> str:
    return (
        f"---\n"
        f"typ: sprawdzian\n"
        f"dokument: sprawdzian cząstkowy Modułu 1 (blok {block}: "
        f'{"T1 BHP + T2 Materiał drzewny" if block == "T12" else "T3 Procesy pracy + T4 Organizacja"})\n'
        f"kurs: Praca w tartaku\n"
        f"podprojekt: B\n"
        f"faza: B4-operacyjne\n"
        f"grupa: O3-ocena\n"
        f"język: {lang}\n"
        f"wersja: 1.0\n"
        f"stan-na: {STAN_NA}\n"
        f"podstawa-prawna:\n"
        f"{PODSTAWA_PRAWNA}\n"
        f"charakter: {CHARAKTER[(lang, block)]}\n"
        f"strony: {STRONY[lang]}\n"
        f"---\n"
    )


def build_key_yaml(block: str) -> str:
    return (
        f"---\n"
        f"typ: klucz odpowiedzi\n"
        f"dokument: klucz odpowiedzi do sprawdzianu cząstkowego Modułu 1 (blok {block}: "
        f'{"T1 BHP + T2 Materiał drzewny" if block == "T12" else "T3 Procesy pracy + T4 Organizacja"}); '
        f"narzędzie instruktorskie do oceny arkuszy\n"
        f"kurs: Praca w tartaku\n"
        f"podprojekt: B\n"
        f"faza: B4-operacyjne\n"
        f"grupa: O3-ocena\n"
        f"język: pl\n"
        f"wersja: 1.0\n"
        f"stan-na: {STAN_NA}\n"
        f"podstawa-prawna:\n"
        f"{PODSTAWA_PRAWNA}\n"
        f"charakter: dokument wewnętrzny Fundacji wykorzystywany przez instruktora do "
        f"oceny arkuszy odpowiedzi sprawdzianu cząstkowego Modułu 1 ({block}); nie podlega "
        f"wydawaniu Kursantom ani podmiotom zewnętrznym\n"
        f"strony: instruktor Kursu (oceniający), Fundacja pomocy prawnej EGIDA (autor i "
        f"właściciel klucza)\n"
        f"---\n"
    )


def build_id_table(lang: str, identifier: str) -> str:
    labels = ID_LABELS[lang]
    return (
        f"| {labels['id_caption']} | {labels['ev_caption']} | {labels['date_caption']} |\n"
        f"|---|---|---|\n"
        f"| {identifier} | | |\n"
    )


def build_sprawdzian_document(lang: str, block: str, questions_body: str) -> str:
    identifier = f"SPC-M1-{block}-1.0/2026"
    labels = ID_LABELS[lang]
    parts: list[str] = []
    parts.append(build_yaml(lang, block))
    parts.append("")
    parts.append(f"# {SPC_TITLE_H1[(lang, block)]}")
    parts.append("")
    parts.append(LEAD_SENTENCE[lang])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(INTRO_PARA[(lang, block)])
    parts.append("")
    parts.append(build_id_table(lang, identifier))
    parts.append("---")
    parts.append("")
    parts.append(INSTRUCTION_HEADER[lang])
    parts.append("")
    parts.append(INSTRUCTION_BODY[lang])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(QUESTIONS_HEADER[lang])
    parts.append("")
    parts.append(questions_body.rstrip())
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(EVALUATION_HEADER[lang])
    parts.append("")
    parts.append(EVALUATION_BODY[lang])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(f"## {PROJECT_NOTE_HEADER[lang]}")
    parts.append("")
    parts.append(PROJECT_NOTE_BODY[lang])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(f"## {labels['footnote_label']}")
    parts.append("")
    parts.append(f"[^1]: {SPC_FOOTNOTE_1[lang]}")
    parts.append("")
    parts.append(f"[^2]: {SPC_FOOTNOTE_2[lang].format(block=block)}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(labels["footer"])
    parts.append("")
    return "\n".join(parts)


def build_key_document(block: str, key_table: str) -> str:
    identifier = f"KOD-SPC-M1-{block}-1.0/2026"
    parts: list[str] = []
    parts.append(build_key_yaml(block))
    parts.append("")
    parts.append(f"# {KEY_TITLE_H1_PL[block]}")
    parts.append("")
    parts.append(
        "**Dokument wewnętrzny Fundacji pomocy prawnej EGIDA**: narzędzie instruktorskie "
        "do oceny arkuszy odpowiedzi sprawdzianu cząstkowego Modułu 1 "
        f'(blok {block}) Kursu praktycznego „Praca w tartaku".'
    )
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(KEY_INTRO_PL[block])
    parts.append("")
    parts.append(
        "| Identyfikator wzoru[^1] | Numer ewidencyjny ocenionego arkusza[^2] | "
        "Data oceny (DD-MM-RRRR) |"
    )
    parts.append("|---|---|---|")
    parts.append(f"| {identifier} | | |")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Klucz odpowiedzi")
    parts.append("")
    parts.append(key_table.rstrip())
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(KEY_INTERPRETATION_PL[block])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Przypisy")
    parts.append("")
    parts.append(f"[^1]: {KEY_FOOTNOTE_1_PL_TEMPLATE.format(block=block)}")
    parts.append("")
    parts.append(f"[^2]: {KEY_FOOTNOTE_2_PL_TEMPLATE.format(block=block)}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(
        "*Dokument sporządzony przez Fundację pomocy prawnej EGIDA. Wzór objęty wewnętrzną "
        "kontrolą wersji. Dokument wewnętrzny - nie podlega wydawaniu Kursantom ani "
        "podmiotom zewnętrznym.*"
    )
    parts.append("")
    return "\n".join(parts)


def sprawdzian_target_dir(block: str, idx: int) -> Path:
    return TARGET_ROOT / f"{idx:02d}-sprawdzian-czastkowy-M1-{block}"


def key_target_dir(block: str, idx: int) -> Path:
    return TARGET_ROOT / f"{idx:02d}-klucz-sprawdzianu-M1-{block}"


def export() -> list[Path]:
    written: list[Path] = []
    blocks_layout = [
        ("T12", 10, 12),  # spr T12 -> 10, klucz T12 -> 12
        ("T34", 11, 13),  # spr T34 -> 11, klucz T34 -> 13
    ]

    for block, sp_idx, key_idx in blocks_layout:
        sp_dir = sprawdzian_target_dir(block, sp_idx)
        sp_dir.mkdir(parents=True, exist_ok=True)
        for lang in LANGS:
            src = SOURCE_FILE_DIR / f"{lang}.md"
            if not src.exists():
                print(f"[SKIP] {src} nie istnieje", file=sys.stderr)
                continue
            questions = parse_questions(src, lang, block)
            out = sp_dir / f"{lang}.md"
            out.write_bytes(build_sprawdzian_document(lang, block, questions).encode("utf-8"))
            written.append(out)

        key_dir = key_target_dir(block, key_idx)
        key_dir.mkdir(parents=True, exist_ok=True)
        key_table = parse_key_pl(block)
        out_key = key_dir / "pl.md"
        out_key.write_bytes(build_key_document(block, key_table).encode("utf-8"))
        written.append(out_key)

    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    print("=== Sprawdziany czastkowe Modulu 1 (SPC-M1-T12 + SPC-M1-T34) ===")
    written = export()
    for p in written:
        size = p.stat().st_size
        print(f"  {p.relative_to(REPO_ROOT)}  ({size} bytes)")

    print(f"\nZapisano {len(written)} plikow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
