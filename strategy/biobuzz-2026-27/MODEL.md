# BIOBUZZ 2026-27: cycle-time and expected-value model

> **DRAFT. PLAN.md §19 step 4. PROVISIONAL. Revise after the first events.**
> This is an estimate built from the manual's point values and time limits plus stated
> assumptions. It is **not** a proof of optimal strategy. No such proof exists for this kind of
> problem: matches are adversarial, information is incomplete, and human execution varies.
> Input for the §19 step 5 deliberation checkpoint. Nothing here is merged or ACTIVE.

- Model: `strategy/biobuzz-2026-27/model.py`. Stdlib only, fixed seeds, deterministic. Two runs
  gave byte-identical output (same md5).
- Run: `python3 model.py` (full report, about 7 s) and `python3 model.py --self-test`.
- Sources: `season-extensions/biobuzz-2026-27.yaml`, plus manual text via
  `rules.py section/lookup/term --season biobuzz-2026-27` (§10.1, 10.3.1, 10.4, 10.5.x; G402,
  G407, G409, G410, G417, G418, G426, G427; TIP, CONTROL, LAUNCH, PARK, LEAVE), and Tables 10-2
  and 10-3 from the structured manual-table copies.
- Nothing about BIOBUZZ comes from memory.

---

## 1. Method

**What is simulated.** One alliance: 2 robots sharing 1 HIVE, 1 NECTAR pool, a POLLEN budget,
the FLOWERS and the GARDEN. It is an event-driven Monte Carlo.

- Each robot runs a sequence of phases.
- Phase timelines:
  - AUTO: 0–30 s.
  - TELEOP: 30–150 s on the model clock.
  - The 8 s transition is skipped, because G403 forbids powered movement then.
- Robots are resumed in time order, so both robots' launches land in the same CELL in the right
  sequence.

**Robot phases**

| phase | when | what happens |
|---|---|---|
| AUTO launch | 0 – (30 − AUTO park travel) | First volley is the 4 preloads after `AUTO_FIRST_VOLLEY_S`. Later cycles take `cycle × AUTO_CYCLE_FACTOR`. |
| TELEOP launch | until end − park travel (flower robots stop early) | Cycle = `cycle × DEFENSE_CYCLE_MULT`, plus `NECTAR_EXTRA_S` if the load includes NECTAR. |
| GARDEN | same windows, for GARDEN robots | Deliver up to capacity per trip. |
| FLOWER | last 60 s only (G410) | One FLOWER per trip. POLLEN first, NECTAR placed last so it is top-most (owns the FLOWER) and also bottom-most (Bottom NECTAR Bonus). Partway through, the partner fills a different FLOWER. Falls back to launching when no FLOWERS or NECTAR are left. |
| PARK | reserved travel at the end of AUTO and TELEOP | Bernoulli success. |

**Rules and mechanics built in**

- **Capacity (G407).** A robot takes at most `capacity ≤ 4` elements at the start of each cycle
  and holds them until the volley. This is what limits elements per cycle.
- **HIVE TIP accounting.** Each element hit into the upward CELL adds its POLLEN-equivalent (eq).
  - The HIVE tips when `eq(up) − eq(down) ≥ T0`.
  - The first CELL holds 3 staged NECTAR. Each is worth `(T0 − FIRST_TIP_LAUNCHED_EQ)/3` in that
    draw, so the first tip needs about 3 POLLEN and later empty-CELL tips need about 8. This
    matches the setup-guide calibration.
  - Elements in the same volley after a tip land in the new upward CELL.
- **Spill on TIP (ASSUMPTION, with alternatives).**
  - Each element in the tipping CELL is retained with probability `SPILL_RETAIN_FRAC`. Otherwise it
    spills to the floor: POLLEN goes back to the budget, NECTAR to the field pool.
  - Retained elements have torque weight `RETAINED_COUNTERWEIGHT`. That weight applies while they
    are down (resisting the next tip) and after they rotate back up (helping).
  - Retained elements also lock up supply. They score 2 pts only if their CELL is upward at the end.
- **Human NECTAR (G426/G427).**
  - Each own-HIVE tip moves 1 of the 5 ALLIANCE AREA NECTAR onto the field (G426.A).
  - At 1:00 left, all remaining NECTAR enter (G426.B).
  - Launchers that fire NECTAR keep enough on the field to reserve one per untouched FLOWER.
