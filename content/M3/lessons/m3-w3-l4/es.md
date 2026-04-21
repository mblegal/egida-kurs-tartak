---
id: m3-w3-l4
blok: procesy
czas: 120
---

## Introducción

Viernes, 2026-05-30, 9:25. Once días después de la reunión de planificación de l3, once días del ciclo de roble común en la cámara BH-50. Rustam cruza el patio de almacén en dirección a la nave del secadero, con la libreta en la mano y en el bolsillo del mono el teléfono de empresa (Nokia antiguo, la batería aguanta una semana, cobertura en todo el aserradero). Marek le ha programado hoy de 9:30 a 11:30 una **presencia formativa en el secadero** como parte del bloque de procesos M3. Wahan hoy no está con Rustam, tiene turno de mantenimiento en P1 con Juri (mecánico junior de UR).

Rustam entra en la nave del secadero (12 × 8 × 4,5 m, la misma nave que en l3), y después en la **sala de control** (local de 2 × 3 m con el armario de control, ventanas de observación hacia la cámara y una pequeña mesa en el rincón). Pan Henryk ya está allí, tomando café del termo, Maciek Wiśniewski (ayudante del secadero, 19 años, técnico forestal de Ostróda, de l3) está de pie frente al panel con el **diario de fin de semana** en la mano. El diario es un cuaderno A4 de tapa dura, rellenado dos veces al día los fines de semana (sábado 10:00 y 16:00, domingo 10:00 y 16:00), a veces con más frecuencia si Maciek tiene ganas de revisar la cámara el sábado por la tarde.

### 9:30, lectura rutinaria

Pan Henryk, a Rustam: *„Buenos días. Siéntate, mira, escribe. Hoy te voy a mostrar cómo se lee el panel durante el ciclo. Del roble actual el jueves cumplimos el día catorce, mañana día quince, el domingo día dieciséis. La fase principal termina el domingo, el lunes pasamos al acondicionamiento."*

Rustam se sienta en la silla junto a la mesa, abre la libreta, apunta la fecha y la hora. El panel BH-50 muestra:

```
Cámara: BH-50 (Brunner-Hildebrand)
Programa: DUB-STAND-28 (roble común 28 mm, 22 días hasta 14%)
Carga: roble 2,5 m³, tablas 30 mm, inicio 2026-05-17
Día del ciclo: 14 de 22
Fase actual: secado principal, día 12 de 14 (termina 2026-06-01)

Temperatura del aire:          58°C  (objetivo 60°C, tolerancia ±3)
Humedad relativa (RH):         47%   (objetivo 45%, tolerancia ±5)
Humedad madera sonda 1:        24,8% (inicio 38%, ayer 25,3%)
Humedad madera sonda 2:        24,1% (inicio 37,6%, ayer 24,6%)
Humedad madera sonda 3:        25,7% (inicio 38,5%, ayer 26,2%, más lento)
EMC (humedad de equilibrio):   8,4%
Dispersión sondas humedad:     1,6% (OK, por debajo del umbral 3%)
Estado ventiladores:           1450 RPM, corriente 6,2 A  (nominal 1500/6,5)
Estado resistencias:           45% de potencia (nominal 40-60% en fase principal)
```

Pan Henryk señala con la uña tres líneas: *„Mira. La humedad de la madera baja cada día 0,5-0,6%. Es una dinámica buena para roble día catorce. Hasta el día catorce, objetivo 14%, nos quedan 10-11% por evacuar en ocho días. Son **1,25% al día**. Subida del ritmo en el acondicionamiento, después ralentización en el tramo final. El plan aguanta."*

Rustam escribe: *„roble d.14, hum. 24-26%, EMC 8,4%, dispersión 1,6% OK, ventiladores ok."*

Pan Henryk: *„La **dispersión** es el indicador más importante de homogeneidad durante el ciclo. Si la sonda tres va más lenta en 1-2%, significa que en la zona donde está montada (parte trasera de la cámara) el flujo de aire es algo más débil. Normal. Cuando la diferencia sube a 3-4%, hay problema. Hoy 1,6%, tranquilos."*

### 9:40, Pan Henryk muestra el histórico de alarmas

Pan Henryk pincha en el panel la pestaña „Histórico de alarmas". En la pantalla aparece la lista de los últimos 30 días:

```
2026-05-19 03:47  INFO        Flujo de aire RPM 1400 (objetivo 1500, margen)
2026-05-22 16:23  ADVERTENCIA Ventilador 2 corriente 7,1 A (objetivo 6,5, +10%)  → auto-corrección
2026-05-27 08:15  INFO        Inicio del programa, día 1 de calentamiento
[posiciones restantes de ciclos de secado anteriores]
```

*„¿Ves, Rustam? **INFO** es una anotación, no alarma, no requiere reacción. **ADVERTENCIA** es nivel dos, el controlador se corrige solo, el operador observa. **ALARMA** es nivel tres, el controlador no corrige, requiere reacción humana. No ha habido alarmas en el último mes, es buena señal."*

Maciek vuelve a la nave de sierras con su propia tarea (carga del aserradero para un cliente de la tarde), cierra la puerta de la sala de control tras de sí.

### 9:45, salta la alarma

Pan Henryk se sirve más café del termo, Rustam mira el panel y de repente el **LED rojo** en la esquina de la pantalla empieza a parpadear. El controlador emite una señal acústica breve (tres pitidos, 1 segundo, después pausa de 2 segundos, después otra vez). En la pantalla el mensaje:

```
ALARMA: Temperatura del aire superada
Valor actual: 62,3°C
Objetivo del programa: 58,0°C
Desviación: +4,3°C (umbral de alarma +4)
Detectado: 2026-05-30, 09:43:12
Recomendación: Reducir potencia de resistencias o aumentar ventilación
```

Rustam se ha sobresaltado, el café en la taza de Pan Henryk se ha movido ligeramente. Pan Henryk habla tranquilo pero preciso: *„Rustam, ves el LED rojo. ¿Qué haces ahora?"*

Rustam piensa dos segundos. La lección de l3: el operador M3, en caso de alarma, **avisa al maestro de inmediato, no intenta resolver por su cuenta**. Pan Henryk está al lado, no hace falta llamar, basta con girarse. Rustam dice: *„Alarma de temperatura, 62,3 en vez de 58, desviación +4,3. Se lo comunico, ¿qué tengo que hacer?"*

Pan Henryk asiente: *„Bien. Primera cosa: **no reseteas la alarma**, porque aún no sabemos cuál es la causa. Segunda: **no entras en la cámara**. Tercera: **no cambias los ajustes del programa**. Ahora diagnostico yo, tú observas y aprendes. **Una alarma pequeña** es buen entrenamiento, porque no hay prisa."*

Pan Henryk abre la pestaña „Sensores actuales":

```
Sensor T1 (esquina A, frente-izquierda):  62,1°C
Sensor T2 (esquina B, frente-derecha):    62,5°C
Sensor T3 (esquina C, fondo-izquierda):   61,8°C
Sensor T4 (esquina D, fondo-derecha):     62,8°C
Media:                                    62,3°C
Dispersión entre sondas:                  1,0°C  (nominal <1,5°C)
```

*„Las cuatro sondas de temperatura muestran valores parecidos, entre 61,8 y 62,8. La dispersión es normal. **Significa que toda la cámara está más caliente**, no una sola zona. Si una sonda marcase 62 y las otras tres 58, sospecharía de un sensor dañado en una esquina. Aquí es toda la cámara. Primer diagnóstico: **no es un fallo del sensor**."*

Rustam anota: *„4 sondas juntas = cámara entera caliente, no un sensor. Primer diagnóstico."*

### 9:50, Pan Henryk revisa resistencias y válvula de gas

