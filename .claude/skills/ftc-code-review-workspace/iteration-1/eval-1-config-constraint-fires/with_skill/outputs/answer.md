# Pre-competition code review — Team 12345

Sanity check done. I reviewed this *against your confirmed config* (mecanum, raw LinearOpMode, no
pathing, stock goBILDA/REV, rookie), not a generic robot. Two tiers below: the first is
**deterministic** — a script found it, so it's a finding, not an opinion. The second is **judgment** —
I show you the code and the concern; you decide.

Codebase is small (3 files: `MainTeleOp.java`, `Shooter.java`, `TurretAimer.java`), so I read every
line rather than spin up the heavyweight full-review pass — no cost saving worth it at this size.

---

## Deterministic findings (a script confirmed these)

### 1. Turret code exists but your config says you have no turret  — CONFIRM BEFORE THE EVENT
`config_lint.py` flagged `TeamCode/TurretAimer.java`. Your `team-config.yaml` declares
`turret: {value: none, confirmed: true}`, but there's a `TurretAimer` class referencing turret aiming.

This is the R34/R40 case. I'm **not** telling you which it is — that's yours to confirm:
- **Stale/dead code** (most likely): you don't have a turret, this is leftover, and it's just dead
  weight in the module. Delete it so nobody wires an inspection question or a build around it.
- **Config mismatch**: you *do* have a turret and the config is wrong — in which case stop, and go fix
  the config first (that's a `ftc-team-config` job, not something I patch here).

Either way, resolve it before competition so your code and your declared robot agree.

### 2. God OpMode — `MainTeleOp.java` (317 lines, 6 hardware devices grabbed in one class)  — medium
`failure_mode_lint.py` flagged this: all your hardware wiring (`fl/fr/bl/br/intake/shoot`) and your
control/telemetry logic live in one `runOpMode`. No subsystem separation.

Why this matters for *you* (rookie team, so here's the full why, not just the label): a single 300-line
OpMode is the class that everyone edits at once and nobody fully understands at 11pm before a match.
When the flywheel and the drivetrain and telemetry all share one method, a change to one silently
touches the others, and a bug in one stops the whole robot. The fix isn't cosmetic — pull each mechanism
(drivetrain, intake, shooter) into its own small class the OpMode calls. This is exactly the structural
separation the elite-team corpus is built around, and your config (`raw_linear_opmode`) fully supports
it — plain classes with `init(hardwareMap)` + `update()` methods, no framework required.

Tie-back: this is `known-failure-modes.md`'s God-OpMode failure mode; the fix ties to your confirmed
`raw_linear_opmode` style (no new dependency needed).

### 3. Mutable cross-OpMode state — `flywheelOffset`  — low, but VERIFY
`public static double flywheelOffset` is non-final and gets **written** inside `runOpMode`
(`flywheelOffset = 0.25`). The linter flags this as a **signal, not a settled bug**, and the distinction
matters:

A `static` lives on the app process, not on your OpMode run. State written during one match **silently
survives into the next OpMode run**. This is invisible in code review and invisible in single-match
testing — it only leaks into the *following* run — which is exactly why it surfaces at competition as
"the robot behaved differently for no reason" and gets misread as a battery or hardware flake.

What to do: confirm `flywheelOffset` is **unconditionally reset every run** before it's first read
(e.g. set it in your init path, not left to carry over). If it's reset each run, you're fine. If it's a
live-tunable value you *want* to persist, that's a decision — just make it a deliberate one, not an
accident. Right now it's assigned once to `0.25` in the lifecycle method, so verify that's intended.

---

## Judgment tier (a smell — here's the evidence, you judge)

### `Shooter.java` is command-based, but the rest of your robot isn't
`Shooter.java` extends `com.seattlesolvers.solverslib.command.SubsystemBase` — that's the SolversLib
command framework (the FTCLib-successor). But:
- Your config says `opmode_style: raw_linear_opmode`.
- `MainTeleOp` is a raw `LinearOpMode` that grabs `shoot` straight from `hardwareMap` and **never uses
  the `Shooter` class at all**.

So `Shooter` is an orphan: a command-based subsystem sitting in a robot that's otherwise written as a
raw linear OpMode that doesn't call it. Two readings, and again you confirm which:
- The config is right (you're raw-linear) → `Shooter.java` is a half-started/abandoned direction; either
  wire it in properly or remove it so it's not dead weight.
- You actually adopted SolversLib command-based → your config is stale and should be updated (hand back
  to `ftc-team-config`).

Provenance note, stated exactly as the corpus stores it, not inflated: a team in the corpus (15083)
also extends `com.seattlesolvers.solverslib.command.SubsystemBase`. That corpus entry (15083-B) is
tagged **`confidence: single-source`**, **provenance: `shared-ancestry`**, and is explicitly recorded as
a **provenance guard, not a transferable pattern** (`applicable_when: n/a`). So this is **not** evidence
that command-based is "what good teams do" — it's one team, on a shared library, flagged precisely so it
*doesn't* get counted as independent endorsement. For a rookie team the honest call is: match your code
to one style and make the config say so; don't adopt a command framework because a corpus name-drops it.

---

## What I did NOT find (so you can stop worrying about it)
- **Telemetry**: present (`telemetry.update()` is called) — the missing-telemetry check passed.
- **Stale PID / SDK tampering**: no PID files and nothing touching `libs/` — clean. (Never modify
  anything under `libs/` — it makes the Robot Controller inspection-illegal.)
- Bus-factor / VCS-discipline stats came back empty (0 commits) because this folder has no git history
  of its own — that's a stat, not a finding, and not something to act on here.

---

## Priority before the weekend
1. **Resolve the turret code** (finding 1) — dead code or config mismatch, decide and act.
2. **Verify `flywheelOffset` resets every run** (finding 3) — this is the classic "flaky at comp" trap.
3. Decide `Shooter.java`'s fate (wire in or delete) so code and config agree.
4. Splitting `MainTeleOp` into subsystems (finding 2) is the right structural fix but the biggest job —
   do it if you have time; don't destabilize a working robot the night before if you don't.

Nothing here is a legality question — if you want a rules/inspection pass, that's `ftc-rule-check`.
