---
id: m2-w2-l2
blok: material
czas: 120
---

## Introducción

Martes, séptimo día de la segunda semana. Ayer Sofía entendió **qué significa el número 38%**. Hoy aprenderá **cómo obtener ese número de forma que sea verdadero**. Porque medir la humedad suena como «clava algo en la madera y lee el resultado». La realidad es más interesante: la misma tabla, medida en tres sitios, da tres resultados distintos, y todos son correctos a la vez. La pregunta es **qué resultado se convierte en tu decisión**.

A las 7:30 el capataz Marek pone dos instrumentos sobre la mesa. El primero es un higrómetro de resistencia **Brookhuis FMC** con dos electrodos clavables y pantalla digital. El segundo es un higrómetro capacitivo **Merlin HM8-WS25**, del tamaño de una polvera, sin electrodos, sólo con una placa redonda. Marek le entrega el primero: «Empieza por el de resistencia. Dentro de dos meses te daré el capacitivo para la madera de exportación, pero primero tienes que entender para qué sirven los dos electrodos y por qué siempre se mide en dos puntos».

Esta lección trata de **cómo sacar del higrómetro un valor en el que puedas confiar**, y de cómo reconocer las situaciones en las que incluso una medición bien hecha dice algo distinto de lo que piensas.

## Objetivos

Después de esta lección:

1. Entiendes el **principio del higrómetro de resistencia**: la resistencia eléctrica de la madera cae exponencialmente al aumentar la humedad (de miles de millones de Ω al 6% a miles de Ω al 30%).
2. Sabes **clavar los electrodos correctamente**: perpendiculares a las fibras, a 1/4 a 1/3 del grosor de la tabla, por los dos lados (cara superior e inferior), en dos puntos a lo largo de la pieza (testa y centro).
3. Entiendes el **gradiente de humedad** en tabla recién aserrada: testa seca (de 3 a 8 pp menos que el centro), núcleo húmedo, albura entre ambos. Sabes por qué la testa miente.
4. Conoces la **corrección por especie** y la **corrección por temperatura**: coeficientes integrados en higrómetros de mejor gama, correcciones manuales en los más sencillos (tabla del manual, no «a ojo»).
5. Conoces los **límites físicos** de la medición por resistencia: rango fiable del 6 al 30% MC; bajo 6% la señal es inestable, sobre 30% la resistencia es tan pequeña que la electrónica se «cae».
6. Sabes **cuándo usar el higrómetro capacitivo**: madera aserrada de exportación clase A (sin agujeros), tablas para chapa, parqué con suelo radiante. El capacitivo mide en una capa de 20 a 30 mm desde la superficie, mientras que el de resistencia mide en el punto de clavado (en profundidad).
7. Sabes **anotar la medición** para que el capataz y el turno siguiente sepan: número de tronco/tabla, especie, lugar, resultado %, fecha, hora y tu firma.

## Contenido

### Cómo ve el agua un higrómetro de resistencia

El principio es sencillo, aunque las cifras sean grandes. **La madera seca es prácticamente un aislante**: una tabla de roble al 6% de humedad tiene una resistencia entre los dos electrodos del orden de 10⁹ a 10¹⁰ ohmios (miles de millones). **La madera húmeda es un conductor**: esa misma tabla al 30% tiene una resistencia de 10³ a 10⁴ ohmios (miles). La diferencia es de seis órdenes de magnitud: como comparar un grano de arena con un camión.

El higrómetro envía por los electrodos una pequeña corriente de prueba (del orden del microamperio), mide la resistencia y la convierte en porcentaje de humedad **a partir de la calibración para haya a 20°C** (es el estándar industrial recogido en la PN-EN 13183-2). Todas las demás especies y temperaturas requieren corrección, y de eso hablaremos enseguida.

::: info
**¿Por qué precisamente haya?** Porque tiene propiedades eléctricas intermedias entre el pino (blando, resinoso) y el roble (duro, ácido). Los fabricantes la eligieron como punto de referencia para que las correcciones en ambos sentidos fueran pequeñas. Pero eso significa que **para el pino hay que restar al valor leído ~1 a 2%, y para el roble añadir ~1%**. Los higrómetros de mejor gama tienen un selector de especies (de 15 a 30 especies integradas) y lo hacen automáticamente.
:::

### Electrodos: cuáles, a qué profundidad, en qué dirección

El Brookhuis FMC que Sofía sostiene tiene dos **electrodos clavables** (aislados en la parte cercana al mango, sin aislamiento en la punta). El aislamiento tiene sentido: sin él la corriente pasaría por la capa superficial (siempre más húmeda o más seca que el interior), falseando la medición.

