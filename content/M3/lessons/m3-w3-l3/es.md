---
id: m3-w3-l3
blok: procesy
czas: 120
---

## Introducción

Jueves, 2026-05-29, las 14:00. Mykoła está en la **nave del secadero** de EGIDA, un edificio independiente de 12 × 8 × 4,5 m, separado de la nave de sierras por una explanada de almacenamiento de 30 metros. El interior está caliente (28-30°C, aunque la cámara está funcionando, la nave recibe calor a través del aislamiento), el aire tiene el característico olor a roble húmedo (llevan 12 días en el ciclo), el ruido de los ventiladores de extracción es uniforme, 55-60 dB. La tarea de hoy, **reunión de planificación** sobre la próxima *wsadka* (carga del secadero) de la cámara: cuándo, qué, con qué programa, por cuánto tiempo.

En la nave hay tres personas: **Don Henryk** (62 años, *mistrz suszarni* (maestro del secadero) de EGIDA, jubilado estacional, de marzo a noviembre trabaja en EGIDA, de diciembre a febrero pasa el invierno en su casa cerca de Ełk; 38 años de experiencia en secado, de los cuales 22 en aserraderos de Masuria), **Marek Kowalski** (capataz) y **Mykoła Hrycenko** (operador autónomo M3, su presencia en esta reunión es parte planificada de su formación M3, la última parte del bloque de procesos). Wasyl no está (M1 tiene hoy turno de mantenimiento en la nave de sierras, no tiene formación de secado programada).

La planificación de la campaña de secado no es competencia del operador M3 en el sentido "decisorio". **El maestro del secadero decide**. El operador M3 **participa, aporta información, documenta**. Esta es la diferencia que Mykoła aprende hoy a vivir: **no toda decisión productiva en la que participa un operador autónomo es una decisión del operador autónomo**. En algunas áreas (secado, regulación eléctrica, cambio de programa del controlador) el operador **asiste a un especialista** en lugar de liderar.

### 14:05, estado actual de la cámara

Don Henryk abre la puerta de la **sala de control del secadero** (una habitación de 2 × 3 m con el armario de control y ventanas de observación hacia la cámara). El panel de control con pantalla LCD muestra el estado:

```
Cámara: BH-50 (Brunner-Hildebrand, 50 m³ brutos, 38 m³ netos de madera aserrada)
Carga actual: roble común 2,5 m³, tablas de 30 mm, inicio 2026-05-17
Día del ciclo: 13 de 22 (fases: calentamiento 2d, principal 14d, acondicionamiento 4d, enfriamiento 2d)
Fase actual: secado principal, día 11 de 14

Temperatura del aire:             58°C  (objetivo 60°C, tolerancia ±3)
Humedad relativa (RH):            42%   (objetivo 40%, tolerancia ±5)
Humedad de la madera sonda 1:     28,4% (inicio 38%)
Humedad de la madera sonda 2:     27,9% (inicio 37,6%)
Humedad de la madera sonda 3:     29,1% (inicio 38,5%, seca más lento)
EMC (humedad de equilibrio):      7,1%  (objetivo final del roble: 14%)

Finalización planificada: sábado 2026-06-07, salida de la madera el lunes 2026-06-09.
```

Don Henryk comenta en voz alta, medio para Marek, medio para Mykoła:

*"El roble va con normalidad. La humedad baja como debe. 28% en el día 11 está dentro del plan, llegaremos al 14% en 9 días más. El fin de semana no interfiere, la cámara trabaja sola, el controlador en automático. El sábado y el domingo vendrá Maciek a leer y anotar en el diario, como todos los fines de semana."*

Maciek es el ayudante del secadero, M1 en EGIDA, aprende bajo la tutela de Don Henryk (no Maciek Melnyk, otro Maciek, Maciej Wiśniewski, 19 años, segundo curso del instituto técnico de la madera de Ostróda, prácticas en EGIDA).

*"El lunes día 9 sacamos el roble, la pila en la zona de enfriamiento, después clasificación. El martes día 10 la cámara queda **vacía**. Desde el martes programa nuevo."*

Marek asiente. Mykoła mira el panel y anota los datos en su agenda de bolsillo (para él, no en la KDP-001, porque no es un documento de producción sino de planificación).

### 14:15, qué hay para la carga

Marek saca el cuaderno del capataz, lee la lista de madera fresca en el almacén del aserradero, a la espera de secado:

```
Estado de la madera fresca pendiente en el almacén de secado (de las fichas WZ de los clasificadores):

A. Pino silvestre, tablas 28 × 155 × 4050 mm, fresca 28-32%:
   - ZLE-2026-05-077 (Mykoła, ZLE int. ZLE-077): 0,58 m³
   - ZLE-2026-05-079 (Damian, viernes 23.05): 0,72 m³
   - Excedentes de almacén (material cortado en primavera para clasificación): 1,12 m³
   Total pino: 2,42 m³

B. Roble común, tablas 28 × 155 × 4050 mm, fresco 35-38%:
   - ZLE-2026-05-081 (Mykoła, lunes 26.05 nueva campaña de roble): 0,38 m³
   - ZLE-2026-05-075 (Mykoła, 12-14.05 de Part 25, madera en almacén desde el 15.05): 1,84 m³
   Total roble: 2,22 m³

C. Haya común, tablas 25 × 130 × 4000 mm, fresca 32%:
   - Cliente Stolarz Meblowy de Mrągowo, pedido ZLE-2026-05-082: 0,68 m³
   Total haya: 0,68 m³

D. Abedul (restos del invierno, baja prioridad): 0,42 m³

TOTAL: 5,74 m³ en el almacén del aserradero para secado.
```

Don Henryk dice brevemente: *"Cinco metros cúbicos y tres cuartos. La cámara tiene 38 metros netos. Eso es el **15% de llenado**, muy poco para un ciclo."*

Aquí empieza el problema principal de la reunión. La *komora suszarnicza* (cámara de secado convencional) BH-50 está diseñada para trabajar con un **llenado del 80-100%** (30-38 m³ netos). Con un 15% de llenado:

- El flujo de aire es demasiado rápido (sin resistencia, los ventiladores solo "airean")
- La temperatura no se estabiliza uniformemente en la cámara (convección desigual)
- El consumo de energía por metro cúbico es 3-4 veces mayor (electricidad, gas para los calefactores, servicio)
- El *program suszarniczy* (programa de secado) (calibrado para una carga completa) da resultados no estándar, aumenta el riesgo de grietas internas en la tabla

Don Henryk continúa: *"Tenemos tres opciones. Escucha, Mykoła, porque esto es exactamente lo que algún día tú mismo tendrás que evaluar como futuro maestro, si sigues este camino."*

### 14:25, tres opciones y compromisos

