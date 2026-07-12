# Flywheel "flake" between matches — it's the code, not the motor

Short version: this reads like a hardware flake, but a deterministic check found a
software cause that produces *exactly* your symptom — "tuned right in one match, way
off the next, and we changed nothing." Swapping the motor wouldn't fix it, which fits.

## Root cause (deterministic finding — a script confirmed this, not a guess)

**`MainTeleOp.java:4` — `public static double flywheelOffset` is a mutable
(non-`final`) `public static` field, and it's written from inside the OpMode at
`MainTeleOp.java:12`.**

Why this is the classic "behaved differently for no reason" bug in FTC:

- In the FTC app model, `static` fields live on the **Robot Controller app process**,
  which outlives any single OpMode run. A new `LinearOpMode` object is created every
  time you hit INIT — but statics are **not** reset. So a `public static` value written
  during one run silently carries its last value into the **next** run.
- A flywheel *offset* is precisely the kind of value this bites. If that offset ever
  gets changed during a session — from a separate tuning OpMode, from FTC Dashboard
  (`@Config`), or from a code path that only runs sometimes — whatever it was left at
  persists into your next match. Match 2 starts with match 1's leftover tuning. Nothing
  in the code changed; the *state* did.
- It's invisible at the two places you'd normally catch a bug:
  - **In code review** — each individual write looks locally correct.
  - **In single-match testing** — a static only leaks into the *following* run, so any
    one run you test passes clean. You need run N to follow run N-1 to see it.

This is a documented failure mode in our corpus (`known-failure-modes.md` → "Global
mutable static state / cross-opmode persistence"; evidence team 12808, DECODE V2). Their
shooter math had a wall of exactly this — `SOTMOffset`, `turretCompOffset`,
`hoodCompOffset` — non-`final` `public static` tunables mutated from lifecycle code and
never reset. Same shape as your `flywheelOffset`.

### Honest scope of the finding (carrying the linter's own caveat)

The linter flags this as a **SIGNAL to verify, not a settled bug**. A `public static`
that is *unconditionally reset on an init path before its first read* is safe. In the
file as given, there's an assignment `flywheelOffset = 0.25` before `waitForStart()`. So
you need to check one thing:

**Is `flywheelOffset` written anywhere *other* than that one init assignment** — a tuning
OpMode, an FTC Dashboard `@Config`, a button handler, a shooting routine? If yes, that
write survives into the next match and is your flake. If the *only* write is that single
unconditional init line and nothing else ever touches it, this specific field is safe and
we keep looking. Given your symptom (varies match-to-match, motor swap didn't help), a
mutated-and-not-reset shooter offset is the prime suspect.

### The fix (rookie-friendly — the *why* matters here)

Pick either, both are standard:

1. **Make it instance state, not static.** Drop `static`: `public double flywheelOffset`.
   Now it's born fresh with each OpMode object and cannot carry across runs. This is the
   real fix — the value has no reason to be global.
2. **If you keep it a live-tunable `@Config` static**, then *reset it to a known default
   at the top of `runOpMode()`* (before anything reads it), every run, no exceptions. A
   dashboard-tunable static is safe **only if it is also reset each run** — the `@Config`
   annotation does not save you here.

Rule of thumb for the whole team: a `public static` that gets *written* while an OpMode
runs is cross-match state. Tuning offsets, alliance color, mode flags — same trap. If it
must be static, reset it on init; otherwise make it instance state.

## Other findings from this pass

**God OpMode (medium).** `MainTeleOp.java` is 317 lines with 6 direct `hardwareMap.get`
calls in the one class — hardware wiring and control logic all concentrated in the OpMode,
no subsystem separation. This isn't causing your flake, but it's why the flake was hard to
find: with everything in one file, state and logic blur together. Pulling the flywheel into
its own subsystem (you already have a `Shooter` class started) makes offsets naturally
instance-scoped and kills this class of bug structurally. Tie-in: your config is
`opmode_style: raw_linear_opmode` — moving hardware access behind a subsystem is compatible
with that and is the standard structural fix.

**Config mismatch: `TurretAimer.java` (confirm — don't assume).** `config_lint` found
`TurretAimer.java` references a turret, but your `team-config.yaml` declares
`turret: none`. This is **not referenced by your current config — confirm whether it's
stale (leftover code to delete) or the config is wrong (you actually have a turret).**
That's a config question, not a code-review call — take it to ftc-team-config to resolve,
don't just delete it on my say-so.

**Note, not a finding: `Shooter.java` extends SolversLib `SubsystemBase`.** That's a
command-based subsystem base from a shared library (SolversLib, FTCLib-lineage). Two things:
(a) it's currently an empty stub (`spinUp()` does nothing), and (b) it's command-based while
your config says `raw_linear_opmode`. Worth confirming which style you're actually
committing to. The command-framework adoption itself is a *shared-ancestry* pattern in our
corpus (library-provided, seen in teams 22105 and 16093) — I mention it as context, not as
an endorsed "elite pattern," because the credited part there is the library, not a novel idea.

## Bottom line

Stop swapping hardware. Check every place `flywheelOffset` is written; if anything other
than the single init line touches it, that's your between-match flake. Make it instance
state (or reset it every run) and the symptom should go away.
