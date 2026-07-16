# Library-docs utilization audit — Phase B, findings + fixes + re-verification

Same discipline as TRACEABILITY.md, applied to the 57-file library-docs corpus instead of PLAN.md's
requirements. Every file gets a row. Two failure conditions checked explicitly: a file nothing reads
(orphaned) and a domain a skill needs but has no wired path (a gap the fetch/build pass should have
caught). **This revision adds the six fixes closing Phase B, each with a real re-test — not just the
findings pass.** The original findings-only pass is preserved below with fix status layered in, not
overwritten, so the audit trail stays honest about what was found vs. what was then fixed.

## Method

Step 1 (findings pass): grepped every SKILL.md for any reference to `library-docs`, per-library
directory names, or per-file names — confirmed via `grep -rn` that **only `ftc-construct` (plus, as
of Phase B fix 6, a narrow `ftc-code-review` pointer) references this corpus at all**. Read the FLOW
section (not just the files-read table) line by line against each file's plausible use.

Step 2 (findings pass): for 6 of the 8 libraries the phase named (Pedro, REV, Limelight, goBILDA,
EasyOpenCV, FTC Dashboard), ran a real agent with live tool access against a real confirmed fixture,
then independently re-verified every cited API claim against the actual fetched file with `grep`.
FTCLib and FTC SDK reused prior verified evidence.

Phase B fixes (this revision): six fixes applied per instruction, each re-tested with a real
scenario — see "Phase B fixes applied" below, then the matrix and Steps 3-4 updated in place to
reflect them.

---

## Step 1 — Utilization matrix (57/57 files) — updated with fix status

Legend: **CO** = ftc-construct. **File-level** = FLOW names this exact file. **Directory-level** =
FLOW names the library generically — acceptable per this project's pointer-not-enumerate convention.
**Table-only** (pre-fix) = reachable only via the files-read table, not FLOW — now upgraded to
**Directory-level, required** for EasyOpenCV/FTC Dashboard per fix 2. **Thin-fit** = wired nominally
but content type doesn't clearly match code-generation use. **Orphaned** = no plausible owner.

### pedro-pathing/ (10 files) — owner CO, gated by `software_stack.pathing == pedro_pathing`

| File | Wired? | Note |
|---|---|---|
| installation.md | Directory-level | — |
| path-building.md | Directory-level, **verified** | 6 API calls traced to exact lines |
| followers.md | Directory-level, **verified** | `!follower.isBusy()` traced to line 171 |
| tuning.md | Directory-level | Unexercised |
| localization-tuning.md | Directory-level | Unexercised |
| pidf-tuning.md | Directory-level | Unexercised |
| swerve.md | Directory-level, thin-fit | Pedro's built-in support targets mecanum; swerve needs a custom `Drivetrain` — surfaced as a real caveat in testing, not silently assumed |
| customization.md | Directory-level | Unexercised |
| examples.md | Directory-level, **verified** | 5 of 9 cited API calls traced here |
| ivy-commands.md | Directory-level, thin-fit | Pedro's own command layer vs. the config's FTCLib selection — unaddressed overlap, unchanged this pass |

### ftclib/ (14 files) — owner CO, gated by `opmode_style == ftclib_command_based` (template's baseline)

| File | Wired? | Note |
|---|---|---|
| installation.md | Directory-level | — |
| control.md | Directory-level | — |
| geometry.md | Directory-level | Unexercised |
| gamepad-triggers.md | Directory-level | — |
| hardware-wrappers/overview.md | Directory-level | — |
| hardware-wrappers/motors.md | Directory-level, **verified** | eval-1 + UX test |
| command-framework/overview.md | Directory-level | Unexercised |
| command-framework/subsystems.md | Directory-level, **verified** | eval-1 |
| command-framework/command.md | Directory-level | Unexercised |
| command-framework/command-groups.md | Directory-level | Unexercised |
| command-framework/command-scheduler.md | Directory-level | Unexercised |
| command-framework/binding-commands-to-triggers.md | Directory-level, **verified** | eval-1 + UX test |
| command-framework/robot-and-commandopmode.md | Directory-level | Unexercised |
| command-framework/convenience-features.md | Directory-level | Unexercised |

### roadrunner/ (4 files) — owner CO, gated by `pathing == roadrunner` — **FIX 3 APPLIED, now tested**

