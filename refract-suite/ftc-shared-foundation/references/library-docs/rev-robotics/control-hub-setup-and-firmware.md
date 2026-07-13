> Source: https://docs.revrobotics.com/duo-control/menu/control-hub-gs · Fetched: 2026-07-12

# Control Hub Setup, Networking, and Firmware

This covers first-time Control Hub bring-up, Wi-Fi/network management, and updating the Control Hub's OS, firmware, and Robot Controller (RC) application. Software referenced: REV Hardware Client (RHC) and the Robot Controller Console (the on-hub web UI reachable at `192.168.43.1:8080`).

## Required Materials for Initial Bring-Up

* Control Hub (REV-31-1595)
* 12V Slim Battery (REV-31-1302)
* Driver Hub (REV-31-1596) or another approved FTC Driver Station device
* Gamepad (REV-31-2983, REV-39-1865, or approved FTC gamepad)
* USB-A to USB-C cable (included with Control Hub)
* A Windows PC running the REV Hardware Client

Optional, to add an Expansion Hub: Expansion Hub (REV-31-1153), XT30 extension cable, JST PH 3-pin communication cable (both included with the Expansion Hub).

## Connecting to the Robot Controller Console

The Robot Controller Console is the local network/web UI the Control Hub exposes for configuration and programming (Blocks, OnBot Java, and Manage pages). There are two ways to reach it:

### Option 1: REV Hardware Client (recommended, wired)

You can connect to a Control Hub over Wi-Fi or directly through USB-C with RHC. USB is recommended to reduce disconnects.

1. Power on the Control Hub via the 12V Slim Battery into the XT30 "BATTERY" port. The Control Hub is ready to connect once the LED turns from blue to green.
2. Plug the Control Hub into the PC with a USB-A to USB-C cable.
3. Start RHC. The Control Hub appears on the front page under the **Hardware Tab** — select it.
4. Selecting the connected hardware opens the **Update** tab. Select **Program and Manage** to open the Robot Controller Console built into RHC.
5. Before programming, it's useful to update the Control Hub OS, RC app, and Hub Firmware (see below) from this same screen.
6. Once in the console, the navigation menu (upper right) gives access to Blocks, OnBot Java, and Manage pages.

### Option 2: Web Browser (Chromebook/Mac, or no RHC)

1. With the Control Hub powered, open the Wi-Fi network selector on the connecting device.
2. Find the network matching the Control Hub's SSID — default names begin with `FTC-` or `FIRST-` followed by four random characters. (Connecting in a location without other active hubs makes it easier to identify the right one.)
3. Connect, entering the default password `password` (case-sensitive).
4. Once connected, note that **the connected device loses general internet access** — it only has direct access to the Control Hub.
5. Open a browser (Chrome, Firefox, Edge) and navigate to `192.168.43.1:8080`.

From the console you can update Wi-Fi settings, upgrade the OS/firmware, and program the device. Do this before starting to program.

