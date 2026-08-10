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

### Symptom-patching a layered root cause by extending a wait timer

**Shape.** A mechanism behaves wrong at the boundary between two states (a chassis stop, a
turn-to-hold transition, a settle). The fix tried first is "wait longer" — extend a settle timer,
add a sleep, push a threshold. It doesn't work. The timer gets extended again. It still doesn't
work. Each attempt treats the *symptom* (still moving/wobbling when it should be still) as if it
had one cause, when it actually has several, stacked.

**Why "add more wait" fails silently instead of obviously.** Extending a timer is never wrong on
its face — more time can only help a genuine settle problem, so a failed attempt doesn't disprove
the theory, it just looks like "needs even more." That makes this failure mode self-concealing:
there is no natural point where the approach announces itself as wrong, only a growing pile of
timer edits that keep not working.

**A real, worked example — three real, independent causes, each masked by the layer below it:**

1. **The mechanism was never actually stopped.** A path-following library declaring a path
   "complete" is a statement about the parametric position crossing a threshold, not a statement
   that the chassis has zero velocity — cutting motor power lets a robot *coast*, it does not brake
   it. The first "wobble" was the chassis still physically moving when the next step assumed it was
   still.
2. **Once genuinely stopped, the thing meant to hold still couldn't.** A feedback controller with a
   bang-bang or under-damped correction term can hunt around its target instead of settling on it —
   the classic feedback limit-cycle. Waiting longer doesn't fix a controller that oscillates
   *because* it's still running its correction loop; it just oscillates for longer.
3. **Once the controller could genuinely hold, it was holding against stale information.** A
   filtered rate/velocity estimate computed during a fast preceding motion does not reset to zero
   the instant that motion ends — a filter carries lag by design. A hold command issued right after
   a hard turn was fighting a rotation-rate estimate the robot no longer actually had.

Each layer was invisible until the one above it was fixed — you cannot diagnose "does the hold
controller oscillate" while the chassis is still coasting, and you cannot diagnose "is the rate
estimate stale" while the controller itself still hunts. That nesting is exactly why this needed
going one level deeper each time rather than converging on a single culprit.

**The test question:** when a "wait longer" fix doesn't work, the next question is never "wait
longer still" — it's "what, mechanically, is different about the state *after* the wait that the
current fix assumes is true?" Chassis actually at rest (a real BRAKE + measured-velocity check, not
just zero commanded power)? Controller actually converged (read its own error/output, not just
elapsed time)? Any filtered estimate actually reset for the new context (or still carrying lag from
what just happened)? A settle problem that survives a second timer extension is a strong signal the
real cause is structural, not durational.

**Generalizes to:** any transition boundary in an auto or teleop — a stop-then-shoot, a
turn-then-hold, a deploy-then-verify — where "add a delay" is the first fix reached for. The
underlying lesson is the same one this whole taxonomy is built on: a runtime-semantics/control
problem that looks environmental (flaky, inconsistent, "just needs tuning") until traced to its
actual mechanical cause.

**Tier:** corpus-derived, team-reported symptom sequence with a code-confirmed cause at each layer.
Not from the verbatim handoff.

### Silent build-toolchain break from an unpinned or partially-pinned version

**Shape.** A fresh clone, or a routine dependency bump, fails to build — and the failure presents
as a wall of unrelated compile errors, not as a toolchain version message pointing at the real
cause.

**Concrete mechanism, verified rather than assumed.** An Android Gradle Plugin upgrade began
requiring a specific Android build-tools version that the project had not pinned, and picked its
own (newer) default. An explicit `buildToolsVersion` pin placed in one shared Gradle file was
**silently ignored** — AGP read the pin from a different file than the one it was declared in, so
the fix looked complete (the pin existed, in a plausible location) while doing nothing. The pin
only took effect once duplicated into the specific module AGP actually consults for it.

**Why it reads as a code problem.** A build failure surfaces as compile errors in application code,
because that's where the toolchain gives up — not as a message naming the actual mismatched
version. Nothing points at Gradle or AGP specifically, so debugging effort goes to the code first.

**The test question:** when a build that previously worked (or a fresh clone of a working repo)
fails with a broad wall of errors rather than one specific one, check the toolchain version chain
(AGP version, Gradle wrapper version, any pinned SDK/build-tools versions, and *which specific
file* each pin actually lives in) before spending time in the application code itself. A pin that
exists somewhere is not the same claim as a pin that is being read from where it needs to be read.

**Generalizes to:** any FTC team on a recent Android Gradle Plugin version, and more broadly to any
project where a version pin's *effectiveness* depends on which of several plausible config files it
was placed in — the existence of a pin and its being honored are two different facts, and only one
of them is usually checked.

**Tier:** corpus-derived, code-confirmed (the pin's actual point of effect was verified by moving it
and re-building, not inferred from documentation). Not from the verbatim handoff.

