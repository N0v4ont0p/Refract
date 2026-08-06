> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/what-are-commands.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: What are commands?
---

import { Callout } from 'fumadocs-ui/components/callout'

<Callout title="Note" type="info">
  This page took inspiration from the
  [WPILib commands documentation](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html).
</Callout>

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

