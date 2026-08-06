> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/command-base/command-system/subsystems.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.command.Subsystem
---

# Subsystems

Subsystems are the basic unit of robot organization in the command-based paradigm. A subsystem is an abstraction for a collection of robot hardware that _operates together as a unit_. Subsystems [encapsulate](https://en.wikipedia.org/wiki/Encapsulation_%28computer_programming%29) this hardware, “hiding” it from the rest of the robot code \(e.g. commands\) and restricting access to it except through the subsystem’s public methods. Restricting the access in this way provides a single convenient place for code that might otherwise be duplicated in multiple places \(such as scaling motor outputs or checking limit switches\) if the subsystem internals were exposed. It also allows changes to the specific details of how the subsystem works \(the “implementation”\) to be isolated from the rest of robot code, making it far easier to make substantial changes if/when the design constraints change.

Subsystems also serve as the backbone of the `CommandScheduler`’s resource management system. Commands may declare resource requirements by specifying which subsystems they interact with; the scheduler will never concurrently schedule more than one command that requires a given subsystem. An attempt to schedule a command that requires a subsystem that is already-in-use will either interrupt the currently-running command \(if the command has been scheduled as interruptible\), or else be ignored.

Subsystems can be associated with “default commands” that will be automatically scheduled when no other command is currently using the subsystem. This is useful for continuous “background” actions such as controlling the robot drive, or keeping an arm held at a setpoint. Similar functionality can be achieved in the subsystem’s `periodic()` method, which is run once per run of the scheduler; teams should try to be consistent within their codebase about which functionality is achieved through either of these methods. Subsystems are represented in the command-based library by the Subsystem interface.

## Creating a Subsystem

The recommended method to create a subsystem for most users is to subclass the abstract `SubsystemBase` class, as seen in the command-based template:

```java
import com.arcrobotics.ftclib.command.SubsystemBase;

public class ExampleSubsystem extends SubsystemBase {
  /**
   * Creates a new ExampleSubsystem.
   */
  public ExampleSubsystem() {

  }

  @Override
  public void periodic() {
    // This method will be called once per scheduler run
  }
}
```

This class contains automatically calls the `register()` method in its constructor to register the subsystem with the scheduler \(this is necessary for the `periodic()` method to be called when the scheduler runs\).

Advanced users seeking more flexibility may simply create a class that implements the `Subsystem` interface.

## Creating a Simple Subsystem

Subsystems are easy to create. They combine different sets of hardware to produce either multiple or one particular task. Hence why they are the basic unit of organization in the command system. Below is a simple example:

```java
package org.firstinspires.ftc.robotcontroller.external.samples.CommandSample;

import com.arcrobotics.ftclib2.command.SubsystemBase;
import com.qualcomm.robotcore.hardware.HardwareMap;
import com.qualcomm.robotcore.hardware.Servo;

/**
 * A gripper mechanism that grabs a stone from the quarry.
 * Centered around the Skystone game for FTC that was done in the 2019
 * to 2020 season.
 */
public class GripperSubsystem extends SubsystemBase {

    private final Servo mechRotation;

    public GripperSubsystem(final HardwareMap hMap, final String name) {
        mechRotation = hMap.get(Servo.class, name);
    }

    /**
     * Grabs a stone.
     */
    public void grab() {
        mechRotation.setPosition(0.76);
    }

    /**
     * Releases a stone.
     */
    public void release() {
        mechRotation.setPosition(0);
    }

}
```

## Setting Default Commands

“Default commands” are commands that run automatically whenever a subsystem is not being used by another command.

Setting a default command for a subsystem is very easy; one simply calls `CommandScheduler.getInstance().setDefaultCommand()`, or, more simply, the `setDefaultCommand()` method of the `Subsystem` interface which can be called in the OpMode:

```java
CommandScheduler.getInstance().setDefaultCommand(exampleSubsystem, exampleCommand);
```

```java
exampleSubsystem.setDefaultCommand(exampleCommand);
```