### A latch or freeze silently poisons every downstream read

**Shape.** Some computed state (a sensor-fusion result, an aim solution, any derived struct) gets
deliberately frozen or latched — a legitimate optimization, done to stop recomputing or re-acting on
noisy input for a moment. The freeze is real and intentional. What's missing is an audit of
everything that *reads* that state afterward: every one of those readers is now looking at a
snapshot, and nothing about the read distinguishes "fresh" from "frozen."

**Concrete mechanism.** A freeze condition triggers (e.g. holding a lock steady): the update path
short-circuits and stops writing the struct. Readiness or downstream logic keeps reading the same
struct fields it always did. Those fields are correct at the moment of freeze and **silently stop
being correct** the instant the real world moves on, with nothing in the read path signaling that.

**Why this is worse than a stale value in isolation.** A single stale read is a bounded bug. A
latch feeding *multiple* independent downstream consumers turns one freeze into a cascade that can
loop on itself: consumer A reads the frozen struct and reports "not ready" for an unrelated reason
(e.g. a different subsystem is still settling); the system waits; once that unrelated reason
resolves, consumer A re-reads the *same* frozen struct — because nothing ever un-froze it — and
reports "ready" against data that was true several cycles ago and may no longer be. The action that
fires does so against the stale snapshot, not the current state.

**The fix, general across any latch/cache/freeze pattern:** when a value gets deliberately frozen,
audit every reader of it, not just the writer's own logic. Two disciplines, either is sufficient on
its own but they compose:

- **Mark the freeze visibly** on the struct itself (a `frozenAt` timestamp, a `stale` flag) so a
  reader can at least detect it's looking at a snapshot, rather than trusting the fields blindly.
- **Release the latch the instant the condition that justified it is gone.** A freeze that outlives
  its own justifying condition is not an optimization anymore, it's an unintentional cache with no
  invalidation.

**Generalizes to:** any latch, cache, debounce, or "hold the last good value" pattern feeding more
than one downstream consumer — not specific to aim/vision/sensor-fusion, though that's a common
place to reach for this optimization. The test question: when this value is frozen, does every
reader of it know, and does anything ever tell them to stop trusting it?

**Tier:** corpus-derived, team-reported symptom sequence (readiness state cycling between multiple
mechanisms while the frozen struct never actually updated) with a code-confirmed cause. Not from the
verbatim handoff.

### A proximity-triggered event breaks down as trigger points converge

**Shape.** An autonomous sequence fires an event (a shot, a mechanism action) when the robot's
position comes within some radius of a target point. This works fine when target points are far
apart. It silently breaks when two or more target points end up close enough together that no
single radius can distinguish "near point 1" from "near point 3" — being close to one legitimately
also satisfies being close to the other, and the trigger fires against the wrong target, or fires
early, or fires twice.

**Why it's easy to build this way and easy to miss.** Proximity-triggering is the natural first
design for "do X near this spot" — it doesn't require tracking *which* leg of the path the robot is
currently on, just distance to a point. It works throughout early testing, when target points happen
to be well-separated. It breaks specifically once a path gets refined toward tighter, more efficient
routing — which pulls target points closer together — so the failure tends to appear *later* in
tuning, on a path that already worked, rather than immediately.

**The fix.** Trigger on **leg arrival**, not proximity to a point: track which segment of the path
the robot is currently executing (an index, a named waypoint-reached flag, anything that identifies
the *leg*, not just a distance) and fire the event when that specific leg is reached or completed,
independent of how close its endpoint happens to sit to some other leg's endpoint. This is a strictly
stronger signal than proximity — it can't be fooled by two points being near each other, because it
never asks "how close am I" in the first place.

**The test question:** for any proximity-based trigger, check the actual minimum distance between
every pair of trigger points the path visits. If any two are closer together than the trigger radius
you're using — or would be, after the routing gets refined further — the radius cannot tell them
apart and the trigger needs to become leg-based before it silently misfires.

**Generalizes to:** any autonomous sequence with more than one proximity-triggered event, in any
season — the failure is about the trigger topology, not about what the event does once triggered.

**Tier:** corpus-derived, calculated finding (real minimum-distance computation on real path
coordinates showed points within a fraction of an inch of each other), not from the verbatim
handoff.

## Source tiers (Rule 7)

## Source tiers (Rule 7)

- **Tier-1:** the ASEE PEER survey; FIRST's own troubleshooting docs.
- **Tier-2:** Chief Delphi / FTC Open Alliance community reports; the
  `wpilibsuite/SystemcoreTesting` alpha-tester GitHub issues.

Any claim resting only on tier-2 must be labeled tier-2 wherever this file's
content is surfaced downstream, never presented with tier-1 confidence.
