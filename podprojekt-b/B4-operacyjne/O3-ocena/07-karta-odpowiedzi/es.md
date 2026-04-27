---
typ: karta odpowiedzi
dokument: hoja de respuestas para el cuestionario complementario del Módulo del Curso (hoja universal cumplimentada por el Kursant)
kurs: Praca w tartaku
podprojekt: B
faza: B4-operacyjne
grupa: O3-ocena
klasa: 2
parametryzacja: CSV-DOCX
język: es
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. f w zakresie diagnozy efektów uczenia się Kursanta
charakter: formulario universal de respuestas cumplimentado a mano por el Kursant durante el cuestionario complementario de cualquiera de los tres Módulos del Curso; la hoja se cumplimenta en presencia del instructor o del coordinador y se entrega para su evaluación
strony: Kursant (cumplimentando la hoja), instructor del Curso (evaluando la hoja), Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA, autora y propietaria del modelo)
parametry:
  - IMIE_KURSANTA - nombre (nombres) del Kursant
  - NAZWISKO_KURSANTA - apellido del Kursant
  - NR_KARTY - número de registro de la hoja de respuestas (por ejemplo, 2026/C1/001/KO)
  - KOD_QUIZU - identificador del cuestionario al que se adjunta la hoja (por ejemplo, QUM-M1-1.0/2026)
  - NUMER_MODULU - número del Módulo al que se refiere el cuestionario (1, 2 o 3)
  - TRYB_QUIZU - modalidad de realización del cuestionario (autoevaluación o de recuperación)
  - DATA_QUIZU - fecha de cumplimentación de la hoja en formato DD-MM-AAAA
  - CYKL_KURSU - identificación del ciclo del Curso en el que participa el Kursant (por ejemplo, C1/2026)
  - KOORDYNATOR_KURSU - nombre y apellido del coordinador o instructor que recibe la hoja
  - LICZBA_ZAMKNIETYCH - número de preguntas cerradas en el cuestionario (por ejemplo, 15 para M1, 30 para M2, 15 para M3)
  - LICZBA_OTWARTYCH - número de preguntas abiertas en el cuestionario (por ejemplo, 0 para M1, 15 para M2, 0 para M3)
  - LICZBA_CASEOW - número de preguntas tipo caso en el cuestionario (por ejemplo, 0 para M1, 10 para M2, 0 para M3)
  - CZAS_TRWANIA_MIN - tiempo previsto de cumplimentación de la hoja en minutos (por ejemplo, 30 para M1, 120 para M2, 60 para M3)
  - NAZWA_POLA - nombre genérico del campo de datos sustituido por el script generador
---

# HOJA DE RESPUESTAS PARA EL CUESTIONARIO COMPLEMENTARIO DEL MÓDULO

**Curso práctico „Praca w tartaku" (Trabajo en aserradero)**: curso profesional para personas extranjeras que residen legalmente en el territorio de la República de Polonia, organizado de forma gratuita por la Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA).

---

## Información preliminar

