"""
b4_op_export_quiz.py

Eksporter quizów uzupełniających modułów (M1/M2/M3) z aplikacji A
(content/Mn/artifacts/quiz-uzupelniajacy/{lang}.md) do Podprojektu B4-operacyjne
(podprojekt-b/B4-operacyjne/O3-ocena/...).

Z każdego pliku źródłowego produkuje DWA artefakty:

1. Quiz Uzupełniający Modułu (QUM-Mn-1.0/2026, klasa 1, 4 jęz):
   pełna treść quizu BEZ klucza odpowiedzi (kursant nie może otrzymać klucza),
   z YAML B-OP, identyfikatorem wzoru, wzmianką EFS+ i przypisami.

2. Klucz odpowiedzi (KOD-QUM-Mn-1.0/2026, klasa 3, PL only):
   sekcja klucza + punktacja + notatki dla trenera, dokument wewnętrzny instruktora.

Użycie:
    python scripts/b4_op_export_quiz.py
    python scripts/b4_op_export_quiz.py --module 1
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = REPO_ROOT / "content"
TARGET_ROOT = REPO_ROOT / "podprojekt-b" / "B4-operacyjne" / "O3-ocena"

LANGS: tuple[str, ...] = ("pl", "en", "es", "uk")
MODULES: tuple[int, ...] = (1, 2, 3)
STAN_NA = "2026-04-27"

KEY_HEADERS: dict[str, str] = {
    "pl": "## Klucz odpowiedzi",
    "en": "## Answer key",
    "es": "## Clave de respuestas",
    "uk": "## Ключ відповідей",
}

QUIZ_TITLE_H1: dict[str, str] = {
    "pl": "QUIZ UZUPEŁNIAJĄCY MODUŁU {n}",
    "en": "MODULE {n} SUPPLEMENTARY QUIZ",
    "es": "CUESTIONARIO COMPLEMENTARIO DEL MÓDULO {n}",
    "uk": "ДОДАТКОВИЙ ТЕСТ МОДУЛЯ {n}",
}

KEY_TITLE_H1_PL = "KLUCZ ODPOWIEDZI - QUIZ UZUPEŁNIAJĄCY MODUŁU {n}"

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
        "Niniejszy dokument zawiera **quiz uzupełniający Modułu {n}** Kursu. Quiz służy "
        "sprawdzeniu integracji wiedzy z całego Modułu w trybie samooceny po teście l8 albo "
        "w trybie poprawkowym (gdy test l8 nie został zdany). Wynik quizu samodzielnie nie "
        "rozstrzyga o ukończeniu Modułu, lecz dostarcza Kursantowi i instruktorowi obrazu "
        "obszarów wymagających powtórki lub utrwalenia."
    ),
    "en": (
        "This document contains **the supplementary quiz for Module {n}** of the Course. "
        "The quiz serves to verify the integration of knowledge from the entire Module, either "
        "in self-assessment mode after the l8 test or in retake mode (if the l8 test was not "
        "passed). The result of the quiz alone does not determine completion of the Module, "
        "but it provides the Trainee and the instructor with a picture of the areas requiring "
        "review or consolidation."
    ),
    "es": (
        "El presente documento contiene **el cuestionario complementario del Módulo {n}** "
        "del Curso. El cuestionario sirve para verificar la integración de los conocimientos "
        "de todo el Módulo, ya sea en el modo de autoevaluación tras el test l8 o en el modo "
        "de recuperación (cuando no se ha aprobado el test l8). El resultado del cuestionario "
        "por sí solo no decide la finalización del Módulo, sino que proporciona al Kursant "
        "(cursante) y al instructor una imagen de las áreas que requieren repaso o "
        "consolidación."
    ),
    "uk": (
        "Цей документ містить **додатковий тест Модуля {n}** Курсу. Тест слугує для перевірки "
        "інтеграції знань усього Модуля в режимі самооцінки після тесту l8 або в режимі "
        "повторного складання (якщо тест l8 не складено). Результат тесту самостійно не "
        "вирішує про завершення Модуля, а надає Курсантові та інструкторові картину сфер, "
        "які потребують повторення або закріплення."
    ),
}

QUIZ_ID_LABELS: dict[str, dict[str, str]] = {
    "pl": {
        "id_caption": "Identyfikator wzoru[^1]",
        "ev_caption": "Numer ewidencyjny quizu[^2]",
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
        "ev_caption": "Quiz registration number[^2]",
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
        "ev_caption": "Número de registro del cuestionario[^2]",
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

QUIZ_FOOTNOTE_1: dict[str, str] = {
    "pl": (
        'Identyfikator wzoru określa wersję wzoru quizu w postaci: QUM (skrót od „Quiz '
        'Uzupełniający Modułu") - numer modułu - numer wersji - rok obowiązywania. Numer '
        "wersji jest podnoszony przy każdej aktualizacji wzoru przez Fundację."
    ),
    "en": (
        'The template identifier specifies the version of the quiz template in the form: QUM '
        '(short for "Module Supplementary Quiz") - module number - version number - year of '
        "validity. The version number is raised at every update of the template by the "
        "Foundation."
    ),
    "es": (
        'El identificador del modelo indica la versión del modelo del cuestionario en la '
        'forma: QUM (abreviatura de „Quiz Uzupełniający Modułu", cuestionario complementario '
        "del módulo) - número de módulo - número de versión - año de vigencia. El número de "
        "versión se eleva con cada actualización del modelo por parte de la Fundación."
    ),
    "uk": (
        'Ідентифікатор зразка визначає версію зразка тесту у формі: QUM (скорочення від '
        '„Quiz Uzupełniający Modułu", додатковий тест модуля) - номер модуля - номер версії '
        "- рік чинності. Номер версії підвищується при кожному оновленні зразка Фундацією."
    ),
}

QUIZ_FOOTNOTE_2: dict[str, str] = {
    "pl": (
        "Numer ewidencyjny quizu nadaje koordynator Kursu w chwili przyjęcia wypełnionego "
        "arkusza. Numer ma postać: rok / kolejny numer w roku / QUM-M{n} (np. 2026/001/QUM-M{n})."
    ),
    "en": (
        "The quiz registration number is assigned by the Course coordinator at the moment "
        "the completed sheet is received. The number takes the form: year / consecutive number "
        "in the year / QUM-M{n} (e.g. 2026/001/QUM-M{n})."
    ),
    "es": (
        "El número de registro del cuestionario lo asigna el coordinador del Curso en el "
        "momento de la recepción de la hoja cumplimentada. El número tiene el formato: año / "
        "número correlativo en el año / QUM-M{n} (por ejemplo, 2026/001/QUM-M{n})."
    ),
    "uk": (
        "Реєстраційний номер тесту присвоює координатор Курсу в момент прийняття заповненого "
        "аркуша. Номер має формат: рік / порядковий номер у році / QUM-M{n} (наприклад, "
        "2026/001/QUM-M{n})."
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
        "narzędzie sprawdzające integrację wiedzy z Modułu {n} Kursu; tryb samooceny po "
        "teście l8 (gdy zdany) albo poprawkowy (gdy l8 nie zdany); wynik samodzielnie nie "
        "rozstrzyga o ukończeniu Modułu poza trybem poprawkowym"
    ),
    "en": (
        "an instrument verifying the integration of knowledge from Module {n} of the Course; "
        "self-assessment mode after the l8 test (if passed) or retake mode (if l8 was not "
        "passed); the result alone does not decide completion of the Module outside the retake "
        "mode"
    ),
    "es": (
        "instrumento que verifica la integración de los conocimientos del Módulo {n} del "
        "Curso; modo de autoevaluación tras el test l8 (si se ha aprobado) o modo de "
        "recuperación (si no se ha aprobado el l8); el resultado por sí solo no decide la "
        "finalización del Módulo fuera del modo de recuperación"
    ),
    "uk": (
        "інструмент перевірки інтеграції знань Модуля {n} Курсу; режим самооцінки після "
        "тесту l8 (за умови складання) або повторного складання (якщо l8 не складено); "
        "результат самостійно не вирішує про завершення Модуля поза режимом повторного "
        "складання"
    ),
}

STRONY: dict[str, str] = {
    "pl": (
        "Kursant (rozwiązujący quiz), instruktor Kursu (oceniający arkusz odpowiedzi), "
        "Fundacja pomocy prawnej EGIDA (autor i właściciel narzędzia oceny)"
    ),
    "en": (
        "the Trainee (solving the quiz), the Course instructor (grading the answer sheet), "
        "Fundacja pomocy prawnej EGIDA (the author and owner of the assessment instrument)"
    ),
    "es": (
        "el Kursant (que resuelve el cuestionario), el instructor del Curso (que corrige la "
        "hoja de respuestas), Fundacja pomocy prawnej EGIDA (autor y propietario del "
        "instrumento de evaluación)"
    ),
    "uk": (
        "Курсант (особа, яка проходить тест), інструктор Курсу (особа, яка оцінює аркуш "
        "відповідей), Fundacja pomocy prawnej EGIDA (автор і власник інструменту оцінювання)"
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
    "Niniejszy dokument zawiera **klucz odpowiedzi do quizu uzupełniającego Modułu {n}** "
    "wraz z punktacją, interpretacją wyniku oraz notatkami metodycznymi dla instruktora. "
    "Dokument jest **wewnętrznym narzędziem instruktorskim** i **nie podlega wydawaniu "
    "Kursantom** ani podmiotom zewnętrznym. Klucz służy obiektywnej ocenie arkuszy "
    "odpowiedzi po przeprowadzeniu quizu w trybie samooceny albo poprawkowym."
)

KEY_FOOTNOTE_1_PL = (
    'Identyfikator wzoru określa wersję wzoru klucza w postaci: KOD-QUM (skrót od „Klucz '
    'Odpowiedzi do Quizu Uzupełniającego Modułu") - numer modułu - numer wersji - rok '
    "obowiązywania. Numer wersji jest podnoszony przy każdej aktualizacji wzoru przez "
    "Fundację. Klucz odpowiada wzorowi quizu QUM-M{n}-1.0/2026."
)

KEY_FOOTNOTE_2_PL = (
    "Numer ewidencyjny ocenionego arkusza nadaje koordynator albo instruktor Kursu w "
    "chwili oceny. Numer ma postać: rok / kolejny numer w roku / QUM-M{n}-OCN (np. "
    "2026/001/QUM-M{n}-OCN)."
)


def parse_source_file(path: Path, lang: str) -> tuple[str, str]:
    """Zwraca (treść quizu po YAML do nagłówka klucza, treść klucza+ od nagłówka klucza)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: brak frontmattera")
    yaml_end = text.find("\n---\n", 4)
    if yaml_end == -1:
        raise ValueError(f"{path}: niezamknięty frontmatter")
    body = text[yaml_end + 5 :].lstrip("\n")

    key_marker = KEY_HEADERS[lang]
    needle = f"\n{key_marker}\n"
    key_offset = body.find(needle)
    if key_offset == -1:
        if body.startswith(key_marker + "\n"):
            key_offset = -1
            split_at = 0
        else:
            raise ValueError(f"{path}: nie znaleziono nagłówka klucza '{key_marker}'")
    else:
        split_at = key_offset + 1

    quiz_part = body[:split_at].rstrip() + "\n"
    key_part = body[split_at:].rstrip() + "\n"
    return quiz_part, key_part