- **Scoring (Table 10-2).**
  - LEAVE 3; AUTO/TELEOP PARK 5/5.
  - TIP 20. TIPS finished in AUTO are assessed as AUTO (§10.5.B); the value is the same.
  - 2 pts per element in the upward CELL at the end. This includes the 3 staged NECTAR, so an
    alliance that never launches still gets 6 points.
  - FLOWER: owner gets 2 per element counted as in the FLOWER (at most `FLOWER_CAPACITY`), with a
    chance an opponent steals ownership. Bottom NECTAR Bonus 5.
  - GARDEN: 1 per element, staged POLLEN included.
- **RP (Tables 10-2 and 10-3, "All Other Events").**
  - SWARM: LEAVE+PARK ≥ 16.
  - POLLINATOR 1: TIPS ≥ 4. POLLINATOR 2: TIPS ≥ 7.
  - WIN 3, TIE 1.
  - Win% is measured against an independently simulated reference opponent (mid launcher x2).

**Monte Carlo.** Each match draws every ASSUMPTION uniformly from its [low, high] range. Integer
parameters are drawn uniformly over their integers. Cycle time and hit rate are drawn per robot
inside that profile's range.

**Sensitivity.** A tornado pins one parameter at its low end, then at its high end. Every other
parameter keeps being drawn (common seed). Each row is a conditional expectation. With 1000
matches per cell, swings under about 3 pts or 0.05 RP are noise.

---

## 2. Every input

### MANUAL (exact; cited in code)

- **Timing:** AUTO 30 s, transition 8 s, TELEOP 120 s (§10.1). Last-60-s unlock (G410, G426.B,
  Table 9-1).
- **Capacity:** 4 (G407).
- **Staging (§10.3.1):**
  - 4 POLLEN preloaded per robot.
  - 3 NECTAR in the upward CELL; 5 in the ALLIANCE AREA.
  - 4 POLLEN in each of 4 FLOWERS; 4 in each GARDEN; 40 POLLEN total.
- **Points:** Table 10-2.
- **RP thresholds:** Table 10-3. Championship thresholds are TBA and **not** modelled.

### SETUP-GUIDE (Event Field Setup Guide V1.0 §12.3; a field document, not a rule)

| parameter | low / nominal / high | why |
|---|---|---|
| `TIP_T0_EQ` | 6.5 / 7.5 / 9.0 | Empty CELL: 7th POLLEN no tip, 8th tips, so the threshold is in (7, 8]. Widened so a tip can come on the 7th–9th POLLEN, because the guide says fields vary. The widening is an ASSUMPTION. |
| `FIRST_TIP_LAUNCHED_EQ` | 1.5 / 2.5 / 3.5 | With 3 NECTAR in the CELL, the 3rd POLLEN tips, so (2, 3]. Widened to the 2nd–4th POLLEN (ASSUMPTION). |

### ASSUMPTION (all ranges; none are measurements)

