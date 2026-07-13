> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system · Fetched: 2026-07-12

# Troubleshooting the REV Control System

## General Best Practices

* **Charge the battery** — ensure batteries and phones/hubs are charged before a match.
* **Keep software updated** — RC app, firmware, and OS all receive periodic fixes; staying current avoids known bugs.
* **Isolate the issue** — many symptoms overlap across root causes; eliminate failure points one at a time (swap cables, swap batteries, swap devices) rather than guessing.
* Never plug a battery charger directly into a Control Hub or Expansion Hub — it will damage the hub and eventually cause device failure.

### ESD (Electrostatic Discharge) Mitigation

FTC foam field tiles can build up static that discharges into robots during play:

1. Plug USB devices (e.g. a webcam) into the Control Hub's USB 3.0 port, not USB 2.0 — 2.0 is more susceptible to ESD affecting the Wi-Fi chip.
2. Add a Resistive Grounding Strap (REV-31-1269, 470 Ω) between robot electronics and frame to reduce high-discharge events.
3. Treat the practice area with anti-static spray.
4. See FIRST's own [ESD guidance](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html) for more strategies.

### USB Port Care

Don't force USB connectors (can push the port into the Control Hub/Driver Hub body); keep ports free of debris (power off before compressed air); remove all USB cables from a Driver Hub before storage/transport; never wrap a plugged-in USB cable around the Driver Hub (the most common cause of USB port damage).

## Control Hub Troubleshooting

