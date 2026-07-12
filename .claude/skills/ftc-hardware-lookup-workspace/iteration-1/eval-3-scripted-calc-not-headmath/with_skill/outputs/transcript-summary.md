# Transcript summary — HD Hex + 20:1 spur

## Files read
- `.claude/skills/ftc-hardware-lookup/SKILL.md` — read in full first, per instructions.
- `references/catalogs/motors.json` — located the HD Hex Motor record; confirmed SKU `REV-41-1291`, base free speed 6000 RPM, published stall torque 0.105 N·m, motor-shaft encoder 28 CPR, and that a 20:1 spur gearbox is a listed option for this motor.

## Commands run (key output)
1. `grep -in "hd hex" references/catalogs/motors.json` → matched line 34, name "REV Robotics HD Hex Motor (bare, no gearbox)".
2. `python3 scripts/motor_math.py spec REV-41-1291` → returned full record + tier-1 source (REV docs). Confirmed base values.
3. `python3 scripts/motor_math.py external REV-41-1291 --ext 20` (exit 0) → key output:
   - `output_rpm_after_stage: 300.0`
   - `output_stall_torque_nm_ideal: 2.1`
   - `torque_note`: "ideal (no efficiency loss); base 0.105 N.m (published); real torque is lower — gearboxes/belts lose 10-30%"
   - `speed_note`: base output 6000 rpm ÷ external ratio 20.0

## Where the numbers came from
- **Output speed (300 RPM):** from the script (`external` command), not head-math.
- **Ideal stall/holding torque (2.1 N·m):** from the script (`external` command).
- **Realistic holding torque (1.5–1.9 N·m):** derived by applying the script's own stated 10–30% gearbox-loss caveat to the 2.1 N·m ideal (2.1 × 0.7 ≈ 1.47; 2.1 × 0.9 ≈ 1.89). This is a range explicitly flagged by the script's torque_note, not an invented spec.
- **Output encoder CPR (560):** 28 × 20, per the catalog's own note that output CPR = motor CPR × gearbox ratio for this bare motor. Flagged the script as the place to do tick math for closed-loop use.

No hardware value was recalled from memory. Base specs came from the catalog; all gear arithmetic came from `motor_math.py`. Source surfaced with the answer (tier 1, REV docs) per R68.
