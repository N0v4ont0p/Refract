> Source: https://docs.revrobotics.com/duo-control/menu/configuring-devices · Fetched: 2026-07-12

# Device Configuration, Adding Motors, and the Expansion Hub

Covers the Driver Station configuration-file workflow (hardware mapping), when/how to add a SPARKmini or an Expansion Hub, and RS485/Servo Hub configuration.

## The Configuration File

The configuration file is created through the Driver Station app. For each connected device you assign: a port, a device type (from a list the SDK provides), and a **unique, case-sensitive** name. Saving/activating a configuration restarts the Robot Controller so the SDK can read the file and populate `hardwareMap` with the named devices.

### Creating a Configuration

1. Driver Station app menu (top right) → **Configure Robot**.
2. On the Available Configurations page, select **New**.
3. On the USB Devices page, select the **Control Hub Portal** (shows as **Expansion Hub Portal** if using an Expansion Hub connected via USB, or if using a legacy Android Robot Controller).
   - Warning: pressing **Scan** on an *existing* configuration can erase already-named devices. Create a new configuration file when adding a camera or an Expansion Hub.
4. Within the Hub Portal, select the specific hub to configure (Control Hub, or an RS485-connected Expansion Hub shown alongside it).

### Configuring Actuators and Sensors

Digital/Analog device configuration differs from I2C configuration, because each physical I2C port is a bus that can host multiple sensors (see `sensor-integration.md` for details).

**Motor:** select **Motors** → pick a port (4 available per hub) → choose motor type from the dropdown → name it → **Done**.

**Servo:** select **Servos** → pick a port (6 available per hub) → choose Servo or Continuous Rotation Servo (must match the physical mode the servo itself is set to — see REV's SRS Programmer docs for switching modes) → name it → **Done**.

**Digital device:** select **Digital Devices** → pick a port (8 available; **touch sensors must be on an odd-numbered port**) → choose device type — e.g. a REV Touch Sensor can be configured as either "REV Touch Sensor" or generic "Digital Device," which changes which SDK classes/methods are available → name it → **Done**.

**I2C device:** select the I2C bus (**Bus 0 always hosts the internal IMU**) → **Add** → pick the sensor from the dropdown for the newly created port (e.g. REV Color Sensor V3; use "REV Color/Range Sensor" for Color Sensor V1/V2) → name it → **Done**. Multiple I2C sensors can share a bus as long as their I2C addresses don't conflict.

### Configuring RS485 Devices (Expansion Hub / Servo Hub)

**Expansion Hub:** each Expansion Hub's configuration is unique to it — recreate the config if you swap in a different physical Expansion Hub. In a new configuration, select the Control Hub Portal; an RS485-connected Expansion Hub appears as a separate portal within it. Configure its devices the same way as above; the menu header indicates whether you're in the Expansion Hub's or Control Hub's port list.

**Servo Hub:** in a new configuration, select the Control Hub Portal → select the Servo Hub (shows its set ID) → **Servos** → configure the same as any other servo port.

### Saving

Press **Done** repeatedly back to the USB Devices page → **Save** → name the configuration → **OK** → press back to activate it. The Robot Controller restarts; the active configuration name shows on the configuration screen and the main Driver Station screen.

## Adding More Motors: SPARKmini vs. Expansion Hub

Both the Control Hub and Expansion Hub drive up to 4 DC brushed motors each. Rule of thumb for adding capacity:

* **1–2 more motors needed:** use a SPARKmini Motor Controller (REV-31-1230).
* **3–4 more motors needed:** add an Expansion Hub (REV-31-1153).

### SPARKmini Motor Controller (REV-31-1230)

A 60mm x 22mm in-line brushed DC motor controller with the same performance as a Control/Expansion Hub motor port.

**Wiring:** one XT30 connector for power (into a free hub XT30 port or an XT30 Power Distribution Block, REV-31-1293), one 3-wire servo-PWM connector for control (into a free hub servo port), one JST-VH connector for the motor (e.g. REV HD Hex Motor REV-41-1301 or Core Hex Motor REV-41-1300).

Do not reverse power polarity (no reverse-polarity protection — will permanently damage it) and do not swap the motor/power connections (causes uncontrolled motor operation, also destructive). Both void the warranty.

**Control signal:** extended-range servo-PWM, 500–2500 µs pulse width. 1500 µs (1490–1510 µs) is neutral; below ~1490 µs is proportional reverse (≤500 µs = full reverse); above ~1510 µs is proportional forward (≥2500 µs = full forward).

**Zero-power behavior** (selectable via a physical switch on the housing): **Brake** (motor terminals shorted, dissipates energy) or **Coast** (terminals disconnected, spins down freely). Status LED shows the active mode: blue = Brake, yellow = Coast.

**Key specs:** supply voltage 6–20 V typical (12 V nominal), 25 V absolute max; continuous output current 15 A, peak 20 A; output/PWM frequency ~10 kHz; input pulse width 500–2500 µs at 16–200 Hz; weight 0.87 oz; dimensions 60 × 22 × 12 mm (excl. wires).

### Adding an Expansion Hub (REV-31-1153)

An Expansion Hub has all the same ports as a Control Hub, minus wireless capability. It attaches to a Control Hub (or another Expansion Hub) via:
- XT30 extension cable for power
- 3-pin JST PH cable, RS485 port to RS485 port, for communication

**FTC/FIRST Global legality:** FTC teams may use one Control Hub plus one Expansion Hub (since the 2020-21 season) — confirm current-season limits in the official Game Manual. FIRST Global requires exactly one Control Hub and permits one Expansion Hub.

Note: a configuration file from Robot Controller Application 5.5 or earlier is not compatible — create a new one after adding an Expansion Hub.

**Steps:** wire power (XT30 extension) and RS485 (JST PH) between the hubs → Driver Station → **Configure Robot** → **New** → **Control Hub Portal** (shows as Expansion Hub Portal if the Robot Controller itself is an Android device) → you'll now see both the Control Hub and the Expansion Hub (labeled e.g. "Expansion Hub 2") as configurable targets → configure/program as needed. If the Robot Controller is an Android device with two Expansion Hubs present, their RS485 addresses may need to be changed so they don't conflict.

## Legacy: Expansion Hub with an Android Phone as Robot Controller

This is the pre-Control-Hub control system (an Android phone running the Robot Controller app, paired to an Expansion Hub over USB). It is not the current standard FTC control system but is documented for legacy hardware:

Required materials: Expansion Hub (REV-31-1153), 12V Slim Battery, a configured Android Driver Station and Robot Controller, USB-A-Female-to-Micro-USB cable (REV-31-1807).

Installing the DS/RC apps on the Android Robot Controller phone requires enabling Developer Options and USB Debugging in the phone's Android settings first, then using the REV Hardware Client's Hardware Tab → Update tab → Download/Install for each app. Minimum compatible app version for Expansion Hub support is 3.1 (released May 2017).

Configuration follows the same port/name pattern as above, under "Expansion Hub Portal 1" → "Expansion Hub 1".
