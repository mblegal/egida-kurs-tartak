---
typ: karta
dokument: ficha del participante del Curso (registro administrativo consolidado por Cursante)
kurs: Praca w tartaku (Trabajo en aserradero)
podprojekt: B
faza: B4-operacyjne
grupa: O1-wejście
klasa: 2
parametryzacja: CSV-DOCX
język: es
wersja: 1.0
stan-na: 2026-04-27
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) w zakresie dokumentowania działalności statutowej Fundacji
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), w szczególności art. 6 ust. 1 lit. b oraz lit. f w zakresie prowadzenia ewidencji uczestnictwa Kursanta w Kursie
charakter: registro administrativo consolidado de un único Cursante, que vincula mediante referencias todos los documentos operativos del Curso relativos a ese Cursante; la ficha se abre en el momento de la calificación del candidato y se cierra al finalizar el Curso o al darlo de baja de la lista
strony: Cursante (sujeto del registro), Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA, propietario del registro, coordinador del Curso)
parametry:
  - IMIE_KURSANTA - nombre (nombres) del Cursante
  - NAZWISKO_KURSANTA - apellido del Cursante
  - DATA_URODZENIA - fecha de nacimiento del Cursante en formato DD-MM-AAAA
  - OBYWATELSTWO - nacionalidad del Cursante
  - JEZYK_PIERWSZY - primer idioma del Cursante (PL, EN, ES, UK)
  - NR_FORMULARZA - número de registro del Formulario de inscripción
  - NR_OSWIADCZENIA_KWALIFIKOWALNOSCI - número de registro de la declaración de elegibilidad
  - NR_TESTU_WEJSCIOWEGO - número de registro de la prueba de ingreso
  - NR_ANKIETY_WSTEPNEJ - número de registro de la encuesta inicial
  - NR_UMOWY_KURSU - número de registro del contrato del curso
  - CYKL_KURSU - identificación del ciclo del Curso (p. ej. C1/2026)
  - MODUL_GLOWNY - módulo en el que participa el Cursante (M1, M2, M3)
  - DATA_OTWARCIA_KARTY - fecha de apertura de la ficha en formato DD-MM-AAAA
  - KOORDYNATOR_KURSU - nombre y apellido del coordinador del Curso que abre la ficha
  - NR_KARTY - número de registro de la ficha (p. ej. 2026/C1/001/KU)
---

# FICHA DEL PARTICIPANTE DEL CURSO

**Registro administrativo consolidado del Cursante que participa en el Curso práctico „Praca w tartaku" (Trabajo en aserradero).** La ficha se abre en el momento de la decisión positiva sobre la calificación del candidato; cumple la función de índice de todos los documentos operativos del Curso relativos al Cursante. La ficha es un documento interno de la Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA) y no se entrega al Cursante (el Cursante tiene derecho de acceso conforme al RGPD según las condiciones de la cláusula informativa).

---

## Información preliminar

La ficha del participante cumple la función de registro administrativo básico del Curso en el contexto de un Cursante individual. Cada Cursante calificado para un ciclo del Curso recibe su propia ficha. La ficha contiene datos de identificación, referencias a todos los documentos operativos relativos al Cursante, un resumen del estado de participación y el resultado final del Curso (si el Curso ha sido completado).

La ficha se abre inmediatamente tras la admisión del candidato al Curso y se cierra inmediatamente tras:

a) la expedición del certificado de finalización del Curso al Cursante que ha completado el Curso; o bien

b) la expedición del acta de baja del Cursante de la lista de participantes, si el Cursante ha sido dado de baja.

La ficha es un documento parametrizado: el modelo a continuación contiene marcadores de campos de datos en forma de `{{NOMBRE_DEL_CAMPO}}`. La ficha real de un Cursante concreto se genera reemplazando los marcadores con los valores procedentes de la hoja de datos de la edición del Curso (CSV) mediante un script generador. La lista de marcadores de campos de datos se encuentra en el encabezado YAML de este documento, en el campo `parametry`.

| Identificador del modelo[^1] | Número de registro de la ficha[^2] | Fecha de apertura de la ficha (DD-MM-AAAA) |
|--------------------------|------------------------------|-----------------------------------|
| KU-1.0/2026              | {{NR_KARTY}}                 | {{DATA_OTWARCIA_KARTY}}           |

---

## Parte A. Datos de identificación del Cursante

