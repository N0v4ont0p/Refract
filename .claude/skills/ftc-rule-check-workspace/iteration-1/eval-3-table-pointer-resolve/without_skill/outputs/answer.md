Short answer: I would not run 30 AWG on your drive motor power leads. It's almost certainly outside spec, and it's a real safety/reliability problem regardless of the exact rule number.

**Heads up on sourcing:** I'm answering from general knowledge here, not from a live lookup of the current FTC Competition Manual. The wire-gauge rule lives in the Robot (electrical wiring) section of the manual, and the exact minimum gauge and wording can change year to year and via Team Updates. Please verify against your season's manual before you commit — treat the numbers below as a sanity check, not a citation.

**Why 30 AWG is the wrong call:**

1. **Current-carrying capacity.** 30 AWG is tiny — it's signal/breadboard wire. It can only safely handle on the order of half an amp to a couple of amps. FTC drive motors (e.g. the goBILDA 5203 / REV yellowjacket / NeveRest class) can pull well into the double digits of amps at stall — think ~9–11 A stall per motor, and spikes when you slam direction or push against a wall. 30 AWG will heat up, drop voltage, and can melt insulation or fail open. That's a fire/brownout risk, not just a performance one.

2. **The manual expects appropriately-sized wiring.** FTC's electrical rules require wiring to be sized for the load, and motor/battery power wiring has a minimum gauge that is much thicker than 30 AWG. The motors themselves ship with leads in roughly the 18–22 AWG range for exactly this reason. Downsizing the power path below what the motor came with is going the wrong direction.

3. **Inspection risk.** Undersized or sketchy power wiring is the kind of thing a robot inspector can flag. Even if you found a loophole in the letter of the rule, a leg-eaten 30 AWG motor lead is an easy "come back and fix that" at inspection.

**On the weight goal:** the power wiring on an FTC robot is a rounding error on total weight — you're talking grams. You will not meaningfully lighten the robot by thinning motor leads, and the downside (voltage drop = less torque/speed at the wheels, plus melt/brownout risk) costs you far more than the grams save. If weight is the real problem, look at structure, wheels, and mechanism material instead.

**What to do instead:** keep the motor's factory leads, or if you're extending/re-terminating, match or exceed the motor's existing gauge (commonly ~18 AWG for these power runs). Then confirm the current manual's exact minimum-gauge rule for motor and battery wiring for your season before finals — I don't want you relying on my memory for the inspection-critical number.