| File | Wired? | Note |
|---|---|---|
| installation.md | Directory-level, **verified (partial)** | Maven coordinates inferred from here for the import-path claim |
| trajectories.md | Directory-level, **verified (partial)** | **Fix 3 test result:** 7 of 11 cited API calls traced to exact quoted lines (`.setTangent`, `.splineTo`, `.lineToY`, `.splineToConstantHeading`, `Pose2d`/`Vector2d`, `Actions.runBlocking`). 4 were explicitly flagged NOT GROUNDED and stubbed rather than guessed: `actionBuilder()`'s entry point, the terminal `.build()`, the `MecanumDrive` constructor signature, and critically the **entire localizer/pose-read API needed for teleop heading correction** — none of these appear in the fetched docs. |
| tuning.md | Directory-level, **verified** | `MecanumDrive`/`TankDrive` class-choice line cited |
| core-concepts.md | Directory-level, **verified (partial)** | `HolonomicController.compute()` internals documented, but no public teleop-pose-read accessor — the same localizer gap as trajectories.md |

**New finding from the fix-3 test, not previously known:** RoadRunner's fetched docs cover
trajectory-*building* well but have a **real corpus gap for reading the robot's current pose during
teleop** (the exact thing a field-centric or heading-correction feature needs) — parallel in shape to
goBILDA's gap (files correctly consulted, genuinely missing the needed content), not a wiring problem.
The generated code stubbed the missing piece (`UnsupportedOperationException` + TODO) rather than
inventing a plausible-looking accessor name. Flagging for the same Phase F candidate list as goBILDA
(see below) — team 19859's actual RoadRunner usage, if any, likely has the real answer no fetched doc
provides.

### rev-robotics/ (5 files) — owner CO — **FIX 5 notes applied**

