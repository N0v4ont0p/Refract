> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/class-api.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Class API
---

The second way to create commands is by implementing the `Command` interface
directly as a Java class. For most commands, the
[Command Builder](./command-builder) is the better choice. If you need
reusability or parameters, a static method that returns a builder command
(as described on the previous page) is usually enough.

The Class API exists for the rare cases where your command truly needs
**internal mutable state** that persists across its lifecycle. For example,
a command that tracks how many times it has been run, or one that accumulates
sensor readings over time. If your command doesn't need that, use the Command Builder API.

## Arm Command Class

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

## Defaults You Must Provide

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

## Why Stateless Commands Are Preferred

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

## When to Use Each API

Use the **Command Builder** for the vast majority of commands. If you need
reusability or parameters, wrap the builder in a static method (as described
on the [Command Builder](./command-builder) page).

Use the **Class API** only when your command truly needs internal mutable
state that persists across its lifecycle, like tracking a running total or
accumulating sensor data over time.
