# Hub generation: SystemCore / MotionCore / A301 (next system — NOT yet FTC-legal)

> STATUS: **Reviewed & merged** (Phase 7, approved 2026-07-03), with five Rule-7
> corrections applied: kernel `6.6.64-rt47` (not a 6.6→6.12 range), custom Buildroot
> OS (confirmed not a standard distro), `ExpansionHubDaemon`/RHSP hybrid mechanism,
> FTC DS/networking downgraded to UNCONFIRMED, and Java/Python versions downgraded
> to [T2, single-source].
>
> **FORWARD-LOOKING, STILL-EVOLVING (alpha).** This is exactly the category
> Rule 7 exists for. Not FTC-legal until 2027-28. Nothing here should be treated
> as settled; every claim carries a tier tag and source. Re-verify before relying.

Tags: **[T1]** = tier-1 (official FIRST / WPILib / Limelight source).
**[T2]** = tier-2 (alpha-tester GitHub issues, Chief Delphi / Open Alliance, third-party summaries).
**[UNCONFIRMED]** = no source resolves it yet; do not fill the gap.

---

## Confirmed (tier-1)

### Architecture
- **[T1]** **SystemCore** is powered by a **Raspberry Pi Compute Module 5 (CM5)**
  — **quad-core ARM Cortex-A76** — with a **Raspberry Pi RP2350** handling
  reconfigurable I/O (PWM, digital, analog). *Independently confirmed by three
  tier-1 sources: FIRST's announcement, docs.wpilib.org, and Limelight's
  systemcore-os-public repo — this triple-sourcing is genuine Rule-7 corroboration.*
