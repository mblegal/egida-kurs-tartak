---
id: m3-w3-l1
blok: procesy
czas: 120
---

## Introducción

Lunes, 26-05-2026, 6:58 de la mañana. Rustam entra en la nave de aserraderos. Detrás va Wahan. Después del fin de semana, tras cerrar el jueves la campaña de roble, tras el servicio del Sr. Krzysztof el jueves por la mañana (l8, cilindro de elevación del cabezal LT70 sustituido, aceite Shell TTF-SB añadido, prueba de estanqueidad de 30 minutos superada), la P3 trabaja desde el jueves por la tarde sin fugas. El viernes trabajó en ella Damian (segundo operador independiente de EGIDA, acababa los restos de pino). El lunes por la mañana la máquina está caliente por el precalentamiento inicial del sábado por la mañana (de la lección m3-w1-l7), lista para un nuevo encargo.

En el bolsillo del mono de Rustam va la **orden de producción** en papel, formato A5, impresa el viernes a las 16:00 por Marek Kowalski. El encargo **ZLE-2026-05-077**, recogido en la oficina de EGIDA, a la entrada, a las 6:55. Marek la enseñó brevemente, preguntando *"Rustam, ¿la coges hoy en la P3?"*, a lo que Rustam asintió con la cabeza, comprobó el material en el almacén y volvió a la nave. La orden tiene este aspecto:

```
EGIDA ASERRADERO STRZAŁOWO
Orden de producción nº ZLE-2026-05-077
Fecha de emisión: 2026-05-22 (viernes)
Fecha de ejecución: 2026-05-26 (lunes), turno 7:00-15:00

Material: pino silvestre (Pinus sylvestris), almacén SO-SOS-12,
          4 trozas, *dłużyca* (fuste / tronco entero) 4,1 m, diámetro medio 32 cm,
          humedad actual 32% (fresca, cortada el 2026-05-18),
          clase C (sin defectos críticos, clasificada por la Sra. Ania el 23.05)

Surtido objetivo: tablas de suelo en bruto
                  28 × 155 × 4050 mm (sobredimensión +3 mm grosor, +5 mm anchura, +50 mm longitud)
                  Clase resistente: C24 (requisito del cliente)
                  Objetivo tras secado y mecanizado: 25 × 150 × 4000 mm, hum. 12%

Cantidad objetivo: aproximadamente 0,55 m³ de madera aserrada en bruto (equivale a ~0,48 m³ tras secado y mecanizado)

Máquina: P3 Wood-Mizer LT70 (prioritaria) o P1 Serra SM40 (de reserva)
Operador: R. Nazarov
Ayudante: W. Petrosjan (M1 estacionario P3)

Selección de parámetros de corte: decisión del operador independiente (M3)
  - Anotar los parámetros elegidos en la ficha KDP-001 antes del primer corte
  - En caso de duda, consulta al encargado (M. Kowalski, tel. 501 ***)

Firma del emisor: M. Kowalski, encargado de EGIDA, 2026-05-22
```

Tres líneas de la orden son clave: **material**, **surtido objetivo**, **selección de parámetros a decisión del operador**. Hasta marzo de 2026 (M2, bajo supervisión) los parámetros los elegía el encargado y los anotaba en la orden. Desde abril, desde que Rustam aprobó el examen M3 y pasó a "independiente", es el **operador** quien elige: qué cinta monta, qué tensión ajusta, con qué velocidad de avance arranca, qué esquema de corte aplica y en qué orden corta la troza. El encargado ve la elección a posteriori (ficha KDP-001 en sobre de mensajería a la oficina, al final del turno).

Rustam deja la orden en el panel de la P3, coge del escritorio en la esquina de la nave una **ficha KDP-001** nueva (ficha de selección de parámetros, formato A4, introducida en EGIDA en marzo de 2026 por sugerencia del auditor externo como herramienta probatoria: quién ajustó qué y cuándo). Wahan mira por encima del hombro, con la agenda abierta. *"Wahan, hoy aprendemos cómo se deciden los parámetros. Mira cómo pienso, porque algún día pensarás tú solo igual."*

### 7:02, análisis del material y del surtido

Rustam va al almacén SO-SOS-12, estante 4, donde están las cuatro trozas preparadas el viernes. Metro metálico, humidímetro Tanel ET-6 (el mismo de la lección M2 sobre humedad), linterna LED. Cada troza la comprueba:

- **Troza 1** (SO-SOS-12-P1): long. 4,12 m, diám. de testa fina 34 cm, diám. de cepa 36 cm, conicidad 0,5 cm/m (buena). Humedad en el extremo fino, 5 cm desde la testa, 8 mm de profundidad: **33,2%**. Segunda medición a 1 m de la testa: 31,8%. Tercera a 2 m de la testa: 32,5%. **Media 32,5%** (fresca, pino clásico a los 7 días tras la tala). Defectos visibles: nudo resinoso en el extremo fino a 80 cm de longitud, diámetro del nudo 3 cm (admisible para C24 según PN-EN 1611-1, véase l2 M3 T2). Sin fendas medulares visibles en la testa.
- **Troza 2** (SO-SOS-12-P2): long. 4,09 m, diám. 31 cm, hum. 31,9%, sin defectos visibles en la testa. La mejor de las cuatro.
- **Troza 3** (SO-SOS-12-P3): long. 4,15 m, diám. 33 cm, hum. 33,5%, en la cepa una pequeña fenda radial de 8 cm de longitud, admisible para C24 (límite 1/3 del diámetro, o sea 11 cm). Troza a cortar con cuidado, la fenda irá hacia abajo.
- **Troza 4** (SO-SOS-12-P4): long. 4,11 m, diám. 30 cm (la más esbelta), hum. 32,1%, sin defectos. De ella saldrán menos tablas que de las demás, pero todas de calidad uniforme.

Volumen neto total (cálculo simplificado, cilindro medio): **~1,32 m³ de *dłużycy* (fustes)**. Rendimiento esperado para pino silvestre en tablas de suelo de 28 mm: **55-60%** (es decir, de 1,32 m³ de fuste saldrán 0,73-0,79 m³ de madera aserrada en bruto). El encargo exige 0,55 m³, con lo cual hay un **margen de 25-30%** para descartes, defectos internos detectados tras el corte, no conformidad de la clase resistente. Margen cómodo, pero no excesivo.

Rustam anota estos datos en la ficha KDP-001 en la sección "Material de entrada". Wahan los copia a la agenda; Rustam no le corrige, que aprenda a tomar notas.

### 7:15, decisión sobre la cinta

Rustam vuelve a la nave, se coloca frente al armario de cintas (estante metálico junto a la P3, 8 baldas, cada una con una cinta de repuesto en su rollo con papel protector). Recuerda de las l6 y l7: **el aserradero de cinta LT70 de EGIDA usa cintas de 38 × 1,07 mm**. El tipo de acero, el ángulo de ataque (*hook angle*), el paso de los dientes (*tooth pitch*) y el tipo de filo (estelita, aleación, temple) son variables.

Cintas posibles en el armario:

1. **Estelita 38/7-9** (acero con estelita, paso variable 7 y 9 TPI, ángulo de ataque 9°), nº de almacén ST-38-7/9-S12. **Típica para roble y haya dura**. Precio 380 zł netos.
2. **Aleación 38/7/8** (acero de aleación, paso 7/8 TPI fijo, ángulo de ataque 10°), nº ST-38-7/8-A12. **Universal pino-abeto**. Precio 145 zł netos.
3. **Aleación 38/10** (acero de aleación, paso 10 TPI fijo, ángulo 10°), nº ST-38-10-A12. Para **tablas finas** (menos de 20 mm de grosor), virutas más finas. Precio 165 zł netos.
4. **Aleación 38/22 rara** (paso 22 TPI, ángulo 13°, para **tronzar trozas de gran diámetro** y para madera congelada). Precio 175 zł netos. De la l6, usada para roble en situación de emergencia.
5. **Estelita 38/10** (acero con estelita, paso 10 TPI, ángulo 9°), nº ST-38-10-S12. Roble, tablas más gruesas. Precio 405 zł netos.
6. **Gastadas de varios afilados** (apartadas en un lugar separado, al final de su vida útil)

Rustam piensa en voz alta en polaco, Wahan escucha:

*"El encargo es pino fresco, 32% de humedad, grosor objetivo 28 mm en mojado. Para pino fresco elegimos acero de **aleación**, no estelita. La estelita cuesta 2,5 veces más y mantiene el filo más tiempo, pero en pino fresco la resina sella rápido la estelita, el desafilado es más rápido que en roble. En pino es mejor una cinta más barata de aleación, afilada con más frecuencia."*