Esta hoja de respuestas sirve para documentar las respuestas del Kursant a las preguntas del cuestionario complementario de cualquiera de los tres Módulos del Curso. La hoja es **universal**: contiene tres partes correspondientes a los tres tipos de preguntas que aparecen en los cuestionarios de los Módulos (cerradas, abiertas, casos). El Kursant cumplimenta solamente las partes que se corresponden con la estructura del cuestionario al que se adjunta la hoja - el número de preguntas en cada parte está indicado en el encabezado de la hoja (campo „Número de preguntas en el cuestionario"). El resto de las filas o campos se dejan sin cumplimentar.

La hoja se cumplimenta de forma **autónoma**, con bolígrafo o lápiz, en presencia del coordinador o instructor del Curso. No se permite el uso de apuntes, manuales, teléfono, ordenador ni la ayuda de otras personas. El tiempo de cumplimentación de la hoja se indica en el encabezado de la hoja (campo „Duración del cuestionario"). Transcurrido el tiempo, el Kursant termina de cumplimentarla y la entrega.

La hoja es un documento parametrizado: la hoja real para un Kursant concreto y un ciclo concreto del Curso se genera mediante la sustitución de los campos `{{NAZWA_POLA}}` por los valores procedentes de la hoja de datos de la edición del Curso (CSV) por medio de un script generador. La lista de denominaciones de los campos de datos se encuentra en el encabezado YAML de este documento, en el campo `parametry`.

| Identificador del modelo[^1] | Número de registro de la hoja[^2] | Fecha de cumplimentación de la hoja (DD-MM-AAAA) |
|------------------------------|-----------------------------------|--------------------------------------------------|
| KO-1.0/2026                  | {{NR_KARTY}}                      | {{DATA_QUIZU}}                                   |

---

## Sección A. Identificación del Kursant y del cuestionario

| Campo | Valor |
|-------|-------|
| Nombre (nombres) del Kursant: | {{IMIE_KURSANTA}} |
| Apellido del Kursant: | {{NAZWISKO_KURSANTA}} |
| Ciclo del Curso: | {{CYKL_KURSU}} |
| Número del Módulo al que se refiere el cuestionario: | {{NUMER_MODULU}} |
| Identificador del cuestionario (código del modelo): | {{KOD_QUIZU}} |
| Modalidad del cuestionario: | {{TRYB_QUIZU}} |
| Duración del cuestionario (en minutos): | {{CZAS_TRWANIA_MIN}} |

### Número de preguntas en el cuestionario (información para el Kursant)

| Parte de la hoja | Tipo de preguntas | Número de preguntas en este cuestionario |
|------------------|-------------------|-------------------------------------------|
| Sección B | preguntas cerradas (A/B/C/D, una correcta) | {{LICZBA_ZAMKNIETYCH}} |
| Sección C | preguntas abiertas (respuesta de 1 a 3 frases) | {{LICZBA_OTWARTYCH}} |
| Sección D | preguntas tipo caso (análisis de 4 a 6 frases) | {{LICZBA_CASEOW}} |

Cumplimenta solamente las filas que se corresponden con el número real de preguntas del cuestionario. Las filas que excedan ese número, déjalas sin cumplimentar o táchalas con una barra inclinada.

---

## Sección B. Respuestas a las preguntas cerradas

En cada fila señala **una sola** respuesta (A, B, C o D) poniendo una x en la casilla correspondiente. Si no conoces la respuesta, señala „no sé". Si el cuestionario exige justificación de la respuesta (Módulo 3), escribe la justificación en la columna „Justificación" en 2 o 3 frases.

| Número de pregunta | A | B | C | D | no sé | Justificación (si es exigida) |
|--------------------|---|---|---|---|-------|-------------------------------|
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

## Sección C. Respuestas a las preguntas abiertas

En cada campo escribe la respuesta a la pregunta cuyo número se señala a la izquierda. La respuesta debe tener **de 1 a 3 frases**. Si no conoces la respuesta, escribe „no sé".

**Pregunta abierta 1**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 2**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 3**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 4**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 5**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 6**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 7**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 8**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 9**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 10**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 11**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 12**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 13**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 14**

|  |
|--|
|  |
|  |
|  |

**Pregunta abierta 15**

|  |
|--|
|  |
|  |
|  |

---

## Sección D. Respuestas a las preguntas tipo caso

En cada campo escribe el análisis de la situación descrita en la pregunta cuyo número se señala a la izquierda. El análisis debe tener **de 4 a 6 frases** y contener: descripción del problema desde la perspectiva del Kursant, indicación de las reglas o disposiciones aplicadas, propuesta de actuación.

**Caso 1**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 2**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 3**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 4**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 5**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 6**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 7**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 8**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 9**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

**Caso 10**

|  |
|--|
|  |
|  |
|  |
|  |
|  |
|  |

---

## Sección E. Declaración del Kursant

Por la presente declaro que he cumplimentado la hoja de respuestas de forma autónoma, sin recurrir a apuntes, manuales, teléfono, ordenador ni a la ayuda de otras personas. Las respuestas anotadas son mis propias respuestas. Comprendo que la hoja se entregará para su evaluación por el instructor del Curso conforme a la clave de respuestas vigente para el cuestionario en cuestión.

| Campo | Valor |
|-------|-------|
| Fecha de cumplimentación de la hoja (DD-MM-AAAA): | {{DATA_QUIZU}} |
| Firma manuscrita del Kursant: |  |

---

## Sección F. Recepción de la hoja por el coordinador o instructor

| Campo | Valor |
|-------|-------|
| Fecha de recepción de la hoja (DD-MM-AAAA): | {{DATA_QUIZU}} |
| Nombre y apellido del coordinador o instructor que recibe la hoja: | {{KOORDYNATOR_KURSU}} |
| Firma manuscrita del coordinador o instructor: |  |

---

## Mención del proyecto

El Curso „Praca w tartaku" (Trabajo en aserradero) ha surgido como resultado del potencial desarrollado en el marco del proyecto „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Construyendo los fundamentos para el apoyo a los extranjeros en el mercado laboral en el Voivodato de Opole), realizado por la Asociación SMART (líder) en colaboración con la Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA, socio) en los años 2026-2027 con fondos del Fondo Social Europeo Plus. El Curso en sí no se financia con fondos del proyecto y no constituye una acción del proyecto; es una iniciativa estatutaria independiente de la Fundación, llevada a cabo de forma gratuita en favor de las personas extranjeras.

---

## Notas al pie

[^1]: El identificador del modelo determina la versión del modelo de la hoja de respuestas en el formato: KO (abreviatura de „karta odpowiedzi", hoja de respuestas), número de versión, año de vigencia. El número de versión se incrementa con cada actualización del modelo por parte de la Fundación. La hoja es universal para los tres Módulos del Curso y para todas las modalidades del cuestionario (autoevaluación, de recuperación).

[^2]: El número de registro de la hoja lo asigna el coordinador del Curso en el momento de la recepción de la hoja cumplimentada del Kursant. El número tiene el formato: año / identificación del ciclo / número correlativo en el ciclo / KO (por ejemplo, 2026/C1/001/KO). El número está vinculado de manera unívoca con el número de la Tarjeta de participante del Kursant y con el identificador del cuestionario.

---

*Documento elaborado por la Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA). Modelo parametrizado; la hoja de respuestas real se genera mediante la sustitución de los campos `{{NAZWA_POLA}}` por los valores procedentes de la hoja de datos de la edición del Curso. La hoja, una vez cumplimentada y entregada para su evaluación, constituye un documento operativo del Curso y queda sujeta al archivo junto con el resto de la documentación del ciclo.*