| File | Wired? | Note |
|---|---|---|
| control-hub-setup-and-firmware.md | Directory-level | Plausible fit, unexercised |
| device-configuration-and-expansion-hub.md | Directory-level, **verified** | Device-naming/RS485-addressing claim traced to 3 quoted lines |
| onbot-java-programming.md | **Orphaned — intentionally, per Fix 5.** | **Intentionally unreachable: the quickstart template is Gradle-based, `ftc-construct` never generates OnBot Java blocks.** Recorded here explicitly so this is never rediscovered as a mystery gap in a future audit — this is a structural consequence of the template's architecture, not an oversight. |
| sensor-integration-guide.md | Directory-level | Plausible fit, unexercised |
| troubleshooting.md | **No current owner — correctly excluded, per Fix 5.** | Diagnostic/symptom-driven content doesn't fit any current skill's stated job (not CO's generation-grounding remit, not CR's structural review, not RC's legality domain). Explicitly flagged as excluded-by-design rather than left silently orphaned — if a future skill's scope ever covers hardware troubleshooting narrative, this is the file to wire it to. |

### limelight/ (4 files) — owner CO, gated by `sensing.vision == limelight_3a`

| File | Wired? | Note |
|---|---|---|
| setup.md | Directory-level | Unexercised |
| pipelines.md | Directory-level, thin-fit | Camera-side config, not TeamCode — weaker fit than java-api.md |
| java-api.md | Directory-level, **verified** | 8 API calls traced |
| localization.md | Directory-level, **verified** | `updateRobotOrientation` traced here |

### gobilda-build-guides/ (8 files) — **FIX 4 permanent note applied**

| File | Wired? | Note |
|---|---|---|
| ftc-starter-bot-full-build.md | Thin-fit | No plausible code-generation use case |
| ftc-starter-bot-mecanum-drivetrain-variant.md | Thin-fit | Same |
| strafer-chassis-drivetrain-build.md | Thin-fit | Same |
| hammerhead-chassis-drivetrain-build.md | Thin-fit | Same |
| beeline-chassis-drivetrain-build.md | Thin-fit | Same |
| viper-slide-linear-slide-build.md | Thin-fit, **tested, data gap confirmed** | Correctly abstained (`SLIDE_MAX_TICKS = 0`, TODO) — the guide has assembly steps and BOM, not the derived net-travel spec generation needs |
| cascading-low-side-linear-slide-build.md | Thin-fit | Unexercised, same category |
| linear-actuator-kit-build.md | Thin-fit | Unexercised |

**PERMANENT NOTE (Fix 4 — this is now load-bearing text, not a one-off observation):** This is a
**known, structural corpus gap** — the source material (goBILDA's own public build guides) lacks the
derived specs code generation needs (net travel distance, not raw segment length); this is not a
wiring or routing defect, and re-auditing "why doesn't CO consult these more" in a future pass will
re-find the same answer. Correct abstention (fail-safe placeholder + TODO, per standing-principles'
ask-don't-guess rule) is the **designed, expected behavior** here, not a shortfall to fix by searching
harder. **Flagged explicitly as a Phase F target:** team 19859's own mechanisms (built from these same
goBILDA kits) almost certainly have the real measured travel distances no third-party guide provides
— a first-party measured-spec addition to the corpus (in a future phase, not this one) would close
this permanently in a way no amount of fetching more public documentation can. `ftc-construct`'s
SKILL.md §3 now carries this same note inline, so a live generation run abstains immediately rather
than re-discovering the gap by searching.

### ftc-sdk/ (6 files) — owner CO, gated by `opmode_style == raw_linear_opmode`

| File | Wired? | Note |
|---|---|---|
| sdk-overview.md | Directory-level | Unexercised |
| dev-environment-setup.md | Directory-level | Unexercised |
| opmode-basics.md | Directory-level, **verified** | eval-2 |
| hardware-configuration.md | Directory-level | Unexercised |
| programming-patterns.md | Directory-level | Unexercised |
| sensors.md | Directory-level | Unexercised |

### easyopencv/ (3 files) — owner CO, gated by `sensing.vision == webcam_easyopencv` — **FIX 2 APPLIED**

| File | Wired? | Note |
|---|---|---|
| setup.md | **Directory-level, required** (was table-only) | FLOW §3 now explicitly names `easyopencv/` for this axis value |
| camera-api.md | **Directory-level, required, verified** | Fix-2 re-test: quoted the exact new FLOW instruction, then correctly grounded every API call |
| pipeline-api.md | **Directory-level, required, verified** | Same |

**Fix 2 confirmed closed**: SKILL.md §3 now reads *"`sensing.vision` → `limelight/` when
`limelight_3a`, `easyopencv/` when `webcam_easyopencv` — this axis is in scope exactly like
`software_stack` is; never skip grounding a vision pipeline just because vision isn't
`software_stack`."* Re-test confirmed a fresh agent quoted this exact instruction from the FLOW
section (not the files-read table) before generating — correct behavior no longer depends on model
initiative.

### ftc-dashboard/ (3 files) — owner CO by template inheritance — **FIX 2 APPLIED**

| File | Wired? | Note |
|---|---|---|
| setup.md | **Directory-level, required** (was table-only) | — |
| telemetry-api.md | **Directory-level, required, verified** | Fix-2 re-test: quoted the new "template-inherited domains" instruction, then correctly used the packet API (not just `@Config`) |
| tuning-widgets.md | **Directory-level, required** | Named by the same new instruction; not needed for the specific test question asked |

**Fix 2 confirmed closed**: SKILL.md §3 now reads *"Template-inherited domains — read before
extending, not just before adopting... the moment a request EXTENDS the baseline — a new tunable, a
new graphable field, a custom dashboard widget — read `ftc-dashboard/` first."* Re-test confirmed a
fresh agent quoted this exact instruction and correctly distinguished "`@Config` alone doesn't make a
value graphable" as a result of reading the doc, not assuming the template's existing pattern was
sufficient.

---

## Tally — updated post-fix

- **57 files total.**
- **~44 files** directory-level-or-better wired, consistent with the pointer-not-enumerate
  convention. **17 files across 6 libraries (Pedro ×3, FTCLib ×3, Limelight ×2, REV ×1, FTC SDK ×1,
  RoadRunner ×4 partial, EasyOpenCV ×3, FTC Dashboard ×3)** now have independently re-verified real
  usage.
- **6 files (EasyOpenCV ×3, FTC Dashboard ×3): gap CLOSED (Fix 2).** Upgraded from table-only to
  required directory-level wiring, re-tested, confirmed no longer dependent on model initiative.
- **2 files (rev-robotics: onbot-java-programming.md, troubleshooting.md): explicitly annotated, not
  fixed (Fix 5) — correctly excluded by design, not silently orphaned anymore.**
- **8 files (gobilda-build-guides): explicitly annotated as a permanent structural corpus gap, not a
  wiring defect (Fix 4)** — correct abstention is the designed behavior; a Phase F target for
  first-party measured specs, not fixable by more fetching.
- **4 files (roadrunner): tested for the first time (Fix 3).** Trajectory-building is genuinely
  grounded; teleop pose-read/localizer access is a genuine corpus gap, same shape as goBILDA's —
  correctly stubbed, not fabricated, and flagged for the same Phase F candidate list.

**Post-fix state: 0 files with an unaddressed wiring gap.** Every file now has one of: verified real
usage, directory-level wiring not yet exercised (a testing-coverage gap, not a routing one), or an
explicit, load-bearing annotation stating why it's excluded/thin/structurally-gapped. Nothing is
silently orphaned anymore.

---

## Step 2 — Real-usage verification, per library (byte-match, not self-report) — updated

| Library | Result | Independently re-verified? |
|---|---|---|
| Pedro Pathing | **Genuinely grounded** — 9 API calls traced | Yes, grep-confirmed |
| FTCLib | **Genuinely grounded** (eval-1/eval-2 reuse) | Previously confirmed |
| REV Robotics | **Genuinely grounded** — addressing claim traced, model flagged its own convention vs. documented behavior | Not re-grepped |
| Limelight | **Genuinely grounded** — 8 API calls traced | Yes, grep-confirmed |
| goBILDA | **Not grounded — correctly abstained** (permanent corpus gap, Fix 4) | Yes, grep-confirmed the gap is real |
| EasyOpenCV | **Genuinely grounded, now via required instruction (Fix 2), not initiative** | Yes, grep-confirmed |
| FTC Dashboard | **Genuinely grounded, now via required instruction (Fix 2), not initiative** | Yes, grep-confirmed |
| FTC SDK | **Genuinely grounded** (eval-2 reuse) | Previously confirmed |
| **RoadRunner (Fix 3, new)** | **Partially grounded — trajectory-building real, localizer/pose-read a genuine corpus gap** | Yes, per-call grep-checked |

---

## Phase B fixes applied (six, in order of consequence)

### Fix 1 — CO's rule-check brought to genuine parity with RC's real 5-part flow

**Change:** `ftc-construct` SKILL.md §5 (both copies) now runs `check_freshness.py` as an actual
first step, and requires an explicit "reason over the retrieved, cross-referenced text and form a
`{verdict, citations, reasoning}`" step between `rules.py lookup` and `rules.py verify` — matching
RC's own 5-part structure instead of approximating it with retrieval-plus-citation-existence alone.

**Re-test:** ran a real generation scenario, forcing `check_freshness.py --live-tu 40` (a supported,
deterministic override — same mechanism this project's own R79 eval used) against the stored corpus
(TU 32), guaranteeing `STALE`. **Confirmed fixed**: the final user-facing report explicitly stated
*"Because the freshness check came back STALE, that verdict is caveated: this is the verdict from the
local corpus (current through Team Update 32), but it may not reflect the newest Team Update (live is
at TU 40, 8 updates ahead) — worth re-checking before relying on it at competition."* Previously, this
check never ran at all and nothing would have surfaced it.

### Fix 2 — EasyOpenCV and FTC Dashboard wiring made structural, not incidental

**Change:** SKILL.md §3's grounding bullets rewritten to explicitly cover the `sensing.vision` axis
(not just `software_stack`) and template-inherited domains (FTC Dashboard) requiring a fresh read
when EXTENDED beyond baseline.

**Re-test:** fresh agent, both scenarios, quoted the exact new instruction text from the FLOW section
before generating (not the files-read table) — confirmed above in the matrix. **Gap closed.**

### Fix 3 — RoadRunner tested for the first time, not assumed by analogy

**Change:** none to the skill itself — a genuine gap in test coverage, not in wiring.

**Re-test:** built a new confirmed fixture (`veteran-roadrunner-confirmed.yaml`), ran a real
generation scenario. **Result: partially grounded** — trajectory-building API calls (7 of 11) traced
to real quoted lines; the localizer/pose-read API needed for teleop heading correction is genuinely
absent from the fetched docs and was correctly stubbed rather than fabricated. This is a real,
newly-discovered corpus gap, not a false "verified" stamp — see the roadrunner/ matrix section and
the Phase F note there.

### Fix 4 — goBILDA gap marked permanent, not re-discoverable as a mystery

**Change:** `ftc-construct` SKILL.md §3 now states the goBILDA build-guides exception inline
("known, permanent partial exception... treat a miss here as an ask-don't-guess abstention... not
something to keep searching the guide for"), and this audit file carries the same note as a
load-bearing record, with an explicit Phase F flag: team 19859's own real measured specs are the
actual fix, not more fetching from third-party guides.

### Fix 5 — REV's two orphaned files explicitly annotated

**Change:** matrix entries for `onbot-java-programming.md` ("intentionally unreachable, template is
Gradle-based") and `troubleshooting.md` ("no current owner, correctly excluded") now state this
plainly in the audit record, so a future utilization audit doesn't re-discover these as new mysteries.

### Fix 6 — CR gets a narrow, explicit handoff to RC's real flow for legality-flavored existing-code queries

**Change:** `ftc-code-review` SKILL.md (both copies) gains a new §5, "Legality-flavored questions
about existing code — resolve via ftc-rule-check's real flow, don't approximate." When a review
already in progress turns out to hinge on legality, CR now invokes `check_freshness.py` +
`rules.py lookup` + `rules.py verify` directly (the exact same scripts, same discipline as CO's own
§5) and reasons to the same `{verdict, citations, reasoning}` shape — rather than reviewing it
structurally or guessing. This mirrors R27's existing sequential-boundary pattern (RC resolves a
table pointer into HW's data by path, never re-derived inline) applied to CR resolving a legality
pointer into RC's scripts by path, never re-derived inline either. Not new legality logic living in
CR, not a third skill — CR's "Not this skill" section updated to state the narrow exception
explicitly: a *pure* legality question with no code in view still goes to RC directly, unchanged.

**Re-test:** mixed structural-review + legality request against the real `sample-robot/` fixture
("review our shooter/turret code, and is a flywheel shooter actually legal?"). Confirmed: real
`check_freshness.py` invocation (returned `UNVERIFIABLE`, carried into the reasoning), real
`rules.py lookup`/`verify` against corpus-grepped candidate IDs (not guessed), verdict `legal` with
a citation independently re-checked byte-for-byte against `rules.json`. The ordinary structural pass
ran unmodified alongside it, catching a real R34 mismatch. **Gap closed, verified, not just
described.**

This resolves Step 4's open question: the combined chain is now reachable for existing code too, via
CR, using RC's actual mechanism rather than a duplicated approximation — closing the tradeoff the
original Step 4 analysis flagged (CR's scope grows narrowly and explicitly, rather than a third
overlapping entry point being built).

---

## Step 3 — Is "config → code → rule check → code review, like magic" actually closed? — UPDATED post-Fix-1

`ftc-construct`'s SKILL.md §5 now runs, precisely: `config_lint.py` + `failure_mode_lint.py`
(unchanged), then **`check_freshness.py` as an actual first step** (Fix 1), then `rules.py lookup`,
then **an explicit reason-to-verdict step producing `{verdict, citations, reasoning}`** (Fix 1), then
`rules.py verify`, with ambiguity handled as its own real outcome. This is now a line-for-line match
to RC's own 5-part flow, not an approximation of it:

| RC's real flow | Does CO's step 5 do this, post-fix? |
|---|---|
| Step 0: freshness | **Yes, now** — re-tested with a forced-STALE scenario, confirmed the caveat reaches the final report |
| Step 1: retrieve | Yes (unchanged) |
| Step 2: reason → verdict | **Yes, now explicit** — no longer implicit/model-dependent |
| Step 3: verify citations | Yes (unchanged) |
| Step 4: ambiguity as a real outcome | Yes, now explicit alongside the verdict step |

**This closes the gap the original audit found.** CO's mandatory rule-check is now genuinely at
parity with a direct RC invocation, not a lighter approximation of it — verified with a real forced
staleness test, not just a text-level comparison.

**Reporting UX**: unchanged from the original finding — still genuinely unified, confirmed again in
the Fix 1 re-test (the staleness caveat was woven into the same coherent narrative, not bolted on as
a separate disconnected block).

---

## Step 4 — RESOLVED (Fix 6), was previously held open

Original question: should the combined chain (config-relevance + rule-check + lint) be reachable
on-demand against code that already exists, not just newly generated code?

**Resolved via Fix 6**: `ftc-code-review` now has a narrow, explicit path to RC's real flow when a
review turns legality-flavored, using the same sequential-boundary pattern as the existing RC/HW
table-pointer (R27). This gives existing code the same combined-chain check newly generated code
gets, without growing CR's general scope, without new legality logic living inside CR, and without a
third overlapping skill — the exact tradeoff the original analysis weighed.

**Re-tested, confirmed working**: ran a real mixed request against the existing
`evals/fixtures/sample-robot/` code — "review our shooter/turret code, and is a high-speed flywheel
shooter actually legal?" `check_freshness.py` ran for real (returned `UNVERIFIABLE` this time — a
live fetch with no parseable Team Update marker — carried into the final reasoning rather than
dropped, exactly as the new §5 instructs). Candidate rule IDs (R207, R801) were found by grepping
the real corpus, not guessed; `rules.py lookup`/`verify` ran for real; verdict `legal`, citation
independently re-checked byte-for-byte against `rules.json` — matches verbatim. The ordinary
structural review ran alongside it, unmodified, and caught a real R34 config-mismatch
(`TurretAimer.java` references a turret against a config declaring `turret: none`), correctly routed
back to `ftc-team-config` rather than resolved inline — confirming the new §5 addition didn't
disturb CR's existing behavior.