*"El grosor de 28 mm es medio, no fino. Para tablas por encima de 22 mm el paso **7/8 TPI** es óptimo. El más fino (10 TPI) corta más despacio y hace demasiada viruta. Elijo la **aleación 38/7/8**, cinta número ST-38-7/8-A12."*

*"El ángulo de ataque de 10° es el estándar para pino. Para roble sería 9° (madera más dura, menor ángulo para que no se arranquen los dientes). Para pino congelado 13° (ángulo mayor, mejor entrada en la madera). Hoy es pino fresco de mayo, 10° va bien."*

Saca la cinta del armario, comprueba la etiqueta: ST-38-7/8-A12, proveedor Wood-Mizer Polska, fecha del último afilado **2026-05-20** (calentamiento del taller de afilado en las instalaciones de WM antes de la temporada), contador de cortes desde el afilado **0** (recién afilada). Perfecta.

En la KDP-001, sección "Selección de cinta":
```
Cinta: aleación 38 × 1,07 mm, paso 7/8 TPI, ángulo de ataque 10°
Nº de almacén: ST-38-7/8-A12
Contador tras afilado: 0 (recién afilada desde 2026-05-20)
Justificación: pino fresco 32%, tablas 28 mm, óptima aleación 7/8 TPI
```

### 7:22, tensión y guías

Rustam abre la cubierta lateral de la P3, sube la palanca del tensor a la posición SUELTO, retira la cinta anterior (la de Damian del viernes, aleación 38/7/8 con etiqueta de desgaste de 140 cortes, vuelve a la rotación de afilado), monta la nueva. Recorrido de la cinta entre las ruedas: tensión, ajuste de guías, alineación (alineación vertical).

La **tensión de la cinta** es un parámetro **dependiente del operador** (de la l6 M3 T2). El manómetro del Wood-Mizer LT70 muestra el valor en PSI (libras por pulgada cuadrada). Rango seguro para cintas de 38 mm: **2200-2400 PSI**. Elección dentro del rango:

- Madera dura (roble, haya, fresno), cinta de estelita: **2400 PSI** (máximo del rango). Mayor tensión mantiene la cinta más rígida en vertical, menos vibraciones en el corte, corte más limpio, pero mayor carga sobre la soldadura (riesgo de rotura) y sobre las ruedas de cinta.
- Madera blanda (pino, abeto), cinta de aleación: **2200 PSI** (límite inferior del rango). La cinta "respira", menor riesgo de rotura, menor carga sobre las ruedas. El corte queda mínimamente más sensible a los nudos pero de forma aceptable.
- Madera congelada o muy dura (roble congelado, exóticas): **2400 PSI** más observación cuidadosa del manómetro en los primeros 5 minutos de corte.

Hoy es pino fresco, aleación 7/8. Rustam ajusta **2200 PSI** (gira el volante del tensor cinco vueltas y media a la derecha, observa el manómetro subiendo). El manómetro se detiene en 2200, vibra ligeramente, pero no baja. Temperatura de la nave 18 °C, sin deriva de tensión. **OK**.

Las **guías de la cinta** (rodillos a ambos lados de la cinta, inferior y superior, regulan la posición lateral de la cinta y evitan que la cinta "flote" en el corte). Cada guía tiene un ajuste de **distancia respecto a la cinta**. Rango: **3-4 mm** (de la l6). Demasiado apretada (por debajo de 3 mm): la guía toca la cinta, se calienta, se desgasta rápido, genera vibraciones. Demasiado floja (por encima de 4 mm): la cinta "flota", corte ondulado.

Rustam ajusta con galgas de espesores de 3,5 mm (estándar de EGIDA, centro del rango). Cuatro puntos de ajuste (inferior y superior, izquierdo y derecho). Cada uno por turnos: la galga entra floja, pero sin holgura. Si entra demasiado floja, el mando de ajuste gira a la derecha 1/8 de vuelta. Si no entra en absoluto, gira a la izquierda 1/4 de vuelta. **Calibración 3 minutos, cuatro puntos OK**.

En la KDP-001, sección "Ajustes de la máquina":
```
Tensión de la cinta: 2200 PSI (límite inferior del rango para pino y aleación)
Guías de la cinta: 3,5 mm de holgura, cuatro puntos calibrados
Temperatura de la nave al inicio: 18 °C
```

### 7:30, velocidad de avance y esquema de corte

La **velocidad de avance** (*feed rate*) es la velocidad con la que el cabezal del aserradero se desplaza sobre el carril durante el corte. Se mide en pies por minuto (imperial Wood-Mizer) o metros por minuto. El panel de la LT70 de EGIDA la muestra en pies/min, Rustam la convierte mentalmente a m/min (1 pie = 0,305 m, es decir, 30 pies/min ≈ 9 m/min).

Rango de la LT70: **0-80 pies/min** (0-24 m/min). La elección depende de cuatro factores:

1. **Especie de madera**. Pino blando → rápido (30-40 pies/min). Roble duro → lento (10-20 pies/min). Haya → medio (15-25 pies/min).
2. **Humedad**. Madera fresca → más rápido (menor resistencia al corte). Seca → más lento (mayor resistencia, mayor calentamiento de la cinta).
3. **Grosor de corte**. Tablas gruesas (50+ mm) → más lento (más tiempo en la madera, más virutas). Finas (menos de 25 mm) → más rápido (menos material retirado).
4. **Diámetro de la troza**. Troza grande → más lento en el primer pase (corte por el mismo cogollo es el más difícil). Troza pequeña → más rápido.

Condiciones de hoy: pino fresco, grosor 28 mm, diámetro 32 cm. Recomendación Wood-Mizer en el DTR de la LT70, tabla 3.5: **30-35 pies/min** (9-10,5 m/min). Rustam elige **32 pies/min** como arranque (centro del rango). Corrección posible tras el primer corte (observación del corte, rectitud de la tabla, sonido del motor).

El **esquema de corte** (*sawing pattern*) es el orden de los cortes y la forma de girar la troza. Dos esquemas básicos para tablas de suelo de pino:

**Esquema A: corte por pieza cuadrada (*cant sawing*).** La troza reposa plana sobre la bancada de la máquina. El primer corte retira la *oblina* (costero): el borde redondeado con la corteza. Giro de 180°, el segundo corte retira la segunda *oblina*. Giro de 90°, el tercer corte retira la tercera *oblina*. Giro de 180°, el cuarto corte retira la cuarta *oblina*. Ahora tenemos una pieza cuadrada (**cant**, pieza cuadrada). De la pieza cortamos en paralelo tablas de 28 mm de grosor. **Ventajas**: simple, rápido (el operador no rota la troza a menudo), buen rendimiento para trozas medianas y grandes (30 cm +). **Inconvenientes**: cada tabla contiene la médula en el centro de la longitud, lo que baja la clase resistente (C24 exige máximo 25% de médula).

**Esquema B: corte por cuarterones con giro (*quarter sawing*).** La troza se corta verticalmente por la médula en dos mitades. Cada mitad se gira 90° y se corta verticalmente por el eje de la médula en cuartos. Los cuartos se cortan en paralelo en tablas. **Ventajas**: los anillos anuales quedan perpendiculares a la superficie de la tabla (mayor resistencia mecánica, mejor estabilidad dimensional, clase C24 + más fiable, a veces C30). **Inconvenientes**: más operaciones, más lento, menor rendimiento para trozas estrechas (por debajo de 30 cm la pérdida es grande), exige girar la troza.

Rustam piensa: *"El encargo exige C24. Clase segura, no C30 ni C16. El esquema A es más rápido y da C24 para pino silvestre al 32% de humedad sin problema. El esquema B sería mejor para C30 pero el encargo no lo exige, la carga de trabajo del operador sería el doble, el rendimiento un 5% peor. **Elijo A**, corte por pieza cuadrada estándar."*

En la KDP-001, sección "Parámetros de corte":
```
Velocidad de avance: 32 pies/min (centro del rango 30-35 para pino fresco 28 mm)
Esquema de corte: A (cant sawing, giro 4 veces, primer corte retira la oblina)
Grosor de tabla: 28 mm (+3 mm sobredimensión por secado y mecanizado hasta 25 mm objetivo)
Anchura de tabla: 155 mm (+5 mm sobredimensión hasta 150 mm objetivo)
Longitud de tabla: 4050 mm (+50 mm sobredimensión por recorte de testas hasta 4000 mm)
Estrategia de tandas: 4 costeros + 8-10 tablas por pieza (previstas 8 tablas de P1 y P2, 9-10 de P3 y P4)
```