**Opción A, esperar a la carga completa.** No poner en marcha la cámara hasta tener 30+ m³ de madera en almacén. EGIDA procesa **~3 m³/turno** (una persona en una máquina), con 5 días laborables y 2 sierras son **30 m³/semana teóricamente**, en la práctica (clasificación, averías, fines de semana) **~22 m³/semana**. Desde hoy hasta la carga completa de 30 m³: hoy 5,74 m³, faltan 24 m³ más, es decir **8-10 días laborables**, o sea ~**13 días de calendario**. Carga lista hacia **2026-06-11 miércoles**.

Ventajas: economía óptima, el ciclo del programa se mantiene, la calidad de secado es la mejor.
Desventajas: **el cliente de ZLE-077 espera recogida el 2026-06-20** (desde hoy 22 días). Ciclo de secado 8-9 días más elaboración final más entrega 3 días = 11-12 días desde el inicio del secado. Es decir inicio como máximo **2026-06-08 lunes**. Con la opción A el inicio sería el día 11, 3 días tarde.

**Opción B, externalización para una parte de la madera.** EGIDA tiene un contrato con el *suszarnia zewnętrzna* (secadero externo) **"Drew-Sus"** en Mrągowo (a 40 km de Strzałowo), tarifas 2026:

- Secado de pino tablas 25-30 mm: **180 zł/m³**, ciclo 7-9 días en sus instalaciones
- Transporte ida y vuelta para camión de contenedores (3-5 m³ de carga): **350 zł por viaje**
- Total para lote de 3 m³: 540 zł secado + 350 zł transporte = **890 zł / 3 m³ = 297 zł/m³**

Para ZLE-077 (0,58 m³) lote individual: demasiado pequeño para un viaje propio. Habría que consolidarlo con el pino de ZLE-079 0,72 m³ y pino excedentes 1,12 m³ = 2,42 m³ en total. Más roble si el mismo secadero lo acepta (no, roble y pino programas diferentes, por separado). Así que **2,42 m³ de pino por 719 zł = 297 zł/m³** (sin roble, el roble se queda para la siguiente carga EGIDA).

Ventajas: ZLE-077 terminado dentro del plazo (inicio externo ~2 de junio, fin ~12 de junio, transporte 13 de junio, el cliente recoge el 20 de junio, colchón de 7 días). El roble de EGIDA espera a la próxima carga completa, no bloquea ZLE-077.
Desventajas: coste 297 zł/m³ vs **~85 zł/m³ del secado propio** (electricidad, gas, amortización de la cámara), es decir **212 zł de diferencia por m³, 512 zł para 2,42 m³**. El cliente paga por tablas acabadas a humedad del 12%, no por el método de secado, así que **EGIDA compra puntualidad por 512 zł**.

**Opción C, híbrida.** Externalización para el pino (2,42 m³, plazo crítico), cámara propia para el roble (2,22 m³, plazo holgado, el cliente aún no recoge, puede esperar). Pero solo con el roble (2,22 m³) faltan otros **28 m³** para completar la carga de EGIDA, es decir **12 días laborables cortando solo roble** (~2 m³/turno × 6 turnos × 2 sierras = 24 m³), no es realista (la campaña de roble está limitada por la materia prima disponible de la Oficina Forestal de Strzałowo, contingente de junio ~4-5 m³).

Realistamente la híbrida significa: externalización para el pino, **espera de 3-4 semanas** para el roble (la próxima carga de roble sería hacia **2026-07-01** cuando tengamos más troncos).

### 14:45, decisión

Don Henryk, tras un momento de reflexión, le dice a Marek:

*"Marek, yo me quedaría con la opción B. El pino sale fuera, 512 zł extra en el margen, pero el cliente lo recibe a tiempo y nadie habla de retrasos. La cámara propia la arranco con roble cuando haya 30 m³, probablemente a mediados de junio, entonces nueva carga."*

Marek: *"¿Y cuánto nos estropea la economía de ZLE-077?"*

Don Henryk rápido mentalmente: *"Precio de venta de madera de pino C24 tablas 25 × 150 después de secado y elaboración: **1700 zł/m³** cliente ZLE-077. Coste de producción EGIDA para el pino: **~1100 zł/m³** (materia prima del bosque 380, trabajo de aserrado 220, secado propio 85, elaboración 200, amortización 180, otros 35). Margen 600 zł/m³. Con 0,58 m³ = **348 zł de margen**. Secado externo más 212 zł/m³ = más 123 zł, el margen baja a **225 zł**. Sigue siendo rentable, el cliente ni se entera."*

*"Aceptado,"* dice Marek. *"Opción B. Mañana por la mañana llamo a Drew-Sus, acuerdo la carga el martes 3 de junio, pedido de todo el pino del almacén 2,42 m³. Nuestra cámara la dejamos vacía hasta mediados de junio, luego arrancamos carga completa de roble."*

Don Henryk asiente, va al escritorio en el rincón de la sala de control, rellena la *karta KS-001* (ficha KS-001 del secadero, formato A4, dedicada a cada decisión de carga). Mykoła mira por encima del hombro.

### 14:55, ficha KS-001 rellenada

Don Henryk escribe en las secciones:

**Sección 1, Carga planificada (si procede)**:
```
Tipo de carga: pino silvestre, tablas 28 × 155 × 4050 mm sin secar
Volumen planificado: 2,42 m³ (ZLE-077 0,58 + ZLE-079 0,72 + excedente almacén 1,12)
Humedad inicial (media de 4 puntos de medición): 30-32%
Humedad objetivo: 12% ±1%
Programa de secado elegido: NO APLICA (carga externa Drew-Sus)
Justificación: volumen pequeño, cámara propia no rentable,
             el plazo del cliente ZLE-077 exige secado hasta el 12.06,
             la externalización permite mantener la puntualidad.
```

**Sección 2, Próxima carga planificada (para cámara propia)**:
```
Inicio planificado: ~2026-06-15 (tras reunir 30+ m³)
Tipo planificado: roble común, tablas 28 × 155 × 4050 mm
Volumen previsto: 30-38 m³ (carga completa, requiere 17 días de acumulación)
Programa planificado: DUB-STAND-28 (roble estándar tablas 28 mm, ciclo 22 días)
Humedad inicial prevista: 35-38%
Humedad objetivo: 14%
```

**Sección 3, Notas y observaciones**:
```
Carga actual (roble desde el 17.05) va con normalidad, plan de salida el 07.06.
Próxima campaña de roble de la Oficina Forestal de Strzałowo planificada 08-15.06.
Don Henryk vacaciones 2 semanas 20.06-04.07, Maciek solo con la cámara,
   en caso de problema escalado Marek -> BTM (servicio polaco del secadero).
Mykoła Hrycenko participa en la reunión (formación M3 bloque procesos, l3).
```

**Firma**: Don Henryk, fecha, hora.