| Campo | Valor |
|------|---------|
| Nombre (nombres): | {{IMIE_KURSANTA}} |
| Apellido: | {{NAZWISKO_KURSANTA}} |
| Fecha de nacimiento (DD-MM-AAAA): | {{DATA_URODZENIA}} |
| Nacionalidad: | {{OBYWATELSTWO}} |
| Primer idioma del Cursante: | {{JEZYK_PIERWSZY}} |
| Número de registro del Formulario de inscripción: | {{NR_FORMULARZA}} |

Los datos personales detallados (dirección de correspondencia, documentos de residencia, contacto de emergencia) se encuentran en el Formulario de inscripción con el número de registro indicado arriba y no se repiten en la presente ficha en virtud del principio de minimización de datos del art. 5 ap. 1 letra c) del RGPD.

---

## Parte B. Documentos operativos vinculados

La ficha indexa todos los documentos operativos del Curso relativos al Cursante. En la columna „Número de registro" se introduce el número de la posición indicada o la mención „no aplica", si el documento no ha sido (todavía) expedido.

### B.1. Documentos de ingreso

| Documento | Número de registro | Estado en la fecha de apertura de la ficha |
|----------|--------------------|-------------------------------|
| Formulario de inscripción (FRK) | {{NR_FORMULARZA}} | expedido |
| Declaración de elegibilidad (OSK) | {{NR_OSWIADCZENIA_KWALIFIKOWALNOSCI}} | expedida |
| Prueba de ingreso (TW) | {{NR_TESTU_WEJSCIOWEGO}} | expedida o no aplica |
| Encuesta inicial (AW) | {{NR_ANKIETY_WSTEPNEJ}} | expedida o no aplica |
| Contrato del curso (UK) | {{NR_UMOWY_KURSU}} | expedido o pendiente de firma |

### B.2. Documentos de ejecución (a completar durante el Curso)

| Documento | Frecuencia | Modo de registro en la ficha |
|----------|---------------|----------------------------|
| Listas de asistencia diaria (LO) | por sesión | de forma agregada en la parte D.1 |
| Acta de la formación en seguridad e higiene en el trabajo (PIB) | por módulo o por puesto de trabajo | anotación en la parte D.2 |
| Registro de materiales entregados (RM) | abierto al inicio, cerrado al final | anotación en la parte D.3 |

### B.3. Documentos de cierre (a completar al finalizar el Curso)

| Documento | Número de registro | Estado |
|----------|--------------------|------|
| Resultado de la prueba final | anotación en la parte E.2 | expedido o no aplica |
| Certificado de finalización del Curso (Z-UK) | anotación en la parte F.1 | expedido o no aplica |
| Acta de baja de la lista (si procede) | anotación en la parte F.2 | expedida o no aplica |

---

## Parte C. Estado de participación del Cursante

| Campo | Valor |
|------|---------|
| Ciclo del Curso: | {{CYKL_KURSU}} |
| Módulo en el que participa el Cursante: | {{MODUL_GLOWNY}} |
| Fecha de apertura de la ficha: | {{DATA_OTWARCIA_KARTY}} |

### C.1. Estado actual (marcar uno)

☐ calificado, en espera del inicio del ciclo  
☐ participante activo, en curso de un módulo  
☐ participante suspendido temporalmente (por la causa descrita en D.4)  
☐ participante que ha completado el Curso (certificado expedido)  
☐ participante dado de baja de la lista (acta de baja expedida)  
☐ otro estado (describir abajo)

Descripción del otro estado (si procede):

|  |
|--|
|  |

---

## Parte D. Ejecución del Curso: asistencia y desarrollo

### D.1. Asistencia acumulada (a completar por el coordinador tras cada sesión)

| Módulo | Número de sesiones del módulo | Número de sesiones con asistencia | Asistencia porcentual |
|-------|------------------------|------------------------|------------------------|
| M1 |  |  |  |
| M2 |  |  |  |
| M3 |  |  |  |
| Total |  |  |  |

### D.2. Formaciones en seguridad e higiene en el trabajo

| Etapa | Fecha de la formación (DD-MM-AAAA) | Número del acta PIB | Observaciones |
|------|--------------------------------|----------------------|-------|
| Antes de M1 |  |  |  |
| Antes de M2 |  |  |  |
| Antes de M3 |  |  |  |
| Otra |  |  |  |

### D.3. Registro de materiales entregados

| Campo | Valor |
|------|---------|
| Número de registro del registro de materiales (RM): |  |
| Fecha de apertura del registro: |  |
| Fecha de cierre del registro: |  |
| Estado de liquidación de los préstamos: | ☐ liquidados en su totalidad ☐ liquidados con observaciones ☐ no liquidados |

