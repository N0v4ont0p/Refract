**Yes, there's a problem. The 8 motors are fine, but 10 servos is 2 too many for BIOBUZZ.**

I checked the V1 2026-27 BIOBUZZ Competition Manual, which was released at kickoff.

**1. Servo count: this fails inspection as the robot is now**
- R503 says: "ROBOTS are limited to a total of 8 motors and 8 servos." Last season (DECODE) allowed 10 servos, and FIRST's BIOBUZZ preview says outright that the servo limit was cut to 8.
- The limit covers every mechanism across all configurations you use at an event. If you swap mechanisms between matches, add up the servos from every setup.
- Continuous rotation servos and linear servos count toward the 8.
- You can't turn the 2 extra servos into motors, because you're already at 8 motors. Your options are:
  - Combine functions, for example one servo driving two linked parts through a linkage.
  - Drive something passively with springs, surgical tubing or gravity.
  - Drop the least important mechanism.

**2. Motors: 8 is exactly the limit**
- That's legal, but only if every motor is on the R501 list. The list includes goBILDA 5202/5203/5204 Yellow Jackets, goBILDA 5000, REV HD Hex, REV Core Hex, NeveRest, Studica Maverick, SWYFT Spike, TorqueNADO and a few others.
- You have no room to add a motor this season.

**3. Other things to check on a reused robot**
- **Expansion limit is back (R105).** The robot still has to start inside an 18 x 18 x 18 in. cube (R102). After the match starts, it must stay inside an 18 x 24 x 29 in. (tall) box at full extension. That limit has to be enforced physically, not by software. FIRST's preview notes that "Expansion limits are back," so a DECODE robot that reaches further may need hard stops or shorter slides.
- **Servo specs (R502).** Each servo must be at most 8 W of output power and at most 4 A stall current at 6V. Linear servos must be at most 1 A. Stall current is measured without any software limits.
- **Power wiring (R505).** At most 2 motors per motor port and 2 servos per servo port, and only through the approved devices (REV hubs, REV Servo Hub or Servo Power Module, goBILDA Servo Power Injector, Studica Servo Power Block, SPARKmini). REV hubs give servos only 5V. The power modules give 6V.
- **Your team must have built the robot (R101).** Reusing your own robot is fine.

**Questions I'd ask you, and what I'd do with each answer**
1. **What does each of the 10 servos do, and which 2 matter least for BIOBUZZ?** I'd suggest which 2 to cut or combine, and a passive or linkage replacement where one makes sense.
2. **Do you plan to swap mechanisms between matches at an event?** If yes, I'd add up servos and motors across every configuration, since R503 counts the total.
3. **Which motor and servo models are on the robot?** I'd check each against the R501 list and the R502 limits, and flag any high-power servo that needs paperwork at inspection.
4. **How far does the robot reach when fully extended (width, length, height)?** If it goes past 18 x 24 x 29 in., I'd work out where hard stops are needed.
5. **What powers the servos: hub ports directly, or a Servo Hub or power module?** I'd check the per-port limits and whether any servos misbehave at 5V.

Sources:
- [BIOBUZZ Competition Manual Preview Release](https://community.firstinspires.org/biobuzz-cm-preview-release)
- [V1 2026-2027 FIRST Tech Challenge Competition Manual](https://ftc-resources.firstinspires.org/ftc/game/manual) (R101, R102, R105, R501-R505)