> Source: https://raw.githubusercontent.com/FTCLib/FTCLib-Docs/v2.1.0/command-base/command-system/convenience-commands.md · Fetched: 2026-07-12
> Note: docs.ftclib.org (GitBook) returned HTTP 403 to automated fetch tools; content below is pulled from the FTCLib-Docs GitHub source at tag v2.1.0 (the same version live at https://docs.ftclib.org/ftclib/command-base/command-system/convenience-commands), which is the exact markdown GitBook renders for that page.

# Convenience Features

FTCLib offers convenience features to make your paradigm program more compact. The idea is that it improves the overall structure of your program. Some of these convenience commands are just that: for convenience. This does not mean they are exceptional. Plenty are simplified for minimal competitive use, such as the `PurePursuitCommand` (see FTCLib's Pathing / Pure Pursuit docs, not included in this reference set).

## Framework Commands

Framework commands exist to decrease the amount of program needed for simplistic tasks, like updating a number. Rather than having the user create an entire command for one simplistic task (which when done for multiple menial tasks builds up and makes the structure fairly disheveled), the user can utilize framework commands.

### InstantCommand

`InstantCommand` is a versatile framework command that on initialization runs some task and then ends on that same iteration of the CommandScheduler's `run()` method. This is especially useful for button-triggered events.

```java
GamepadEx toolOp = new GamepadEx(gamepad2);

toolOp.getGamepadButton(GamepadKeys.Button.A)
    .whenPressed(new InstantCommand(() -> {
        // your implementation of run() here
    }));

/* AN EXAMPLE */

Motor intakeMotor = new Motor(hardwareMap, "intake");

toolOp.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
    .whileHeld(new InstantCommand(() -> {
        intakeMotor.set(0.75);
    }))
    .whenReleased(new InstantCommand(intakeMotor::stopMotor));
```

You should actually use subsystems here instead of the motor object. That way we can add the subsystem's requirements to the `InstantCommand`. Below is a proper example.

```java
/**
 * This is a pedagogical intake subsystem for
 * a universal intake consisting of one motor
 * that drives a belt that connects to a pulley
 * that drives a PVC tube.
 */
public class Intake extends SubsystemBase {
    private Motor m_intakeMotor;
    
    public Intake(Motor intakeMotor) {
        m_intakeMotor = intakeMotor;
    }
    
    public void run() {
        m_intakeMotor.set(0.75);
    }
    
    public void stop() {
        m_intakeMotor.stopMotor();
    }
}
```

And then we can set up our command bindings as such:

```java
/* in your opmode */

Motor intakeMotor = new Motor(hardwareMap, "intake");
Intake intake = new Intake(intakeMotor);

toolOp.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
    // the second parameter is a varargs of subsystems
    // to require
    .whileHeld(new InstantCommand(intake::run, intake))
    .whenReleased(new InstantCommand(intake::stop, intake));
```

This removes a lot of unnecessary clutter of commands since in a custom implementation the user would have to define a command for both running the intake and stopping it. With `InstantCommand`, the amount of code on the user-side is dramatically reduced.

### RunCommand

As opposed to an `InstantCommand`, a `RunCommand` runs a given method in its execute phase. This is useful for `PerpetualCommand`s, default commands, and simple commands like driving a robot.

```java
/* in your opmode */

Motor intakeMotor = new Motor(hardwareMap, "intake");
Intake intake = new Intake(intakeMotor);

toolOp.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
    // the second parameter is a varargs of subsystems
    // to require
    .whileHeld(new RunCommand(intake::run, intake))
    .whenReleased(new InstantCommand(intake::stop, intake));
    
// say we have a drive subsystem
// with a drive method
schedule(new RunCommand(driveSubsystem::drive, driveSubsystem));
```

### ConditionalCommand

`ConditionalCommand` has a wide variety of uses. `ConditionalCommand` takes two commands and runs one when supplied a value of true, and another when supplied a value of false.

One use is for making a toggle between commands without using the inactive or active states of the `toggleWhenPressed()` binding. Let's update our intake to have two more methods we can use for this toggling feature:

```java
/**
 * This is a pedagogical intake subsystem for
 * a universal intake consisting of one motor
 * that drives a belt that connects to a pulley
 * that drives a PVC tube.
 */
public class Intake extends SubsystemBase {
    private Motor m_intakeMotor;
    private boolean m_active;
    
    public Intake(Motor intakeMotor) {
        m_intakeMotor = intakeMotor;
        m_active = true;
    }
    
    // switch the toggle
    public void toggle() {
        m_active = !m_active;
    }
    
    // return the active state
    public boolean active() {
        return m_active;
    }
    
    public void run() {
        m_intakeMotor.set(0.75);
    }
    
    public void stop() {
        m_intakeMotor.stopMotor();
    }
}
```

We can then use a conditional command in a trigger binding to produce a toggling effect once pressed:

```java
/* in your opmode */

Motor intakeMotor = new Motor(hardwareMap, "intake");
Intake intake = new Intake(intakeMotor);

toolOp.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
    .whenPressed(new ConditionalCommand(
        new InstantCommand(intake::run, intake),
        new InstantCommand(intake::stop, intake),
        () -> {
            intake.toggle();
            return intake.active();
        }
    ));
```

An example of usage could be in Velocity Vortex, where the beacons were either red or blue. Using a color sensor, we can detect the color and then perform some action based on whether it was red or blue.

```java
// pseudocode for instantiating the command
ConditionalCommand pressBeacon = new ConditionalCommand(
    new InstantCommand(beaconPresser::pushRed, beaconPresser),
    new InstantCommand(beaconPresser::pushBlue, beaconPresser),
    () -> vision.output() == BeaconColor.RED
);

pressBeacon.schedule();    // schedule the command

/* This is also useful in sequential command groups */
```

As you can see, conditional commands are very useful for switching between states with a certain state. We will see later that we would want to use a `SelectCommand` when working with several states and not a simple command that switches between two.

### ScheduleCommand

Does exactly as the name suggests: schedules commands. You can input a variable number of command arguments to schedule, and the command will schedule them on initialization. After this, the command will finish. This is useful for forking off of command groups.

So far we've been using the convenience commands we've learned in tandem and how they can be used together to produce more efficient paradigm utility. This is no exception for the `ScheduleCommand`. We can use a conditional command to schedule a desired command.

```java
SequentialCommandGroup auto = new SequentialCommandGroup(
    ...,
    new ConditionalCommand(
        new ScheduleCommand(
            // schedule commands
        ),
        new ScheduleCommand(
            // schedule commands
        ),
        ...    // boolean supplier
    ),
    ...
);
```

It is important to note that the schedule command will finish immediately. Which means any following commands in the sequential command group will be run. The point of the schedule command is to fork off from the command group so that it can be run separately by the scheduler.

### SelectCommand

The select command is similar to a conditional command but for several commands. This is especially useful for a state machine. Let's take a look at the ring stack from the 2020-2021 Ultimate Goal season.

```java
public enum Height {
    ZERO, ONE, FOUR
}

public Height height() {
    // some code to detect height of the starter stack
}

...

SelectCommand wobbleCommand = new SelectCommand(
    // the first parameter is a map of commands
    new HashMap<Object, Command>() {{
        put(Height.ZERO, new new PurePursuitCommand(...)));
        put(Height.ONE, new PurePursuitCommand(...)));
        put(Height.FOUR, new PurePursuitCommand(...)));
    }},
    // the selector
    this::height
);
```

A select command is finished when the selected command also finishes. An alternative use of the select command is to run a command given a supplier instead of a map. Below is a comparable version to the one above:

```java
public enum Height {
    ZERO, ONE, FOUR
}

public Height height() {
    // some code to detect height of the starter stack
}

// returns a command for the wobble goal action
public Command wobbleCommand() {
    Height rings = this.height();
    switch (rings) {
        case Height.ZERO:
            return ...;
        case Height.ONE:
            return ...;
        case Height.FOUR:
            return ...;
    }
}

...

SelectCommand wobbleCommand = new SelectCommand(
    // pass in a command supplier
    this::wobbleCommand
);
```

### PerpetualCommand

As opposed to an instant command, a perpetual command swallows a command and runs it perpetually i.e. it will continue to execute the command passed in as an as argument in the constructor and ignore that command's `isFinished` condition. It can only end if it is interrupted. This makes them useful for default commands, which are interrupted when another command requiring that subsystem is currently being run and is not scheduled again until that command ends.

Let's take a look back at the command bindings for when we learned `InstantCommand`, Instead of doing `whileHeld` and `whenReleased` binding, a more idiomatic method is to use a default command to stop the intake when the button is released instead (which cancels the command once the trigger/button is inactive, allowing the default command to be scheduled).

```java
/* in your opmode */

Motor intakeMotor = new Motor(hardwareMap, "intake");
Intake intake = new Intake(intakeMotor);

toolOp.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
    .whileHeld(new InstantCommand(intake::run, intake));

intake.setDefaultCommand(new PerpetualCommand(stopIntakeCommand));

// this isn't actually needed; really you'd do this:
intake.setDefaultCommand(new RunCommand(intake::stop, intake));
```

Note that a perpetual command adds all the requirements of the swallowed command.

### WaitUntilCommand

A `WaitUntilCommand` is run until the boolean supplied returns true. This is useful for when you have forked off from a command group. Let's expand upon the example from the [`ScheduleCommand`](convenience-features.md#schedulecommand) but with a single schedule command.

```java
SequentialCommandGroup auto = new SequentialCommandGroup(
    ...,
    // schedule the command that forks off from
    // the command group
    new ScheduleCommand(forkedCommand),
    // wait until that command is finished
    new WaitUntilCommand(forkedCommand::isFinished),
    ...    // more commands
);
```

The following commands in the auto command group are only run after that forked command is finished due to that `WaitUntilCommand`.

### StartEndCommand

The `StartEndCommand` is essentially an `InstantCommand` with a custom end function. It takes two `Runnable` parameters an optional varargs of subsystems to require. The first parameter is run on initialize and the second is run on end.

### FunctionalCommand

The last framework command we will discuss is the `FunctionalCommand`. It is useful for doing an inline definition of a complex command instead of creating a new command subclass. Generally, it is better to write a class for anything past a certain complexity.

The `FunctionalCommand` takes four inputs and a variable amount of subsystems for adding requirements. The four inputs determine the initialization, execution, and end actions, followed by the boolean supplier that determines if it is finished.

A good use of this is inside of a sequential command group. Let's use the previous command group and add a functional command.

```java
SequentialCommandGroup auto = new SequentialCommandGroup(
    ...,
    new FunctionalCommand(
        // init actions
        driveSubsystem::resetEncoders,
        // execute actions
        () -> {
            /* list of actions */
            // remember run() returns void
        },
        // end actions
        driveSubsystem::stop,
        // is finished supplier
        () -> {
            /* logic that returns a boolean */
        },
        driveSubsystem,
        ...    // any other required subsystems
    ),
    new ScheduleCommand(forkedCommand),
    new WaitUntilCommand(forkedCommand::isFinished),
    ...
);
```

## Command Decorators

Decorators are methods that allow you to make command bindings and logic without having to create new commands.

### withTimeout

Returns a `ParallelRaceGroup` with a specified timeout in milliseconds.

```java
schedule(
    fooCommand.withTimeout(1000) // ends after 1000 milliseconds
);
```

### interruptOn

Returns a `ParallelRaceGroup` that ends once a specified condition is met.

```java
schedule(
    fooCommand.interruptOn(() -> {
        /* BOOLEAN SUPPLIER */
        return ...;
    })
);
```

### whenFinished

Returns a `SequentialCommandGroup` that runs a given Runnable after the calling command finishes.

```java
schedule(
    fooCommand.whenFinished(() -> {
        /* RUNNABLE */
    })
);
```

### beforeStarting

Returns a `SequentialCommandGroup` that runs a given Runnable before the calling command is initialized.

```java
schedule(
    fooCommand.beforeStarting(() -> {
        /* RUNNABLE */
    })
);
```

### andThen

Returns a `SequentialCommandGroup` that runs all the given commands in sequence after the calling command finishes.

```java
schedule(
    fooCommand.andThen(
        barCommand, bazCommand, ...
    )
);
```

### deadlineWith

Returns a `ParallelDeadlineGroup` with the calling command as the deadline to run in parallel with the given commands.

```java
schedule(
    // ends when fooCommand finishes
    fooCommand.deadlineWith(
        barCommand, bazCommand, ...
    )
);
```

### alongWith

Returns a `ParallelCommandGroup` that runs the given commands in parallel with the calling command.

```java
schedule(
    fooCommand.alongWith(
        barCommand, bazCommand, ...
    )
);
```

### raceWith

Returns a `ParallelRaceGroup` that runs all the commands in parallel until one of them finishes.

```java
schedule(
    // runs until one of the commands finishes
    fooCommand.raceWith(
        barCommand, bazCommand, ...
    )
);
```

### perpetually

Swallows the command into a `PerpetualCommand` and returns it.

```java
// returns a perpetual command
PerpetualCommand perpetual = fooCommand.perpetually();
```

### asProxy

Swallows the command into a `ProxyScheduleCommand` and returns it. This is similar to a `ScheduleCommand` except it ends when all the commands that it scheduled are finished rather than immediately.

```java
// reurns a proxy schedule command
ProxyScheduleCommand proxySchedule = fooCommand.asProxy();
```
