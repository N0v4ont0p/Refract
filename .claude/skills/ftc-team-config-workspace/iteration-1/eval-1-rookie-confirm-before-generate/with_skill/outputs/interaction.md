# What I would say to the user (verbatim) — and where I stopped

Hi team 99902, welcome to FTC! I can absolutely write you a driving TeleOp. Before I generate
any robot code, I need to confirm a few things about your robot — a wrong guess that compiles
is worse than a question that costs one turn, so bear with me for one quick round.

## Here's what I've got so far (please check me on it)

From your message I've penciled in:

- **Drivetrain:** mecanum, on the goBILDA Strafer chassis kit
- **Wheels:** stock goBILDA mecanum wheels, **96mm** diameter (that's what the Strafer kit
  ships with — if yours came with a different size, tell me)
- **Control system:** REV Control Hub, **no Expansion Hub** (just the one hub, like you said —
  that means all 4 drive motors plug into the Control Hub's 4 motor ports, which works fine)
- **Team:** 99902, rookie

None of that is locked in yet — it's a pre-fill waiting on your yes.

## Three questions I still need answered

These three actually change what code I write, which is why I'm asking instead of guessing:

**1. OpMode style — how do you want the code structured?**
An "OpMode" is the program that runs on your robot during a match. There are two common ways
to structure it:

- **Raw LinearOpMode** — one Java file, top-to-bottom: read the gamepad, set motor powers,
  repeat in a loop. Everything in one place; this is what the official FTC samples and most
  tutorials use.
- **FTCLib command-based** — a library that splits the robot into "subsystems" and "commands".
  More structure up front, pays off as the robot grows, but there's an extra library to install
  and more concepts to learn.

Both are fully legal and both work great — which would you like? (If you have no preference,
say so and I'll lay out the tradeoff in one more sentence and let you pick.)

**2. Path-following library — are you using one?**
Libraries like **Road Runner** or **Pedro Pathing** help robots drive precise paths in the
autonomous period. They don't matter much for a driver-controlled TeleOp, but I record it now
because it shapes everything I generate later. For a rookie team that hasn't set one up,
**"none"** is a completely normal answer.

**3. Mechanisms — is there anything on the robot besides the drivetrain?**
This season (DECODE 2025-26), robots commonly have some of: an **intake** (roller or claw),
a **shooter** (flywheel or elastic catapult), a **turret** (only if there's a shooter),
a **gate mechanism**, or a **classifier interaction** mechanism. If it's just the Strafer
chassis right now — "nothing yet, just the drivetrain" is a perfectly good answer, and I'll
generate drive-only code with no extra stubs cluttering it up.

## Confirm-back

Once you answer, I'll read the full picture back to you in one line — something like:
*"mecanum on stock goBILDA 96mm Strafer, REV Control Hub only, raw LinearOpMode, no pathing
library, no mechanisms yet — rookie team 99902"* — and after you say **yes**, I'll write the
TeleOp OpMode file for you.

---

*Session note: this run is non-interactive, so I stopped here — no OpMode was generated.
The config gate (`validate_config.py`) reports `generation_allowed: false` with
`drivetrain.type` unconfirmed and `software_stack.pathing`, `software_stack.opmode_style`,
and `season_mechanisms` missing. Code generation waits for the answers above and an explicit
"yes" on the confirm-back.*
