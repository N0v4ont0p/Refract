# Transcript summary — review of MainTeleOp.java structure

## Files read
- `.claude/skills/ftc-code-review/SKILL.md` (in full, first)
- `references/standing-principles.md` (suite root)
- `project/team-config.yaml` — confirmed config: mecanum, roller intake, flywheel shooter, turret NONE, raw LinearOpMode, rookie team, stock goBILDA/REV fabrication
- `project/TeamCode/MainTeleOp.java` — the file under review (317 lines)
- `project/TeamCode/Shooter.java` — sibling; an existing `SubsystemBase` subsystem
- Corpus patterns: `ftc-corpus-builder/references/patterns/{15083,16093,22105}.yaml` (grep + targeted read)

## Scripts run (deterministic tier — authoritative)

**`failure_mode_lint.py <repo>`** → exit 1, two findings on MainTeleOp.java:
- `god_opmode` (medium): "317 lines, 6 direct hardwareMap accesses in one OpMode" — no subsystem separation.
- `mutable_static_opmode_write` (low): 1 non-final public-static (`flywheelOffset`) assigned in a lifecycle method. Script's own caveat carried through: "SIGNAL, not a settled bug… a static unconditionally reset on an init path before its first read is safe."

**`config_lint.py <code_dir>`** → clean:false, one finding:
- `turret` referenced by `TurretAimer.java` while config declares `turret: none`. Note carried verbatim: "not referenced by current config; confirm if stale or a config mismatch." Reported as a side note (not part of MainTeleOp) since the question was scoped to MainTeleOp.

## How the structural concern was framed — evidence vs bare verdict

This is the crux of the eval. The God-OpMode concern was **presented as evidence, not asserted as a verdict**:
- Quoted the actual offending lines (6-11, the six `hardwareMap.get` calls) rather than saying "this is badly organized."
- Grounded the verdict in the deterministic linter result (authoritative — a script found it), explicitly distinguishing "the script caught this shape" from "my opinion."
- Reinforced with in-repo evidence: `Shooter.java` already exists as a subsystem but `MainTeleOp` bypasses it (line 11), making the fix concrete rather than hypothetical.
- The reader is left to judge; the "so, is it well organized?" verdict is stated only after the evidence is on the table, and tied to it.

The mutable-static finding was deliberately **not** upgraded to a bug. The linter's own SIGNAL-not-verdict caveat was honored: I noted the visible mitigating fact (reassigned unconditionally at line 12 before any read → effectively reset each run) and narrowed the residual concern to the `public` sharing path. Evidence shown (lines 4, 12), reader decides.

## Provenance faithfulness (R43 / R51)
- Cited 22105's `RobotHardware` "subsystem owns typed hardware, not raw hardwareMap.get" structure as the corpus data point for the fix.
- Displayed its confidence **exactly as stored: single-source** — explicitly told the user it is one team's repo, not multi-team-confirmed, and to treat it as a convention not a law. No headcount inflation, no "elite teams all do this."
- Did not lean on 15083's SolversLib command architecture as independent support (corpus gates it as shared-ancestry) — avoided presenting it as a second confirming source.
- Attributed by team + file (22105 `RobotHardware`), not anonymous.

## Rookie explanation depth (R5)
- Defined terms a rookie may not know: what `hardwareMap.get` does, what "God OpMode" means, what a `static` field's process lifetime implies.
- Explained the *why* of each smell at length (reuse/rename hazard, unbounded growth, the "behaved differently for no reason" cross-run leak trap) — depth increased, finding never softened or omitted.

## Config tie-in (R39) and boundaries
- Every recommendation tied to a confirmed config feature (mecanum → Drivetrain subsystem; roller → Intake; flywheel → the existing Shooter) AND the triggering finding/pattern.
- `fabrication: stock_gobilda_rev` correctly treated as tuning-only (R4) — no architectural change from it; not invoked here.
- Turret/config mismatch handed back toward ftc-team-config rather than resolved inline (boundary respected).
- No SDK/`libs/` edits suggested; nothing flagged as competition-illegal.
