# Transcript summary — eval-3 (constraint violation surfaced), with_skill

## Files read
- `.claude/skills/ftc-team-config/SKILL.md` (in full, first)
- `references/standing-principles.md` (suite root — deterministic-first, abstention, source-tiering, ask-don't-guess)
- `core-feature-model.yaml` (suite root — legal axis vocabulary; drivetrain.type, software_stack mandatory)
- `season-extensions/ACTIVE` → `season-extensions/decode-2025-26.yaml` (season mechanisms, known_archetypes, `constraints_on_core`: `fixed_shooter_on_swerve` requires `core.drivetrain.type: swerve`)
- `.claude/skills/ftc-team-config/scripts/validate_config.py` (read to understand the expected team-config schema)
- Workdir listing: empty — no existing team-config.yaml, no team repo code.

## Scripts/commands run and key output
1. `python3 .claude/skills/ftc-corpus-builder/scripts/extract_feature_vector.py <workdir>` — everything `unknown` (workdir is empty; nothing inferable). Confirms all mandatory fields must come from the user.
2. `python3 .claude/skills/ftc-team-config/scripts/validate_config.py <workdir>/team-config.yaml` — exit 1:
   - errors: `constraint violated: archetype 'fixed_shooter_on_swerve' requires core.drivetrain.type='swerve', config has 'mecanum'`
   - unconfirmed_mandatory: `drivetrain.type`, `software_stack.pathing`, `software_stack.opmode_style (missing)`, `season_mechanisms (none recorded)`
   - `valid: false`, `generation_allowed: false` (full output in `outputs/validation-output.json`)
3. `python3 .claude/skills/ftc-team-config/scripts/question_order.py` — top-ranked residual question is `software_stack.opmode_style` (15/61 patterns branch on it), used to order the follow-up questions in the user message.

## How the archetype/drivetrain conflict was handled
- The user's request is internally contradictory: `fixed_shooter_on_swerve` archetype + "we run mecanum". The season extension's `constraints_on_core` makes this a hard entry-time error, and the skill says a physically incoherent config "should fail here, at entry, not surface later as generated code that can't work".
- I drafted `team-config.yaml` recording the user's stated values verbatim (mecanum, roadrunner, team 99903, requested archetype) with `source: asked, confirmed: false` on every field, and ran the deterministic validator so the rejection is the script's authoritative output, not my own reading of the YAML.
- The conflict was **surfaced to the user, not silently resolved in either direction**: I did not drop the archetype to fit mecanum, and I did not change the drivetrain to swerve to fit the archetype. The user message (outputs/interaction.md) explains why the constraint exists (the drivetrain itself provides aim in that archetype), presents three coherent resolutions (turreted_shooter on mecanum / fixed shooter on mecanum knowingly outside named archetypes / actually swerve), and asks which is true.
- Remaining mandatory questions (opmode_style, season mechanism set) were bundled into the same turn in empirical order; hub_generation was recorded as inferred per the time-gate (2025 season start → REV Control Hub is the sole legal option, zero information gain in asking).
- **Stopped there.** No confirmation was fabricated, nothing was flipped to `confirmed: true`, and no robot code was generated — `generation_allowed` is false and stays false until the user resolves the conflict and confirms the config.

## Outputs
- `outputs/team-config.yaml` — draft (also left in workdir), invalid by design pending user resolution
- `outputs/validation-output.json` — validator output (exit 1)
- `outputs/interaction.md` — verbatim user-facing message where the session stopped
- `outputs/transcript-summary.md` — this file
