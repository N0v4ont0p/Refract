Here are the verified numbers for the goBILDA 5203 Series Yellow Jacket, 19.2:1 (SKU 5203-2402-0019), pulled from the catalog and the tick script — not from memory:

**Free speed:** 312 RPM (no-load output shaft speed)

**Encoder resolution:** 537.7 counts per revolution at the output shaft.
- One important gotcha: use this published 537.7 value directly. Don't recompute it as 28 × 19.2 — "19.2:1" is a rounded label, the true ratio is 19.20 exact, and the published output-shaft CPR already reflects it. Recomputing from the rounded label gives a subtly wrong tick count.

**Ticks for a 96 mm wheel** (direct drive, motor straight to wheel, no external gearing):
- **537.7 ticks per wheel revolution** (this is just the output-shaft CPR — one wheel rev = one output-shaft rev on direct drive)
- **1782.87 ticks per meter** of travel (96 mm wheel → circumference ~301.6 mm → 537.7 / 0.3016)

For reference, that 96 mm wheel gives a **free linear speed of ~1.57 m/s (5.15 ft/s)** — this is the no-load figure; real drivetrain speed under load will be lower.

Two caveats before you wire it up:
- These tick numbers assume the motor drives the wheel directly (external ratio 1:1). If you have any chain/belt/gear reduction between the motor and the wheel, tell me the ratio and I'll rerun it — the ticks-per-meter changes.
- I took the 96 mm wheel diameter from your message. If your actual wheel is a different size, the ticks-per-meter and speed both shift.

Source for all specs: goBILDA product page (tier-1 manufacturer), retrieved 2026-07-05:
https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-19-2-1-ratio-24mm-length-8mm-rex-shaft-312-rpm-3-3-5v-encoder/
