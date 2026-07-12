# Transcript summary — eval-1 oblique in-catalog spec (with_skill)

## Files read (full paths)
- `/Users/georgehu/Desktop/FTC Training AI/.claude/skills/ftc-hardware-lookup/SKILL.md` — read in full first, per instructions.

No other reference files were opened directly; the catalog values were surfaced through the script (which reads `references/catalogs/motors.json` internally).

## Scripts/commands run (with key output)

All run from cwd `/Users/georgehu/Desktop/FTC Training AI/.claude/skills/ftc-hardware-lookup`.

1. `python3 scripts/motor_math.py spec 5203-2402-0019` — exit 0
   - Key output: `no_load_rpm_output: 312`, `encoder_cpr_output: 537.7`, `gear_ratio_label: "19.2:1"`, `motor_base: RS-555`, stall torque 24.3 kg.cm / 338 oz-in, stall current 9.2 A.
   - Encoder note from catalog: published at OUTPUT shaft, reflects exact 19.20 ratio; do NOT recompute from rounded 19.2 label (537.7/28 = 19.20 exact).
   - Source: goBILDA product page, tier 1, retrieved 2026-07-05.

2. `python3 scripts/motor_math.py ticks 5203-2402-0019 --wheel-mm 96` — exit 0
   - Key output: `ticks_per_meter: 1782.87`, `ticks_per_wheel_rev: 537.7`, `cpr_source: encoder_cpr_output (published at output shaft)`.

3. `python3 scripts/motor_math.py wheel-speed 5203-2402-0019 --wheel-mm 96` — exit 0
   - Key output: `free_wheel_speed_m_s: 1.568`, `free_wheel_speed_ft_s: 5.145`, assumptions: output_rpm 312.0, wheel 96mm, external_ratio 1.0, note that this is FREE (no-load) speed.

## Provenance of every number I gave the user

| Number given | Source | From memory? |
|---|---|---|
| Free speed 312 RPM | `spec` script output (`no_load_rpm_output`) | No |
| Encoder resolution 537.7 CPR | `spec` script output (`encoder_cpr_output`) | No |
| "don't recompute as 28 × 19.2 / true ratio 19.20" caveat | catalog `encoder_cpr_output_note` via `spec` script + SKILL.md guidance | No |
| 537.7 ticks per wheel rev (direct drive) | `ticks` script output (`ticks_per_wheel_rev`) | No |
| 1782.87 ticks per meter | `ticks` script output (`ticks_per_meter`) | No |
| ~1.57 m/s (5.15 ft/s) free linear speed | `wheel-speed` script output | No |
| Circumference ~301.6 mm (explanatory) | Arithmetic I noted for explanation only (π × 96mm); the load-bearing tick figure came from the script, not this hand-calc | Hand-arithmetic, illustrative only |
| external-ratio / wheel-size caveats | SKILL.md §2 (wheel diameter is a config input; pass external ratio) + script assumptions block | No |
| Source URL + tier 1 + retrieved date | `spec`/`ticks`/`wheel-speed` script `source` block | No |

No hardware value was recalled or estimated from memory. Every spec and computed number traces to a script invocation whose output is quoted above.
