> Source: https://docs.revrobotics.com/duo-control/sensors/intro-to-sensors · Fetched: 2026-07-12

# Sensor Integration Guide

Covers REV's sensor classification (basic/intermediate/advanced), wiring and configuration for each port type (digital, analog, I2C), the IMU, motor/Through Bore encoders, and integrating 3rd-party (5V) sensors.

## Sensor Basics and Classification

Time-based actions (run a motor for N seconds) degrade as battery voltage drops and mechanisms wear in. Sensors give the robot feedback so behavior stays accurate and repeatable — e.g. autonomously stopping at a location, reacting to a signal color, preventing an arm from over-rotating, stopping a fixed distance from a wall, or counting held game pieces.

REV classifies sensors by programming complexity:

* **Basic** — Analog and Digital sensors. Codable with simple if/else logic.
* **Intermediate** — I2C sensors (Color Sensor, 2m Distance Sensor) and motor Encoders. Require two-way communication or signal decoding.
* **Advanced** — Vision sensors and the IMU. Require more complex code and often combine data from multiple sources.

## Digital Sensors

Digital sensors report one of two binary states (TRUE/FALSE, 1/0, High/Low). Electrically, REV Hub digital ports use **3.3V logic** — High is 3.0V, Low is 0V. A sensor's datasheet specifies whether it's **active-high** or **active-low** (i.e., whether a logic low→high transition, or the reverse, means "triggered").

REV digital sensors: Touch Sensor (REV-31-1425), Magnetic Limit Switch (REV-31-1462), Digital LED Indicator (REV-31-2010).

**Wiring:** JST PH 4-pin sensor cable. Black = ground, red = power, blue/white = the two signal channels. Each physical digital port hosts **two logical ports** via its two channels — marked like 0-1, 2-3, etc. The `n+1` channel is the odd port (1, 3, 5, 7), `n` is the even port (0, 2, 4, 6). Two sensors can share one physical port via a Sensor Splitter Cable, but check each sensor's datasheet first — some (like the Touch Sensor) only use one channel.

**Configuration:** Driver Station → Configure Robot → **Digital Devices** → pick a port (touch sensors **must** go on an odd port) → choose device type (e.g. "REV Touch Sensor" vs. generic "Digital Device" — this choice determines which SDK classes/methods you get) → name it → Done.

**Typical use:** limit switches — stopping an arm/lift at its physical travel limit (prevents mechanical damage) and zeroing encoder position at a known point.

## Analog Sensors

Analog sensors report a continuous range rather than two states — a proportional voltage, readable by REV Hubs from **0V to 5.0V**. REV's analog sensor is the Potentiometer (REV-31-1155), commonly used to measure the angle of an arm-type joint.

**Wiring:** same JST PH 4-pin convention as digital (black=ground, red=power, blue/white=signal). Each physical analog port hosts two logical ports (0-1, 2-3); `n+1` = odd, `n` = even. A Sensor Splitter Cable (REV-31-1386) can share one port between two sensors, subject to each sensor's pinout.

**Configuration:** Configure Robot → **Analog Input Devices** → pick a port → select "Analog Input" → name it → Done.

## I2C Sensors

I2C is a two-way bus protocol: one **host** (the Hub) talks to multiple **devices** on a bus, each with a fixed address assigned by its manufacturer. Every physical I2C port on a Hub is a separate bus. Two devices sharing the same address (e.g. two REV Color Sensor V3s) cannot be on the same bus — they must go on separate physical I2C ports; REV does not sell a splitter for this, so a custom cable would be required to combine two on one port.

REV's I2C sensors: IMU (built into the Control Hub, and into Expansion Hubs shipped before Dec 2021), Color Sensor (REV-31-1557), 2m Distance Sensor (REV-31-1505). **I2C Bus 0 always hosts the internal IMU.**

**Wiring:** JST PH 4-pin cable; black=ground, red=power, blue=SCL (clock), white=SDA (data). The clock line (SCL) timestamps the data line (SDA) — this is why I2C can carry more complex data than simple digital/analog signaling.

**Configuration:** Configure Robot → select the I2C bus → **Add** → choose the specific sensor from the dropdown (drivers for all FTC-legal I2C devices are built into the SDK) → name it → Done. Example: adding a Color Sensor V3 onto Bus 0 alongside the internal IMU.

**Typical uses:**
* **Color Sensor** (all versions) — senses color within ~2cm; used for autonomous decisions between differently-colored game elements.
* **2m Distance Sensor** — higher-accuracy proximity than a color sensor; combined with odometry, useful for autonomous obstacle navigation.
* **IMU** — see below.

## The IMU (Inertial Measurement Unit)