**Profundidad de clavado**: para una tabla de 50 mm de grosor los electrodos se clavan a **12 a 17 mm** (1/4 a 1/3 del grosor). Para una tabla de 25 mm, a 6 a 8 mm. Para un escuadrón grueso de 100 mm, a 25 a 30 mm. Regla: **la punta del electrodo debe quedar en el núcleo de la tabla, no en la capa superficial**.

**Dirección**: los electrodos se clavan **perpendicularmente a la dirección de las fibras**, nunca en paralelo. ¿Por qué? Porque a lo largo de las fibras la resistencia es de 2 a 3 veces menor (el agua «fluye» más fácilmente a lo largo de los tubos leñosos que transversalmente), y el resultado quedaría sobreestimado en 3 a 5 puntos porcentuales.

::: warning
**Trampas del primer día**:
- **Demasiado superficial**: mides la capa superficial, no la madera. En verano, una tabla al sol tiene una costra seca de 2 a 3 mm y un núcleo húmedo. Una lectura a 5 mm puede mostrar 14% mientras que la humedad real de esa tabla es del 28%.
- **Demasiado profundo con la punta desafilada**: el electrodo se dobla, el contacto se vuelve inseguro, las lecturas saltan. Cambio de puntas cada 200 a 300 mediciones (las llamadas «agujas de repuesto» incluidas en el maletín del higrómetro).
- **Clavado en un nudo o en una fisura**: el nudo tiene una humedad distinta a la madera sana, la fisura conduce aire (aislante). Elige un sitio limpio, a 3 a 5 cm del nudo.
- **Sujetar el mango con la mano desnuda**: con madera muy húmeda (>80%), tu piel crea un camino paralelo para la corriente y el resultado sale subestimado. Para mediciones de verificación de cara a exportación, usa un higrómetro con mango aislado y guantes de algodón.
:::

### Por qué por los dos lados de la tabla: el gradiente de humedad

Aquí empieza el oficio. Sofía coge una tabla de pino de 50 mm de grosor, recién salida de la sierra y aún caliente. Mide por la cara superior: **36%**. Da la vuelta a la tabla y mide por la cara inferior: **41%**. ¿Qué valor es el verdadero?

**Ambos son verdaderos. La tabla tiene un gradiente de humedad.**

En la madera recién cortada y aún sin secar, el agua está repartida de forma desigual:
- **Núcleo** (centro del grosor de la tabla): humedad más alta, a menudo **3 a 8 puntos porcentuales** por encima de las capas exteriores.
- **Albura exterior** (superficie y 5 a 10 mm hacia el interior): humedad más baja, porque el agua se evapora antes por la superficie.
- **Cara apoyada en el suelo o en el listón separador**: más húmeda, porque el agua gravita hacia abajo y no se evapora tan rápido como por arriba.

**Regla**: mides **por arriba y por abajo** y tomas la media. Si la diferencia supera 5 puntos porcentuales (en el ejemplo de Sofía: 36% frente a 41%, diferencia de 5), lo apuntas como «gradiente alto» y lo comunicas al capataz. Es una señal de que la tabla necesita estacionarse y **no debe entrar directamente en el secadero de cámara** (porque se rajaría por diferencia de tensiones).

### Por qué en dos puntos a lo largo: testas frente al centro

La madera pierde agua por todas sus caras, pero **las testas (las secciones transversales)** se deshacen del agua **de 10 a 12 veces más rápido** que los cantos y las caras. La razón es anatómica: los vasos y los tubos leñosos están abiertos en la testa y cerrados (o al menos muy obstruidos) en los laterales.

**Consecuencia práctica**: si mides la humedad **a 20 cm de la testa**, obtendrás un resultado **2 a 6 puntos porcentuales menor** que en el centro de la tabla. Para una tabla de 4 m de longitud:
- Medición a 20 cm de la testa: 24%
- Medición en el centro (a 2 m): 29%
- Medición a 20 cm de la otra testa: 23%

Media: 25,3%, **pero la decisión comercial la tomas a partir del valor central (29%)**, porque es el que representa el estado real de la madera. Las testas son un «escaparate publicitario»: se ven bien y dicen poco.

::: tip
**Regla de los 20 cm**: **nunca midas a menos de 20 cm del extremo de la tabla**. Si tienes que medir una tabla corta (<1 m), mide justo en el centro y anota que era corta, porque la exactitud es entonces menor.
:::

### Corrección por especie y corrección por temperatura

Un higrómetro moderno (Brookhuis, Exotek, Delmhorst) tiene integradas **de 30 a 50 curvas de especie**: eliges «pino» en el menú y el aparato corrige automáticamente la resistencia según la calibración de pino. Los equipos más antiguos (o los más baratos, de hasta 500 zł) sólo tienen calibración de haya, y entonces usas una **tabla de correcciones** del manual de instrucciones.

::: example
**Tabla de correcciones (valores promediados, aproximados):**

