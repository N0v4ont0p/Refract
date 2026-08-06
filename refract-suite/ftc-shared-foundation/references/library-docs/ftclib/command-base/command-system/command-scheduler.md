> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/command-base/command-system/command-scheduler.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.command.CommandScheduler
---

# Command Scheduler

The `CommandScheduler` is the class responsible for actually running commands. Each iteration, the scheduler polls all registered buttons, schedules commands for execution accordingly, runs the command bodies of all scheduled commands, and ends those commands that have finished or are interrupted.

The `CommandScheduler` also runs the `periodic()` method of each registered `Subsystem`.

## Using the Command Scheduler

The `CommandScheduler` is a _singleton_, meaning that it is a globally-accessible class with only one instance. Accordingly, in order to access the scheduler, users must call the `CommandScheduler.getInstance()` command.

For the most part, users do not have to call scheduler methods directly - almost all important scheduler methods have convenience wrappers elsewhere \(e.g. in the `Command` and `Subsystem` interfaces\).

However, there is one exception: users _must_ call `CommandScheduler.getInstance().run()` from the periodic method of their opmode. If this is not done, the scheduler will never run, and the command framework will not work.

To schedule a command, users call the `schedule()` method. This method takes a command \(and, optionally, a specification as to whether that command is interruptible\), and attempts to add it to list of currently-running commands, pending whether it is already running or whether its requirements are available. If it is added, its `initialize()` method is called.

## The Scheduler Run Sequence

The `initialize()` method of each `Command` is called when the command is scheduled, which is not necessarily when the scheduler runs \(unless that command is bound to a button\).

What does a single iteration of the scheduler’s `run()` method actually do? The following section walks through the logic of a scheduler iteration.

### Step 1: Run Subsystem Periodic Methods

First, the scheduler runs the `periodic()` method of each registered `Subsystem`.

### Step 2: Poll Command Scheduling Triggers

Secondly, the scheduler polls the state of all registered triggers to see if any new commands that have been bound to those triggers should be scheduled. If the conditions for scheduling a bound command are met, the command is scheduled and its `initialize()` method is run.

### Step 3: Run/Finish Scheduled Commands

Thirdly, the scheduler calls the `execute()` method of each currently-scheduled command, and then checks whether the command has finished by calling the `isFinished()` method. If the command has finished, the `end()` method is also called, and the command is de-scheduled and its required subsystems are freed.

Note that this sequence of calls is done in order for each command - thus, one command may have its `end()` method called before another has its `execute()` method called. Commands are handled in the order they were scheduled.

### Step 4: Schedule Default Commands

Finally, any registered `Subsystem` has its default command scheduled \(if it has one\). Note that the `initialize()` method of the default command will be called at this time.

## Disabling the Scheduler

The scheduler can be disabled by calling `CommandScheduler.getInstance().disable()`. When disabled, the scheduler’s `schedule()` and `run()` commands will not do anything.

The scheduler may be re-enabled by calling `CommandScheduler.getInstance().enable()`.

If you want to reset the scheduler \(clear the instance\), call `CommandScheduler.getInstance().reset()`.

## Command Event Methods

Occasionally, it is desirable to have the scheduler execute a custom action whenever a certain command event \(initialization, execution, or ending\) occurs. This can be done with the following three methods:

### onCommandInitialize

The `onCommandInitialize` method runs a specified action whenever a command is initialized.

### onCommandExecute

The `onCommandExecute` method runs a specified action whenever a command is executed.

### onCommandFinish

The `onCommandFinish` method runs a specified action whenever a command finishes normally \(i.e. the `isFinished()` method returned true\).

### onCommandInterrupt

The `onCommandInterrupt` method runs a specified action whenever a command is interrupted \(i.e. by being explicitly canceled or by another command that shares one of its requirements\).

