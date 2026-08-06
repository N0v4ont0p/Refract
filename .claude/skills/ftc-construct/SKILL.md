---
name: ftc-construct
description: 'Config-gated FTC robot code generation, grounded in library documentation, the elite-team pattern corpus, and the hardware catalog: scaffolds new OpModes, subsystems, and mechanisms from the quickstart interface template (Drivetrain/Shooter/Turret/Intake) once a team config is confirmed, and runs a mandatory rule-check and code-review verification pass on everything it writes before declaring anything done. Use whenever the user wants NEW robot code written from scratch — a new OpMode, subsystem, or mechanism feature ("write a teleop", "add an intake subsystem", "generate the shooter code"). Reads the confirmed team-config.yaml by reference; if none exists or required fields are unconfirmed, hands back to ftc-team-config rather than generating against a guess — this skill never re-elicits a config itself. Does not review or audit code that already exists in the repo (ftc-code-review) and does not establish or change the config itself (ftc-team-config).'
---

# FTC Construct

Generation is where every other skill's discipline either pays off or gets thrown away in one
sitting: a config confirmed field-by-field, a corpus provenance-tagged pattern-by-pattern, a
hardware catalog cited value-by-value — all of it is wasted if the actual generated code guesses
an API call, invents a tuning constant, or writes a mechanism the config doesn't declare. This
skill exists to make code generation as grounded as every other skill already is, and to check its
own output the same way a reviewer would, before calling anything done.

Read `references/standing-principles.md` (suite root) first — the deterministic-first, abstention,
and ask-don't-guess principles there apply here at least as much as anywhere else in the suite. The
suite root is the directory containing `core-feature-model.yaml`; paths below are relative to it
unless stated otherwise.

## Files this skill reads

