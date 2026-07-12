**Verdict: illegal as-is — a 19-inch-wide robot will not pass inspection or be allowed to start the match.**

Here's the rule it runs into, straight from the manual:

**R101 — STARTING CONFIGURATION is limited to an 18-inch Cube.** In the STARTING CONFIGURATION (the physical setup your robot is in when a match begins), the robot "must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. (45.70 cm) long, by 18 in. (45.70 cm) high volume." The only thing allowed to poke outside that box is a pre-loaded scoring element (an ARTIFACT you started the match holding). The robot structure itself gets zero tolerance over 18 inches.

19 inches is over the 18-inch limit in a dimension the inspectors physically check with a sizing tool, so this is not a gray area — it fails.

Two things worth knowing so you can fix it:

1. **"About 19 inches" isn't precise enough — but it doesn't save you here.** 18 in. (45.70 cm) is a hard ceiling, not a target with slop. Even if your real number is 18.5 or 18.9, you're still over. Measure it exactly with a tape or, better, build/borrow an 18-inch sizing box and see if the robot drops in fully self-contained. If it's genuinely at or under 18.00 in. on every side, you're fine; anything above, you have to trim.
2. **At inspection the robot has to hold this size by itself.** Per **R102**, in starting configuration the robot must be fully self-supported — it can't lean on the sides or top of the sizing tool to squeeze in. You can hold the shape mechanically while powered off, or by running an init OpMode that pre-positions the servos/motors. So "it fits if I push it in" doesn't count; it has to sit inside the 18-inch box on its own.

How this actually bites you on match day: even if you somehow got past inspection, **G304** requires the robot to be "confined to its STARTING CONFIGURATION (see R101 and R102)" when set up on the field. An oversized robot means the match won't start until it's fixed (or the robot gets DISABLED), so there's no sneaking it through.

What to do: shave off the extra inch-plus somewhere on the wide axis — a common culprit is bumpers/side plates, intake arms, or wheels sticking out past the frame. Get it fully inside 18.00 in. and re-measure in a sizing box before you go to inspection.

One thing that's *not* your problem yet: once the match starts you're allowed to expand — **R105** lets the robot go up to 18 in. tall freely, up to 38 in. tall under the extra conditions in G415, and slide out horizontally as long as the total horizontal footprint at maximum mechanical extension stays within 18 in. So the 18-inch limit is only about the *starting* box; the width issue is purely a start-of-match / inspection problem, and it's a real one.

(Citations verified against the tagged manual: R101, R102, R105, G304, G414, I304. R101's 18-inch limit is in the base manual and has not been changed by a Team Update in the local rules snapshot — but if you want to be airtight, confirm no newer Team Update touched it, since I'm reading a local copy, not a live feed.)