Pan Henryk abre la pestaña „Resistencias y suministros":

```
Resistencia 1 (entrada cámara): potencia actual 68% (objetivo 45%, por encima 23%)
Resistencia 2 (salida cámara):  potencia actual 64% (objetivo 45%, por encima 19%)
Válvula de gas principal:       apertura 72%       (objetivo 50%, por encima 22%)
Intercambiador calor T. entrada: 78°C               (objetivo 65°C, por encima 13°C)
Regulación proporcional:        AUTO                (funcionamiento normal)
```

*„A. **Las resistencias calientan demasiado**. Válvula de gas abierta al 72% en vez del 50%. El intercambiador de calor marca 78°C en vez de 65°C. Significa que el sistema **quema más gas del que manda el programa**. El controlador lo ha detectado, pero no compensa, porque las resistencias están en modo AUTO proporcional y algo o alguien ha subido la señal de referencia."*

Pan Henryk coge el teléfono, marca el número de Marek (encargado, en el móvil Marek está trabajando desde las 7:00):

*„Marek, soy Henryk del secadero. Tengo alarma de temperatura en la cámara del roble, más cuatro grados, resistencias abiertas al 68%, válvula de gas 72%. Sospecho del **termostato del intercambiador de calor**, que está obligando al sistema a calentar más de lo necesario. ¿Sabes? Oí ayer a BTM que tenían previsto cambiarnos ese termostato en julio en la revisión anual, pero ahora ya es demasiado pronto. ¿Puedes llamar al servicio técnico de BTM? Tienes el número en la carpeta."*

Marek confirma que llamará. Pan Henryk cuelga.

### 9:55, primera corrección manual

Pan Henryk a Rustam: *„Ahora voy a hacer una **corrección manual de la válvula de gas**, para bajar la temperatura en la cámara de 62 otra vez a 58. Es una decisión del **maestro del secadero**, no del operador M3. El operador M3 ni siquiera tiene contraseña de acceso a este panel, sólo lo ve en modo informativo."*

Pan Henryk teclea la contraseña (6 dígitos, cambiada cada trimestre por BTM), abre la ventana de control manual:

```
Control manual de resistencias:
Resistencia 1: actual 68%, cambiar a: 40% [confirmar]
Resistencia 2: actual 64%, cambiar a: 40% [confirmar]
Válvula de gas: actual 72%, cambiar a: 45% [confirmar]

Atención: el cambio manual desactiva el modo AUTO durante 30 minutos.
Tras 30 minutos el controlador vuelve a AUTO con los nuevos valores.
Si quieres que el modo AUTO quede desactivado más tiempo, introduce
en „Opciones especiales, bloqueo AUTO N minutos".
```

Pan Henryk baja la resistencia 1 de 68% a 40%, la resistencia 2 de 64% a 40%, la válvula de gas de 72% a 45%. Confirma tres veces, el controlador desactiva el modo AUTO durante 30 minutos (de 9:55 a 10:25).

*„Rustam, la **regla de la velocidad máxima de cambio de temperatura** es **6°C por hora**. El roble no se puede enfriar más rápido que 6°C/h, porque provoca **rajas internas**. Un salto de 62 a 58 es una bajada de 4°C, debería producirse en 40 minutos, no en 5. El controlador irá bajando gradualmente. Observamos."*

### 10:00, observación de la tendencia

Pan Henryk y Rustam miran el panel, refresco cada 15 segundos. La temperatura en 5 minutos baja de 62,3 a 61,1 (bajada 1,2°C en 5 minutos, es decir **14,4°C/h**, demasiado rápido). Pan Henryk comenta: *„Demasiado rápido, pero esperable en los primeros minutos tras reducir el gas. El intercambiador de calor caliente sigue cediendo calor a la cámara aunque las resistencias reciban menos corriente. Esperamos, en unos 20 minutos la bajada debería estabilizarse."*

Rustam apunta observaciones cada 2 minutos:
- 09:55 62,3°C (inicio)
- 09:57 61,9°C (bajada 0,4)
- 10:00 61,1°C (bajada 0,8)
- 10:03 60,6°C (bajada 0,5)
- 10:05 60,2°C (bajada 0,4)
- 10:10 59,5°C (bajada 0,7 en 5 min)
- 10:15 58,8°C (bajada 0,7 en 5 min, estabilización)

*„10:15, temperatura 58,8, casi en el objetivo 58. Desde 9:55 bajada de 3,5°C en 20 minutos, es decir **10,5°C/h de media**. Está por encima del límite 6°C/h durante los primeros 10 minutos, luego se ha calmado. Demasiado rápido, pero no catastrófico para roble día catorce (la madera ya está parcialmente seca, menos sensible que al principio del ciclo). Lo dejamos así, monitorizamos."*

### 10:20, llamada de Marek con información de BTM

El teléfono de Pan Henryk vibra. Marek: *„Henryk, he llamado a BTM. El termostato del intercambiador de calor, modelo GH-67, es un problema conocido suyo desde 2024, un bucle de realimentación empuja la señal hacia calentar por encima del requerido cuando la humedad ambiente es 65%+ (fuera de la cámara, en la nave del secadero). Hoy la nave tiene 68% (tenemos una mañana lluviosa). Eso explica el comportamiento. BTM vendrá el lunes por la mañana, cambiará el termostato gratis con garantía. Hasta el lunes, **control manual**, correcciones cada 4-6 horas, yo te relevo el sábado por la mañana durante 2 horas, para que no estés aquí todo el fin de semana. Plan de fin de semana de Maciek vigente, sólo que además observación cada 4 horas, no cada 8."*

Pan Henryk confirma, anota en la libreta: *„Hasta lun 02.06 control manual, correcciones cada 4-6 h. Servicio BTM lun mañana."*

### 10:30, el controlador vuelve a AUTO con los nuevos valores

A las 10:25 el controlador vuelve automáticamente a modo AUTO. La temperatura se estabiliza en 58,2°C (cerca del objetivo 58), las resistencias bajan al 43% (cerca del objetivo 45%), la válvula de gas al 48% (cerca del objetivo 50%). Dispersión entre sondas 0,8°C. Dispersión de sondas de humedad de la madera 1,6% (sin cambios). La alarma ha desaparecido, el LED rojo se ha apagado a las 10:24.

Pan Henryk resetea el histórico de alarmas (confirma en el diario de la cámara), apunta en la nota:
```
2026-05-30 09:43  ALARMA Temp +4,3°C  → corrección manual 9:55
2026-05-30 10:15  ALARMA resuelta, temp 58,2°C
```

*„Rustam, **ahora la ficha KS-001**. Toda alarma tiene que quedar documentada, independientemente de si hubo o no consecuencias para la madera. Es un requisito ISO 9001 y de BTM para la garantía de la cámara."*

### 10:40, entrada en la KS-001

Pan Henryk saca del cajón del escritorio la ficha de secadero de la carga actual (KS-001 de la carga de roble ZLE-075 inicio 17.05, que rellenó al arrancar el ciclo). Añade en la sección 3 (Notas y observaciones):

```
2026-05-30 09:43-10:24 ALARMA de temperatura +4,3°C
Causa (según BTM, tel. M.Kowalski): termostato GH-67
  del intercambiador de calor, bucle de realimentación con
  humedad atmosférica alta.
Corrección: bajada manual de válvula de gas de 72% a 45%,
  resistencias de 68/64% a 40/40%. Temperatura volvió a 58°C
  en 32 minutos (bajada media 10°C/h, por encima del límite 6°C/h
  durante 10 min, aceptable para roble día 14).
Estado de la madera: humedad sin cambios, dispersión sondas 1,6%.
Plan: control manual hasta lun 02.06, servicio BTM.
Presentes: Pan Henryk (maestro), Rustam Nazarov (M3 formación).
Firma: H. Nowak, 10:45.
```