If the SSID/password is forgotten, see [Managing Wi-Fi](#managing-wi-fi-on-the-control-hub) below for reset procedures.

## Updating Wi-Fi Settings

Every Control Hub ships with a default network name and password. Changing both is recommended, especially with multiple hubs active nearby (competitions, classrooms) — it also adds basic network security.

**Wi-Fi bands:** the Control Hub (REV-31-1595) supports 2.4 GHz and 5 GHz. REV recommends 5 GHz for competition. Devices' band support varies:

| Device | Notes | Wi-Fi Band |
|---|---|---|
| REV Driver Hub (REV-31-1596) | | 2.4 GHz & 5 GHz (Dual Band) |
| Moto G4 / 4th Gen | | 2.4 GHz only |
| Moto G5 / G5 Plus | | 2.4 GHz & 5 GHz |
| Moto E4 | US SKUs XT1765, XT1765PP, XT1766, XT1767 | 2.4 GHz & 5 GHz |
| Moto E5 | XT1920 | 2.4 GHz & 5 GHz |
| Moto E5 Play | XT1921 | 2.4 GHz & 5 GHz |

As of the 2024-25 season, Android Driver Station phones must run Android 7 (Nougat) or newer.

**Steps** (same whether reached via RHC or browser):

1. In the Robot Controller Console, open the menu button (upper right) and select **Manage**.
2. On the Manage page you can change: Control Hub name, password, Wi-Fi band, and channel. Change only what you need — leaving band/channel at default and applying just name/password is fine.
3. Select **Apply Wi-Fi Settings** when done.
4. Reconnect to the new network afterward. If connected via USB, RHC stays connected but may need to be closed/reopened to reflect changes.

Recommended FTC naming convention: `<team-number>-RC` (e.g. `99999-RC`).

## Managing Wi-Fi on the Control Hub

Settings are also reachable via the Driver Station application (**Program & Manage** in its menu) — useful at events where field techs request a band/channel change.

### Wi-Fi Reset (User Button)

If you can't reconnect after switching to 5 GHz, perform a physical Wi-Fi factory reset (resets SSID/password to default and band to 2.4 GHz):

1. Press and hold the Control Hub's user button (under the LED, right side of device).
2. While holding, power on the Control Hub.
3. Release when the LED flashes through multiple colors; the Control Hub is ready to connect once it flashes blue then green. Takes several minutes.

### Changing Wi-Fi Band (User Button, OS 1.1.2+)

Switches band only, without needing RHC or the console:

1. Power on the Control Hub (holding the button as it boots).
2. After it's fully booted (LED solid green), press and hold the button again.
3. Release when the LED flashes **magenta** (switched to 5 GHz) or **yellow** (switched to 2.4 GHz). The most recently used channel on that band is applied (default: auto).

## Connecting a Driver Station to the Control Hub

Pairing only needs to be done once per hardware pair; repeat if either device is replaced.

1. Power on the Control Hub; ready to pair once LED is green.
2. **Driver Hub:** Open Driver Station app → menu (three dots) → **Settings** → **Pair with Robot Controller** → **Wi-Fi Settings** → select the Control Hub's SSID (`FIRST-`/`FTC-` prefix) → enter password (default `password`) → **CONNECT**. After a few seconds the Driver Station shows network name, ping, and battery voltage.
3. **Other supported Android Driver Station:** app menu → **Settings** → **Pairing Method** → **Control Hub** → **Pair with Robot Controller** → **Wifi Settings** → select SSID → enter password → **CONNECT**.

## Wiring and Next Steps

Wiring best practices: use appropriately sized cables (route neatly if longer than needed), manage cables with zip ties/Velcro, keep cables clear of moving mechanisms (drivetrain, arms), label wires by function, and "smart tug" every connection before each practice/match to verify it's seated.

**Hardware mapping** — before programming, the Control Hub needs to know what's plugged into which port. This is a two-part process:
1. Create a configuration file (via the Driver Station app) naming each device with a port, device type, and unique name.
2. Reference that name via `hardwareMap` in your OpMode (Blocks handles this step for you; OnBot Java requires you to call `hardwareMap` yourself).

See the OnBot Java / Blocks programming guides and the device-configuration reference in this directory for the full configuration walkthrough.

**Adding an Expansion Hub** adds a full second set of ports (4 more motor, 6 more servo, all sensor ports). See `expansion-hub-and-device-configuration.md` in this directory.

## Slim Battery (REV-31-1302) Best Practices

* Charge rate: 1.5 A min, 3.0 A max, 1.8–2.0 A recommended.
* Don't overcharge — disconnect once full; typical charge time is under 2 hours; don't charge a battery that hasn't discharged meaningfully.
* Minimum no-load voltage: 9.0 V. Discharging past this can permanently damage cells. Brief dips under load are fine; don't run the robot until it stops responding, and unplug promptly after use.
* Let the battery cool before/after charging; mild warmth after heavy use or charging is normal.

## Updating Firmware (Control Hub + Expansion Hub)

The Control Hub contains an internal Expansion Hub board plus an Android controller. REV periodically releases firmware updates for the Expansion Hub portion — both standalone Expansion Hub and Control Hub users need to update it.

### Using REV Hardware Client (recommended)

**Control Hub:** requires RC app 5.5+ first (close/reopen RHC after updating the RC app if needed). Power on, connect via USB-C, select the Control Hub in RHC's Hardware Tab → **Update** tab → under **Hub Firmware** select **Download**, then **Update**. Status changes to "Up-to-Date" on success.

**Expansion Hub** (standalone): connect via USB-A to Mini-USB. Same Download → Update flow under **Hub Firmware** in RHC.

### Using the Robot Controller Console

Download the firmware `.bin` from REV's site, then:

1. Connect via Wi-Fi (see [connecting to the console](#connecting-to-the-robot-controller-console)) and open the console in a browser.
2. **Manage** tab → scroll to **Update REV Hub Firmware**. Use the bundled version shown, or click **Select Firmware…** to pick a downloaded file. Selected files are stored on-device at `FIRST/updates/Expansion Hub Firmware`.
3. Click **Update to…** / **Update using…**, then confirm with **Update Hub Firmware**.
4. Do not unplug the Hub or restart the robot during the update.

**Standalone Expansion Hub via Robot Controller Console:** must connect via USB-A to USB Mini cable — **never have USB and RS485 connected to the Expansion Hub at the same time**. Same Manage-tab flow as above; the console will show both Control Hub and Expansion Hub firmware versions to confirm before updating.

## Updating the Control Hub Operating System

Recommended: REV Hardware Client (auto-detects out-of-date OS, downloads, installs). Alternative: Robot Controller Console with a manually downloaded OS zip.

Applies to REV-31-1595 hubs; contact REV support for the older REV-31-1152 (Control Hub v0).

**Via RHC:** power on and connect over USB-C → select Control Hub in Hardware Tab → Update tab → under **Control Hub Operating System** select **Download**, then **Update**. Keep the hub powered throughout upload and install; it reboots to finish. Status message: "Operating System update complete."

**Via Robot Controller Console:** connect over Wi-Fi to the hub's SSID → browse to `192.168.43.1:8080` → **Manage** tab → **Select Update File** → choose the downloaded OS zip → **Update & Reboot**. Keep the hub powered through upload and reboot; reconnect afterward to verify.

Important OS 1.1.2+ behavior: updating from 1.1.1 or earlier switches the Control Hub to the 5 GHz band regardless of prior setting. Devices that only support 2.4 GHz will not be able to connect wirelessly until you [switch the band back](#changing-wi-fi-band-user-button-os-112) via the user button or Wi-Fi settings.

## Updating the Robot Controller (RC) Application

If you update the RC app, update the Driver Station app to the matching version.

**Via RHC:** connect Control Hub over USB-C → Hardware Tab → Update tab → under **Robot Controller App** select **Download**, then **Update**. Status message: "Robot Controller app update complete."

**Via Robot Controller Console:** download the latest `FtcRobotController-release.apk` from the [FIRST-Tech-Challenge/FtcRobotController GitHub releases](https://github.com/FIRST-Tech-Challenge/FtcRobotController). On the **Manage** page, **Select App** → choose the downloaded APK → **Update**. If the new APK's digital signature differs from what's installed (e.g. previously built via Android Studio, now installing a GitHub release), the hub will prompt to uninstall the old app first — confirm with **OK**. Note: this uninstall step resets the Control Hub's network name/password to factory defaults, requiring reconnection with default credentials.

**Via Android Studio:** fork/clone the [FtcRobotController repo](https://github.com/FIRST-Tech-Challenge/FtcRobotController) and deploy directly; see the [FTC Android Studio tutorial](https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.html) for setup.

## Updating the Driver Hub

Two updatable pieces: Driver Hub OS and the Driver Station app.

**Via the Driver Hub's own Software Manager app:** open it, press **Update All**. Requires the Driver Hub to have internet-connected Wi-Fi. Can take several minutes — keep it charged or plugged in.

**Via REV Hardware Client:** connect the Driver Hub over USB-C → select it in the Hardware Tab → Update tab shows any Out-of-Date items → **Update** downloads and installs each.

## Deploying Code Wirelessly via Android Studio (Wireless ADB)

Android Studio uses ADB (Android Debug Bridge) to build and install the RC app onto the Control Hub. By default this is over USB; the Control Hub also supports wireless ADB on port 5555.

**Setup via REV Hardware Client** (requires Android Studio + RHC on the same PC):

1. Power on the Control Hub (ready when LED turns green).
2. Connect the PC to the Control Hub's Wi-Fi network (connect via USB to RHC first if the password needs resetting).
3. Open RHC and confirm the Control Hub shows as connected over Wi-Fi.
4. The Control Hub should now appear in Android Studio's device dropdown.

## Accessing and Downloading Log Files

Log files (Robot Controller log, Wi-Fi log, Updater log, plus XML configuration files) help diagnose Control Hub/Expansion Hub issues. See `troubleshooting.md` in this directory for interpreting log content (error/warning/info/fatal/debug/verbose categories).

**Log Viewer (RHC):** Utilities Tab → select a connected device's logs or logs downloaded to the PC, then filter/search by tag.

**Sending diagnostics to REV Support (RHC):** connect the Control Hub over USB-C → select it → **Send Diagnostics to REV** button → fill out the short form. This is the preferred path when working with REV support.

**Manual file access (PC):** connect via USB-C, browse to `This PC\Control Hub v1.0\Internal shared storage`. Robot Controller, Wi-Fi, and Updater logs live at that level; a `FIRST` folder holds XML files named after your robot configurations.

**Manual file access (Mac):** Macs don't support MTP natively — install the [Android File Transfer](https://www.android.com/filetransfer/) app first, then browse to the same `Internal shared storage` location.

**Via Robot Controller Console:** **Manage** page → **Download Logs** button → retrieves `robotControllerLog.txt` to the PC's Downloads folder; open with a text editor (e.g. Notepad++).

## REV Hardware Client — Feature Summary

* Auto-detects supported devices over USB; can also connect a Control Hub over Wi-Fi.
* One-click update of all software on all connected devices.
* Pre-download software updates without a device connected.
* Back up/restore user data (config files, Blocks/Java code) from the Control Hub.
* Install/switch between DS and RC apps on Android devices.
* Access to the Robot Controller Console.
* Self-updates; displays devices connected via RS485.

Supported devices: REV Control Hub (REV-31-1595), REV Expansion Hub (REV-31-1153), REV Driver Hub (REV-31-1596), REV Servo Hub (REV-11-1855), and any Android device via ADB. (REV ION/FRC hardware on REVLib 2026+ must use the newer REV Hardware Client 2 instead — not covered here, as it targets FRC.)