### 7:38, última comprobación, arranque

Ficha KDP-001 rellenada, Rustam la pliega al formato A4 (un solo pliegue), la mete en un sobre de papel con la anotación "**ZLE-2026-05-077 P3 26.05 Rustam**", la deja en el escritorio del encargado en la esquina de la nave. Marek la recogerá después del turno.

En el panel de la P3: ajuste de la velocidad de avance a **32 pies/min** (potenciómetro del panel, escala 0-80, giro a la posición central entre 30 y 35). Altura del cabezal fijada: el primer corte retirará una *oblina* (costero) de 3-5 cm de grosor (depende de la conicidad de la troza, apreciación visual de Rustam).

Wahan está de pie junto al transportador auxiliar, tiene la tarea de recoger la *oblina* (costero) y las tablas de la plataforma de salida (el operador de la LT70 está solo en la plataforma principal). Entre ellos, comunicación visual y gestos breves (de M1 l1: "STOP" = palma plana en vertical, "adelante" = movimiento circular, "más despacio" = mano hacia abajo).

**7:40 motor arrancado**, 37 kW eléctrico, LED verde, LED naranja en modo *ready*, cinta iniciando revoluciones. 10 segundos de arranque hasta plena velocidad. 7:41 primer corte, troza 1, retirada de la primera *oblina*. Las tablas salen.

## Objetivos

Tras esta lección:

1. Conoces los **cinco parámetros de corte** que el operador independiente selecciona antes de iniciar un encargo en el aserradero de cinta: 1) **selección de la cinta** (tipo de acero estelita vs aleación, anchura 38 mm fija para la LT70, paso de dientes 7/8 vs 10 vs 22 TPI, ángulo de ataque 9-13°); 2) **tensión de la cinta** (2200-2400 PSI dentro del rango seguro, elección según la especie y el tipo de acero); 3) **guías de la cinta** (holgura 3-4 mm, cuatro puntos de ajuste); 4) **velocidad de avance** (0-80 pies/min, elección de 10-40 en la práctica, según especie, humedad, grosor de corte, diámetro de la troza); 5) **esquema de corte** (cant sawing A estándar o quarter sawing B para clases resistentes más altas). Entiendes que ninguno de estos parámetros figura en la orden de producción, todos son **decisión del operador**.
2. Entiendes **cómo la especie y la humedad influyen en la elección de la cinta y la tensión**. Pino y abeto frescos (hum. 25-35%) → aleación, tensión 2200 PSI. Pino y abeto secos (por debajo del 20%) → aleación con ángulo de ataque mayor o estelita, tensión 2300 PSI. Roble, haya, fresno duros → estelita, tensión 2400 PSI. Madera congelada (invierno, diciembre-febrero) → aleación con 22 TPI, tensión 2400 PSI. Entiendes que la **resina** del pino sella más rápido la estelita que la aleación, por eso la aleación se prefiere para pino fresco pese a su desafilado más rápido.
3. Conoces la **regla de selección de la velocidad de avance** en función de variables: especie (pino 30-40, haya 15-25, roble 10-20 pies/min como puntos de partida), humedad (corrección hasta un 10% más rápida para fresca, hasta un 10% más lenta para seca), grosor de corte (tablas por encima de 50 mm más despacio), diámetro de la troza (troza grande más lenta en el primer pase). Entiendes que la elección es un **arranque**, no el objetivo, y exige **corrección tras el primer corte** a partir de la observación del corte, la rectitud de la tabla y el sonido del motor.
4. Entiendes la **diferencia entre el esquema A (cant sawing) y el esquema B (quarter sawing)**. Esquema A: giro de la troza 4 veces, retirada de 4 costeros hasta formar un cuadrado, luego tablas en paralelo desde la pieza. Rápido, universal, bueno para C24. Esquema B: partir la troza en mitades por la médula, luego en cuartos, luego tablas en paralelo. Más lento, más caro en trabajo, mejor clase resistente (C30+), mejor estabilidad dimensional. Entiendes que la **elección de esquema depende de las exigencias de clase del encargo**, no de las preferencias del operador, y que intentar "subir más arriba" de lo que pide el cliente es malgastar el trabajo del operador.
5. Conoces la **ficha de selección de parámetros KDP-001** introducida en EGIDA en marzo de 2026. Formato A4, cuatro secciones: "Material de entrada" (dimensiones, humedad, defectos de las trozas), "Selección de cinta" (tipo, nº de almacén, contador tras afilado), "Ajustes de la máquina" (tensión, guías, temperatura de la nave), "Parámetros de corte" (velocidad de avance, esquema, grosores, longitudes). Se rellena **antes del primer corte**, copia al encargado al final del turno, retención de 2 años en papel más 5 años en escaneo en OneDrive. Base legal de la documentación: auditoría de calidad ISO 9001 (EGIDA está certificada), trazabilidad hacia atrás del encargo en caso de reclamación (l2 m3-w4), y **art. 211 pto. 7 del Código de Trabajo** (el trabajador está obligado a cooperar con el empleador en el cumplimiento de las obligaciones de SST).
6. Sabes **llevar a cabo la decisión paramétrica** en **30-40 minutos** antes del inicio del turno en un encargo concreto. Etapas: 1) lectura de la orden (5 min); 2) inspección del material en el almacén (10 min, mediciones de humedad, observación de defectos); 3) decisión sobre la cinta (5 min, selección del armario según especie y surtido); 4) montaje de la cinta, tensión, guías (10 min); 5) decisión sobre la velocidad de avance y el esquema (5 min, apunte en KDP-001); 6) arranque. Entiendes que **las prisas en esta ventana de 30-40 minutos generan errores que cuestan 2-4 horas** de corrección posterior o, en el caso extremo, una cinta rota y un coste de 150 zł más 40 minutos de sustitución de emergencia.

## Contenido

### 1. Qué parámetros elige el operador y cuáles son fijos

En el aserradero de cinta Wood-Mizer LT70 (ni en el Serra SM40, ni en ningún otro aserradero de cinta estacionario de EGIDA) no todos los parámetros son a elegir. Una parte se ajusta una sola vez en la instalación de la máquina y no se cambia nunca, una parte viene forzada por la construcción de la máquina (por ejemplo la anchura de la cinta), y una parte es fija para el encargo (la dimensión objetivo de la tabla viene indicada en la orden, no es decisión del operador).

**Parámetros fijos constructivos** (el operador no los cambia):
- Anchura de la cinta: **38 mm** (la LT70 usa esa anchura, la Serra también, P1-P3 todas de 38 mm)
- Grosor de la cinta: **1,07 mm** (estándar Wood-Mizer, otros grosores exigirían cambiar las ruedas guía)
- Potencia del motor: **37 kW** eléctrica para EGIDA, la LT70 también tiene versión de combustión de 48 kW, pero eso es decisión de compra, no del operador
- Rango de velocidad de avance: **0-80 pies/min** (límite físico del carril del mástil vertical y del motor de avance)
- Rango de tensión de la cinta: **2200-2400 PSI** seguro (el manómetro tiene rango 0-3000, pero por encima de 2400 PSI el riesgo de rotura de la soldadura crece exponencialmente)

**Parámetros impuestos por la orden** (el operador ejecuta, no decide):
- Especie de madera (del almacén, la elige el encargado al comprar en el distrito forestal)
- Clase resistente objetivo (C24, C30, C16, la indica el cliente)
- Dimensión objetivo de la tabla tras secado y mecanizado (encargo del cliente)
- Cantidad de tablas (del encargo)

**Parámetros de decisión del operador**:
1. Selección de la cinta del armario (tipo de acero, paso de dientes, ángulo de ataque)
2. Tensión de la cinta en el rango 2200-2400 PSI
3. Ajuste de guías (holgura 3-4 mm)
4. Velocidad de avance (10-40 pies/min habitualmente)
5. Esquema de corte (A cant vs B quarter)
6. Orden de las trozas del encargo (cuál primero, por qué)
7. Sobredimensiones de grosor de tabla (2-4 mm sobre la dimensión objetivo)
8. Momento de corrección de parámetros (tras el primer corte, tras los primeros 10 cm, tras la primera tabla)

Son ocho decisiones que el operador M3 toma por turno. El operador M2 (bajo supervisión) ejecuta los parámetros indicados por el encargado en la orden, el operador M1 (ayudante) ejecuta tareas de apoyo sin decisión paramétrica. La **autonomía paramétrica** es la diferencia clave de M3.

### 2. Selección de cinta por especie y surtido

De la l6 M3 T2 sabemos: la cinta de un aserradero de cinta tiene cuatro variables:

- **Tipo de acero**: aleación (*alloy steel*) vs estelita (acero con capa de estelita en los dientes). La aleación más barata, se afila con facilidad, se desafila más rápido en madera dura. La estelita mantiene el filo 3-5 veces más tiempo, pero cuesta 2,5 veces más y no soporta las resinas del pino.
- **Paso de los dientes** (*tooth pitch*, TPI, *teeth per inch*): 7 TPI = raro (tablas gruesas), 10 TPI = medio (tablas finas), 22 TPI = muy raro (diámetros grandes, madera congelada). Número de dientes por pulgada. Paso más raro = virutas más grandes = corte más rápido, tablas más gruesas. Paso más denso = virutas más pequeñas = corte más liso, tablas finas.
- **Ángulo de ataque** (*hook angle*): 9°, 10°, 13°. Ángulo menor (9°) = mordida menos agresiva, bueno para madera dura, menor riesgo de rotura de diente. Ángulo mayor (13°) = más agresivo, bueno para blanda o congelada, mayor rendimiento pero mayor carga sobre la cinta.
- **Tipo de afilado de los dientes**: rectificado normal del acero, rectificado más aplicación de estelita, temple por inducción. Para EGIDA, los dos primeros tipos en rotación.

**Tabla de selección de cinta para situaciones típicas en EGIDA** (compilación de Wood-Mizer DTR más experiencia de los encargados):

| Especie y estado | Surtido | Tipo de cinta | Paso | Ángulo | Etiqueta ejemplo |
|---|---|---|---|---|---|
| Pino fresco 25-35% | Tablas 22-32 mm | Aleación | 7/8 | 10° | ST-38-7/8-A12 |
| Pino fresco | Tablas 15-20 mm (finas) | Aleación | 10 | 10° | ST-38-10-A12 |
| Pino seco < 20% | Tablas 22-32 mm | Estelita | 9 | 9° | ST-38-9-S12 (sellado con resina más lento) |
| Roble fresco 30-40% | Tablas 22-32 mm | Estelita | 7/9 | 9° | ST-38-7/9-S12 (efectiva en roble fresco) |
| Roble seco 20-25% | Tablas 22-32 mm | Estelita | 9 | 9° | ST-38-9-S12 |
| Haya / fresno | Tablas 22-32 mm | Estelita | 7/9 | 9° | ST-38-7/9-S12 |
| Congelada (diciembre-febrero) | cualquiera | Aleación | 22 | 13° | ST-38-22-A12 |
| Gran diámetro (45+ cm) | Tablas gruesas 40+ mm | Aleación | 22 | 13° | ST-38-22-A12 |

Para el encargo de hoy (pino fresco 32%, tablas 28 mm) la primera fila: **aleación 7/8, ángulo 10°**. Rustam ha elegido ST-38-7/8-A12 del almacén. Correcto.

### 3. Tensión de la cinta, influencia profunda en el corte

La tensión de la cinta en un aserradero de cinta es la fuerza con la que las ruedas del aserradero tiran de la cinta en vertical. El manómetro de la LT70 marca en PSI (libras por pulgada cuadrada, 1 PSI ≈ 0,0069 MPa, 2200 PSI ≈ 15 MPa). Físicamente: la cinta es una cuerda de corte entre dos ruedas, la tensión la mantiene recta en el plano de corte. Poca tensión, la cinta "respira", flota en el corte, corte ondulado. Demasiada tensión, la soldadura de la cinta (el punto donde la cinta se soldó en bucle cerrado) queda sobrecargada, aumenta el riesgo de rotura, coste típico 145-200 zł por cinta más 40 minutos de sustitución.

**Rango seguro de la LT70**: **2200-2400 PSI**. El límite inferior de 2200 es el mínimo para un corte recto aceptable. El superior de 2400 es el límite por encima del cual el fabricante (Wood-Mizer) no garantiza la durabilidad de las soldaduras. En la práctica de EGIDA, la elección dentro del rango:

- **2200 PSI**: pino y abeto (blandos, resinosos), cinta de aleación, corte normal de verano.
- **2300 PSI**: madera mixta en el turno (mitad pino, mitad roble), compromiso.
- **2400 PSI**: roble, haya, fresno (duros), cinta de estelita, o madera congelada. Máximo.

**Qué cambia con cada 100 PSI al alza**:

- Corte más recto (menos "ola"), sobre todo en nudos y defectos internos
- La tabla sale más uniforme en grosor (menos +/-0,5 mm a lo largo de 4 m)
- Vibraciones de la cinta menores, sonido de corte más agudo y uniforme
- El desgaste de la soldadura de la cinta aumenta (vida media de la cinta 140-180 cortes a 2200 PSI, 110-140 cortes a 2400 PSI)
- La carga sobre los rodamientos de las ruedas aumenta (pero poco, por debajo del 1% de reducción de vida útil por cada 100 PSI)

Para el encargo de hoy (pino fresco, aleación, trabajo cómodo) **2200 PSI** es la elección estándar. Rustam así la ajustó. Para pino seco o mezcla de pino y alerce (que es más duro) consideraría 2300.

**Trampa frecuente de los principiantes**: "basta tensar más y el corte será mejor". No siempre, porque a veces un mejor corte lo da la corrección de la velocidad de avance (más despacio), no la tensión. Y una tensión por encima de 2400 PSI cuesta en cintas más a menudo de lo que aporta en calidad de corte.

::: info
**El manómetro de la LT70 no mide directamente los PSI en la cinta**, mide la presión del aceite hidráulico en el cilindro del tensor. La escala se calibra en la fabricación de la máquina (tabla de conversión presión hidráulica → PSI de cinta). La calibración es permanente, pero **la junta del cilindro** (la misma que la de l8) si gotea, el manómetro muestra un valor rebajado. Por eso en la KDP-001 anotamos el valor del manómetro junto con la fecha de la última calibración. El servicio Wood-Mizer Polska comprueba la calibración una vez al año (revisión B de l8).
:::

### 4. Guías de la cinta, detalle pequeño pero crítico

Las guías de la cinta son cuatro rodillos (inferiores y superiores, izquierdo y derecho) entre los que la cinta pasa antes del corte. Función: **mantener la cinta en un mismo plano**, no dejarla desviarse lateralmente bajo la presión del corte en la madera.

Cada guía se regula con un tornillo. La distancia del rodillo a la cinta se mide con galgas de espesores (instrumento universal de acero con un juego de láminas de distintos grosores, en EGIDA de 0,05 a 1,00 mm). Holgura estándar en la LT70: **3-4 mm**.

- **3 mm** (límite inferior): para madera dura, para cinta de estelita, mejor guiado, ligera pérdida por desgaste de guías (desafilado ~20% más rápido)
- **4 mm** (límite superior): para madera blanda, aleación, menor fricción, mayor vida útil de las guías
- **3,5 mm**: estándar de EGIDA para trabajo típico, compromiso

**Cuatro puntos de ajuste**: superior izquierdo, superior derecho, inferior izquierdo, inferior derecho. Cada uno se regula por separado. En teoría los cuatro deberían ser idénticos. En la práctica, desviación admisible **0,1 mm** (la galga de 0,1 mm entra en un punto, no entra en el vecino).

**Calibración como procedimiento del operador antes de cada turno** (si no hay sustitución de cinta):
1. Saca la galga del grosor recomendado (por ej. 3,5 mm).
2. Insértala entre el rodillo de la guía y la cinta. Debe entrar con ligera resistencia, pero sin forzar.
3. Si entra con demasiada facilidad (flojo) → mando de ajuste a la derecha 1/8 de vuelta, nuevo intento.
4. Si no entra en absoluto → mando a la izquierda 1/4 de vuelta, nuevo intento.
5. Cuatro puntos por turnos, tiempo total 3-5 minutos.

La falta de calibración de las guías es una de las tres causas más frecuentes de corte ondulado (las otras dos: tensión de cinta demasiado baja, velocidad de avance demasiado alta). El operador M1 y M2 no comprueba las guías (lo hace el operador independiente), pero mira por encima del hombro al operador M3 mientras lo hace.

### 5. Velocidad de avance, el parámetro más dinámico

La velocidad de avance es el único parámetro que **cambia en el transcurso del turno**. La cinta es la misma, la tensión es la misma, las guías son las mismas. Pero la velocidad la **corriges** a partir de la observación del corte.

**Arranque**: recomendación de Wood-Mizer del DTR (tabla 3.5 LT70) o experiencia de EGIDA. Para pino fresco 28 mm de tabla, como Rustam hoy: **32 pies/min** (centro del rango recomendado 30-35).

