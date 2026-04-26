---
id: m2-w1-l3
blok: bezpieczenstwo
czas: 120
---

## Introducción

Tercer día de Andrij como operador. Entra a la nave vestido como operador (la lección 2 se le quedó en la cabeza), se acerca a la sierra de cinta y pone la mano sobre el botón verde de START. El capataz lo detiene con una palabra: **„Primero STOP."**

Andrij lo mira desorientado. Quiere **arrancar** la máquina, no pararla. El capataz le gira la mano y le muestra el pulsador tipo seta, rojo sobre amarillo, a 30 cm a la izquierda del START verde. **„Antes de pulsar START, comprueba que el STOP funciona y está a tu alcance. Si no sabes dónde está el STOP, no toques el START."**

Esta lección explica por qué en cualquier máquina de madera el sistema de parada **tiene prioridad** sobre el de arranque. Por qué la seta es roja sobre amarillo. Por qué en un taller con tres puestos de sierra ves **seis setas**, y no tres. Y por qué la prueba diaria del STOP no es paranoia del capataz, sino exigencia del Rozp. MG 2000 (Reglamento del Ministerio de Economía de Polonia de 14 de abril de 2000 sobre SSL en la operación de máquinas para madera).

Primera regla: **tu mano vuelve al STOP antes de que la otra toque el START**. Así trabajarás en 2026, en 2036 y el último día antes de la jubilación.

## Objetivos

Después de esta lección:

1. Entiendes el principio fail-safe: en cualquier máquina de madera el STOP tiene prioridad sobre el START. Esta jerarquía resulta de la construcción, la norma y la ley, no de la elección del operador.
2. Reconoces el pulsador de emergencia según PN-EN ISO 13850: rojo, fondo amarillo, forma de seta (fácil de golpear con la palma o el codo), con autoenclavamiento.
3. Conoces las tres categorías de parada (0, 1, 2) y sabes cuál corresponde a la sierra de cinta, la sierra circular y la fresadora.
4. Localizas todos los pulsadores de emergencia del puesto desde cualquier posición (alcance <1 metro) y sabes señalar las cuatro trampas que invalidan un E-stop.
5. Realizas la prueba funcional diaria del E-stop antes de empezar a trabajar y sabes cómo reportarla al capataz.

## Contenido

### Principio fail-safe: STOP > START

**Fail-safe** es un principio de construcción según el cual un fallo del sistema **detiene** la máquina, no la arranca. Se aplica desde los años 60 en aviación y desde los 80 en la industria de la madera. Recogido en la legislación polaca en el **Reglamento del Ministro de Economía del 14 de abril de 2000**, § 7 apdo. 1:

> *„Las máquinas para madera deben estar equipadas con dispositivos de mando que aseguren su parada inmediata en situación de peligro. Estos dispositivos deben ser fácilmente accesibles desde cada puesto de operación."*

En la práctica, esto significa tres reglas constructivas:

- **El STOP es más fuerte que el START**. Si pulsas los dos a la vez, la máquina se para.
- **El STOP funciona incluso con un fallo de alimentación**. La seta desconecta el circuito mecánicamente, con independencia del PLC.
- **El STOP es pasivo en reposo**. Hay que pulsarlo una vez (parada), y luego **girarlo y extraerlo** (reinicio). El desbloqueo espontáneo queda descartado.

::: info
**Historia del principio**: en los años 70 del siglo XX, en los talleres de madera se usaba un único botón START-STOP (un interruptor, dos posiciones). Tras una serie de amputaciones en la RDA y en Finlandia, la norma EN 418 (1993) obligó a **separar los circuitos**. Implementación polaca: PN-EN 418 (1999), después PN-EN ISO 13850 (2015).
:::

### El pulsador tipo seta: rojo sobre amarillo

La norma **PN-EN ISO 13850:2015** describe el pulsador de emergencia (E-stop) con precisión:

- **Color del pulsador**: rojo.
- **Color del fondo bajo el pulsador**: amarillo.
- **Forma**: de seta (cabeza de champiñón), diámetro 40-60 mm, sobresaliendo 15-20 mm del plano.
- **Mecanismo**: al pulsar se enclava, el desbloqueo se hace por **giro a la derecha** (llave, pestillo, a veces tirando).

