> Source: https://pedropathing.com/docs/ivy · Fetched: 2026-07-12

# Ivy — Command-Based Autonomous Framework for Pedro Pathing

> Source: https://pedropathing.com/docs/ivy · Fetched: 2026-07-12

## Installation

Welcome to **Ivy by Pedro Pathing**, a simple, easy to use, and powerful
command-based control flow library for FTC.

### Install Ivy

In your `build.dependencies.gradle` file, add the following line in the
`dependencies` block:

```groovy [build.dependencies.gradle]
implementation 'com.pedropathing:ivy:1.0.0'
```

Click the **Sync Now** button that appears in your IDE.

---

> Source: https://pedropathing.com/docs/ivy/what-are-commands · Fetched: 2026-07-12

## What are commands?

> **Note:**
> This page took inspiration from the
> [WPILib commands documentation](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html).

Ivy is a library that implements the **command-based programming paradigm**.
While it is not the only way to write robot code, command-based robot code is
clean, extensible, reusable, and modular. Command-based programming is also
a type of declarative programming, which means that you write code
describing _what_ you want your robot to do, instead of specifying _how_ to do
it.

The building block of command-based programming is, of course, the
**command**. A command represents an action the robot can perform. Commands
are run by the **command scheduler**, which runs scheduled commands at the
appropriate times. One of the biggest benefits of commands is that they can
run in parallel with each other. This is done using **cooperative
multitasking**. This means that each command must give up control of the
thread periodically to allow other commands to run, which allows all
commands to run on a single thread.

To run commands in parallel, the
scheduler runs each command for a short period of time and then runs the
next command, running each scheduled command once per loop. For example, if
the scheduler was running command A and command B in parallel, it would run
a tiny bit of command A, a tiny bit of command B, then a tiny bit of
command A again, and so on.

Commands have **four core parts**:

- `start()`: Called immediately when the command is scheduled to run.
- `execute()`: Called every loop by the scheduler. This is where the command
  performs a tiny bit of its action.
- `done()`: Returns whether the command finished or should continue running
  next loop.
- `end(endCondition)`: Called when the command finishes, is
  interrupted, or is suspended (more on that later).

Let's take a look at an example command that raises an arm using a PID
controller and cuts power to the motors when the arm reaches the target
position. Since we don't know how to create commands yet, we'll just
consider what each part of the command would do.

- `start()`: Does nothing.
- `execute()`: Uses the PID controller to set the arm motor's power.
- `done()` Returns whether the arm is within tolerance of the target position.
- `end()`: Sets the arm motor's power to zero.

---

> Source: https://pedropathing.com/docs/ivy/requirements-and-priorities · Fetched: 2026-07-12

## Requirements and Priorities

