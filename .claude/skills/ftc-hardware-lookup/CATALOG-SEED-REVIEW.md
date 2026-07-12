# Hardware catalog seed — Rule-7 review checkpoint

**This is a separate sign-off gate (your instruction).** The catalog seed is NOT "done" because the
files parse — it is done when every value below is confirmed Rule-7-verified against its source.
**Status correction:** the SKILL.md body and eval were completed on a "continue" instruction before
this gate closed. That does not shortcut the gate — this sign-off still governs the VALUES, and the
body reads every value FROM the catalog at runtime, so anything flagged here propagates on correction
without a body edit. The gate stays open until you check the values below.

Every value was fetched from a manufacturer page this session (2026-07-05), tier-1. Verify any row by
opening its source URL. Values are stored **as published**; unit conversions are done by
`motor_math.py`, not baked into the catalog.

## Motors (`references/catalogs/motors.json`)

| SKU | Field | Seeded value | Source (tier-1) |
|---|---|---|---|
| 5203-2402-0019 | ratio / no-load RPM | 19.2:1 / 312 RPM @12V | gobilda.com 5203 19.2:1 page |
| | no-load current | 0.25 A | same |
| | stall torque | 24.3 kg·cm (338 oz-in) | same |
| | stall current | 9.2 A | same |
| | encoder CPR (output) | 537.7 | same — **note: reflects exact ratio; 537.7/28=19.20. Do not recompute from "19.2"** |
| | max output power | *not listed* (abstain) | — |
| 5203-2402-0014 | ratio / no-load RPM | 13.7:1 / 435 RPM @12V | gobilda.com 5203 13.7:1 page |
| | stall torque / current | 18.7 kg·cm (260 oz-in) / 9.2 A | same |
| | encoder CPR (output) | 384.5 | same — 384.5/28=13.73 exact (label rounds to 13.7) |
| REV-41-1291 | HD Hex bare: free speed | 6000 RPM | docs.revrobotics.com HD Hex |
| | stall torque / current | 0.105 N·m / 8.5 A | same |
| | free current / max power | 0.4 A / 15 W | same |
| | encoder CPR (motor) | 28 (at motor shaft) | same — output CPR = 28 × gearbox, computed by script |
| | listed gearboxes | UltraPlanetary 4:1,5:1; spur 20:1,40:1 | same |
| REV-41-1300 | Core Hex: ratio / RPM | 72:1 / 125 RPM output | revrobotics.com Core Hex page |
| | stall torque / current | 3.2 N·m / 4.4 A | same |
| | encoder CPR (output) | 288 | same |
| | free current | *not listed* (abstain) | — |

## Servos (`references/catalogs/servos.json`)

| SKU | Field | Seeded value | Source |
|---|---|---|---|
| 2000-0025-0002 | operating voltage | 4.8–7.4 V | gobilda.com 2000 series 25-2 page |
| | stall torque | 240/300/350 oz-in @ 4.8/6.0/7.4V | same — **voltage-dependent; never quote one figure without the voltage** |
| | no-load speed | 0.25/0.20/0.17 s/60° @ 4.8/6.0/7.4V | same |
| | rotation (standard mode) | 300° | same |

## Two Rule-7 points worth an explicit look

1. **Encoder CPR is published at the OUTPUT shaft and reflects the EXACT (non-rounded) gear ratio.**
   537.7 (not 28×19.2=537.6) and 384.5 (not 28×13.7=383.6). The catalog stores the published value
   and the tick-math uses it directly. This is the same class of error as the 21813 matrix: the
   "obvious" recomputation from the round label is subtly wrong, and only using the source value is
   right. Flagged in the JSON `_note` fields.
2. **The abstention path is load-bearing and tested.** `motor_math.py` on any SKU not in the catalog
   exits 3 with an explicit refusal + the list of known SKUs — it does not guess. Verified this session
   with an unseeded SKU string (`5203-2402-0027`, used only as a not-in-catalog probe — I have NOT
   verified that string is the real 26.9:1 part number, and the skill wouldn't need it to: any SKU not
   in the catalog abstains). Coverage gaps are safe; the only unsafe thing would be a fabricated value,
   which the structure prevents.

## What is deliberately NOT seeded (abstain, per INDEX.json)

Other 5203/5202 ratios · assembled UltraPlanetary figures · batteries (legality → rules Table 12-4) ·
wheels (diameter comes from team config) · sensors. Each abstains with a manufacturer pointer.

## Sign-off

- [x] Values spot-checked against sources — **APPROVED 2026-07-08**: Rule-7 sourcing real and specific, encoder-CPR handling applies (not restates) the 21813 lesson, abstention verified not assumed, not-seeded list honest not padded.
- [x] Approved → body already built around this seed (eval passed); seed now signed off.
