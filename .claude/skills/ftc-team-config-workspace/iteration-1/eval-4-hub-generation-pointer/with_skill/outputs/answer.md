Short version: **no — don't plan your code around SystemCore this season or next.** It isn't legal for FTC competition until the 2027-28 season, and even when it arrives there's no forced cutover. Stay on the REV Control Hub.

Here's the picture, with confidence labeled (tier-1 = official FIRST/WPILib/vendor sources; tier-2 = alpha-tester reports and community threads):

**What's settled (tier-1):**
- SystemCore becomes legal for FTC competition **starting the 2027-28 season**. For the current season and next (through 2026-27), the REV Control Hub is the *only* legal control system — there is literally no decision to make yet.
- After that, there's a **transition period through at least 2030-31** during which the legacy REV system and a **hybrid approach are both legal**. This is not a binary "old vs. new" switch — the alpha program explicitly includes a hybrid configuration pairing SystemCore with existing batteries, motors, and REV Expansion Hubs.
- What it actually is: SystemCore is a Limelight-built controller on a Raspberry Pi CM5; MotionCore is a separate power/CAN/actuator unit; and the FIRST A301 will be **the only legal actuator on the new system** (replacing third-party motors and servos there). The battery system is explicitly still in development.

**Why "planning code around it" now isn't really possible (the honest part):**
- The **FTC SDK and programming-language story is unconfirmed** — FIRST hasn't stated it, and as recently as May 2026 it was still an open community question. (Reported OS-level runtimes like Java 25 / Python 3.13 are tier-2, single-source, and are the OS layer, not the FTC SDK.)
- Whether FTC **keeps the OpMode model** or moves to something like FRC's continuous TimedRobot lifecycle is unconfirmed. Tier-2 alpha reports hint at a shift, but nothing is settled.
- **Library compatibility (e.g. FTCLib) across the two generations is unconfirmed**; tier-2 reports say the alpha software runs only on SystemCore.

So there is no stable API to target. Any "SystemCore-ready" scaffolding you wrote today would be a guess at interfaces that don't exist yet and will very likely change before 2027-28.

**What actually transfers:** clean code structure. Keeping drivetrain and mechanism logic behind subsystem interfaces, hardware mapping in one place, and control logic separated from hardware access is good practice on the Control Hub today — and it's the part of your codebase that survives any platform change. That's where to invest, not speculative SystemCore abstractions.

**For your team config:** through the 2026-27 season I'll just record `hub_generation: rev_control_hub` as inferred — it's the only legal value, so it's not even a question. When the 2027-28 hybrid window opens, hub generation becomes a real decision with real tradeoffs (full SystemCore, staying legacy, or hybrid), and we'll revisit it with a fresh briefing then. Tell your mentor: nothing to decide now, no deadline pressure — both systems stay legal for years, and the details worth deciding on are still unconfirmed.

Now, back to setup — want to continue with the rest of your robot config?
