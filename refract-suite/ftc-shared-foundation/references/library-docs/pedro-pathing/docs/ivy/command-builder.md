> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/command-builder.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Command Builder
---

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
 
### Lambdas and Functional Interfaces
 
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

### Reusable Commands with Static Methods

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