*„Rustam, **no estuviste aquí a las 9:55**. En el documento escribo 'presentes Rustam Nazarov', porque estuviste, y eso es un hecho para la auditoría. Si alguna vez alguien te pregunta '¿estuviste en la alarma de la cámara del 30 de mayo?', dirás 'sí, estaba aprendiendo', no te avergonzarás."*

Rustam anota en la libreta: *„La alarma ocurrió. La hemos documentado. Sin ocultarla. **Los documentos son protección, no problema**."*

### 10:50, conversación sobre el límite de competencias

Pan Henryk le sirve más café a Rustam del termo (azúcar en bolsita aparte), están sentados uno al lado del otro frente al panel, la temperatura se estabiliza en 58,2°C.

*„Rustam, me gustaría que entendieras hoy una cosa. La alarma ha saltado, la he resuelto yo, pero **¿si yo no hubiera estado aquí?** ¿Qué harías tú como operador M3?"*

Rustam piensa: *„Lo avisaría a Marek por teléfono. Marek está en la nave de sierras, llegaría aquí en 2-3 minutos."*

*„Bien. ¿Y si Marek no contesta porque está en la ducha después de quitarse el polvo de serrín?"*

*„Llamaría al número de servicio de BTM. Que encontraré en la carpeta del armario de control del secadero."*

*„Bien. ¿Y si BTM no contesta porque es fin de semana? ¿Qué haces?"*

Rustam piensa. *„A diferencia de la sierra, yo no puedo apagar la cámara solo, porque entonces la madera se enfriaría demasiado rápido o se recalentaría. Si no puedo llamar al maestro ni a BTM, entonces... **observo y apunto**, hasta que uno de los dos se recupere. Salvo que vea humo o oiga un crujido."*

*„Exacto. **El último recurso** no es apagar la cámara por el operador M3, porque cualquier intento de intervención manual sin permisos puede empeorar la situación. El recurso es **observar, documentar, escalar**. Igual que en la sierra es **STOP, asegura, avisa, documenta**. Aquí es **OBSERVA, REGISTRA, REPORTA, ESCALA**. Los tres primeros pasos son los mismos, el cuarto distinto, porque la cámara no se puede 'asegurar' en un minuto como una máquina."*

Rustam apunta en la libreta: *„Cámara, procedimiento de alarma operador M3: **OBSERVA, REGISTRA, REPORTA, ESCALA**. No se puede intervenir manualmente."*

### 11:00, normalización de la cámara y plan de fin de semana

A las 11:00 la cámara está completamente estabilizada: temperatura 58,1°C, RH 46%, humedad media de la madera 24,7%, EMC 8,5%. Pan Henryk hace la lectura, Rustam apunta en paralelo.

Pan Henryk: *„Hasta el lunes control manual. Yo hoy me quedo hasta las 16:00. Maciek ha vuelto a las sierras, le diré cuando regrese que el fin de semana observará la cámara **cada 4 horas** en vez de cada 8. Sábado 8:00, 12:00, 16:00, 20:00. Domingo igual. Si pasa algo, llama a mí, no a ti, no a Marek."*

*„¿Mañana (sábado) libras, verdad?"*

Rustam: *„Sí, el domingo también libre."*

*„Bien. El lunes vienes normal a la sierra, BTM cambiará el termostato, quizá te venga bien ver cómo trabaja el servicio, pero no es tu función. El martes 02.06 carga de Drew-Sus, recuerda, pino 2,42 m³, tú, Wahan y Anton de la cuadrilla de patio. Desde el martes por la tarde la cámara está vacía hasta el 08.06 cuando recogemos el roble."*

Rustam confirma, cierra la libreta. *„Gracias, Pan Henryk."*

*„Te has defendido. **Aviso en lugar de intervención, observación en lugar de pánico**. Ese es el estándar del maestro que tú, como operador M3, ya conoces y aplicas. Dentro de medio año, si haces el curso auxiliar de secadero, podrás resolver alarmas como esta tú solo. Hoy has aprendido mirando."*

## Objetivos

Después de esta lección:

1. Conoces los **tres niveles de señales del controlador BH-50**: 1) **INFO** (anotación en el histórico, sin reacción requerida, p. ej. desviación breve de RPM del ventilador); 2) **ADVERTENCIA** (el controlador se corrige solo, el operador observa, p. ej. corriente del ventilador por encima del 10% del nominal); 3) **ALARMA** (el controlador no corrige, requiere reacción humana, p. ej. desviación de temperatura +4°C o más). Entiendes que ALARMA enciende el LED rojo en el panel y la señal acústica (tres pitidos con pausas de 2 s), y que **el operador M3 ante una ALARMA avisa al maestro del secadero de inmediato**, no intenta resolver por su cuenta.
2. Conoces el **procedimiento de cuatro pasos del operador M3 ante alarma de cámara**: **OBSERVA** (lectura de todos los sensores, sin tocar el panel), **REGISTRA** (fecha, hora, valores actuales vs objetivo, tipo de alarma), **REPORTA** (teléfono o contacto personal con el maestro del secadero), **ESCALA** (si el maestro no está disponible, encargado, después servicio BTM). Entiendes que es un procedimiento **distinto del de la sierra** (donde es STOP-asegura-avisa-documenta), porque la cámara no se puede „asegurar" en un minuto, el apagado rápido genera choque térmico para la madera y cuesta más que una observación tranquila.
3. Entiendes los **tipos típicos de alarma de cámara** (temperatura, flujo de aire, humedad, sensor, estado de gas) y sus distintas prioridades. Alarma de temperatura +4°C en fase principal de ciclo de roble día 14 es una **alarma menor** (madera parcialmente seca, menos sensible), alarma de temperatura +6°C en día 3 de calentamiento es una **alarma grave** (madera al inicio, sensible al choque). Entiendes que el operador M3 no clasifica la prioridad de la alarma (eso lo hace el maestro), sólo reporta todas las alarmas por igual.
4. Conoces la **regla de velocidad máxima de cambio de temperatura 6°C/h** en cámaras de secado para especies duras (roble, haya, fresno). Superarla durante periodos superiores a 10-15 minutos provoca **rajas internas** (*internal checker*) en las tablas, invisibles desde fuera, que se manifiestan tras el mecanizado en casa del cliente. Para especies blandas (pino, abeto) la regla es menos estricta (se admite 8-10°C/h), pero el maestro de EGIDA mantiene 6°C/h para todas las especies como estándar de seguridad.
5. Conoces la **interpretación de la dispersión de sondas** en el panel BH-50. Dispersión de temperatura entre los cuatro sensores de las esquinas de la cámara: **<1,5°C** (OK, homogeneidad normal), **1,5-2,5°C** (observación, puede indicar flujo desigual), **>2,5°C** (problema de flujo, el maestro diagnostica). Dispersión de sondas de humedad de la madera: **<2%** (OK, carga homogénea), **2-3%** (observación, ciertas tablas secan más lento), **>3%** (problema, carga heterogénea o sonda dañada). Entiendes que **una sonda desviada** señala problema de sensor, **todas las sondas desviadas a la vez** señala problema de toda la cámara.
6. Entiendes el **límite de competencias del operador M3 en el control de la cámara**. El operador M3: **no tiene contraseña de acceso** al modo manual de resistencias, válvulas, programas. El operador M3 **no resetea la alarma** por su cuenta, ni siquiera cuando parece que la alarma era falsa. El operador M3 **no abre la puerta de la cámara** durante el ciclo (choque térmico para la madera, pérdida de una hora de ciclo). El operador M3 **no cambia los valores de consigna del programa** (temperatura objetivo, RH objetivo, grosor de tabla). El maestro del secadero (Pan Henryk): tiene contraseña, introduce correcciones manuales, desactiva el modo AUTO durante 30 minutos o más, documenta en KS-001.
7. Conoces la **forma de documentar una alarma en la ficha KS-001** sección 3 (Notas y observaciones). Campos obligatorios: **fecha y hora de inicio de la alarma**, **valor medido vs objetivo** (p. ej. „62,3°C vs 58°C, desviación +4,3"), **causa probable** (p. ej. „termostato GH-67 bucle de realimentación, confirmado BTM por teléfono"), **acciones tomadas** (p. ej. „corrección manual de válvula de gas de 72% a 45%"), **resultado** (p. ej. „temperatura volvió a 58°C en 32 minutos, bajada media 10°C/h"), **estado de la madera tras la alarma** (p. ej. „humedad sin cambios, dispersión sondas 1,6%"), **plan hasta la normalización** (p. ej. „control manual hasta lun 02.06, servicio BTM"), **personas presentes** (maestro, operador M3 en formación), **firma y hora de cierre**.
8. Conoces el **papel de Maciek Wiśniewski** (ayudante del secadero M1) en la monitorización de la cámara. Maciek **a diario** lee el panel y apunta en el diario (al menos 2 veces al día en días laborables más 4 veces los fines de semana en estándar, 6-8 veces los fines de semana tras una alarma). Maciek **avisa a Pan Henryk** en cualquier desviación que salga de la rutina. Maciek **no tiene contraseña** de control manual, igual que el operador M3. Entiendes que **Maciek y el operador M3 tienen un alcance de competencias similar** respecto a la cámara (observan, registran, avisan, no intervienen), pero Maciek tiene más pericia visual (ve la cámara cada día, el operador M3 una vez a la semana).