Retención: **3 años en papel** en la oficina del secadero, **5 años escaneado** en OneDrive de EGIDA.

### 15:05, pedido externo, llamada telefónica

Marek sale de la sala de control hacia su propia oficina (5 minutos a pie por la explanada), hace una llamada a Drew-Sus. Vuelve tras 20 minutos con la confirmación:

- Drew-Sus acepta 2,42 m³ de pino el martes **2 de junio 8:00-10:00** (carga con su camión en EGIDA).
- Ciclo de secado **8 días** (inicio martes por la tarde, fin el miércoles 10 de junio).
- Transporte ida y vuelta **350 zł netos** tarifa plana.
- Secado **180 zł/m³ netos** × 2,42 = **435,60 zł netos**.
- Total **785,60 zł netos, 966,30 zł brutos**. Factura tras recepción de la madera seca (12.06).

Marek informa a Don Henryk del plazo. Don Henryk añade en la KS-001 en la sección 3:
```
Actualización 14:55: pedido Drew-Sus confirmado.
Carga martes 02.06 8:00-10:00 (Marek coordina).
Salida 10.06, transporte de vuelta 11.06, elaboración final y entrega al cliente 13-20.06.
Coste: 785,60 zł netos.
```

## Objetivos

Tras esta lección:

1. Conoces la **estructura de la cámara de secado de EGIDA**: Brunner-Hildebrand BH-50 (fabricante austriaco con tradición alemana, distribución en Polonia desde 2005), capacidad bruta **50 m³**, neta **38 m³** de madera aserrada. Tipo convencional (calentamiento con aire caliente más ventiladores axiales más extracción de humedad al exterior), no por condensación, no al vacío. Año de fabricación EGIDA 2011, servicio BTM Polska (distribuidor polaco). Una sola cámara para todo el aserradero.
2. Conoces las **cinco fases del ciclo típico de secado en cámara convencional**: 1) **calentamiento** (2-3 días, la temperatura sube de 20 a 30-40°C, humedad RH 95% para que la madera no pierda agua en exceso), 2) **secado previo** (4-7 días, temperatura 40-50°C, RH 85% -> 65%, la madera cede el primer 10-15% de humedad), 3) **secado principal** (5-14 días, temperatura pico 60-70°C, RH 40-50%, humedad de la madera del 25% al objetivo), 4) **acondicionamiento** (2-4 días, temperatura 55-65°C, RH 70-80%, nivelación de tensiones internas), 5) **enfriamiento** (1-2 días, temperatura baja a 25-30°C, madera lista para salir).
3. Conoces los **tiempos típicos de ciclo** para las principales especies de EGIDA (programas del controlador BH-50): **pino fresco 25-32 mm**: 7-9 días, humedad objetivo 12% (carpintería de construcción) u 8-10% (carpintería de muebles); **roble fresco 28-30 mm**: 20-24 días, objetivo 14%; **haya fresca 25-28 mm**: 14-18 días, objetivo 10%; **abedul 20-25 mm**: 12-15 días, objetivo 12%. Entiendes que el tiempo depende del grosor de la tabla cuadráticamente (una tabla el doble de gruesa = aprox. cuatro veces más ciclo) y que las especies más duras (roble) se secan mucho más lento que las blandas (pino).
4. Conoces **EMC (contenido de humedad de equilibrio de la madera)** como valor de control del programa: para una temperatura de 25°C y RH del aire del 60% la EMC de la madera es ~10%. El controlador BH-50 mantiene esta relación (para el pino objetivo 12% requiere temperatura de 60°C y RH ~50% al final del ciclo), no "seca directamente" sino que **crea condiciones en las que la madera tiende a ~12%**. Entiendes que una bajada demasiado rápida de humedad (exposición a RH < 30% en la fase inicial) provoca grietas en el extremo de la tabla (*end checks*), y demasiado lenta (RH > 60% en la fase principal) provoca moho interno.
5. Conoces el **problema de la homogeneidad de la carga y el límite económico inferior**. La cámara BH-50 está diseñada para un llenado del 80-100% (30-38 m³ netos). Un llenado inferior al 60% (23 m³) produce desigualdad de temperatura (las esquinas de la cámara son más frías que el centro) y un resultado impredecible. **En la práctica EGIDA mínimo 30 m³ por carga**, lo que significa que la madera en el almacén de secado se reúne durante **10-17 días** (producción típica de EGIDA ~22 m³/semana, de los cuales el 60% va al secado, 40% se vende en verde o se aparta).
6. Conoces los **criterios para elegir secado externo** (Drew-Sus en Mrągowo para EGIDA): 1) plazo del cliente crítico, menos de 20 días hasta la entrega; 2) lote específico que no puede mezclarse con la carga propia planificada (p.ej. pino vs roble); 3) lote único de 0,5-3 m³ sin posibilidad de agregarlo en la próxima semana. Conoces las tarifas 2026: **180 zł/m³ de secado más 350 zł de tarifa plana de transporte ida y vuelta**, se traduce en **~260-300 zł/m³ para lotes de 2-3 m³**, frente a **~85 zł/m³ del secado propio**.
7. Entiendes el **límite de competencias del operador M3 en secado**. El operador M3: participa en las reuniones de planificación, aporta información sobre la madera fresca en el almacén de secado, comprende el programa del controlador, lee e interpreta los indicadores del panel, en caso de alarma puede **realizar un diagnóstico preliminar** (alarma de temperatura, alarma de flujo de aire) y notificarlo al maestro del secadero. El maestro del secadero (Don Henryk en EGIDA): **decide** sobre el programa, la carga, el momento de inicio, las correcciones durante el ciclo, el acondicionamiento. El operador M3 **no pone en marcha el programa por su cuenta** (requiere formación de fábrica BTM, que el operador M3 no tiene), **no modifica parámetros** durante el ciclo, **no clasifica la madera tras el secado** (eso es el clasificador, Doña Ania).
8. Conoces la **ficha KS-001** (ficha del secadero): formato A4, cuatro secciones (carga planificada, próxima carga, notas y observaciones, firma), rellenada **por el maestro del secadero** para cada decisión de carga (planificación, observaciones de la carga actual, finalización de carga, decisiones externas). Retención **3 años en papel** más **5 años escaneado en OneDrive**. El operador M3 **no rellena la KS-001 por su cuenta**, pero participa en su cumplimentación durante las reuniones de planificación (entiende la estructura del documento).

## Contenido

### 1. Qué es el secado de la madera y para qué sirve

La **madera recién cortada** (pino, roble, haya, abedul) contiene típicamente un **35-55% de humedad** (porcentaje de masa de agua en la masa total de la madera). Esta agua está en dos formas: 1) **agua libre** en la luz de las células de los vasos conductores, 2) **agua ligada** en las paredes celulares (ligada químicamente por celulosa y hemicelulosa). El agua libre sale más rápido (primeros 8-20 días de secado), el agua ligada más lento (siguientes semanas).