Every Control Hub has a built-in IMU; Expansion Hubs shipped **before December 2021** also have one (later units don't). It combines an accelerometer, gyroscope, and magnetometer to report orientation and angular velocity. Acceleration data anchors pitch/roll against gravity so those don't drift; heading (yaw) does drift slowly over time from accumulated small errors.

**I2C address 0x28, always on port 0.**

**Which chip:** original hubs shipped with the Bosch BNO055; since **September 2022**, Control Hubs ship with the Bosch BHI260AP instead. Check which one you have via the Manage page (Program & Manage menu). A new configuration file auto-detects the correct type on I2C port 0.

### Universal `IMU` interface (RC app 8.1+, recommended)

Works with both BNO055 and BHI260AP. Converts raw values into **robot-centric** values (based on how you tell it the hub is mounted), rather than hub-centric — so results don't depend on the hub happening to be mounted logo-up.

Robot Coordinate System: origin inside the robot; Z points up (ceiling); Y points out the robot's front; X points out the right side; right-handed rotation convention.

`IMU.getRobotYawPitchRollAngles()` is the method most teams should use:
* **Yaw** (heading) — rotation about Z (side-to-side lateral rotation).
* **Pitch** — rotation about X (front-to-back tilt).
* **Roll** — rotation about Y (side-to-side tilt).

### Legacy `BNO055IMU` interface

Only works with hubs that have the original BNO055 chip; only reliable when the hub is mounted flat with the logo facing up; values are hub-relative, not robot-relative; you must manually specify axis order (ZXY is the common recommendation). Hub-relative axes: X runs bottom (servo ports) to top (USB ports); Y runs sensor-port side to motor-port side; Z points up through the REV logo.

### Setting Orientation in Code

**Blocks:** IMU blocks live under the Sensors menu. Easiest option: describe orientation via the logo-facing direction and USB-facing direction (default is logo UP, USB FORWARD). For non-flat mounting, use an orientation-parameter block (or a Quaternion block) to describe the rotation needed to go from the default orientation to the actual one.

**OnBot Java:**

```java
RevHubOrientationOnRobot.LogoFacingDirection logoDirection = RevHubOrientationOnRobot.LogoFacingDirection.UP;
RevHubOrientationOnRobot.UsbFacingDirection  usbDirection  = RevHubOrientationOnRobot.UsbFacingDirection.FORWARD;

RevHubOrientationOnRobot orientationOnRobot = new RevHubOrientationOnRobot(logoDirection, usbDirection);

imu.initialize(new IMU.Parameters(orientationOnRobot));
```

For a non-orthogonal mount, define rotations along X/Y/Z instead — see the `SensorIMUNonOrthogonal` sample bundled with OnBot Java in the FTC SDK.

**Recommended mounting:** BHI260AP hubs — mount flat on a horizontal plane for best accuracy. BNO055 hubs — flat on either horizontal or vertical plane is fine.

### IMU ESD Resets (2023-24 season issue)

Some teams saw the IMU unexpectedly reset after an ESD event. Control Hub OS 1.1.4 reduces this on BHI260AP hubs. Additional mitigations: standard ESD prep (grounding strap REV-31-1269, anti-static field spray — coordinate with event hosts), verify your code references the IMU correctly, check for a secure/charged battery connection (poor connections/low voltage have also caused resets), and give drivers a manual re-init trigger (e.g. a gamepad button) with a known field-alignment reference to re-zero against.

### Adding an External / Second IMU

Useful when the built-in IMU isn't available (e.g. newer Expansion Hub) or a second one is wanted. REV's **9-Axis IMU (REV-31-3332)** requires RC app v10.0+; configure it like any other I2C device — pick the I2C bus (not bus 0 if the internal IMU is already there), **Add**, select "REV 9-Axis IMU" from the dropdown, name it, Done. It then appears under Sensors in Blocks, or in `hardwareMap` (auto-added in OnBot Java if "Setup Code for Configured Hardware" was checked when creating the OpMode).

Other compatible external IMU/gyro options: navX2 Sensor Bundle (Kauai Labs/AndyMark — fully supported, includes correct FTC cabling); Adafruit 9-DOF Absolute Orientation IMU (the same chip as pre-2022 Control Hubs — needs a custom/soldered adapter cable, then configures/programs identically to an internal IMU on I2C port 0); Modern Robotics Integrating Gyro via REV's Logic Level Converter + Sensor Cable Adapter (single-axis only, not a full IMU).

## Encoders

An encoder converts a motor shaft's angular position/motion into an electrical signal a microcontroller can read.

**Absolute vs. relative (incremental):** absolute encoders report the actual angle directly and retain position through a power cycle (no re-homing needed); relative/incremental encoders report motion (e.g. "5 RPM forward") and only produce data while turning — they need a startup calibration routine to establish a reference point, since they don't know their position at boot.

**Optical vs. magnetic:** optical encoders read a slotted/reflective disk via a photodiode — light, compact, but sensitive to dirt/fingerprints on the disk. Magnetic encoders use Hall-effect sensors reading a rotating magnet — more tolerant of harsh/dirty environments. REV's HD Hex and Core Hex motors use 12-pole magnetic quadrature encoders.

### Quadrature Encoders

Two Hall-effect sensors ("Channel A" and "Channel B") are mounted 90° apart around the magnet. As poles pass, each channel outputs a changing voltage; the 90° phase offset between A and B lets the controller determine rotation direction as well as count, not just count alone (a single channel could count rotations but not tell direction). On REV's HD Hex/Core Hex motors, Channel A leads Channel B when positive voltage is applied to M+ — but gearbox differences or swapped encoder wiring can reverse this in practice, so verify empirically when debugging direction issues.

**Key terms:**
* **Cycle** — one complete pass through all four quadrature states.
* **CPR (Cycles Per Rotation)** — cycles per revolution of the *encoder* shaft (depends on magnet pole count).
* Most controllers use **4x decoding** (both channels, both edges) — this is a property of the decoding electronics, not the encoder hardware, so REV defines specs by CPR rather than PPR.

Formulas:
```
Counts per rotation (encoder shaft) = CPR × 4
Counts per rotation (output shaft)  = CPR × 4 × gearbox reduction
Degrees per count = 360° / counts per rotation (output shaft)
```

### REV Motor Encoder Specs

**Core Hex Motor (REV-41-1300)** — 72:1 reduction, 125 RPM free speed, 4 CPR (1 rise of Channel A per encoder-shaft rev), **288 counts per output-shaft rotation**.

**HD Hex Motor (REV-41-1291)** — 28 CPR (7 rises of Channel A) at all reductions:
| Reduction | Free Speed (RPM) | Counts/output-shaft rotation |
|---|---|---|
| Bare motor | 6000 | 28 |
| 40:1 | 150 | 1120 |
| 20:1 | 300 | 560 |

Both motors use a 2-pin JST-VH for power and a 4-pin JST-PH for encoder feedback, into the Control/Expansion Hub's encoder ports (paired with each motor port).

### Through Bore Encoder (REV-11-1271)

A standalone rotary sensor placeable anywhere you need to measure rotation, not just on a motor shaft. Outputs both ABI quadrature (relative) and an absolute-position pulse — **but the FTC Control System (Control Hub/Expansion Hub) currently only supports the incremental/quadrature output via the motor encoder ports; the absolute pulse output is not supported.**

Includes a 5mm hex insert (press in narrow-end-first; remove wide-end-first if it's stuck) and a 4-pin JST PH to 6-pin JST PH adapter cable — the 6-pin end plugs into the encoder, the 4-pin end into a Control/Expansion Hub encoder port. Both A and B channels are used.

## Using 3rd-Party (5V) Sensors

REV Control/Expansion Hubs are **3.3V logic level** devices. Many legacy/3rd-party sensors (e.g. older Modern Robotics parts) are 5V logic. Bridge them with REV's **Logic Level Converter (REV-31-1389)** plus, for some devices, a **Sensor Adapter Cable (REV-31-1384)**. All REV-brand motors and sensors are natively 3.3V-compatible — no converter needed for REV parts.

The Logic Level Converter is a bidirectional level-shifter board (5V↔3.3V) using a MOSFET per signal line — works for digital and I2C signals alike. It's only needed on Digital/I2C ports for 5V devices.

**Connecting a 5V encoder:** the Logic Level Converter's pinout matches standard FTC-legal 3rd-party motor encoder cables directly; its included 4-pin JST PH cable then plugs into a Control Hub encoder port. Motors terminated with Anderson Power Pole connectors need the JST-VH-to-Anderson-Power-Pole cable (REV-31-1381) for the power side.

**Connecting a 5V sensor:** generally needs the Logic Level Converter plus a rewired/crossed sensor cable to match the Control Hub's pinout (purchasable as an add-on, or manually re-pinned). Zip-tie the sensor-to-cable connection to prevent accidental disconnects.

**Wiring a limit switch/microswitch (3rd-party):** digital inputs on REV Hubs have a pull-up resistor (pulled high by default) — incorrect wiring can make the hub unresponsive. Recommended: signal wire → COM, ground wire → NC (normally closed), leave NO (normally open) unconnected. Unpressed = switch closed = signal tied to ground = reads `FALSE`; pressed = switch opens = reads `TRUE`. For inverted logic, wire ground to NO instead (or just flip the boolean in code). Leave the power wire and the unused signal channel disconnected.

### Sensor Compatibility Notes (as of Sept 2025, RC app v11.0)

Directly compatible with no adapter needed: navX2-Micro, REV 9-Axis IMU, REV Color Sensor V2/V3, REV 2m Distance Sensor, OctoQuad, goBILDA Pinpoint Odometry Computer, AndyMark standard color/lidar/IMU sensors, REV HD Hex/Core Hex motor encoders, most quadrature motor encoders (NeveRest, MATRIX, Tetrix, Studica), REV Touch Sensor, REV Through Bore Encoder (incremental only), Limelight 3A (USB 3.0 port required).

Needs a custom wiring harness or adapter cable: Adafruit BNO055 breakout and TCS34725 color sensor (3.3V-compatible but need custom harnesses), HuskyLens (custom adapter cable), SparkFun Optical Tracking Odometry Sensor (SparkFun adapter cable), goBILDA Yellow Jacket/5000-series motors (goBILDA adapter cable), various Modern Robotics I2C sensors (adapter needed per sensor).

**Not officially supported:** Modern Robotics Rate Gyro, Optical Distance Sensor, Light Sensor, and Magnetic Sensor.

Always cross-check the vendor's current documentation, since compatibility/adapters can change between SDK/RC-app releases.