**Corrección tras el primer corte** (primera *oblina* retirada, Rustam observa la superficie de corte):

- Superficie **lisa y recta** (corte como una hoja de papel, sin ola) → velocidad OK, deja 32.
- Superficie con ligero **"escamado"** en la dirección del corte (pequeños picos cada 5-10 cm a lo largo) → velocidad **demasiado rápida**, reduce a 28-30 pies/min.
- Superficie **ondulada** (ola con amplitud de 1-2 mm cada 20-30 cm) → velocidad **muy excesiva**, pero la causa suele ser **cinta desafilada** o **tensión incorrecta**. Reduce a 22-25 pies/min, pero primero comprueba la cinta.
- Tabla **más gruesa por un extremo**, más fina por el otro (cuña) → la velocidad no es la causa, es la **alineación de la cinta** (ajuste de alineación de la cinta respecto a la bancada), tarea de servicio, notifícalo al encargado.
- Sonido del motor **irregular**, "ondulante" → velocidad **demasiado rápida**, el motor se acerca a la sobrecarga, reduce 3-5 pies/min.
- Sonido del motor **muy agudo, silbante** → velocidad **demasiado lenta** (el motor trabaja "flojo", la cinta no muerde la madera, energía desperdiciada), aumenta 3-5 pies/min.

Rustam enseña esta corrección a Wahan mediante **ejemplos con nombre**. Cada troza posterior es una oportunidad para cambiar la velocidad y Wahan aprende a escuchar el motor.

**Anotación en KDP-001** final (al terminar el turno, por la tarde), en el campo "Parámetros realmente aplicados":
```
Inicio de turno: 32 pies/min (pino fresco, aleación 7/8)
Troza 1: 32 p/min todo el tiempo, corte recto, OK
Troza 2: 32 p/min al inicio, tras los primeros 2 m reducido a 30 (ligero escamado), OK
Troza 3: 30 p/min al inicio (memoria de P2), todo el tiempo 30, OK
Troza 4: 30 p/min todo el tiempo, última tabla ligeramente "áspera" porque la cinta ya lleva 140 cortes, dentro de norma
```

Este es el documento de fuerza del encargado: ve que el operador no solo fijó el parámetro, sino que lo **siguió**.

### 6. Esquema de corte A (cant sawing), estándar

Esquema A, *cant sawing* (corte por pieza cuadrada, después en paralelo):

**Etapa 1**. La troza reposa horizontalmente sobre la bancada, la sección transversal de testa redonda visible por el frente de la máquina. Rustam arranca el avance, el cabezal avanza sobre el carril, la cinta retira la **primera *oblina*** (costero: protuberancia redondeada de la cara superior de la troza, normalmente 3-5 cm de grosor en el centro, más fina en los extremos). Estima el grosor del costero visualmente antes del arranque con el ajuste de altura del cabezal. Efecto: troza con la parte superior plana.

**Etapa 2**. Giro de la troza 180° (con ayuda del volteador hidráulico, *log turner*). La antigua parte superior ahora es inferior, la antigua inferior es superior. Rustam retira la **segunda *oblina***. Efecto: troza con dos caras planas opuestas, dos costeros originales a los lados izquierdo y derecho.

**Etapa 3**. Giro de la troza 90° (el mismo volteador). Uno de los dos costeros laterales queda ahora arriba. Rustam retira la **tercera *oblina***. Efecto: troza con tres caras planas.

**Etapa 4**. Giro de la troza 180°. El último costero (cuarto) arriba. Retirada. Efecto: **pieza cuadrada (*cant*)**, dimensiones próximas al cuadrado. Para pino de Ø 32 cm de diámetro, el cuadrado queda de unos 23 × 23 cm (lados con margen, pérdidas del 20-25% en los 4 costeros).

**Etapa 5 y siguientes**. De la pieza cuadrada Rustam corta en paralelo tablas de 28 mm de grosor. Contando: 23 cm / 28 mm = 8,2, es decir **8 tablas** limpias más una "media tabla" (resto de 15-20 mm), que va a leña o a mecanizado como listón. Ocho tablas de dimensiones 28 × 155 mm (anchura limitada por la sección de la pieza cuadrada) y longitud 4050 mm.

**Tiempo del esquema A completo para una troza de 32 cm y 4 m**: 4 costeros a ~35 segundos = 2 min 20 s, más 8 tablas a ~30 segundos (la tabla es más corta que la troza, igual de larga) = 4 min, más 4 giros a ~15 s = 1 min. Total **~7-8 minutos** desde el primer corte hasta la última tabla.

**Rendimiento típico** del esquema A para pino Ø 32 cm y 4 m: **8 tablas × 28 × 155 × 4050 mm = 0,141 m³** desde una troza de volumen **1,04 m³** (fuste crudo, cilindro π × 0,16² × 4 = 0,322 m³, con margen por conicidad contamos 1,04, pero a veces con menos precisión). Coeficiente de rendimiento: 40% con volumen bajo, 60% con métrica completa incluyendo costero. Las fórmulas varían en la literatura, EGIDA usa la simplificada "rendimiento = volumen de madera aserrada en bruto / volumen del fuste" y para pino silvestre en tablas de 28 mm espera **55-65%**.

### 7. Esquema de corte B (quarter sawing), para clase superior

Esquema B, *quarter sawing* (corte por cuarterones):

**Etapa 1**. La troza reposa horizontalmente, Rustam ajusta el primer corte de modo que la cinta pasa por el centro de la troza, por la médula. El corte recorre toda la longitud de la troza. Efecto: **troza en dos semicírculos** (forma rica de letra D).

**Etapa 2**. Un semicírculo se aparta (carro del ayudante), el otro se gira 90° respecto a la posición inicial (cara plana ahora abajo, redondeo arriba). Corte por el centro de este semicírculo, perpendicular al corte inicial. Efecto: **cuartos de troza** (forma de Y irregular).

**Etapa 3**. Cada cuarto se corta en paralelo en tablas, empezando por la cara recta interior (donde estaba la médula). Las tablas de los dos-tres primeros son **las mejores**: anillos anuales perpendiculares a la superficie de la tabla ("tablas cuarteadas"), resistencia mecánica máxima, estabilidad dimensional frente a cambios de humedad la más alta. Las tablas del cuarto cercano a la corteza son más débiles (anillos oblicuos), pero aún mejores que en el esquema A.

**Etapa 4**. Repite las etapas 2-3 para el segundo semicírculo.

**Tiempo para una troza de 32 cm y 4 m**: 1 corte divisor + 2 cortes de cuarterón + 8-10 tablas de 4 cuartos = **~12-15 minutos** (aprox. el doble que el esquema A).

**Rendimiento típico**: **45-55%** (peor que A por mayores pérdidas geométricas en forma de cuarto).

**Clase resistente**: **C24 segura, C30 probable** (en 3-4 tablas de 10 de cada troza).

**Cuándo elegir B**:
- El encargo exige C30 o C35 (cliente: "necesito tener una clase fiable C30 en elementos estructurales")
- El encargo exige alta estabilidad dimensional (muebles, parqués caros, carpintería de ventanas)
- El precio del surtido justifica el trabajo adicional (suelo de parqué de roble a 180 zł/m², merece la pena)

**Cuándo no**:
- Encargo C24 estándar (el ZLE-077 de hoy)
- Queda poca vida de la cinta (el esquema B desgasta la cinta más rápido, 15-20% de reducción de vida útil por troza)
- Presión de tiempo (encargo para mañana, no hay el doble de tiempo)

Rustam hoy ha elegido A. Wahan anotó en la agenda la pregunta: *"¿Cuándo B?"* para hablar después del turno.

### 8. Documentación de la decisión, ficha KDP-001

KDP-001 (Ficha de Selección de Parámetros, *Karta Doboru Parametrów*) es un formulario A4 introducido en EGIDA en marzo de 2026 tras la auditoría de calidad ISO 9001 de febrero (el auditor señaló que la **falta de rastro probatorio** de quién fijó qué parámetros en el encargo era un riesgo en caso de reclamación del cliente). Estructura de la ficha:

**Encabezado**: nº de encargo, fecha, operador, máquina, ayudante (si lo hay).

**Sección 1, Material de entrada**:
- Lista de trozas del almacén (nº de almacén, dimensiones, humedad, defectos visibles)
- Suma de volumen estimada
- Comentario sobre defectos críticos (si los hay, por ej. "P3 fenda radial 8 cm, precaución")

