# known-failure-modes.md — FTC team failure-mode taxonomy (canonical)

Repo-root, shared, cross-cutting reference — same status as `core-feature-model.yaml`.
Not owned by one skill. Consumed by `ftc-code-review` (§17 rule-based checks),
`ftc-construct` (§23 — the quickstart template it scaffolds from actively counters these modes;
this absorbed what §16 originally scoped as a standalone `ftc-quickstart-builder` skill), and
Phase 4 repo mining (used as an active lens while extracting patterns, not a
separate checklist afterward).

Source material is stored **verbatim** as handed off — do not reconstruct or
paraphrase. Source tiers per Rule 7 are recorded at the bottom.

---

## Methodology

Synthesized from (1) an ASEE PEER academic survey on FTC team challenges,
(2) FIRST's own troubleshooting docs plus `wpilibsuite/SystemcoreTesting`
alpha-tester bug reports on GitHub, (3) community-reported failure patterns
(Chief Delphi, FTC Open Alliance), (4) established software-engineering theory
(bus factor, Conway's Law, technical debt) applied to volunteer/student teams.
Organized via an adapted Ishikawa/6M model — People, Process, Hardware,
Software, Measurement/Testing, Environment.

---

## Root-cause table (Category — Pain Point — Underlying Mechanism)

| Category | Pain Point | Underlying Mechanism |
|---|---|---|
| People | Knowledge loss on graduation | no mentorship pipeline, tacit knowledge leaves with the student |
| People | Single lead-coder bottleneck | bus factor of 1 |
| People | Programming/mechanical silos | Conway's Law in miniature |
| Process | No version control/code review | work overwritten, no rollback |
| Process | No engineering-notebook discipline | design decisions untraceable |
| Process | Deadline-driven scope creep | late mechanical changes force programming to chase a moving target |
| Hardware | Encoder drift & slop | backlash + loose mounts degrade odometry invisibly |
| Hardware | Wiring/connector failures | poor strain relief, un-crimped joints — the single most common in-match failure |
| Hardware | Voltage brownouts | under-provisioned power vs. stall current → hub reboots mid-match |
| Software | PID instability | constants tuned for one robot state don't survive mechanical changes |
| Software | Firmware/SDK version mismatches | hub firmware/SDK/library versions drift out of sync |
| Measurement | No pre-match checklists or telemetry | intermittent faults undiagnosable, symptoms get fixed, not causes |
| Environment | Competition RF/network interference | field Wi-Fi congestion, outside the team's control |

---

## Compounding chain

no documentation/version control → knowledge loss at graduation (bus factor 1)
→ new coder inherits code they don't understand → programming↔mechanical
communication gap widens → hardware changes late without programming's knowledge
→ PID/encoder assumptions invalidated silently → no telemetry to catch drift
before competition → failure surfaces mid-match.

**Core insight:** most reported "hardware failures" and "software bugs" are
actually process failures that surfaced late, for lack of an earlier structural
checkpoint.

---

## Severity × frequency

| Item | Severity | Frequency | Detectability |
|---|---|---|---|
| Wiring/connector failure | very high | high | low detectability (intermittent) |
| Knowledge loss on graduation | high-annual | high-compounding | N/A-structural |
| No code review/version control | high | medium-high | low |
| PID instability post-mechanical-change | medium-high | medium | medium (if tested) |
| Voltage brownout | medium | high | medium |
| I2C bus conflicts | medium | high | low |
| Programming/mechanical silo | high | high (root cause of many others) | N/A-structural |

**Highest-leverage fixes:** knowledge loss and programming/mechanical silos —
both structural root causes, not symptoms.

---

## SystemCore transition failure surface

(from `wpilibsuite/SystemcoreTesting` alpha reports + community forums)

- API churn during alpha (e.g. `OpModeRobot` non-functional, forcing a
  `TimedRobot` workaround);
- hardware lock-in (only the A301 legal on SystemCore/MotionCore — legacy
  motors/servos/sensors not reusable, a full rebuild not incremental);
- no finalized Driver Hub yet, testing on non-representative PC setups;
- documentation fragmented across forums/GitHub/blog posts, testers explicitly
  noting missing FTC-specific guidance; and
- the same silo root-cause recurring at the platform level — OpMode's init/loop
  shifting to WPILib's enabled/disabled model changes when mechanisms can safely
  deploy, and a team that doesn't redesign around that sees failures that look
  like bugs but are actually a design/model mismatch.

---

## Corpus-derived risk classes (Session 1, Phase 4 mining — NOT part of the verbatim handoff)

Added from evidence found while mining real team repos. Kept structurally separate so the
handed-off material above stays verbatim. Each is framed as a **new instance of this
taxonomy's own Core insight** (a process / runtime-semantics failure that surfaces looking
like a hardware or environmental bug), not a generic sibling category bolted on.

### Global mutable static state / cross-opmode persistence

**Category:** Process / runtime-semantics. **Evidence case:** team 12808 (RevAmped), DECODE V2
(public repo). **Detectability:** deterministic — `failure_mode_lint.py` check
`mutable_static_opmode_write`.

