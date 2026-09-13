# Hub generation: REV Control Hub (current, FTC-legal)

> STATUS: **Reviewed & merged** (Phase 7, approved 2026-07-03).
> This is the settled, currently-shipping system. It is the **sole FTC-legal
> control system now through the 2026-27 season** (the SystemCore hybrid window
> opens 2027-28 — see `systemcore-motioncore.md`).

Every claim is tagged **[T1]** (tier-1: official FIRST manual / REV catalog) or
**[T2]** (tier-2: community/secondary), per Rule 7. **Rule numbers are season data** — the manual
renumbers every year — so each citation gives the rule's *headline* plus its number per season. Verify
before quoting: `rules.py lookup <ID> --season <slug>` (corpus: `ftc-rule-check/references/rules/<slug>/`).
Re-cited 2026-09-13 against BIOBUZZ V1 + TU00; DECODE numbers kept for anyone reading older answers.

| Claim | Rule headline | BIOBUZZ 2026-27 | DECODE 2025-26 |
|---|---|---|---|
| single ROBOT CONTROLLER: Control Hub, or smartphone + Expansion Hub; at most one additional Expansion Hub | "Control the ROBOT with a single ROBOT CONTROLLER" | R701 | R701 |
| OPERATOR CONSOLE uses a REV Driver Hub or an Android device | "Use only a specified DRIVER STATION device" | R901 | R901 |
| one 12V NiMH main battery, legal packs in the main-power table | BIOBUZZ "ROBOTS can contain only 1 main battery" / DECODE "Battery limit - everyone has the same main ROBOT power" | R601 → [[TABLE:12-4]] | R601 → [[TABLE:12-4]] |
| one main power switch, legal switches tabled | "Connect the ROBOT battery though the Main Power Switch" | R603 → [[TABLE:12-5]] | R609 → [[TABLE:12-5]] |
| power-regulating devices enumerated / powered per table | "All actuators must be controlled and powered through approved devices"; BIOBUZZ "All Power regulating devices must be connected and powered through approved ports" / DECODE "Energize Power Regulating Devices as specified" | R505 → [[TABLE:12-3]]; R608 → [[TABLE:12-7]] | R505 → [[TABLE:12-3]]; R614 → [[TABLE:12-7]] |
| legal motors tabled | BIOBUZZ "Only specific motors are allowed" / DECODE "Allowable motors" | R501 → [[TABLE:12-1]] (adds WATTOS Stingray) | R501 → [[TABLE:12-1]] |
| legal smartphone list | DECODE "Use only legal Android smartphone devices" | **no equivalent rule or table in BIOBUZZ V1** (DECODE Table 12-10 removed) | R704 → [[TABLE:12-10]] |

## Role in the control system
- **[T1]** The ROBOT control system is built on the **REV Control Hub
  (REV-31-1595)**, or a smartphone Android device connected to a **REV Expansion Hub
  (REV-31-1153)**; a ROBOT may add no more than one additional Expansion Hub. (single-controller rule, table above)
- **[T1]** The **OPERATOR CONSOLE** uses a **REV Driver Hub (REV-31-1596)** or an
  Android device, with USB/OTG for gamepads. (driver-station rule, table above)

## Power
- **[T1]** Exactly **one 12V NiMH main battery** is the only legal source of
  electrical energy for control and actuation, with a COTS in-line 20A ATM mini
  blade fuse; legal packs are enumerated in the main-power table. (main-battery rule)
- **[T1]** All battery power to power-regulating devices goes through **one main power switch**
  from the legal-switch table. (main-power-switch rule)
- **[T1]** Power-regulating devices (servo power modules, SPARKmini, Servo Hub, etc.) are
  enumerated and must be powered per the power-requirements table. (regulator rules)

## Actuators / sensors (legacy ecosystem)
- **[T1]** Legal motors are enumerated in the motor table (AndyMark NeveRest, goBILDA Yellow
  Jacket, REV HD Hex / Core Hex, TETRIX, etc.; BIOBUZZ adds the WATTOS Stingray). BIOBUZZ caps a
  ROBOT at 8 motors and 8 servos (R503; DECODE allowed 10 servos).
- This multi-vendor motor/servo/sensor ecosystem is exactly what the
  SystemCore/A301 transition replaces — noted here as the contrast baseline.

## SDK integrity (competition-legality constraint)
- **[project rule — PLAN §14.1, not manual text]** Modifying or omitting a compiled library in the
  SDK's `libs/` folder is treated as making the Robot Controller app competition-illegal, and
  generated code never does it. A search of both the DECODE and BIOBUZZ manual corpora (2026-09-13)
  found **no rule text** stating this, so it was previously mis-tagged [T1]. The nearest manual rule
  is "Only specified modifications to core control system devices are permitted" (BIOBUZZ R706),
  which covers the devices and DRIVER STATION software, not TeamCode's libraries. Keep the
  discipline; don't cite it as a manual rule.

## Facts deliberately NOT stated here
Internal SoC / RAM / flash specs of the Control Hub and Driver Hub are **not**
asserted in this file — they were not verified from a tier-1 source this session.
When needed, populate them from the **REV catalog as a §9 structured table**
(`ftc-hardware-lookup`), never from prose recall. (Operating rule 1 + §9: hardware
specs are lookup/arithmetic, never generated.)

## Onboarding / elicitation implication
Because REV Control Hub is the **only** legal option now through 2026-27 (BIOBUZZ R701 lists only REV
Control Hub / smartphone + Expansion Hub), the
`control_hardware.hub_generation` axis has **zero information gain** at elicitation
time and must **not** be asked (§13 purposefulness). This is a *time-gated* rule,
not a permanent omission — see the design requirement in `systemcore-motioncore.md`
for when it flips.
