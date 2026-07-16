# Device naming/addressing convention for a second REV Expansion Hub

## Source read (before writing any code)
`refract-suite/ftc-shared-foundation/references/library-docs/rev-robotics/device-configuration-and-expansion-hub.md`
(fetched 2026-07-12 from docs.revrobotics.com/duo-control/menu/configuring-devices)

## The claim

**hardwareMap addressing does not change when you add a second Expansion Hub.**
Every device — regardless of which physical hub (Control Hub or either Expansion
Hub) it's wired to — is looked up in `hardwareMap` purely by the unique,
case-sensitive **name string** assigned to it in the Driver Station configuration
file. There is no hub-number prefix, no `hub2.` namespace, and no separate
`hardwareMap` per hub in the SDK. The only thing that is hub-specific is the
**RS485 communication address** of the hub itself (a hardware-config concern, not
a `hardwareMap.get()` concern), and that only needs attention in the two-hub-on-one-Android-RC
edge case the doc calls out.

## Exact citation

File: `device-configuration-and-expansion-hub.md`

> "The configuration file is created through the Driver Station app. For each
> connected device you assign: a port, a device type (from a list the SDK
> provides), and a **unique, case-sensitive** name. Saving/activating a
> configuration restarts the Robot Controller so the SDK can read the file and
> populate `hardwareMap` with the named devices." (line 9)

> "**Expansion Hub:** each Expansion Hub's configuration is unique to it —
> recreate the config if you swap in a different physical Expansion Hub. In a
> new configuration, select the Control Hub Portal; an RS485-connected Expansion
> Hub appears as a separate portal within it. Configure its devices the same way
> as above; the menu header indicates whether you're in the Expansion Hub's or
> Control Hub's port list." (line 33)

> "...you'll now see both the Control Hub and the Expansion Hub (labeled e.g.
> "Expansion Hub 2") as configurable targets → configure/program as needed. If
> the Robot Controller is an Android device with two Expansion Hubs present,
> their RS485 addresses may need to be changed so they don't conflict." (line 72)

Together these lines establish: (1) the name is what populates `hardwareMap`,
per-device, independent of hub (line 9); (2) the second hub is only distinguished
in the *configuration UI* as a separate portal/target, not via any device-name
scheme (line 33); (3) the only hub-level "address" concept the doc documents is
the RS485 address of the hub itself, needed only to disambiguate two physical
Expansion Hub units on the same RC, not a per-device naming convention (line 72).

## What the doc does NOT say

The doc does not prescribe any specific device-naming pattern (no
"deviceName_2", no hub-index prefix, nothing REV-mandated) for devices on a
second hub. The `_hub2` suffix used in `SecondExpansionHubHardware.java` is a
team-readability convention this generation adopted, not a documented
REV/FTC-SDK requirement — that distinction is called out explicitly in the code
comments so it isn't mistaken for an SDK rule.

## Verdict inputs (for the audit report)

- specific_claim_made: "hardwareMap.get() addresses devices by their configured
  name string only; hub identity is not part of the lookup or any SDK-mandated
  naming scheme — the second hub is distinguished only in the DS config UI as a
  separate portal, and the only hub-level 'address' is the RS485 address."
- citation: verbatim lines 9, 33, 72 of
  `device-configuration-and-expansion-hub.md` (quoted above).
- verdict: genuinely grounded — the claim traces to specific quoted lines in the
  fetched REV doc, and where the doc is silent (a device-naming *pattern* for
  the second hub), that silence is stated explicitly rather than papered over
  with an invented convention.