**Mechanism.** In the FTC app model, `static` fields live on the app process, which outlives any
single `LinearOpMode` run — a new OpMode instance is created each run, but statics are NOT reset.
So a mutable (non-`final`) `public static` field that is *written during a run* (from an OpMode /
command lifecycle method) silently carries its last value into the *next* run. Tuning offsets,
alliance state, mode flags, etc. leak across matches.

**Why this is a pure instance of the Core insight, not a new category.** It is invisible at BOTH
of the two checkpoints that catch most defects:
- **Invisible in code review** — each write is locally correct; nothing at the write site looks
  wrong, and the field's declaration looks like ordinary config.
- **Invisible in single-match testing** — a static only carries stale state into the *following*
  run, so any single run (the normal way a fix is "verified") passes clean. The failure needs
  run N to *follow* run N-1 with the wrong prior state.
It therefore surfaces as "the robot behaved differently in match 2 than match 1 for no reason" —
which reads as a hardware flake, brownout, or field/RF issue (Hardware/Environment), when the
actual cause is runtime state semantics (Process). Exactly the taxonomy's Core insight
(most "hardware failures"/"software bugs" are process failures surfacing late), extended: here
late-surfacing is *structural* — the two normal detection points miss it by construction.

**Evidence (specific fields, 12808 — cited, not summarized).** `SimpleShooterMath` declares a wall
of non-`final` `public static` tunables — `SOTMOffset`, `turretCompOffset`, `hoodCompOffset`,
`turretFarOffset`, `K_flywheelPrediction`, `CALIBRATION_ANGLE`, `blueX`/`redX` — and mutates them
from lifecycle code (`SimpleShooterMath.update()` writes `SOTMOffset`; `Robot.java` writes
`SimpleShooterMath.turretCompOffset` across cycle states). `TrackingThread` adds static mode flags
(`trackHood`/`trackTurret`/`far`). None are reset on an init path. (The `@Config` dashboard
annotation does not save this: a live-tunable static is safe only if it is ALSO reset each run.)

**Secondary sub-smell (one line, not its own class).** 12808's `TrackingThread`/`GyroThread` are
*synchronous* classes whose thread-implying names suggest concurrency that does not exist (verified:
no real threads in fielded code) — a comprehension hazard only, not a data race.

> Provenance footnote for Tier-2 close-out: this risk class exists because D's *original* framing —
> "12808 has a real multi-threaded / data-race architecture" — did NOT survive source verification.
> That makes **three** Session-1 catches where a plausible-sounding label was corrected against
> actual source: the Iron Reign/KookyBotz idiom attribution, 24089's "physics kept/abandoned"
> counterexample, and this. The taxonomy gained a *real* entry precisely by refusing to ship the
> wrong one — the system working as designed, not a miss.

### Case study: file-versioning as a substitute for version control (team 32477)

**Category:** Process / "No version control/code review" — the root-cause table's entry, here as a
CLEAN, fully-formed real-repo instance. **Evidence case:** team 32477 (public repo
`FTC-32477-Decode-Program-History`), a Tier-3 learning team.

**Why this case is worth keeping.** In this corpus's Tier-1/2 (deliberately STRONG teams), the
"no version control discipline" mode only ever appeared as a *partial* signal — a bus-factor blip,
an occasional trivial commit message. It never appeared cleanly because strong teams mostly use git
properly. 32477 is the first repo where the failure mode is the WHOLE structure — so it turns the
abstract root-cause-table row into something a future reader can see concretely, rather than just
re-reading the description.