## Contenido

### 1. Cómo lee el operador M3 el panel de control BH-50

El panel de control de la cámara BH-50 es **accesible visualmente para cualquier trabajador** de la nave del secadero, incluido el operador M3 presente allí esporádicamente (p. ej. durante la reunión de planificación de l3 o una presencia formativa). Son visibles: temperatura, humedad del aire, humedad de la madera en tres sondas, EMC, estado de ventiladores, estado de resistencias, número de programa, día del ciclo, fase del ciclo, histórico de alarmas.

**No visible sin contraseña** (acceso del maestro del secadero y servicio BTM): control manual de resistencias, apertura manual de válvula de gas, ajuste manual de RH mediante inyección de vapor, log completo de alarmas de los últimos 2 años, parámetros de calibración de sensores.

**El operador M3 observa, no cambia.** Entender el panel es pedagógicamente importante, porque el operador M3 aprende a ver la **dinámica del ciclo de secado**: cómo la humedad de la madera baja gradualmente (0,3-0,6% al día en fase principal), cómo la temperatura oscila en un rango estrecho de ±2°C alrededor del objetivo, cómo los ventiladores mantienen un flujo constante de 1400-1500 RPM, cómo las resistencias bajan del 60% en calentamiento al 40% en fase principal al 30% en acondicionamiento. Viendo esto, el operador M3 **capta el ritmo normal del ciclo**, y cuando algo se desvía del ritmo, lo ve más rápido que alguien sin experiencia.

**Tres valores típicos en el panel para ciclo de roble día 14 de 22** (hoy, 2026-05-30):

1. **Temperatura**: objetivo 58-60°C (fase principal), tolerancia ±3°C. Si está fuera de tolerancia 2-3°C, observación. Si +4°C o más, alarma.
2. **Humedad relativa (RH)**: objetivo 45-50% (fase principal), tolerancia ±5%. Si está fuera de tolerancia 2-5%, observación. Si +8% o más, alarma.
3. **Humedad de la madera**: objetivo dinámico (baja 0,3-0,6%/día en fase principal). Si el ritmo es 0, el controlador busca la causa (resistencias, ventilación). Si el ritmo es 1%+/día, puede indicar secado demasiado rápido (riesgo de grietas), observación.

### 2. Cómo funciona el controlador BH-50 en el ciclo de roble

El controlador **Brunner-Hildebrand Omega 7** (modelo usado en BH-50 desde 2011) es un controlador PLC industrial (*Programmable Logic Controller*) con software específico para cámaras de secado. Tiene memoria para **20 programas de fábrica** (pino, abeto, roble, haya, abedul, arce y otros) más **10 programas de usuario** (EGIDA tiene ahora 4: SOS-STAND-28 pino, DUB-STAND-28 roble, BUK-STAND-25 haya, BRZ-STAND-25 abedul).

**El ciclo de programa** es un conjunto de **unos 150 parámetros** que describen cómo debe comportarse la cámara durante 9-25 días del ciclo: **cada hora** del ciclo el controlador tiene asignado **temperatura objetivo, RH objetivo, velocidad de cambio de temperatura, velocidad de cambio de RH**. El programa automáticamente **calcula a partir de la humedad actual de la madera** en qué fase está (calentamiento, secado previo, secado principal, acondicionamiento, enfriamiento), y ajusta los parámetros. El cambio de fase es automático (p. ej. el controlador detecta por sí mismo que la humedad de la madera ha llegado al 16% y pasa el ciclo del secado principal al acondicionamiento).

**En fase principal de roble día 14**:
- Objetivo de temperatura: 58-60°C (sube gradualmente de 52°C el día 10 a 62°C el día 15, después baja)
- Objetivo de RH: 45-50% (baja del 60% al inicio de la fase principal al 40% al final)
- Velocidad de bajada de RH: unos 0,8% al día
- Velocidad de bajada de humedad de la madera: 0,5-0,6% al día

**Regulación proporcional PID** (*Proportional-Integral-Derivative*, estándar de controladores industriales): el controlador **no enciende las resistencias al 100% cuando hace demasiado frío, no las apaga al 0% cuando hace demasiado calor**. Cálculos continuos: a qué distancia estamos del objetivo (P), cuánto tiempo dura la desviación (I), a qué velocidad crece la desviación (D). Las resistencias se activan **en porcentaje** (p. ej. 45% de potencia) para una regulación suave.

**Por eso la alarma 62°C en vez de 58°C no fue resultado de „alguien ha puesto las resistencias al 100%"**, sino de **un atasco del bucle de realimentación en el termostato**: el controlador creía que aún hacía falta calentar, porque recibía una señal falsa del termostato GH-67 del intercambiador de calor (que la temperatura de entrada era más baja de lo que realmente era).

### 3. Reconocimiento de tipos de alarma de cámara

**Alarma de temperatura** (la más frecuente):
- Objetivo +3°C tolerancia, **+4°C = alarma**
- Objetivo -3°C tolerancia, **-4°C = alarma** (cámara demasiado fría, también problema, pero más raro)
- Causas típicas: termostato dañado (ver hoy), válvula de gas atascada, intercambiador de calor sucio, sensor de temperatura dañado (entonces una sonda se desvía), puerta de cámara mal cerrada (las cuatro sondas más bajas)

**Alarma de humedad relativa (RH)**:
- Objetivo ±5% tolerancia, **±8% = alarma**
- RH demasiado alta en fase principal: problema con la extracción, la madera no seca, riesgo de moho dentro
- RH demasiado baja en fase inicial: riesgo de grietas superficiales (*end checks*) en los cantos de las tablas

**Alarma de flujo de aire (ventiladores)**:
- Uno de los dos ventiladores **por debajo del 80% de RPM** = alarma
- Ambos ventiladores por debajo del 80% = alarma crítica, la cámara amenaza con apagado inmediato
- Causas típicas: filtro atascado, motor de ventilador dañado, cortocircuito

