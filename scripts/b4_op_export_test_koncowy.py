"""
b4_op_export_test_koncowy.py

Eksporter Testu Końcowego Kursu z aplikacji A
(content/M3/lessons/m3-w4-l8/{lang}.md - lekcja jest jednocześnie testem końcowym
całego Kursu, 108 pkt, próg 70% = 76 pkt, proporcja 20/30/50 M1/M2/M3) do
Podprojektu B4-operacyjne (podprojekt-b/B4-operacyjne/O3-ocena/...).

Z każdego pliku źródłowego (4 jęz) produkuje:

1. Test Końcowy Kursu (TKK-1.0/2026, klasa 1, 4 jęz):
   pełna treść testu (Wprowadzenie + Cele + Instrukcja + Część 1 + Część 2 + Część 3)
   BEZ klucza odpowiedzi i bez sekcji „Kluczowe terminy" / „Sprawdź siebie",
   z YAML B-OP, identyfikatorem wzoru, wzmianką EFS+ i przypisami.

2. Klucz odpowiedzi do testu końcowego (KOD-TKK-1.0/2026, klasa 3, PL only):
   sekcja klucza + ocena testu (kryteria oceny scenariuszy i zadań, interpretacja
   wyniku, ścieżki rozwoju), dokument wewnętrzny instruktora.

Użycie:
    python scripts/b4_op_export_test_koncowy.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE_TEMPLATE = REPO_ROOT / "content" / "M3" / "lessons" / "m3-w4-l8"
TARGET_ROOT = REPO_ROOT / "podprojekt-b" / "B4-operacyjne" / "O3-ocena"

LANGS: tuple[str, ...] = ("pl", "en", "es", "uk")
STAN_NA = "2026-04-27"

KEY_HEADERS: dict[str, str] = {
    "pl": "### Klucz odpowiedzi (dla trenera; kursant NIE widzi)",
    "en": "### Answer key (for instructor; student does NOT see it)",
    "es": "### Clave de respuestas (para el formador; el alumno NO la ve)",
    "uk": "### Ключ відповідей (для тренера; слухач НЕ бачить)",
}

END_OF_KEY_HEADERS: dict[str, str] = {
    "pl": "## Kluczowe terminy",
    "en": "## Key terms",
    "es": "## Términos clave",
    "uk": "## Ключові терміни",
}

TKK_TITLE_H1: dict[str, str] = {
    "pl": "TEST KOŃCOWY KURSU",
    "en": "FINAL COURSE TEST",
    "es": "EXAMEN FINAL DEL CURSO",
    "uk": "ПІДСУМКОВИЙ ТЕСТ КУРСУ",
}

KEY_TITLE_H1_PL = "KLUCZ ODPOWIEDZI - TEST KOŃCOWY KURSU"

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

INTRO_PARA: dict[str, str] = {
    "pl": (
        "Niniejszy dokument zawiera **test końcowy całego Kursu**. Test obejmuje treść "
        "wszystkich trzech Modułów (M1 Pomocnik, M2 Operator pod nadzorem, M3 Operator "
        "samodzielny) w proporcji 20% / 30% / 50% (zgodnie z hierarchią kompetencji) i jest "
        "warunkiem dopuszczenia do egzaminu praktycznego oraz wydania zaświadczenia "
        "ukończenia Kursu. Test składa się z trzech części: pytania zamknięte (60 pkt), "
        "scenariusze decyzyjne (30 pkt) i zadania praktyczne (18 pkt), razem **108 punktów** "
        "i czas **120 minut**, próg zaliczenia **70% = 76 punktów**."
    ),
    "en": (
        "This document contains **the final test of the entire Course**. The test covers the "
        "content of all three Modules (M1 Helper, M2 Operator under supervision, M3 Independent "
        "operator) in the proportion 20% / 30% / 50% (in line with the competence hierarchy) "
        "and is a condition for admission to the practical exam and the issuance of the Course "
        "completion certificate. The test consists of three parts: multiple-choice questions "
        "(60 pts), decision scenarios (30 pts) and practical tasks (18 pts), totalling "
        "**108 points** and a duration of **120 minutes**, with a pass threshold of "
        "**70% = 76 points**."
    ),
    "es": (
        "El presente documento contiene **el examen final de todo el Curso**. El examen abarca "
        "el contenido de los tres Módulos (M1 Ayudante, M2 Operador bajo supervisión, "
        "M3 Operador autónomo) en la proporción 20% / 30% / 50% (de acuerdo con la jerarquía "
        "de competencias) y es condición para la admisión al examen práctico y la expedición "
        "del certificado de finalización del Curso. El examen consta de tres partes: preguntas "
        "de opción múltiple (60 pts), escenarios de decisión (30 pts) y tareas prácticas "
        "(18 pts), en total **108 puntos** y una duración de **120 minutos**, con umbral de "
        "aprobación **70% = 76 puntos**."
    ),
    "uk": (
        "Цей документ містить **підсумковий тест усього Курсу**. Тест охоплює зміст усіх "
        "трьох Модулів (M1 Помічник, M2 Оператор під наглядом, M3 Самостійний оператор) у "
        "пропорції 20% / 30% / 50% (відповідно до ієрархії компетенцій) і є умовою допуску до "
        "практичного іспиту та видачі посвідчення про завершення Курсу. Тест складається з "
        "трьох частин: тестові питання (60 балів), сценарії прийняття рішень (30 балів) і "
        "практичні завдання (18 балів), разом **108 балів** і тривалість **120 хвилин**, поріг "
        "складання **70% = 76 балів**."
    ),
}

ID_LABELS: dict[str, dict[str, str]] = {
    "pl": {
        "id_caption": "Identyfikator wzoru[^1]",
        "ev_caption": "Numer ewidencyjny testu[^2]",
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
        "ev_caption": "Test registration number[^2]",
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
        "ev_caption": "Número de registro del examen[^2]",
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
        "ev_caption": "Реєстраційний номер тесту[^2]",
        "date_caption": "Дата заповнення (ДД-ММ-РРРР)",
        "footnote_label": "Виноски",
        "footer": (
            "*Документ складений Fundacją pomocy prawnej EGIDA (Фундацією правової допомоги "
            "EGIDA). Зразок підлягає внутрішньому контролю версій. Примірник Курсанта і "
            "примірник Фундації є тотожними щодо змісту.*"
        ),
    },
}

TKK_FOOTNOTE_1: dict[str, str] = {
    "pl": (
        'Identyfikator wzoru określa wersję wzoru testu w postaci: TKK (skrót od „Test '
        'Końcowy Kursu") - numer wersji - rok obowiązywania. Numer wersji jest podnoszony '
        "przy każdej aktualizacji wzoru przez Fundację."
    ),
    "en": (
        'The template identifier specifies the version of the test template in the form: TKK '
        '(short for "Final Course Test") - version number - year of validity. The version '
        "number is raised at every update of the template by the Foundation."
    ),
    "es": (
        'El identificador del modelo indica la versión del modelo del examen en la forma: '
        'TKK (abreviatura de „Test Końcowy Kursu", examen final del curso) - número de '
        "versión - año de vigencia. El número de versión se eleva con cada actualización del "
        "modelo por parte de la Fundación."
    ),
    "uk": (
        'Ідентифікатор зразка визначає версію зразка тесту у формі: TKK (скорочення від '
        '„Test Końcowy Kursu", підсумковий тест курсу) - номер версії - рік чинності. '
        "Номер версії підвищується при кожному оновленні зразка Фундацією."
    ),
}

TKK_FOOTNOTE_2: dict[str, str] = {
    "pl": (
        "Numer ewidencyjny testu nadaje koordynator Kursu w chwili przyjęcia wypełnionego "
        "arkusza. Numer ma postać: rok / kolejny numer w roku / TKK (np. 2026/001/TKK)."
    ),
    "en": (
        "The test registration number is assigned by the Course coordinator at the moment "
        "the completed sheet is received. The number takes the form: year / consecutive number "
        "in the year / TKK (e.g. 2026/001/TKK)."
    ),
    "es": (
        "El número de registro del examen lo asigna el coordinador del Curso en el momento "
        "de la recepción de la hoja cumplimentada. El número tiene el formato: año / número "
        "correlativo en el año / TKK (por ejemplo, 2026/001/TKK)."
    ),
    "uk": (
        "Реєстраційний номер тесту присвоює координатор Курсу в момент прийняття заповненого "
        "аркуша. Номер має формат: рік / порядковий номер у році / TKK (наприклад, "
        "2026/001/TKK)."
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

CHARAKTER: dict[str, str] = {
    "pl": (
        "podsumowujące narzędzie oceny obejmujące treść wszystkich trzech Modułów Kursu "
        "(M1, M2, M3) w proporcji 20% / 30% / 50%; warunek dopuszczenia do egzaminu "
        "praktycznego i wydania zaświadczenia ukończenia Kursu"
    ),
    "en": (
        "summative assessment instrument covering the content of all three Course Modules "
        "(M1, M2, M3) in the proportion 20% / 30% / 50%; condition for admission to the "
        "practical exam and the issuance of the Course completion certificate"
    ),
    "es": (
        "instrumento de evaluación sumativa que abarca el contenido de los tres Módulos "
        "del Curso (M1, M2, M3) en la proporción 20% / 30% / 50%; condición para la admisión "
        "al examen práctico y la expedición del certificado de finalización del Curso"
    ),
    "uk": (
        "підсумковий інструмент оцінювання, що охоплює зміст усіх трьох Модулів Курсу "
        "(M1, M2, M3) у пропорції 20% / 30% / 50%; умова допуску до практичного іспиту і "
        "видачі посвідчення про завершення Курсу"
    ),
}

STRONY: dict[str, str] = {
    "pl": (
        "Kursant (rozwiązujący test), instruktor Kursu (oceniający arkusz odpowiedzi), "
        "koordynator Kursu (przyjmujący arkusz i nadający numer ewidencyjny), Fundacja "
        "pomocy prawnej EGIDA (autor i właściciel narzędzia oceny)"
    ),
    "en": (
        "the Trainee (solving the test), the Course instructor (grading the answer sheet), "
        "the Course coordinator (receiving the sheet and assigning the registration number), "
        "Fundacja pomocy prawnej EGIDA (the author and owner of the assessment instrument)"
    ),
    "es": (
        "el Kursant (que resuelve el examen), el instructor del Curso (que corrige la hoja "
        "de respuestas), el coordinador del Curso (que recibe la hoja y asigna el número de "
        "registro), Fundacja pomocy prawnej EGIDA (autor y propietario del instrumento de "
        "evaluación)"
    ),
    "uk": (
        "Курсант (особа, яка проходить тест), інструктор Курсу (особа, яка оцінює аркуш "
        "відповідей), координатор Курсу (особа, яка приймає аркуш і присвоює реєстраційний "
        "номер), Fundacja pomocy prawnej EGIDA (автор і власник інструменту оцінювання)"
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

KEY_INTRO_PL = (
    "Niniejszy dokument zawiera **klucz odpowiedzi do testu końcowego Kursu** wraz z "
    "kryteriami oceny scenariuszy decyzyjnych i zadań praktycznych, interpretacją wyniku "
    "oraz ścieżkami rozwoju Kursanta po zaliczeniu albo niezaliczeniu testu. Dokument jest "
    "**wewnętrznym narzędziem instruktorskim** i **nie podlega wydawaniu Kursantom** ani "
    "podmiotom zewnętrznym. Klucz służy obiektywnej ocenie arkuszy odpowiedzi po "
    "przeprowadzeniu testu końcowego."
)

KEY_FOOTNOTE_1_PL = (
    'Identyfikator wzoru określa wersję wzoru klucza w postaci: KOD-TKK (skrót od „Klucz '
    'Odpowiedzi do Testu Końcowego Kursu") - numer wersji - rok obowiązywania. Numer wersji '
    "jest podnoszony przy każdej aktualizacji wzoru przez Fundację. Klucz odpowiada wzorowi "
    "testu TKK-1.0/2026."
)

KEY_FOOTNOTE_2_PL = (
    "Numer ewidencyjny ocenionego arkusza nadaje koordynator albo instruktor Kursu w "
    "chwili oceny. Numer ma postać: rok / kolejny numer w roku / TKK-OCN (np. "
    "2026/001/TKK-OCN)."
)


def parse_source_file(path: Path, lang: str) -> tuple[str, str]:
    """Zwraca (treść testu po YAML do nagłówka klucza, treść klucza od nagłówka klucza
    do nagłówka 'Kluczowe terminy' exclusive)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: brak frontmattera")
    yaml_end = text.find("\n---\n", 4)
    if yaml_end == -1:
        raise ValueError(f"{path}: niezamknięty frontmatter")
    body = text[yaml_end + 5 :].lstrip("\n")

    key_marker = KEY_HEADERS[lang]
    end_marker = END_OF_KEY_HEADERS[lang]

    needle_key = f"\n{key_marker}\n"
    key_offset = body.find(needle_key)
    if key_offset == -1:
        raise ValueError(f"{path}: nie znaleziono nagłówka klucza '{key_marker}'")
    split_at_key = key_offset + 1

    needle_end = f"\n{end_marker}\n"
    end_offset = body.find(needle_end, split_at_key)
    if end_offset == -1:
        raise ValueError(f"{path}: nie znaleziono końcowego nagłówka '{end_marker}'")
    split_at_end = end_offset + 1

    test_part = body[:split_at_key].rstrip() + "\n"
    key_part = body[split_at_key:split_at_end].rstrip() + "\n"
    return test_part, key_part