| Especie | Corrección para una lectura del 15% |
|---|---|
| Pino | –1,5% (lectura 15% → real 13,5%) |
| Abeto (picea) | –1,0% |
| Haya (patrón) | 0% |
| Roble | +1,0% (lectura 15% → real 16%) |
| Alerce | –0,5% |
| Abedul | +0,5% |
:::

La **corrección por temperatura** es la segunda dimensión. La calibración es a 20°C. En invierno, con una nave a 0 a 5°C, **la madera tiene mayor resistencia a la misma humedad, y el higrómetro muestra un valor menor que el real**: hay que añadir de 1 a 3 puntos porcentuales. En verano, a 30°C, la resistencia es menor y hay que restar de 1 a 2 puntos. Los aparatos de mejor gama tienen sensor de temperatura y lo hacen automáticamente; en los más baratos usas una tabla.

Sofía trabaja en una nave calentada a 16°C. La corrección por temperatura es pequeña (–0,5 pp). La corrección por especie para el pino: –1,5 pp. Su lectura bruta de 38%, una vez aplicadas las correcciones: **~36%**. Sigue siendo madera fresca, sigue estando por encima del PSF, la decisión comercial no cambia, pero ahora Sofía sabe que ese número es verdadero.

### Límite físico de la medición por resistencia: cuándo echar mano del capacitivo

El higrómetro de resistencia funciona de forma fiable en el rango de **6 a 30% MC**. Fuera de ese rango:

- **Por debajo del 6%**: la resistencia crece tanto (>10¹¹ Ω) que la electrónica del medidor pierde precisión. Las lecturas «saltan» entre 4% y 8% en la misma medición. Para madera sobresecada (5 a 7%, por ejemplo parqué con calefacción por suelo radiante) se usa un higrómetro de laboratorio con secado de la probeta en estufa (*oven-dry method*, PN-EN 13183-1).
- **Por encima del 30%**: la resistencia cae tanto que el higrómetro muestra «30%» para todo lo que esté entre el 30% y el 100%. La madera fresca (50 a 90%) medida con higrómetro de resistencia sólo da la información «húmeda», sin dato concreto. Para precisión por encima del 30% se usa el método gravimétrico (pesar húmedo, secar, pesar seco, calcular: 24 horas).

El **higrómetro capacitivo (sin clavos)** funciona según otro principio: mide la capacidad eléctrica de la madera (que depende de la constante dieléctrica, que a su vez crece con la humedad). Apoyas la placa redonda sobre la superficie de la tabla, la presionas y lees. No deja agujeros de electrodos, algo crítico para la madera aserrada de exportación clase A, las chapas y los parqués de exposición.

::: info
**Diferencias prácticas entre el de resistencia y el capacitivo**:
- **De resistencia**: mide en un punto (donde están las puntas de los electrodos), en profundidad (a la profundidad de clavado), con exactitud (±0,5 pp tras las correcciones). Deja agujeros.
- **Capacitivo**: mide en una capa superficial de hasta 20 a 30 mm de profundidad, promedia un área de unos 10×10 cm, con una imprecisión de ±1 a 2 pp. No deja agujeros.

**Para el trabajo diario de un operador júnior**: usas el de resistencia. El capacitivo lo recibirás cuando asciendas y tengas que medir madera de cliente premium.
:::

### Cómo anotar la medición para que tenga sentido

Un número en el cuaderno sin contexto no vale nada. Registro estándar:

::: example
**Tronco 14, pino, entrega 04.04, medición 11.04 07:45 – Sofía**
- Posición A (testa inferior, a 20 cm del extremo, cara superior): 32%
- Posición B (centro de la pieza, cara superior): 38%
- Posición C (centro de la pieza, cara inferior): 41%
- Posición D (testa superior, a 20 cm del extremo, cara superior): 33%
- **Valor representativo (media B+C): 39,5% → tras correcciones ~37%**
- Observación: gradiente arriba/abajo 3 pp, gradiente testa/centro 5 pp, material fresco, NO enviar al secadero de cámara antes de 2 semanas de estacionamiento.
- Firma: M. Santos
:::

Sofía copia estos datos al libro de mediciones y lo firma. Es un **documento interno** y vuelve a aparecer en m2-w4-l5 (documentación del puesto). Sin firma no tiene valor. Con firma se convierte en parte de la trazabilidad: si la tabla sale al cliente y vuelve con reclamación del tipo «estaba demasiado húmeda», el libro demuestra que el aserradero lo sabía y decidió conscientemente.

## Términos clave

