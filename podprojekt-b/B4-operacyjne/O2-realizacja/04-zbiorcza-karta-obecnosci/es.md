---
typ: tarjeta
dokument: tarjeta acumulativa de asistencia del Cursante (resumen acumulado de asistencia a todas las sesiones del ciclo)
kurs: Praca w tartaku (Trabajo en aserradero)
podprojekt: B
faza: B4-operacyjne
grupa: O2-realizacja
klasa: 2
parametryzacja: CSV-DOCX
język: es
wersja: 1.0
stan-na: 27-04-2026
podstawa-prawna:
  - Ustawa z dnia 24 kwietnia 2003 r. o działalności pożytku publicznego i o wolontariacie (tekst jednolity Dz.U. z 2024 r. poz. 1491 z późn. zm.) en el ámbito de la documentación de la actividad estatutaria de la Fundación
  - Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO), en particular el art. 6 ap. 1 lit. b y lit. f en el ámbito de la información de retorno al Cursante sobre su asistencia
charakter: documento individual por Cursante; resumen acumulativo de la asistencia a todas las sesiones del ciclo del Curso; cumple el papel de información de retorno para el Cursante y de base de la decisión de admisión a la prueba final
strony: Cursante (destinatario de la información sobre su asistencia), Fundacja pomocy prawnej EGIDA (Fundación de Asistencia Jurídica EGIDA) (entidad que la elabora y propietaria del registro)
parametry:
  - IMIE_KURSANTA - nombre (nombres) del Cursante
  - NAZWISKO_KURSANTA - apellido del Cursante
  - NR_KARTY_UCZESTNIKA - número de registro de la Tarjeta del participante (KU) vinculada
  - NR_FORMULARZA - número de registro del Formulario de inscripción
  - CYKL_KURSU - identificación del ciclo del Curso
  - MODUL_GLOWNY - módulo en el que participa el Cursante (M1, M2, M3)
  - DATA_OTWARCIA_KARTY - fecha de apertura de la tarjeta (normalmente la fecha de la primera sesión)
  - DATA_ZAMKNIECIA_KARTY - fecha de cierre de la tarjeta (normalmente la fecha de la última sesión)
  - LACZNA_LICZBA_SESJI - número total de sesiones del ciclo a la fecha de cierre de la tarjeta
  - LICZBA_SESJI_OBECNYCH - número de sesiones a las que el Cursante ha asistido
  - FREKWENCJA_PROCENTOWA - asistencia del Cursante expresada en porcentaje
  - PROG_FREKWENCJI_REGULAMIN - umbral de asistencia exigido por el Reglamento del Curso (p. ej. 80%)
  - DECYZJA_DOPUSZCZENIA - decisión sobre la admisión del Cursante a la prueba final (sí / no / condicionalmente)
  - KOORDYNATOR_KURSU - nombre y apellido del coordinador que firma la tarjeta
  - NR_KARTY_OBECNOSCI - número de registro de la tarjeta acumulativa de asistencia (p. ej. 2026/C1/001/ZKO)
---

# ZBIORCZA KARTA OBECNOŚCI KURSANTA (TARJETA ACUMULATIVA DE ASISTENCIA DEL CURSANTE)

**Resumen acumulado de la asistencia del Cursante a todas las sesiones del ciclo del Curso práctico „Praca w tartaku" (Trabajo en aserradero).** La tarjeta es elaborada de forma individual para cada Cursante por el coordinador del Curso, sobre la base de las listas de asistencia diarias. La tarjeta se entrega al Cursante en copia tras el cierre del ciclo, como información de retorno sobre su asistencia, y se incorpora al expediente del Cursante.

---

## Información preliminar

La tarjeta acumulativa de asistencia cumple dos funciones:

a) **interna**: constituye la base de la decisión del coordinador del Curso sobre la admisión del Cursante a la prueba final y, posteriormente, sobre la expedición del certificado de finalización del Curso, conforme al umbral de asistencia establecido en el Reglamento del Curso;

b) **externa**: constituye información de retorno para el Cursante sobre su asistencia real, entregada en copia conforme al derecho del Cursante de acceder a sus propios datos personales tratados por la Fundación.

La tarjeta se elabora actualizando la cuadrícula de asistencia tras cada sesión y se cierra al finalizar el ciclo con un resumen totalizador.

| Identificador del modelo[^1] | Número de registro de la tarjeta[^2] | Ciclo del Curso | Tarjeta del participante vinculada |
|--------------------------|------------------------------|------------|------------------------------|
| ZKO-1.0/2026             | {{NR_KARTY_OBECNOSCI}}       | {{CYKL_KURSU}} | {{NR_KARTY_UCZESTNIKA}}   |

---

## Część A (Sección A). Identificación del Cursante

| Campo | Valor |
|------|---------|
| Nombre (nombres): | {{IMIE_KURSANTA}} |
| Apellido: | {{NAZWISKO_KURSANTA}} |
| Número de registro del Formulario de inscripción: | {{NR_FORMULARZA}} |
| Número de registro de la Tarjeta del participante vinculada: | {{NR_KARTY_UCZESTNIKA}} |
| Ciclo del Curso: | {{CYKL_KURSU}} |
| Módulo en el que participa el Cursante: | {{MODUL_GLOWNY}} |
| Fecha de apertura de la tarjeta (DD-MM-AAAA): | {{DATA_OTWARCIA_KARTY}} |

---

## Część B (Sección B). Cuadrícula de asistencia por sesión

Cada fila de la tabla corresponde a una sola sesión del ciclo, en orden cronológico conforme al Cronograma detallado. En la columna „Asistencia" se anota uno de los siguientes signos: **+** (presente), **-** (ausente injustificado), **U** (ausente justificado), **S** (tardanza significativa, superior a 15 minutos), **W** (salida anticipada antes del final de la sesión).