| parameter | low / nom / high | why this range |
|---|---|---|
| `NECTAR_TIP_EQ` | 1.0 / 1.5 / 1.9 | Tip weight of a **launched** NECTAR. The calibration pair implies 3N ≈ 5P (1.67) for NECTAR staged against the back wall. But the guide says 3P+3N has *less mass* than 8P, so tipping isn't mass-only, and launched NECTAR lands anywhere. 1.0 = no advantage. |
| `SPILL_RETAIN_FRAC` | 0 / 0 / 0.5 | The manual only says elements "spill out of a TIPPED HIVE" (G409 intent) and doesn't say how completely. Nominal is full spill; 0.6 is tested as an alternative. |
| `RETAINED_COUNTERWEIGHT` | 0 / 1 / 1 | Does a retained element add torque? 1 = simple lever. 0 = wedged near the pivot, no torque. Only matters when retention > 0. |
| `AUTO_FIRST_VOLLEY_S` | 3 / 5 / 8 | Drive to a launch spot and fire preloads; no intake needed. |
| `AUTO_CYCLE_FACTOR` | 1.0 / 1.25 / 1.6 | Path-planned intake in AUTO is usually slower than a driver. |
| `AUTO_PARK_TRAVEL_S`, `TELEOP_PARK_TRAVEL_S` | 2.5 / 4 / 7 | LOADING ZONE position relative to the HIVE is FIGURE-ONLY. |
| `P_LEAVE` | 0.95 / 0.98 / 1 | Trivial criterion (off the wall), but software and hardware can fail. |
| `P_AUTO_PARK` | 0.80 / 0.90 / 1 | The 23x11 in zone is small; "at least partially in" is lenient. |
| `P_TELEOP_PARK` | 0.85 / 0.93 / 1 | Two robots plus human NECTAR entry (G427.C) share one zone. |
| `DEFENSE_CYCLE_MULT` | 1.0 / 1.1 / 1.4 | Traffic and defense in TELEOP only. G402 protects AUTO. |
| `CYCLE_Q`, `HIT_Q` | 0 / 0.5 / 1 | Position inside each profile's cycle and hit range. |
| `NECTAR_HIT_FACTOR` | 0.8 / 0.9 / 1.0 | 3.6 in NECTAR vs 2.8 in POLLEN (§9.8) through one launcher. |
| `NECTAR_EXTRA_S` | 0 / 2 / 5 | NECTAR sits in the LOADING ZONE or the spill area, not wherever the POLLEN is. |
| `POLLEN_SHARE` | 12 / 16 / 24 | POLLEN this alliance can cycle. MANUAL: 16 preload + 16 FLOWER = 32 non-GARDEN POLLEN, /2 = 16. Low = opponent wins the floor. High = also raids the 8 GARDEN POLLEN. |
| `FLOWER_CAPACITY` | 5 / 6 / 7 | Elements at least partly in the scoring volume. Top ring is 21.5 in; the middle-ring height is FIGURE-ONLY. |
| `FLOWER_STAGED_REMAIN` | 0 / 2 / 3 | Staged POLLEN still in the scoring volume at 1:00. Robots can pull POLLEN from the bottom (G418.B), and the manual's overview says AUTO collects "POLLEN from FLOWERS". |
| `FLOWERS_ACCESSIBLE` | 2 / 3 / 4 | FLOWER positions are FIGURE-ONLY. |
| `FLOWER_PRESTAGE_FRAC` | 0 / 0.5 / 0.8 | Gathering or driving before 1:00. Placement is always after 1:00 (asserted). |
| `P_FLOWER_STOLEN_OPEN` / `_FULL` | 0–0.6 / 0–0.25 | Opponent tops our NECTAR. A full FLOWER needs POLLEN pulled out of the bottom first. |
| `P_OPP_NECTAR_FIRST` | 0 / 0.2 / 0.5 | Opponent NECTAR is already lowest, so no bonus for us. |
| `GARDEN_STAGED_REMAIN` | 2 / 4 / 4 | GARDENS aren't protected (§10.5.3). |
| `P_GARDEN_STAYS` | 0.6 / 0.85 / 1 | The GARDEN is a 2 in strip and balls roll. |
| Profile cycle / hit ranges | slow 24–34 s, 0.50–0.80; mid 15–22 s, 0.65–0.90; fast 9–14 s, 0.80–0.95; flower trip 12–20 s (fast-all 10–16); GARDEN trip 14–24 s | These *define* the capability being asked about. They are not predictions of any robot. |

**Structural simplifications (not parameters)**

- Opponents only enter through the parameters above.
- No fouls. That leaves out, for example, a G410 MAJOR per early NECTAR and G426/G427 MINORs.
- No breakdowns and no AUTO path conflicts (G402).
- No adaptive strategy switching.
- Pulling FLOWER POLLEN for ammo isn't linked to `FLOWER_STAGED_REMAIN`.
- POLLEN placed into FLOWERS before 1:00 isn't modelled (open Q&A item).
- Launching into a FLOWER isn't modelled (open Q&A item).
- Human NECTAR entry is instantaneous.
- Uniform priors aren't calibrated to anything.

---

## 3. Results (excerpts of `python3 model.py`, seed 20260912)

### 3.1 Nominal points per robot-second (analytic)

