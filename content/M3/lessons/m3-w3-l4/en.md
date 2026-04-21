---
id: m3-w3-l4
blok: procesy
czas: 120
---

## Introduction

Friday, 2026-05-30, 9:25. Eleven days after the planning briefing in l3, eleven days into the drying cycle for English oak in the BH-50 kiln. Rustam walks across the yard toward the drying hall, notebook in hand, work phone (an old-style Nokia, battery lasts a week, signal covers the whole sawmill) in his overall pocket. Marek has scheduled him from 9:30 to 11:30 today for a **training presence in the drying section** as part of the M3 process block. Wahan is not with Rustam today; he is on a maintenance shift on P1 with Juri (junior maintenance mechanic).

Rustam enters the drying hall (12 × 8 × 4.5 m, the same hall as in l3), then the **control room** (a 2 × 3 m space with the control cabinet, observation windows onto the kiln, and a small desk in the corner). Pan Henryk is already there, drinking coffee from a thermos; Maciek Wiśniewski (drying helper, 19 years old, Ostróda wood-technology school, from l3) stands in front of the panel with the **weekend log** in his hand. The log is an A4 hardcover notebook, filled in twice a day on weekends (Saturday 10:00 and 16:00, Sunday 10:00 and 16:00), sometimes more often if Maciek feels like checking the kiln on Saturday evening.

### 9:30, routine reading

Pan Henryk, to Rustam: *„Good morning. Sit down, watch, write. Today I will show you how to read the panel during a cycle. The current oak reached day fourteen on Thursday; tomorrow is day fifteen, Sunday is day sixteen. The main phase ends on Sunday; Monday we switch to conditioning."*

Rustam sits on a stool by the desk, opens his notebook, writes down the date and time. The BH-50 panel shows:

```
Kiln: BH-50 (Brunner-Hildebrand)
Program: DUB-STAND-28 (English oak 28 mm, 22 days to 14%)
Charge: oak 2.5 m³, 30 mm boards, start 2026-05-17
Cycle day: 14 of 22
Current phase: main drying, day 12 of 14 (ends 2026-06-01)

Air temperature:         58°C  (target 60°C, tolerance ±3)
Relative humidity (RH):  47%   (target 45%, tolerance ±5)
Wood moisture probe 1:   24.8% (start 38%, yesterday 25.3%)
Wood moisture probe 2:   24.1% (start 37.6%, yesterday 24.6%)
Wood moisture probe 3:   25.7% (start 38.5%, yesterday 26.2%, drying slower)
EMC (equilibrium MC):    8.4%
Moisture probe spread:   1.6% (OK, below 3% threshold)
Fan status:              1450 RPM, current 6.2 A (nominal 1500/6.5)
Heater status:           45% power (nominal 40-60% in main phase)
```

Pan Henryk points a fingernail at three lines: *„Look. The wood moisture drops every day by 0.5-0.6%. That's good dynamics for oak on day fourteen. To reach 14% target we still have 10-11% to shed in eight days. That's **1.25% per day**. The pace rises in conditioning, then slows at the end. The plan is holding."*

Rustam writes: *„oak d.14, moist. 24-26%, EMC 8.4%, spread 1.6% OK, fans ok."*

Pan Henryk: *„**Spread** is the most important uniformity indicator during a cycle. If probe three runs 1-2% slower, it means that where it is mounted (rear of the kiln) the airflow is a bit weaker. Normal. When the difference grows to 3-4%, you have a problem. Today 1.6%, calm."*

### 9:40, Pan Henryk shows the alarm history

Pan Henryk clicks the „Alarm history" tab on the panel. On the screen, a list from the last 30 days:

```
2026-05-19 03:47  INFO     Airflow RPM 1400 (target 1500, margin)
2026-05-22 16:23  WARNING  Fan 2 current 7.1 A (target 6.5, +10%) → auto-correction
2026-05-27 08:15  INFO     Program start, day 1 of heating
[remaining entries from previous drying cycles]
```

*„You see, Rustam, **INFO** is a note, not an alarm, no reaction required. **WARNING** is level two; the controller corrects by itself, the operator observes. **ALARM** is level three; the controller does not correct, human reaction required. There have been no alarms in the last month, that's a good sign."*

Maciek returns to the saw hall with his own task (loading the sawmill for the afternoon client) and closes the control-room door behind him.

### 9:45, the alarm fires

Pan Henryk pours more coffee from the thermos, Rustam watches the panel, and suddenly **a red LED** in the corner of the screen starts to pulse. The controller emits a short acoustic signal (three beeps, 1 second, then a 2-second pause, then again). On the screen a message:

```
ALARM: Air temperature exceeded
Current value: 62.3°C
Program target: 58.0°C
Deviation:     +4.3°C (alarm threshold +4)
Detected:      2026-05-30, 09:43:12
Recommendation: reduce heater power or increase ventilation
```

Rustam flinched, the coffee in Pan Henryk's mug swayed slightly. Pan Henryk speaks calmly but precisely: *„Rustam, you see the red LED. What do you do now?"*

Rustam thinks for two seconds. The lesson from l3: an M3 operator, in case of an alarm, **signals the foreman immediately and does not try to solve it alone**. Pan Henryk is next to him; no phone call needed, just turn around. Rustam says: *„Temperature alarm, 62.3 instead of 58, deviation +4.3. I am reporting it to you, what should I do?"*

Pan Henryk nods: *„Good. First thing, **you do not reset the alarm**, because we don't yet know the cause. Second, **you do not enter the kiln**. Third, **you do not change the program settings**. I diagnose now, you observe and learn. A **small alarm** is good training, because there is no rush."*

Pan Henryk opens the „Live sensors" tab:

```
Sensor T1 (corner A, front-left):  62.1°C
Sensor T2 (corner B, front-right): 62.5°C
Sensor T3 (corner C, rear-left):   61.8°C
Sensor T4 (corner D, rear-right):  62.8°C
Average:                            62.3°C
Spread between probes:              1.0°C (nominal <1.5°C)
```

*„All four temperature probes show similarly, between 61.8 and 62.8. The spread is normal. **This means the entire kiln is hotter**, not one zone. If one probe showed 62 and the other three showed 58, I would suspect a damaged sensor in one corner. Here it is the whole kiln. First diagnosis: **it is not a sensor fault**."*