def build_test_yaml(lang: str) -> str:
    return (
        f"---\n"
        f"typ: test\n"
        f"dokument: test końcowy Kursu (test podsumowujący obejmujący treść wszystkich "
        f"trzech Modułów w proporcji 20/30/50)\n"
        f"kurs: Praca w tartaku\n"
        f"podprojekt: B\n"
        f"faza: B4-operacyjne\n"
        f"grupa: O3-ocena\n"
        f"język: {lang}\n"
        f"wersja: 1.0\n"
        f"stan-na: {STAN_NA}\n"
        f"podstawa-prawna:\n"
        f"{PODSTAWA_PRAWNA}\n"
        f"charakter: {CHARAKTER[lang]}\n"
        f"strony: {STRONY[lang]}\n"
        f"---\n"
    )


def build_key_yaml() -> str:
    return (
        f"---\n"
        f"typ: klucz odpowiedzi\n"
        f"dokument: klucz odpowiedzi do testu końcowego Kursu (narzędzie instruktorskie do "
        f"oceny arkuszy)\n"
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
        f"oceny arkuszy odpowiedzi testu końcowego Kursu; nie podlega wydawaniu Kursantom "
        f"ani podmiotom zewnętrznym\n"
        f"strony: instruktor Kursu (oceniający), koordynator Kursu (nadzorujący przyjęcie "
        f"i ocenę), Fundacja pomocy prawnej EGIDA (autor i właściciel klucza)\n"
        f"---\n"
    )