| action | pts | seconds | pts/s |
|---|---:|---:|---:|
| TELEOP PARK (travel only) | 5.0 | 4.0 | 1.25 |
| FLOWER, first trip to a fresh FLOWER (mid trip) | 15.4 | 17.6 | 0.87 |
| Launch 4 NECTAR, mid launcher (tip value only) | 11.2 | 22.4 | 0.50 |
| Launch 4 POLLEN, fast launcher (tip value only) | 9.3 | 12.7 | 0.74 |
| Launch 4 POLLEN, mid launcher (tip value only) | 8.3 | 20.4 | 0.41 |
| Launch 4 POLLEN, mid, end-of-match CELL value only | 6.2 | 20.4 | 0.30 |
| GARDEN 4 POLLEN (mid trip) | 3.4 | 20.9 | 0.16 |

A tip is worth 20/7.5 = 2.67 pts per in-CELL POLLEN-eq over the long run. A launched element that
never completes a tip is still worth 2 pts if it is in the upward CELL at the end.

### 3.2 Alliances (Monte Carlo, 2000 matches each)

Win% and E[RP] are against the mid launcher x2 reference, drawn independently.

| alliance | mean | p10 | p90 | AUTO | TELEOP | tips | P(SWARM) | P(POLL1) | P(POLL2) | E[bonus RP] | win% | E[RP] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| park/leave only | 33 | 29 | 36 | 15 | 18 | 0.0 | 0.99 | 0.00 | 0.00 | 0.99 | 0 | 0.99 |
| garden + park | 48 | 41 | 54 | 15 | 33 | 0.0 | 0.99 | 0.00 | 0.00 | 0.99 | 0 | 0.99 |
| slow launcher x2 | 86 | 72 | 101 | 34 | 52 | 2.4 | 1.00 | 0.04 | 0.00 | 1.03 | 8 | 1.29 |
| mid launcher x2 | 120 | 92 | 146 | 36 | 84 | 4.0 | 0.99 | 0.70 | 0.01 | 1.71 | 49 | 3.18 |
| fast launcher x2 | 172 | 94 | 232 | 50 | 122 | 6.5 | 1.00 | 0.79 | 0.59 | 2.38 | 79 | 4.75 |
| mid x2, no AUTO park | 116 | 82 | 146 | 32 | 84 | 4.2 | 0.81 | 0.73 | 0.04 | 1.57 | 42 | 2.86 |
| mid x2, never park | 108 | 74 | 138 | 32 | 76 | 4.3 | 0.00 | 0.74 | 0.05 | 0.79 | 35 | 1.84 |
| mid+NECTAR ammo x2 | 130 | 106 | 157 | 36 | 94 | 4.6 | 0.99 | 0.86 | 0.05 | 1.91 | 61 | 3.74 |
| mid+NECTAR x2, no human | 124 | 100 | 148 | 36 | 88 | 4.2 | 0.99 | 0.78 | 0.02 | 1.79 | 53 | 3.38 |
| mid + mid/flower | 130 | 103 | 157 | 36 | 94 | 3.1 | 1.00 | 0.32 | 0.00 | 1.31 | 61 | 3.15 |
| mid/flower x2 | 126 | 103 | 151 | 37 | 90 | 2.5 | 0.99 | 0.11 | 0.00 | 1.11 | 57 | 2.84 |
| mid + flower/garden | 96 | 77 | 119 | 30 | 66 | 1.4 | 0.99 | 0.00 | 0.00 | 0.99 | 18 | 1.53 |
| fast + park-only | 107 | 65 | 140 | 35 | 72 | 3.3 | 1.00 | 0.50 | 0.01 | 1.51 | 36 | 2.60 |
| fast-all x2 | 184 | 143 | 228 | 49 | 135 | 5.4 | 0.99 | 0.88 | 0.23 | 2.11 | 95 | 4.97 |

### 3.3 Capacity per cycle (G407), mid launcher x2

| capacity | mean pts | tips | P(POLL1) | P(POLL2) |
|---:|---:|---:|---:|---:|
| 2 | 91 | 2.6 | 0.06 | 0.00 |
| 3 | 108 | 3.4 | 0.46 | 0.00 |
| 4 | 120 | 4.0 | 0.70 | 0.01 |