**Sección 2, Selección de cinta**:
- Tipo, anchura, grosor, paso, ángulo, nº de almacén
- Fecha del último afilado
- Contador de cortes desde el afilado (cero si recién afilada)
- Justificación de la elección (1-2 frases, por qué esta cinta)

**Sección 3, Ajustes de la máquina**:
- Tensión de la cinta (PSI, del manómetro)
- Guías (holgura en mm, si están calibradas)
- Temperatura de la nave (influye en la deriva de la tensión durante el turno)

**Sección 4, Parámetros de corte**:
- Velocidad de avance inicial (pies/min)
- Esquema de corte (A o B)
- Grosor de tabla (sobredimensión indicada)
- Anchura, longitud (sobredimensiones indicadas)
- Estrategia (cuántas tablas por troza se prevén)

**Sección 5, Parámetros realmente aplicados** (se rellena al final del turno):
- Cambio de velocidad (de qué a qué, cuándo, por qué)
- Cambio de tensión (si lo hubo)
- Sustitución de cinta durante el turno (si la hubo, por qué)
- Observaciones de defectos internos detectados

**Sección 6, Firma**:
- Nombre y apellido del operador, fecha, hora de fin de turno

**Retención**: **2 años papel** en la oficina del aserradero, **5 años escaneo electrónico** en el OneDrive de EGIDA (carpeta del encargo, acceso encargado + director). Pasados los 2 años el papel va a la destructora, el escaneo sigue.

**Uso del documento**:
1. **Reclamación del cliente** (tabla demasiado blanda, demasiado corta, rota a los 6 meses): el encargado abre la KDP, comprueba si el operador dio buenos parámetros. Si sí, la culpa es del material (proveedor Distrito Forestal Strzałowo) o del secado. Si no, la culpa es del operador (conversación correctiva, eventual formación).
2. **Auditoría FSC/PEFC** (m3-w4-l3): el auditor quiere ver el rastro de calidad del encargo, la KDP-001 es el primer documento de la cadena.
3. **Formación de un operador nuevo**: el director muestra KDP buenas ("así se rellena"), KDP malas ("así no se rellena, falta la justificación de la elección de cinta").
4. **Autoevaluación del operador**: a los 6 meses el operador tiene un fajo de 100-150 KDP propias, ve los patrones de sus decisiones, aprende de su propio trabajo.

::: warning
**Una entrada falsa en la KDP-001** se trata como una entrada falsa en el diario de trabajo. Remite al **art. 52 § 1 pto. 1 del Código de Trabajo** (infracción grave de las obligaciones), base para rescindir la relación laboral sin preaviso. EGIDA no ha tenido un suceso así, pero el director una vez al mes confronta de forma aleatoria las KDP con la realidad (pregunta al operador por detalles del encargo, observa el resultado del corte). La regla funciona en ambos sentidos: un apunte honesto es prueba para el operador de que trabajó bien, un mal apunte es prueba en su contra.
:::

### 9. Errores frecuentes de principiantes operadores M3

Compilación de los informes de los encargados de EGIDA de 2024-2025, defectos en la selección de parámetros en operadores que pasaron a M3 en el primer semestre de trabajo autónomo:

**Error 1. Selección de cinta por memoria del turno anterior**. "Ayer era roble, cogí estelita 7/9. Hoy es pino, cojo la misma estelita, porque está a mano." Resultado: la estelita en pino se sella con resina en 40 cortes (en lugar de 140 de la aleación), la cinta va al afilado tras un turno, coste 120 zł innecesarios más tiempo. **Correcto**: cada turno es una elección nueva, no un traslado automático. La KDP-001 fuerza esa reflexión.

**Error 2. Maximización de la tensión "por seguridad"**. "Pongo 2400 siempre, porque el corte es el mejor". Resultado: la cinta vive 110-140 cortes en lugar de 140-180, los costes de cintas en el presupuesto anual son un 25% más altos, la soldadura se rompe más a menudo en el corte (corte interrumpido, recogida por 145-200 zł adicionales). **Correcto**: tensión ajustada a la especie y al tipo de cinta, rango óptimo 2200-2300 PSI para la mayoría de encargos.

**Error 3. Velocidad de avance "ya rápido de entrada"**. "Más rápido significa que haré más, 40 pies/min desde el arranque". Resultado: la primera tabla ligeramente ondulada (corregir a 32 tras la primera troza supone perder 20 minutos y 2 tablas a C16 en lugar de C24), desgaste de cinta 15% más rápido, motor se calienta por encima de lo normal. **Correcto**: inicio con la recomendación Wood-Mizer DTR, corrección solo tras el primer corte y solo basada en observación.

**Error 4. Esquema B "por si acaso"**. "C24 está bien, pero haré B, porque las clases superiores son mejores, el cliente se alegrará". Resultado: trabajo el doble de largo, rendimiento 10% peor, el cliente paga igualmente por C24 no por C30 (porque no pidió C30), la economía del turno peor en un 30%. **Correcto**: exactamente lo que pide el cliente, no más. El encargado puede autorizar el esquema B solo en casos establecidos.

**Error 5. Falta de entrada en KDP-001 "porque hay poco tiempo"**. "La relleno por la tarde". Resultado: por la tarde el operador recuerda la mitad, los detalles de la cinta y las guías se confunden con el turno anterior, la KDP queda imprecisa. El auditor ISO lo señalará como no conformidad. **Correcto**: la KDP se rellena **antes del primer corte** (secciones 1-4), la sección 5 tras el turno.

**Error 6. Copia de la solución de un compañero sin comprender**. "Damian ajustó 30 pies/min ayer, cojo lo mismo". Resultado: Damian tenía pino seco al 18% (especie y humedad distintas), 30 pies/min era demasiado lento para pino fresco al 32%, la cinta resbala, efecto subóptimo. **Correcto**: cada encargo tiene sus parámetros, el parámetro comparativo es la KDP anterior **de condiciones similares**, no la última anotada.

### 10. Cuando la decisión paramétrica se le escapa al operador

No todo encargo está en la zona de confort del operador M3. Hay situaciones en las que el operador debe **preguntar al encargado** antes de decidir. Tres escenarios:

**Escenario A, especie desconocida**. Encargo de "madera exótica" (jatoba, meranti, iroko) que el operador ve por primera vez. Características de corte, resistencia, resinas, humedad final son desconocidas desde la experiencia. **Procedimiento**: el operador pregunta al encargado, que consulta con el servicio de Wood-Mizer (línea Polonia, tiempo de reacción 15-30 minutos), obtiene la recomendación de cinta y tensión, la decisión se anota en la KDP con la anotación "según consulta con WM Polska, 2026-05-... h. ...".

**Escenario B, diámetro de troza fuera del rango de la LT70**. La LT70 tiene diámetro máximo de corte **67 cm**, mínimo **10 cm**. Una troza de Ø 72 cm (raro, pero ha pasado que el distrito forestal destaca un pino grande) queda fuera de rango, el operador la redirige a otra estación (Serra SM40 tiene máximo 80 cm) o la troza va a seccionado (corte manual con motosierra en piezas más pequeñas antes de la LT70). No intenta encajarla "a pelo", porque se arriesga a dañar la máquina, romper la cinta, e incluso lesiones.

**Escenario C, humedad de la troza extrema**. Troza "seca como un hueso" (por debajo del 15%, raro en el almacén de EGIDA, pero una vez se dio con una balda olvidada de 2024) o "tras inundación" (45%+, hinchada, pesa el doble de lo que debería). Los parámetros normales de corte están descalibrados, la recomendación Wood-Mizer DTR no lo cubre. **Procedimiento**: el operador pregunta, el encargado decide, los documentos se anotan.

**Regla EGIDA**: en casos no estándar el operador independiente **siempre puede llamar al encargado antes de arrancar**. El encargado no se molesta por preguntas, al contrario, las prefiere a accidentes y reclamaciones. En la KDP-001 hay un campo "Consulta con encargado (sí/no, fecha, hora, persona)", así que anotamos explícitamente que el operador preguntó.

### 11. Primer día de la P3 tras el servicio, observaciones de respaldo

Ten en cuenta que hoy es el **primer día de la P3 tras el servicio del Sr. Krzysztof del jueves**. Cilindro de elevación del cabezal con junta sustituida, 400 ml de aceite hidráulico añadidos, todo probado bajo supervisión. Rustam tiene dos motivos de vigilancia adicional:

**Motivo 1. Manómetro**. El manómetro de la tensión de la cinta está asociado al cilindro del tensor, no al de elevación. Pero ambos cilindros están en el mismo sistema hidráulico (depósito común de aceite Shell TTF-SB, bomba común). Si el sistema hidráulico tras el servicio tiene una presión de trabajo mínimamente distinta a antes, el manómetro del tensor puede mostrar valores algo distintos. Rustam **comprueba la calibración del manómetro** girando el mando del tensor de SUELTO al rango pleno, observando la subida de 0 a 2200 PSI de forma fluida, sin saltos. **OK**, manómetro fluido, calibración aparentemente mantenida.

**Motivo 2. Fuga**. Ayer (viernes) Damian trabajó en la P3 tras el servicio, sin incidencia. El sábado la máquina estuvo fría, pudo aparecer condensado (cambio de temperatura día y noche). Rustam **antes del arranque comprueba el suelo bajo el cilindro de elevación**: ninguna mancha, ninguna humedad, seco. **OK**, el servicio aguanta.

Apunte en KDP-001, sección "Ajustes de la máquina", anotación:
```
P3 primer día tras servicio de WM Polska del 21.05 (Sr. Krzysztof).
Manómetro del tensor mantuvo calibración, arranque 0-2200 PSI fluido.
Bajo el cilindro de elevación seco, sin fuga desde el sábado.
Arranque del encargo ZLE-077, 7:40.
```

Esto no es un requisito formal, es un **buen hábito del operador independiente**. En caso de detectar una avería durante el turno, Rustam tendrá el rastro "tras el arranque estaba OK" como punto de referencia.

## Escena de cierre, 14:30, primeras tres trozas terminadas

Lunes 26-05-2026, 14:30 horas. Rustam y Wahan han cerrado **tres trozas de cuatro**: P1, P2, P3. La troza P4 en cola de corte, inicio 14:35, fin estimado 15:10, es decir, 10 minutos después de la hora formal de fin de turno (15:00). El encargado (Marek) lo ve y no hay problema, pagará los 10 minutos de hora extra a tarifa estándar.

### Balance de las tres trozas

**Troza 1**: retirados 4 costeros (3 min 40 s), retiradas 8 tablas de 28 × 155 mm (4 min 30 s), más 1 listón de resto de 18 × 155 mm (a leña). Total 8 tablas, **0,1412 m³** de madera aserrada en bruto. La primera y la última tabla de la pieza cuadrada contenían parte del costero (nudo resinoso a 80 cm, Rustam lo marcó para el clasificador). Rendimiento de la troza P1: **57%**.

**Troza 2**: Troza la mejor (sin defectos). Costeros 3 min 50 s, 9 tablas de 28 × 155 mm (5 min), resto de 12 × 155 mm (a leña). **9 tablas, 0,158 m³**. Rendimiento: **64%**. La mejor.

**Troza 3**: Troza con fenda radial de 8 cm en la cepa. Rustam orientó la fenda **hacia abajo** en la primera colocación (no hacia arriba, porque entonces quedaría en el costero, desperdicio). Tras retirar el cuarto costero la fenda se reveló en la pieza cuadrada como una marca de 8 cm de longitud en la esquina superior. Rustam corta 8 tablas, de las cuales **7** son limpias, la 8.ª contiene la fenda (queda clasificada como C16 en lugar de C24, bajada de calidad, pero aceptable para surtido de suelo). Total 8 tablas, **0,141 m³**. Rendimiento: **56%**.

**Suma tras tres trozas**: 25 tablas de **buena calidad** (surtido objetivo), 0,441 m³ de madera aserrada en bruto. Más 1 tabla C16 con fenda de P3 (tal vez vaya a listón de friso en lugar de suelo).

### Observaciones de parámetros

Velocidad de avance:
- Troza 1, arranque 32 pies/min, sin corrección, OK (corte recto).
- Troza 2, arranque 32, tras los primeros 2 m del cabezal ligero escamado en la superficie, Rustam reduce a 30 pies/min, resto de cortes OK. Decisión a partir de la observación de la superficie.
- Troza 3, arranque 30 (memoria de P2, el pino fresco se comporta de forma similar), todo el tiempo 30, OK. La ligera bajada de clase de la tabla 8.ª de P3 es defecto del material, no del parámetro.

Tensión de la cinta:
- 2200 PSI durante las tres trozas, sin corrección. El manómetro vibraba en el rango 2180-2220 (desviación admisible), no hubo necesidad de reajustar.

Guías:
- Calibradas por la mañana a 3,5 mm, al finalizar P2 Rustam hizo una prueba rápida con galga, la holgura aguanta (3,5-3,6 mm, deriva mínima).

Cinta:
- Aleación 38/7/8 ST-38-7/8-A12, contador tras 3 trozas = **~90 cortes** (costeros + tablas + giros por troza ~30 cortes, 3 trozas = 90). La cinta sigue fresca, para el turno de hoy es suficiente, sustitución no antes de 140-180 cortes, es decir, 2 trozas más que hoy (mañana martes troza 4 más otras 4 si continúa el encargo).

### Anotación en KDP-001, sección 5 (parámetros reales)

Rustam añade en la sección 5 de la ficha:

```
Parámetros realmente aplicados:
Troza 1: 32 p/min, sin corrección, 8 tablas C24, 0 defectos.
Troza 2: 32→30 p/min (tras 2 m de corte, escamado), 9 tablas C24, 0 defectos.
Troza 3: 30 p/min, 7 tablas C24 + 1 tabla C16 (fenda de material),
        marca para el clasificador.
Tensión: 2200 PSI estable, sin corrección.
Cinta: 38/7/8 aleación, tras 3 trozas contador ~90 cortes, estado bueno.
Estrategia de orden de trozas: P2 (la mejor) en segundo lugar,
        para estabilizar parámetros antes de P3 (con fenda).
```

### Reflexión de Rustam

Rustam conversa con Wahan tomando café en la pausa 14:35 antes de arrancar P4:

*"Wahan, ¿te has fijado en que en P2 cambié la velocidad tras 2 metros? Los primeros 2 metros iban bien, luego empecé a ver pequeños picos en la superficie de corte, cada 10 cm. ¿Lo conoces? Eso significa que la velocidad es demasiado alta, la cinta no llega a morder. Reduje, los pequeños picos desaparecieron. Corrección más rápida, más barata que una tabla estropeada."*

Wahan asiente. En la agenda tiene la nota: *"32 arranque pino → si picos, bajar a 30. Solo si son picos, no ola, porque ola es cinta o tensión."*

*"¿Por qué crees que empecé por P1, no por P2?"*

Wahan piensa un momento: *"Porque... ¿P1 era la primera en el almacén?"*

*"No. Porque P1 tiene nudo resinoso, y yo quería el primer corte con nudo, para comprobar cómo funcionan los parámetros en la variante más difícil. Si funcionan en lo difícil, funcionarán en lo fácil. Al revés no. **De lo difícil a lo fácil en el primer corte del turno**, luego a lo fácil al final. Eso se recuerda."*

Wahan apunta: *"Primera troza = la más difícil o la típica. No la más fácil, porque los parámetros engañarán."*

*"Y una cosa más. En la KDP-001 verás que en la sección 5 anoté por qué cambié la velocidad en P2. No solo 'cambié', sino 'cambié porque escamado'. Si alguien viene dentro de un año o dos y lo mira, verá no solo qué, sino también por qué. **Un parámetro sin justificación es magia. Un parámetro con justificación es conocimiento.**"*

### 15:10, troza 4 terminada, turno cerrado

Troza 4 (la más esbelta, sin defectos): 4 costeros 3 min 30 s, 8 tablas de 28 × 155 mm, resto de 6 × 155 mm a leña. **8 tablas, 0,141 m³**. Rendimiento: **61%**.

**Suma de cuatro trozas**: 33 tablas de surtido objetivo (32 C24 + 1 C16 con fenda), **0,582 m³** de madera aserrada en bruto. El encargo exigía 0,55 m³, por tanto **excedente del 5%**, bueno como búfer de secado (de esos 0,58 m³ tras secado y mecanizado quedarán ~0,49 m³, pedido del cliente 0,48 m³, excedente del 2%). **Encargo realizado conforme a las expectativas**.

Rustam retira la cinta (irá para mañana, en el almacén bajo funda), limpia el puesto con Wahan (10 minutos), rellena la KDP-001 definitivamente (sección 5 más firma más hora 15:18), pliega la ficha en el sobre, la deja en el escritorio del encargado.

Marek llegará por la tarde, la leerá, anotará sus observaciones en el expediente personal de Rustam (si las hay), la KDP irá a escanearse mañana por la mañana al OneDrive.

## Términos clave

**Selección de parámetros de corte** (*dobór parametrów cięcia*, EN *cutting parameter selection*, ES *selección de parámetros de corte*, UK *підбір параметрів різання*): proceso de decisión del operador independiente antes de iniciar un encargo, que abarca la elección de cinta, tensión, guías, velocidad de avance y esquema de corte a partir del material y del surtido objetivo.