| File | Role |
|---|---|
| `team-config.yaml` (team's project root) | the confirmed config this generation is *against* — read first, never re-elicited here |
| `.claude/skills/ftc-team-config/scripts/validate_config.py` | authoritative `generation_allowed` gate — read by path, not re-implemented |
| `refract-suite/ftc-shared-foundation/quickstart-template/` | the interface-based scaffolding source (Drivetrain fixed + per-mechanism interfaces derived from `season_mechanisms`) |
| `refract-suite/ftc-shared-foundation/references/library-docs/<library>/` | grounded API usage — `pedro-pathing/`, `ftclib/`, `roadrunner/`, `rev-robotics/`, `limelight/`, `gobilda-build-guides/`, `ftc-sdk/`, `easyopencv/`, `ftc-dashboard/`, `ticktree/` (Phase G — pre-alpha, API unstable) |
| `.claude/skills/ftc-corpus-builder/references/patterns/*.yaml` | provenance-tagged elite-team patterns — cited with confidence/provenance displayed faithfully, same discipline as ftc-code-review |
| `.claude/skills/ftc-hardware-lookup/references/catalogs/` + `scripts/motor_math.py` | any spec/tuning value used in generated code — read by path, never guessed |
| `.claude/skills/ftc-code-review/scripts/{config_lint.py,failure_mode_lint.py}` | mandatory post-generation verification (step 5 below) |
| `scripts/emit_tuning.py` (this skill) | tuning constants: `render` supplies them from the confirmed config so none are ever model-authored; `verify` is the mandatory post-generation provenance gate (step 5) |
| `scripts/check_freshness.py` (suite root) | mandatory post-generation freshness gate, run BEFORE the rule-check below (step 5) |
| `.claude/skills/ftc-rule-check/scripts/rules.py` | mandatory post-generation legality re-check, at genuine parity with ftc-rule-check's own flow (step 5 below) |
| `known-failure-modes.md` (suite root) | the taxonomy the quickstart template already counters by construction — still worth checking generated additions against |

## The flow

### 0. Precondition — confirmed config, or hand back

Run, whether or not `team-config.yaml` exists yet — the script handles a missing file cleanly, no
existence check needed here first:

```bash
python3 .claude/skills/ftc-team-config/scripts/validate_config.py <team-config.yaml>
```

`config_found: false` in the output means there's no config on disk at all; `generation_allowed:
false` with a populated `unconfirmed_mandatory` means one exists but isn't ready. Either way — if
`generation_allowed` is not `true` — **stop and hand back to ftc-team-config.** State plainly
what's missing (the exact `unconfirmed_mandatory` list the script returns); do not ask the missing
questions yourself, and do not generate against a guess. This is this skill's version of the R58
gate ftc-team-config already carries: a wrong guess that compiles is worse than a handback that
costs one turn.

### 1. Derive the interface set

Same rule as ftc-team-config's generation-rules section: `Drivetrain` is the one always-fixed
interface; every other mechanism interface comes from the confirmed config's `season_mechanisms`
keys, resolved through `season-extensions/ACTIVE`. No hardcoded mechanism list — read the config,
not a memory of what any one season happens to have.

### 2. Scaffold from the quickstart template

Copy and adapt from `refract-suite/ftc-shared-foundation/quickstart-template/` — it already ships
one example implementation per DECODE mechanism (`MecanumDrivetrain`, `FlywheelShooter`,
`SingleAxisTurret`, `RollerIntake`) plus a telemetry-by-default `TeamOpMode` base and
`RobotConstants`. Match what the config actually selects:

- config value matches an existing template example → adapt that example directly (rename, wire
  to the team's actual `hardwareMap` device names);
- config value has no template example (a mechanism option the template did not cover, or a
  season after DECODE) → write a new class against the mechanism's interface, following the
  template's own conventions (telemetry wired through `TeamOpMode`, no hardware access outside the
  owning subsystem class);

  **If the shipped template is the wrong base entirely** — the team is starting a project from
  nothing, or the config selects a stack the template's examples don't sit on — offer real upstream
  starters, **filtered by what the config already confirms**, not as a menu of everything that
  exists. A team that has confirmed `pedro_pathing` has no use for RoadRunner's starter, and
  listing it invites a choice that contradicts a decision already made. Verified upstream, not
  recalled — each name and its state was checked against the real repo:

  | Offer when | Starter | State (verified 2026-08-06) |
  |---|---|---|
  | `software_stack.pathing == pedro_pathing` | `Pedro-Pathing/Quickstart` | active, current — Pedro's own official starter |
  | `software_stack.pathing == roadrunner` | `acmerobotics/road-runner-quickstart` | active — RoadRunner's own official starter; it does exist |
  | `software_stack.opmode_style == ftclib_command_based` | `FTCLib/FTCLib-Quickstart` | the generic command-based starter; last pushed 2023-08, no newer official one exists |
  | always | this suite's own `quickstart-template/` | interface-based, config-derived — the default |

  Pedro's starter and FTCLib's are **both** offerable to one team, because they answer different
  axes (`pathing` vs `opmode_style`) and compose. Two Pedro repos that turn up in a search —
  `Pedro-Pathing/Pedro-Pathing-Quickstart` and `Pedro-Pathing/Beginner-Quickstart` — are **archived**
  (both since 2024-12), and the first's own description redirects to the current one. Never offer
  either; an archived starter is a dead end a team discovers weeks later.

  **Sequencing caveat, flagged rather than resolved.** This filtering works here because
  `software_stack.pathing` and `opmode_style` are in the mandatory always-ask set, so step 0's
  `generation_allowed` gate guarantees both are confirmed before this skill runs. It does **not**
  hold for a team with no project at all asking "how do we start" — that arrives at
  `ftc-team-config` *before* any stack is confirmed, and there the filter has nothing to filter on.
  Whether a starter should be offered unfiltered at that point, or whether the pathing question
  should simply be asked first, is a real open design question about question ordering — not
  something to settle inside this skill's generation branch. Raise it; don't improvise a resolution.
- a `season_mechanisms` key is `none` → no code for it, not commented out — same rule as
  ftc-team-config's generation rules.

### 3. Ground the implementation

- **API usage is grounded per config axis that selects a library — required, not incidental to
  whichever axis happens to be named here.** Cite
  `refract-suite/ftc-shared-foundation/references/library-docs/<library>/` for whichever library the
  relevant axis actually selects:
  - `software_stack.pathing` / `software_stack.opmode_style` → Pedro Pathing / RoadRunner / FTCLib's
    command framework / raw SDK;
  - `sensing.vision` → `limelight/` when `limelight_3a`, **`easyopencv/` when `webcam_easyopencv`**
    — this axis is in scope exactly like `software_stack` is; never skip grounding a vision pipeline
    just because vision isn't `software_stack`.
  - **`software_stack.behavior_layer` → `ticktree/` when `ticktree`** (Phase G — pre-alpha, API
    unstable; re-check the doc header's fetch commit against the library's actual current state
    before trusting it against a materially newer TickTree commit). TickTree is orthogonal, not a
    replacement for `pathing`/`opmode_style` — it composes WITH whichever command framework the
    config already selects, sitting above it as a reactive arbitration layer. Two constraints from
    the library's own design, not incidental: (1) `OpModeTreeRunner` is composition-only — never
    generate code that extends it as a base class; the correct shapes are
    `OpModeTreeRunner.runLinear(tree, this::opModeIsActive)` after `waitForStart()` for
    `LinearOpMode`, or explicit `loop(){tree.tick();}`/`stop(){tree.halt();}` for the raw `OpMode`
    base (no wrapper exists for that path, by design). (2) Command leaves
    (`FtcLibCommandAction`/`SolversLibCommandAction`) are RUNNING/SUCCESS only — never generate code
    that assumes a wrapped `Command` can directly signal FAILURE; express it via `Timeout`/`Guard`/
    `Condition` structure instead, per the library's own documented constraint.
  Read the relevant file before writing a call against an unfamiliar API in either case; don't
  recall it.
- **Template-inherited domains — read before extending, not just before adopting.** The quickstart
  template already wires FTC Dashboard (telemetry via `RobotTelemetry`, tunables via
  `RobotConstants`'s `@Config`). Adapting that existing pattern needs no fresh read. But the moment
  a request EXTENDS the baseline — a new tunable, a new graphable field, a custom dashboard widget —
  read `ftc-dashboard/` first: a `@Config` field alone does not make a value graphable, and other
  FTC-Dashboard-specific mechanics don't fall out of the template's existing wiring by inspection
  alone.
- **Catalog values** (gear ratios, spec numbers, encoder counts) are never generated — read them
  from `ftc-hardware-lookup`'s catalog and scripts by path, exactly as ftc-hardware-lookup itself
  would.
- **Device names come from `device_map`, verbatim.** Every `hardwareMap.get()` call this skill
  writes uses the exact confirmed string from the config — never a convention, never a tidied-up
  version of it, never a library default. If a device the generated code needs has no `device_map`
  entry, that is a handback to `ftc-team-config`, not a name to invent: the config is incomplete for
  what was asked.
- **Physical tuning constants — the hard rule (standing-principles §13).** A robot's mass, a PIDF
  gain, a pod offset, a ticks-per-inch scalar: these are properties of one physical robot, derivable
  from no source that exists. Unlike every other wrong value this suite guards against, a wrong one
  here compiles, deploys, passes every linter, and drives the robot. Two paths, no third:

  **This is mechanised, not left to care.** Do not type a tuning number into generated code at all
  — write the structure with placeholders and let the value come from a lookup, the same way
  `motor_math.py` supplies a motor spec:

  ```bash
  python3 <this-skill>/scripts/emit_tuning.py render <template> --config <team-config.yaml> -o <out>
  ```

  `{{tuning.<field>}}` and `{{device.<key>}}` resolve against the confirmed config. A
  measured+confirmed constant renders as its exact value; anything else renders as `Double.NaN`
  plus the field's real tuning procedure. A placeholder for a field the config does not carry is a
  **hard refusal**, not a fallback — that is a handback to `ftc-team-config`.

  **(a) The config carries real tuned values** (`origin: measured`, `confirmed: true`) — carry them
  forward **verbatim**. Never regenerate, never round, never "adjust to something more reasonable",
  never substitute a library default because the real value looks unusual. A measured constant that
  looks wrong is a fact about that robot, not an error to correct. If it genuinely looks wrong, say
  so to the user; do not quietly change it.

  **(b) The config has no tuned value** (`origin: untuned`, or `tuning_status` is `untuned` /
  `not_yet_tunable`) — generate a **correctly-structured scaffold** with every tuning-dependent
  field loudly marked, using the same fail-fast convention this suite already applies elsewhere
  (the R92/R93 pattern shown publicly on the docs site), now extended to this domain:

  ```java
  // TODO(UNTUNED): produced by Pedro's ForwardZeroPowerAccelerationTuner — see
  //   library-docs/pedro-pathing/tuning.md. This is NOT a placeholder to be filled in with a
  //   plausible number; run the tuner on THIS robot. Path following will be wrong until you do.
  .forwardZeroPowerAcceleration(UNTUNED)   // no value: this must not silently default
  ```

  The structure is real, the wiring is real, the value is conspicuously absent. Attach the actual
  tuning procedure read from `library-docs/<library>/` — Pedro's tuner sequence, RoadRunner's
  `ForwardPushTest`/`LateralPushTest`/ramp-logger/`ManualFeedforwardTuner` order — never a procedure
  written from memory, and never a generic "tune the PID until it works."

  **A fabricated-but-plausible tuning constant is never acceptable output. There is no "reasonable
  default" fallback, and a library default is not an exception** — it is the worst case, because it
  is a real measured number off somebody else's robot and reads as tuned (Pedro ships
  `mass = 10.65`, `forwardZeroPowerAcceleration = -34.62719`; RoadRunner ships `inPerTick = 1`,
  `kS = 0`). This is enforced by construction, not by intent: `origin` is a closed set of
  `{measured, untuned}` in `core-feature-model.yaml`, `validate_config.py` rejects any other origin
  and rejects a non-null value under `untuned`, and step 0's `generation_allowed` gate already ran.
  A guessed constant has no representable form in the config this skill reads from, so there is
  nothing to carry forward and nothing to launder into output.
- **Corpus patterns**: when a pattern from `ftc-corpus-builder/references/patterns/*.yaml` applies
  (its `applicable_when` matches the confirmed config), cite it — but display its `confidence` and
  `provenance.classification` exactly as stored, never inflated, and carry its `notes` caveats
  verbatim. Same discipline ftc-code-review's pattern-citation step already enforces — a pattern's
  provenance is displayed here, not re-graded.
- **REV setup/wiring docs** (`rev-robotics/`) ground any generated hub or device-configuration code
  the same way — read the relevant file, don't recall an addressing/naming convention from memory.
  **goBILDA build guides** (`gobilda-build-guides/`) are a known, permanent partial exception: they
  are physical assembly instructions, not code/API references, and even the closest-fit file
  (`viper-slide-linear-slide-build.md`) has been confirmed to lack the derived numbers (net travel
  distance) generation actually needs — a corpus-completeness gap, not a wiring one. Treat a miss
  here as an ask-don't-guess abstention (ship a fail-safe placeholder with a TODO, per
  standing-principles), not something to keep searching the guide for.

### 4. Structural rules — non-negotiable, same as ftc-team-config

- No code for a mechanism the config declares `none` or leaves absent.
- Never touch `libs/` — a hard legality line (an FTC-illegal Robot Controller app), not a style
  preference.
- Mark generated files' origin: a short header comment noting this suite generated the file (the
  same lineage marker ftc-team-config writes as `_meta.suite_generated_code: true` in
  `team-config.yaml`), so a future corpus-mining pass never mistakes this suite's own output for
  independent confirmation of its own recommendations.

### 5. Mandatory verification — no exceptions, run before declaring anything done

Every generation ends here, unconditionally, whether the code "looks right" or not.

**Linters, unconditional:**

```bash
python3 .claude/skills/ftc-code-review/scripts/config_lint.py <code_dir> --config <team-config.yaml>
python3 .claude/skills/ftc-code-review/scripts/failure_mode_lint.py <repo_path>
```

**Rule-check, at genuine parity with `ftc-rule-check`'s own flow — retrieval-plus-citation-existence
alone is not enough, and a config being *confirmed* is not the same claim as a mechanism being
*legal*:**

0. **Freshness first, not skipped.** Run `python3 scripts/check_freshness.py` (suite root) before
   anything else in this step — same script, same call, `ftc-rule-check` itself runs as its own
   step 0. If it reports `STALE` or `UNVERIFIABLE`, that caveat travels into the final report
   verbatim; do not silently proceed as if the corpus is guaranteed current.
1. **Retrieve.** For anything the generated code touches that has a rules dimension (mechanism
   restrictions, size/expansion limits if relevant), run
   `python3 .claude/skills/ftc-rule-check/scripts/rules.py lookup <id>` — rule text plus one hop of
   cross-references.
2. **Reason, then form a verdict — not optional.** Read the retrieved text, including the
   cross-referenced neighbors (a size/mechanism rule usually hinges on one), and reason over it
   against what the generated code actually does. Emit the same structure `ftc-rule-check` itself
   would: `{verdict: legal|illegal|ambiguous, citations: [{id, text}], reasoning}`. A lookup without
   this step is retrieval, not a verdict.
3. **Verify citations before shipping — non-negotiable.** Run
   `python3 .claude/skills/ftc-rule-check/scripts/rules.py verify <id>`; an unverified citation
   doesn't ship, same as `ftc-rule-check`'s own step 3.
4. **Ambiguous is a real outcome.** If reasoning genuinely can't resolve to legal/illegal, the
   verdict is `ambiguous`, not a confident guess — same as `ftc-rule-check`'s own step 4.

**Tuning-constant provenance, unconditional:**

```bash
python3 <this-skill>/scripts/emit_tuning.py verify <code_dir> --config <team-config.yaml>
```

This is the gate that actually closes the generation path, and it is not a default-matcher: every
numeric literal in a tuning-field position must equal what the confirmed config says, exactly. A
field marked `untuned` must carry `Double.NaN`, not a number. A tuning field with no config entry
at all is an error. It does not need to recognise a value as invented or as a library default —
only as *not the number the config says* — which is why it catches cases the check below cannot.

`failure_mode_lint.py`'s `template_default_tuning_constant` check remains as the second layer,
covering the case `verify` cannot see: constants a team never wrote at all, inherited silently from
a library's own field initializers (Pedro ships three distinct such sets). A finding from either
against this skill's own output is a generation bug, not a note to pass along.

Report the **combined** result — "code written and verified against rules and known failure
patterns," with the actual linter output, the freshness status, and the full `{verdict, citations,
reasoning}` attached — never just "code written." If either linter reports a finding, the freshness
check flags `STALE`/`UNVERIFIABLE`, or the rule-check verdict comes back `illegal` or `ambiguous`,
surface it plainly before calling the task done. A finding on code this skill just generated is not
a reason to soften how it gets reported.

## What this skill does not do

Establishing or re-opening the config itself (`ftc-team-config` — this skill reads a confirmed
config, it does not create one). Reviewing or auditing code that already exists in the repo
(`ftc-code-review` — this skill's linter calls are a generation-time gate, not a standalone audit;
reviewing pre-existing code is CR's job). Hardware specs and math with no code-generation request
attached (`ftc-hardware-lookup`). Legality verdicts with no code attached (`ftc-rule-check`). If
invoked with no confirmed config, say so and hand back — never improvise a config to unblock
generation.