In the previous example with the arm raising command, you would likely also have a command
that lowers the arm. Let's imagine a situation in which the arm is actively raising.
There are numerous different ways that you may
want to schedule the lowering command. In some situations, you may want to lower the arm
immediately, overriding the raising command. In others, you may want to wait until the raising
command finishes before lowering the arm, but you may decide this after you scheduled the raising
command (meaning you can't use a sequential composition, as described in a later section).
You may also want to immediately lower the arm, but then immediately raise it again.

With the tools provided so far, it would be inconvenient and verbose to have to write a
separate command for each of these scenarios. To solve this problem, Ivy provides
**requirements**. Requirements are a way to specify that a given command uses certain objects
or subsystems on your robot. In the above example, you would have the raising and lowering commands
require the arm motor(s) or the arm subsystem if you've created a class. In general, a command can
have any number of requirements, and a requirement can be any object.

By themselves, requirements are not very useful. However, when combined with priorities,
they allow you to specify how commands that share requirements should interact. A priority is an integer that specifies
how important a command is. The default priority is 0.

When you try to schedule a command with conflicting requirements with any currently scheduled
commands, there are three types of behaviors that can occur:

- **Interrupted Behavior**: If all currently scheduled commands have a lower priority than the new,
  conflicting command, this determines what happens to each currently scheduled command.
  `InterruptedBehavior` is an enum with types `END` and `SUSPEND`. `END` means that each
  currently scheduled command will terminate and not be run again, while `SUSPEND` means
  that the currently scheduled command will be suspended and continue when the conflicting
  command finishes. In both cases, `end()` will be called on each currently scheduled command.
  Defaults to `END`.
- **Blocked Behavior**: If any currently scheduled command has a higher priority than the new,
  conflicting command, this determines what happens to the conflicting command. `BlockedBehavior`
  is an enum with types `CANCEL` and `QUEUE`. `CANCEL` means that the conflicting command will be
  canceled, while `QUEUE` means that the conflicting command will be queued and run after the currently
  scheduled conflicting commands finish.
  Defaults to `CANCEL`.
- **Conflict Behavior**: If the highest priority of all currently scheduled commands is equal to
  the new conflicting command, this determines what happens to the new conflicting command.
  `ConflictBehavior` is an enum with types `CANCEL`, `QUEUE`, and `OVERRIDE`. `CANCEL` means that
  the new conflicting command will not be scheduled, `QUEUE` means that the new conflicting command will
  be queued and run after the currently scheduled conflicting commands finish, and `OVERRIDE` means that
  the new conflicting command will interrupt the currently scheduled conflicting commands and run instead
  (note, this triggers the `InterruptedBehavior` of the currently scheduled conflicting commands).
  Defaults to `OVERRIDE`.

Returning to our arm example, instead of creating separate commands for each of the scenarios,
we can create a single command and modify its priority to handle each scenario.

Note that requirements are a completely optional feature, and you can use Ivy perfectly well
without them. However, they are a powerful tool that can help you write simpler and safer code
should you want to use them.

---

> Source: https://pedropathing.com/docs/ivy/command-builder · Fetched: 2026-07-12

## Command Builder

Ivy has **two different APIs** to create commands. Unless you specifically need
internal state in your commands, you should use the **Command Builder API**
described on this page. The other API, the [Class API](./class-api), is
explained on a later page.

To create a command using the Command Builder API, call `Command.build()`.
Then, you can set the behavior of the command using the various methods on the builder.

```java
Command myFirstCommand = Command.build()
    .setStart(() -> {
        // executed on start
    })
    .setExecute(() -> {
        // executed on execute
    })
    .setDone(() -> {
        // return true to end the command
    })
    .setEnd(endCondition -> {
        // executed on end
    })
    .requiring(/* requirements */)
    .setInterruptedBehavior(/* interrupted behavior */)
    .setBlockedBehavior(/* blocked behavior */)
    .setConflictBehavior(/* conflict behavior */)
    .setPriority(/* priority */);
```

All methods are optional, so you're free to not call a method you don't need.
For example, the arm command from the earlier page could be written as follows:

```java
Command raiseArm = Command.build()
    .setStart(() -> pidController.setTarget(RAISED_ARM_POSITION))
    .setExecute(() -> {
        armMotor.setPower(pidController.calculate(armMotor.getCurrentPosition()));
    })
    .setDone(() -> Math.abs(pidController.getTarget() - armMotor.getCurrentPosition()) < 10)
    .setEnd(endCondition -> armMotor.setPower(0))
    .requiring(armMotor);
```

`setStart` and `setExecute` have a parameter of type `Runnable`. `setDone` has a parameter of type
`BooleanSupplier`. `setEnd` has a parameter of type `Consumer<EndCondition>`. If you understand what those mean, you can skip the next section; otherwise,
read on.

#### Lambdas and Functional Interfaces

Look at the `setStart` call in the example above:

```java
.setStart(() -> {
    // executed on start
})
```

The `() -> { }` syntax is a **lambda expression**, also known as an **anonymous function**. It lets you define
the behavior of a function inline, without having to create a separate named method. You can think of what comes
before the arrow as the parameter list (like you usually use in a method declaration but without the name or return type)
and what comes after the arrow as the body of the function.

This works because `setStart` takes a `Runnable`, which is a **functional interface**, or a type representing a function
A functional interface has a single method, and the parameters and return type of that method define
the signature of function it represents. Here are some common ones:

| Interface | Takes | Returns | Lambda Syntax |
|---|---|---|---|
| `Runnable` | nothing | nothing | `() -> { /* code */ }` |
| `Consumer<T>` | one value of type `T` | nothing | `(value) -> { /* code */ }` |
| `Supplier<T>` | nothing | a value of type `T` | `() -> { return value; }` |

So when you write `setStart(() -> pidController.setTarget(RAISED_ARM_POSITION))`, you're creating a function
that takes no parameters and returns nothing, meaning matches the signature of and is a `Runnable` type.
Since `setStart` takes in a `Runnable`, this is valid to pass in! When the scheduler calls `start()`
on the command, it will call your function. The same goes for the other methods mentioned.

`setEnd` takes a `Consumer<EndCondition>`, so its lambda receives a parameter:

```java
.setEnd(endCondition -> {
    // endCondition tells you *why* the command ended
    // in this case endCondition isn't actually used in the body, but you could use it
    // to change the ending behavior of the command based on the reason it ended
    armMotor.setPower(0);
})
```

Note that you don't have to use anonymous functions; you can use named functions as well. To pass in a named
function, use `object::methodName` (you use `this` in lieu of `object` if you are working in that class, and
you use the name of the class instead if the method is static).

For example, if you had an arm subsystem class with a method `setRaisedArmTarget()`, you could use
`setStart(arm::setRaisedArmTarget)` instead of `setStart(() -> arm.setRaisedArmTarget())`.

Check out
[this explanation by WPILib](https://docs.wpilib.org/en/stable/docs/software/basic-programming/functions-as-data.html) if
you want to learn more about passing around functions.

#### Reusable Commands with Static Methods

You might think you need the [Class API](./class-api) to make a command
reusable with different parameters. However, in most cases you don't. Instead, you can
write a static method that returns a builder command:

```java
public static Command raiseArm(double target) {
    return Command.build()
        .setStart(() -> pid.setTarget(target))
        .setExecute(() -> armMotor.setPower(pid.calculate(armMotor.getCurrentPosition())))
        .setDone(() -> Math.abs(target - armMotor.getCurrentPosition()) < 10)
        .setEnd(endCondition -> armMotor.setPower(0))
        .requiring(armMotor);
}
```

Now you can call `raiseArm(1000)` anywhere, and each call
creates a fresh, independent command. This pattern gives you the reusability
of a class without the boilerplate.

Commands built this way are also **stateless**, meaning they don't hold onto
any internal state between runs. This is a good thing. Stateless commands are
safer to reuse because there's no risk of leftover state from a previous run
affecting the next one. They are also easier to compose, since you can freely
pass them into sequential, parallel, and race compositions without worrying
about shared mutable state.

---

> Source: https://pedropathing.com/docs/ivy/command-compositions · Fetched: 2026-07-12

## Command Compositions

Remember on the [What are Commands?](./what-are-commands) page where we said that
commands can be run in parallel? That's an example of a **command composition**.
A command composition is, at its core, a command that is "composed" of smaller
commands. Let's take a look at the different types of command compositions
in Ivy.

### Sequential

Sequential compositions are probably the most common type of command composition.
They take a list of commands and run them one after the other. To create a
sequential composition, use the `sequential` function:

```java
Command myCommand = sequential(
    command1,
    command2,
    command3
);
```

Notice that the command returned by `sequential` is a command itself, which
means you can nest compositions inside each other. This is one of the
beauties of command compositions: they can be nested arbitrarily.

You can also create sequential compositions using the `then` method:

```java
Command myCommand = command1.then(command2).then(command3);
Command myCommand = command1.then(command2, command3);
```

### Parallel

Sequential compositions are great for running commands one after the other, but
what if you want to run multiple commands at the same time? For this, you can
use a parallel compositions. Parallel compositions are created using the
`parallel` function:

```java
Command myCommand = parallel(
    command1,
    command2,
    command3
);
```

As with sequential compositions, you can nest parallel compositions. This
means you can put a parallel composition inside a sequential composition or
a sequential composition inside a parallel composition!

You can also create parallel compositions using the `with` method:

```java
Command myCommand = command1.with(command2).with(command3);
Command myCommand = command1.with(command2, command3);
```

### Race

Race compositions are similar to parallel compositions, but instead of
finishing when all commands finish, they finish when the first command
finishes. The remaining commands are cancelled. Race compositions are created
using the `race` function:

```java
Command myCommand = race(
    command1,
    command2,
    command3
);
```

You can also create race compositions using the `raceWith` method:

```java
Command myCommand = command1.raceWith(command2).raceWith(command3);
Command myCommand = command1.raceWith(command2, command3);
```

### Deadline

Deadline compositions are similar to parallel and race compositions, but
they finish when a specific "deadline" command finishes. The remaining
commands are cancelled. Deadline compositions are created using the `deadline`
function:

```java
Command myCommand = deadline(
    deadlineCommand,
    command1,
    command2,
    command3
);
```

### Repeat

A repeat composition is a command that runs a command a specified number of times.
Repeat compositions are created using the `repeat` function:

```java
Command repeatCommand = repeat(command, 3); // repeats command 3 times
```

You can also pass an `IntSupplier` (essentially the same as `Supplier<Integer>` explained on the previous page)
instead of an `int` if you want to dynamically
determine the number of times the command should be repeated.

### Loop

A loop composition runs a command and restarts it whenever it finishes. Loop
compositions are created using the `loop` function:

```java
Command loopCommand = loop(command);
```

Loop commands never finish. To make one finish after a condition, you can
put it in a race composition with another command.

---

> Source: https://pedropathing.com/docs/ivy/pedro-commands · Fetched: 2026-07-12

## Pedro Commands

Ivy includes built-in commands for controlling your robot's movement using
[Pedro Pathing](https://pedropathing.com). To use them, add the following
static import:

```java
import static com.pedropathing.ivy.pedro.PedroCommands.*;
```

All Pedro commands take a `Follower` as their first argument. Usually your Follower
is one created from your `Constants` file's `createFollower()` method.

### Follow

Makes the robot follow a `PathChain`. The command finishes when the follower
is no longer busy (i.e. the path is complete).

```java
Command goToBasket = follow(follower, basketPath);
```

You can optionally specify whether the robot should hold its position at the
end of the path, and a maximum power between 0 and 1:

```java
Command goToBasket = follow(follower, pickupCloseSpikemark, true);          // hold at end
Command goToBasket = follow(follower, pickupCloseSpikemark, 0.5);           // cap max power at half
Command goToBasket = follow(follower, pickupCloseSpikemark, true, 0.5);     // both
```

If you don't pass `holdEnd`, it defaults to your follower's
`automaticHoldEnd` setting. If you don't pass `maxPower`, it defaults to
the follower's current max power.

### Hold

Makes the robot hold a position. The command finishes when the robot is
within tolerance of the target (based on translational and heading error).

To hold the robot's current position:

```java
Command stayHere = hold(follower);
```

To hold a specific pose:

```java
Command holdAtBasket = hold(follower, new Pose(50, 30, Math.toRadians(90)));
```

You can also pass custom `PathConstraints` to control how tight the
completion tolerance is:

```java
Command preciseHold = hold(follower, targetPose, new PathConstraints(
    0.995,  // tValueConstraint
    100     // timeoutConstraint (ms)
));
```

### Turn To

Makes the robot turn in place to a specified heading (in radians). The
command finishes when the follower is no longer busy.

```java
Command faceForward = turnTo(follower, Math.toRadians(0));
Command faceLeft = turnTo(follower, Math.toRadians(90));
```

As with `hold`, you can pass custom `PathConstraints`:

```java
Command preciseTurn = turnTo(follower, Math.toRadians(180), customConstraints);
```

### Composing Pedro Commands

Since Pedro commands are regular Ivy commands, you can compose them with
everything else. For example:

```java
Command auto = sequential(
    follow(follower, shootPreloads),
    Shooter.shoot(), // the shoot method here would be a command
    instant(() -> claw.open()),
    parallel(
        follow(follower, pickupCloseSpikemark),
        instant(() -> intake.activate())
    )
/* ... */
);
```

---

> Source: https://pedropathing.com/docs/ivy/creating-opmodes · Fetched: 2026-07-12

## Scheduling and OpMode use

Now that you know how to create and compose commands, it's time to wire
everything together in an OpMode. The **Scheduler** is the engine that runs
your commands. You tell it which commands to run, and it takes care of
executing them, resolving conflicts, and managing queued or suspended commands.

### The Scheduler

The Scheduler is a static class, meaning you don't need to create an instance
of it. You interact with it through its static methods.

#### Scheduling Commands

To run a command, schedule it:

```java
Scheduler.schedule(raiseArmCommand);
```

If you include the static import
```
import static com.pedropathing.ivy.Scheduler.schedule;
```

you can use the `schedule()` method directly.

You can also schedule multiple commands at once:
```java
schedule(raiseArmCommand, openClawCommand);
```
By default, all commands run in the scheduler in parallel. To make commands
run sequentially, you must explicitly use a sequential composition.

Every command also has a convenience method that does the same thing:

```java
raiseArmCommand.schedule();
```

#### Running the Loop

The scheduler doesn't run on its own. You need to call `Scheduler.execute()`
once per loop iteration. Each call runs one cycle of every active command:
it calls `execute()` on each running command, checks if any are done, starts
queued commands whose requirements have freed up, and resumes any suspended
commands that can continue.

```java
Scheduler.execute();
```

#### Checking Command State

You can check whether a command is actively running:

```java
Scheduler.isRunning(raiseArmCommand); // true if currently executing
```

Or whether it is scheduled in any form (running, queued, or suspended):

```java
Scheduler.isScheduled(raiseArmCommand);
```

These are also available as convenience methods on the command itself:

```java
raiseArmCommand.isScheduled();
```

#### Cancelling Commands

To stop a command before it finishes naturally:

```java
Scheduler.cancel(raiseArmCommand);
```

Or using the convenience method:

```java
raiseArmCommand.cancel();
```

#### Resetting

To clear all running, queued, and suspended commands at once:

```java
Scheduler.reset();
```

### Putting It Together

Here is a minimal `LinearOpMode` that uses Ivy. It defines a couple of
commands, schedules them, and runs the scheduler loop.

```java
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.pedropathing.ivy.Scheduler;

import static com.pedropathing.ivy.commands.Commands.*;
import static com.pedropathing.ivy.groups.Groups.*;

@TeleOp
public class MyOpMode extends LinearOpMode {
    @Override
    public void runOpMode() {
        //Since the scheduler is static, we need to reset it before each OpMode
        //so commands don't carry over from one OpMode to the next
        Scheduler.reset();

        // Initialize hardware
        DcMotor armMotor = hardwareMap.get(DcMotor.class, "arm");
        Servo claw = hardwareMap.get(Servo.class, "claw");

        // Define commands
        Command raiseArm = Command.build()
            .setExecute(() -> armMotor.setPower(0.5))
            .setDone(() -> armMotor.getCurrentPosition() > 1000)
            .setEnd(endCondition -> armMotor.setPower(0))
            .requiring(armMotor);

        Command openClaw = instant(() -> claw.setPosition(1.0));

        // Compose: raise the arm, wait 200ms, then open the claw
        Command sequence = sequential(
                raiseArm,
                waitMs(200),
                openClaw
        );

        waitForStart();

        // Schedule the sequence when the OpMode starts
        schedule(sequence);

        while (opModeIsActive()) {
            // Run the scheduler each loop
            Scheduler.execute();
        }
    }
}
```

---

> Source: https://pedropathing.com/docs/ivy/utilities-and-decorators · Fetched: 2026-07-12

## Utilities and Decorators

Ivy provides a set of pre-built utility commands for common patterns, as well
as decorator methods that modify the behavior of existing commands. To use
them, add the following static import to the top of your file (if you don't use the import,
you can either import the utilities individually, or use the `Commands` class):

```java
import static com.pedropathing.ivy.commands.Commands.*;
```

### Utility Commands

#### Instant

Instant commands run once and finishes immediately. They are useful for
actions that don't represent physical movement, but instead a state change. For example,
use instants to increment a counter or toggle a boolean.

```java
Command activateShooter = instant(() -> shooter.activate());
```

#### Infinite

Infinite commands run forever until they are cancelled or interrupted. They
are useful for behaviors that need to keep running in the background, like
continuously reading a sensor.

```java
Command getBallColor = infinite(() -> currentColor = sensor.readColor());
```

#### Wait

Wait commands are pretty self-explanatory. They wait for a specified number
of milliseconds and then finish. They are useful for adding delays between
other commands in a sequential composition.

```java
Command pause = waitMs(500); // waits 500ms
```

#### Wait Until

Creates a command that waits until a condition becomes true and then finishes (
it takes in a `BooleanSupplier` that returns the condition).

```java
Command waitForArm = waitUntil(() -> armMotor.getCurrentPosition() > 100);
```

#### On Interrupt

Creates a command that runs forever and performs a callback when it is
interrupted. This is useful for cleanup logic that runs when a group
of commands is cancelled.

```java
Command cleanup = onInterrupt(() -> armMotor.setPower(0));
```

### Control Flow Commands

These commands choose which command to run based on a condition evaluated at
start time. The condition is checked once when the command starts, not
continuously or when it is scheduled.

#### Conditional

Conditional commands choose between two commands based on a boolean condition, like an if/else
statement (the condition is a `BooleanSupplier`).

```java
Command handleArm = conditional(
    () -> armIsRaised,
    lowerArmCommand,
    raiseArmCommand
);
```

When the scheduler calls `handleArm.start()`, it checks the condition. If it returns `true`, it
runs `lowerArmCommand`. Otherwise, it runs `raiseArmCommand`.

#### Branch

Branch commands choose between multiple commands based on conditions, like a series of
if/else-if statements. The behavior is determined by the first condition that returns `true`. If none
match, the command finishes immediately.

```java
LinkedHashMap<BooleanSupplier, Command> cases = new LinkedHashMap<>();
cases.put(() -> position == Position.HIGH, moveToHigh);
cases.put(() -> position == Position.MID, moveToMid);
cases.put(() -> position == Position.LOW, moveToLow);

Command handlePosition = branch(cases);
```

The order you insert entries into the `LinkedHashMap` determines the priority
of each condition. The first entry is checked first, etc.

#### Match

Match commands choose a command based on the value of an enum, like a switch statement. This
is a cleaner alternative to `branch` when your conditions map to enum values.

```java
enum ArmState { RAISED, LOWERED, STOWED }

EnumMap<ArmState, Command> cases = new EnumMap<>(ArmState.class);
cases.put(ArmState.RAISED, raiseCommand);
cases.put(ArmState.LOWERED, lowerCommand);
cases.put(ArmState.STOWED, stowCommand);

Command handleArm = match(() -> currentArmState, cases);
```

If the enum value does not have a matching entry in the map, the command
finishes immediately.

The first argument of the `match()` method is a `Supplier<T>` that returns the value to match on,
where `T` is the type of the enum and also must be the same type as the keys in the `EnumMap`. If the
type of the Supplier is not the same as the type of the enum, you'll get a compile error.

#### Lazy

Lazy commands defer the creation of a command until the moment it starts. This is useful
when the command you want to run depends on state that isn't known ahead of
time.

```java
Command deferred = lazy(() -> {
    Pose targetPosition = getTargetPose();
    return Command.build()
        .setStart(() -> pid.setTarget(targetPosition))
        .setExecute(() -> drivetrain.setPower(pid.calculate(drivetrain.getCurrentPosition())))
        .setDone(() -> drivetrain.getCurrentPosition().withinTolerance(targetPosition));
});
```

The `lazy` command is useful here because it allows you to get a necessary state for a command
when it starts while keeping the command itself stateless. Stateless commands are much more
flexible and reusable, which is why lazy commands are so useful.

### Decorators

Decorators are methods you can call on any command to modify its behavior.
They return a new command, leaving the original unchanged.

#### Until

Runs a command until a condition becomes true. Internally, this creates a `Race` composition
with the original command and a `WaitUntil` command with the provided condition. The condition
is a `BooleanSupplier`.

```java
Command runIntake = infinite(() -> intake.setPower(1.0))
    .until(intake::isFull);
```

#### Unless

Skips the command entirely if a condition is true at start time. If the
condition is false, the command runs normally. The condition is a `BooleanSupplier`.

```java
Command raiseArm = raiseArmCommand.unless(() -> armIsAlreadyRaised);
```

#### Proxy

Wraps a command so that it runs through the Scheduler independently rather than
being managed directly by its parent composition. When a proxy starts, it
schedules the original command as a separate entity in the Scheduler. When
the proxy is interrupted, it cancels the original command.

This is useful when you want a command inside a composition to have an
independent lifecycle. Normally, if a composition is interrupted, all of its
children are interrupted too. A proxied command can outlive the composition
that started it. It can also be individually cancelled or inspected from
outside the composition using `Scheduler.cancel()` or
`Scheduler.isScheduled()`.

```java
Command proxied = someCommand.proxy();
```

---

> Source: https://pedropathing.com/docs/ivy/class-api · Fetched: 2026-07-12

## Class API

The second way to create commands is by implementing the `Command` interface
directly as a Java class. For most commands, the
[Command Builder](./command-builder) is the better choice. If you need
reusability or parameters, a static method that returns a builder command
(as described on the previous page) is usually enough.

The Class API exists for the rare cases where your command truly needs
**internal mutable state** that persists across its lifecycle. For example,
a command that tracks how many times it has been run, or one that accumulates
sensor readings over time. If your command doesn't need that, use the Command Builder API.

### Arm Command Class

To create a command class, implement the `Command` interface and provide all
of its required methods:

```java
import com.pedropathing.ivy.Command;
import com.pedropathing.ivy.behaviors.*;

import java.util.Set;

public class RaiseArm implements Command {
    private final DcMotor armMotor;
    private final PIDController pid;
    private final double target;

    public RaiseArm(DcMotor armMotor, PIDController pid, double target) {
        this.armMotor = armMotor;
        this.pid = pid;
        this.target = target;
    }

    @Override
    public void start() {
        pid.setTarget(target);
    }

    @Override
    public void execute() {
        armMotor.setPower(pid.calculate(armMotor.getCurrentPosition()));
    }

    @Override
    public boolean done() {
        return Math.abs(target - armMotor.getCurrentPosition()) < 10;
    }

    @Override
    public void end(EndCondition endCondition) {
        armMotor.setPower(0);
    }

    @Override
    public Set<Object> requirements() {
        return Set.of(armMotor);
    }

    @Override
    public int priority() {
        return 0;
    }

    @Override
    public InterruptedBehavior interruptedBehavior() {
        return InterruptedBehavior.END;
    }

    @Override
    public BlockedBehavior blockedBehavior() {
        return BlockedBehavior.CANCEL;
    }

    @Override
    public ConflictBehavior conflictBehavior() {
        return ConflictBehavior.OVERRIDE;
    }
}
```

You can then create instances of this class:

```java
Command raise = new RaiseArm(armMotor, pid, RAISED_POSITION);
```

Compare this with the equivalent [Command Builder](./command-builder) version:

```java
Command raise = Command.build()
    .setStart(() -> pid.setTarget(RAISED_POSITION))
    .setExecute(() -> armMotor.setPower(pid.calculate(armMotor.getCurrentPosition())))
    .setDone(() -> Math.abs(RAISED_POSITION - armMotor.getCurrentPosition()) < 10)
    .setEnd(endCondition -> armMotor.setPower(0))
    .requiring(armMotor);
```

Both create the same command. The class version is more verbose but gives you
a named type with internal state. Note that you don't need the class version
just for reusability or parameters. As described on the
[Command Builder](./command-builder) page, a static method that returns a
builder command achieves the same thing with less boilerplate and without
introducing mutable state.

### Defaults You Must Provide

When you use the Command Builder, it fills in sensible defaults for everything
you don't set:

| Method | Default |
|---|---|
| `requirements()` | empty (no requirements) |
| `priority()` | `0` |
| `interruptedBehavior()` | `InterruptedBehavior.END` |
| `blockedBehavior()` | `BlockedBehavior.CANCEL` |
| `conflictBehavior()` | `ConflictBehavior.OVERRIDE` |
| `start()` | does nothing |
| `execute()` | does nothing |
| `done()` | returns `false` (runs forever) |
| `end(endCondition)` | does nothing |

When implementing the `Command` interface directly, you must provide all of
these yourself. If you want the same defaults as the builder, use the values
in the table above.

### Why Stateless Commands Are Preferred

Commands built with the Command Builder are **stateless**. They don't hold
onto mutable fields between runs, which means:

- There's no risk of leftover state from a previous run leaking into the
  next one.
- They are safe to reuse, compose, and schedule multiple times without
  worrying about shared mutable state.
- They are easier to debug, since the command's behavior is fully
  determined by the lambdas you pass in and the external objects they
  reference.

Class-based commands, by contrast, can hold mutable fields that change as the
command runs. This makes them harder to reuse safely. If you schedule the same
instance twice, the second run might see state left over from the first. In general,
if you use the Class API, you will want to create a new command instance each time
you need to schedule that command.

### When to Use Each API

Use the **Command Builder** for the vast majority of commands. If you need
reusability or parameters, wrap the builder in a static method (as described
on the [Command Builder](./command-builder) page).

Use the **Class API** only when your command truly needs internal mutable
state that persists across its lifecycle, like tracking a running total or
accumulating sensor data over time.

---

> Source: https://pedropathing.com/docs/ivy/example-repos · Fetched: 2026-07-12

## Example Repos

Here are some example repositories that use Ivy. Each link below
points to a specific file that demonstrates Ivy usage.

### #365 MOE

[GitHub Repository](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode)

- [Auto.java](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/Auto.java) — autonomous using lots of compositions and Pedro commands
- [Tele.java](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/Tele.java) — teleop example
- [IntakingState.java](https://github.com/MOEbo-Sapiens/MOEbo-Sapiens-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/states/IntakingState.java) — example usage within a finite state machine

### #12649 Code Blooded

[GitHub Repository](https://github.com/BeepBot99/CodeBloodedDecodeV2)

- [RobotOpMode.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/robot/RobotOpMode.java) — base OpMode class that integrates the Scheduler
- [Intake.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/subsystems/Intake.java) — subsystem defining commands with `Commands.*`
- [Turret.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/subsystems/Turret.java) — subsystem using `Commands.infinite` for continuous control
- [BlueClose15Full.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/BlueClose15Full.java) — autonomous OpMode scheduling command sequences
- [CompetitionTeleOp.java](https://github.com/BeepBot99/CodeBloodedDecodeV2/blob/master/src/main/java/org/firstinspires/ftc/teamcode/opmodes/teleop/CompetitionTeleOp.java) — teleop OpMode scheduling commands from subsystems

### #22131 Traffic Cones

[GitHub Repository](https://github.com/BaronClaps/22131-Decode)

- [CommandOpMode.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/command/CommandOpMode.java) — base OpMode class wrapping the Scheduler
- [Robot.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/Robot.java) — central robot class building commands with `CommandBuilder`
- [Intake.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/subsystem/Intake.java) — subsystem defining commands with `Commands.*`
- [Shooter.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/config/subsystem/Shooter.java) — subsystem using `CommandBuilder` and `Commands`
- [Auto15.java](https://github.com/BaronClaps/22131-Decode/blob/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmode/auto/Auto15.java) — autonomous OpMode using `Groups.sequential` and `PedroCommands`