- **[T1]** SystemCore is a **Limelight Vision** device ("Limelight Systemcore…
  designed specifically with FIRST in mind").
- **[T1]** **MotionCore** is a **separate device** — power distribution, CAN
  communication, and actuator/encoder support in one unit — connected to
  SystemCore via **CAN FD over a bridge port**.
- **[T1]** The **FIRST A301** is a **CAN-based smart brushless actuator**, and per
  FIRST's own words *"will be the only legal actuator in the new control system,"*
  replacing all existing third-party motors and servos on that system. It was
  created *"through direct collaboration between FIRST and REV Robotics."*

### OS / kernel  (specific versions from independent firmware reverse-engineering — mind the tiers)
- **[T1]** **Real-time Linux** (FIRST's wording).
- **[T2]** **Kernel `6.6.64-rt47`** (PREEMPT_RT), from independent reverse-engineering
  of the actual firmware image (dunkirk.sh, Apr 2026). This is the *single confirmed
  running version*. Do **not** conflate it with "6.12" — 6.12 is mainline
  PREEMPT_RT's merge version, a different fact. (An earlier "6.6→6.12 range" framing
  here was wrong and has been removed.)
- **[T2]** **Not a standard distribution — confirmed.** The image is a **custom
  Buildroot build with no standard package manager** (dunkirk.sh). This upgrades the
  earlier "Ubuntu?" question from unconfirmed to *confirmed NOT Ubuntu/Debian/any
  standard distro.*
- **[T2]** The image ships an **`ExpansionHubDaemon`** that speaks **RHSP (REV Hub
  Serial Protocol) over USB-serial** specifically to support **legacy REV Expansion
  Hub** hardware (dunkirk.sh) — a concrete mechanism behind the hybrid configuration.
- **[T2, single-source]** OS-runtime language support reported as **Java 25 /
  Python 3.13 / C++** — this traces to **one** source only (Limelight
  `systemcore-os-public` repo) and is **not** independently corroborated, so it is
  tier-2 per Rule 7, not tier-1. It is also the OS-runtime layer, **not** the
  FTC-facing SDK/language story (which is separately unconfirmed, below).

### Timeline & legality
- **[T1]** Legal for FTC teams to **compete starting the 2027-28 season.**
- **[T1]** **Transition period through at least 2030-31**, during which the
  **legacy system and a hybrid approach are both legal.** → The transition is NOT
  a binary REV-or-SystemCore choice.
- **[T1]** Alpha explicitly includes a **hybrid configuration**: SystemCore paired
  with **existing batteries, motors, and REV Expansion Hubs**, alongside
  full-system testing with A301 actuators.

### Battery
- **[T1]** An **18V lithium power-tool battery + a robot-mounted dock**,
  **explicitly still in development** as of FIRST's most recent post — not finalized.

### Reliability (design goals, stated by FIRST)
- **[T1]** Reliability is an **explicit, stated design goal**, not just hoped-for:
  FIRST cites **reverse-polarity and short-circuit protection, ESD protection,
  robust update/recovery, and positive-retention connectors** specifically to
  reduce accidental disconnects. *Worth citing directly — it validates the same
  reliability-first standard this whole system is held to.*

### Driver Station (2027) — described for FRC; FTC applicability UNCONFIRMED
- **[T1, FRC]** A **new Driver Station**: *"more robust… proper port handling so
  firewall modifications should no longer be necessary."* First iteration on
  **laptops** (Windows/macOS/Linux, x64+arm64); **planned** support for a future
  hardware appliance and the **existing REV Driver Hub via an OS update**; *"not
  compatible with either the existing FRC or FTC control systems."*
- **[UNCONFIRMED for FTC]** Whether FTC's Driver Station / networking protocol
  matches the FRC one is **not established**. The reverse-engineering corroboration
  is of the **FRC image specifically** (roboRIO-pattern hostnames, NI discovery
  services — FRC-only conventions), so shared-component agreement on kernel/hardware
  does **not** carry to protocol-level specifics, which differ by program.

---

## Not yet confirmed — verify before relying (Rule 7)

- **OS distribution — RESOLVED (see OS/kernel above):** confirmed **NOT** a standard
  distro — a custom Buildroot image **[T2]**. No longer an open question.
- **Full lifecycle model — [UNCONFIRMED for FTC].** WPILib's FRC standard is
  `TimedRobot` (enabled/disabled; `robotInit`/`autonomousInit`/`autonomousPeriodic`/
  `teleopInit`/`teleopPeriodic`) — **[T1] for FRC**. Whether FTC keeps the per-match
  OpMode-selection model or moves to this continuous enabled/disabled program is
  **not officially stated**. **[T2]** alpha reports note `OpModeRobot` was
  non-functional, forcing a `TimedRobot` workaround — evidence of a shift, but
  tier-2 and evolving. Do not resolve this ambiguity.
- **FTCLib compatibility across both hub generations — [UNCONFIRMED].** No tier-1
  statement that FTCLib runs on SystemCore. **[T2]** alpha software is "not
  compatible with Control Hub or roboRIO; only SystemCore is supported." Do **not**
  assume continuity of any library across the boundary.
- **FTC language / SDK story — [UNCONFIRMED].** FIRST's own posts do not state the
  FTC programming language or SDK. The OS-runtime language versions (Java 25 / Py 3.13
  / C++) are **[T2, single-source]** (above) and are the OS layer, not the FTC SDK.
  A **Chief Delphi thread as recent as May 2026** shows the FTC-specific language
  story is **still an open community question** — a reason for *more* scrutiny here,
  not less. **Keep flagged as unconfirmed — do not resolve.**
- **Networking / Driver Station protocol (FTC) — [UNCONFIRMED].** See the Driver
  Station section: the described protocol is **[T1] for FRC** only; its FTC
  applicability is not established, and the reverse-engineering corroboration is
  FRC-image-specific (FRC-only hostname/discovery conventions).

---

## Cross-check: failure-mode taxonomy
The SystemCore-alpha section of `known-failure-modes.md` (repo root) independently
corroborates several points above (API churn / `OpModeRobot` workaround, A301
hardware lock-in, no finalized Driver Hub, fragmented docs, the OpMode→enabled/
disabled mental-model shift). Those are tagged **[T2]** there (alpha reports /
forums), consistent with this file.

---

## DESIGN REQUIREMENT — time-gated `hub_generation` elicitation

This is the concrete meaning of "onboarding must clarify the adaptation period."
On merge, this becomes a documented addition to **PLAN §15** (pending sign-off).

- **Now → end of 2026-27 season (REV Control Hub is the sole legal option):**
  **do NOT ask** `control_hardware.hub_generation`. Only one value is legal, so the
  question has zero information gain and would violate §13's purposefulness principle.
- **The moment the hybrid-legal window opens (targeted 2027-28):**
  `hub_generation` **joins the mandatory-ask set** alongside drivetrain topology,
  the season mechanism set, and software stack — **but it must be preceded by a
  short briefing, not asked cold.** The briefing explains:
  1. what SystemCore/MotionCore/A301 changes about the team's code;
  2. that **both systems stay legal for years** (through at least 2030-31) — not a
     forced cutover;
  3. that a **hybrid REV+SystemCore configuration** may be a real option, not just
     "old system or new system."
  Only after that briefing does the skill ask which platform (or hybrid config) the
  team is actually building on. Present the choice with real tradeoffs — the same
  aircraft-grade standard as Rule 7 — never default silently to either system.

Implementation note: this is a **time-gate**, so it should key off the active season
(via `season-extensions/ACTIVE`) reaching 2027-28, not a hardcoded date, and the
`control_hardware.hub_generation` axis already exists in `core-feature-model.yaml`
for exactly this reason (its enum already carries both values).

---

## Sources
- **[T1]** FIRST, "Control System Update — FIRST Tech Challenge Edition," community.firstinspires.org
- **[T1]** WPILib, "The 2027 FIRST Driver Station," wpilib.org/blog
- **[T1]** WPILib SystemCore docs, docs.wpilib.org/en/latest/docs/software/systemcore-info/
- **[T2, single-source]** Limelight, `LimelightVision/systemcore-os-public` — sole
  source for the Java 25 / Python 3.13 runtime versions (uncorroborated → tier-2).
- **[T2]** dunkirk.sh (Apr 2026) — independent reverse-engineering of the actual
  firmware image: kernel `6.6.64-rt47`, custom Buildroot (no standard package
  manager), `ExpansionHubDaemon` speaking RHSP over USB-serial. NB: this analysis
  targets the **FRC** image specifically (FRC-only hostname/discovery conventions).
- **[T2]** `wpilibsuite/SystemcoreTesting` alpha-tester issues/discussions (GitHub)
- **[T2]** Chief Delphi "SystemCore / MotionCore rollout questions" thread
- **[T2]** Chief Delphi (May 2026) — FTC-specific programming language still an open question
