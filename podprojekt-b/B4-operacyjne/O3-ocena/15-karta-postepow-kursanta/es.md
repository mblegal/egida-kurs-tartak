---
typ: ficha de progreso
dokument: ficha de progreso del Kursante (resumen consolidado de los resultados de todas las herramientas de evaluación durante el ciclo del Curso, parametrizada para un Kursante individual)
kurs: Praca w tartaku (Trabajo en aserradero)
podprojekt: B
faza: B4-operacyjne
grupa: O3-ocena
klasa: 2
parametryzacja: CSV-DOCX
język: es
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (Ley polaca de 24 de abril de 2003 sobre actividades de utilidad pública y voluntariado, texto unificado Dz.U. de 2024, pos. 1491 con modificaciones posteriores) en el ámbito de la actividad estatutaria de la Fundación
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RGPD), en particular el art. 6 ap. 1 letra f, en el ámbito del diagnóstico de los efectos del aprendizaje del Kursante y de la información de retorno para la persona que aprende
charakter: documento consolidado parametrizado que presenta al Kursante y al instructor una imagen completa del progreso durante el ciclo del Curso (pruebas parciales, cuestionarios complementarios, pruebas de módulo, prueba final); herramienta de información de retorno para el Kursante y base de las decisiones metodológicas del instructor; emitido al Kursante en su idioma y en polaco para los archivos
strony: Kursante (cursante), persona a la que se refiere la ficha y destinataria de la información sobre el progreso; instructor del Curso (autor de las decisiones metodológicas basadas en la ficha); coordinador del Curso (persona que lleva el registro de las fichas de progreso del ciclo); Fundación de asistencia jurídica EGIDA (propietaria de la herramienta)
parametry:
  - IMIE_KURSANTA: nombre (nombres) del Kursante
  - NAZWISKO_KURSANTA: apellido del Kursante
  - NR_KARTY_UCZESTNIKA: número de registro de la tarjeta de participante del Kursante (por ejemplo, 2026/C1/001/KU)
  - CYKL_KURSU: identificación del ciclo del Curso (por ejemplo, C1/2026)
  - DATA_GENERACJI: fecha de generación de la ficha de progreso en formato DD-MM-AAAA
  - WYNIK_SPC_M1_T12: resultado de la prueba parcial del Módulo 1, bloque T1+T2, en formato X/30 o el valor especial no se presentó
  - WYNIK_SPC_M1_T34: resultado de la prueba parcial del Módulo 1, bloque T3+T4, en formato X/30 o el valor especial no se presentó
  - WYNIK_QUM_M1: resultado del cuestionario complementario del Módulo 1 en formato X/30 o el valor especial no se presentó (autoevaluación o recuperación, indicado en la columna contigua)
  - TRYB_QUM_M1: modalidad de realización del cuestionario complementario del Módulo 1 (autoevaluación o recuperación o no aplica)
  - WYNIK_QUM_M2: resultado del cuestionario complementario del Módulo 2 en formato X/110 o el valor especial no se presentó
  - TRYB_QUM_M2: modalidad de realización del cuestionario complementario del Módulo 2 (autoevaluación o recuperación o no aplica)
  - WYNIK_QUM_M3: resultado del cuestionario complementario del Módulo 3 en formato X/45 o el valor especial no se presentó
  - TRYB_QUM_M3: modalidad de realización del cuestionario complementario del Módulo 3 (autoevaluación o recuperación o no aplica)
  - WYNIK_TEST_M1: resultado de la prueba de módulo del Módulo 1 (lección l8 de la semana 4) en formato X/110 o el valor especial no se presentó
  - WYNIK_TEST_M2: resultado de la prueba de módulo del Módulo 2 (lección l8 de la semana 4) en formato X/40 o el valor especial no se presentó
  - WYNIK_TEST_M3: resultado de la prueba de módulo del Módulo 3 (lección l8 de la semana 4, equivalente a la prueba final del Curso) en formato X/108 o el valor especial no se presentó
  - WYNIK_TKK: resultado de la prueba final del Curso en formato X/108 o el valor especial no se presentó
  - DECYZJA_TKK: decisión tras la prueba final del Curso (aprobado o no aprobado o no se presentó)
  - KOMENTARZ_INSTRUKTORA: comentario breve del instructor para el Kursante sobre la imagen general del progreso (opcional)
  - INSTRUKTOR: nombre y apellido del instructor que dirige al Kursante
  - KOORDYNATOR_KURSU: nombre y apellido del coordinador del Curso
  - NR_KARTY_POSTEPOW: número de registro de la ficha de progreso (por ejemplo, 2026/001/KP)
