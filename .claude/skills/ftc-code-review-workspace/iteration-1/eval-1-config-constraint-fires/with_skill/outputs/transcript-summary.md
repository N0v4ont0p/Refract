# Transcript summary — eval-1-config-constraint-fires (with_skill)

## Files read (in order)
1. `.claude/skills/ftc-code-review/SKILL.md` — full, first, as instructed.
2. `core-feature-model.yaml` (suite root) — season-invariant feature schema.
3. `references/standing-principles.md` (suite root) — deterministic-first, ask-don't-guess, tiering.
4. `.../with_skill/project/team-config.yaml` — the confirmed config the review is *against*.
5. `.../project/TeamCode/TurretAimer.java` — 5-line turret class.
6. `.../project/TeamCode/Shooter.java` — extends SolversLib `SubsystemBase`.
7. `.../project/TeamCode/MainTeleOp.java` — 317-line raw `LinearOpMode`.
8. `.claude/skills/ftc-code-review/scripts/config_lint.py` — read to confirm arg handling (it had
   defaulted to a fixtures config via cwd rglob; re-ran with explicit `--config`).
9. Corpus: `ftc-corpus-builder/references/patterns/15083.yaml` + `cross-team-findings.yaml` — checked
   for a command-based/SolversLib pattern to cite provenance faithfully.

## Commands run

### `failure_mode_lint.py <project>`  (deterministic tier — authoritative)
Two findings + stats. Key output:
- `god_opmode` (medium): `MainTeleOp.java` 317 lines, 6 direct hardwareMap accesses in one OpMode.
- `mutable_static_opmode_write` (low): 1 non-final public-static (`flywheelOffset`) assigned in a
  lifecycle method. Linter labels it SIGNAL not bug — verify reset each run.
- Stats: telemetry signal found (no missing-telemetry finding); 0 commits (bus-factor/vcs empty);
  0 PID files.

### `config_lint.py <project>`  (deterministic tier — authoritative)
First run auto-discovered `evals/fixtures/sample-robot/team-config.yaml` (cwd rglob default). Re-ran
with `--config <project>/team-config.yaml` to review against the TEAM's actual config. Both runs gave
the same finding (the team config's declared_absent set matched the fixture's):
- `turret`: config declares `turret: none` but `TeamCode/TurretAimer.java` references it →
  "confirm if stale or a config mismatch." `clean: false`, exit 1.

## Which findings came from a script vs judgment

| Finding | Source |
|---|---|
| Turret code vs `turret: none` config (finding 1) | **Script** — `config_lint.py` |
| God OpMode, MainTeleOp 317 lines / 6 devices (finding 2) | **Script** — `failure_mode_lint.py` |
| `flywheelOffset` mutable static (finding 3) | **Script** — `failure_mode_lint.py` |
| `Shooter.java` command-based but orphaned / config says raw_linear_opmode (judgment section) | **Judgment** — my read of Shooter.java + MainTeleOp + config; provenance cited from corpus 15083-B verbatim (single-source / shared-ancestry / provenance-guard, not inflated) |
| Telemetry present, no SDK tampering, VCS stats empty | **Script** — `failure_mode_lint.py` stats |

## Skill-boundary decisions
- **Did NOT spawn the `full-review` Opus-xhigh subagent** (SKILL §4). Whole codebase is 3 trivial files
  already fully read line-by-line; the isolated-context cost buys nothing here. Noted in answer.
- **Did NOT edit the config** despite the turret/Shooter mismatch — SKILL says review *against* config,
  hand back to `ftc-team-config` if config is wrong. Flagged for user confirmation instead.
- **experience: rookie** → expanded the *why* on the God-OpMode and static findings (R5), did not soften
  or drop any finding.
- **fabrication: stock_gobilda_rev** → no tuning-value advice was gated on it; didn't change any finding.
- Corpus provenance displayed exactly as stored (R43/R51): 15083-B is single-source, shared-ancestry, a
  provenance guard — presented as "one team on a shared library," not as endorsement.
