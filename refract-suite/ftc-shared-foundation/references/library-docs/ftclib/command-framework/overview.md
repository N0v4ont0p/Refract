> Source: https://raw.githubusercontent.com/FTCLib/FTCLib-Docs/v2.1.0/command-base/command-system/README.md · Fetched: 2026-07-12
> Note: docs.ftclib.org (GitBook) returned HTTP 403 to automated fetch tools; content below is pulled from the FTCLib-Docs GitHub source at tag v2.1.0 (the same version live at https://docs.ftclib.org/ftclib/command-base/command-system), which is the exact markdown GitBook renders for that page.

# Command System

The current command system for FTCLib is modeled closely after that of [WPILib](https://docs.wpilib.org/en/latest/docs/software/commandbased/index.html). Some of the following information may be copied from the source material.

The command-based paradigm is one that allows programming to follow a set design pattern. The specific command system that FTCLib uses follows a declarative programming style. The emphasis is, instead, on what the program _should_ do rather than how to do it. This minimizes the iteration-by-iteration robot logic needed to write out a certain action. Very simply, you can bind some actions to buttons/triggers such as the example below:

```java
aButton.whenPressed(intake::run);
```

Or, instead of binding to a button, you can simply schedule an action to occur by registering it.

## Terminology

Let's discuss some of the basic terminology for the paradigm.

### Subsystem

A **subsystem** is the basic unit of robot organization in the design-based paradigm. Subsystems [encapsulate](https://en.wikipedia.org/wiki/Encapsulation_%28computer_programming%29) lower-level robot hardware (such as motor controllers, sensors, and/or pneumatic actuators), and define the interfaces through which that hardware can be accessed by the rest of the robot code. Subsystems allow users to “hide” the internal complexity of their actual hardware from the rest of their code - this both simplifies the rest of the robot code, and allows changes to the internal details of a subsystem without also changing the rest of the robot code. Subsystems implement the `Subsystem` interface.

### Command

A **command** defines high-level robot actions or behaviors that utilize the methods defined by the subsystems. A command is a simple [state machine](https://en.wikipedia.org/wiki/Finite-state_machine) that is either initializing, executing, ending, or idle. Users write code specifying which action should be taken in each state. Simple commands can be composed into “command groups” to accomplish more-complicated tasks. Commands, including command groups, implement the `Command` interface.

#### How Commands Are Run

For a more detailed explanation, please see the [Command Scheduler](command-scheduler.md).

Commands are run by the `CommandScheduler`, which is a singleton at the base of the command system. The command scheduler is in charge of polling buttons for new commands to schedule, checking the resources required by those commands to avoid conflicts, executing currently-scheduled commands, and removing commands that have finished or been interrupted. The scheduler’s `run()` method may be called from any place in the user’s code.

Multiple commands can run concurrently, as long as they do not require the same resources on the robot. Resource management is handled on a per-subsystem basis: commands may specify which subsystems they interact with, and the scheduler will never schedule more than one command requiring a given subsystem at a time. This ensures that, for example, users will not end up with two different pieces of code attempting to set the same motor controller to different output values. If a new command is scheduled that requires a subsystem that is already in use, it will either interrupt the currently-running command that requires that subsystem (if the command has been scheduled as interruptible), or else it will not be scheduled.

Subsystems also can be associated with “default commands” that will be automatically scheduled when no other command is currently using the subsystem. This is useful for continuous “background” actions such as controlling the robot drive, or keeping an arm held at a setpoint.

When a command is scheduled, its `initialize()` method is called once. Its `execute()` method is then called once per call to `CommandScheduler.getInstance().run()`. A command is unscheduled and has its `end(boolean interrupted)` method called when either its `isFinished()` method returns true, or else it is interrupted (either by another command with which it shares a required subsystem, or by being canceled).

#### Command Groups

It is often desirable to build complex commands from simple pieces. This is achievable by [composing](https://en.wikipedia.org/wiki/Object_composition) commands into “command groups.” A [command group](command-groups.md) is a command that contains multiple commands within it, which run either in parallel or in sequence. The command-based library provides several types of command groups for teams to use, and users are encouraged to write their own, if desired. As command groups themselves implement the `Command` interface, they are [recursively composable](https://en.wikipedia.org/wiki/Object_composition#Recursive_composition) - one can include command groups _within_ other command groups. This provides an extremely powerful way of building complex robot actions with a simple library.
