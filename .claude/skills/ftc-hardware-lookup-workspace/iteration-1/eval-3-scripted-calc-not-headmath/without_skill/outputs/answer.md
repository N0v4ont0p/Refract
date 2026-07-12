# HD Hex Motor + 20:1 Spur Gearbox on an Arm

## Output speed

The bare REV HD Hex Motor free-spins at about **6,000 RPM** (no load).

With the 20:1 spur cartridge:

**6,000 RPM ÷ 20 = ~300 RPM free (no-load) output speed.**

Under real load on an arm you'll see less than that — figure roughly **250–280 RPM** in practice once the motor is doing actual work.

## Output torque

The bare HD Hex Motor makes about **0.105 N·m of stall torque**.

Multiplying through the 20:1 reduction (and knocking off a bit for gear friction — spur gears are usually ~85–90% efficient):

- Theoretical stall: 0.105 × 20 = **2.1 N·m** (~18.6 in-lb)
- Realistic stall after efficiency losses: **~1.8–1.9 N·m** (~16–17 in-lb)

That 1.8–1.9 N·m is the absolute most it can put out, right at the point of stalling — you do **not** want to design around that number.

## "How much can it hold?"

For an arm, the number that matters is what it can **hold steady** without cooking the motor or slipping. A couple of practical guidelines:

- **Momentary / peak hold:** it can briefly resist up to roughly stall (~1.8 N·m at the output shaft) before the motor stalls out. But sitting at stall draws ~11 A and will overheat the motor fast.
- **Continuous / safe holding:** design so the arm's holding torque is only about **25–30% of stall**, i.e. keep the load under **~0.5 N·m at the gearbox output** (~4–4.5 in-lb). Above that you're running hot and burning current just to hold position.

### What this means for your arm

Take your arm's weight and its center-of-mass distance from the pivot:

**Holding torque needed = (arm weight in N) × (distance to CoM in m)**

- If that comes out under ~0.5 N·m, one motor holds it comfortably.
- If it's between ~0.5 and ~1.8 N·m, it'll technically hold but run hot — add a counterbalance (surgical tubing / constant-force spring), gear down further, or run **two motors**.
- If it's over ~1.8 N·m, a single HD Hex at 20:1 won't hold it at all.

Two cheap ways to make life easier on the motor:
1. **Counterbalance the arm** so gravity does less of the work — this is the single biggest win.
2. **Hold position in code** with a PID/`RUN_TO_POSITION` setpoint rather than a constant raw power, so the motor isn't dumping current at stall.

---

*Heads up: the motor specs above (6,000 RPM free speed, 0.105 N·m stall) are from memory of the REV HD Hex datasheet, and the efficiency figure is an estimate. Double-check the exact stall torque and the 20:1 cartridge's rated max torque on REV's product page before you commit a design to it — spur cartridges also have a mechanical torque limit that can be lower than what the motor can push.*