def build_quiz_yaml(module_n: int, lang: str) -> str:
    return (
        f"---\n"
        f"typ: quiz\n"
        f"dokument: quiz uzupełniający Modułu {module_n} (test sprawdzający integrację "
        f"wiedzy z Modułu {module_n} Kursu)\n"
        f"kurs: Praca w tartaku\n"
        f"podprojekt: B\n"
        f"faza: B4-operacyjne\n"
        f"grupa: O3-ocena\n"
        f"język: {lang}\n"
        f"wersja: 1.0\n"
        f"stan-na: {STAN_NA}\n"
        f"podstawa-prawna:\n"
        f"{PODSTAWA_PRAWNA}\n"
        f"charakter: {CHARAKTER[lang].format(n=module_n)}\n"
        f"strony: {STRONY[lang]}\n"
        f"---\n"
    )


def build_key_yaml(module_n: int) -> str:
    return (
        f"---\n"
        f"typ: klucz odpowiedzi\n"
        f"dokument: klucz odpowiedzi do quizu uzupełniającego Modułu {module_n} (narzędzie "
        f"instruktorskie do oceny arkuszy)\n"
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
        f"oceny arkuszy odpowiedzi quizu uzupełniającego Modułu {module_n}; nie podlega "
        f"wydawaniu Kursantom ani podmiotom zewnętrznym\n"
        f"strony: instruktor Kursu (oceniający), Fundacja pomocy prawnej EGIDA (autor i "
        f"właściciel klucza)\n"
        f"---\n"
    )


