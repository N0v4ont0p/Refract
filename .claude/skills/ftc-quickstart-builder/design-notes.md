# ftc-quickstart-builder — design notes (Phase 9 intent; build deferred to §16)

> The QuickStart repo build is **§16**, out of scope for Session 1. This file
> records the design intent so it is not lost when §16 runs.

## The starter template's defaults must ACTIVELY COUNTER the failure taxonomy

Not merely "avoid contradicting" `known-failure-modes.md` — the defaults should
structurally prevent its highest-leverage failure modes:

- **Telemetry scaffolding ON by default, not opt-in.** Directly counters
  Measurement / "No telemetry" — the mode that makes every other fault
  undiagnosable. A rookie forking the template should get telemetry for free.
- **Engineering-notebook-style documentation scaffolding** (README, design-decision
  log, meaningful commit conventions). Counters Process / "No engineering-notebook
  discipline" and the compounding knowledge-loss-on-graduation chain.
- **Interface-based architecture (PLAN §10, dynamic interface generation) prevents
  the God-OpMode / silo pattern BY CONSTRUCTION** — state this as a *deliberate
  consequence*, not a side effect. A team building on `Drivetrain` + per-mechanism
  interfaces cannot easily produce a 696-line do-everything TeleOp (the exact
  pattern `failure_mode_lint.py` flags on rookie repos).

## Cross-references
- Deterministic detector of these modes in existing repos:
  `../ftc-code-review/scripts/failure_mode_lint.py`.
- Canonical taxonomy: repo-root `known-failure-modes.md`.
- The God-OpMode mode is named independently by the SystemCore comparison material
  and by the taxonomy — cite both when justifying the interface-first default.
