> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/utilities-and-decorators.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Utilities and Decorators
---

Ivy provides a set of pre-built utility commands for common patterns, as well
as decorator methods that modify the behavior of existing commands. To use
them, add the following static import to the top of your file (if you don't use the import,
you can either import the utilities individually, or use the `Commands` class):

```java
import static com.pedropathing.ivy.commands.Commands.*;
```

## Utility Commands

### Instant

Instant commands run once and finishes immediately. They are useful for
actions that don't represent physical movement, but instead a state change. For example,
use instants to increment a counter or toggle a boolean.

```java
Command activateShooter = instant(() -> shooter.activate());
```

### Infinite

Infinite commands run forever until they are cancelled or interrupted. They
are useful for behaviors that need to keep running in the background, like
continuously reading a sensor.

```java
Command getBallColor = infinite(() -> currentColor = sensor.readColor());
```

### Wait

Wait commands are pretty self-explanatory. They wait for a specified number
of milliseconds and then finish. They are useful for adding delays between
other commands in a sequential composition.

```java
Command pause = waitMs(500); // waits 500ms
```

### Wait Until

Creates a command that waits until a condition becomes true and then finishes (
it takes in a `BooleanSupplier` that returns the condition).

```java
Command waitForArm = waitUntil(() -> armMotor.getCurrentPosition() > 100);
```

### On Interrupt

Creates a command that runs forever and performs a callback when it is
interrupted. This is useful for cleanup logic that runs when a group
of commands is cancelled.

```java
Command cleanup = onInterrupt(() -> armMotor.setPower(0));
```

## Control Flow Commands

These commands choose which command to run based on a condition evaluated at
start time. The condition is checked once when the command starts, not
continuously or when it is scheduled.

### Conditional

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

### Branch

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

### Match

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

### Lazy

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

## Decorators

Decorators are methods you can call on any command to modify its behavior.
They return a new command, leaving the original unchanged.

### Until

Runs a command until a condition becomes true. Internally, this creates a `Race` composition
with the original command and a `WaitUntil` command with the provided condition. The condition
is a `BooleanSupplier`.

```java
Command runIntake = infinite(() -> intake.setPower(1.0))
    .until(intake::isFull);
```

### Unless

Skips the command entirely if a condition is true at start time. If the
condition is false, the command runs normally. The condition is a `BooleanSupplier`.

```java
Command raiseArm = raiseArmCommand.unless(() -> armIsAlreadyRaised);
```

### Proxy

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