| N.º de sesión | Fecha de la sesión (DD-MM-AAAA) | Módulo | Título de la sesión | Asistencia | Número de la Lista de asistencia (LO) |
|-----------|--------------------------|-------|--------------|-----------|------------------------------|
| 1   |  |  |  |  |  |
| 2   |  |  |  |  |  |
| 3   |  |  |  |  |  |
| 4   |  |  |  |  |  |
| 5   |  |  |  |  |  |
| 6   |  |  |  |  |  |
| 7   |  |  |  |  |  |
| 8   |  |  |  |  |  |
| 9   |  |  |  |  |  |
| 10  |  |  |  |  |  |
| 11  |  |  |  |  |  |
| 12  |  |  |  |  |  |
| 13  |  |  |  |  |  |
| 14  |  |  |  |  |  |
| 15  |  |  |  |  |  |
| 16  |  |  |  |  |  |
| 17  |  |  |  |  |  |
| 18  |  |  |  |  |  |
| 19  |  |  |  |  |  |
| 20  |  |  |  |  |  |
| 21  |  |  |  |  |  |
| 22  |  |  |  |  |  |
| 23  |  |  |  |  |  |
| 24  |  |  |  |  |  |

---

## Część C (Sección C). Resumen numérico (a cumplimentar por el coordinador tras el cierre del ciclo)

### C.1. Asistencia por módulo

| Módulo | Número de sesiones del módulo | Número de sesiones asistidas | Número de sesiones de ausencia justificada | Número de sesiones de ausencia injustificada | Asistencia porcentual |
|-------|------------------------|------------------------|----------------------------------------------|------------------------------------------------|------------------------|
| M1 |  |  |  |  |  |
| M2 |  |  |  |  |  |
| M3 |  |  |  |  |  |
| **Total** | {{LACZNA_LICZBA_SESJI}} | {{LICZBA_SESJI_OBECNYCH}} |  |  | {{FREKWENCJA_PROCENTOWA}} |

### C.2. Umbral de asistencia exigido por el Reglamento del Curso

| Campo | Valor |
|------|---------|
| Umbral de asistencia establecido en el punto VII del Reglamento del Curso (en porcentaje): | {{PROG_FREKWENCJI_REGULAMIN}} |
| ¿La asistencia del Cursante alcanza el umbral?: | ☐ sí ☐ no ☐ concurren circunstancias especiales (descritas a continuación) |
| Descripción de las circunstancias especiales (si procede): |  |

---

## Część D (Sección D). Decisión sobre la admisión a la prueba final

| Campo | Valor |
|------|---------|
| Decisión del coordinador: | {{DECYZJA_DOPUSZCZENIA}} |
| Justificación breve de la decisión: |  |
| Fecha de adopción de la decisión (DD-MM-AAAA): |  |
| Nombre y apellido del coordinador que adopta la decisión: | {{KOORDYNATOR_KURSU}} |
| Firma autógrafa del coordinador: |  |

---

## Część E (Sección E). Entrega de la copia al Cursante

| Campo | Valor |
|------|---------|
| Fecha de cierre de la tarjeta (DD-MM-AAAA): | {{DATA_ZAMKNIECIA_KARTY}} |
| Fecha de entrega de la copia al Cursante (DD-MM-AAAA): |  |
| Modo de entrega de la copia: | ☐ en mano con acuse de recibo ☐ por correo postal ☐ por vía electrónica conforme al Contrato del curso |
| Anotación del Cursante sobre la recepción de la copia (si se ha entregado en mano): |  |
| Firma autógrafa del Cursante en la recepción de la copia (si se ha entregado en mano): |  |

---

## Mención del proyecto

El Curso „Praca w tartaku" ha surgido como resultado del potencial generado en el marco del proyecto „Budowa fundamentów wsparcia cudzoziemców na rynku pracy w województwie opolskim" (Construcción de los fundamentos del apoyo a personas extranjeras en el mercado laboral de la voivodía de Opole), ejecutado por Stowarzyszenie SMART (líder) en cooperación con Fundacja pomocy prawnej EGIDA (socio) en los años 2026-2027 con fondos del Fondo Social Europeo Plus. El propio Curso no se financia con los fondos del proyecto y no constituye una acción del proyecto; es una iniciativa estatutaria independiente de la Fundación, impartida de forma gratuita en favor de las personas extranjeras.

---

## Notas

[^1]: El identificador del modelo determina la versión del modelo de la tarjeta acumulativa de asistencia con la forma: ZKO (abreviatura de „zbiorcza karta obecności", tarjeta acumulativa de asistencia), número de versión, año de vigencia. El número de versión se incrementa con cada actualización del modelo por parte de la Fundación.

[^2]: El número de registro de la tarjeta acumulativa de asistencia es asignado por el coordinador del Curso en el momento de la apertura de la tarjeta (normalmente el día de la primera sesión del ciclo). El número tiene la forma: año / identificación del ciclo / número correlativo del ciclo / ZKO (p. ej. 2026/C1/001/ZKO). El número debe corresponder al número de la Tarjeta del participante vinculada (conservando el sufijo distinto KU o ZKO).

---

*Documento elaborado por Fundacja pomocy prawnej EGIDA. Modelo parametrizado; la tarjeta efectiva se obtiene sustituyendo los campos `{{NAZWA_POLA}}` por los valores de la hoja de datos de la edición del Curso e introduciendo la asistencia en la sección B. La tarjeta acumulativa de asistencia se entrega al Cursante en copia tras el cierre del ciclo.*