| Termin polski | English | Español | Українська |
|---|---|---|---|
| Wilgotnościomierz oporowy | Resistance moisture meter | Higrómetro de resistencia | Опірний вологомір |
| Elektrody pomiarowe | Measurement electrodes | Electrodos de medición | Вимірювальні електроди |
| Gradient wilgotności | Moisture gradient | Gradiente de humedad | Градієнт вологості |
| Poprawka gatunkowa | Species correction | Corrección por especie | Видова поправка |
| Poprawka temperaturowa | Temperature correction | Corrección por temperatura | Температурна поправка |
| Wilgotnościomierz pojemnościowy | Capacitive (pinless) moisture meter | Higrómetro capacitivo (sin clavos) | Ємнісний (безконтактний) вологомір |
| Zeszyt pomiarowy | Measurement logbook | Libro de mediciones | Журнал вимірювань |

## Autoevaluación

1. Clavas los electrodos en una tabla de roble de 50 mm de grosor. ¿A qué profundidad tienes que clavarlos? ¿Qué dirección respecto a las fibras?
2. Tienes una tabla de 4 m de longitud. ¿Dónde medirás la humedad para que el resultado sea representativo: a 20 cm de la testa, en el centro, en ambos sitios? ¿Por qué?
3. Lectura bruta del higrómetro del 22% para pino en una nave a 5°C. ¿Cuál es el nivel real de humedad tras aplicar la corrección por especie (–1,5 pp) y la corrección por temperatura (+2 pp)?
4. ¿Por qué no mides con el de resistencia la madera fresca del 50 al 80%? ¿Qué obtendrás si lo intentas?
5. El capataz te pide medir madera aserrada de exportación de roble clase A lista para expedir. ¿Usas el de resistencia o el capacitivo? ¿Por qué?

## Vínculo con la práctica

Mañana (lección 3) conocerás la **manipulación de la troza larga**: por qué todo el tronco se divide en trozas de distinta calidad (base, centro, cima) y dónde traza el capataz las marcas de corte. Antes, hoy:

- **Pide al capataz el higrómetro después del turno**, mide tres tablas distintas (una fresca, una estacionada, una de exportación) y anota los resultados en el cuaderno.
- **Compara la medición por arriba y por abajo**: ¿ves gradiente? ¿De qué tamaño?
- **Revisa la tabla de correcciones por especie** en el manual de vuestro higrómetro, comprueba si están las especies con las que trabajáis (pino, abeto, roble, haya).
- **Grábate en la memoria**: siempre por los dos lados, siempre en dos puntos, siempre con firma.

## Notas para el formador

**Analogía conductora**: medir con un higrómetro es como medir la tensión arterial en el médico. Una sola medición, en un brazo, con prisas y tras un café, no vale nada. Tres mediciones espaciadas, en calma, en ambos brazos, dan el cuadro real. La madera también tiene «brazos» (arriba y abajo) y un «pulso» (el gradiente). Funciona con alumnos de cualquier nacionalidad porque todos saben qué es la tensión.

**Práctica en la nave**: esta lección requiere contacto físico con el higrómetro. Si tienes un solo aparato para 6 alumnos, rotación de 10 minutos por cabeza midiendo la misma tabla: enseña cómo manos distintas dan lecturas ligeramente distintas (±0,3 pp, dentro del margen de error). Si no hay aparato físico, visualización con el PDF del manual del Brookhuis FMC o del Delmhorst RDM-3 desde YouTube.

**Dónde vuelve esta lección**: m2-w4-l1 planificación de corte (humedad como parámetro para elegir la cinta de sierra), m2-w4-l5 documentación (libro de mediciones), m3-w1-l1 secado en cámara (medición como base de la decisión de secado), m3-w2-l5 reclamaciones (libro de mediciones como prueba de diligencia).

**Trampas de los alumnos migrantes**:
- «Una medición basta, si el número es digital»: **no**, la cifra es una ilusión de precisión. Haz cuatro mediciones y calcula la media.
- Clavar los electrodos en un nudo (porque es el punto visualmente más marcado de la tabla): enseña con el dedo que el nudo no es madera, es una entidad aparte.
- Confundir el gradiente con un error de medición: una diferencia de 3 a 5 pp es información, no un defecto. El capataz quiere verla.
- Anotar el resultado sin firmarlo, «total, nadie lo va a revisar»: sí, lo revisará si hay reclamación. La firma es profesionalidad.

**Caso Sofía, para ampliar**: ¿por qué el capataz le da primero el de resistencia y el capacitivo sólo dentro de dos meses? Porque el de resistencia obliga a pensar en la estructura de la madera (gradiente, profundidad), mientras que el capacitivo da un «número cómodo» y el alumno puede no entender por qué está en ese sitio concreto. Orden didáctico, no económico.

**Glosario fonético PL**: «wilgotnościomierz» es una de las palabras sectoriales más largas del polaco. Acepta las abreviaturas «miernik», «przyrząd», «higrometr» (en diccionario, higrometr es más amplio y abarca también el aire). En materiales impresos queda el nombre completo. En la nave, abreviar es normal.