**Para qué secamos**:

1. **Estabilidad dimensional**. La madera fresca se contrae tras el corte, a medida que pierde agua. La contracción es desigual: radial (12-20% al máximo para el roble), tangencial (8-12% para el roble), longitudinal (<1%). Si una tabla no está seca antes de usarla en un edificio, **se contrae en la estructura** (grietas, juntas entre tablas, techos que se hunden).

2. **Resistencia mecánica**. La madera secada al 12% tiene una **resistencia a la flexión mayor en un 40-60%** que la madera fresca. Las clases de resistencia (C16, C24, C30) están **calibradas para una humedad del 12%**. La madera secada a otro objetivo (p.ej. 18%) da una resistencia distinta, hace falta un factor de conversión.

3. **Protección contra hongos y mohos**. La madera con humedad inferior al 20% **no es medio de crecimiento** para hongos de moho. La madera fresca es ideal para el moho (agua + celulosa + temperatura ambiente real).

4. **Posibilidad de elaboración**. La madera fresca **no se mecaniza bien** con cepilladora (resbala, cepilla desigual), **no se encola bien** (las colas requieren humedad del 8-12%), **no se barniza** (el barniz no agarra en madera mojada). Para **carpintería de muebles** el requisito es 8-10%, para **carpintería de construcción y suelos** 12%, para **armaduras de cubierta** 18%.

5. **Reducción de masa y coste de transporte**. 1 m³ de pino fresco al 35% de humedad pesa **~720 kg**. El mismo pino al 12% de humedad pesa **~520 kg**. Diferencia de 200 kg/m³, para 10 m³ son 2000 kg menos de transporte. Coste de transporte EGIDA -> cliente Varsovia de media 35-45 zł/km, camión de 15 t: ahorro real.

### 2. Dos formas básicas de secado

**Secado natural (*sezonowanie* (secado al aire / oreo))**: la madera almacenada en una explanada cubierta sin aislamiento con calefacción, el agua se evapora a la atmósfera con aire frío. Tiempo: **6-12 meses para tabla de 25 mm de pino**, **24-36 meses para tabla de 28 mm de roble**. Ventajas: bajo coste (sin energía, solo tiempo), calidad natural del secado (lento, sin tensiones). Desventajas: **muy lento** (la capacidad de EGIDA si solo secase al aire sería el ~30% de la actual), **estacional** (en invierno la humedad baja muy lento, en primavera riesgo de moho), **sin control del objetivo** (la humedad final depende del clima, no del requisito).

EGIDA usa el secado al aire para **prioridades bajas** (abedul, restos de roble, lotes sin cliente concreto), **explanada de almacenamiento de 800 m²** detrás de la nave, 4-6 pilas (cada una de 15-25 m³), rotación continua.

**Secado en cámara**: madera en cámara cerrada, calentamiento controlado, humedad del aire regulada, ventilación forzada. Tiempo: **7-30 días** según especie y grosor. Ventajas: **rápido, controlado, repetible** (un programa 5 veces da 5 veces el mismo resultado), humedad objetivo precisa (±1%). Desventajas: **caro en energía** (la BH-50 de EGIDA consume 800-1200 kWh por ciclo de 20 días más gas ~400 kg), requiere **especialista** (maestro del secadero), riesgo de grietas con un programa erróneo.

EGIDA usa la cámara para **la producción principal** (pino C24, roble para suelos, haya para muebles), pedidos de clientes planificados, cada lote con plazo.

### 3. Cuándo secado combinado

En la práctica de EGIDA tres estrategias combinadas:

**Secado al aire previo más cámara**. Para el roble fresco (35-38% de humedad) aplicamos **2-3 semanas de oreo en la explanada** (baja a ~28-30% de humedad), después **cámara 20-24 días** (del 28% al 14%). Total 5-6 semanas. Ventajas: ahorro de energía en la cámara (el primer 10% de humedad la madera lo cede "gratis" en la explanada), la cámara trabaja en el rango en el que es eficiente.

**Cámara más oreo final** (raro, para clientes especiales). Cámara hasta el 14%, luego oreo 2-3 meses, la madera "madura" en un clima estable, las tensiones llegan al equilibrio. Se usa para exportación a regiones de clima distinto (Alemania, Países Bajos), donde la madera ya está "asentada" y no se agrieta en el transporte.

**En dos etapas en la cámara**. Madera muy fresca (pino fresco 32%+), cámara programa de fase de calentamiento y secado previo (7 días), luego **pausa en nave climatizada** (3-5 días, la madera se estabiliza), a continuación **cámara segundo programa** de secado principal y acondicionamiento (5-8 días). Total 15-20 días. Se usa para lotes grandes donde acortar el ciclo no es crítico.

### 4. Programa de secado para pino fresco 28 mm

Ejemplo del programa **SOS-STAND-28** (pino estándar tablas 28 mm fresco hasta 12%), usado por EGIDA en la cámara BH-50 (y usado también por Drew-Sus, porque tienen un controlador Brunner similar):

```
DÍA 1 (calentamiento):
  Temperatura: 20 -> 35°C (despacio, ~0,5°C/h)
  Humedad RH: 95% (muy alta, la madera no se seca)
  Objetivo: igualar la temperatura de toda la masa de madera
  Final del día 1: madera a 35°C, humedad de la madera sin cambios (32%)

DÍA 2-3 (secado previo):
  Temperatura: 35 -> 50°C
  Humedad RH: 95% -> 70%
  Objetivo: eliminar el agua libre (la más fácil)
  Final del día 3: humedad de la madera ~20-22% (del 32%, caída 10-12%)

DÍA 4-7 (secado principal):
  Temperatura: 50 -> 70°C (pico)
  Humedad RH: 70% -> 40%
  Objetivo: humedad de la madera al 14-15%
  Final del día 7: madera a 70°C, humedad de la madera 14%

DÍA 8 (acondicionamiento):
  Temperatura: 70 -> 60°C
  Humedad RH: 40% -> 70%
  Objetivo: nivelación de tensiones internas, sin grietas internas
  Final del día 8: madera a 60°C, humedad 12-13%

DÍA 9 (enfriamiento):
  Temperatura: 60 -> 25°C (naturalmente, ventiladores sin calentamiento)
  Humedad RH: 70% (estable)
  Objetivo: madera lista para salir sin shock térmico
  Final del día 9: madera a 25°C, humedad 12%, SALIDA DE LA CÁMARA.
```

**Tiempo total**: 9 días (ciclo nominal). En la práctica ±1-2 días según la humedad inicial y los parámetros de la cámara.

