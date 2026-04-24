"""Generator D2 Program szczegółowy z structure.json + kluczowych terminów lekcji.

Użycie: python scripts/generate_program_szczegolowy.py <lang> > content/materialy-pomocnicze/program-szczegolowy/<lang>.md

lang ∈ {pl, en, es, uk}
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BLOCK_NAMES = {
    "bezpieczenstwo": {
        "pl": "Bezpieczeństwo i odpowiedzialność",
        "en": "Safety and responsibility",
        "es": "Seguridad y responsabilidad",
        "uk": "Безпека і відповідальність",
    },
    "material": {
        "pl": "Materiał i narzędzia",
        "en": "Material and tools",
        "es": "Material y herramientas",
        "uk": "Матеріал та інструменти",
    },
    "procesy": {
        "pl": "Procesy produkcyjne",
        "en": "Production processes",
        "es": "Procesos de producción",
        "uk": "Виробничі процеси",
    },
    "organizacja": {
        "pl": "Organizacja pracy",
        "en": "Work organization",
        "es": "Organización del trabajo",
        "uk": "Організація роботи",
    },
}

MODULE_TITLES = {
    "M1": {
        "pl": "Moduł 1 - Pomocnik (rola pomocnicza)",
        "en": "Module 1 - Helper (support role)",
        "es": "Módulo 1 - Ayudante (rol de apoyo)",
        "uk": "Модуль 1 - Помічник (допоміжна роль)",
    },
    "M2": {
        "pl": "Moduł 2 - Młodszy operator (rola samodzielna na ograniczonych maszynach)",
        "en": "Module 2 - Junior operator (autonomous role on limited machines)",
        "es": "Módulo 2 - Operador junior (rol autónomo en máquinas limitadas)",
        "uk": "Модуль 2 - Молодший оператор (самостійна роль на обмежених машинах)",
    },
    "M3": {
        "pl": "Moduł 3 - Operator samodzielny z elementami nadzoru",
        "en": "Module 3 - Autonomous operator with supervisory elements",
        "es": "Módulo 3 - Operador autónomo con elementos de supervisión",
        "uk": "Модуль 3 - Самостійний оператор з елементами нагляду",
    },
}

INTROS = {
    "pl": (
        "Dokument zawiera listę 96 lekcji kursu tartakowego z tytułem, krótkim opisem celu dydaktycznego i pięcioma-ośmioma kluczowymi terminami polskimi dla każdej lekcji. Lista jest wygenerowana automatycznie ze specyfikacji modułów i treści lekcji przez skrypt `scripts/generate_program_szczegolowy.py`. Wszystkie dane pochodzą z ukończonych plików lekcji M1/M2/M3 fazy 3 Podprojektu A. Pełne treści lekcji znajdują się w katalogu `content/M{1,2,3}/lessons/`."
    ),
    "en": (
        "This document contains a list of 96 sawmill course lessons with titles, brief learning-goal descriptions and five to eight key Polish terms for each lesson. The list is generated automatically from module specifications and lesson content by the script `scripts/generate_program_szczegolowy.py`. All data comes from completed lesson files M1/M2/M3 in phase 3 of Subproject A. Full lesson content is in the `content/M{1,2,3}/lessons/` directory. Key terms are kept in Polish because the course is taught in Polish and Polish vocabulary is a core learning outcome."
    ),
    "es": (
        "Este documento contiene una lista de 96 lecciones del curso de aserradero con títulos, breves descripciones del objetivo didáctico y de cinco a ocho términos clave en polaco para cada lección. La lista se genera automáticamente a partir de las especificaciones de módulos y del contenido de las lecciones mediante el script `scripts/generate_program_szczegolowy.py`. Todos los datos proceden de los archivos de lección M1/M2/M3 completados en la fase 3 del Subproyecto A. El contenido completo de las lecciones se encuentra en el directorio `content/M{1,2,3}/lessons/`. Los términos clave se mantienen en polaco porque el curso se imparte en polaco y el vocabulario polaco es un resultado clave del aprendizaje."
    ),
    "uk": (
        "Цей документ містить список 96 уроків курсу лісопилки з назвами, короткими описами навчальної мети і п'ятьма-вісьма ключовими польськими термінами для кожного уроку. Список генерується автоматично зі специфікацій модулів і змісту уроків скриптом `scripts/generate_program_szczegolowy.py`. Усі дані походять із завершених файлів уроків M1/M2/M3 фази 3 Підпроєкту A. Повний зміст уроків знаходиться в каталозі `content/M{1,2,3}/lessons/`. Ключові терміни подано польською, оскільки курс викладається польською і польська лексика є ключовим навчальним результатом."
    ),
}

TITLES = {
    "pl": "Program szczegółowy kursu „Praca w tartaku\"",
    "en": "Detailed course program \"Work in a Sawmill\"",
    "es": "Programa detallado del curso «Trabajo en un aserradero»",
    "uk": "Детальна програма курсу «Робота на лісопилці»",
}

LABELS = {
    "pl": {
        "week_header": "### Tydzień {n} - {block} (`{block_id}`)",
        "lesson_header": "#### Lekcja {n} (`{id}`): {title}",
        "goal_label": "**Cel**:",
        "terms_label": "**Kluczowe terminy polskie**:",
        "duration_label": "**Czas**:",
        "minutes": "minut",
        "summary": "**Lekcji łącznie**: {lessons}. **Terminów polskich zaindeksowanych**: {terms}.",
    },
    "en": {
        "week_header": "### Week {n} - {block} (`{block_id}`)",
        "lesson_header": "#### Lesson {n} (`{id}`): {title}",
        "goal_label": "**Goal**:",
        "terms_label": "**Key Polish terms**:",
        "duration_label": "**Duration**:",
        "minutes": "minutes",
        "summary": "**Total lessons**: {lessons}. **Polish terms indexed**: {terms}.",
    },
    "es": {
        "week_header": "### Semana {n} - {block} (`{block_id}`)",
        "lesson_header": "#### Lección {n} (`{id}`): {title}",
        "goal_label": "**Objetivo**:",
        "terms_label": "**Términos clave en polaco**:",
        "duration_label": "**Duración**:",
        "minutes": "minutos",
        "summary": "**Total de lecciones**: {lessons}. **Términos polacos indexados**: {terms}.",
    },
    "uk": {
        "week_header": "### Тиждень {n} - {block} (`{block_id}`)",
        "lesson_header": "#### Урок {n} (`{id}`): {title}",
        "goal_label": "**Мета**:",
        "terms_label": "**Ключові польські терміни**:",
        "duration_label": "**Тривалість**:",
        "minutes": "хвилин",
        "summary": "**Усього уроків**: {lessons}. **Польських термінів заіндексовано**: {terms}.",
    },
}


def sanitize(text: str) -> str:
    """Replace em-dashes (U+2014) and en-dashes (U+2013) from legacy lesson data with ASCII hyphens."""
    return text.replace("\u2014", "-").replace("\u2013", "-")


def extract_terms(lesson_md_path: Path, max_terms: int = 8):
    """Extract first N bold terms from ## Kluczowe terminy section."""
    if not lesson_md_path.exists():
        return []
    text = lesson_md_path.read_text(encoding="utf-8")
    section = re.search(r"## Kluczowe terminy\s*\n(.*?)(?:\n## |\Z)", text, re.DOTALL)
    if not section:
        return []
    body = section.group(1)
    terms = re.findall(r"-\s+\*\*([^*]+)\*\*", body)
    return [sanitize(term) for term in terms[:max_terms]]