Rustam writes a note: *„4 probes close together = whole kiln hot, not one sensor. First diagnosis."*

### 9:50, Pan Henryk checks the heaters and the gas valve

Pan Henryk opens the „Heaters and media" tab:

```
Heater 1 (kiln inlet):       current power 68% (target 45%, +23%)
Heater 2 (kiln outlet):      current power 64% (target 45%, +19%)
Main gas valve:              opening 72%       (target 50%, +22%)
Heat exchanger inlet temp.:  78°C              (target 65°C, +13°C)
Proportional control:        AUTO              (normal operation)
```

*„A. **The heaters are heating too hard**. Gas valve open to 72% instead of 50%. Heat exchanger at 78°C instead of 65°C. That means the system **is burning more gas than the program asks for**. The controller noticed, but does not compensate, because the heaters are in AUTO proportional mode and someone or something has pushed the reference signal up."*

Pan Henryk picks up the phone, dials Marek (the foreman, on the mobile from 7:00):

*„Marek, Henryk from drying. I have a temperature alarm in the oak kiln, plus four degrees, heaters open to 68%, gas valve 72%. I suspect **the heat-exchanger thermostat**, which is pushing the system to heat more than needed. You remember, I heard from BTM yesterday they plan to replace this thermostat in July during the annual inspection, but now it's too early for that. Can you call BTM service? You have the number in the folder."*

Marek confirms he will call. Pan Henryk hangs up.

### 9:55, first manual correction

Pan Henryk to Rustam: *„Now I will do a **manual correction of the gas valve** to bring the kiln temperature from 62 back to 58. This is a **drying foreman's** decision, not an M3 operator's. An M3 operator does not even have a password to this panel, just an informational view."*

Pan Henryk enters the password (6-digit, changed quarterly by BTM), opens the manual-control window:

```
Manual heater control:
Heater 1: currently 68%, change to: 40% [confirm]
Heater 2: currently 64%, change to: 40% [confirm]
Gas valve: currently 72%, change to: 45% [confirm]

Note: a manual change disables AUTO mode for 30 minutes.
After 30 minutes the controller returns to AUTO with new values.
If you want AUTO to stay off longer, enter it in
„Special options, AUTO lockout for N minutes".
```

Pan Henryk lowers heater 1 from 68% to 40%, heater 2 from 64% to 40%, the gas valve from 72% to 45%. He confirms three times; the controller disables AUTO for 30 minutes (from 9:55 to 10:25).

*„Rustam, the **maximum rate-of-change rule for temperature** is **6°C per hour**. Oak must not be cooled faster than 6°C/h, because that causes **internal checker**. The drop from 62 to 58 is 4°C; it should be done in 40 minutes, not in 5. The controller will lower it gradually. We observe."*

### 10:00, trend observation

Pan Henryk and Rustam watch the panel, refreshing every 15 seconds. In 5 minutes the temperature drops from 62.3 to 61.1 (a drop of 1.2°C in 5 minutes, i.e. **14.4°C/h**, too fast). Pan Henryk comments: *„Too fast, but expected in the first minutes after reducing the gas. The hot heat exchanger gives off heat into the kiln even when the heaters draw less current. We wait; within 20 minutes the drop should stabilise."*

Rustam writes observations every 2 minutes:
- 09:55 62.3°C (start)
- 09:57 61.9°C (drop 0.4)
- 10:00 61.1°C (drop 0.8)
- 10:03 60.6°C (drop 0.5)
- 10:05 60.2°C (drop 0.4)
- 10:10 59.5°C (drop 0.7 in 5 min)
- 10:15 58.8°C (drop 0.7 in 5 min, stabilising)

*„10:15, temperature 58.8, almost at the 58 target. Since 9:55 a drop of 3.5°C in 20 minutes, i.e. an **average of 10.5°C/h**. That is above the 6°C/h limit for the first 10 minutes, then it calmed down. Too fast but not catastrophic for oak day fourteen (the wood is already partially dried, less sensitive than at the start of the cycle). We leave it as is, we monitor."*

### 10:20, Marek calls with information from BTM

Pan Henryk's phone vibrates. Marek: *„Henryk, I called BTM. The heat-exchanger thermostat, model GH-67, a problem known to them since 2024, the feedback loop pushes the signal toward heating beyond the set point when ambient humidity is 65%+ (outside the kiln, in the drying hall). Today the hall is at 68% (we have a rainy morning). That explains the behaviour. BTM will come Monday morning, replace the thermostat for free under warranty. Until Monday, **manual control**, corrections every 4-6 hours; I'll relieve you Saturday morning for 2 hours so you don't sit there all weekend. Maciek's weekend plan stays, only additionally observation every 4 hours, not every 8."*

Pan Henryk confirms, writes in his notebook: *„Until Mon 02.06 manual control, corrections every 4-6 h. BTM service Mon morning."*

### 10:30, controller returns to AUTO with new values

At 10:25 the controller automatically returns to AUTO. The temperature stabilises at 58.2°C (close to the 58 target), the heaters drop to 43% (close to the 45 target), the gas valve to 48% (close to the 50 target). Probe spread 0.8°C. Wood-moisture probe spread 1.6% (unchanged). The alarm has cleared, the red LED went off at 10:24.

Pan Henryk resets the alarm history (confirms in the kiln log), enters a note:
```
2026-05-30 09:43  ALARM Temp +4.3°C → manual correction 9:55
2026-05-30 10:15  ALARM resolved, temp 58.2°C
```

*„Rustam, **now the KS-001 card**. Every alarm must be documented, regardless of whether there were consequences for the wood or not. This is an ISO 9001 requirement and a BTM requirement for the kiln warranty."*

### 10:40, entry in KS-001

Pan Henryk takes the current-charge drying card from the desk drawer (KS-001 for the oak charge ZLE-075 start 17.05, which he filled out at cycle start). He adds to section 3 (Notes and observations):

```
2026-05-30 09:43-10:24 Temperature ALARM +4.3°C
Cause (per BTM, phone call M.Kowalski): GH-67 thermostat
  of the heat exchanger, feedback loop at high
  ambient humidity.
Correction: manual reduction of the gas valve from 72% to 45%,
  heaters from 68/64% to 40/40%. Temperature returned to 58°C
  in 32 minutes (avg drop 10°C/h, above the 6°C/h limit
  for 10 min, acceptable for oak day 14).
Wood state: moisture unchanged, probe spread 1.6%.
Plan: manual control until Mon 02.06, BTM service.
Present: Pan Henryk (foreman), Rustam Nazarov (M3 training).
Signature: H. Nowak, 10:45.
```

