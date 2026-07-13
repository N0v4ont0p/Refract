> Source: https://ftc-docs.firstinspires.org/en/latest/control_hard_compon/index.html · Fetched: 2026-07-12
> Source: https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/index.html · Fetched: 2026-07-12
> Source: https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/myblocks/hardware_example/hardware-example.html · Fetched: 2026-07-12

# Hardware Map and Device Configuration

## Control System Architecture

The _FIRST_ Tech Challenge Control System comprises two primary divisions: the Driver Station (DS) and the Robot Controller (RC).

**Driver Station** covers Driver Station Components.

**Robot Controller** covers:
- Power Distribution
- REV Hubs
- Motors
- Encoders (Rotation Counters)
- Servos
- Sensors
- UVC Webcam

## Configuring Your Hardware

Configuration covers setting up control system hardware for use in an FTC project:

- **Motors & Actuators** — setting up DC motors and servo systems.
- **Sensors** — color/distance sensors and digital touch sensors.
- **Cameras** — external webcams, UVC cameras, and display/preview options.
- **Expansion** — adding secondary expansion hubs to the control system to expand available motor/sensor ports beyond a single control hub's capacity.
- **Configuration management** — saving the hardware configuration so it persists across robot sessions.

Sections are organized as: Getting Started (foundational guidance on creating an initial hardware configuration) → Device-Specific Configuration (per-device setup for DC motors, servos, sensor types) → Camera Options (connecting external cameras via USB/powered hubs, monitoring feeds via image preview or screencasting) → Multi-Hub Setup (connecting expansion hubs) → Configuration Storage (saving the hardware map).

## Accessing Configured Hardware via `hardwareMap`

Once a device is named in the robot configuration file, code retrieves it through the `hardwareMap` object. Example — a Blocks "myBlock" that wiggles a named servo:

```java
package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion;
import org.firstinspires.ftc.robotcore.external.ExportToBlocks;
import com.qualcomm.robotcore.hardware.Servo;

public class SampleMyBlocks_v01 extends BlocksOpModeCompanion {

    @ExportToBlocks (
    comment = "Move a conventional servo back and forth. Assumes servo starts" +
              " from position 0. Servo name must be in the active configuration.",
    tooltip = "Wiggle a user-designated servo.",
    parameterLabels = {"Servo name", "Duration (milliseconds)", "Number of cycles"}
    )
    public static void wiggleServo (String servoName, int duration, int cycles) {

        Servo myServo = hardwareMap.get(Servo.class, servoName);

        for (int i = 0; i < cycles && linearOpMode.opModeIsActive(); i++)  {
        
            myServo.setPosition(0.5);
            linearOpMode.sleep(duration);
            myServo.setPosition(0);
            linearOpMode.sleep(duration);
        }
    }
}
```

**Key technical points:**
- `Servo myServo = hardwareMap.get(Servo.class, servoName);` does three things at once: declares a `Servo` variable, retrieves the named device from the configured devices list, and assigns it to the new variable.
- Loop control monitors `opModeIsActive()` (via `linearOpMode`) so the loop stops if the OpMode is stopped mid-cycle.
- Device methods (`setPosition()`) come from the `Servo` class; `sleep()` comes from `linearOpMode`, one of the objects inherited through `BlocksOpModeCompanion`.

**Hard-coded vs. parameterized device names:**
- Hard-coding the device name makes the myBlock simpler and needs no user input, but requires knowing the exact name in advance and breaks if the configuration changes.
- Taking the device name as a parameter requires the user to enter the exact name from the active configuration (visible in the Configure Robot menu or Blocks drop-down lists), but survives configuration changes.

A more complete example in the source page uses five of the six `BlocksOpModeCompanion` objects — `linearOpMode`, `hardwareMap`, `telemetry`, `gamepad1`, and `gamepad2` — adding telemetry progress updates and gamepad-gated start.
