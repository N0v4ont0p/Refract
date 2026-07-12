Here are the numbers for the goBILDA 5203 Yellow Jacket, 19.2:1 variant:

**Free speed:** ~312 RPM (at the output shaft)

**Encoder resolution:** 537.7 counts per revolution (CPR) of the output shaft
- The bare motor encoder is 28 counts/rev (7 cycles per rev × 4 for quadrature)
- 28 × 19.2 gear ratio ≈ 537.7 CPR at the output

**Ticks for a 96mm wheel:**
Assuming the wheel is mounted directly on the motor's output shaft (1:1, no extra reduction):

- Ticks per wheel revolution = **537.7**
- Wheel circumference = π × 96mm = **301.6 mm**
- Ticks per mm = 537.7 / 301.6 ≈ **1.783 ticks/mm**
- Or inverted: ~0.561 mm per tick

So in your odometry constants you'd use something like:
```
TICKS_PER_REV   = 537.7
WHEEL_DIAMETER  = 96.0   // mm
TICKS_PER_MM    = TICKS_PER_REV / (Math.PI * WHEEL_DIAMETER)  // ≈ 1.783
```

Two things to double check before you commit these:
1. **Gearing between motor and wheel.** The 537.7 figure is for a wheel bolted straight to the output shaft. If you have any chain/belt/gear reduction between the motor and the wheel, multiply through by that ratio.
2. **These are from memory** — 312 RPM free speed and 537.7 CPR are the values goBILDA publishes for the 5203-2402-0019 (19.2:1), but since you're wiring up odometry where a wrong constant quietly corrupts every pose estimate, pull up the goBILDA product page / spec sheet for that exact part number and confirm the 537.7 before you lock it in. goBILDA lists the exact encoder resolution per ratio right on the listing.

Note also: for odometry you usually want dead/tracking wheels rather than drive-motor encoders (drive encoders pick up wheel slip). If these 5203s are your drive motors, drive-encoder odometry works but expect drift under aggressive driving.