**Parámetros del controlador**:
- Sensores de temperatura: 4 (esquinas de la cámara más el centro)
- Sensores de humedad relativa del aire: 2 (entrada del ventilador más salida)
- *Sondy wilgotności drewna* (sondas de humedad de la madera): 3 (sondas clavadas en tablas en 3 pilas distintas: delante, centro, atrás de la cámara)
- Desviación admisible: temperatura ±2°C del valor de consigna, RH ±5% del valor de consigna
- Alarma del controlador: superación de la desviación admisible en un 50% (4°C temp, 8% RH)

**Consumo de energía**: ~180 kWh/día (electricidad de los ventiladores), ~25 kg de gas/día (calentamiento), total **~85 zł/m³ por ciclo** con carga completa de 38 m³.

### 5. Programa de secado para roble fresco 28 mm

El roble requiere un **ciclo mucho más lento**, porque tiene mayor riesgo de grietas (estructura tangencial-radial con gran diferencia de contracción, núcleo de la madera sensible al shock térmico):

```
DÍA 1-2 (calentamiento lento):
  Temperatura: 20 -> 30°C (muy despacio, 0,2°C/h)
  Humedad RH: 95%
  Objetivo: temperatura de la masa de madera sin shock

DÍA 3-10 (secado previo):
  Temperatura: 30 -> 40°C (despacio)
  Humedad RH: 90% -> 75%
  Objetivo: humedad de la madera 38% -> 28%

DÍA 11-18 (secado principal):
  Temperatura: 40 -> 60°C (pico del roble, no más alto)
  Humedad RH: 75% -> 45%
  Objetivo: humedad de la madera 28% -> 16%

DÍA 19-21 (acondicionamiento largo):
  Temperatura: 60 -> 55°C
  Humedad RH: 45% -> 75%
  Objetivo: nivelación de tensiones (el roble es especialmente sensible, riesgo de grietas internas)

DÍA 22 (enfriamiento):
  Temperatura: 55 -> 25°C
  Humedad RH: 75% estable
  Final: madera a 25°C, humedad 14%, SALIDA.
```

**Tiempo total**: **22 días nominales**, a menudo 24-25 días en la práctica para lotes grandes.

**Diferencias clave vs pino**:
- Temperatura pico **60°C** (vs 70°C pino), más alto el roble se agrieta
- Acondicionamiento **3 días** (vs 1 día pino), el roble requiere una nivelación larga
- Humedad objetivo **14%** (vs 12% pino), el roble no alcanza el 12% sin quedar quebradizo

**Consumo de energía**: ~180 kWh/día × 22 días = 3960 kWh más ~400 kg de gas = ~**80-90 zł/m³** (parecido al pino, porque es más lento pero con temperaturas más bajas).

### 6. Qué ve el operador M3 en el panel del controlador

El panel de control de la BH-50 en la sala de control del secadero muestra **en tiempo real**:

**Pantalla principal**:
- Nº de programa (p.ej. SOS-STAND-28)
- Día del ciclo (p.ej. 5 de 9) y fase (p.ej. "Secado principal")
- Temperatura del aire de la cámara (en °C, de los cuatro sensores más la media)
- Humedad relativa del aire (RH en %, de los dos sensores más la media)
- Humedad de la madera (de las tres sondas, más la media, más la dispersión)
- EMC (calculada a partir de la temperatura y RH del aire, comparación con la humedad actual de la madera)
- Estado de los ventiladores (revoluciones RPM, corriente A)
- Estado de los calefactores (potencia kW actual, porcentaje del máximo)

**Pantalla de alarmas** (si cualquiera de los sensores está fuera de rango):
- Tipo de alarma (temperatura, humedad, flujo, sensor)
- Hora de detección (hora, minuto)
- Valor leído vs esperado
- Recomendación automática (p.ej. "aumentar ventilación", "detener ciclo")

**Qué entiende el operador M3** (sin intervenir):
- Si la temperatura está a ±2°C del valor de consigna, **OK**, el programa se mantiene.
- Si la humedad de la madera baja monótonamente (cada día 1-2%), **OK**, el secado avanza.
- Si la dispersión entre las tres sondas de humedad de la madera es <2%, **OK**, carga homogénea.
- Si la dispersión es >3%, algo va mal (problema de colocación de pilas, flujo de aire desigual, notifícalo al maestro).
- Si hay alarma roja en la pantalla, **notifícalo al maestro inmediatamente** (no intentes resolverlo por tu cuenta).

**Qué NO hace el operador M3**:
- No cambia los parámetros del programa (temperatura, RH, duración de fase)
- No conmuta a otro programa durante el ciclo
- No abre la puerta de la cámara durante el ciclo (deja escapar el calor, shock térmico de la madera)
- No apaga los ventiladores ni los calefactores
- No resetea la alarma sin permiso del maestro

### 7. Homogeneidad de la carga, por qué es crítica

La cámara de secado seca **toda la carga simultáneamente bajo el mismo programa**. Si la carga es **no homogénea** (distintas especies, distintos grosores, distintas humedades), el programa óptimo para una parte de la carga es **erróneo para el resto**. Ejemplos:

**A. Pino 25 mm más roble 25 mm juntos**. Programa de pino 9 días al 12%. Roble tras 9 días en este programa: temperatura 70°C (demasiado alta para el roble, se agrieta), humedad del roble todavía 22% (no secado). Programa de roble 22 días al 14%. Pino tras 22 días: humedad 8% (demasiado baja, madera quebradiza), temperatura 60°C (OK), pero tiempo 2,5 veces más largo del necesario (pérdida de energía). **No mezcles especies en una misma carga.**

**B. Pino 25 mm y pino 45 mm juntos**. La misma especie, pero distinto grosor. Programa de 25 mm 9 días. El de 45 mm en 9 días: humedad 20% (no secado), el ciclo hay que alargarlo 3-5 días. Programa de 45 mm 15 días. El de 25 mm en 15 días: humedad 9% (sobresecado), quebradizo. **Grosores distintos significan compromiso o dos cargas.**

**C. Pino fresco 32% más pino oreado 22% juntos**. La misma especie, el mismo grosor, pero distinta humedad de partida. Comportamiento distinto en las fases iniciales: el fresco cede mucha agua (satura el aire), el oreado cede poca (no satura). En la fase principal el fresco aún está húmedo, el oreado ya sobresecado. **Mezclar humedades de partida es admisible solo en un rango de ±5% (p.ej. 28-33% juntos, 20-25% juntos)**.

**Evaluación de la homogeneidad antes de la carga** (procedimiento del maestro del secadero):
1. Medición de humedad **en al menos 10 tablas** de distintos lotes de la carga planificada.
2. Cálculo de la dispersión. Si <±5% de la media, carga homogénea.
3. Registro en la KS-001 sección "Carga planificada" (media, mínimo, máximo).
4. Si la dispersión es mayor, división en dos cargas o descarte de una parte para otra carga.

