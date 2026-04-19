---
id: m2-w1-l3
blok: bezpieczenstwo
czas: 120
---

## Introduction

Hai's third day as an operator. He walks into the hall dressed like an operator (lesson 2 stuck in his head), approaches the band saw and places his hand on the green START button. The foreman stops him with a single word: **"STOP first."**

Hai looks confused. After all, he wants to **start** the machine, not stop it. The foreman turns his hand around and points to the red mushroom on a yellow background, 30 centimetres to the left of the green START. **"Before you press START, check that STOP works and is within your reach. If you don't know where STOP is, don't touch START."**

This lesson explains why, on every woodworking machine, the stopping circuit **has priority** over the starting circuit. Why the mushroom is red on yellow. Why a workshop with three saw stations has **six mushroom buttons**, not three. And why a daily STOP test is not the foreman's paranoia but a requirement of Rozp. MG 2000 (Polish Ministry of Economy Regulation of 14 April 2000 on OSH in woodworking machine operation).

The first rule of this lesson: **your hand returns to STOP before the other one touches START**. This is how you will work in 2026, in 2036 and on the last day before retirement.

## Objectives

After this lesson:

1. You understand the fail-safe principle: on every woodworking machine, the stopping circuit (STOP) has priority over the starting circuit (START). This hierarchy comes from design, standards and law, not from the operator's choice.
2. You recognise an emergency stop mushroom per PN-EN ISO 13850: red colour, yellow background, mushroom shape (easy to strike with the palm or elbow), self-latching after being pressed.
3. You know the three stop categories (0, 1, 2) and you know which one applies to the band saw, the circular saw and the spindle moulder.
4. You can locate all emergency stops at a station from every working position (reach <1 metre) and you can point to four types of traps that invalidate an E-stop.
5. You perform a daily functional test of the emergency stop before starting work and you know how to report it to the foreman.

## Content

### Fail-safe principle: STOP > START

**Fail-safe** is a machine-design principle in which a system failure **stops** the machine rather than starting it. Used since the 1960s in aviation, since the 1980s in the wood industry. Enshrined in Polish law in the **Regulation of the Minister of Economy of 14 April 2000**, § 7(1):

> *"Woodworking machines shall be equipped with control devices ensuring their immediate stopping in a situation of danger. These devices shall be easily accessible from every operating station."*

In practice this means three design rules:

- **STOP is stronger than START**. If you press both at the same time, the machine stops.
- **STOP works even when power is lost**. The mushroom breaks the circuit mechanically, independently of the PLC controller.
- **STOP is passive at rest**. You have to press it once (stop), then **twist and pull it out** (reset). Self-release is excluded by design.

::: info
**History of the principle**: in the 1970s, woodworking plants used a single START-STOP button (one switch, two positions). After a series of amputations in East Germany and Finland, the EN 418 standard (1993) forced the **separation of circuits**. Polish implementation: PN-EN 418 (1999), later replaced by PN-EN ISO 13850 (2015).
:::

### The mushroom button: red on yellow

The **PN-EN ISO 13850:2015** standard describes the emergency stop (E-stop) precisely:

- **Button colour**: red.
- **Background colour behind the button**: yellow.
- **Shape**: mushroom-like (head of a mushroom), diameter 40-60 mm, protruding 15-20 mm above the panel surface.
- **Mechanism**: pressing latches it; release is by **clockwise rotation** (key, bolt, sometimes a pull).

Why red on yellow and not red on a grey control panel? Contrast. In sawmill conditions (lighting 300-500 lux, dust 2-10 mg/m³), the operator's eye recognises red on yellow **in 0.2 second**, red on grey **in 0.5-0.8 second**. Three times faster. That is the difference between "hand on STOP before the board hits" and "board hit, hand on the way".

::: warning
**Beware of counterfeits**: cheap imported saws from big-box stores sometimes have an "e-stop" in red on a black panel, no yellow background, no self-latching (the spring pops it back when released). **This is not an E-stop in the sense of PN-EN ISO 13850**. Report such a button to the foreman and do not start the machine.
:::

### Three stop categories

The **PN-EN 60204-1** standard (machine safety, electrical equipment) defines three stop categories:

**Category 0**: immediate cut-off of power to the motor. The machine **stops by run-down** (i.e. it keeps spinning thanks to inertia until friction brings it to rest). A circular saw with a 4 kW motor has a run-down of **8-15 seconds**. A band saw with a flywheel: **20-30 seconds**. During that time the blade is **still dangerous**.

**Category 1**: controlled stop with a brake. The motor receives a braking signal, the blade stops in **3-8 seconds**. Standard for new circular saws in the EU (required since 2006, Machinery Directive 2006/42/EC).