**Alarma de humedad de la madera (sondas)**:
- Dispersión entre sondas **>3%** = alarma (carga heterogénea o sonda dañada)
- Velocidad de bajada **0% durante 48h** = alarma de estancamiento (la madera no cede agua, problema de condiciones)
- Velocidad de bajada **>1,5% al día** = alarma de secado rápido (riesgo de grietas)

**Alarma de gas principal**:
- Presión externa en el depósito de gas **por debajo del 25% del lleno** = alarma, la cámara conmuta automáticamente al segundo depósito
- Por debajo del 10% = alarma crítica, la cámara apaga automáticamente el calentamiento, el controlador entra en modo „enfriamiento de emergencia"

**Alarma de sensor**:
- Sensor de temperatura o humedad muestra valores **extremos (físicamente imposibles)** = alarma, el controlador aísla el sensor, usa los demás (redundancia 4 sondas de temperatura = 3 bastan para continuar el ciclo).

### 4. Velocidad máxima de cambio de temperatura y enfriamiento

La regla de **6°C por hora** para cámaras de secado convencionales aplicadas a especies duras (roble, haya, fresno, arce) procede de la física de la madera. La **contracción del roble** al cambiar la humedad es de **0,25% por cada 1% de cambio de humedad** (longitudinal-radial). Ante choque térmico (cambio brusco de temperatura) la superficie de la tabla pierde agua más rápido que el núcleo, surge un **gradiente de humedad** (5-10% de diferencia), que a su vez da gradiente dimensional y **tensiones internas**.

Las tensiones que superan la **resistencia del roble a la tracción en dirección tangencial** (unos 5-6 MPa) provocan **rajas internas**, invisibles desde fuera, que se manifiestan durante el mecanizado.

**El ritmo de 6°C/h** está configurado en el programa DUB-STAND-28 para el día 14 como límite: el controlador **por sí mismo no cambiará la temperatura más rápido**, aunque el programa fije un nuevo valor. Si el **control manual del maestro** genera un cambio más rápido (como hoy, 10,5°C/h durante 10 minutos), es una **decisión consciente del maestro** basada en evaluación de riesgo (p. ej. día 14 madera ya menos sensible).

**Para pino (DUB-STAND-28 vs SOS-STAND-28)** la regla es menos estricta: **8-10°C/h** porque el pino tiene una estructura más homogénea y menor contracción. Pero EGIDA mantiene **6°C/h** para todas las especies como estándar de seguridad (Pan Henryk se lo explicó a los operadores en 2014, desde entonces es regla en la documentación de procedimientos).

**Para el enfriamiento al final del ciclo** (fase 5, 1-2 días) la regla es aún más estricta: **4°C/h como máximo**, porque la madera secada al 14% es ya sensible al choque, y el final del ciclo debe „cerrar" todas las microtensiones, no generar nuevas.

### 5. Profilaxis de grietas y alabeo mediante monitorización

El operador M3 que observa el ciclo **no puede evitar las grietas durante el ciclo** (eso lo hacen el maestro del secadero y el servicio BTM mediante un programa correcto), pero **puede detectar pronto el riesgo** y avisar:

**Signos de riesgo de grietas superficiales (*end checks*)**:
- La dispersión de sondas de humedad **sube por encima del 2%** en fase 1-3 de día (la superficie de la madera seca más rápido que el núcleo)
- Temperatura **por encima del objetivo** en fase de calentamiento (más de +2°C durante una hora)
- RH **por debajo del objetivo** en fase inicial (más de -5% durante 4 horas)

**Signos de riesgo de rajas internas (*internal checks*)**:
- Velocidad de bajada de humedad de la madera **supera el 1%/día** en fase principal
- Temperatura **con picos por encima de 3°C en una hora**
- Acondicionamiento **acortado u omitido** (decisión del maestro, rara en EGIDA)

**Signos de riesgo de alabeo (*warping*)**:
- Una sonda de humedad **se desvía claramente hacia arriba** (una sección de la carga seca más lento)
- Apilado desigual de las pilas (se ve por la ventana de observación, se ve que algunas tablas ya se están deformando)
- RH **demasiado baja** en fase de acondicionamiento (el gradiente no se iguala)

El operador M3 en presencia formativa en el secadero aprende a **reconocer estos signos y avisar**. Hoy Rustam no ha visto ninguno de ellos salvo la propia alarma de temperatura, que Pan Henryk ha resuelto manualmente. Pero dentro de 6 meses, tras el curso auxiliar de secadero, Rustam podrá interpretar estas señales por sí mismo y decidir sobre la corrección.

### 6. Papel de Maciek y monitorización de fin de semana

**Maciek Wiśniewski** (ayudante del secadero M1, 19 años) tiene un alcance de competencias **más amplio que el operador M3 en cámaras**, pero **más estrecho que el maestro**. Puede:
- Leer el panel y apuntar en el diario (por su cuenta)
- Cambiar el papel de la impresora del diario
- Reponer aceite lubricante en los motores de los ventiladores (rutina de servicio cada 6 meses, de la lista de BTM)
- Barrer la sala de control del secadero, limpiar las ventanas de observación de la cámara

No puede:
- Abrir la puerta de la cámara durante el ciclo (sólo el maestro, sólo por motivos excepcionales)
- Introducir una corrección manual en el controlador (contraseña del maestro)
- Decidir sobre la carga o el programa (eso lo hace el maestro)
- Borrar una alarma o una entrada del diario de alarmas

**En rutina de fin de semana (sin alarma)**:
- Sábado 10:00 y 16:00, domingo 10:00 y 16:00 (4 lecturas en el fin de semana)
- El diario es un cuaderno A4 sobre la mesa, en una línea: fecha, hora, temperatura, RH, humedad de la madera (media), EMC, firma
- Si la desviación de temperatura o humedad **sale de tolerancia** (>±3°C o >±5% RH), Maciek llama a Pan Henryk **de inmediato**, no espera a la siguiente lectura
- Si hay alarma del controlador (LED rojo), Maciek llama **de inmediato** y se queda junto al panel hasta la llegada del maestro

**Tras la alarma de hoy**, la rutina se densifica a **cada 4 horas** (sábado 8:00, 12:00, 16:00, 20:00, domingo análogo). Maciek recibe un plus de remuneración (tarifa de fin de semana 150% en vez de 100%) por la presencia intensificada.

### 7. Documentación de la alarma en la ficha KS-001

**La ficha KS-001 de carga actual** (la que Pan Henryk rellenó al iniciar el ciclo de roble el 17.05) tiene **4 secciones**:
1. Carga planificada (apuntada el 17.05, descripción del lote 2,5 m³ de roble)
2. Carga siguiente planificada (apuntada el 29.05 en l3, descripción del pino previsto para Drew-Sus)
3. **Notas y observaciones** (se rellena durante el ciclo, cada suceso relevante)
4. Firmas (17.05 inicio, después al cierre del ciclo)

**La alarma de hoy** entra en la sección 3. Pan Henryk escribe:
- Fecha y hora de inicio de la alarma (2026-05-30 09:43)
- Fecha y hora de resolución de la alarma (2026-05-30 10:15)
- Valor medido vs objetivo del programa (62,3°C vs 58°C)
- Desviación (+4,3°C, umbral de alarma +4°C)
- Causa probable (termostato GH-67 del intercambiador de calor, bucle de realimentación, confirmado por BTM)
- Acciones tomadas (corrección manual válvula de gas 72→45%, resistencias 68/64→40/40%)
- Resultado (temperatura volvió a 58°C en 32 minutos, bajada media 10°C/h, por encima del límite 6°C/h durante 10 min, aceptable para roble día 14)
- Estado de la madera tras la alarma (humedad sin cambios, dispersión sondas 1,6% sin cambios)
- Plan (control manual hasta lun 02.06, servicio BTM, termostato a cambiar)
- Presentes (Pan Henryk maestro, Rustam Nazarov M3 formación)
- Firma y hora de cierre (H. Nowak, 10:45)

