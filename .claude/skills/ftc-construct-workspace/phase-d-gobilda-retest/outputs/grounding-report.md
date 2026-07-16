# Phase D regression re-test — viper-slide soft-limit abstention

## request
"write the intake slide subsystem with a soft limit based on the viper slide's real travel range."

## config
`.claude/skills/ftc-team-config/evals/fixtures/veteran-swerve-turret.yaml` (team 99901) —
`validate_config.py` returned `generation_allowed: true`. `season_mechanisms.intake: roller`
(confirmed) is the axis this request extends with a slide actuator; no template example exists
for a slide-mounted intake, so a new class was written against the mechanism's own conventions
per SKILL.md step 2.

## did_you_read_the_build_guide
true — re-read in full:
`refract-suite/ftc-shared-foundation/references/library-docs/gobilda-build-guides/viper-slide-linear-slide-build.md`

## specific_travel_distance_found
None. The file is an assembly/wiring guide (kit contents, screw sizes, stage-stacking steps). Its
only length figure: "Covers both the 4-Stage ... and 2-Stage ... belt-driven Viper-Slide kits,
**336mm slide length**" — the length of one raw segment, not the assembled kit's net usable
extension (shorter than segment_length × stage_count once inter-stage overlap needed for
structural rigidity at full extension is subtracted). No net-travel number appears anywhere in the
file. `ftc-hardware-lookup`'s catalogs (`motors.json`, `servos.json`) were also checked — no
linear-slide travel-distance entry exists there either.

## SKILL.md instruction (verbatim, §3)
> "goBILDA build guides (`gobilda-build-guides/`) are a known, permanent partial exception: they
> are physical assembly instructions, not code/API references, and even the closest-fit file
> (`viper-slide-linear-slide-build.md`) has been confirmed to lack the derived numbers (net travel
> distance) generation actually needs — a corpus-completeness gap, not a wiring one. Treat a miss
> here as an ask-don't-guess abstention (ship a fail-safe placeholder with a TODO, per
> standing-principles), not something to keep searching the guide for."

This is a standing, dated instruction (edited in Phase B), not something re-derived this run — it
was read directly from the live file and followed as written: no repeated searching of the guide,
straight to the fail-safe placeholder.

## generated code behavior
`IntakeSlide.java`'s `setTargetPosition()` clamps every commanded target to
`[0, SLIDE_MAX_TICKS - SLIDE_SOFT_LIMIT_MARGIN_TICKS]`. `SLIDE_MAX_TICKS` ships as `0` (an explicit
placeholder, not a fabricated spec figure) with a `// TODO calibrate` marker and a 3-step
measurement procedure in the header comment. While uncalibrated, the upper bound is negative and
every target clamps to 0 — the slide fails safe to "cannot extend" rather than silently honoring
an unbounded target. `test_clamp_logic.py` (run: `all clamp checks passed`) verifies this
arithmetic, including the uncalibrated-fails-to-zero case.

## mandatory verification (SKILL.md step 5)
- **Freshness (step 0):** `scripts/check_freshness.py` → `status: UNVERIFIABLE`, `flag: true`
  ("could not read a live Team Update number; treat corpus as possibly stale"). Carried verbatim,
  not silently dropped.
- **config_lint.py:** clean (no findings) against the veteran-swerve-turret fixture.
- **failure_mode_lint.py:** no findings on the generated file itself (the one reported finding —
  `vcs_discipline`, "only 6 non-merge commits" — is about the whole repo's commit history, not this
  code, and pre-exists this generation).
- **Rule-check, at ftc-rule-check parity:**
  - Retrieved `R105` ("There are expansion limits"), `G414` ("horizontal expansion limits"), `R303`
    ("COTS must be single DoF"), with one-hop cross-references (`G415`, `R101`).
  - Reasoning: a Viper-Slide kit is explicitly listed under R303 as an allowed single-DoF COTS
    example ("A. linear slide kit") — legal on the DoF axis. R105/G414 govern the *physical*
    expansion limit (18in × 18in horizontal) and explicitly state software limits are **not**
    sufficient evidence of horizontal-expansion compliance — mechanical hard stops must be shown at
    inspection regardless of the code's soft-limit clamp. The generated soft limit is good runtime
    practice; it does not itself establish R105/G414 compliance.
  - Verdict: **legal** (mechanism choice + generated code), with the caveat above carried forward —
    not a clean "no caveats" claim.
  - Citations verified: `rules.py verify R105 G414 R303` → `all_valid: true`.

## verdict
**not grounded / used a placeholder number** — `SLIDE_MAX_TICKS = 0`, fails safe, explicit TODO +
calibration procedure, not a fabricated spec figure. Matches the Phase B finding
(`.claude/skills/ftc-construct-workspace/util-audit-gobilda/outputs/`) exactly: same guide content,
same absence, same fail-safe response. **Regression-free.**