Start by identifying the symptom:
* Driver Station device can't connect to the Control Hub's Wi-Fi at all → see [connectivity troubleshooting](#connectivity-driver-stationhub-wont-connect).
* Connected to Wi-Fi but no ping/communication → same connectivity flow below.
* Status LED solid blue for more than 30 seconds after startup → see [Solid Blue LED](#status-led-solid-blue-for-30-seconds).

### Connectivity: Driver Station/Hub Won't Connect

Diagnostic questions to isolate the cause:

* **What's the local Wi-Fi environment like?** Use a Wi-Fi analyzer app to check for channel congestion, then set the Control Hub to a less-crowded channel (Manage page, or the physical user-button band switch).
* **Is the connecting device already joined to another Wi-Fi network with internet?** The Control Hub's network has no internet — some devices auto-switch to a remembered network instead.
* **Are you at a school or business?** Institutional Wi-Fi security may block unrecognized access points; ask the network administrator about allow-listing the Control Hub's SSID.
* **2.4 GHz or 5 GHz band?** REV recommends 5 GHz for competition on dual-band devices.
* **Does it disconnect specifically when a mechanism runs?** This points to a brownout, not a Wi-Fi problem — symptoms include a Driver Station power error, a disconnect sound, displayed voltage dropping to ≤9V while running code, or motors running slower than commanded. Fix by reviewing [battery best practices](control-hub-setup-and-firmware.md#slim-battery-rev-31-1302-best-practices) — a physically fine-but-failing battery is a common cause.

If the SSID isn't listed at all, try manually entering it. A full Wi-Fi factory reset (via the user button) downgrades the connection to 2.4 GHz — remember to switch back to 5 GHz afterward if that's what your Driver Station needs. Look for behavioral patterns (works at home, not at school; works until the robot starts driving) — correlation isn't causation, but it's useful data for REV Support, along with logs (see `control-hub-setup-and-firmware.md`, log/diagnostics section).

### Status LED Solid Blue for 30+ Seconds

Indicates the Robot Controller isn't communicating with the Control Hub's I/O — root cause unclear from the LED alone. First step: update all software (OS, firmware, RC app) via REV Hardware Client, or via Android Studio (requires RC app 5.0+; rebuild/redeploy from a 5.0+ project).

### XT30 Pins Compressed

The most common cause of a loose/wiggly XT30 connection. Each male XT30 pin has 4 tines that need a small gap between them — sometimes compressed even when a gap is visible. Fix: very carefully separate the tines with an X-ACTO knife or similarly thin blade. Overextending the tines weakens them permanently — this kind of wear is not covered under warranty.

### DC Motor Port Voltage Testing

To check whether a motor port is internally damaged/shorted, run code that drives the port at 100% power and measure voltage at the port's terminals with a multimeter (set to DC voltage). A healthy port reads voltage close to the battery's supply voltage. A port that reads near-zero while the battery is charged and the code is running indicates a damaged internal motor controller for that port — the fix is REV's Control Hub Repair Service, not a field repair.

## Expansion Hub Troubleshooting

Diagnostic questions:
* Did a firmware update precede the problem?
* What's the Status LED doing?
* Does the Driver Station report "Can't find the Expansion Hub Portal"?
* Did the RC app open automatically on connect/power-up?
* Any issue specifically with primary/secondary Hub communication?

Note: Expansion Hubs purchased after December 2021 no longer include an internal IMU.

**Common fixes by symptom:**
* Firmware update failed / hub unresponsive → retry the [firmware update](control-hub-setup-and-firmware.md#updating-firmware-control-hub--expansion-hub).
* LED not lighting at all → firmware update, then if still dark, do the USB Serial Converter check below.
* Hub not recognized / not communicating with phones → power-cycle procedure below.
* Trouble seeing a *secondary* Expansion Hub → confirm the first Expansion Hub is connected to the Robot Controller, then change the second hub's RS485 address (see FTC's [Using a Second Expansion Hub](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Using-Two-Expansion-Hubs#checking-the-address-of-an-expansion-hub) wiki).

**XT30 pins compressed:** same fix as Control Hub above.

**USB Serial Converter check** (legacy Android-RC systems): Device Manager → Universal Serial Bus Controllers → look for "USB Serial Converter". If absent, email REV support with the troubleshooting steps taken and the Expansion Hub's order number if available. (On Mac: System Information / System Profiler via Spotlight, in /Applications/Utilities.)

**Expansion Hub power cycle:** unplug USB from the RC phone → power off the main robot switch (cut 12V to the Expansion Hub) → wait a few seconds → power back on → force-close the RC app on the phone → replug USB (RC app should auto-open). If it doesn't auto-open, the Expansion Hub-to-phone connection is bad — check cables, then the micro/mini USB connectors themselves; consider a strain-relief mount (e.g. REV-41-1214) to protect the USB-mini port from cable stress.

## Driver Hub Troubleshooting

Terminology used below: **Power Off** = long-press (1–2s) the power button, tap "power off." **Hard Reboot** = hold power button 10+ seconds without touching the screen until the LED and screen go dark, then release.

**Updating the OS:** install on a fully charged Driver Hub; don't touch the screen while the update progress bar is showing (touching it diverts to a menu post-install — don't hard-reboot in that case either); verify the new version afterward in REV Hardware Client.

**Intermittent power loss (loose battery bay):** some units have slight extra space in the battery bay causing intermittent contact. Fix with a folded-paper/tape shim opposite the contacts, or REV-supplied foam tape (cut to ~2in x ≤1/4in x ≤1/16in, applied opposite the battery contacts below the door ridge).

**Charging/power symptoms** (only turns on while charging; rapid discharge; reports low battery well above 0% and shuts off; won't boot even when charged; won't turn on while on the charger; stops charging): work through, in order — check battery orientation, confirm you're using the Driver Hub's original *non-PD* charger, unplug/replug the charger, fully update the Driver Hub, run a battery recalibration (below), attempt lockout recovery (below), and if all else fails, swap in a known-good battery to isolate battery vs. unit.

**Battery calibration:** plug into the Driver Hub's original charger *without the battery installed* → confirm it reports 100% (if not, you may be using a PD charger by mistake) → install the battery while still charging → charge at least 8 hours without removing battery/cable → unplug → hard reboot.

**Battery lockout recovery** (a protective "safe mode" — symptoms: only powers on while on USB with no battery; appears not to charge after long connection; won't power on with battery+USB; won't turn on but the red status LED lights on USB): with the battery installed, plug into the original wall charger via the orange USB-A-to-USB-C cable (battery LED should blink red) → charge 5 minutes → unplug, wait, replug → check if the charging icon now appears when pressing power (if not, repeat — typically takes 4–5 cycles) → once it appears, charge fully off for 8 hours to complete calibration.

**"Control Hub in Recovery Mode" shown for a Driver Hub in RHC:** perform a factory reset (Settings → System → Reset options → Erase all data).

**"App not installed" error / Driver Station won't open** after an OS+app update: remove the Driver Station icon from the home screen (drag to X) and re-drag it from the app drawer.

**Android permissions lockout:** factory reset (Settings → System → Reset options → Erase all data — this erases all Driver Hub data).

**Wi-Fi immediately turns off / won't stay on:** usually a failed Wi-Fi chip (physical damage) — use the Driver Hub Repair Service (REV-31-1596-RFB); contact support if still under warranty.

**Known, unresolved software issues:**
* Wi-Fi driver doesn't restart correctly waking from sleep — hard reboot fixes it; keep the screen on and Driver Station app open before a match to prevent sleep entirely.
* Unlock takes 2–10 seconds — this is normal, not a bug.
* Device freezes/crashes in sleep (including cases where status LED B is solid green but the screen won't wake) — hard reboot.
* Inconsistent battery drain in sleep mode, sometimes causing shutdowns — known issue, fix pending in a future update.

**Battery installation:** REV logo facing out, -/+ near the device contacts; attach the rear door with the included M3 hardware.

**Escalate to REV Support** (support@revrobotics.com) if: boot-loops, freezes on boot even after a hard reboot, or charging/power issues persist after multiple calibration attempts.

## Status LED Blink Codes

### Control Hub (RC App 6.0+; 5.5-and-below hubs follow the Expansion Hub FW 1.7.0+ codes instead)

| LED | When | Meaning |
|---|---|---|
| Solid Blue | At boot | Powered, battery >7V, waiting to initialize comms |
| Solid Blue | Anytime | Waiting for Driver Station Host communication |
| Solid Green | Anytime | Powered with active communication to the Android platform |
| Blinking Blue | Anytime | Keep-alive timed out; clears when comms resume |
| Blinking Orange | Anytime | Battery <7V — charge it, or hub is running on USB power only |
| Blinking Magenta | During Wi-Fi band change | Switched to 5 GHz |
| Blinking Yellow | During Wi-Fi band change | Switched to 2.4 GHz |

### Driver Hub

* **LED A** blinking white = OS booting.
* **LED B** solid green = device is on.
* **Battery Status LED**: blinking red = charging; solid red = fully charged.

### Expansion Hub (Firmware 1.7.0+)

| LED | When | Meaning |
|---|---|---|
| Solid Blue | At boot | Powered, battery >7V, waiting to initialize comms |
| Solid Blue | Anytime | Waiting for Robot Controller communication |
| Solid Green + N blue blinks every ~5s | Anytime | Active comms; N = the hub's RS485 address (factory default is 2) |
| Blinking Blue | Anytime | Keep-alive timed out |
| Blinking Orange | Anytime | Battery <7V or USB-only power |

## 12V Slim Battery (REV-31-1302) Best Practices and Troubleshooting

* The 12V Slim Battery Charger (REV-31-1299) has a rate switch, often shipped at 0.9A — set it to 1.8A for faster charging.
* Charger LED: red while charging, green when done.
* Let the battery cool to room temperature after charging before use.
* When unplugging from the Control Hub, pull on the connector body, not the XT30 wire sheathing (can expose/damage the solder joints).
* Do not use a battery with fraying or visibly damaged wire sheathing.

**If the battery isn't powering the Control Hub:** check the XT30 connector for damage/looseness, inspect the red/black wires for damage, and check the inline fuse (open the black fuse housing on the red wire — if the bridge is broken, replace with a standard 20A automotive fuse). If the battery no longer holds a charge well, it may simply need replacing.