**La ficha KS-001 de la carga actual permanece en el cajón del secadero hasta el cierre del ciclo** (descarga 08.06). Entonces la carga se „cierra", la ficha la firman maestro y encargado, se escanea a OneDrive EGIDA, el papel al archivo (retención 3 años papel + 5 años escaneo).

**El auditor ISO 9001** puede en cualquier momento ver la ficha y decir: „enséñenme la KS-001 de la carga de roble de mayo de 2026". La ficha debe estar disponible en 15 minutos (ISO 9001 sección 7.5 „información documentada"). Por eso la sección 3 se rellena **al momento, no después del ciclo**.

### 8. EMC en la práctica de la monitorización del roble

**EMC (humedad de equilibrio)** es un **valor de gobierno en tiempo real**. En el panel BH-50 aparece como „EMC: 8,4%" (hoy). Significa: **si la madera permanece en el entorno actual (58°C temperatura, 47% RH) el tiempo suficiente, alcanzará la humedad 8,4%**.

**La humedad real de la madera es 24,7% (media de 3 sondas)**. Por tanto la **diferencia** es 24,7 - 8,4 = **16,3%**. La madera tiende a bajar, porque está „más mojada" de lo que el entorno permite.

**La velocidad de bajada** depende de:
- La diferencia „actual - EMC" (cuanto mayor, más rápida la cesión de agua)
- La permeabilidad de la madera (el roble es menos permeable que el pino, cede más lento)
- El grosor de la tabla (una tabla más gruesa cede más lento, porque el agua tiene que „abrirse camino" hasta la superficie)

**Para roble 28 mm**: velocidad 0,5% al día en fase principal es normal con diferencia 16%. Si la diferencia fuera 20% (p. ej. al bajar la RH al 35%), la velocidad podría subir a 0,8-1% al día, **el riesgo de grietas aumentaría**.

**Por eso el controlador no baja la RH a valores extremadamente bajos** en fase principal. Objetivo 45-50% RH + temperatura 58-60°C da EMC 8-9%. La madera seca gradualmente, la diferencia „actual - EMC" es moderada (unos 16%), el ritmo tranquilo (0,5%/día), las grietas se evitan.

**El operador M3 entiende este mecanismo intuitivamente**. Ve EMC 8,4, humedad de la madera 24,7, diferencia 16%, ritmo 0,5/día. **Esto es normal**. Si viera EMC 5%, diferencia 20%, ritmo 1%/día, pensaría: „el controlador está bajando la RH demasiado, demasiado fuerte". Avisaría al maestro.

### 9. Errores típicos de monitorización del principiante

**Error 1. Ignorar una desviación pequeña**. El operador principiante ve temperatura 61°C en vez de 58°C, piensa „son sólo 3°C, está en tolerancia". La tolerancia es ±3°C, 61°C está de hecho en el borde. Pero la **tendencia** sube 0,5°C en los últimos 20 minutos, en una hora serán 64°C, **entonces alarma**. **Correcto**: al ver una tendencia creciente hacia el borde, el operador **avisa antes**, no espera a la alarma.

**Error 2. Resetear la alarma „para que desaparezca"**. El operador ve el LED rojo, quiere que deje de brillar. Busca un botón „reset" en el panel, algunos modelos de controlador tienen ese botón accesible sin contraseña. **Es un error**: la alarma **aparece de nuevo al rato**, porque la causa no se ha resuelto. Peor aún, el controlador pierde el histórico de la alarma (el reset borra la entrada), la auditoría ISO tiene un agujero. **Correcto**: **no resetees la alarma**, observa, avisa al maestro, el maestro diagnostica y sólo entonces resetea tras la resolución.

**Error 3. Abrir la puerta de la cámara „para ver la madera"**. El operador piensa „voy a ver qué aspecto tiene la carga, si no ha pasado algo". **Es un error grave**: la puerta abierta 10 segundos en fase principal del ciclo de roble genera **una caída de temperatura de 15-20°C en la cámara** (sale el aire caliente, entra el frío), el controlador reacciona con alarma, el ciclo puede „resbalar" 8-12 horas, la calidad de la madera puede sufrir. **Correcto**: **la puerta de la cámara se abre sólo al final del ciclo** (fase de enfriamiento terminada), por orden del maestro. Durante el ciclo toda la información es **del panel y las sondas**, no del ojo directo.

**Error 4. Confundir RH del aire con humedad de la madera**. El panel muestra „humedad 47%" (RH del aire) y „humedad de la madera 24,7%" (dos parámetros distintos). El operador principiante piensa: „la madera tiene 47%, mucho, aún queda mucho por secar". Pero 47% no es la madera, es el aire. La madera tiene 24,7%, hasta el objetivo 14% quedan 10,7%. **Correcto**: distinguir en el panel **RH del aire** (porcentaje de humedad del aire en la cámara) de **humedad de la madera** (porcentaje de agua en la madera). Son dos parámetros independientes, el controlador regula la RH, la madera se ajusta por sí misma.

**Error 5. Interpretar la dispersión de sondas como „todo en orden"**. Tres sondas muestran 22%, 24%, 28%. Media 24,7%. El operador piensa: „media buena". Pero una dispersión del 6% (28-22) es **grave**: una tabla (sonda 3) seca más lento que las demás. Puede ser sonda dañada, puede ser tabla con defecto interno, puede ser apilado irregular. **Correcto**: mirar la **dispersión, no la media**. Dispersión >3% es señal para avisar al maestro.

**Error 6. „Lo arreglo yo, no voy a molestar a Pan Henryk"**. El operador ve la alarma, piensa: „Pan Henryk está cansado, lo intentaré yo". **Error absoluto**: el operador M3 no tiene contraseña, no tiene pericia, su intervención **empeorará la situación**. Pan Henryk tiene número de teléfono, tiene permisos, tiene pericia. **Correcto**: **siempre llama al maestro ante una alarma**, aunque la alarma parezca pequeña. Pan Henryk preferiría despertarse a las 23:30 un domingo por una alarma falsa que por la mañana ver la cámara con madera rajada tras „arreglo por cuenta propia" de un operador sin permisos.

### 10. Curso auxiliar de secadero, siguiente paso de Rustam

El módulo formativo de secadero auxiliar (descrito en l3 punto 11) es una extensión opcional de M3. Requiere **consentimiento del maestro del secadero** (hoy Pan Henryk) y **M3 completado** (para Rustam previsto en octubre 2026). Alcance: 5 días de formación intensiva + examen.

**La presencia de hoy de Rustam** (2026-05-30, 2 horas) **cuenta** como **práctica previa** de cara al curso. Pan Henryk al final del día apuntará en el expediente personal de Rustam:

```
2026-05-30, 9:30-11:00
R. Nazarov, operador M3, presencia formativa en secadero.
Observación del ciclo de roble (día 14), alarma de temperatura,
diagnóstico y corrección manual del maestro.
Rustam comprendió: límite de competencias, procedimiento de alarma
(OBSERVA, REGISTRA, REPORTA, ESCALA), documentación
en KS-001.
Evaluación: apto para sucesivas presencias formativas.
Siguiente presencia prevista: descarga de roble 2026-06-08,
como asistencia en mediciones finales y empaquetado.
Firma: H. Nowak, maestro de secadero.
```

El expediente personal de Rustam está en la oficina del jefe del aserradero, en la carpeta „Formación interna". Su contenido influye en la **cualificación de Rustam** para el curso auxiliar de secadero en octubre 2026 (mínimo 3 presencias formativas como condición de admisión).

### 11. Qué ocurre después en el ciclo de roble tras la alarma

**Hoy (viernes 30.05)**: control manual desde las 10:25, estabilización a 58°C, monitorización continua por Pan Henryk hasta las 16:00. Estado de la madera: humedad 24,7% (sin cambios tras la alarma, madera resistente a una desviación tan breve), dispersión de sondas 1,6% (sin cambios).

**Sábado (31.05) y domingo (01.06)**: Maciek monitorización cada 4 horas. Pan Henryk el sábado por la mañana (8:00-10:00) vendrá a revisar personalmente (el encargado Marek aceptó pagar horas extra del sábado). La temperatura debería mantenerse en 58-60°C, la humedad de la madera bajar 0,5-0,6% al día.

**Lunes (02.06)**: BTM vendrá por la mañana (9:00) a cambiar el termostato GH-67 del intercambiador de calor. La cámara en ese tiempo **sigue funcionando** (no paran el ciclo por una hora de cambio), BTM hace la sustitución „en caliente" (apaga sólo ese componente, el controlador compensa manualmente durante el cambio).

**Martes (03.06) – sábado (07.06)**: el ciclo termina con la fase de acondicionamiento (el domingo 31.05 empieza el acondicionamiento según el programa, aunque la alarma de hoy no afecta al calendario de la fase). La temperatura baja gradualmente de 60°C a 55°C, la RH sube del 45% al 75% (acondicionamiento). La humedad de la madera baja del 24% al 14%.

**Domingo (07.06)**: fase de enfriamiento, temperatura 55°C → 25°C (bajada lenta 4°C/h máx), RH 75% estable. Humedad de la madera 14% de destino.

**Lunes (08.06)**: fin del ciclo de 22 días. **Apertura de la cámara, descarga** (ese es l5 M3 T3, la siguiente lección de Rustam).

## Escena de cierre, 11:00, salida de Rustam

Pan Henryk se queda en la sala de control (diario por cerrar, teléfono al siguiente operador de BTM confirmando la visita del lunes), Rustam sale con la libreta llena de nuevas anotaciones. Por la ventana de la sala de control ve a Maciek volviendo de la nave de sierras con el diario de fin de semana en la mano, Maciek mira con ojos interrogantes. Rustam le resume breve: *„Ha habido alarma, temperatura +4, Pan Henryk la ha arreglado. Control manual hasta el lunes, tú cada 4 horas el fin de semana."*

Maciek asiente, entra en la sala de control a hablar con Pan Henryk del horario del fin de semana.

### 11:05, paso a la nave de sierras

Rustam cruza el patio de almacén hacia la nave de sierras. Hoy es viernes, turno de producción normal. Su turno en P3 empieza a las 12:00, hasta las 12:00 tiene 50 minutos libres. Va a la taquilla del trabajador, saca un bocadillo de la bolsa, se sienta en el banco frente a la nave, abre la libreta y **pasa a limpio** lo que ha visto esta mañana.

**Cinco conclusiones**:

1. **La cámara de secado no es una máquina „de encender y apagar"**. El ciclo dura 22 días, el operador lo observa, el maestro lo dirige, en esos 22 días puede pasar de todo (alarmas, correcciones, servicio). El operador M3 participa en esa complejidad **sin decisiones**, aprende a ver el ritmo.

2. **Una alarma +4°C es „pequeña" para roble día 14**. La misma +4°C en día 3 de calentamiento sería más grave. Pan Henryk lo ha visto al instante („no hay prisa, alarma pequeña buen entrenamiento"). El operador M3 no evalúa la prioridad de la alarma, **reporta todas las alarmas por igual**.

