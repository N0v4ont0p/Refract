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

Read `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/standing-principles.md` (suite root) first — the
deterministic-first, abstention, and ask-don't-guess principles there apply here at least as much
as anywhere else in the suite. The suite root is the directory containing `core-feature-model.yaml`;
paths below are relative to it unless stated otherwise.

## Files this skill reads

| File | Role |
|---|---|
| `team-config.yaml` (team's project root) | the confirmed config this generation is *against* — read first, never re-elicited here |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-team-config/scripts/validate_config.py` | authoritative `generation_allowed` gate — read by path, not re-implemented |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/quickstart-template/` | the interface-based scaffolding source (Drivetrain fixed + per-mechanism interfaces derived from `season_mechanisms`) |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/references/library-docs/<library>/` | grounded API usage — `pedro-pathing/`, `ftclib/`, `roadrunner/`, `rev-robotics/`, `limelight/`, `gobilda-build-guides/`, `ftc-sdk/`, `easyopencv/`, `ftc-dashboard/` |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/patterns/*.yaml` | provenance-tagged elite-team patterns — cited with confidence/provenance displayed faithfully, same discipline as ftc-code-review |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-hardware-lookup/references/catalogs/` + `scripts/motor_math.py` | any spec/tuning value used in generated code — read by path, never guessed |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/{config_lint.py,failure_mode_lint.py}` | mandatory post-generation verification (step 5 below) |
| `${CLAUDE_PLUGIN_ROOT}/skills/ftc-rule-check/scripts/rules.py` | mandatory post-generation legality re-check (step 5 below) |
| `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/known-failure-modes.md` (suite root) | the taxonomy the quickstart template already counters by construction — still worth checking generated additions against |

## The flow

### 0. Precondition — confirmed config, or hand back

Run, whether or not `team-config.yaml` exists yet — the script handles a missing file cleanly, no
existence check needed here first:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-team-config/scripts/validate_config.py <team-config.yaml>
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

Copy and adapt from `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/quickstart-template/` — it already
ships one example implementation per DECODE mechanism (`MecanumDrivetrain`, `FlywheelShooter`,
`SingleAxisTurret`, `RollerIntake`) plus a telemetry-by-default `TeamOpMode` base and
`RobotConstants`. Match what the config actually selects:

- config value matches an existing template example → adapt that example directly (rename, wire
  to the team's actual `hardwareMap` device names);
- config value has no template example (a mechanism option the template did not cover, or a
  season after DECODE) → write a new class against the mechanism's interface, following the
  template's own conventions (telemetry wired through `TeamOpMode`, no hardware access outside the
  owning subsystem class);
- a `season_mechanisms` key is `none` → no code for it, not commented out — same rule as
  ftc-team-config's generation rules.

### 3. Ground the implementation

- **API usage** cites `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/references/library-docs/<library>/`
  for whichever library the config's `software_stack` actually selects (Pedro Pathing vs. RoadRunner
  vs. FTCLib's command framework vs. raw SDK) — read the relevant file before writing a call
  against an unfamiliar API; don't recall it.
- **Hardware values** (gear ratios, tuning constants, spec numbers) are never generated — read them
  from `ftc-hardware-lookup`'s catalog and scripts by path, exactly as ftc-hardware-lookup itself
  would.
- **Corpus patterns**: when a pattern from `${CLAUDE_PLUGIN_ROOT}/ftc-shared-foundation/patterns/*.yaml`
  applies (its `applicable_when` matches the confirmed config), cite it — but display its
  `confidence` and `provenance.classification` exactly as stored, never inflated, and carry its
  `notes` caveats verbatim. Same discipline ftc-code-review's pattern-citation step already
  enforces — a pattern's provenance is displayed here, not re-graded.
- **goBILDA build guides / REV / Limelight docs** ground any generated setup or wiring code the
  same way — read the relevant file, don't recall a wiring convention from memory.

### 4. Structural rules — non-negotiable, same as ftc-team-config

- No code for a mechanism the config declares `none` or leaves absent.
- Never touch `libs/` — a hard legality line (an FTC-illegal Robot Controller app), not a style
  preference.
- Mark generated files' origin: a short header comment noting this suite generated the file (the
  same lineage marker ftc-team-config writes as `_meta.suite_generated_code: true` in
  `team-config.yaml`), so a future corpus-mining pass never mistakes this suite's own output for
  independent confirmation of its own recommendations.

### 5. Mandatory verification — no exceptions, run before declaring anything done

Every generation ends here, unconditionally, whether the code "looks right" or not:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/config_lint.py <code_dir> --config <team-config.yaml>
python3 ${CLAUDE_PLUGIN_ROOT}/skills/ftc-code-review/scripts/failure_mode_lint.py <repo_path>
```

Then re-verify legality against anything the generated code touches that has a rules dimension
(mechanism restrictions, size/expansion limits if relevant) through ftc-rule-check's own
citation-grounded flow (`rules.py lookup` + `rules.py verify`) — a config being *confirmed* is not
the same claim as a mechanism being *legal*, and this skill does not substitute one for the other.

Report the **combined** result — "code written and verified against rules and known failure
patterns," with the actual linter and citation output attached — never just "code written." If
either linter reports a finding, or a rule-check verdict comes back `illegal` or `ambiguous`,
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