**The anti-pattern, concretely.** Versioning is done by COPYING THE WHOLE PROGRAM INTO A NEW FOLDER
and suffixing filenames — not by git history. The repo holds parallel top-level folders
`TeleOp_All_v0.1/ v1.0/ v2.0/ v2.1/ v2.2/ v2.3/ v3.0/ v3.0_CNBEQ2/` and `Autonomous_All_v0.1/
v3.0_CNBEQ2/`, and the SAME subsystem is copy-renamed across them: `ChassisDriveSystem_1_0.java`,
`_2_0`, `_2_1`, `_2_2`, `_2_3`; likewise `SubsystemManager_1_0…_2_3`. Git IS present but used only as
a dumping ground: **5 total commits**, each just *adding* a whole new version folder ("Add version
2.3 of TeleOp", "Add v3.0 of TeleOp and Autonomous"). The version history lives in FOLDER NAMES, not
in git.

**What git would have shown instead (the concrete cost).** `ChassisDriveSystem` went 228 lines (v1.0)
→ 140 lines (v2.0) — a ~88-line net deletion, ~300 changed lines: a MAJOR simplification of the drive
subsystem. Under version control that is ONE commit whose diff shows exactly what was cut and (via the
message) why, with `blame` to trace each surviving line and `revert` to undo it. As folder-copies it
is instead two DISCONNECTED files in `v1.0/` and `v2.0/` with NO recorded relationship: no diff, no
merge, no blame, no bisect — and a reader must already KNOW to hand-diff `_1_0` against `_2_0` to see
that anything changed at all. Every rollback is "copy an old folder back"; every "what changed between
v2.2 and v2.3?" is a manual folder compare.

**Compounding (the taxonomy's own chain, made concrete).** Running the deterministic linter on 32477
also fired `god_opmode` on **19** OpModes — `TeleOp_All_*.java` and `Autonomous_All_*.java` monoliths
of 386–788 lines with 8–9 inline `hardwareMap` accesses each (no subsystem separation) — plus
`vcs_discipline` (5 commits) and a low `mutable_static_opmode_write` (`ErrorRange`, `TARGET_RPM`). So
32477 is the compounding-chain in one repo: no-VCS + god-class together, each folder-copy duplicating
the same ~700-line monolith, so a fix to one must be hand-propagated across every version folder.

> Phase-9 methodology note (honest): 32477 is the FIRST place the FIVE deterministic checks did real
> work rather than staying quiet. On the strong Tier-1/2 teams they almost never fired. Here
> `vcs_discipline` merely CORROBORATED a decision already made qualitatively (the folder structure was
> visible without a linter) — but `god_opmode` ADDED a dimension the qualitative pass had NOT seen (the
> 700-line monolithic OpModes), genuinely shaping this case study from "a VCS story" into "a VCS + god-
> class compounding story." That is the first evidence in this corpus of a deterministic check *shaping*
> an extraction/framing decision, not just firing in a post-hoc scan — and it only happened once the
> checks met a team that actually has the problems they target.

---

### Mechanism state chained to a sensor-fusion result (the aim-lock cascade)

**Shape.** One or more mechanisms are gated on a derived, fallible result — "do we have an aim
lock?", "is the pose valid?", "did vision see the target?" — that can legitimately have no answer
on any given loop. When it has no answer, everything downstream of the gate stops together.

**Why it reads as several bugs.** The gate is invisible in the symptom. A real report of this
looked like four independent failures at once: gate doesn't move, turret doesn't move, auto-aim
doesn't move, intake doesn't work. Four subsystems, four apparent problems, one cause — a single
`if (hasLock)` wrapped around all of them. Debugging effort goes to four mechanisms in turn, and
each one checks out fine in isolation, which is the worst possible position to debug from.

**Why it happens.** It reads as safety at the time it is written: "don't run the intake unless we
know where we are." But a sensor-fusion result is not a safety interlock, it is an *estimate*, and
estimates are legitimately absent sometimes — occluded target, bad frame, mid-recalculation. The
gate converts a normal transient into a total mechanism stop.

**Fix pattern** (confirmed against a team's own working version of the same robot code, which did
it this way and did not exhibit the failure):

- Command mechanisms **unconditionally, every loop**, from whatever solve is available — a
  distance-based flywheel/hood command runs off the current distance estimate whether or not an aim
  lock has converged.
- Drive sequencing mechanisms (gates, feeders, intakes) from **plain timers or driver input**, not
  from the fusion result.
- Let the lock state gate **only the thing it actually describes** — whether to *fire*, not whether
  the robot is allowed to move its intake.

**Generalizes to:** any auto or teleop where mechanism enablement is chained to vision, odometry
confidence, AprilTag visibility, or a solver's convergence flag. The test question is: *if this
estimate returns nothing for two seconds, how many mechanisms stop?* If the answer is more than
one, the gate is in the wrong place.

**Tier:** corpus-derived, team-reported symptom with a code-confirmed fix pattern. Not from the
verbatim handoff.

### Two named tuning constants sharing one literal

**Shape.** Two distinct, differently-named tuning fields are set to the identical value — e.g. a
"fire at this distance" threshold and a "hold at this distance" threshold both hardcoded to the
same number. Whatever behaviour was supposed to vary between them cannot.

**Why it is silent.** Both constants are individually plausible. Nothing is out of range, nothing
fails to compile, and each value looks like a real measurement. The symptom is a mechanism that
appears not to respond to a parameter it genuinely reads — reported in one real case as a shooter
firing at the wrong range with a hood that "doesn't seem to move", when the hood was in fact
correctly tracking a distance that never changed.

**Why it happens.** Usually a copy-paste during tuning, or a placeholder that was meant to be split
later. Sometimes it is legitimate — two thresholds can genuinely coincide — which is why this is a
**smell, not a defect**: the finding is "confirm this is deliberate", not "this is wrong".

**Detectable deterministically.** `failure_mode_lint.py`'s `duplicate_tuning_literal` check flags
two or more distinct tuning-constant names in one file sharing an identical non-trivial literal.
Trivial values (0, 1, -1) are excluded — they coincide constantly and flagging them would bury the
real signal.

**Tier:** corpus-derived, team-reported symptom, code-confirmed cause.

## Source tiers (Rule 7)

- **Tier-1:** the ASEE PEER survey; FIRST's own troubleshooting docs.
- **Tier-2:** Chief Delphi / FTC Open Alliance community reports; the
  `wpilibsuite/SystemcoreTesting` alpha-tester GitHub issues.

Any claim resting only on tier-2 must be labeled tier-2 wherever this file's
content is surfaced downstream, never presented with tier-1 confidence.