**Category 2**: controlled stop with power retained (the machine "stands by", ready to resume). Used rarely, mainly on automated industrial lines.

**What this means for the operator**: category 0 is an **old machine**. Category 1 is a **new machine with a brake**. With category 0, **do not approach the blade for 30 seconds** after pressing STOP. Counting aloud ("one thousand one, one thousand two…") is not a foreman's quirk, it is **finger protection**.

::: example
**A case from a Polish sawmill (Opolskie, 2022)**: an operator of a 2001 band saw (category 0) pressed STOP, saw a block stuck between the guides, and reached for it **after 12 seconds**. The flywheel was still spinning. Amputation of the index finger. Conclusion by PIP (Polish Labour Inspectorate): machine functional, operator ignored the run-down time. Recommendation: **upgrade to category 1 with a brake**.
:::

### Location and the 'hand-on-STOP' ritual

Rozp. MG 2000 § 7(2) requires the emergency stop to be **"easily accessible from every operating station"**. At a band saw with two operators (feeder + tailer), this means **two mushroom buttons**: one at each station, each within one-hand reach (<1 metre).

The ritual that becomes a habit after a month on the job:

1. **Approaching the machine**: locate the mushroom visually. Check the colour (red on yellow), the shape (protruding), the condition (no marks from being struck, no chips glued to it).
2. **Before starting up**: place your left palm on the mushroom. Only then does your right hand move to START.
3. **During cutting**: the left hand **does not leave the reach of the mushroom**. It moves the wood, but returns to a position above the mushroom between cuts.
4. **In a danger situation**: you strike with the palm, the elbow or the hip. You don't hunt with a finger. The mushroom is large enough that you will hit it even in dim light or with your eyes closed.

### Four traps that invalidate an E-stop

::: warning
A mushroom can **physically exist** and **legally not exist**. Four situations in which an E-stop will not work:

1. **Unreachable**: blocked by a stack of boards, a tool box, a bag of sawdust. You see it, you can't reach it.
2. **Jammed**: a wedge, a nut, a piece of wood pushed under the mushroom. You press it, it springs back.
3. **Mechanically defective**: rust, broken self-latching mechanism, loose mounting. You press it, it doesn't stop.
4. **Untested**: works in theory, nobody has checked it for months. You press it, maybe it works, maybe not.
:::

The first three traps are visible to the operator from the PPE cabinet. The fourth trap requires a **daily functional test**.

### E-stop functional test (daily, before the shift)

Rozp. MG 2000 § 7(4) places on the operator the duty of **checking the operation of safety devices before starting work**. The E-stop test looks like this:

1. **Start the machine with no load** (motor only, no wood). Band or blade at idle speed.
2. **Press the mushroom**. The machine must stop immediately (category 1: brake in 3-8 s) or begin to run down (category 0: 15-30 s).
3. **Rotate the mushroom** to release. The button must pop out by itself after the rotation.
4. **Restart**. The machine must start from zero, with no memory of the previous state.
5. **Log entry**: "E-stop station X, OK, [signature, time]". In some workshops the entry is just a single "+" on a chalk board, but there must be an entry.

::: tip
**If any of the five steps did not go as it should: physically stop the machine (main disconnect), report to the foreman, do not start work. Art. 210 § 1 of the Polish Labour Code gives you the right to refrain from work when the conditions threaten life or health.**
:::

## Key terms

- **STOP awaryjny (E-stop)** – Emergency STOP (E-stop) – Parada de emergencia (E-stop) – Аварійний STOP (E-stop)
- **Grzybek STOP** – Mushroom STOP button – Pulsador tipo seta – Грибоподібна кнопка STOP
- **PN-EN ISO 13850** – PN-EN ISO 13850 – PN-EN ISO 13850 – PN-EN ISO 13850
- **Wybieg maszyny** – Run-down time – Tiempo de inercia – Час вибігу машини
- **Reset grzybka** – Mushroom reset – Reinicio del pulsador – Скидання грибоподібної кнопки
- **Kategoria zatrzymania 0/1/2** – Stop category 0/1/2 – Categoría de parada 0/1/2 – Категорія зупинки 0/1/2
- **Test funkcjonalny E-stop** – E-stop functional test – Prueba funcional del E-stop – Функціональний тест аварійного STOP

## Check yourself

**Question 1.** You are working at a 2001 circular saw (category 0, no brake). You press the E-stop. After how many seconds can you safely approach the blade?

A) Right away, because the E-stop stops the motor immediately.
B) After 3-8 seconds.
C) **After 15-30 seconds (run-down time of the flywheel), ideally after a full visual stop.**
D) After an hour, because the blade heats up.

**Question 2.** Why is the E-stop mushroom red on yellow, and not on grey?