*„Rustam, **you were not here at 9:55**. In the document I write 'present Rustam Nazarov' because you were here, and that is a fact for the audit. If someone asks you one day 'were you there at the kiln alarm on 30 May', you say 'yes, I was learning', you will not be ashamed."*

Rustam writes in his notebook: *„The alarm happened. We documented it. Without hiding. **Documents are protection, not a problem**."*

### 10:50, a talk about the limits of competence

Pan Henryk pours Rustam more coffee from the thermos (sugar from a separate sachet); they sit side by side in front of the panel, temperature stable at 58.2°C.

*„Rustam, I would like you to understand one thing today. The alarm fired, I solved it, but **had I not been here**? What would you as an M3 operator have done?"*

Rustam thinks: *„I would have phoned Marek. Marek is on the saw hall, he would be here in 2-3 minutes."*

*„Good. And if Marek does not answer, because he is in the shower after a sawdust cleaning round?"*

*„I would have called the BTM service number. Which I would find in the folder in the drying control cabinet."*

*„Good. And if BTM does not answer, because it is the weekend? What do you do?"*

Rustam thinks. *„Unlike with a saw, I cannot switch the kiln off on my own, because the wood would then cool too fast or heat up. If I cannot reach the foreman or BTM, then... **I observe and write**, until one of them comes back. Unless I see smoke or hear cracking."*

*„Exactly. **The last resort** is not the M3 operator switching the kiln off, because any attempt at manual intervention without authorisation may make things worse. The rescue is **observation, documentation, escalation**. Just as on the saw it is **STOP, secure, report, document**. Here it is **OBSERVE, RECORD, REPORT, ESCALATE**. The first three steps are the same, the fourth is different, because you cannot 'secure' a kiln in a minute like a machine."*

Rustam writes in his notebook: *„Kiln, M3 operator alarm procedure: **OBSERVE, RECORD, REPORT, ESCALATE**. No manual intervention."*

### 11:00, normalising the kiln and the weekend plan

At 11:00 the kiln is fully stable: temperature 58.1°C, RH 46%, average wood moisture 24.7%, EMC 8.5%. Pan Henryk does a reading, Rustam records in parallel.

Pan Henryk: *„Manual control until Monday. I stay today until 16:00. Maciek went back to the saws; I will tell him when he returns that over the weekend he monitors the kiln **every 4 hours** instead of every 8. Saturday 8:00, 12:00, 16:00, 20:00. Sunday similarly. If anything happens, he calls me, not you, not Marek."*

*„You are off tomorrow (Saturday), right?"*

Rustam: *„Yes, Sunday off as well."*

*„Good. Monday come normally to the saw, BTM will replace the thermostat, you might find it useful to watch how the service is done, but it is not your role. Tuesday 02.06 loading for Drew-Sus, remember, pine 2.42 m³, you, Wahan and Anton from the yard brigade. From Tuesday evening the kiln is empty until 08.06 when we collect the oak."*

Rustam confirms, closes his notebook. *„Thank you, Pan Henryku."*

*„You handled it. **Signalling instead of intervention, observation instead of panic**. These are the foreman's standards, which you as an M3 operator already know and apply. In half a year, if you take the assistant drying course, you will be able to resolve alarms like this yourself. Today you were learning by watching."*

## Objectives

After this lesson:

1. You know the **three signal levels of the BH-50 controller**: 1) **INFO** (a record in history, no reaction required, e.g. a brief fan RPM deviation); 2) **WARNING** (controller corrects itself, operator observes, e.g. fan current above 10% of nominal); 3) **ALARM** (controller does not correct, human reaction required, e.g. temperature deviation of +4°C or more). You understand that an ALARM lights the red LED on the panel and triggers an acoustic signal (three beeps with 2 s pauses), and that **the M3 operator, in case of an ALARM, signals the drying foreman immediately** and does not try to solve it alone.
2. You know the **four-step M3 operator procedure for a kiln alarm**: **OBSERVE** (read all sensor indications without touching the panel), **RECORD** (date, time, current vs target values, alarm type), **REPORT** (phone or in-person contact with the drying foreman), **ESCALATE** (if the foreman is unreachable, the shift supervisor, then BTM service). You understand that this procedure is **different from the saw** (where it is STOP-secure-report-document), because a kiln cannot be „secured" in a minute; a quick shut-down generates thermal shock to the wood and costs more than calm observation.
3. You understand **typical kiln alarms** (temperature, airflow, humidity, sensor, gas state) and their different priorities. A +4°C temperature alarm in the main phase of oak day 14 is a **minor alarm** (wood partially dried, less sensitive), a +6°C temperature alarm on day 3 of heating is a **serious alarm** (wood at the start, sensitive to shock). You understand that the M3 operator does not classify alarm priority (that is the foreman's job), only reports all alarms equally.
4. You know the **maximum temperature rate-of-change rule of 6°C/h** for drying kilns for hardwood species (oak, beech, ash). Exceeding this rule for periods longer than 10-15 minutes causes **internal checker** inside the boards, invisible from outside, revealed after processing at the customer. For softwoods (pine, spruce) the rule is less strict (8-10°C/h is allowed), but the EGIDA foreman keeps 6°C/h for all species as a safety standard.
5. You know the **interpretation of probe spread** on the BH-50 panel. Temperature spread between the four sensors at the kiln corners: **<1.5°C** (OK, normal uniformity), **1.5-2.5°C** (observe, may indicate uneven airflow), **>2.5°C** (airflow problem, foreman diagnoses). Wood-moisture probe spread: **<2%** (OK, uniform charge), **2-3%** (observe, some boards dry slower), **>3%** (problem, the charge was non-uniform or a probe is damaged). You understand that **one outlying probe** signals a sensor problem, **all probes drifting in parallel** signals a whole-kiln problem.
6. You understand the **limit of the M3 operator's competence in kiln control**. The M3 operator: **has no password** to manual control of heaters, valves, programs. The M3 operator **does not reset the alarm** on their own, even when the alarm seems false. The M3 operator **does not open the kiln door** during a cycle (thermal shock to the wood, loss of an hour of the cycle). The M3 operator **does not change program set-points** (target temperature, target RH, board thickness). The drying foreman (Pan Henryk): has the password, enters manual corrections, disables AUTO for 30 minutes or longer, documents in KS-001.
7. You know the **way an alarm is documented in the KS-001 card** section 3 (Notes and observations). Required fields: **alarm start date and time**, **measured value vs target** (e.g. „62.3°C vs 58°C, deviation +4.3"), **probable cause** (e.g. „GH-67 thermostat feedback loop, confirmed BTM by phone"), **actions taken** (e.g. „manual correction of gas valve from 72% to 45%"), **result** (e.g. „temperature returned to 58°C in 32 minutes, average drop 10°C/h"), **wood state after the alarm** (e.g. „moisture unchanged, probe spread 1.6%"), **normalisation plan** (e.g. „manual control until Mon 02.06, BTM service"), **persons present** (foreman, M3 operator in training), **signature and time of entry**.
8. You know the **role of Maciek Wiśniewski** (drying helper M1) in monitoring the kiln. Maciek reads the panel and enters it into the log **daily** (at least 2 times a day on working days plus 4 times on weekends in standard mode, 6-8 times on weekends after an alarm). Maciek **signals Pan Henryk** at every deviation going outside the routine. Maciek **does not have a password** for manual control, same as the M3 operator. You understand that **Maciek and the M3 operator have a similar scope of competence** with respect to the kiln (they observe, record, signal, do not intervene), but Maciek has more visual practice (he sees the kiln every day, the M3 operator once a week).

## Content

### 1. How the M3 operator reads the BH-50 control panel

The BH-50 control panel is **visually accessible to every employee** in the drying hall, including the M3 operator who is present only occasionally (e.g. during the planning briefing in l3 or a training presence). Visible are: temperature, air humidity, wood moisture on three probes, EMC, fan status, heater status, program number, cycle day, cycle phase, alarm history.

**Not visible without a password** (drying-foreman and BTM-service access): manual heater control, manual opening of the gas valve, manual RH adjustment by steam injection, the full alarm log for the last 2 years, sensor calibration parameters.

**The M3 operator observes, does not change.** Understanding the panel is pedagogically important because the M3 operator learns to see the **dynamics of the drying cycle**: how wood moisture drops gradually (0.3-0.6% per day in the main phase), how temperature oscillates in a narrow ±2°C band around target, how fans maintain a steady flow of 1400-1500 RPM, how the heaters descend from 60% in heating to 40% in the main phase to 30% in conditioning. Seeing this, the M3 operator **senses the normal rhythm of the cycle**, and when something deviates from the rhythm, sees it faster than someone without experience.

**Three typical values on the panel for the oak cycle day 14 of 22** (today, 2026-05-30):

1. **Temperature**: target 58-60°C (main phase), tolerance ±3°C. If outside tolerance by 2-3°C, observe. If +4°C or more, alarm.
2. **Relative humidity (RH)**: target 45-50% (main phase), tolerance ±5%. If outside tolerance by 2-5%, observe. If +8% or more, alarm.
3. **Wood moisture**: dynamic target (drops 0.3-0.6%/day in the main phase). If the rate is 0, the controller looks for a cause (heaters, ventilation). If the rate is 1%+/day, it may mean too fast drying (risk of checks), observe.

### 2. How the BH-50 controller works in an oak cycle

The **Brunner-Hildebrand Omega 7** controller (the model used in BH-50 since 2011) is an industrial PLC (Programmable Logic Controller) with software specific to drying kilns. It has memory for **20 factory programs** (pine, spruce, oak, beech, birch, maple and others) plus **10 user programs** (EGIDA currently has 4: SOS-STAND-28 pine, DUB-STAND-28 oak, BUK-STAND-25 beech, BRZ-STAND-25 birch).

A **program cycle** is a set of **about 150 parameters** describing how the kiln must behave over 9-25 days of the cycle: **for every hour** of the cycle, the controller has a target temperature, target RH, temperature rate-of-change, and RH rate-of-change. The program automatically **derives from current wood moisture** which phase it is in (heating, pre-drying, main drying, conditioning, cooling) and adapts the parameters. Phase switching is automatic (e.g. the controller detects that wood moisture has reached 16% and switches the cycle from main drying to conditioning).

**In the main phase of oak day 14**:
- Target temperature: 58-60°C (rises gradually from 52°C on day 10 to 62°C on day 15, then falls)
- Target RH: 45-50% (drops from 60% at the start of the main phase to 40% at the end)
- RH descent rate: about 0.8% per day
- Wood-moisture descent rate: 0.5-0.6% per day

**Proportional-integral-derivative (PID) control** (the standard for industrial controllers): the controller **does not switch heaters to 100% when too cold, does not switch them to 0% when too hot**. Live computations: how far we are from target (P), how long the deviation lasts (I), how fast the deviation grows (D). Heaters are switched on **proportionally** (e.g. 45% power) for smooth regulation.

**That is why the 62°C alarm instead of 58°C was not the result of „someone set heaters to 100%"**, but the result of **a feedback loop stuck on the thermostat**: the controller thought it still needed to heat, because it was getting a false signal from the GH-67 thermostat of the heat exchanger (that the inlet temperature was lower than it actually was).

### 3. Recognising types of kiln alarms

**Temperature alarm** (the most common):
- Target ±3°C tolerance, **+4°C = alarm**
- Target ±3°C tolerance, **-4°C = alarm** (too cold a kiln, also a problem, but rarer)
- Typical causes: damaged thermostat (see today), stuck gas valve, fouled heat exchanger, damaged temperature sensor (then one probe drifts apart), kiln door not fully closed (all four probes lower)

**Relative humidity (RH) alarm**:
- Target ±5% tolerance, **±8% = alarm**
- Too high RH in the main phase: exhaust problem, wood does not dry, risk of mould inside
- Too low RH in the early phase: risk of surface checks (end checks) on the ends of boards

**Airflow (fan) alarm**:
- One of the two fans **below 80% RPM** = alarm
- Both fans below 80% = critical alarm, the kiln risks an immediate shut-down
- Typical causes: clogged filter, damaged fan motor, electrical short

**Wood-moisture (probe) alarm**:
- Probe spread **>3%** = alarm (non-uniform charge or damaged probe)
- Descent rate **0% for 48h** = stagnation alarm (wood not releasing water, problem with conditions)
- Descent rate **>1.5% per day** = fast-drying alarm (check risk)

**Main gas alarm**:
- External pressure in the gas tank **below 25% full** = alarm, the kiln automatically switches to the second tank
- Below 10% = critical alarm, the kiln automatically stops heating, the controller enters „emergency cooling" mode

**Sensor alarm**:
- The temperature or humidity sensor shows **extreme (physically impossible) values** = alarm, the controller isolates the sensor, uses the remaining ones (redundancy of 4 temperature probes = 3 are enough to continue the cycle).

### 4. Maximum temperature and cooling rate-of-change

The **6°C per hour** rule for conventional drying kilns applies to hardwood species (oak, beech, ash, maple) and comes from wood physics. **Oak shrinkage** at a change in moisture is **0.25% per 1% of moisture change** (longitudinal-radial). In thermal shock (a sudden temperature change) the surface of a board loses water faster than the core, creating a **moisture gradient** (5-10% difference), which in turn produces a dimensional gradient and **internal stress**.

Stresses exceeding **the tensile strength of oak in the tangential direction** (around 5-6 MPa) cause **internal checker**, invisible from outside, revealed during processing.

**The 6°C/h rate** is set in the DUB-STAND-28 program on day 14 as a limit: the controller **will not change the temperature faster on its own**, even if the program demands a new value. If **the foreman's manual control** produces a faster change (like today, 10.5°C/h for 10 minutes), it is the **foreman's conscious decision** based on a risk assessment (e.g. day 14, the wood is already less sensitive).

**For pine (DUB-STAND-28 vs SOS-STAND-28)** the rule is less strict: **8-10°C/h**, because pine has a more uniform structure and less shrinkage. But EGIDA keeps **6°C/h** for all species as a safety standard (Pan Henryk explained it to operators in 2014; the rule has been in the procedure documentation since).

**For cooling at the end of the cycle** (phase 5, 1-2 days) the rule is even stricter: **4°C/h maximum**, because wood dried to 14% is already sensitive to shock, and the finish of the cycle should „fill in" all micro-stresses, not generate new ones.

### 5. Preventing checks and warping through monitoring

The M3 operator observing the cycle **cannot prevent checks during the cycle** (that is done by the drying foreman and BTM service through a correct program), but **can detect the risk early** and report it:

**Signs of surface-check (end-check) risk**:
- Moisture-probe spread **grows above 2%** in the day 1-3 phase (board surface drying faster than core)
- Temperature **above target** in heating (more than +2°C for an hour)
- RH **below target** in the initial phase (more than -5% for 4 hours)

**Signs of internal-check risk**:
- Wood-moisture descent rate **exceeds 1%/day** in the main phase
- Temperature **jumps of more than 3°C in an hour**
- Conditioning **shortened or skipped** (foreman's decision, rare at EGIDA)

**Signs of warping risk**:
- One moisture probe **clearly drifts higher** (one section of the charge dries slower)
- Uneven stacking (visible through the observation window, you can see some boards already bending)
- RH **too low** in the conditioning phase (gradient does not level out)

The M3 operator during a training presence in the drying section learns to **recognise these signs and report them**. Today Rustam did not see any of them except the temperature alarm itself, which Pan Henryk solved manually. But in 6 months, after the assistant drying course, Rustam will be able to interpret these signals on his own and decide on corrections.

### 6. Maciek's role and weekend monitoring

**Maciek Wiśniewski** (drying helper M1, 19 years old) has a competence scope that is **broader than the M3 operator's in the kiln**, but **narrower than the foreman's**. He can:
- Read the panel and enter it in the log (on his own)
- Replace the paper in the log printer
- Top up lubricating oil in the fan motors (a routine service every 6 months, from the BTM list)
- Sweep the drying control room, wash the kiln observation windows

He cannot:
- Open the kiln door during a cycle (only the foreman, only in exceptional cases)
- Enter a manual correction into the controller (foreman's password)
- Decide on the charge or the program (that is the foreman's)
- Clear an alarm or a log entry

**In the weekend routine (without an alarm)**:
- Saturday 10:00 and 16:00, Sunday 10:00 and 16:00 (4 readings per weekend)
- The log is an A4 notebook on the desk, one line: date, time, temperature, RH, average wood moisture, EMC, signature
- If a temperature or humidity deviation is **outside tolerance** (>±3°C or >±5% RH), Maciek calls Pan Henryk **immediately**, does not wait for the next reading
- If there is a controller alarm (red LED), Maciek calls **immediately** and stays at the panel until the foreman arrives

**After today's alarm** the routine is tightened to **every 4 hours** (Saturday 8:00, 12:00, 16:00, 20:00, Sunday similarly). Maciek gets additional pay (150% weekend rate instead of 100%) for the denser presence.

### 7. Documenting the alarm in the KS-001 card

**The KS-001 card of the current charge** (the one Pan Henryk filled out at the start of the oak cycle on 17.05) has **4 sections**:
1. Planned charge (entered 17.05, description of the 2.5 m³ oak batch)
2. Next planned charge (entered 29.05 in l3, description of the planned pine for Drew-Sus)
3. **Notes and observations** (entered during the cycle, every significant event)
4. Signatures (17.05 start, then after the final cycle)

**Today's alarm** goes into section 3. Pan Henryk writes:
- Alarm start date and time (2026-05-30 09:43)
- Alarm resolution date and time (2026-05-30 10:15)
- Measured value vs program target (62.3°C vs 58°C)
- Deviation (+4.3°C, alarm threshold +4°C)
- Probable cause (GH-67 thermostat of the heat exchanger, feedback loop, confirmed by BTM)
- Actions taken (manual correction of gas valve 72→45%, heaters 68/64→40/40%)
- Result (temperature returned to 58°C in 32 minutes, avg drop 10°C/h, above the 6°C/h limit for 10 min, acceptable for oak day 14)
- Wood state after the alarm (moisture unchanged, probe spread 1.6% unchanged)
- Plan (manual control until Mon 02.06, BTM service, thermostat to be replaced)
- Present (Pan Henryk foreman, Rustam Nazarov M3 training)
- Signature and time of entry (H. Nowak, 10:45)

**The KS-001 card of the current charge stays in the drying-section desk until the cycle is closed** (unloading 08.06). Then the charge is „closed", the card is signed by the foreman and the shift supervisor, scanned to EGIDA OneDrive, the paper sent to the archive (retention 3 years paper + 5 years scan).

**An ISO 9001 auditor** may at any time ask to see the card and say: „show me KS-001 for the oak charge from May 2026". The card must be available within 15 minutes (ISO 9001 section 7.5 „documented information"). That is why section 3 is filled in **as events happen, not after the cycle**.

### 8. EMC in oak monitoring practice

**EMC (equilibrium moisture content)** is **a live control value**. On the BH-50 panel it appears as „EMC: 8.4%" (today). It means: **if the wood stays in the current environment (58°C temperature, 47% RH) long enough, it will reach a moisture content of 8.4%**.

**The actual wood moisture is 24.7% (average of 3 probes)**. So the **difference** is 24.7 - 8.4 = **16.3%**. The wood is driving downward, because it is „wetter" than the environment allows.

**The rate of descent** depends on:
- The difference „current - EMC" (the larger, the faster the water release)
- Wood permeability (oak is less permeable than pine, releases slower)
- Board thickness (a thicker board releases slower, because water has to „work" its way to the surface)

**For oak 28 mm**: a rate of 0.5% per day in the main phase is normal at a difference of 16%. If the difference were 20% (e.g. by lowering RH to 35%), the rate could rise to 0.8-1% per day, **and the risk of checks would grow**.

**That is why the controller does not lower RH to extremely low values** in the main phase. Target 45-50% RH + temperature 58-60°C gives EMC 8-9%. The wood dries gradually, the „current - EMC" difference is moderate (about 16%), the rate is calm (0.5%/day), checks are avoided.

**The M3 operator understands this mechanism intuitively**. They see EMC 8.4, wood moisture 24.7, difference 16%, rate 0.5/day. **That is normal.** If they saw EMC 5%, difference 20%, rate 1%/day, they would think: „the controller is pushing RH down too hard, too aggressively". They would report it to the foreman.

### 9. Typical monitoring mistakes of a beginner

**Mistake 1. Ignoring a small deviation**. A beginner operator sees temperature 61°C instead of 58°C, thinks „that's only 3°C, within tolerance". The tolerance is ±3°C; 61°C is indeed on the edge. But the **trend** grew by 0.5°C in the last 20 minutes, in an hour it will be 64°C, **then alarm**. **Correct**: seeing a trend rising toward the limit, the operator **signals earlier**, does not wait for the alarm.

**Mistake 2. Resetting the alarm „to make it disappear"**. The operator sees the red LED, wants it not to light. Looks for a „reset" button on the panel; some controller models have such a button accessible without a password. **That is a mistake**: the alarm **reappears soon after**, because the cause has not been resolved. Worse, the controller loses the alarm history (a reset deletes the entry), the ISO audit has a hole. **Correct**: **do not reset the alarm**, observe, report to the foreman; the foreman diagnoses and only then resets after resolution.

**Mistake 3. Opening the kiln door „to check on the wood"**. The operator thinks „I'll see what the charge looks like, whether something went wrong". **That is a serious mistake**: a door open for 10 seconds in the main phase of an oak cycle produces **a 15-20°C temperature drop in the kiln** (hot air goes out, cold air comes in), the controller reacts with an alarm, the cycle may be „slipped" by 8-12 hours, and wood quality may suffer. **Correct**: **the kiln door opens only at the end of the cycle** (cooling phase finished), on the foreman's order. During the cycle all information comes **from the panel and probes**, not from direct eye.

**Mistake 4. Confusing air RH with wood moisture**. The panel shows „humidity 47%" (air RH) and „wood moisture 24.7%" (two different parameters). A beginner operator thinks: „the wood is at 47%, a lot, still a lot to dry". But 47% is not wood, it is air. The wood is at 24.7%, 10.7% left to the 14% target. **Correct**: distinguish on the panel between **air RH** (percentage of air humidity in the kiln) and **wood moisture** (percentage of water in the wood). These are two independent parameters; the controller regulates RH, the wood adjusts on its own.

**Mistake 5. Interpreting probe spread as „everything is fine"**. Three probes show 22%, 24%, 28%. Average 24.7%. The operator thinks: „a good average". But a spread of 6% (28-22) is **serious**: one board (probe 3) dries slower than the others. It may be a damaged probe, a board with an internal defect, or uneven stacking. **Correct**: look at the **spread, not the average**. A spread >3% is a signal to report to the foreman.

**Mistake 6. „I will fix it myself, I will not bother Pan Henryk"**. The operator sees the alarm, thinks: „Pan Henryk is tired, I will try myself". **An absolute mistake**: the M3 operator has no password, no practice; their intervention **will make things worse**. Pan Henryk has a phone number, has authority, has experience. **Correct**: **always call the foreman at an alarm**, even if the alarm looks small. Pan Henryk would rather be woken at 23:30 on a Sunday for a false alarm than see in the morning a kiln with cracked wood after a „self-repair" by an operator without authority.

### 10. Assistant drying course, Rustam's next step

The assistant drying-section training module (described in l3 item 11) is an optional extension of M3. It requires **the drying foreman's consent** (today Pan Henryk) and **a completed M3** (for Rustam scheduled for October 2026). Scope: 5 days of intensive training plus an exam.

**Rustam's presence today** (2026-05-30, 2 hours) **counts** as **preliminary practice** toward the training. Pan Henryk will enter into Rustam's personnel file at the end of the day:

```
2026-05-30, 9:30-11:00
R. Nazarov, M3 operator, drying-section training presence.
Observation of oak cycle (day 14), temperature alarm,
foreman's diagnosis and manual correction.
Rustam understood: limit of competence, alarm procedure
(OBSERVE, RECORD, REPORT, ESCALATE), documentation
in KS-001.
Assessment: ready for further training presences.
Next presence planned: oak unloading 2026-06-08,
as assistance in final measurements and packaging.
Signature: H. Nowak, drying foreman.
```

Rustam's personnel file is in the sawmill manager's office, in the folder „Internal training". Its contents influence **Rustam's qualification** for the assistant drying course in October 2026 (minimum 3 training presences as a condition for admission).

### 11. What happens next in the oak cycle after the alarm

**Today (Friday 30.05)**: manual control from 10:25, stabilisation at 58°C, continuous monitoring by Pan Henryk until 16:00. Wood state: moisture 24.7% (unchanged after the alarm, wood resistant to such a short deviation), probe spread 1.6% (unchanged).

**Saturday (31.05) and Sunday (01.06)**: Maciek monitors every 4 hours. Pan Henryk will come on Saturday morning (8:00-10:00) to check in person (foreman Marek agreed to pay Saturday overtime). Temperature should stay at 58-60°C, wood moisture should drop by 0.5-0.6% per day.

**Monday (02.06)**: BTM comes in the morning (9:00) to replace the GH-67 thermostat of the heat exchanger. During this time the kiln **works** (they do not stop the cycle for a one-hour replacement); BTM does the swap „hot" (switches off only this one component, the controller compensates manually for the duration).

**Tuesday (03.06) – Saturday (07.06)**: the cycle ends with the conditioning phase (Sunday 31.05 begins conditioning as per program, although today's alarm does not affect the phase calendar). Temperature gradually drops from 60°C to 55°C, RH rises from 45% to 75% (conditioning). Wood moisture drops from 24% to 14%.

**Sunday (07.06)**: cooling phase, temperature 55°C → 25°C (slow descent 4°C/h max), RH 75% stable. Wood moisture 14% at target.

**Monday (08.06)**: end of the 22-day cycle. **Kiln opening, unloading** (that is l5 M3 T3, Rustam's next lesson).

## Closing scene, 11:00, Rustam's exit

Pan Henryk stays in the control room (log to close, phone call to the next BTM operator confirming the Monday visit), Rustam walks out with a notebook full of new entries. Through the control-room window he sees Maciek returning from the saw hall with the weekend log in his hand; Maciek looks at him questioningly. Rustam shows him briefly: *„There was an alarm, temperature +4, Pan Henryk fixed it. Manual control until Monday, you every 4 hours on the weekend."*

Maciek nods, walks into the control room to talk to Pan Henryk about the weekend schedule.

### 11:05, moving to the saw hall

Rustam walks across the yard to the saw hall. Today is Friday, a normal production shift. His shift on P3 starts at 12:00, until 12:00 he has 50 minutes free. He goes to the employee locker, takes a sandwich out of his bag, sits on the bench in front of the hall, opens his notebook and **writes up cleanly** what he saw this morning.

**Five conclusions**:

1. **A drying kiln is not a machine „to switch on and off"**. The cycle lasts 22 days, the operator observes it, the foreman leads, and over those 22 days anything can happen (alarms, corrections, service). The M3 operator takes part in this complexity **without decisions**, learning to see the rhythm.

2. **A +4°C alarm is „minor" for oak day 14**. The same +4°C on day 3 of heating would be more serious. Pan Henryk saw this right away („no rush, a small alarm, good training"). The M3 operator does not assess alarm priority; they **report all alarms equally**.

3. **The GH-67 thermostat** is a component Rustam did not know before. Today he learned that a kiln controller has many components, **each of which can fail independently**, and that BTM service holds knowledge of typical faults which the M3 operator does not have and does not need to have.

4. **The OBSERVE, RECORD, REPORT, ESCALATE procedure** is **different from the saw procedure** (STOP, secure, report, document). The kiln has no instant „STOP". The operator must understand this difference, because saw intuition says „stop the machine", but in the kiln **stopping the cycle** generates more problems than it solves.

5. **Documentation = protection**. Pan Henryk enters in KS-001 even „minor" alarms, even „Rustam's training presence". An ISO 9001 audit shows that the kiln is monitored, alarms are resolved, staff is trained. Without those entries nothing can be proved. **Paper is protection, not an obstacle**.

Rustam closes the notebook, puts it on the bench, finishes the last of the tea from the thermos. At 11:35 he enters the saw hall and starts preparing P3 for his shift (cleaning the machine bed from the sawdust of Damian's morning shift).

### 11:55, assignment of the day

Marek brings the assignment for the day on P3 from 12:00 to 15:00. It is **ZLE-2026-05-082**, client Stolarz Meblowy Mrągowo (from l3), common beech 25 × 130 × 4000 mm. A different species, a different assortment, a different class (C24 furniture grade, but with an aesthetic condition). Rustam will fill in a new KDP-001.

But that is the next lesson, not today. Today Rustam finishes the drying notes and starts the beech production at 12:00. Wahan will join at 12:15 after finishing maintenance with Juri.

## Key terms

**Kiln alarm** (*alarm komory suszarniczej*, EN *kiln alarm*, ES *alarma de secadero*, UK *тривога сушильної камери*): a controller signal indicating that a parameter has gone past its tolerance threshold; it requires a human reaction (drying foreman), is marked by a red LED and an acoustic signal, and is documented in the KS-001 card.

**Brunner-Hildebrand Omega 7 controller** (*sterownik Omega 7*, EN *Omega 7 controller*, ES *controlador Omega 7*, UK *контролер Omega 7*): the industrial PLC used in the BH-50 kiln, contains 20 factory programs plus 10 user programs, PID proportional control, 24 months of alarm-history memory.

**PID proportional control** (*regulacja PID*, EN *PID control*, ES *control PID*, UK *ПІД-регулювання*): a control algorithm computing the output from the proportional (P), integral (I) and derivative (D) deviation, used in the kiln controller for smooth regulation of heaters, gas valve and fans without jumps.

**GH-67 heat-exchanger thermostat** (*termostat GH-67*, EN *GH-67 heat exchanger thermostat*, ES *termostato GH-67*, UK *термостат GH-67*): a component of the gas installation of the Brunner-Hildebrand BH-50 kiln, regulating the inlet temperature of the heat exchanger to the kiln, with a known feedback-loop problem at high ambient humidity, routinely replaced during the annual BTM inspection.

**OBSERVE-RECORD-REPORT-ESCALATE procedure** (*procedura alarmu komory dla M3*, EN *kiln alarm procedure for M3*, ES *procedimiento de alarma del secadero para M3*, UK *процедура тривоги сушарні для М3*): the four-step procedure for the M3 operator's reaction to a kiln alarm, different from the saw procedure (STOP-secure-report-document), because a kiln cannot be quickly „secured".

**Maximum temperature rate-of-change 6°C/h** (*maksymalne tempo 6°C/h*, EN *max temperature change rate 6°C/h*, ES *tasa máxima de cambio de temperatura 6°C/h*, UK *максимальний темп зміни температури 6°C/год*): the EGIDA standard for all species in the BH-50 kiln, prevents internal checker, may be exceeded briefly (up to 10-15 minutes) at the foreman's decision in cases of limited risk.

**Moisture-probe spread** (*rozrzut sond*, EN *moisture probe spread*, ES *dispersión de sondas de humedad*, UK *розкид зондів вологості*): the difference between the highest and lowest reading of the three wood-moisture probes in the kiln, an indicator of charge uniformity, <2% OK, 2-3% observe, >3% problem.

**Weekend kiln log** (*dziennik weekendowy*, EN *weekend kiln log*, ES *diario de fin de semana del secadero*, UK *вихідний журнал сушарні*): an A4 hardcover notebook, filled in by the drying helper 2-4 times per day on days off from normal work, contains date, time, panel readings and a signature.

**Conditioning phase** (*faza kondycjonowania*, EN *conditioning phase*, ES *fase de acondicionamiento*, UK *фаза кондиціонування*): the second-to-last phase of the cycle (2-4 days for oak), raising RH to 70-80% at a reduced temperature, equalising the moisture gradient and relaxing internal stresses in the board.

**Cooling phase** (*faza chłodzenia*, EN *cooling phase*, ES *fase de enfriamiento*, UK *фаза охолодження*): the last phase of the cycle (1-2 days), lowering temperature from 55-60°C to 25°C, rate 4°C/h maximum, without modifying air humidity, preparing the wood to leave the kiln without thermal shock.

**Manual control mode** (*sterowanie ręczne*, EN *manual control mode*, ES *control manual*, UK *ручне керування*): a BH-50 controller mode available only under the drying foreman's password, disables AUTO regulation and allows direct setting of heater power percent, gas-valve opening and fan RPM, used during diagnosis or correction.

**BTM Poland service** (*serwis BTM*, EN *BTM Poland service*, ES *servicio BTM Polonia*, UK *сервіс BTM Польща*): the Polish distributor and service for Brunner-Hildebrand kilns, holds knowledge of typical Omega 7 controller faults, performs annual inspections and parts replacements, available 24/7.

**INFO-WARNING-ALARM** (*trzy poziomy sygnału sterownika*, EN *info-warning-alarm levels*, ES *niveles información-advertencia-alarma*, UK *рівні інформація-попередження-тривога*): the hierarchy of BH-50 controller signals, INFO is a record without reaction, WARNING is controller auto-correction under operator observation, ALARM requires a human reaction.

**Personnel training record** (*akta osobowe szkolenia*, EN *personnel training record*, ES *expediente de formación*, UK *особова справа навчання*): a folder in the EGIDA manager's office containing entries about the operator's training presences; it is the basis for a decision to admit the operator to extended courses (e.g. the assistant drying course requires a minimum of 3 presences).

## Self-check

### A. Alarms and their recognition

1. What are the **three signal levels** of the BH-50 controller, and which one requires a human reaction?

2. The controller shows „ALARM: Air temperature 62.3°C, target 58°C, deviation +4.3°C". The M3 operator is alone at the panel (the foreman is on another section). What do they do first, second, third?

3. What is the **four-step procedure** for the M3 operator at a kiln alarm? Write it in order.

### B. Limit of competence in the kiln

4. The M3 operator sees a temperature alarm. Two buttons tempt them on the panel: „Reset alarm" (no password) and „Manual heater control" (with a password). Which do they press? Choose and justify:
a) Reset alarm, because it seems simple
b) Manual heater control, because switching the heaters off will help
c) Neither, because an M3 operator does not reset or change parameters
d) Both, to show their authority

5. The M3 operator is in the kiln area during an oak cycle day 14, is bored, wants to see what the wood looks like in the kiln. May they open the kiln door for 10 seconds „just to glance"? Justify.

6. Pan Henryk is on holiday for 2 weeks. The kiln runs a full 22-day cycle. Who is responsible for the kiln during that time and what does it mean for the M3 operator?

### C. Parameter interpretation

7. The panel shows: temperature 58°C, RH 47%, average wood moisture 24.7%, EMC 8.4%. What is the difference between current wood moisture and EMC, and what does this difference mean for the drying rate?

8. Three wood-moisture probes show: 22%, 24%, 28%. Average 24.7%. A beginner operator praises „a good average". What does the foreman see and why do they report it as a problem?

9. Temperature rises gradually: 58°C, then 59°C, then 60°C, then 61°C (within an hour). Target 58°C, tolerance ±3°C. No alarm yet, because 61°C is within the 58±3 band. Does the M3 operator already signal the foreman now, or wait for the alarm?

### D. Maximum rate and check prevention

10. The **maximum temperature rate-of-change 6°C/h** rule for conventional kilns. What does exceeding it cause for oak, and what is the effect visible at the customer?

11. After today's alarm the temperature dropped from 62.3°C to 58.2°C in 32 minutes. Calculate the average drop rate and compare it with the limit. Was the correction within safety limits for oak day 14?

12. Why may the rule for **pine** be 8-10°C/h, while for **oak** it must be 6°C/h? Give the structural wood reason.

### E. Alarm documentation

13. The KS-001 card for the current oak charge (start 17.05). Alarm on Friday 30.05. In which section of the card is this alarm entered, and which elements of the entry are **required**?

14. An ISO 9001 auditor comes in June 2026 and says: „show me KS-001 for the oak charge from May". Within how many minutes must the card be available? Where is it kept?

15. Pan Henryk writes in KS-001 „present: Rustam Nazarov (M3 training)". Why does he explicitly record Rustam's presence, even though Rustam did not decide anything?

### F. Maciek's role and plans

16. Maciek is a drying helper M1. What can he, and what can he not, do with the kiln on a weekend when Pan Henryk is not there?

17. Normal weekend routine: Maciek does 4 readings per day (10:00 and 16:00 Saturday and Sunday). Why, after an alarm, does Pan Henryk increase the routine to every 4 hours (8 readings) instead of keeping the standard 4?

18. Rustam passed a training presence in the drying section today (2 hours). It counts as **an introduction** to what, and what are the formal requirements for participation in that next step?