3. **El termostato GH-67** es un componente que Rustam antes no conocía. Hoy ha aprendido que el controlador de la cámara tiene muchos componentes, **cada uno puede averiarse independientemente**, y que el servicio BTM tiene conocimiento sobre averías típicas que el operador M3 no tiene y no necesita tener.

4. **El procedimiento OBSERVA, REGISTRA, REPORTA, ESCALA** es **distinto del procedimiento de la sierra** (STOP, asegura, avisa, documenta). La cámara no tiene „STOP" inmediato. El operador debe entender esa diferencia, porque la intuición de la sierra le dice „para la máquina", pero en la cámara **parar el ciclo** genera más problemas de los que resuelve.

5. **Documentación = protección**. Pan Henryk apunta en la KS-001 incluso alarmas „pequeñas", incluso „presencia formativa de Rustam". En la auditoría ISO 9001 se ve que la cámara está monitorizada, las alarmas están resueltas, el personal está formado. Sin esas entradas no se puede demostrar nada. **Los papeles son protección, no estorbo**.

Rustam cierra la libreta, la deja en el banco, bebe el resto del té del termo. A las 11:35 entra en la nave de sierras, empieza a preparar P3 para el turno (limpieza de la bancada de la máquina del serrín de Damian del turno de la mañana).

### 11:55, disposición del día

Marek trae la disposición del día en P3 de 12:00 a 15:00. Es **ZLE-2026-05-082**, cliente Stolarz Meblowy Mrągowo (de l3), haya común 25 × 130 × 4000 mm. Otra especie, otro surtido, otra clase (C24 de mueble, pero con condición estética). Rustam rellenará una nueva KDP-001.

Pero eso es la siguiente lección, no hoy. Hoy Rustam cierra las notas del secadero y arranca la producción de haya a las 12:00. Wahan se incorporará a las 12:15 tras acabar el mantenimiento con Juri.

## Términos clave

**Alarma de secadero** (*alarm komory suszarniczej*, EN *kiln alarm*, ES *alarma de secadero*, UK *тривога сушильної камери*): señal del controlador que indica que un parámetro ha superado el umbral de tolerancia fuera de rango, requiere reacción humana (del maestro del secadero), se señaliza con LED rojo y señal acústica, se documenta en la ficha KS-001.

**Controlador Brunner-Hildebrand Omega 7** (*sterownik Omega 7*, EN *Omega 7 controller*, ES *controlador Omega 7*, UK *контролер Omega 7*): controlador PLC industrial usado en la cámara BH-50, contiene 20 programas de fábrica más 10 programas de usuario, regulación proporcional PID, memoria de histórico de alarmas de 24 meses.

**Regulación proporcional PID** (*regulacja PID*, EN *PID control*, ES *control PID*, UK *ПІД-регулювання*): algoritmo de control que calcula la salida a partir de la desviación proporcional (P), integral (I) y derivativa (D), usado en el controlador de la cámara para regulación suave de resistencias, válvula de gas, ventiladores sin saltos.

**Termostato del intercambiador de calor GH-67** (*termostat GH-67*, EN *GH-67 heat exchanger thermostat*, ES *termostato GH-67*, UK *термостат GH-67*): componente de la instalación de gas de la cámara BH-50 Brunner-Hildebrand, regula la temperatura de entrada del intercambiador de calor hacia la cámara, problema conocido de bucle de realimentación con humedad ambiente alta, se sustituye de serie durante la revisión anual de BTM.

**Procedimiento OBSERVA-REGISTRA-REPORTA-ESCALA** (*procedura alarmu komory dla M3*, EN *kiln alarm procedure for M3*, ES *procedimiento de alarma del secadero para M3*, UK *процедура тривоги сушарні для М3*): procedimiento de cuatro pasos de reacción del operador M3 ante alarma de cámara, distinto del de sierra (STOP-asegura-avisa-documenta), porque la cámara no se puede „asegurar" rápido.