A) Because yellow is an industrial colour.
B) **Because the red-on-yellow contrast lets the operator's eye recognise the E-stop in 0.2 second, three times faster than red on grey.**
C) Because that is the fashion in Germany and Poland copied it.
D) Because yellow repels insects.

**Question 3.** You approach the band saw and see a piece of lath lying under the mushroom, apparently by accident. What do you do?

A) I remove the lath, start the machine and work normally.
B) I leave the lath and test whether the mushroom works despite the obstacle.
C) **I do not start the machine. The mushroom is jammed (trap 2 of four), I report to the foreman and wait for repair or confirmation.**
D) I press the mushroom together with the lath to "train the mechanism".

**Reflection**: Tomorrow, before you press any START button anywhere in the workshop, **find the mushroom**. If you do not see it within 1 metre of reach, find the foreman, not the machine. An operator who starts a machine without a located STOP violates Rozp. MG 2000 § 7(1) and risks his own fingers. Both consequences are real.

## Link to practice

**Tomorrow morning at the sawmill:**

1. **STOP map**: walk around your station and draw on a sheet of paper where all the emergency stops are (mushroom buttons, STOP ropes on guards, foot pedals). At a band saw with two operators there should be at least two mushrooms. Count how many there really are.
2. **Daily test**: perform the five-step E-stop test described in the lesson. On the first test ask the foreman to assist, so that he sees it and confirms. Record it in the log or on the board.
3. **Hand ritual**: for the first week of work, **left palm on the mushroom before the right touches START**, without exception. After a week this becomes muscle memory and no longer requires conscious focus. The foreman will check you visually from 3 metres away.

## Trainer notes

**Lesson emphases:**

- The second step of the **check – start – report** ritual. After "check yourself" from lesson 2 comes **"check the machine"**, beginning with STOP. Stress: **starting up is not the first action but the third (after checking PPE and checking the E-stop).**
- Hai, continuation of the arc: in the pilot "first time alone", in l2 "dressing like an operator", here "placing the left palm on STOP". A bodily gesture anchored in habit. In l4 he will perform the five-point checklist that closes the ritual of the week.
- The fail-safe principle is not "safer = more expensive". It is the **legal standard** stemming from Rozp. MG 2000 and PN-EN ISO 13850. Machines without this standard are **illegal to operate** after 2006 (Machinery Directive 2006/42/EC).

**Migrant pitfalls:**

- In many countries (Vietnam, Moldova, Georgia, partly Ukraine) old machines without an E-stop are still in use. The operator carries over the reflex "the only button is START, in case of trouble switch off the mains". In Poland this shortcut costs fingers (flywheel run-down 15-30 s without a brake).
- Show the difference physically: red mushroom on yellow vs. red button on a grey panel. Ask the migrants: "how many shifts of dust do you need to darken the hall so that red on grey disappears?". Answer: one (dust after 2 h of cutting oak).
- The fourth trap (untested) is the hardest pedagogically. The operator thinks "the foreman tested it last week, that's enough". Rozp. MG 2000 requires a **daily test**. Show the log entry as evidence, not bureaucracy.

**Link to M1:**

- Week 1 l8 of M1: the evacuation brigade STOP ritual. The same sign (red mushroom on yellow) returns here as the operator STOP. In M1 STOP was on the wall (evacuation); in M2 STOP is on the panel (machine).
- Week 4 l6 of M1: reporting incidents 5W1H. An E-stop test and an unserviceable STOP are a classic "near-miss" to report before an accident.

**Difficult questions:**

- "How many times a day should I test STOP?" Once, before the shift begins, on the machine with no load. In addition, after every failure, after every blade/band change, and after every longer stoppage (>4 h).
- "What if STOP pops out on its own during work?" The self-latching mechanism is damaged. Switch off the machine at the main disconnect, report to the foreman, do not try to "press it harder". Replacement is required by an authorised person.
- "Can I press STOP for convenience (instead of using the normal cycle STOP)?" No. The E-stop is designed for **danger situations**, not for routine stops. Frequent use wears out the self-latching mechanism and shortens its life 5-10 times. For routine stopping there is the black cycle STOP button.

**Teaching aids:**

- Physical demonstration of an E-stop mushroom dismounted from a machine (old item from a replacement): unscrewed, showing the self-latching mechanism and the mechanical circuit break.
- Printed § 7 of Rozp. MG 2000 in 4 languages (PL/EN/ES/UK) on the wall next to the station.
- A stopwatch or a phone with a second hand for the run-down test: the learner measures the actual run-down of their own machine and records it in the log.
- A 30 s video of a finger amputation on a category 0 saw (PIP reconstruction, 2022) to discuss ethically: "not for shock, but to understand why 30 s of waiting".
