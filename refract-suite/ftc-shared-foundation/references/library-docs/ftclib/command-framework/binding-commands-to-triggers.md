> Source: https://raw.githubusercontent.com/FTCLib/FTCLib-Docs/v2.1.0/command-base/command-system/binding-commands-to-triggers.md · Fetched: 2026-07-12
> Note: docs.ftclib.org (GitBook) returned HTTP 403 to automated fetch tools; content below is pulled from the FTCLib-Docs GitHub source at tag v2.1.0 (the same version live at https://docs.ftclib.org/ftclib/command-base/command-system/binding-commands-to-triggers), which is the exact markdown GitBook renders for that page.

# Binding Commands to Triggers

Apart from autonomous commands, which are scheduled at the start of the autonomous period, and default commands, which are automatically scheduled whenever their subsystem is not currently in-use, the most common way to run a command is by binding it to a triggering event, such as a button being pressed by a human operator. The command-based paradigm makes this extremely easy to do.

As mentioned earlier, command-based is a [declarative](https://en.wikipedia.org/wiki/Declarative_programming) paradigm. Accordingly, binding buttons to commands is done declaratively; the association of a button and a command is “declared” once, during robot initialization. The library then does all the hard work of checking the button state and scheduling (or cancelling) the command as needed, behind-the-scenes. Users only need to worry about designing their desired UI setup - not about implementing it!

Command binding is done through the `Trigger` class and its various `Button` subclasses.

## Trigger/Button Bindings

There are a number of bindings available for the `Trigger` class. All of these bindings will automatically schedule a command when a certain trigger activation event occurs - however, each binding has different specific behavior. `Button` and its subclasses have bindings with identical behaviors, but slightly different names that better-match a button rather than an arbitrary triggering event.

### whenActive/whenPressed

This binding schedules a command when a trigger changes from inactive to active (or, accordingly, when a button changes is initially pressed). The command will be scheduled on the iteration when the state changes, and will not be scheduled again unless the trigger becomes inactive and then active again (or the button is released and then re-pressed).

### whileActiveContinuous/whileHeld

This binding schedules a command repeatedly while a trigger is active (or, accordingly, while a button is held), and cancels it when the trigger becomes inactive (or when the button is released). Note that scheduling an already-running command has no effect; but if the command finishes while the trigger is still active, it will be re-scheduled.

### whileActiveOnce/whenHeld

This binding schedules a command when a trigger changes from inactive to active (or, accordingly, when a button is initially pressed) and cancels it when the trigger becomes inactive again (or the button is released). The command will _not_ be re-scheduled if it finishes while the trigger is still active.

### whenInactive/whenReleased

This binding schedules a command when a trigger changes from active to inactive (or, accordingly, when a button is initially released). The command will be scheduled on the iteration when the state changes, and will not be re-scheduled unless the trigger becomes active and then inactive again (or the button is pressed and then re-released).

### toggleWhenActive/toggleWhenPressed

This binding toggles a command, scheduling it when a trigger changes from inactive to active (or a button is initially pressed), and cancelling it under the same condition if the command is currently running. Note that while this functionality is supported, toggles are _not_ a highly-recommended option for user control, as they require the driver to mentally keep track of the robot state.

Since v1.2.0, courtesy of Ethan Leitner, the toggle binding has an additional option of switching between two commands. This is a replacement of the `ConditionalCommand` option for toggling. Simply pass two commands into the method instead of one, and the binding will toggle between those two commands.

### cancelWhenActive/cancelWhenPressed

This binding cancels a command when a trigger changes from inactive to active (or, accordingly, when a button is initially pressed). the command is canceled on the iteration when the state changes, and will not be canceled again unless the trigger becomes inactive and then active again (or the button is released and re-pressed). Note that cancelling a command that is not currently running has no effect.

## Binding a Command to a Gamepad Button

The most-common way to trigger a command is to bind a command to a button on the gamepad.

### Creating a GamepadButton

In order to create a `GamepadButton`, we first need a `GamapadEx`.

```java
GamepadEx driverOp = new GamepadEx(gamepad1);
GamepadEx toolOp = new GamepadEx(gamepad2);
```

When the object is instantiated, users can then pass it into the `GamepadButton` class.

```java
Button exampleButton = new GamepadButton(
    driverOp, GamepadKeys.Button.A
);

// alternatively, you can use the mapped GamepadButtons
// built in to the GamepadEx class
driverOp.getGamepadButton(GamepadKeys.Button.A);
```

### Binding a Command to a Button

Putting it all together, it is very simple to bind a command to a Button.

```java
exampleButton.whenPressed(new ExampleCommand());

/* It is super useful to also use instant commands */
exampleButton.whenPressed(new InstantCommand(() -> {
    // your implementation of Runnable.run() here
}));
```

It is useful to note that the command binding methods all return the trigger/button that they were initially called on, and thus can be chained to bind multiple commands to different states of the same button. For example:

```java
exampleButton
    // Binds a FooCommand to be scheduled when the `X` button
    // of the driver gamepad is pressed
    .whenPressed(new FooCommand())
    // Binds a BarCommand to be scheduled when that same button
    // is released
    .whenReleased(new BarCommand());
    
// instantiation + binding
    
/* You can also do this when you create a button object */
Button exampleButton = new GamepadButton(
    driverOp, GamepadKeys.Button.A
    // then bind commands
).whenPressed(new FooCommand())
    .whenReleased(new BarCommand());
    
/* You can also do this with the GamepadEx button mapping */
driverOp.getGamepadButton(GamepadKeys.Button.A)
    .whenPressed(new FooCommand())
    .whenReleased(new BarCommand());
```

Remember that button binding is _declarative._ Bindings only need to be declared once, ideally some time during robot initialization. The library handles everything else.

## Composing Triggers

The `Trigger` class (including its `Button` subclasses) can be composed to create composite triggers through the `and()`, `or()`, and `negate()` methods. For example:

```java
// Binds an ExampleCommand to be scheduled when both the 'X' and
// 'Y' buttons of the driver gamepad are pressed
new GamepadButton(driverOp, GamepadKeys.Button.X)
    .and(new GamepadButton(exampleController, GamepadKeys.Button.Y))
    .whenActive(new ExampleCommand());
```

Note that these methods return a `Trigger`, not a `Button`, so the `Trigger` binding method names must be used even when buttons are composed.

## Creating Your Own Custom Trigger

While binding to buttons is by far the most common use case, advanced users may occasionally want to bind commands to arbitrary triggering events. This can be easily done by simply writing your own subclass of `Trigger` or `Button`:

```java
public class ExampleTrigger extends Trigger {
  @Override
  public boolean get() {
    // This returns whether the trigger is active
  }
}
```

Alternatively, this can also be done inline by passing a lambda to the constructor of `Trigger` or `Button`:

```java
// Here it is assumed that "condition" is an object with a
// method "get" that returns whether the trigger should be active
Trigger exampleTrigger = new Trigger(condition::get);
```

This can be used for implementing a type of "triggering condition," which one might see with a sensor. On the activation of the trigger, you can cause certain commands to be scheduled or cancelled.