¿Por qué rojo sobre fondo amarillo, y no rojo sobre un panel gris? Contraste. El ojo del operador en las condiciones de un aserradero (iluminación 300-500 lux, polvo 2-10 mg/m³) reconoce el rojo sobre amarillo **en 0,2 segundos**, el rojo sobre gris **en 0,5-0,8 segundos**. Tres veces más rápido. Esa es la diferencia entre „mano en el STOP antes de que la tabla golpee" y „la tabla golpeó, la mano va en camino".

::: warning
**Cuidado con las falsificaciones**: las sierras baratas de hipermercados tienen a veces un „e-stop" rojo sobre panel negro, sin fondo amarillo, sin autoenclavamiento (muelle que rebota al soltar). **Eso no es un E-stop en el sentido de PN-EN ISO 13850**. Repórtalo al capataz y no arranques la máquina.
:::

### Tres categorías de parada

La norma **PN-EN 60204-1** (seguridad de las máquinas, equipamiento eléctrico) define tres categorías de parada:

**Categoría 0**: corte inmediato de la alimentación del motor. La máquina **se para por inercia** (es decir, sigue girando gracias a la inercia hasta que el rozamiento la detiene). Una sierra circular con motor de 4 kW tiene un tiempo de inercia de **8-15 segundos**. Una sierra de cinta con volante de inercia: **20-30 segundos**. Durante ese tiempo la hoja **sigue siendo peligrosa**.

**Categoría 1**: parada controlada con freno. El motor recibe una señal de frenado y la hoja se detiene en **3-8 segundos**. Estándar en sierras circulares nuevas en la UE (exigido desde 2006, Directiva de máquinas 2006/42/CE).

**Categoría 2**: parada controlada manteniendo la alimentación (la máquina „vela", lista para reanudar). Se usa pocas veces, sobre todo en líneas automáticas industriales.

**Qué significa esto para el operador**: la categoría 0 es una **máquina vieja**. La categoría 1 es una **máquina nueva con freno**. Con categoría 0 **no te acerques a la hoja durante 30 segundos** después de pulsar STOP. Contar en voz alta („mil uno, mil dos…") no es una manía del capataz, es **protección de los dedos**.

::: example
**Caso de un aserradero polaco (Opolskie, 2022)**: un operador de una sierra de cinta de 2001 (categoría 0) pulsó STOP, vio un taco entre las guías y fue a cogerlo **a los 12 segundos**. El volante seguía girando. Amputación del dedo índice. Conclusión de la PIP (Inspección de Trabajo polaca): máquina en orden, el operador omitió el tiempo de inercia. Recomendación: **modernización a categoría 1 con freno**.
:::

### Ubicación y el ritual „mano en STOP"

El Rozp. MG 2000 § 7 apdo. 2 exige que el pulsador de emergencia sea **„fácilmente accesible desde cada puesto de operación"**. En una sierra de cinta con dos operadores (alimentador + recibidor) esto significa **dos pulsadores tipo seta**: uno en cada puesto, cada uno al alcance de una mano (<1 metro).

El ritual que se convierte en hábito tras un mes de trabajo:

1. **Al acercarte a la máquina**: localiza la seta con la vista. Comprueba el color (rojo sobre amarillo), la forma (que sobresalga), el estado (sin marcas de golpes, sin virutas pegadas).
2. **Antes de arrancar**: pon la mano izquierda sobre la seta. Solo entonces la mano derecha va al START.
3. **Durante el corte**: la mano izquierda **no se sale del alcance de la seta**. Empuja la madera, pero vuelve a la posición sobre la seta entre corte y corte.
4. **En situación de peligro**: golpeas con la palma, el codo o la cadera. No buscas con el dedo. La seta es lo bastante grande como para acertar incluso en penumbra o con los ojos cerrados.

### Cuatro trampas que invalidan un E-stop

::: warning
La seta puede **existir físicamente** y **no existir jurídicamente**. Cuatro situaciones en las que el E-stop no actúa:

1. **Inaccesible**: bloqueada por una pila de tablas, una caja de herramientas, un saco de serrín. La ves, no la alcanzas.
2. **Bloqueada**: una cuña, una tuerca, un trozo de madera encajado bajo la seta. La aprietas, vuelve sola.
3. **Mecánicamente defectuosa**: óxido, mecanismo de autoenclavamiento dañado, fijación floja. La aprietas, no para.
4. **Sin probar**: funciona en teoría, nadie lo ha comprobado en meses. La aprietas, igual funciona, igual no.
:::

Las tres primeras trampas las ve el operador desde el armario de los EPI. La cuarta trampa exige una **prueba funcional diaria**.

### Prueba funcional del E-stop (diaria, antes del turno)

El Rozp. MG 2000 § 7 apdo. 4 impone al operador la obligación de **comprobar el funcionamiento de los dispositivos de seguridad antes de iniciar el trabajo**. La prueba del E-stop tiene este aspecto:

1. **Arranque de la máquina sin carga** (solo el motor, sin madera). Cinta/disco a revoluciones en vacío.
2. **Pulsación de la seta**. La máquina debe pararse al instante (categoría 1: freno en 3-8 s) o empezar la marcha por inercia (categoría 0: 15-30 s).
3. **Giro de la seta** para desbloquear. El botón debe saltar solo tras el giro.
4. **Rearranque**. La máquina debe partir desde cero, sin memoria del estado anterior.
5. **Registro en el parte**: „E-stop puesto X, OK, [firma, hora]". En algunos talleres el registro es una sola „+" hecha con tiza en la pizarra, pero el registro tiene que estar.

::: tip
**Si cualquiera de los cinco pasos no se ha cumplido correctamente: para la máquina físicamente (interruptor principal), reporta al capataz, no empieces el trabajo. El art. 210 § 1 del Código de Trabajo polaco (KP) te da derecho a abstenerte de trabajar cuando las condiciones ponen en peligro la vida o la salud.**
:::

## Términos clave

- **STOP awaryjny (E-stop)** – Emergency STOP (E-stop) – Parada de emergencia (E-stop) – Аварійний STOP (E-stop)
- **Grzybek STOP** – Mushroom STOP button – Pulsador tipo seta – Грибоподібна кнопка STOP
- **PN-EN ISO 13850** – PN-EN ISO 13850 – PN-EN ISO 13850 – PN-EN ISO 13850
- **Wybieg maszyny** – Run-down time – Tiempo de inercia – Час вибігу машини
- **Reset grzybka** – Mushroom reset – Reinicio del pulsador – Скидання грибоподібної кнопки
- **Kategoria zatrzymania 0/1/2** – Stop category 0/1/2 – Categoría de parada 0/1/2 – Категорія зупинки 0/1/2
- **Test funkcjonalny E-stop** – E-stop functional test – Prueba funcional del E-stop – Функціональний тест аварійного STOP

## Autoevaluación

**Pregunta 1.** Trabajas en una sierra circular de 2001 (categoría 0, sin freno). Pulsas el E-stop. ¿Después de cuántos segundos puedes acercarte con seguridad a la hoja?

A) Al instante, porque el E-stop detiene el motor inmediatamente.
B) A los 3-8 segundos.
C) **A los 15-30 segundos (tiempo de inercia del volante), preferiblemente tras la parada visual completa.**
D) Al cabo de una hora, porque el disco se calienta.

