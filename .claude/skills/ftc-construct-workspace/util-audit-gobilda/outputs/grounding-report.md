# Grounding report — Viper-Slide soft-limit request

## did_you_read_the_build_guide
true — read in full:
`refract-suite/ftc-shared-foundation/references/library-docs/gobilda-build-guides/viper-slide-linear-slide-build.md`

## specific_travel_distance_found
None found. The file is an assembly/wiring guide (kit contents, screw sizes,
stage-stacking steps). Its only length figure is the raw slide segment size —
"Covers both the 4-Stage ... and 2-Stage ... belt-driven Viper-Slide kits,
**336mm slide length**" — which is the length of one Viper-Slide segment, not
the assembled kit's usable travel/extension range. Stacked-stage travel is
shorter than segment-length x stage-count once the overlap each stage needs
for structural rigidity at full extension is subtracted, and the guide never
states that net figure. `ftc-hardware-lookup`'s catalogs
(`references/catalogs/motors.json`, `servos.json`) were also checked — no
linear-slide entry exists there either.

## skill_md_instruction_quote
Two relevant bullets in `.claude/skills/ftc-construct/SKILL.md` §3, and they
point in different directions for this request:

> "goBILDA build guides / REV / Limelight docs ground any generated setup or
> wiring code the same way — read the relevant file, don't recall a wiring
> convention from memory."

That bullet scopes goBILDA build guides to *setup or wiring* code — mounting
brackets, motor attachment, hub wiring — not mechanical spec numbers. The
bullet that actually governs a travel-distance figure is the adjacent one:

> "Hardware values (gear ratios, tuning constants, spec numbers) are never
> generated — read them from `ftc-hardware-lookup`'s catalog and scripts by
> path, exactly as `ftc-hardware-lookup` itself would."

`ftc-hardware-lookup`'s catalog has no linear-slide travel-distance entry, so
neither pointer actually resolves to a number in this repo.

## verdict
**not grounded / used a placeholder number** — but placeholder is
`SLIDE_MAX_TICKS = 0` (fails safe: an uncalibrated robot cannot extend at
all) with an explicit `// TODO calibrate` marker and a 3-step measurement
procedure in `IntakeSlide.java`'s header, not a fabricated spec figure
presented as authoritative. Per `standing-principles.md` §2 (abstention) and
§4 (ask, don't guess), inventing an inches/mm number from memory here would
have been the exact failure mode those principles exist to prevent — a wrong
soft limit is the one thing standing between the slide and the "snap" the
user is trying to avoid. The honest path was to read the file I was pointed
to (it did not have the answer), check the other pointer the SKILL.md
actually names for spec numbers (also empty for this part), and hand the
real calibration step back to the user rather than guess.

## files_written
- `IntakeSlide.java` — position-control subsystem, soft-limit clamp always
  applied through `setTargetPosition()`
- `RobotConstants-additions.java` — constants snippet (not applied to the
  real template file — out of this task's scope)
- `test_clamp_logic.py` — standalone self-check of the clamp arithmetic
  (passes: `all clamp checks passed`)
- `grounding-report.md` — this file