### D.4. Eventos relevantes durante el Curso

|  |
|--|
|  |

---

## Parte E. Resultados didácticos

### E.1. Resultados de las pruebas modulares

| Módulo | Fecha de la prueba (DD-MM-AAAA) | Puntuación obtenida | Puntuación máxima | Resultado porcentual | Aprobada |
|-------|--------------------------|----------------------------|------------------------------|------------------|-----------|
| M1 |  |  |  |  | ☐ sí ☐ no |
| M2 |  |  |  |  | ☐ sí ☐ no |
| M3 |  |  |  |  | ☐ sí ☐ no |

### E.2. Prueba final del Curso

| Campo | Valor |
|------|---------|
| Fecha de la prueba final (DD-MM-AAAA): |  |
| Puntuación obtenida: |  |
| Puntuación máxima: |  |
| Resultado porcentual: |  |
| Resultado de la prueba final: | ☐ aprobada ☐ no aprobada ☐ no presentado |

### E.3. Hoja individual de evaluación del instructor (cualitativa)

|  |
|--|
|  |

---

## Parte F. Cierre de la ficha

### F.1. Expedición del certificado de finalización del Curso

| Campo | Valor |
|------|---------|
| Fecha de expedición del certificado (DD-MM-AAAA): |  |
| Número de registro del certificado: |  |
| Modo de entrega del certificado: | ☐ en persona contra acuse de recibo ☐ por correo postal ☐ por vía electrónica |
| Fecha de entrega del certificado al Cursante: |  |

### F.2. Baja de la lista de participantes (si procede)

| Campo | Valor |
|------|---------|
| Fecha de baja (DD-MM-AAAA): |  |
| Número de registro del acta de baja: |  |
| Motivo de la baja: | ☐ renuncia del Cursante ☐ asistencia baja por debajo del umbral del Reglamento del Curso ☐ no aprobación de la prueba final ☐ infracción grave de las normas de seguridad e higiene en el trabajo ☐ otro motivo (describir abajo) |
| Descripción del otro motivo de baja (si procede): |  |

### F.3. Cierre de la ficha

| Campo | Valor |
|------|---------|
| Fecha de cierre de la ficha (DD-MM-AAAA): |  |
| Nombre y apellido del coordinador que cierra la ficha: |  |
| Firma manuscrita del coordinador que cierra la ficha: |  |

---

## Parte G. Notas del coordinador

En esta parte el coordinador anota observaciones de carácter administrativo relativas al Cursante, tales como contactos relevantes con el Cursante, modificaciones de datos, señales de los instructores, decisiones del coordinador.

|  |
|--|
|  |

---

## Parte H. Apertura de la ficha

| Campo | Valor |
|------|---------|
| Fecha de apertura de la ficha (DD-MM-AAAA): | {{DATA_OTWARCIA_KARTY}} |
| Nombre y apellido del coordinador que abre la ficha: | {{KOORDYNATOR_KURSU}} |
| Firma manuscrita del coordinador que abre la ficha: |  |

---

## Mención del proyecto

El Curso „Praca w tartaku" (Trabajo en aserradero) ha surgido como resultado del potencial desarrollado en el marco del proyecto „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Construcción de los fundamentos de apoyo a los extranjeros en el mercado laboral de la voivodía de Opole), ejecutado por la Asociación SMART (líder) en colaboración con la Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA, socio) en los años 2026-2027 con financiación del Fondo Social Europeo Plus. El propio Curso no se financia con fondos del proyecto y no constituye una acción del proyecto; es una iniciativa estatutaria independiente de la Fundación, llevada a cabo de forma gratuita en favor de personas extranjeras.

---

## Notas al pie

[^1]: El identificador del modelo determina la versión del modelo de la ficha en la forma: KU (abreviatura de „karta uczestnika", ficha del participante) - número de versión - año de vigencia. El número de versión se incrementa con cada actualización del modelo realizada por la Fundación.

[^2]: El número de registro de la ficha lo asigna el coordinador del Curso en el momento de la apertura de la ficha. El número tiene la forma: año / identificación del ciclo / número correlativo en el ciclo / KU (p. ej. 2026/C1/001/KU). El número está vinculado de forma unívoca con el número del Formulario de inscripción del Cursante.

---

*Documento elaborado por la Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA). Modelo parametrizado; la ficha real se genera reemplazando los campos `{{NOMBRE_DEL_CAMPO}}` con los valores procedentes de la hoja de datos de la edición del Curso. La ficha del participante constituye un documento interno de la Fundación.*