**Pregunta 2.** ¿Por qué la seta del E-stop es roja sobre fondo amarillo, y no sobre gris?

A) Porque el amarillo es un color industrial.
B) **Porque el contraste rojo-amarillo permite al ojo del operador reconocer el E-stop en 0,2 segundos, tres veces más rápido que el rojo sobre gris.**
C) Porque es la moda en Alemania y Polonia la copió.
D) Porque el amarillo ahuyenta a los insectos.

**Pregunta 3.** Te acercas a la sierra de cinta y ves que bajo la seta hay un trozo de listón, aparentemente por casualidad. ¿Qué haces?

A) Retiro el listón, arranco la máquina y trabajo con normalidad.
B) Dejo el listón y pruebo si la seta funciona pese al obstáculo.
C) **No arranco la máquina. La seta está bloqueada (trampa 2 de las cuatro), reporto al capataz y espero a que lo reparen o lo confirmen.**
D) Pulso la seta junto con el listón, para „entrenar el mecanismo".

**Reflexión**: Mañana, antes de pulsar cualquier botón START en todo el taller, **encuentra la seta**. Si no la ves a menos de 1 metro, busca al capataz, no a la máquina. Un operador que arranca una máquina sin un STOP localizado vulnera el Rozp. MG 2000 § 7 apdo. 1 y arriesga sus propios dedos. Las dos consecuencias son reales.

## Vínculo con la práctica

**Mañana por la mañana en el aserradero:**

