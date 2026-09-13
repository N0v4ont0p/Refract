**No, that's not legal.** For BIOBUZZ, what counts is how far the arm can physically reach, not where your code stops it. An arm that can mechanically get to 32 in. fails inspection, even though you only ever drive it to 28 in.

**What the rules say** (2026-2027 Competition Manual, V1, the version released at kickoff on Sept 12):

- **R105.A:** After the match starts, the robot must stay inside an 18 in. x 24 in. footprint and be no taller than **29 in.** above the field floor at any time.
- **R105.B:** The robot has to be held within those limits by its physical build, **without using software**.
- **The note under R105:** At inspection you must show the robot's maximum mechanical extension. It says a robot that can mechanically go past the limit "would be in violation even if the ROBOT has software limiting the position of the extension during the MATCH" (Figure 12-3 shows this case).
- **G416:** Going past the R105 limits during a match is a verbal warning, or a MAJOR FOUL each time if the referee judges it deliberate. In practice you won't get that far, because the inspector won't pass the robot.

Your 28 in. match height is fine. Being able to reach 32 in. is what breaks the rule.

**How to fix it:** Add a physical hard stop so the arm can't go above 29 in. no matter what the motor or code does. That could be a stop block, a shorter slide or a limiting strap. Set it a little under 29 in. (around 28 to 28.5 in.) so bumps and slop can't push you over. Keep your software limit too, so the motor doesn't stall against the stop. Then show the inspector the arm at full extension.

**Also check:**
- The 29 in. is measured from the floor with all wheels down, and it includes anything the arm is holding. Measure the highest point of the whole robot, not just the top of the arm.
- The same rule applies to the 18 x 24 in. footprint. Any slide or intake that can physically reach past it needs a hard stop as well.
- This is V1 of the manual. Watch the Team Updates, since limits can change.

If anyone asks how to confirm this: measure the arm at full mechanical travel with the robot powered off, from the field tiles to the highest point, while holding the tallest game piece it carries. If it's over 29 in., add the stop. If it's 29 in. or less, you're legal and the software limit is optional.

Sources:
- [2026-2027 FIRST Tech Challenge Competition Manual V1 (BIOBUZZ)](https://ftc-resources.firstinspires.org/ftc/game/manual), R105, G416
- [BIOBUZZ Game & Season, FIRST](https://www.firstinspires.org/programs/ftc/game-and-season)