def generate(lang: str) -> str:
    assert lang in ("pl", "en", "es", "uk")
    labels = LABELS[lang]

    lines = []
    lines.append("---")
    lines.append("id: program-szczegolowy")
    lines.append("faza: 5")
    lines.append("typ: materialy-pomocnicze")
    lines.append("dokument: D2")
    lines.append(f"język: {lang}")
    lines.append("---")
    lines.append("")

    lines.append(f"# {TITLES[lang]}")
    lines.append("")
    lines.append(INTROS[lang])
    lines.append("")

    total_lessons = 0
    total_terms = 0

    for module_id in ("M1", "M2", "M3"):
        structure_path = ROOT / "content" / module_id / "structure.json"
        structure = json.loads(structure_path.read_text(encoding="utf-8"))

        lines.append(f"## {MODULE_TITLES[module_id][lang]}")
        lines.append("")

        for week in structure["weeks"]:
            block_id = week["blockId"]
            block_name = BLOCK_NAMES[block_id][lang]
            lines.append(
                labels["week_header"].format(n=week["week"], block=block_name, block_id=block_id)
            )
            lines.append("")

            for idx, lesson in enumerate(week["lessons"], start=1):
                lesson_id = lesson["id"]
                title = sanitize(lesson["tytul"][lang])
                opis = sanitize(lesson["opis"][lang])
                czas = lesson["czas"]

                lesson_md_path = ROOT / "content" / module_id / "lessons" / lesson_id / "pl.md"
                terms = extract_terms(lesson_md_path, max_terms=8)
                total_lessons += 1
                total_terms += len(terms)

                lines.append(
                    labels["lesson_header"].format(n=idx, id=lesson_id, title=title)
                )
                lines.append("")
                lines.append(f"{labels['duration_label']} {czas} {labels['minutes']}")
                lines.append("")
                lines.append(f"{labels['goal_label']} {opis}")
                lines.append("")
                if terms:
                    lines.append(f"{labels['terms_label']} {', '.join(terms)}.")
                    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(labels["summary"].format(lessons=total_lessons, terms=total_terms))
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else "pl"
    out = generate(lang)
    sys.stdout.buffer.write(out.encode("utf-8"))