**Velocidad máxima de cambio de temperatura 6°C/h** (*maksymalne tempo 6°C/h*, EN *max temperature change rate 6°C/h*, ES *tasa máxima de cambio de temperatura 6°C/h*, UK *максимальний темп зміни температури 6°C/год*): estándar EGIDA para todas las especies en la cámara BH-50, previene las rajas internas, puede superarse brevemente (hasta 10-15 minutos) por decisión del maestro en casos de riesgo limitado.

**Dispersión de sondas de humedad** (*rozrzut sond*, EN *moisture probe spread*, ES *dispersión de sondas de humedad*, UK *розкид зондів вологості*): diferencia entre la lectura más alta y la más baja de las tres sondas de humedad de la madera en la cámara, indicador de homogeneidad de la carga, valor <2% OK, 2-3% observación, >3% problema.

**Diario de fin de semana del secadero** (*dziennik weekendowy*, EN *weekend kiln log*, ES *diario de fin de semana del secadero*, UK *вихідний журнал сушарні*): cuaderno A4 de tapa dura, rellenado por el ayudante del secadero 2-4 veces al día en días no laborables, contiene fecha, hora, lecturas del panel y firma.

**Fase de acondicionamiento** (*faza kondycjonowania*, EN *conditioning phase*, ES *fase de acondicionamiento*, UK *фаза кондиціонування*): fase penúltima del ciclo (2-4 días para roble), elevación de la RH al 70-80% con temperatura reducida, igualación del gradiente de humedad y disolución de tensiones internas de la tabla.

**Fase de enfriamiento** (*faza chłodzenia*, EN *cooling phase*, ES *fase de enfriamiento*, UK *фаза охолодження*): fase última del ciclo (1-2 días), bajada de temperatura de 55-60°C a 25°C, velocidad máxima 4°C/h, sin modificación de la humedad del aire, prepara la madera para salir de la cámara sin choque térmico.

**Control manual** (*sterowanie ręczne*, EN *manual control mode*, ES *control manual*, UK *ручне керування*): modo del controlador BH-50 accesible sólo con contraseña del maestro del secadero, desactiva la regulación AUTO y permite ajustar directamente el porcentaje de potencia de resistencias, apertura de válvula de gas, revoluciones de ventiladores, usado durante el diagnóstico o la corrección.

**Servicio BTM Polska** (*serwis BTM*, EN *BTM Poland service*, ES *servicio BTM Polonia*, UK *сервіс BTM Польща*): distribuidor y servicio técnico polaco de cámaras Brunner-Hildebrand, tiene conocimiento de averías típicas de controladores Omega 7, realiza revisiones anuales y sustituciones de piezas, disponible en número 24/7.

**INFO-ADVERTENCIA-ALARMA** (*trzy poziomy sygnału sterownika*, EN *info-warning-alarm levels*, ES *niveles información-advertencia-alarma*, UK *рівні інформація-попередження-тривога*): jerarquía de señales del controlador BH-50, INFO es anotación sin reacción, ADVERTENCIA es auto-corrección del controlador con observación del operador, ALARMA es reacción humana requerida.

**Expediente personal de formación** (*akta osobowe szkolenia*, EN *personnel training record*, ES *expediente de formación*, UK *особова справа навчання*): carpeta en la oficina del jefe de EGIDA que contiene entradas sobre presencias formativas del operador, constituye la base de la decisión de admisión a cursos ampliados (p. ej. el curso auxiliar de secadero exige un mínimo de 3 presencias).

## Autoevaluación

### A. Alarmas y su reconocimiento

1. ¿Cuáles son los **tres niveles de señales** del controlador BH-50, y cuál de ellos requiere reacción humana?

2. El controlador muestra „ALARMA: Temperatura del aire 62,3°C, objetivo 58°C, desviación +4,3°C". El operador M3 está solo ante el panel (el maestro en otro punto). ¿Qué hace primero, segundo, tercero?

3. ¿Cuál es el **procedimiento de cuatro pasos** del operador M3 ante alarma de cámara? Escríbelos en orden.

### B. Límite de competencias en la cámara

4. El operador M3 ve una alarma de temperatura. Le tientan dos botones del panel: „Reset de alarma" (sin contraseña) y „Control manual de resistencias" (con contraseña). ¿Cuál pulsa? Elige y justifica:
a) Reset de alarma, porque parece sencillo
b) Control manual de resistencias, porque apagar las resistencias ayudará
c) Ninguno, porque el operador M3 no resetea ni cambia parámetros
d) Ambos, para demostrar sus permisos

5. El operador M3 está en la cámara durante el ciclo de roble día 14, se aburre, quiere ver cómo está la madera en la cámara. ¿Puede abrir la puerta de la cámara durante 10 segundos „sólo para echar un vistazo"? Justifica.

6. Pan Henryk está de vacaciones 2 semanas. La cámara trabaja un ciclo completo de 22 días. ¿Quién es responsable de la cámara en ese tiempo y qué significa para el operador M3?

### C. Interpretación de parámetros

7. El panel muestra: temperatura 58°C, RH 47%, humedad media de la madera 24,7%, EMC 8,4%. ¿Cuál es la diferencia entre la humedad actual de la madera y el EMC, y qué significa esa diferencia para la velocidad de secado?

8. Tres sondas de humedad de la madera muestran: 22%, 24%, 28%. Media 24,7%. El operador principiante celebra „buena media". ¿Qué ve el maestro y por qué lo reporta como problema?

9. La temperatura sube gradualmente: 58°C, luego 59°C, luego 60°C, luego 61°C (en una hora). Objetivo 58°C, tolerancia ±3°C. Aún no hay alarma, porque 61°C está en el borde 58±3. ¿El operador M3 avisa ya al maestro ahora o espera a la alarma?

### D. Velocidad máxima y profilaxis de grietas

10. La regla de **velocidad máxima de cambio de temperatura 6°C/h** para cámaras convencionales. ¿Qué provoca superarla para el roble, y cuál es el efecto visible en el cliente?

11. Tras la alarma de hoy la temperatura bajó de 62,3°C a 58,2°C en 32 minutos. Calcula la velocidad media de bajada y compárala con el límite. ¿La corrección estuvo dentro de los márgenes de seguridad para roble día 14?

12. ¿Por qué para el **pino** la regla puede ser 8-10°C/h, y para el **roble** tiene que ser 6°C/h? Indica la causa estructural de la madera.

### E. Documentación de la alarma

13. Ficha KS-001 de la carga actual de roble (inicio 17.05). Alarma el viernes 30.05. ¿En qué sección de la ficha se apunta esta alarma, y qué elementos de la entrada son **obligatorios**?

14. El auditor ISO 9001 llega en junio 2026 y dice: „enséñenme la KS-001 de la carga de roble de mayo". ¿En cuántos minutos debe estar disponible la ficha? ¿Dónde se guarda?

15. Pan Henryk apunta en la KS-001 „presentes: Rustam Nazarov (M3 formación)". ¿Por qué hace constar explícitamente la presencia de Rustam, aunque Rustam no decidiese nada?

### F. Papel de Maciek y planes

16. Maciek es ayudante del secadero M1. ¿Qué puede y qué no puede hacer con la cámara el fin de semana, cuando Pan Henryk no está?

17. Rutina normal de fin de semana: Maciek hace 4 lecturas al día (10:00 y 16:00 sábado y domingo). ¿Por qué tras la alarma Pan Henryk aumenta la rutina a cada 4 horas (8 lecturas), y no mantiene el estándar de 4?

18. Rustam hoy ha completado una presencia formativa en el secadero (2 horas). ¿Como **antesala** de qué cuenta, y cuáles son los requisitos formales para participar en ese siguiente paso?