### 8. Acondicionamiento y tensiones internas

El **acondicionamiento** (fase 4 del ciclo, tras el secado principal) es la **fase clave de calidad**, a menudo infravalorada por el operador principiante. Físicamente: la madera tras el secado principal tiene un **gradiente de humedad interno**. La capa exterior de la tabla (superficie) está seca (8-10%), el núcleo de la tabla está más húmedo (14-15%). El gradiente genera **tensiones internas** (compresión de las capas exteriores, tracción del núcleo).

Si la tabla sale de la cámara en este estado y va a elaboración (cepilladora, sierra escuadradora), **las tensiones se manifiestan**: la tabla tras el corte "cruje" (microfisuras internas), tras el cepillado se deforma (warping), tras varias semanas en el edificio el cliente ve **grietas internas** (internal checks).

El acondicionamiento **invierte parcialmente el gradiente**: al subir la humedad del aire (RH del 40% al 70%) con temperatura algo más baja (60°C desde 70°C), las capas exteriores de la tabla **absorben algo de humedad** del aire (la humedad de la superficie sube del 8% al 11%), el núcleo sigue equilibrándose hacia abajo (15% -> 13%). Tras 2-3 días el gradiente **baja al 2-3%** (desde 6-7%), tensiones disueltas.

**Test en la práctica**: el operador M3 mira el indicador de dispersión entre las sondas de humedad tras el acondicionamiento. Si tres sondas muestran 11,8 / 12,0 / 12,3% (dispersión 0,5%), acondicionamiento logrado. Si 10,5 / 12,0 / 13,8% (dispersión 3,3%), acondicionamiento insuficiente, el maestro prolonga la fase un día.

::: info
**Saltarse el acondicionamiento** es el atajo de secado más común "por ahorro". Un operador sin formación ve que la madera "ya está seca" tras la fase principal (humedad 12% en las sondas), quiere sacarla. El maestro responde: **"ves la media, no ves las tensiones". La madera sin acondicionamiento parece idéntica por fuera, pero se agrieta en 2-4 semanas en casa del cliente**, la reclamación es inevitable. El coste de la reclamación (sustitución de la madera más coste de transporte más visita al cliente) siempre superará el ahorro de los 2 días de acondicionamiento (40-60 zł de electricidad).
:::

### 9. Humedad de equilibrio EMC y programa

La **EMC (Equilibrium Moisture Content, humedad de equilibrio)** es la humedad a la que **tiende la madera** en un entorno dado (temperatura, RH del aire). Es un concepto fundamental del secado. La EMC depende de la temperatura y RH, no de la especie de madera (existen pequeñas diferencias entre especies, pero en la práctica de EGIDA se usan tablas simplificadas).

**Tabla EMC** (simplificada, para pino y roble a temperatura de 20-70°C):

| Temperatura | RH 30% | RH 50% | RH 70% | RH 90% |
|---|---|---|---|---|
| 20°C | 6,3% | 9,2% | 13,1% | 20,5% |
| 40°C | 5,8% | 8,5% | 12,2% | 19,3% |
| 60°C | 5,2% | 7,7% | 11,2% | 18,0% |
| 70°C | 5,0% | 7,4% | 10,8% | 17,5% |

**Cómo utiliza el controlador la EMC**: en cada fase del ciclo el controlador conoce la temperatura y RH de consigna, calcula la EMC actual, la compara con el objetivo para esa fase. Si la madera está por encima del objetivo EMC para ese instante, **el secado continúa** (el agua se evapora). Si la madera está por debajo de la EMC (secado demasiado rápido), el controlador **aumenta el RH** (inyecta vapor o apaga la ventilación) para que la madera ralentice el secado.

**Clave para entender pino 28 mm al 12%**: el programa final requiere **temperatura de 60°C y RH del 50%**, porque entonces EMC ≈ 7,7% (tabla). La madera tiende al 7,7%, pero debido al grosor de la tabla y a la difusión, en 2-3 días de la última fase no alcanzará el 7,7%, se detendrá en ~12%. **Ahí el controlador termina el ciclo** (objetivo alcanzado). Si el ciclo durase 5 días más, la madera bajaría al 8%, estaría demasiado seca.

El **maestro del secadero** entiende esta dinámica de forma intuitiva. El **operador M3** entiende el principio (EMC, por qué 60°C y 50% RH dan 12% en 28 mm). No tiene que calcular la EMC mentalmente, pero ve en el panel "EMC actual 7,7% vs humedad de la madera 12%" y sabe qué significa.

### 10. Problemas típicos del ciclo y cómo los señala el operador M3

**Problema 1. La temperatura no alcanza el valor de consigna**. El programa marca 70°C, el controlador muestra 62°C. Causas:
- Calefactor averiado (servicio)
- Termostato sucio (servicio)
- Carga demasiado grande, el calefactor no da abasto (el operador informa, el maestro baja el objetivo)
- Puertas sin estanqueidad (el maestro comprueba, eventualmente cambia las juntas)

**Señalización del operador M3**: notificación a Don Henryk tras 2 horas de desviación. "Cámara a 62 en vez de 70, desde hace 2 horas."

**Problema 2. La humedad de la madera baja de forma desigual en las sondas**. Las sondas 1/2/3 muestran 18/14/21%. Dispersión 7%. Causas:
- Sondas colocadas en distintas especies (error de carga, el maestro corrige)
- Carga mal colocada, flujo de aire desigual (el maestro decide la corrección)
- Sonda averiada (el maestro comprueba tras el ciclo)

**Señalización del operador M3**: notificación de dispersión >3%. "Sondas 18/14/21, dispersión 7%, desde la mañana."

**Problema 3. Alarma de ventilación**. El controlador muestra "alarma: flujo de aire por debajo del 80%". Causas:
- Ventilador averiado (el maestro detiene el ciclo, llama al servicio)
- Atasco en los conductos de ventilación (el maestro comprueba)
- Sensor de flujo averiado (el maestro pasa a control manual)

**Señalización del operador M3**: **inmediata**, llamada al maestro. "Alarma de ventilación en la cámara, LED roja."

**Problema 4. Olor a moho en la sala de control**. Señal sutil de que en la cámara hay condiciones propicias al moho (humedad demasiado alta en la fase de secado previo, normalmente por insuficiencia de los calefactores). No siempre lo alarma el controlador, requiere nariz experimentada.

**Señalización del operador M3**: notificación al maestro, "en la nave huele a humedad, seguro que algo pasa en la cámara". El maestro comprueba, decide.

### 11. Formación de secado del operador M3 tras la lección

EGIDA ofrece a los operadores M3 un **módulo de formación adicional de secado** (opcional, tras aprobar M3), que dura 5 días. Alcance:

1. **Día 1**: teoría del secado (difusión, EMC, programas, acondicionamiento), clases de Don Henryk.
2. **Día 2**: observación del ciclo completo desde dentro de la cámara (solo en la fase de enfriamiento, porque en la fase caliente no entramos), mediciones con sondas, manejo del panel.
3. **Día 3**: planificación de carga (similar a la reunión de hoy, pero el operador dirige, el maestro corrige).
4. **Día 4**: diagnóstico de averías (errores introducidos, el operador intenta reconocerlos).
5. **Día 5**: examen (escrito más práctico, umbral 80%). Aprobarlo otorga la cualificación de **"operador auxiliar de secado"** (puede sustituir al maestro 1-2 días, p.ej. fin de semana), pero **no es maestro** (eso requiere 3 años de experiencia y curso BTM).

Mykoła le expresa a Don Henryk su interés en este curso. Don Henryk: *"Termina M3, luego hablamos. Demasiado pronto, aún te quedan 13 lecciones del bloque de procesos y organizativo. Si te interesa, en octubre arrancaremos la formación."*

Mykoła anota en su agenda: *"octubre 2026, módulo auxiliar de secado, 5 días."*

## Escena de cierre, 15:30, salida de la nave del secadero

Mykoła, Marek y Don Henryk salen de la sala de control. Don Henryk se queda junto a la cámara (comprobará las sondas una vez más, beberá agua, volverá a casa a las 17:00), Marek y Mykoła cruzan la explanada de almacenamiento hacia la nave de sierras.

### 15:35, conversación de Marek con Mykoła

Marek, caminando: *"Mykoła, ¿qué has entendido de la reunión de hoy?"*

Mykoła: *"Tres cosas. Primero, el secado **no es cuestión de máquina sino de tiempo**. 22 días para el roble, 9 días para el pino, nada acortará eso salvo saltar a peor calidad. Segundo, la **carga homogénea** es la base, mezclar especies supone riesgo. Tercero, **el maestro del secadero decide, el operador M3 documenta**. No es como en la sierra, donde yo decido solo."*

*"Bien. ¿Y la cuarta cosa?"*

*"¿Cuarta?"*

*"La externalización como opción. Para el cliente ZLE-077 Drew-Sus nos cuesta 512 zł extra, pero salva el plazo. **El plazo es más importante que el margen**, porque un cliente que recibe la mercancía a tiempo encarga el siguiente pedido. Un cliente que recibe 3 días de retraso busca otro aserradero. Los beneficios a largo plazo se miden por la continuidad de pedidos, no por el margen de un pedido único."*

Mykoła anota en su agenda: *"Plazo > margen. Secado externo como opción estratégica, no de emergencia."*

### 15:45, planificación del futuro inmediato

Marek: *"Mañana viernes, día planificado sin tareas atípicas. El lunes 2 de junio carga para Drew-Sus 8:00-10:00, tú y Wasyl ayudáis con el capataz de la explanada, hay que mover las pilas del almacén de secado al camión. Tras la carga, turno normal en P3 desde las 10:15. Una semana después del lunes, el 9 de junio, salida del roble de la cámara, nueva clasificación (Doña Ania), tú asistes con Wasyl en el sorteo. Ese es el bloque l5 de tu curso, descarga de la cámara, salida desde l3."*

Mykoła asiente. Anota en su agenda: *"02.06 carga Drew-Sus, 09.06 salida del roble de la cámara."*

### 15:50, vuelta a la nave de sierras

Marek vuelve a la oficina del capataz, Mykoła a P3. En P3 aún está la cinta recién soldada de ayer, pedido ZLE-2026-05-079 (Damian por la mañana, ahora Mykoła terminará la tarde), pino tablas 25 × 130 mm. Distinto tipo de corte que ayer (más estrechas, más finas), pero no hay que cambiar los parámetros (pino el mismo, grosor distinto solo en 3 mm), **velocidad de avance 34 st/min** (el pino más fino corta más rápido), **tensión 2200 PSI**, sin cambiar la cinta.

Mykoła rellena una nueva KDP-001 para ZLE-079 (primera sección: materia prima, segunda: cinta ya en la máquina, número conocido, secciones 3-4: parámetros). 10 minutos rellenando. Arranca el corte a las 16:02. Trabaja hasta el final del turno a las 17:00. Wasyl en el alimentador.

## Términos clave

**cámara de secado convencional** (*komora suszarnicza konwencjonalna*, EN *conventional kiln dryer*, ES *cámara de secado convencional*, UK *конвенційна сушильна камера*): recinto cerrado con calentamiento por aire caliente, ventiladores axiales y extracción de humedad, capacidad típica 30-80 m³ netos de madera aserrada, ciclo de secado 7-25 días según la especie.

**programa de secado** (*program suszarniczy*, EN *drying schedule / program*, ES *programa de secado*, UK *програма сушіння*): secuencia programada de fases (calentamiento, secado previo, secado principal, acondicionamiento, enfriamiento) con temperaturas y RH definidas para una especie y grosor concretos, p.ej. SOS-STAND-28 para pino de 28 mm (9 días), DUB-STAND-28 para roble de 28 mm (22 días).

**EMC (Equilibrium Moisture Content)** (*wilgotność równowagowa*, EN *equilibrium moisture content EMC*, ES *contenido de humedad de equilibrio*, UK *рівноважна вологість*): humedad a la que tiende la madera en un entorno dado, dependiente de la temperatura y la humedad relativa del aire, valor teórico de control del programa de secado.

**acondicionamiento** (*kondycjonowanie*, EN *conditioning*, ES *acondicionamiento*, UK *кондиціонування*): penúltima fase del ciclo de secado (2-4 días), en la que la humedad del aire se eleva de nuevo (del 40-50% al 70-80%) a temperatura reducida, con el fin de nivelar el gradiente de humedad interno de la tabla y disolver las tensiones.

**carga del secadero** (*wsadka suszarnicza*, EN *kiln charge / load*, ES *carga del secadero*, UK *завантаження сушарні*): contenido completo de la cámara de secado durante un ciclo, tamaño típico 30-38 m³ netos para la BH-50, requisito de homogeneidad de especie, grosor y humedad de partida.

**homogeneidad de la carga** (*jednorodność wsadki*, EN *charge uniformity*, ES *homogeneidad de la carga*, UK *однорідність завантаження*): requisito de que todas las tablas de la carga tengan la misma especie, grosor similar (±3 mm) y humedad de partida similar (±5%), condición para el correcto funcionamiento del programa.

**sondas de humedad de la madera** (*sondy wilgotności drewna*, EN *wood moisture probes*, ES *sondas de humedad de la madera*, UK *зонди вологості деревини*): sensores eléctricos (habitualmente 2 electrodos clavados en la tabla), miden la humedad de la madera durante el ciclo, tres unidades en la BH-50 (delante, centro, atrás de la cámara), dispersión operativa de lecturas <3%.

