## HD Hex Motor + 20:1 spur gearbox

I pulled the base motor spec from the catalog and ran the gear math through the script (I don't do this arithmetic by hand — the numbers below come straight from `motor_math.py`).

**Part:** REV Robotics HD Hex Motor, bare — SKU `REV-41-1291`, with the REV 20:1 spur gearbox (a listed option for this motor).

### Output speed
- **~300 RPM free (no-load)** at the gearbox output.
- Base free speed is 6000 RPM at the motor shaft; ÷ 20 = 300 RPM.
- That's the *free* speed. Under an arm load it turns somewhat slower, and it's zero when the arm is holding still.

### Holding torque
"How much it can hold" is the stall torque at the output — the most it can resist before the shaft gives.

- **Ideal:** ~2.1 N·m (base stall torque 0.105 N·m × 20).
- **Realistic (what it actually delivers):** roughly **1.5–1.9 N·m**. A spur gearbox loses about 10–30% to friction, so the 2.1 figure is a ceiling, not the delivered number. Design against the lower end.

### What this means for the arm
- Size the arm so the holding torque it needs (arm weight × distance from the pivot to the center of mass, at the worst-case horizontal position) stays under ~1.5 N·m, with margin. If you're near or over that, add reduction (e.g. the 40:1 spur, or a chain/belt stage) or a second motor.
- Holding a load at stall draws high current and heats a brushed motor. If the arm has to *hold* position for long stretches, plan for a counterbalance, a passive stop/ratchet, or gravity-compensation in code rather than parking the motor at stall.
- Encoder note if you close the loop on this arm: output counts-per-rev = 28 (motor CPR) × 20 = 560 CPR at the gearbox output. Let the script compute tick math rather than eyeballing it.

**Source:** REV official docs (tier 1) — https://docs.revrobotics.com/duo-build/motion/motors/hd-hex-motor. Base values: free speed 6000 RPM, stall torque 0.105 N·m, motor-shaft encoder 28 CPR. Gear results from `scripts/motor_math.py external REV-41-1291 --ext 20`.