---

# FICHA DE PROGRESO DEL KURSANTE

**Curso práctico „Praca w tartaku" (Trabajo en aserradero)**: curso profesional para personas extranjeras que residen legalmente en el territorio de la República de Polonia, organizado de forma gratuita por la Fundación de asistencia jurídica EGIDA.

---

## Información preliminar

La presente ficha de progreso documenta **la imagen completa de los resultados del Kursante (cursante) durante el ciclo del Curso** en relación con todas las herramientas de evaluación: pruebas parciales, cuestionarios complementarios, pruebas de módulo (lecciones l8 de la semana 4 de cada Módulo) y prueba final del Curso. La ficha es **una herramienta de información de retorno** para el Kursante y **base de las decisiones metodológicas** del instructor (planificación de repasos, decisiones sobre la modalidad de autoevaluación o de recuperación, evaluación de la preparación del Kursante para el examen práctico).

La ficha se emite al Kursante en su idioma materno (polaco, inglés, español o ucraniano) y, con independencia del idioma del Kursante, en versión polaca para los archivos del Curso.

La ficha es un documento parametrizado: la ficha real para un Kursante concreto y un momento concreto del ciclo se genera sustituyendo los campos `{{NAZWA_POLA}}` por los valores de la hoja de datos de la edición del Curso (CSV) mediante un script generador. La lista de identificadores de los campos de datos se encuentra en el encabezado YAML de este documento, en el campo `parametry`.

| Identificador del modelo[^1] | Número de registro de la ficha de progreso[^2] | Fecha de generación de la ficha (DD-MM-AAAA) |
|---|---|---|
| KP-1.0/2026 | {{NR_KARTY_POSTEPOW}} | {{DATA_GENERACJI}} |

---

## Parte A. Identificación del Kursante

| Campo | Valor |
|---|---|
| Nombre (nombres) del Kursante: | {{IMIE_KURSANTA}} |
| Apellido del Kursante: | {{NAZWISKO_KURSANTA}} |
| Número de tarjeta de participante del Kursante: | {{NR_KARTY_UCZESTNIKA}} |
| Ciclo del Curso: | {{CYKL_KURSU}} |
| Instructor responsable: | {{INSTRUKTOR}} |

---

## Parte B. Resultados de las herramientas de evaluación

### Pruebas parciales del Módulo 1

Las pruebas parciales son una herramienta de diagnóstico intermedio del progreso del Kursante después de la segunda y la tercera semana del Módulo 1. Cada prueba consta de 15 preguntas cerradas de 2 puntos cada una (30 puntos en total), con un umbral de aprobación del 70 %, es decir, 21 puntos. No se prevén pruebas parciales para el Módulo 2 ni el Módulo 3 en la versión actual del programa del Curso.

| Herramienta | Identificador del modelo | Máximo | Resultado del Kursante |
|---|---|---|---|
| Prueba parcial M1 (T1+T2) | SPC-M1-T12-1.0/2026 | 30 puntos | {{WYNIK_SPC_M1_T12}} |
| Prueba parcial M1 (T3+T4) | SPC-M1-T34-1.0/2026 | 30 puntos | {{WYNIK_SPC_M1_T34}} |

### Cuestionarios complementarios de los Módulos

Los cuestionarios complementarios son una herramienta de autoevaluación tras la prueba de módulo (cuando se ha aprobado) o una modalidad de recuperación (cuando la prueba de módulo no se ha aprobado). La modalidad de realización del cuestionario se indica en la columna „Modalidad".

| Herramienta | Identificador del modelo | Máximo | Resultado del Kursante | Modalidad |
|---|---|---|---|---|
| Cuestionario complementario M1 | QUM-M1-1.0/2026 | 30 puntos | {{WYNIK_QUM_M1}} | {{TRYB_QUM_M1}} |
| Cuestionario complementario M2 | QUM-M2-1.0/2026 | 110 puntos | {{WYNIK_QUM_M2}} | {{TRYB_QUM_M2}} |
| Cuestionario complementario M3 | QUM-M3-1.0/2026 | 45 puntos | {{WYNIK_QUM_M3}} | {{TRYB_QUM_M3}} |

