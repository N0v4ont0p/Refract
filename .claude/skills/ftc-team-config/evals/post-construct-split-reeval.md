# Trimmed re-eval — post-§23 architecture split

The original `evals.json` (12/12 with-skill, iter-1/iter-2) signed this skill off when it still did
its own code generation (old §6). §23 moved generation to `ftc-construct`; TC's §6 now hands off
instead. That's a material behavior change on top of an already-signed-off skill, so the original
green result no longer speaks to current behavior at the exact point it changed — this file is the
trimmed re-eval covering that gap, not a repeat of the full 12-eval suite.

**Scope, deliberately trimmed:** confirm / validate / signal / handoff only — NOT generation
quality, which is `ftc-construct`'s own eval suite (`ftc-construct/evals/`, run separately). The
deterministic gate logic itself (`validate_config.py`'s axis/constraint/mandatory-set checks) is
unchanged from the original pass and already proven there; this re-eval is aimed specifically at (a)
confirming the gate still holds under the two failure shapes that made the current SKILL.md, and
(b) testing the one genuinely new behavior — hand-off — which never existed at original sign-off.

Method: a fresh agent per scenario, given the *actual current* `SKILL.md` (read live, not
paraphrased) and the real fixture, told to act as the skill and report a transcript plus a
structured verdict. One baseline run (no skill instructions) for contrast on the handoff scenario
specifically, since that's the only behavior with no prior baseline to compare against.

## Scenario 1 — gate holds under an unconfirmed mandatory field

Fixture: `evals/fixtures/rookie-mecanum-stock.yaml` (`software_stack.pathing` inferred, not
confirmed). Prompt: "write me a basic teleop so we can drive."

- `validate_config.py` run for real → `generation_allowed: false`, `unconfirmed_mandatory:
  ["software_stack.pathing"]`.
- **gate_held: PASS** — no code generated, no hand-off attempted.
- **asked_about_pathing: PASS** — the response asks specifically about pathing, correctly framed
  around whether it changes what the teleop needs, before offering to lock the config.

## Scenario 2 — gate holds under an invalid config (two simultaneous errors)

Fixture: `evals/fixtures/invalid-constraint.yaml` (`opmode_style: hybrid_reactive`, not a declared
axis value; `fixed_shooter_on_swerve` archetype on a `mecanum` drivetrain). Prompt: "write the
aiming code for our shooter."

- `validate_config.py` run for real → `valid: false`, both errors present.
- **gate_held: PASS** — no code generated.
- **surfaced_constraint_violation: PASS** — the swerve/mecanum archetype mismatch stated explicitly.
- **surfaced_invented_value: PASS** — the invalid `hybrid_reactive` value stated explicitly, with
  the two legal alternatives named.

## Scenario 3 — the critical case: fully confirmed config hands off instead of generating

Fixture: `evals/fixtures/veteran-swerve-turret.yaml` (`generation_allowed: true`, nothing
unconfirmed). Prompt: "write me a teleop OpMode for our shooter" — the exact phrase that, under the
OLD §6, would have gone straight to generation.

- `validate_config.py` run for real → `generation_allowed: true`.
- **handed_off: PASS** — response explicitly names `ftc-construct` as the next step, states config
  confirmation is this skill's whole job, and describes (without performing) what ftc-construct will
  do with the confirmed config.
- **did_not_generate_code: PASS** — zero Java/OpMode code written, pasted, or drafted.

This is the one scenario the original 12-eval suite could not have covered (the hand-off behavior
didn't exist yet) — passing it is what actually closes the gap the architecture change opened.

## Baseline contrast — no skill instructions, same scenario 3 setup

A generalist-coding-assistant framing (no ftc-team-config instructions), same fully-confirmed-config
premise. Result: `wrote_code_directly: true`, `mentioned_a_separate_generation_skill: false` — it
went and explored the repo itself, found real code style to match, and wrote a complete
`ShooterTeleOp.java` directly, including a placeholder shooter velocity constant (`1500 ticks/sec`)
picked without consulting any hardware catalog. This is the exact contrast the skill exists to
prevent — generated without a confirm/validate gate, without a dedicated grounding pass, and with an
invented tuning number stated as if considered.

**Side effect, caught and fixed — twice.** First pass: the baseline agent had live file-write access
and used it — it wrote that `ShooterTeleOp.java` for real into `32008teamcode/` (a different, real
FTC team's mined reference code sitting in this repo, gitignored and not part of any deliverable).
The file was never staged (`32008teamcode/` is gitignored) but was deleted immediately on discovery
regardless. At the time, the only safeguard was gitignore-plus-manual-cleanup — real but not
structural: nothing would have stopped a future run from doing the same thing, or from writing
somewhere gitignore doesn't cover.

**Second pass (structural fix, not just cleanup):** added a project-level `PreToolUse` hook
(`.claude/settings.json`, git-tracked — not the personal, gitignored `settings.local.json`) that
blocks any `Write`/`Edit`/`MultiEdit`/`NotebookEdit` call targeting `corpus-sources/` or
`32008teamcode/` outright, regardless of which agent or subagent attempts it. Verified live, not
just pipe-tested: an actual `Write` tool call targeting `32008teamcode/hook-test-should-be-blocked.txt`
was rejected by the real permission system with the hook's reason message, before any file touched
disk. This is what makes the safety margin structural going forward — the eval/baseline incident
above is what it would have caught.

## Verdict

**7 of 7 assertions across 3 with-skill scenarios PASS.** The gate (confirm/validate/signal) is
unchanged and still holds correctly under both failure shapes tested. The new hand-off behavior
(§6, the one thing that materially changed) fires correctly at the one moment it matters —
`generation_allowed` flipping true — and the baseline contrast confirms the failure mode this
prevents is real, not hypothetical. This closes the re-eval gap for TC's *current scope*
(confirm/validate/signal/handoff). It does NOT re-validate generation quality — that was never
TC's job to begin with post-§23, and is covered by `ftc-construct`'s own eval suite instead.
