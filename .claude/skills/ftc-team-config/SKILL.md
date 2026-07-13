---
name: ftc-team-config
description: 'Establishes, confirms, and maintains the team''s robot configuration (drivetrain, season mechanisms, sensors, software stack) that gates all FTC robot code generation. Use this skill BEFORE writing or modifying any robot code — whenever the user starts a build session, describes their robot, asks for a new subsystem or mechanism ("add an intake", "write auto-aim"), or mentions hardware changing mid-season — and whenever a code request arrives with no confirmed config in the session, even if the user never says the word "config". Also use when a request contradicts the recorded config (turret code for a no-turret robot). Infers from the repo/BOM first, asks only questions that change what gets built, and always confirms the config back before handing off to ftc-construct — this skill does not write code itself; once the config is confirmed, ftc-construct does the actual generation.'
---

# FTC Team Config

Robot code generated against a wrong assumption compiles, deploys, and fails at a match. This
skill exists so that never happens silently: it establishes a *confirmed* picture of the team's
robot before any hardware-specific code is written, and keeps that picture current as the robot
changes mid-season. Confirmed config generates code; unconfirmed config generates a question.

Read `references/standing-principles.md` at the suite root before acting — the deterministic-first,
abstention, source-tiering, and ask-don't-guess principles there apply to every step below. The
suite root is the directory containing `core-feature-model.yaml`; all paths below are relative to
it. Other skills' data is read directly by path (see the canonical path table in
standing-principles) — never by handing off mid-turn to another skill.

## Files this skill reads and writes

| File | Role |
|---|---|
| `core-feature-model.yaml` | season-invariant axes — the only legal vocabulary for config values |
| `season-extensions/ACTIVE` → `season-extensions/<slug>.yaml` | the current season's mechanism set and constraints |
| `team-config.yaml` (team's project root) | **written by this skill** — the confirmed config, with per-field provenance |
| `.claude/skills/ftc-corpus-builder/scripts/extract_feature_vector.py` | deterministic inference from the team's repo |
| `scripts/validate_config.py` (this skill) | deterministic validation: axis membership, season constraints, mandatory-set confirmation |
| `scripts/question_order.py` (this skill) | empirical question ordering from the pattern corpus |
| `.claude/skills/ftc-hardware-lookup/references/hub-generations/systemcore-motioncore.md` | the hub-generation briefing — read fresh at ask-time, never restated here |

## The flow

### 0. Check what already exists

If `team-config.yaml` exists in the team's project, read it first. Fields marked
`confirmed: true` stay settled — don't re-ask them (re-asking settled questions erodes the trust
that makes the necessary questions land). Fields that are missing, unconfirmed, or contradicted
by what the user just said are the working set.

### 1. Infer before asking

Run the deterministic extractor over the team's repo before asking a single question:

```bash
python3 .claude/skills/ftc-corpus-builder/scripts/extract_feature_vector.py <team-repo-path>
```