### Pruebas de módulo (lección l8 de la semana 4)

Las pruebas de módulo son las herramientas básicas de aprobación de cada Módulo del Curso. Se realizan como lección l8 de la semana 4 de cada Módulo. El umbral de aprobación de la prueba de módulo es del 70 % de los puntos; la no aprobación implica la repetición de las lecciones seleccionadas y una recuperación.

| Herramienta | Máximo | Umbral de aprobación (70 %) | Resultado del Kursante |
|---|---|---|---|
| Prueba de módulo M1 (l8 de la semana 4 del Módulo 1) | 110 puntos | 77 puntos | {{WYNIK_TEST_M1}} |
| Prueba de módulo M2 (l8 de la semana 4 del Módulo 2) | 40 puntos | 28 puntos | {{WYNIK_TEST_M2}} |
| Prueba de módulo M3 (l8 de la semana 4 del Módulo 3, equivalente a la prueba final del Curso) | 108 puntos | 76 puntos | {{WYNIK_TEST_M3}} |

### Prueba final del Curso

La prueba final del Curso abarca el contenido de los tres Módulos en una proporción del 20 % / 30 % / 50 % y es condición para acceder al examen práctico y para la emisión del certificado de finalización del Curso. En la práctica, la prueba final del Curso coincide con la prueba de módulo del Módulo 3 (lección l8 de la semana 4 del Módulo 3); por tanto, el resultado de la prueba final reproduce el resultado de la fila „Prueba de módulo M3" más arriba. El campo se mantiene en la ficha como entrada independiente porque algunos ciclos del Curso pueden introducir una prueba final adicional separada con un número de registro distinto.

| Herramienta | Identificador del modelo | Máximo | Umbral de aprobación (70 %) | Resultado del Kursante | Decisión |
|---|---|---|---|---|---|
| Prueba final del Curso | TKK-1.0/2026 | 108 puntos | 76 puntos | {{WYNIK_TKK}} | {{DECYZJA_TKK}} |

---

## Parte C. Comentario del instructor

{{KOMENTARZ_INSTRUKTORA}}

---

## Parte D. Firmas

| Parte | Nombre y apellido | Fecha | Firma |
|---|---|---|---|
| Kursante (confirmación de recepción de la ficha) | {{IMIE_KURSANTA}} {{NAZWISKO_KURSANTA}} | {{DATA_GENERACJI}} | _________________ |
| Instructor responsable | {{INSTRUKTOR}} | {{DATA_GENERACJI}} | _________________ |
| Coordinador del Curso | {{KOORDYNATOR_KURSU}} | {{DATA_GENERACJI}} | _________________ |

---

## Mención al proyecto

El Curso „Praca w tartaku" (Trabajo en aserradero) ha surgido como resultado del potencial desarrollado en el marco del proyecto „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Construcción de los fundamentos de apoyo a las personas extranjeras en el mercado laboral del voivodato de Opole), ejecutado por la Asociación SMART (líder) en cooperación con la Fundación de asistencia jurídica EGIDA (socio) en los años 2026-2027 con fondos del Fondo Social Europeo Plus. El propio Curso no se financia con los fondos del proyecto y no constituye una acción del proyecto; es una iniciativa estatutaria independiente de la Fundación, llevada a cabo de forma gratuita en favor de las personas extranjeras.

---

## Notas

[^1]: El identificador del modelo determina la versión del modelo de la ficha de progreso en el formato: KP (abreviatura de „Karta Postępów", ficha de progreso), número de versión, año de vigencia. El número de versión se incrementa con cada actualización del modelo por parte de la Fundación.

[^2]: El número de registro de la ficha de progreso lo asigna el coordinador del Curso en el momento de la generación de la ficha. El número tiene el formato: año / número correlativo del año / KP (por ejemplo, 2026/001/KP). Cada Kursante puede recibir varias fichas de progreso durante el ciclo (por ejemplo, después de la prueba de módulo M1, M2, M3 y después de la prueba final), con números de registro y fechas de generación independientes.

---

*Documento elaborado por la Fundación de asistencia jurídica EGIDA. Modelo sujeto a control interno de versiones. El ejemplar del Kursante y el ejemplar de la Fundación son idénticos en cuanto al contenido.*
