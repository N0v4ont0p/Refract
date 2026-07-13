> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/welcome · Fetched: 2026-07-12

# OnBot Java Programming Guide

Covers what OnBot Java is, how to access it on the Control Hub, what an OpMode is, the OnBot Java editor interface, creating a new OpMode, and core programming essentials (hardwareMap, the OpMode lifecycle, comments, common errors).

Synthesized from these pages under `docs.revrobotics.com/duo-control/hello-robot-java/`: `welcome`, `where-to-program`, `where-to-program/what-is-an-opmode`, `part-1/onbot`, `part-1/test-bed-onbot-java`, `part-1/programming-essentials`.

## What OnBot Java Is

OnBot Java is a text-based programming tool based on a modified version of Java that is accessible directly through the Control Hub. It targets programmers with basic to advanced Java skills who want to write text-based OpModes.

REV's programming tools form a tier of increasing complexity/capability:

* **Blocks** — visual drag-and-drop, hides SDK internals.
* **OnBot Java** — text-based; requires direct calls to SDK classes like `hardwareMap`, which stay hidden inside Blocks snippets.
* **Android Studio** — full professional IDE, most capability, most setup.

OnBot Java is accessible directly through the Control Hub (via browser or the REV Hardware Client) — no separate IDE installation required, unlike Android Studio.

## Accessing OnBot Java

Two ways to reach the Robot Controller Console and its OnBot Java editor:

**1. REV Hardware Client (Windows only)**
Install the latest REV Hardware Client on Windows 10+. Power the Control Hub from a 12V battery, connect it to the computer via USB-A to USB-C, launch the app, select the hub once it appears under the Hardware tab, then open "Program and Manage" to reach the Robot Controller Console.

**2. Web browser (cross-platform)**
Use this on Chromebooks, MacBooks, or any machine that can't install the Hardware Client. Connect the device's Wi-Fi to the Control Hub's own network (case-sensitive password), then browse to:

```
192.168.43.1:8080
```

in Chrome, Firefox, or Internet Explorer. Note: while connected to the Control Hub's Wi-Fi, the device loses Internet access — it only reaches the Hub.

Either path lands on the Robot Controller Console homepage, which has **Blocks**, **OnBot Java**, and **Manage** (network configuration) in its toolbar.

## What an OpMode Is

OpModes (operational modes) are the programs that define robot behavior. The Robot Controller (on the Control Hub) executes them; the Driver Hub starts, stops, and initializes them.

Two types:

* **Autonomous (Auto)** — runs with no gamepad input, under a 30-second countdown (toggleable for testing) that auto-stops the OpMode at zero.
* **TeleOp** — manual gamepad control, stoppable at any time.

The Driver Hub shows a green left arrow for Autonomous OpModes and a blue right arrow for TeleOp. Both types support init/start/stop through the Driver Hub. When creating a file in OnBot Java you pick the OpMode type at creation time — RC app 10.2 and earlier use one creation-menu layout, 10.3+ uses an updated one that can auto-detect type when starting from sample code.

## The OnBot Java Editor

The editor (whether reached via browser or REV Hardware Client) has:

* **Create New OpMode button** (+) — starts the new-file flow.
* **Project Browser Pane** — lists your Java project files.
* **Source Code Editing Pane** — where you write code.
* **Message Pane** — build success/failure and compiler errors.
* **Build Everything button** — compiles all `.java` files in the project.

## Creating a New OpMode

Name the OpMode following normal Java class-naming convention (capitalize the first letter of each word) — pick something meaningful to you or your team (your name, team name, class period, etc.), and make sure it doesn't collide with any variable name you'll use.

**RC app pre-10.3:**
- File Name: e.g. `HelloRobot_TeleOp`
- Sample: `BlankLinearOpMode`
- OpMode Type: TeleOp (or Autonomous)
- Setup Code for Configured Hardware: enabled — lets OnBot Java auto-generate the `hardwareMap` calls based on your active robot configuration.

**RC app 10.3+:**
- File Location: `org/firstinspires/ftc/teamcode`
- File Type: Blank OpMode - Linear OpMode
- File Name: e.g. `HelloRobot_TeleOp.java`
- OpMode Type: TeleOp (or Autonomous)
- "Add generated code for configured hardware": enabled

Known bug in v10.3: the configured-hardware code generation doesn't always fire, so you may need to add the `hardwareMap` lines by hand.

To start from an existing sample instead of a blank template, switch File Type to "Example OpMode" and pick one from the dropdown.

**Workflow tip:** if you have an incomplete/broken file that isn't ready to compile, right-click its name in the Project Browser and choose Disable/Comment so "Build Everything" doesn't fail on it.

## Programming Essentials

The `BlankLinearOpMode` template is the structural shell every Linear OpMode starts from:

**hardwareMap (declare hardware, runs after Init, before Play)**

```java
control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
test_motor  = hardwareMap.get(DcMotor.class, "test_motor");
test_servo  = hardwareMap.get(Servo.class, "test_servo");
test_touch  = hardwareMap.get(TouchSensor.class, "test_touch");
```

This is also where you set variables, motor directions, and initial servo positions — it all runs once, between pressing Init and pressing Play.

**waitForStart()**

Code placed between `waitForStart()` and the main loop runs exactly once, right when Play is pressed — good for resetting timers or other one-time setup that needs the match clock, not just Init.

**opModeIsActive() loop (the main program)**

```java
while (opModeIsActive()) {
    telemetry.addData("Status", "Running");
    telemetry.update();
}
```

This loop repeats continuously until Stop is pressed — the bulk of your OpMode's logic lives here.

**Comments**

`//` starts a single-line comment. Use them to document intent or to temporarily disable a line — "the robot will not read comments."

**Common errors**

* **Mismatched brackets** — OnBot Java underlines errors in red, but the reported line can be wrong; check every opening/closing brace in scope, not just the flagged line.
* **Class/filename mismatch** — the `public class` name must match the file name exactly, including case. Rename via right-click in the Project Browser (keep the `.java` extension).
