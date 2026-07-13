# ftc-construct — generation-quality eval (with-skill vs. baseline)

Same bar as the original four skills' eval passes: real agent runs with real tool access, against
real fixtures, graded on explicit assertions — not self-report. 3 with-skill scenarios plus 1
baseline contrast (reused from the TC re-eval, since it already exercised the exact same fixture and
request this suite's baseline would have used — no need to burn a second run to re-prove the same
point).

Outputs live under `.claude/skills/ftc-construct-workspace/eval-N-*/outputs/` — fixtures under
`.claude/skills/ftc-construct/evals/fixtures/` (one new: `rookie-intake-only-confirmed.yaml`, plus
the two existing ftc-team-config fixtures reused where they already fit).

## Eval 1 — shooter generation, grounded (`eval-1-shooter-grounded`)

Fixture: `ftc-team-config/evals/fixtures/veteran-swerve-turret.yaml` (confirmed, flywheel shooter).
Prompt: "write me a teleop OpMode for our shooter."

- `scaffolded_from_template`: **PASS** — adapted the template's `Shooter`/`FlywheelShooter` directly
  (config's `shooter: flywheel` matches the template's existing example); did NOT write a from-scratch
  design.
- `cited_real_library_doc`: **PASS** — `ftclib/hardware-wrappers/motors.md` (Motor/VelocityControl)
  and `ftclib/command-framework/binding-commands-to-triggers.md` (GamepadEx bindings), read before
  writing the corresponding API calls.
- Correctly excluded turret/intake/swerve-drivetrain code (request named only the shooter; swerve
  has no template example, and writing one ungrounded would have violated the same discipline).
- Checked the corpus (9 pattern files) for applicable shooter patterns — none cited, correctly:
  every flywheel-adjacent pattern's `applicable_when` needs a config field this fixture doesn't
  confirm (shoot-on-the-move, empirical aiming). Abstention, not an oversight.
- `ran_mandatory_verification` / `reported_combined_result`: **PASS** — `config_lint.py` clean,
  `failure_mode_lint.py` clean against generated files (findings only against pre-existing
  third-party corpus material, correctly not conflated), `rules.py lookup/verify G416` (launch-zone
  rule) resolved not-implicated. Final summary stated the combined result, not just "code written."

## Eval 2 — no code for undeclared mechanisms (`eval-2-no-undeclared-mechanisms`)

Fixture: **new**, `ftc-construct/evals/fixtures/rookie-intake-only-confirmed.yaml` (confirmed,
roller intake, shooter: none, turret: none, `raw_linear_opmode`). Prompt: "write us the intake
control code."

- `only_intake_code_written`: **PASS**, independently re-checked (`grep -rli "shooter\|turret"` on
  the output directory returns nothing).
- **Real subtlety caught, beyond the eval's original narrow scope:** the template's example
  (`RollerIntake`) is written against FTCLib's command framework, but this fixture's
  `software_stack.opmode_style` is `raw_linear_opmode` — a straight copy would have been WRONG for
  this config. The run detected the mismatch (via `extract_feature_vector.py`'s own style-detection
  logic), kept the library-agnostic `Intake` interface, and rewrote `RollerIntake` + a new
  `IntakeTeleOp` against the raw FTC SDK instead, grounded in `ftc-sdk/opmode-basics.md`. This is
  exactly the config-aware grounding the skill is supposed to do, demonstrated on a case the eval
  wasn't explicitly designed to force.
- `ran_mandatory_verification` / `reported_combined_result`: **PASS** — `config_lint.py`
  `{"declared_absent": [...], "findings": [], "clean": true}`; `failure_mode_lint.py` clean on the
  generated code (one `vcs_discipline` hit is a repo-wide git-history metric, correctly separated
  from a finding against the generated files).

## Eval 3 — hardware values grounded, not invented (`eval-3-hardware-grounded`)

Fixture: `ftc-team-config/evals/fixtures/veteran-swerve-turret.yaml`. Prompt named an UNSEEDED SKU
(`5203-2402-0001`, a 1:1 direct-drive variant) on purpose, to test the abstain-over-guess path
specifically — mirroring the exact failure the baseline (below) actually committed.

- `read_real_catalog_data`: **PASS** — ran `motor_math.py spec/ticks/external` for real; all three
  correctly abstained (exit 3) since the SKU isn't in the seeded catalog, independently re-verified
  (`grep -n "NaN|TODO|abstain"` on the output file shows the real abstention markers, not a
  self-report claim).
- `no_invented_numbers`: **PASS** — `NO_LOAD_RPM_OUTPUT`/`MAX_VELOCITY_TICKS_PER_SEC` are
  `Double.NaN` with a fail-fast `init()` guard and a doc comment quoting the script's actual
  abstain reason, plus the concrete unblocking step (seed the datasheet, re-run the script, wire in
  the result — not hand-type a guess). No number is reported to the user because none exists yet.

## Baseline contrast (reused from the TC re-eval, same premise: fully-confirmed config, "write me a
teleop OpMode for our shooter")

No skill instructions, generalist framing. Result: wrote a complete `ShooterTeleOp.java` directly
into the repo (see TC re-eval report for the full incident writeup — the file landed in a stray
location and was deleted on discovery), using a **placeholder shooter velocity of "1500 ticks/sec"
picked with no catalog lookup at all** — the exact failure eval 3 above was designed to force and
confirm ftc-construct avoids. No mandatory verification step, no mention of a dedicated generation
skill, no distinction between a real spec and a plausible-sounding guess.

## Verdict

**3/3 with-skill scenarios pass their assertions**, independently re-verified (not taken on
self-report alone) via direct `grep` checks on the generated files. The baseline contrast — same
premise, same request — confirms the specific failure mode this skill exists to prevent
(ungrounded generation, no verification, an invented tuning constant) is real and current, not
hypothetical. This closes the eval gap noted in TRACEABILITY.md's original ftc-construct row: the
skill has now been eval-suited at the same bar as the original four (real fixtures, real scripts,
real generated code, graded assertions, baseline contrast), not just boundary/routing-tested.

**Scope note:** 3 scenarios is trimmed relative to the original four skills' larger eval counts
(HW: 4 break-it evals; RC: 6; TC: 12 with-skill runs) — chosen to cover the three highest-leverage
generation-quality dimensions (template fidelity + config-aware adaptation, mechanism-exclusion
discipline, hardware-value grounding) rather than exhaustively. A future pass could extend to
turret/drivetrain generation and a config with an ftc-hardware-lookup catalog HIT (to confirm the
positive path, not just the abstain path) for fuller coverage.
