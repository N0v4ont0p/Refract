> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/command-base/command-system/robot-and-commandopmode.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: Organizing your code with the Robot class and CommandOpMode.
---

# Robot and CommandOpMode

**NOTE**: We recommend using the [CommandOpMode](robot-and-commandopmode.md#commandopmode) for your implementation of the command-based paradigm as it is much friendlier for FTC programs.

## The Robot Class

The [Robot](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/command/Robot.java) class makes using the CommandScheduler so much simpler in the user's code. Similar to WPILib, the Robot class allows for making a Robot paradigm. This allows for the creation of multiple opmodes tied to one object. This is also the basis for disabling the robot, meaning we want to interrupt the commands and not allow for scheduling new ones. This is done with the static `disable()` and `enable()` methods:

```java
// disable the Robot
Robot.disable();

// enable the Robot
Robot.enable();
```

### Creating a Robot Class

The first step in using the Robot paradigm is to create your own Robot subclass. This will maintain all of the commands and subsystems you want to utilize. Also note that you can schedule and register new commands and subsystems from outside the Robot class using the `schedule()` and `register()` methods.

A major downside of the Robot class is that it shares the common commands and subsystems for every use in the OpModes. A recommendation is to create an [enum](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) inside of your robot implementation that specifies TeleOp versus Autonomous so that when the object is constructed, it uses the desired CommandScheduler instance.

Below is an example of utilizing this feature.

```java
// ... in MyRobot.java (extends Robot)

// enum to specify opmode type
public enum OpModeType {
    TELEOP, AUTO
}

// the constructor with a specified opmode type
public MyRobot(OpModeType type) {
    if (type == OpModeType.TELEOP) {
        initTele();
    } else {
        initAuto();
    }
}

/*
 * Initialize teleop or autonomous, depending on which is used
 */
public void initTele() {
    // initialize teleop-specific scheduler
}

public void initAuto() {
    // initialize auto-specific scheduler
}


// ... in your opmode

// our robot object
Robot m_robot = new MyRobot(MyRobot.OpModeType.TELEOP);
```

A downside that cannot be fixed by this is when you want to run several different opmodes of the different types with respect to the same subsystems. This is where the [CommandOpMode](robot-and-commandopmode.md#commandopmode) comes in handy and makes the paradigm a lot more FTC-friendly.

### Running the Robot in Your OpMode

Running the robot in the opmode is simple and only requires a few lines of code and making a call to the `run()` method.

```java
// assumes we have created an enum called OpModeType as seen
// in the previous section
Robot m_robot = new MyRobot(MyRobot.OpModeType.AUTO);

// run the command scheduler tied to that robot instance
while (opModeIsActive() && !isStopRequested()) {
    m_robot.run();
}
m_robot.reset();    // resets the scheduler instance
```

## CommandOpMode

The [CommandOpMode](https://github.com/FTCLib/FTCLib/blob/v2.1.1/core/src/main/java/com/arcrobotics/ftclib/command/CommandOpMode.java) is the center of the FTC-centric command-based paradigm. It makes everything simpler for the user and greatly decreases the amount of code needed to run everything. Unlike the Robot class, it is opmode-specific, so it does not store a common reference to subsystems. If desired, the user can create a map that houses all of the referenced hardware, but this is currently not a feature offered \(but totally supported\) by FTCLib.

If desired, the user can override the methods from the CommandOpMode. Similarly to the Robot class, you can disable the CommandOpMode with static methods \(which actually disable the Robot class, which is what is referenced in the CommandScheduler for `runsWhenDisabled()` commands.

### Initializing your Hardware

CommandOpMode is an abstract class, which means the user must create their own implementation of it. The only method that needs to be implemented is the `initialize()` method, which instantiates all of the hardware and commands to be run by the scheduler. The CommandOpMode class already implements the `runOpMode()` method and runs the scheduler. After the opmode is no longer active or a stop is requested, it resets the instance of the scheduler so a new opmode can be run with a fresh instance. This is very nonintuitive, but it works as designed \(setting the singleton instance to null, where a new instance is then created upon calling `getInstance()`.

```java
// in your implementation of CommandOpMode

@Override
public void initialize() {
    // iniialize hardware

    // schedule all commands
    schedule(commands...);
    // register unregistered subsystems
    register(subsystems...);
}
```

That is functionally all that needs to be done, everything else is done for the user internally. You can find a sample project utilizing CommandOpMode [here](https://github.com/FTCLib/FTCLib/blob/v2.1.1/examples/src/main/java/com/example/ftclibexamples/PurePursuitSample.java).