### 3.4 HIVE spill alternatives (other parameters Monte Carlo, 1000 matches)

| alliance | retain | counter-weight | tips | CELL pts at end | P(POLL1) | P(POLL2) | mean pts |
|---|---:|---:|---:|---:|---:|---:|---:|
| mid x2 | 0.0 | 1 | 4.7 | 7.2 | 0.93 | 0.04 | 129 |
| mid x2 | 0.3 | 1 | 3.6 | 14.9 | 0.53 | 0.01 | 114 |
| mid x2 | 0.3 | 0 | 4.3 | 13.0 | 0.78 | 0.02 | 126 |
| mid x2 | 0.6 | 1 | 2.1 | 21.8 | 0.06 | 0.00 | 91 |
| mid x2 | 0.6 | 0 | 3.3 | 19.9 | 0.40 | 0.00 | 113 |
| fast x2 | 0.0 | 1 | 8.7 | 6.9 | 1.00 | 0.94 | 207 |
| fast x2 | 0.3 | 1 | 5.7 | 17.1 | 0.71 | 0.44 | 157 |
| fast x2 | 0.3 | 0 | 6.9 | 15.6 | 0.88 | 0.61 | 180 |
| fast x2 | 0.6 | 1 | 2.2 | 23.4 | 0.11 | 0.01 | 95 |
| fast x2 | 0.6 | 0 | 3.6 | 21.9 | 0.43 | 0.06 | 122 |
| mid+NECTAR x2 | 0.0 | 1 | 4.9 | 5.6 | 0.93 | 0.06 | 130 |
| mid+NECTAR x2 | 0.6 | 1 | 3.1 | 21.7 | 0.28 | 0.00 | 111 |
| mid+NECTAR x2 | 0.6 | 0 | 4.4 | 19.7 | 0.84 | 0.02 | 136 |

### 3.5 Tip-threshold sweep (empty-CELL eq)

| alliance | T0 | tips | P(POLL1) | P(POLL2) | mean pts |
|---|---:|---:|---:|---:|---:|
| mid x2 | 6.5 | 4.8 | 0.88 | 0.06 | 134 |
| mid x2 | 9.0 | 3.4 | 0.50 | 0.00 | 110 |
| fast x2 | 6.5 | 8.4 | 0.90 | 0.79 | 206 |
| fast x2 | 7.5 | 6.7 | 0.82 | 0.61 | 175 |
| fast x2 | 9.0 | 5.4 | 0.70 | 0.41 | 152 |
| mid+NECTAR x2 | 6.5 | 5.2 | 0.96 | 0.12 | 141 |
| mid+NECTAR x2 | 9.0 | 4.0 | 0.71 | 0.00 | 119 |

---

## 4. Sensitivity ranking (tornado, in text)

### 4a. Reference alliance: mid launcher + mid launcher/flower

Baseline 130 pts, 1.31 bonus RP.

| rank | parameter (low → high) | pts swing | bonus-RP swing |
|---:|---|---:|---:|
| 1 | `CYCLE_Q` (fastest → slowest end of 15–22 s) | −31 | −0.49 |
| 2 | `POLLEN_SHARE` 12 → 24 | +28 | +0.38 |
| 3 | `DEFENSE_CYCLE_MULT` 1.0 → 1.4 | −21 | −0.37 |
| 4 | `TIP_T0_EQ` 6.5 → 9.0 | −20 | −0.46 |
| 5 | `HIT_Q` (0.65 → 0.90 hit) | +18 | +0.38 |
| 6 | `SPILL_RETAIN_FRAC` 0 → 0.5 | −18 | −0.44 |
| 7 | `FLOWER_STAGED_REMAIN` 0 → 3 | +13 | +0.02 |
| 8 | `RETAINED_COUNTERWEIGHT` 0 → 1 | −9 | −0.16 |
| 9 | `P_FLOWER_STOLEN_OPEN` 0 → 0.6 | −7 | 0 |
| 10 | `AUTO_CYCLE_FACTOR` 1.0 → 1.6 | −7 | −0.18 |
| 11–13 | `P_OPP_NECTAR_FIRST`, `FLOWERS_ACCESSIBLE`, `FIRST_TIP_LAUNCHED_EQ` | about 5–6 | ≤ 0.11 |
| 14+ | park/leave reliabilities and travel, GARDEN, `FLOWER_CAPACITY` | ≤ 4 | ≤ 0.13 |

