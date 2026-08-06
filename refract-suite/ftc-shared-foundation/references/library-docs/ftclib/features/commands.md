> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/features/commands.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.command
---

# Commands

The FTCLib provides a Command-based OpMode to define your robot's `OpMode` routine. Instead of hard-coding instructions in your OpMode, you can leverage the reusability of the `CommandOpMode` structure to predefined `Command` routines and run them sequentially. You can also set timeouts for a `Command` to automatically terminate a running command.

## Subsystem

Defines an organized module on your robot. One such example is a linear slide lift powered by a motor connected to a spool, additionally using encoders or touch/magnetic sensors to act as limit switches, preventing the lift from exceeding its bounds. In this example, the motor, its encoder, and any sensors used would fall under a single "Lift" Subsystem.

A Subsystem has five lifecycle phases:

* `initialize()`: Prepares the physical hardware for activation of the Subsystem. This phase is intended to be used for hardware map initialization, zeroing of encoders \(as required\), and gathering any initially required sensor data.
* `reset()`: Returns the Subsystem back to its original state. This phase is distinct from `initialize()` as it is expected that the hardware map is already initialized. This phase is intended to return Subsystem hardware to its original condition and clear saved data.
* `loop()`: This is the main lifecycle phase of a Subsystem. This is where [Commands ](commands.md#command)could be issued to the Subsystem, or user/sensor input is used to operate the Subsystem. This phase is intended to repeatedly loop until `stop()` is called.
* `stop()`: Halts all action of the Subsystem, bringing all hardware devices to stop. It is recommended to set the Zero Power Behavior of Motors to `BRAKE` in this phase, as motion is designed to entirely cease. A Subsystem should be designed to enable a `reset()` from this phase to return it to normal operation.
* `disable()`: Deactivates the Subsystem, rendering it unusable until the next `initialize()`. It is recommended to set the Zero Power Behavior of Motors to `FLOAT` in this phase, as Subsystem will no longer be receiving input. A Subsystem should _NOT_ be designed to enable `reset()`, `initialize()` is required.

## Command

Defines a single, executable command. A Command defines the actions of multiples parts \(or [`Subsystem`](commands.md#subsystem)\) of the robot to take at once. A Command has three lifecycle phases:

* `initialize()`: The initial subroutine of a Command. Called once when the Command is initially scheduled.
* `execute()`: The main body of a Command. Called repeatedly while the Command is scheduled.
* `end()`: The action to take once the Command is completed. Called once on the Command's completion.

`Command` also provides a `isFinished()` method which returns `true` if the Command has completed and `false` otherwise. Note: `end()` will always run after the Command is unscheduled. You do not need to check if the Command `isFinished()` to run your own `end()` method.

## CommandOpMode

Defines an `OpMode` which is designed to run on [Commands](commands.md#command) as opposed to manual method calls. Before using a CommandOpMode, Commands and [Subsystems](commands.md#subsystem) need to be defined. CommandOpMode runs an internal `ElapsedTimer` which ensures Commands terminate after their specified timeouts.

Although CommandOpMode extends `LinearOpMode` , it is not required to use any of the methods provided explicitly. These methods are all called internally by `runOpMode()` \(it is not necessary to override this method within your own extension of CommandOpMode\) within the three lifecycle phases of a CommandOpMode \(it _is_ required to override these methods\):

* `initialize()`: Sets up and calls `initialize()` of all attached Subsystems and Commands. It is vital to setup Subsystems before their Commands, as doing the reverse could likely raise NullPointerExceptions. 
* `initLoop()`: Called repeatedly after `initialize()` but before the user presses "Play" on the Driver Station
* `run()`: The main loop of a CommandOpMode. Called immediately after the user presses the "Play" button on the Driver Station.

Internally, these three lifecycle phases are tied together under an override of the `runOpMode()` method of `LinearOpMode`:

```java
@Override
public void runOpMode() throws InterruptedException {
    commandTimer = new ElapsedTime();
    initialize();
    while(!isStopRequested() && !isStarted()) { // Runs after "Init" 
        initLoop();                             // but before "Play"
    }
    run();
}
```

Once the user defines Commands, Subsystems, and the three lifecycle phases, the user can add Commands to the workflow using `addSequential()`. `addSequential()` adds a Command to be run within a certain specified timeout. The user can also optionally set a custom loop interval time \(which defaults to 20 ms\). `addSequential()` first initializes its passed-in Command, runs it every 20 ms \(terminating if it reaches its timeout\), and checks if the Command `isFinished()`. If true, the Command will exit the loop and run its `end()` lifecycle method.