def build_id_table(lang: str, identifier: str) -> str:
    labels = ID_LABELS[lang]
    return (
        f"| {labels['id_caption']} | {labels['ev_caption']} | {labels['date_caption']} |\n"
        f"|---|---|---|\n"
        f"| {identifier} | | |\n"
    )


def build_test_document(lang: str, test_body: str) -> str:
    identifier = "TKK-1.0/2026"
    labels = ID_LABELS[lang]
    parts: list[str] = []
    parts.append(build_test_yaml(lang))
    parts.append("")
    parts.append(f"# {TKK_TITLE_H1[lang]}")
    parts.append("")
    parts.append(LEAD_SENTENCE[lang])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(INTRO_PARA[lang])
    parts.append("")
    parts.append(build_id_table(lang, identifier))
    parts.append("---")
    parts.append("")
    parts.append(test_body.rstrip())
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
    parts.append(f"[^1]: {TKK_FOOTNOTE_1[lang]}")
    parts.append("")
    parts.append(f"[^2]: {TKK_FOOTNOTE_2[lang]}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(labels["footer"])
    parts.append("")
    return "\n".join(parts)


def build_key_document(key_body: str) -> str:
    identifier = "KOD-TKK-1.0/2026"
    parts: list[str] = []
    parts.append(build_key_yaml())
    parts.append("")
    parts.append(f"# {KEY_TITLE_H1_PL}")
    parts.append("")
    parts.append(
        "**Dokument wewnętrzny Fundacji pomocy prawnej EGIDA**: narzędzie instruktorskie "
        'do oceny arkuszy odpowiedzi testu końcowego Kursu praktycznego „Praca w tartaku".'
    )
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(KEY_INTRO_PL)
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
    parts.append(key_body.rstrip())
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Przypisy")
    parts.append("")
    parts.append(f"[^1]: {KEY_FOOTNOTE_1_PL}")
    parts.append("")
    parts.append(f"[^2]: {KEY_FOOTNOTE_2_PL}")
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


def test_target_dir() -> Path:
    return TARGET_ROOT / "08-test-koncowy-kursu"


def key_target_dir() -> Path:
    return TARGET_ROOT / "09-klucz-testu-koncowego"


def export() -> list[Path]:
    written: list[Path] = []
    test_dir = test_target_dir()
    key_dir = key_target_dir()
    test_dir.mkdir(parents=True, exist_ok=True)
    key_dir.mkdir(parents=True, exist_ok=True)

    pl_key_body: str | None = None

    for lang in LANGS:
        src = SOURCE_FILE_TEMPLATE / f"{lang}.md"
        if not src.exists():
            print(f"[SKIP] {src} nie istnieje", file=sys.stderr)
            continue

        test_body, key_body = parse_source_file(src, lang)
        out_test = test_dir / f"{lang}.md"
        out_test.write_bytes(build_test_document(lang, test_body).encode("utf-8"))
        written.append(out_test)

        if lang == "pl":
            pl_key_body = key_body

    if pl_key_body is None:
        raise RuntimeError("Brak pliku PL m3-w4-l8, klucza nie wygenerowano")

    out_key = key_dir / "pl.md"
    out_key.write_bytes(build_key_document(pl_key_body).encode("utf-8"))
    written.append(out_key)

    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    print("=== Test koncowy Kursu (TKK + KOD-TKK) ===")
    written = export()
    for p in written:
        size = p.stat().st_size
        print(f"  {p.relative_to(REPO_ROOT)}  ({size} bytes)")

    print(f"\nZapisano {len(written)} plikow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