The NECTAR parameters show 0 here only because this alliance doesn't fire NECTAR. See 4c.

**Exchange rates** (model-derived, provisional):

- About **4.5 pts per 1 s** of cycle time, for both robots. `CYCLE_Q` spans 7 s.
- About **0.7 pts per +1 percentage point** of hit rate.
- A turret, vision or intake upgrade is worth it only if it moves these numbers by a comparable
  amount.

### 4b. Last-minute FLOWER play vs keep launching

This compares (mid + mid/flower) minus (mid x2). Baseline: **+9.9 pts, −0.39 bonus RP.**

- **Swing drivers:**
  - `FLOWER_STAGED_REMAIN` 0→3: +3.5 → +16.1 pts.
  - `P_FLOWER_STOLEN_OPEN` 0→0.6: +13.2 → +6.3.
  - `P_OPP_NECTAR_FIRST` 0→0.5: +13.0 → +6.7.
  - `FLOWERS_ACCESSIBLE` 2→4: +5.9 → +11.3.
  - `TIP_T0_EQ` 6.5→9: +6.5 → +11.3. Harder tips make FLOWERS relatively better.
- **RP cost:** stays between −0.24 and −0.46 in every one of the top-10 rows. Across the top-10 rows the RP cost
  is robust; the points gain is not.

### 4c. NECTAR as launcher ammo (intake and launcher handle both diameters)

This compares (mid+NECTAR x2) minus (mid x2). Baseline: **+10.1 pts, +0.19 bonus RP.**

- **Swing drivers:**
  - `POLLEN_SHARE` 12→24: **+27.0 → −0.1**.
  - `NECTAR_TIP_EQ` 1.0→1.9: −0.5 → +20.0.
  - `SPILL_RETAIN_FRAC` 0→0.5: +1.4 → +19.4.
  - `NECTAR_EXTRA_S` 0→5: +18.4 → +2.8.
  - `NECTAR_HIT_FACTOR` 0.8→1.0: +4.3 → +13.1.
- **Reading:** NECTAR ammo mostly insures against POLLEN scarcity. Each alliance has 8 NECTAR it
  alone may CONTROL (G408), and NECTAR may tip more per slot. If POLLEN is plentiful and NECTAR
  tips like POLLEN, it is worth about nothing.

---

## 5. What this says (provisional, under the stated assumptions)

1. **LEAVE + PARK is the most time-efficient scoring in the game.**
   - It earns up to 26 pts for about 8 robot-seconds of travel (1.25 pts/s, versus 0.4–0.9 for
     anything else).
   - It carries the SWARM RP. One robot alone maxes at 13 < 16, so SWARM needs both partners.
   - AUTO PARK lifts P(SWARM) from 0.81 to 0.99 and is net +4 pts for mid launchers.
   - Never parking costs about 12 pts and 0.9 RP.
   - A do-nothing-but-park alliance scores about 33. That includes 6 free CELL points from the
     staged NECTAR and the staged GARDEN POLLEN.
   - This is the most robust conclusion here: it barely moves in the tornado.
2. **HIVE launching is the main points engine and the only route to POLLINATOR RP.**
   - Cycle time and hit rate are the two biggest levers a team controls.
   - A robot that holds all 4 elements (G407) is worth about +12 pts and +0.24 P(POLL1) over one
     that holds 3. Build to exactly 4.
   - POLLINATOR 1 (4 TIPS) looks reachable for two ~15–22 s launchers (P ≈ 0.7).
   - POLLINATOR 2 (7 TIPS) looks realistic only for two ~9–14 s launchers (≈ 0.6), and only if
     spill is near-complete and fields sit near calibration.
3. **"Carry" looks weak.** Fast launcher + park-only (107) scores below mid x2 (120).
   Two decent launchers beat one great one, partly because they cycle in parallel into one HIVE.
4. **GARDEN delivery looks time-inefficient** (0.16 pts/s). Paired with a launcher it is
   *harmful* in the model: GARDEN is a POLLEN sink that starves the HIVE (mid + flower/garden 96 vs
   mid x2 120).