1. **Mapa de STOPs**: recorre tu puesto y dibuja en un papel dónde están todos los pulsadores de emergencia (setas, cuerdas de STOP en los resguardos, pedales). En una sierra de cinta con dos operadores debería haber al menos dos setas. Cuenta cuántas hay realmente.
2. **Prueba diaria**: realiza la prueba de cinco pasos del E-stop descrita en la lección. En la primera prueba pide al capataz que te asista, para que lo vea y lo confirme. Apúntalo en el parte o en la pizarra.
3. **Ritual de manos**: durante la primera semana de trabajo exclusivamente **mano izquierda sobre la seta antes de que la derecha toque el START**. Tras una semana se convierte en hábito muscular y no requiere concentración consciente. El capataz te comprobará con la vista desde 3 metros.

## Notas para el formador

**Acentos de la lección:**

- Segundo paso del ritual **comprueba – arranca – reporta**. Después del „comprueba siéntete" de la lección 2 viene **„comprueba la máquina"**, empezando por el STOP. Subraya: **arrancar no es la primera acción, sino la tercera (tras comprobar los EPI y comprobar el E-stop).**
- Andrij continúa el arco: en el piloto „la primera vez solo", en la l2 „se viste como operador", aquí „mano izquierda sobre el STOP". Gesto corporal anclado en el hábito. En la l4 hará una lista de cinco puntos que cierra el ritual de la semana.
- El principio fail-safe no es „más seguro = más caro". Es un **estándar legal** derivado del Rozp. MG 2000 y de PN-EN ISO 13850. Las máquinas sin este estándar son **ilegales en explotación** desde 2006 (Directiva de máquinas 2006/42/CE).

**Trampas de migrantes:**

- En muchos países de origen (Ucrania, Colombia, Venezuela, Perú, Bolivia) aún se usan máquinas viejas sin E-stop. El operador trae el reflejo „el único botón es START, si acaso corta la alimentación general". En Polonia este atajo cuesta dedos (inercia del volante 15-30 s sin freno).
- Muestra físicamente la diferencia: seta roja sobre amarillo vs. botón rojo sobre panel gris. Pregunta: „¿cuántas capas de polvo bastan para que el rojo sobre gris desaparezca?". Respuesta: una (el polvo tras 2 h cortando roble).
- La cuarta trampa (sin probar) es la más difícil pedagógicamente. El operador piensa „el capataz lo probó la semana pasada, basta". El Rozp. MG 2000 exige **prueba diaria**. Presenta el registro en el parte como prueba, no burocracia.

**Vínculo con M1:**

- Semana 1, l8 de M1: ritual STOP del equipo de evacuación. El mismo signo (seta roja sobre fondo amarillo) vuelve aquí como STOP del operador. En M1 el STOP estaba en la pared (evacuación), en M2 el STOP está en el pupitre (máquina).
- Semana 4, l6 de M1: notificación de sucesos 5W1H. La prueba del E-stop y una avería del STOP son el clásico „near-miss" que hay que reportar antes del accidente.

**Preguntas difíciles:**

- „¿Cuántas veces al día debo probar el STOP?" Una vez, antes de iniciar el turno, con la máquina sin carga. Además, tras cada avería, tras cada cambio de cinta/disco y tras cada parada prolongada (>4 h).
- „¿Y si el STOP salta solo durante el trabajo?" Autoenclavamiento dañado. Apaga con el interruptor principal, reporta al capataz, no intentes „apretarlo más fuerte". Requiere sustitución por persona autorizada.
- „¿Puedo pulsar el STOP por comodidad (en vez del STOP de ciclo)?" No. El E-stop está diseñado para **situaciones de peligro**, no paradas rutinarias. Un uso frecuente desgasta el autoenclavamiento y acorta su vida útil entre 5 y 10 veces. Para la parada rutinaria está el botón negro de STOP de ciclo.

**Materiales de apoyo:**

- Demostración física de una seta de E-stop desmontada de una máquina (pieza vieja sustituida): desarmada, se ve el autoenclavamiento y la desconexión mecánica del circuito.
- Impresión del § 7 del Rozp. MG 2000 en 4 idiomas (PL/EN/ES/UK) en la pared junto al puesto.
- Cronómetro o móvil con segundero para la prueba del tiempo de inercia de la sierra: el alumno mide el tiempo real de inercia de su máquina y lo anota en el parte.
- Vídeo de 30 s de una amputación de dedo en sierra de categoría 0 (reconstrucción de la PIP, 2022) para comentar éticamente: „no por el shock, sino para entender por qué hay que esperar 30 s".