**BH-50** (*Brunner-Hildebrand BH-50*, EN *Brunner-Hildebrand BH-50*, ES *Brunner-Hildebrand BH-50*, UK *Brunner-Hildebrand BH-50*): modelo de cámara de secado del fabricante austro-alemán, capacidad 50 m³ brutos 38 m³ netos de madera aserrada, utilizado por EGIDA desde 2011, distribución polaca por BTM.

**secado al aire / oreo** (*sezonowanie*, EN *air drying / seasoning*, ES *secado al aire / oreo*, UK *природне висихання / сезонування*): secado natural de la madera en explanada cubierta sin calefacción, tiempo 6-36 meses, utilizado en EGIDA para lotes de baja prioridad o como secado previo a la cámara.

**secadero externo** (*suszarnia zewnętrzna*, EN *external drying service*, ES *secadero externo*, UK *зовнішня сушарня*): entidad comercial que presta servicio de secado de madera para otros aserraderos, ejemplo EGIDA: Drew-Sus en Mrągowo, tarifa 180 zł/m³ más 350 zł de transporte a tanto alzado por viaje.

**maestro del secadero** (*mistrz suszarni*, EN *kiln master*, ES *maestro del secadero*, UK *майстер сушарні*): empleado con cualificación BTM o equivalente para manejar la cámara de secado, decide sobre el programa, la carga, las correcciones del ciclo, en EGIDA Don Henryk (jubilado estacional).

**ficha KS-001 del secadero** (*karta suszarni*, EN *kiln log card*, ES *ficha del secadero*, UK *картка сушарні*): formulario A4 cumplimentado por el maestro del secadero para cada decisión de carga, cuatro secciones (planificación, próxima carga, notas, firma), retención 3 años papel + 5 años escaneado.

**humedad objetivo** (*target wilgotności*, EN *target moisture content*, ES *humedad objetivo*, UK *цільова вологість*): humedad final deseada de la madera tras el secado, depende de la aplicación: 8-10% carpintería de muebles, 12% carpintería de construcción y suelos, 14% roble estructural, 18% armaduras de cubierta.

**gradiente de humedad** (*gradient wilgotności*, EN *moisture gradient*, ES *gradiente de humedad*, UK *градієнт вологості*): diferencia de humedad entre la superficie de la tabla (más seca) y su núcleo (más húmedo) tras el secado principal, disuelta en la fase de acondicionamiento, no respetada provoca grietas internas en casa del cliente.

## Autoevaluación

### A. Fases del ciclo y programas

1. Enumera las **cinco fases** del ciclo típico de secado en cámara. ¿Cuál de ellas es la más larga para pino de 28 mm y cuál para roble de 28 mm?

2. Para pino de 28 mm el ciclo nominal es de **9 días**, para roble de 28 mm es de **22 días**. ¿Por qué el roble requiere un ciclo 2,5 veces más largo, aunque el grosor de la tabla sea el mismo?

3. El **acondicionamiento** es la fase que el operador principiante quiere saltarse "por ahorro". ¿Por qué saltarse esta fase es un error y en cuánto tiempo se ven los efectos en casa del cliente?

### B. EMC y control

4. El controlador BH-50 muestra: temperatura 60°C, RH del aire 50%, humedad de la madera 12%. ¿Debe continuarse el ciclo o finalizarse? Justifícalo mediante la EMC.

5. Para pino con objetivo 12% el controlador tiende a una temperatura de **60°C** y RH del **50%**. ¿Por qué no a RH del 30% (EMC ~5%, secado más rápido)?

6. Tres sondas de humedad de la madera muestran: 11,8 / 12,0 / 12,3%. Dispersión: 0,5%. ¿El acondicionamiento es correcto? Justifica.

### C. Carga y homogeneidad

7. El almacén de secado de EGIDA tiene: 2,42 m³ de pino + 2,22 m³ de roble + 0,68 m³ de haya + 0,42 m³ de abedul = 5,74 m³. La cámara BH-50 tiene 38 m³ netos. ¿Se puede arrancar un ciclo? Justifica.

8. ¿Por qué mezclar en una misma carga pino de 25 mm y pino de 45 mm es **malo** (aunque la especie sea la misma)?

9. La carga tiene 30 m³ de pino fresco al 30%, más 2 m³ de pino oreado al 22% (que se quiere terminar de secar al 12%). ¿Aceptas la homogeneidad? Justifica.

### D. Decisión externa vs propia

10. Secado propio de EGIDA: **~85 zł/m³**. Drew-Sus: **180 zł/m³ + 350 zł transporte a tanto alzado**. Para un lote de 2,42 m³ calcula el coste de Drew-Sus por m³.

11. El pedido ZLE-077 (0,58 m³ de pino) tiene un plazo del cliente el 20.06. El secado propio requiere carga completa de 30 m³, acumulación hasta el 11.06, ciclo de 9 días, salida el 20.06 (sin colchón). ¿Aceptas esta planificación o eliges Drew-Sus? Justifica.

12. La máxima "Plazo > margen" Marek la explicó como principio estratégico. ¿Qué significa esto para la relación aserradero-cliente a largo plazo?

### E. Rol del operador M3

13. El operador M3 participa en la reunión de planificación de carga. ¿**Decide** sobre la elección del programa y de la carga? ¿Quién decide en última instancia?

14. El operador M3 ve en el panel del controlador "alarma de ventilación, LED roja". Qué hace: a) resetea la alarma, b) abre la puerta de la cámara, c) notifica al maestro del secadero por teléfono, d) apaga el ventilador manualmente. Elige y justifica.

15. El operador M3 tras aprobar la formación auxiliar de secado (5 días + examen) recibe la cualificación de "operador auxiliar de secado". ¿Qué puede y qué no puede hacer?

### F. Escenarios de planificación

16. EGIDA tiene 28 m³ de pino fresco en el almacén de secado. El cliente espera recogida de madera seca dentro de 18 días. Ciclo de pino 9 días + transporte 1 día + elaboración 4 días + colchón 1 día = 15 días. Acumular los siguientes 2 m³ hasta la carga completa de 30 m³ son 2 días. ¿Arrancas la cámara hoy o esperas 2 días? Justifica.

17. Don Henryk vacaciones 2 semanas 20.06-04.07. En ese tiempo la cámara tiene planificado un ciclo de roble de 22 días (inicio 15.06, salida 07.07). ¿Quién responde por la cámara durante las vacaciones de Don Henryk y qué significa eso para el operador M3?

18. El secadero externo Drew-Sus trabaja con el mismo controlador Brunner que EGIDA, tiene los mismos programas. ¿Por qué no encargar el 100% del secado allí y cerrar la cámara propia? Da dos razones operativas y una económica.
