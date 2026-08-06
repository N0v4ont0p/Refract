> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/creating-opmodes.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Scheduling and OpMode use
---

Now that you know how to create and compose commands, it's time to wire
everything together in an OpMode. The **Scheduler** is the engine that runs
your commands. You tell it which commands to run, and it takes care of
executing them, resolving conflicts, and managing queued or suspended commands.

## The Scheduler

The Scheduler is a static class, meaning you don't need to create an instance
of it. You interact with it through its static methods.

### Scheduling Commands

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

### Running the Loop

The scheduler doesn't run on its own. You need to call `Scheduler.execute()`
once per loop iteration. Each call runs one cycle of every active command:
it calls `execute()` on each running command, checks if any are done, starts
queued commands whose requirements have freed up, and resumes any suspended
commands that can continue.

```java
Scheduler.execute();
```

### Checking Command State

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

### Cancelling Commands

To stop a command before it finishes naturally:

```java
Scheduler.cancel(raiseArmCommand);
```

Or using the convenience method:

```java
raiseArmCommand.cancel();
```

### Resetting

To clear all running, queued, and suspended commands at once:

```java
Scheduler.reset();
```

## Putting It Together

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