def build_id_table(lang: str, identifier: str) -> str:
    labels = QUIZ_ID_LABELS[lang]
    return (
        f"| {labels['id_caption']} | {labels['ev_caption']} | {labels['date_caption']} |\n"
        f"|---|---|---|\n"
        f"| {identifier} | | |\n"
    )


def build_quiz_document(module_n: int, lang: str, quiz_body: str) -> str:
    identifier = f"QUM-M{module_n}-1.0/2026"
    labels = QUIZ_ID_LABELS[lang]
    parts: list[str] = []
    parts.append(build_quiz_yaml(module_n, lang))
    parts.append("")
    parts.append(f"# {QUIZ_TITLE_H1[lang].format(n=module_n)}")
    parts.append("")
    parts.append(LEAD_SENTENCE[lang])
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(INTRO_PARA[lang].format(n=module_n))
    parts.append("")
    parts.append(build_id_table(lang, identifier))
    parts.append("---")
    parts.append("")
    parts.append(quiz_body.rstrip())
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
    parts.append(f"[^1]: {QUIZ_FOOTNOTE_1[lang]}")
    parts.append("")
    parts.append(f"[^2]: {QUIZ_FOOTNOTE_2[lang].format(n=module_n)}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(labels["footer"])
    parts.append("")
    return "\n".join(parts)


def build_key_document(module_n: int, key_body: str) -> str:
    identifier = f"KOD-QUM-M{module_n}-1.0/2026"
    parts: list[str] = []
    parts.append(build_key_yaml(module_n))
    parts.append("")
    parts.append(f"# {KEY_TITLE_H1_PL.format(n=module_n)}")
    parts.append("")
    parts.append(
        "**Dokument wewnętrzny Fundacji pomocy prawnej EGIDA**: narzędzie instruktorskie "
        "do oceny arkuszy odpowiedzi quizu uzupełniającego Modułu "
        f'{module_n} Kursu praktycznego „Praca w tartaku".'
    )
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(KEY_INTRO_PL.format(n=module_n))
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
    parts.append(f"[^1]: {KEY_FOOTNOTE_1_PL.format(n=module_n)}")
    parts.append("")
    parts.append(f"[^2]: {KEY_FOOTNOTE_2_PL.format(n=module_n)}")
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


def quiz_target_dir(module_n: int) -> Path:
    return TARGET_ROOT / f"{module_n:02d}-quiz-uzupelniajacy-M{module_n}"


def key_target_dir(module_n: int) -> Path:
    return TARGET_ROOT / f"{(module_n + 3):02d}-klucz-quizu-M{module_n}"


def export_module(module_n: int) -> list[Path]:
    written: list[Path] = []
    quiz_dir = quiz_target_dir(module_n)
    key_dir = key_target_dir(module_n)
    quiz_dir.mkdir(parents=True, exist_ok=True)
    key_dir.mkdir(parents=True, exist_ok=True)

    pl_key_body: str | None = None

    for lang in LANGS:
        src = SOURCE_ROOT / f"M{module_n}" / "artifacts" / "quiz-uzupelniajacy" / f"{lang}.md"
        if not src.exists():
            print(f"[SKIP] {src} nie istnieje", file=sys.stderr)
            continue

        quiz_body, key_body = parse_source_file(src, lang)
        out_quiz = quiz_dir / f"{lang}.md"
        out_quiz.write_bytes(build_quiz_document(module_n, lang, quiz_body).encode("utf-8"))
        written.append(out_quiz)

        if lang == "pl":
            pl_key_body = key_body

    if pl_key_body is None:
        raise RuntimeError(f"Moduł {module_n}: brak pliku PL, klucza nie wygenerowano")

    out_key = key_dir / "pl.md"
    out_key.write_bytes(build_key_document(module_n, pl_key_body).encode("utf-8"))
    written.append(out_key)

    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--module",
        type=int,
        choices=MODULES,
        default=None,
        help="Eksportuj tylko jeden moduł (1, 2 albo 3); domyślnie wszystkie.",
    )
    args = parser.parse_args(argv)

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

    targets = (args.module,) if args.module is not None else MODULES
    all_written: list[Path] = []
    for n in targets:
        print(f"=== Modul M{n} ===")
        written = export_module(n)
        for p in written:
            size = p.stat().st_size
            print(f"  {p.relative_to(REPO_ROOT)}  ({size} bytes)")
        all_written.extend(written)

    print(f"\nZapisano {len(all_written)} plikow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
