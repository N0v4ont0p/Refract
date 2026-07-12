# Hub generation: REV Control Hub (current, FTC-legal)

> STATUS: **Reviewed & merged** (Phase 7, approved 2026-07-03).
> This is the settled, currently-shipping system. It is the **sole FTC-legal
> control system now through the 2026-27 season** (the SystemCore hybrid window
> opens 2027-28 — see `systemcore-motioncore.md`).

Every claim is tagged **[T1]** (tier-1: official FIRST manual / REV catalog) or
**[T2]** (tier-2: community/secondary), per Rule 7. `[cite: R###]` points at the
tagged rule in the rules corpus (`ftc-rule-check/references/rules/`).

## Role in the control system
- **[T1]** The ROBOT control system is built on the **REV Control Hub
  (REV-31-1595)** — the required primary controller, or an approved Android
  device connected to a REV Expansion Hub. `[cite: R701]`
- **[T1]** The **OPERATOR CONSOLE** uses a **REV Driver Hub (REV-31-1596)** or an
  approved Android device (per R704) with an OTG cable and gamepad(s). `[cite: R901]`
- **[T1]** Additional motor/servo ports come from the **REV Expansion Hub**,
  connected to the Control Hub. `[cite: R701, R614]`

## Power
- **[T1]** Exactly **one 12V NiMH main battery** is the only legal source of
  electrical energy for control and actuation, with a COTS in-line 20A ATM mini
  blade fuse; legal packs are enumerated in Table 12-4. `[cite: R601 → [[TABLE:12-4]]]`
- **[T1]** All power routed through **one main power switch** (Table 12-5). `[cite: R609 → [[TABLE:12-5]]]`
- **[T1]** Power-regulating devices (servo power modules/blocks, SPARKmini,
  Servo Hub) are enumerated and must be powered per Table 12-7. `[cite: R505, R614 → [[TABLE:12-7]]]`

## Actuators / sensors (legacy ecosystem)
- **[T1]** Legal motors are enumerated in **Table 12-1** (AndyMark NeveRest,
  goBILDA Yellow Jacket 520x / 5000 series, REV HD Hex / Core Hex, TETRIX, etc.).
  `[cite: R501 → [[TABLE:12-1]]]`
- This multi-vendor motor/servo/sensor ecosystem is exactly what the
  SystemCore/A301 transition replaces — noted here as the contrast baseline.

## SDK integrity (competition-legality constraint)
- **[T1]** Modifying or omitting a compiled library in the SDK's `libs/` folder
  makes the Robot Controller app competition-illegal. Any generated code must
  respect SDK integrity (§14.1). This carries forward regardless of hub generation.

## Facts deliberately NOT stated here
Internal SoC / RAM / flash specs of the Control Hub and Driver Hub are **not**
asserted in this file — they were not verified from a tier-1 source this session.
When needed, populate them from the **REV catalog as a §9 structured table**
(`ftc-hardware-lookup`), never from prose recall. (Operating rule 1 + §9: hardware
specs are lookup/arithmetic, never generated.)

## Onboarding / elicitation implication
Because REV Control Hub is the **only** legal option now through 2026-27, the
`control_hardware.hub_generation` axis has **zero information gain** at elicitation
time and must **not** be asked (§13 purposefulness). This is a *time-gated* rule,
not a permanent omission — see the design requirement in `systemcore-motioncore.md`
for when it flips.