It detects imports, OpMode style, hardware-map declarations, and pathing libraries mechanically.
For artifacts a parser can't read (a BOM spreadsheet, CAD notes, a photo description), delegate a
first pass to a Haiku-tier subagent (cheap, read-only, "list what this artifact establishes about
the robot, nothing more"); escalate to Sonnet only if the artifact is genuinely ambiguous. Use
the pinned subagent definitions where one fits — never override their pinned models.

Everything inference produces is a **pre-fill, not a decision**: record it with
`source: inferred, confirmed: false`. Inference exists to make the question list short, not to
answer questions on the user's behalf.

### 2. Validate what you have

```bash
python3 <this-skill>/scripts/validate_config.py <team-config.yaml>
```

The script checks three things deterministically, and its output is authoritative over your own
reading of the YAML:

- every value comes from an axis actually declared in the core model or season extension — a
  config value the model invented is an error, not a creative solution;
- the season's `constraints_on_core` hold (e.g. the `fixed_shooter_on_swerve` archetype requires
  a swerve drivetrain — a physically incoherent config should fail here, at entry, not surface
  later as generated code that can't work);
- `generation_allowed` is true only when every mandatory field is present **and confirmed**.

### 3. Ask only what's left — in empirical order

Every question must earn its place: ask it only if the answer changes which patterns or
recommendations apply. The corpus makes this measurable — run:

```bash
python3 <this-skill>/scripts/question_order.py
```

It counts how many of the 60+ mined patterns branch on each feature. A feature 15 patterns key
off (`software_stack.opmode_style`, currently the top of the list) is worth a question; a feature
nothing branches on is not. Use the ranking as a soft order for the residual questions —
highest-information first, so if the user's patience runs out, the questions that mattered most
got asked.

**Three things are asked and confirmed regardless of inferability** — drivetrain topology, the
season's mechanism set, and the software stack — because they gate too much downstream to risk
acting on a guess, however good the guess looks.

**Hub generation is time-gated.** Read the season start year from the ACTIVE slug (e.g.
`decode-2025-26` → 2025). Through the 2026-27 season, the REV Control Hub is the sole legal
control system, so asking has zero information gain — don't ask, record it as inferred. From
2027-28 (the hybrid-legal window), `hub_generation` joins the mandatory set — but read
`.claude/skills/ftc-hardware-lookup/references/hub-generations/systemcore-motioncore.md` fresh and
give the user its briefing *before* asking, because "which control system?" asked cold invites an
uninformed answer to a decision that has real tradeoffs and no forced deadline. Never restate
that file's facts from memory — read it at ask-time; it carries its own source tiers.

### 4. Confirm back before anything generates

Once the config is filled (inferred + asked), state the complete picture back to the user in
plain terms — "mecanum on stock goBILDA 96mm, Pinpoint odometry, Pedro Pathing, raw LinearOpMode,
roller intake, no shooter, no turret" — and get an explicit yes. Only then flip the fields to
`confirmed: true`. Run `validate_config.py` once more; generation is allowed only when it reports
`generation_allowed: true`.

This is the line that governs the whole skill:

> "If a recommendation would differ depending on information you don't have, stop and ask before
> generating code. A wrong guess that compiles is worse than a question that costs one turn."

### 5. Persist

Write `team-config.yaml` to the team's project root. Schema:

```yaml
_meta: {schema: 1, updated: <date>, suite_generated_code: true}   # lineage marker — see below
team: {number: 19859, experience: veteran}
drivetrain:
  type: {value: mecanum, source: asked, confirmed: true}
software_stack:
  pathing: {value: pedro_pathing, source: inferred, confirmed: true}
season_mechanisms:
  intake: {value: roller, source: asked, confirmed: true}
config_history:
  - {date: <date>, change: "initial confirmation"}
```

`source` records how each value arrived (`inferred` vs `asked`); `config_history` appends — a
mechanism added in week 6 must not silently overwrite what was true in week 1, because "when did
the config change" is exactly the question that matters when behavior changes at the same time.

### 6. Hand off to ftc-construct

Once `generation_allowed` is true, this skill's job is done — it does not write the code itself.
Hand off to `ftc-construct`, which reads the just-confirmed `team-config.yaml` and does the actual
generation: scaffolding from the quickstart interface template, grounding API calls and tuning
values in the library docs and hardware catalog, and running a mandatory rule-check and
code-review verification pass before calling anything done. Codegen carries its own dedicated
grounding discipline there instead of being a paragraph bolted onto config confirmation.

Three structural rules that shape what `generation_allowed` actually authorizes, worth knowing
here too even though ftc-construct is the one that enforces them:

- **Interfaces are derived, not enumerated.** `Drivetrain` is the one always-present interface.
  Every other mechanism interface comes from the keys of the ACTIVE season extension's
  `season_mechanisms` block — one interface per declared mechanism the config actually selects.
  No hardcoded mechanism list anywhere: when the season changes, the interface set changes with
  the season file, not with a code edit.
- **No code for undeclared features.** A team with `turret: none` gets no turret code — not
  commented-out, not "just in case". Unused code a team didn't ask for is where stale bugs live.
- **Never touch `libs/`.** Modifying or omitting the SDK's compiled libraries makes the Robot
  Controller app competition-illegal — this is a hard legality line, not a style preference.
  Generated code integrates through TeamCode, full stop.

Mark generated files' origin honestly: this suite's output is quickstart lineage
(`_meta.suite_generated_code: true`). If a future pattern-mining pass encounters code this suite
generated, that marker is what stops the corpus from citing its own output as independent
confirmation of its own recommendations.

### 7. Keep the config live

A config is a snapshot; robots change weekly. When anything in the session contradicts the
recorded config — the user mentions a mechanism that isn't in it, the repo grows a subsystem the
config doesn't declare, a request assumes hardware the config says doesn't exist — stop and
re-open *that part* of the config before proceeding. Re-run validation, re-confirm the changed
fields, append to `config_history`. Working from a stale snapshot produces code for a robot that
no longer exists, and it fails in the way that's hardest to debug: correctly, for the wrong robot.

## What this skill does not do

Legality verdicts (ftc-rule-check's tagged manual), hardware specs and math
(ftc-hardware-lookup's tables and scripts), and code review (ftc-code-review) each have their own
skill — read their data by path when the config work needs it (e.g. resolving whether a declared
mechanism is season-legal), but route the user's *question* there only when it isn't a config
question at all. From-scratch robot design advice ("what should our first robot look like") is
explicitly out of scope for this suite's current pass — say so rather than improvising it.