5. **FLOWER play in the last minute trades RP for points.**
   - The first trip into a fresh FLOWER is efficient per second.
   - Switching one mid robot at 1:00 gains about +10 pts (win% 49 → 61 vs the reference) but costs
     about 0.4 bonus RP, because POLLINATOR 1 is lost more often. E[RP] comes out roughly equal
     (3.15 vs 3.18).
   - FLOWER capability looks worth having for flexibility. When to use it should depend on the
     live TIP count. For example: switch at 1:00 only if 4 TIPS are already done. **This adaptive
     policy is not modelled yet.** It is the obvious next thing to test.
6. **NECTAR as ammo plus human NECTAR entry (G426)** is worth about +10 pts / +0.2 RP on average.
   Human entry alone is worth about +6 pts for a NECTAR-capable alliance. The value is conditional
   on POLLEN scarcity and NECTAR tip weight (4c), both unmeasured.

## 6. What this does NOT say

- **Not optimal strategy.** It compares a handful of hand-picked profiles and fixed policies. No
  search, no adaptation, no game theory.
- **No real opponent model.**
  - Defense is only a cycle multiplier.
  - FLOWER contest and POLLEN competition are only probabilities and a share.
  - Win% uses an independent, non-interacting opponent.
  - There are no fouls, cards or breakdowns.
- **Human execution variance** is only partly represented: park reliability, and hit rate as a
  range. Driver fatigue, missed 1:00 timing (G410 MAJOR per NECTAR) and human-player entry fouls
  (G426/G427 MINOR) are absent.
- **Parameter ranges are priors, not data.** Uniform draws aren't calibrated. Nominal isn't the
  mean. Profile ranges describe hypothetical robots.
- **Tornado limits.** Single-parameter tornados hide interactions. Retention × counter-weight is
  one example, which is why §3.4 is shown as a grid.
- **Out of scope:** Championship and Regional RP thresholds (TBA), and Premier Event modifications.

## 7. Uncertainties, and the measurements that would reduce them most

The list is ordered by how much each measurement would move §4.

1. **POLLEN availability in real matches** (`POLLEN_SHARE`, #2 overall, #1 for the NECTAR-ammo
   decision).
   - From early-event video, count loose floor POLLEN over time.
   - Count elements sitting in HIVES, FLOWERS, GARDENS and robots at about 1:30 and at 1:00.
2. **HIVE spill behavior** (`SPILL_RETAIN_FRAC`, `RETAINED_COUNTERWEIGHT`).
   - On a real HIVE, tip it repeatedly. Count what stays in the downward CELL.
   - Count POLLEN-to-next-tip with those elements present.
   - This alone moves fast-alliance P(POLL2) from 0.94 (full spill) to 0.01 (60% retained with counter-weight), §3.4.
3. **Tip counts on several event fields** (`TIP_T0_EQ`, `FIRST_TIP_LAUNCHED_EQ`,
   `NECTAR_TIP_EQ`).
   - LAUNCHED (not placed) POLLEN to tip an empty CELL and a staged CELL.
   - LAUNCHED NECTAR to tip an empty CELL.
   - Record the field-to-field spread, not one number.
4. **Our own cycle-time and hit-rate distributions** (`CYCLE_Q`, `HIT_Q`, `DEFENSE_CYCLE_MULT`).
   - Timed practice cycles: intake 4, drive, volley.
   - Include hit rate for POLLEN and NECTAR separately, and runs with a partner robot in traffic.
5. **FLOWER geometry and state at 1:00** (`FLOWER_CAPACITY`, `FLOWER_STAGED_REMAIN`).
   - Middle-ring height from the CAD Reference.
   - Whether staged POLLEN sit in the scoring volume.
   - How many are left at 1:00 in real matches.
   - How often opponents top or steal FLOWERS.
6. **LOADING ZONE park** with two robots and human NECTAR entry: travel time and success rate.

## 8. Ties to the season yaml's open deliberation questions