**Ficha KDP-001** (*karta doboru parametrów*, EN *cutting parameter selection card*, ES *ficha de selección de parámetros de corte*, UK *картка підбору параметрів різання*): formulario EGIDA A4 que el operador rellena antes del primer corte del encargo, documenta todos los parámetros de decisión más los parámetros realmente aplicados tras el turno.

**Velocidad de avance** (*prędkość posuwu*, EN *feed rate*, ES *velocidad de avance*, UK *швидкість подачі*): velocidad con la que el cabezal del aserradero se desplaza sobre el carril durante el corte, medida en pies por minuto (Wood-Mizer DTR) o metros por minuto, rango LT70 0-80 pies/min.

**Tensión de la cinta** (*napięcie taśmy*, EN *blade tension*, ES *tensión de la cinta*, UK *натяг стрічки*): fuerza con la que las ruedas del aserradero estiran la cinta en vertical, medida en PSI (libras/pulgada²), rango seguro LT70 2200-2400 PSI.

**Guías de la cinta** (*prowadniki taśmy*, EN *blade guides*, ES *guías de la cinta*, UK *напрямні стрічки*): cuatro rodillos (inferiores y superiores, izquierdo y derecho) que mantienen la cinta en vertical durante el corte, regulados con galgas de espesores en el rango 3-4 mm.

**Esquema de corte A cant sawing** (*schemat cięcia do kwadratu*, EN *cant sawing pattern*, ES *corte por pieza cuadrada*, UK *схема різання до квадрата*): giro de la troza 4 veces, retirada de 4 costeros hasta la pieza cuadrada, corte paralelo de tablas desde la pieza. Rápido, universal, buen rendimiento.

**Esquema de corte B quarter sawing** (*schemat czwartowania*, EN *quarter sawing pattern*, ES *corte por cuarterones*, UK *схема четвертного різання*): partir la troza por la médula en mitades, cada una en cuartos, corte de tablas desde los cuartos. Más lento, mejor clase resistente (C30+) y estabilidad.

**Paso de los dientes TPI** (*podziałka zębów*, EN *tooth pitch TPI teeth per inch*, ES *paso de los dientes TPI*, UK *крок зубів TPI*): número de dientes de cinta por pulgada, habitualmente 7/8 TPI para pino, 7/9 TPI para roble, 10 TPI para tablas finas, 22 TPI para congelada o grandes diámetros.

**Ángulo de ataque** (*kąt natarcia*, EN *hook angle*, ES *ángulo de ataque*, UK *передній кут*): ángulo con el que el diente de la cinta "entra" en la madera, habitualmente 9° para madera dura, 10° para estándar, 13° para congelada.

**Estelita vs aleación** (*stal stellitowa vs stopowa*, EN *stellite vs alloy steel*, ES *acero estelita vs aleación*, UK *стелітова сталь vs сплавна*): dos tipos de filo de cinta, la estelita mantiene el filo 3-5× más tiempo, pero cuesta 2,5× más y no soporta las resinas del pino.

**Orden de producción** (*dyspozycja produkcyjna*, EN *production work order*, ES *orden de producción*, UK *виробничий наряд*): documento A5 emitido por el encargado, que contiene material, surtido objetivo, cantidad y fecha de ejecución, sin parámetros de corte (esos los elige el operador).

**Sobredimensión** (*naddatek*, EN *allowance / oversize*, ES *sobredimensión / margen*, UK *припуск*): diferencia entre la dimensión de corte en bruto y la objetivo tras secado y mecanizado, habitualmente 3 mm de grosor, 5 mm de anchura, 50 mm de longitud para tablas de suelo 25×150×4000.

**Rendimiento** (*uzysk / wydajność surowca*, EN *yield / lumber recovery*, ES *rendimiento / aprovechamiento*, UK *вихід / коефіцієнт виходу*): relación entre el volumen de madera aserrada en bruto y el volumen del fuste, para pino silvestre en tablas de 28 mm habitualmente 55-65%.

**Operador independiente M3** (*operator samodzielny*, EN *independent operator*, ES *operador independiente*, UK *самостійний оператор*): operador tras finalizar el módulo 3 del curso EGIDA, toma decisiones paramétricas en el encargo sin supervisión directa del encargado.

**Cant** (*blat prostokątny*, EN *cant*, ES *pieza cuadrada*, UK *брус / чотиригранний блок*): tablón rectangular o cuadrado formado tras retirar los 4 costeros en el esquema A, del cual se cortan en paralelo las tablas.

## Autoevaluación

### A. Parámetros del operador (preguntas de reconocimiento)

1. Enumera los **cinco parámetros de decisión del operador** en el aserradero de cinta LT70 que no figuran en la orden de producción.

2. El operador M1 (ayudante) ve una cinta de estelita 7/9 en el aserradero. ¿Es un parámetro del operador M3 (independiente) o un parámetro impuesto constructivamente? Justifica la respuesta.

3. ¿Qué significa la sigla **KDP-001** en la documentación de EGIDA? ¿Cuál es el objetivo de rellenar esa ficha antes del corte?

### B. Selección de cinta

4. Encargo: haya fresca al 30% de humedad, tablas 30 mm de grosor, clase C24. Selecciona la cinta entre las opciones: a) aleación 7/8 ángulo 10°, b) estelita 9 ángulo 9°, c) estelita 7/9 ángulo 9°, d) aleación 22 ángulo 13°. Justifica la elección en 2 frases.

5. ¿Por qué la estelita **no** es una buena cinta para pino fresco, aunque mantiene el filo más tiempo que la aleación? Da la causa física.

6. Tras el turno ves que la cinta que usaste en pino seco al 18% de humedad tiene, a los 80 cortes, la superficie de los dientes taponada con depósitos marrones. ¿Qué son esos depósitos y son un problema?

### C. Tensión y velocidad

7. Pones la tensión de la cinta a 2400 PSI para pino fresco por costumbre. ¿Qué tres consecuencias ves a lo largo de 2-3 turnos de trabajo?

8. La velocidad de avance durante el corte de la primera troza la arrancaste a 32 pies/min. Tras 2 metros ves un leve "escamado" en la superficie de corte. ¿Qué haces?
   a) aumentas la velocidad 5 p/min
   b) reduces la velocidad 5 p/min
   c) reduces la tensión
   d) sustituyes la cinta

9. En el panel de la LT70 ves que la velocidad de avance está fijada en 45 pies/min. El corte transcurre, oyes el motor trabajando "ondulante" (el sonido cambia de tono cada 2-3 segundos). ¿Qué significa y qué haces?

10. En la tabla DTR de Wood-Mizer para pino fresco y tabla de 28 mm la recomendación es 30-35 pies/min. ¿Por qué la recomendación es un **rango**, no un valor único?

### D. Esquema de corte

11. El encargo exige clase C24. El operador planea el esquema B (quarter sawing) "para asegurar la clase". El encargado lo rechaza y fija el esquema A. ¿Por qué tiene razón el encargado?

12. El encargo exige clase **C30** en elementos estructurales (pares de cubierta). Material: pino silvestre al 30% de humedad. ¿Qué esquema eliges y por qué?

13. Troza Ø 22 cm (más esbelta que la típica). El operador quiere usar el esquema B. ¿Por qué es una mala elección en términos de economía del encargo?

### E. KDP-001 y documentación

14. En la KDP-001, la sección 5 "Parámetros realmente aplicados" la rellenas al terminar el turno por la tarde. ¿Qué información **debe** anotar ahí el operador si cambió la velocidad de avance durante el turno?

15. El encargado encuentra en la KDP-001 de un operador dos entradas idénticas (velocidad 32, tensión 2200, esquema A) en encargos, uno de los cuales es pino fresco al 32% y el otro roble fresco al 35%. ¿Qué piensa el encargado y por qué?

16. Durante una auditoría ISO 9001 el auditor pregunta por una KDP-001 de hace 6 meses. ¿Dónde la busca: a) escritorio del operador, b) armario del encargado en la oficina, c) escaneo en OneDrive de EGIDA, d) no existe, tras 6 meses se tira? Elige y justifica.

### F. Escenarios de decisión

17. Escenario A de la lección: especie desconocida (jatoba). ¿Cómo actúas como operador M3 independiente? Tres pasos.

18. Escenario B de la lección: diámetro de troza 72 cm, fuera del rango LT70 (máx. 67 cm). ¿Qué tres opciones tienes, y cuál eliges y por qué?
