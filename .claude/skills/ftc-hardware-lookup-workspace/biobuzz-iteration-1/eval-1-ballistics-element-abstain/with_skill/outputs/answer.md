**Short version: I can't give you a hood angle that accounts for drag yet, because the repo has no measured drag data for BIOBUZZ POLLEN. The angle without drag is 20.01° (low arc).**

I ran the trajectory solver with your numbers (distance 120 in, height 24 in, speed 400 in/s, season biobuzz-2026-27, element pollen):

| | Low arc | High arc |
|---|---|---|
| Angle without drag | **20.01°** | 81.3° |
| Angle with drag | none (solver refused) | none (solver refused) |
| Can the shot reach? | yes | yes |

- **Gravity:** 386.4 in/s², from `references/physics/invariants.json`. The skill notes this was corrected from a source team's value of 385.
- **Why there's no drag answer:** the solver found no constants file for this season (`physics/biobuzz-2026-27/` has none). Its message was: "no ballistics constants for element 'pollen' in season 'biobuzz-2026-27' (have: [])". I did not borrow DECODE's ball file instead. That file describes a 5 in hollow 75 g ball, which is a different game piece, so a drag angle from it would be wrong.
- **Why nobody has the numbers:** the BIOBUZZ manual gives POLLEN as roughly 2.8 in but doesn't state its mass. Manufacturer listings exist, but they're less reliable and don't say which listed size is POLLEN and which is NECTAR. Someone has to measure a real one.
- **What the 20.01° means:** it's a correct no-drag answer and a reasonable starting hood setting. Drag slows the ball, so the real angle will be different. Plan to adjust it on the field. It's also only valid if 400 in/s is the ball's actual exit speed, not a speed worked out from flywheel RPM. Solving the math doesn't mean any team actually aims this way.

**Questions I would ask you:**
1. **What does one POLLEN weigh (grams, on a scale) and what is its diameter (calipers)?** With both numbers, I'd add a POLLEN constants file for BIOBUZZ and rerun the solver to get the drag angle. I'd only add it with your permission, since this run wasn't allowed to change repo files. Without them, 20.01° with on-field tuning is the honest answer.
2. **Is 400 in/s measured (for example from high-speed video) or estimated from flywheel RPM?** If it's estimated, the real exit speed is usually lower because the ball slips on the wheels. I'd ask for a measured speed or tell you to tune the angle, since any angle from an estimated speed is only a guess.
3. **Is 24 in measured from where the ball leaves the launcher to where it should enter the target?** If it's measured from the floor or the robot base instead, I'd rerun with the corrected height.
4. **Low arc (20°) or high arc (81°)?** I've assumed low arc for a hood shooter. If you want the lob, I'd give the 81.3° result instead, which has the same drag limitation.

Commands run from the repo root; no files were changed.