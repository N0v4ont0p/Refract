# SystemCore and your REV Control Hub: what's the deal?

Short version for your mentor: **plan your code around the REV Control Hub for this coming season (2026-27). SystemCore doesn't become a competition-legal FTC controller until the 2027-28 season**, and even then there's a long transition window. Nothing about SystemCore should change what you write this year.

## The timeline (per FIRST's official control system announcements)

- **2026-27 (this coming season):** FTC stays on the current control system — REV Control Hub (+ optional Expansion Hub) with the FTC SDK. SystemCore is not legal for FTC competition this season. (FRC gets it first, starting with their 2027 season.)
- **2027-28:** SystemCore becomes *available* for FTC teams to compete with. It replaces the Control Hub as the main processor/IO, paired with **MotionCore** for power and CAN distribution, and the new **FIRST A301** is slated to be the only legal actuator *within the new controller ecosystem*.
- **Through at least 2030-31:** FIRST has committed to a transition period where the **legacy setup (Control Hub + Expansion Hub + existing motors/servos) remains legal**, along with at least one **hybrid configuration** (SystemCore + REV Expansion Hubs + your current motors and battery). So your existing hardware isn't a dead end — you'll have years of runway.

## What this means practically

1. **Don't restructure anything this season for SystemCore.** It can't be on your competition robot this year, and hardware/SDK details are still being finalized through FIRST's alpha/beta testing program.
2. **Your Control Hub investment is safe for a while.** Legacy and hybrid configs are legal through at least 2030-31, so there's no forced hardware buy in 2027 either.
3. **The one cheap thing worth doing now:** write your code with clean separation between hardware access and robot logic — e.g., subsystem classes (Drivetrain, Intake, Arm) that wrap `hardwareMap` lookups, with OpModes calling subsystem methods rather than touching motors directly. That's just good FTC practice anyway (it makes hardware swaps and tuning easier today), and it means whatever the SystemCore-era SDK looks like, your porting work is confined to a thin hardware layer instead of scattered through every OpMode.
4. **Keep an eye on it next spring/summer.** FIRST publishes control system updates on the FIRST community blog and ftc-docs; the concrete "what changes for FTC software" details will firm up as the 2027-28 season approaches, and there may be public beta opportunities if your team wants early exposure.

Bottom line for the mentor: **this season = Control Hub, full stop. Next season (2027-28) is when SystemCore becomes an option, not a requirement, and the old hardware stays legal until at least 2030-31.** The best prep isn't planning around SystemCore — it's writing well-abstracted code on the platform you have.

Sources:
- [Control System Update — FIRST Tech Challenge Edition (FIRST community blog)](https://community.firstinspires.org/control-system-update-first-tech-challenge-edition)
- [Introducing the FIRST A301 (FIRST community blog)](https://community.firstinspires.org/introducing-the-first-a301)
- [Chief Delphi discussion of the FTC control system update](https://www.chiefdelphi.com/t/frc-blog-control-system-update-first-tech-challenge-edition/508944)
