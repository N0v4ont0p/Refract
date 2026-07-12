# Is `MainTeleOp.java` well organized?

Short version: no, not really — and the good news is the fix is one you've already half-started elsewhere in the repo. Let me show you *why*, with the actual lines, rather than just asserting it.

I reviewed this against your confirmed config (mecanum drive, roller intake, flywheel shooter, raw LinearOpMode style, rookie team). Two things came back from the deterministic linters — these aren't opinions, a script confirmed each one, so I'm reporting them as findings.

---

## Finding 1 — God OpMode (deterministic, medium)

**What the script found:** `MainTeleOp.java` is 317 lines with 6 direct `hardwareMap.get(...)` calls all inside `runOpMode()`.

**The evidence (lines 6-11):**
```java
var fl = hardwareMap.get(Object.class, "fl");
var fr = hardwareMap.get(Object.class, "fr");
var bl = hardwareMap.get(Object.class, "bl");
var br = hardwareMap.get(Object.class, "br");
var intake = hardwareMap.get(Object.class, "intake");
var shoot = hardwareMap.get(Object.class, "shoot");
```

**Why this is a real structural problem (not just a style nit):**

"God OpMode" means one class is doing everyone's job at once — it wires up every piece of hardware *and* holds all the control logic *and* prints all the telemetry, with no separation between those responsibilities. `hardwareMap.get` is the call that grabs a physical device (a motor, a servo) by the name you gave it in the Driver Station config. When all six of those live directly in your teleop:

- **Nothing is reusable.** When you write your autonomous OpMode, you'll grab `"fl"`, `"fr"`, `"bl"`, `"br"` all over again by hand. If you ever rename a motor in the config, you now have to remember to change it in *two* places, and the day you forget is the day auto and teleop disagree about which motor is which.
- **It only grows.** 317 lines today, and every new feature (a second shooter speed, an intake reverse) gets stacked into the same `runOpMode()`. There's no natural home for new logic, so it all piles into one method.
- **It's hard to test or reason about in pieces**, because the drivetrain, intake, and shooter aren't separable things — they're just variables sharing one giant method.

**The fix — and you're already doing it for one subsystem:** Pull each mechanism into its own subsystem class that owns its own hardware, and have `MainTeleOp` *talk to* those classes instead of grabbing hardware itself. Here's the thing — `Shooter.java` already exists in your repo:

```java
public class Shooter extends SubsystemBase {   // Shooter.java
    public void spinUp() { }
}
```

But `MainTeleOp` ignores it and does `hardwareMap.get(Object.class, "shoot")` on line 11 instead. So the target structure isn't hypothetical for you — extend what `Shooter.java` started to a `Drivetrain` (your four mecanum motors) and an `Intake` (your roller), and let `MainTeleOp` just call `shooter.spinUp()`, `drivetrain.drive(...)`, etc.

**Provenance, stated honestly:** the "subsystem owns its hardware, the OpMode just calls it" structure shows up in the corpus as team **22105's** `RobotHardware` layer (their subsystems depend on typed wrappers rather than raw `hardwareMap.get`). I want to be straight with you about how strong that evidence is: it's tagged **single-source** — one team's repo, not an independently-confirmed-across-many-teams law. So treat it as a well-reasoned convention, not gospel. That said, this particular finding doesn't rest only on the corpus — the linter caught the God-OpMode shape deterministically, and you already have a half-built `Shooter` subsystem proving the direction.

---

## Finding 2 — Mutable static written during the run (deterministic, low — a SIGNAL to check)

**What the script found:** a non-final `public static` field that gets assigned inside a lifecycle method.

**The evidence (lines 4 and 12):**
```java
public static double flywheelOffset = 0.0;   // line 4
...
flywheelOffset = 0.25;                        // line 12, inside runOpMode()
```

**Why this class of thing matters (the "behaved differently for no reason" trap):** a `static` field doesn't belong to one run of your OpMode — it lives on the app process and *outlives* the OpMode. So a value written during one match can silently survive into the *next* match. That's nasty because it's invisible in a normal code read and invisible in single-match testing (the leak only shows up on the *following* run), and when it bites, it looks exactly like a random hardware flake: "the flywheel was off today for no reason."

**But I'm not going to call this a bug, because the code doesn't show one.** The linter itself flags this as a *signal, not a settled defect*, and here the mitigating detail is visible: `flywheelOffset` is reassigned to `0.25` unconditionally at the very top of every run (line 12), before anything reads it — so within this file it's effectively reset each time. The reason it's still worth a flag: it's `public`, so *another* OpMode could read or write it, and that's the path where a stale value could actually leak. **Action:** confirm nothing outside this file depends on `flywheelOffset` carrying over, and if it doesn't need to be shared, make it a plain instance field (`double flywheelOffset`) instead of `public static`. If it's meant to be a live-tunable knob, keep it but make sure it's reset per run (which it currently is).

---

## One thing outside this file, since I ran the config check

Not part of `MainTeleOp`, but the config linter flagged it and you should know: your config says `turret: none`, but there's a `TurretAimer.java` in the repo. That's either dead/stale code or a config mismatch — I can't tell which from here. Worth confirming so it doesn't confuse your inspection or your next build. (This is a config question, so if it turns out the config is wrong rather than the code, that's a job for reconfirming your team config, not this review.)

---

## So, is it well organized?

As it stands, no — it's a single 317-line OpMode doing hardware wiring, control, and telemetry all in one method, and it bypasses a `Shooter` subsystem you already wrote. That's the God-OpMode shape, confirmed by the linter, not just my read. The path forward is concrete and already begun: give the drivetrain and intake the same subsystem treatment `Shooter` started to get, and have `MainTeleOp` call into them. Do that and this file shrinks to something you can actually read at a competition at 8am. Nothing here is competition-illegal or urgent-broken — it's a maintainability problem that gets more expensive every week you build on top of it, which is exactly why it's cheaper to split now while it's three subsystems and not ten.