| yaml `open_questions` id | how the model treats it | what would change |
|---|---|---|
| `tip-threshold` | Range (§3.5). First tip ~3 POLLEN, later ~8, per setup-guide calibration. | Measurement #3. POLL2 viability moves most. |
| `cell-height` | Not modelled directly. It only enters through the hit-rate and cycle-time ranges. | Once measured, launcher geometry sets realistic `HIT_Q`/`CYCLE_Q`, the #1 and #5 sensitivities. |
| `launch-into-flower` | Excluded; placement only. | If legal, FLOWER trip time drops and §5.5 shifts toward FLOWERS. |
| `pollen-flower-before-60s` | Excluded; no pre-1:00 FLOWER POLLEN. | If allowed without penalty, pre-filling FLOWERS makes the 1:00 NECTAR trip much more valuable (`FLOWER_STAGED_REMAIN` is #1 in 4b). |
| `opponent-nectar-garden` | Not modelled. | Low stakes: GARDEN is already the least efficient action. |
| `loading-zone-conflict` | Covered by `P_TELEOP_PARK`, `NECTAR_EXTRA_S`, and the G426.B entry at 1:00. | PARK is the most time-efficient action, so an alliance protocol ("human enters all NECTAR at 1:00, robots park after") protects SWARM. |
| `turret-value` | Not a profile. Use the §4a exchange rates. | A turret earns its place only if it cuts several seconds per cycle or adds many hit-rate points *measured*, not assumed. |
| `intake-two-diameters` | The `nectar_ammo` capability (§4c). | Worth about 10 pts / 0.2 RP on average, but conditional on measurements #1 and #3. Measure before committing intake geometry to both diameters. |

---

## 9. Run output excerpts

`python3 model.py --self-test`:

```
self-test OK: 7 groups of invariants passed
```

**Invariant groups**

1. The park/leave-only alliance with certain reliability scores exactly LEAVE+PARK = 2*(3+5+5) = 26
   every match, total 26 + 6 (staged CELL NECTAR) + 4 (staged GARDEN) = 36, AUTO = 16, 0 TIPS,
   SWARM earned.
2. One park-only robot plus a do-nothing robot gets 13, no SWARM.
3. RP thresholds are read from the constants at call time. Raising SWARM to 27 removes SWARM;
   POLLINATOR thresholds of 0 award both.
4. HIVE accounting matches the calibration.
   - 3rd POLLEN tips a staged CELL; 8th tips an empty CELL; 5 NECTAR at 1.5 eq tip.
   - Staged NECTAR spill to the field; G426.A human entries = TIPS.
   - Full retention with counter-weight needs 16 POLLEN and returns retained elements upward.
   - Retention without counter-weight tips on the 8th and retained elements add 0 eq.
5. Over Monte Carlo runs of every alliance:
   - All point components ≥ 0; total = AUTO + TELEOP.
   - Max load ≤ 4 (G407).
   - Every FLOWER placement after 1:00 (G410).
   - Human entries ≤ 5, pre-1:00 entries ≤ TIPS, none without a human (G426).
   - POLL2 ⇒ POLL1; AUTO points bounded.
   - Profile capacity ≤ 4; every range low ≤ nominal ≤ high.
   - MANUAL staging sums to 40 POLLEN / 8 NECTAR.
6. Determinism: same seed gives identical results.
7. Launchers tip, and fast launchers tip more than slow ones.

`python3 model.py` (header and §1; the full tables are reproduced in §3–§4 above):

```
# BIOBUZZ 2026-27 quant model output -- DRAFT, §19 step 4, PROVISIONAL (revise after first events)
seed=20260912  matches/config=2000

## 1. Nominal points per robot-second (analytic, no RP, no interaction)

Tip value per in-CELL eq = 20/7.5 = 2.67 pts (long-run, ignores end-of-match partial fill)
...
### 6b. Last-minute FLOWER play: (mid + mid/flower) minus (mid x2). Baseline delta +9.9 pts, -0.39 bonus RP.
### 6c. NECTAR as launcher ammo: (mid+NECTAR x2) minus (mid x2). Baseline delta +10.1 pts, +0.19 bonus RP.
```

*DRAFT — §19 step 4. Revise after the first events with scouting data: re-fit `CYCLE_Q`/`HIT_Q`
per team, replace the uniform priors with measured tip and spill counts, and add an adaptive
"switch to FLOWERS if TIPS ≥ 4" policy.*
