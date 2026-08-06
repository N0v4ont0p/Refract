> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/command-base/command-system/command-groups.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.command.CommandGroup
---

# Command Groups

Individual commands are capable of accomplishing a large variety of robot tasks, but the simple three-state format can quickly become cumbersome when more advanced functionality requiring extended sequences of robot tasks or coordination of multiple robot subsystems is required. In order to accomplish this, users are encouraged to use the powerful command group functionality included in the command-based library.

As the name suggests, command groups are combinations of multiple commands. The act of combining multiple objects \(such as commands\) into a bigger object is known as [composition](https://en.wikipedia.org/wiki/Object_composition). Command groups _compose_ multiple commands into a _composite_ command. This allows code to be kept much cleaner and simpler, as the individual _component_ commands may be written independently of the code that combines them, greatly reducing the amount of complexity at any given step of the process.

Most importantly, however, command groups _are themselves commands_ - they implement the `Command` interface. This allows command groups to be [recursively composed](https://en.wikipedia.org/wiki/Object_composition#Recursive_composition) - that is, a command group may contain _other command groups_ as components.

## Types of Command Groups

The command-based library supports four basic types of command groups: `SequentialCommandGroup`, `ParallelCommandGroup`, `ParallelRaceGroup`, and `ParallelDeadlineGroup`. Each of these command groups combines multiple commands into a composite command - however, they do so in different ways:

### SequentialCommandGroup

A `SequentialCommandGroup` runs a list of commands in sequence - the first command will be executed, then the second, then the third, and so on until the list finishes. The sequential group finishes after the last command in the sequence finishes. It is therefore usually important to ensure that each command in the sequence does actually finish \(if a given command does not finish, the next command will never start!\).

### ParallelCommandGroup

A `ParallelCommandGroup` runs a set of commands concurrently - all commands will execute at the same time. The parallel group will end when all commands have finished.

### ParallelRaceGroup

A `ParallelRaceGroup` is much like a `ParallelCommandgroup`, in that it runs a set of commands concurrently. However, the race group ends as soon as any command in the group ends - all other commands are interrupted at that point.

### ParallelDeadlineGroup

A `ParallelDeadlineGroup`also runs a set of commands concurrently. However, the deadline group ends when a _specific_ command \(the “deadline”\) ends, interrupting all other commands in the group that are still running at that point.

## Creating Command Groups

Users have several options for creating command groups. One way - similar to the previous implementation of the command-based library - is to subclass one of the command group classes. Below is an example of a command group:

```java
import com.arcrobotics.ftclib.command.SequentialCommandGroup;

/**
 * A complex auto command that drives forward,
 * releases a stone, and then drives backward.
 */
public class ReleaseAndBack extends SequentialCommandGroup {

    private static final double INCHES = 3.0;
    private static final double SPEED = 0.5;

    /**
     * Creates a new ReleaseAndBack command group.
     *
     * @param drive The drive subsystem this command will run on
     * @param grip The gripper subsystem this command will run on
     */
    public ReleaseAndBack(DriveSubsystem drive, GripperSubsystem grip)
    {
        addCommands(
                new DriveDistance(INCHES, SPEED, drive),
                new ReleaseStone(grip),
                new DriveDistance(INCHES, SPEED, drive)
        );
        addRequirements(drive, grip);
    }

}
```

The `addCommands()` method adds commands to the group, and is present in all four types of command group.

## Inline Command Groups

Command groups can be used without subclassing at all: one can simply pass in the desired commands through the constructor:

```java
new SequentialCommandGroup(new FooCommand(), new BarCommand());
```

This is called an inline command definition, and is very handy for circumstances where command groups are not likely to be reused, and writing an entire class for them would be wasteful.

## Recursive Composition of Command Groups

As mentioned earlier, command groups are [recursively composable](https://en.wikipedia.org/wiki/Object_composition#Recursive_composition) - since command groups are themselves commands, they may be included as components of other command groups. This is an extremely powerful feature of command groups, and allows users to build very complex robot actions from simple pieces. For example, consider the following code:

```java
new SequentialCommandGroup(
   new DriveToGoal(m_drive),
   new ParallelCommandGroup(
      new RaiseElevator(m_elevator),
      new SetWristPosition(m_wrist)),
   new ScoreTube(m_wrist));
```

Notice how the recursive composition allows the embedding of a parallel control structure within a sequential one. Notice also that this entire, more-complex structure, could be again embedded in another structure. Composition is an extremely powerful tool, and one that users should be sure to use extensively.

## Command Group and Requirements

As command groups are commands, they also must declare their requirements. However, users are not required to specify requirements manually for command groups - requirements are automatically inferred from the commands included. As a rule, _command groups include the union of all of the subsystems required by their component commands._ Thus, the `ReleaseAndBack` shown previously will require both the drive subsystem and the gripper subsystem of the robot.

Additionally, requirements are enforced within all three types of parallel groups - a parallel group may _not_ contain multiple commands that require the same subsystem.

Some advanced users may find this overly-restrictive - for said users, the library offers a `ScheduleCommand` class that can be used to independently “branch off” from command groups to provide finer granularity in requirement management.

## Restrictions on Command Group Components

Since command group components are run through their encapsulating command groups, errors could occur if those same command instances were independently scheduled at the same time as the group - the command would be being run from multiple places at once, and thus could end up with inconsistent internal state, causing unexpected and hard-to-diagnose behavior.

For this reason, command instances that have been added to a command group cannot be independently scheduled or added to a second command group. Attempting to do so will throw an exception and crash the user program.

Advanced users who wish to re-use a command instance and are _certain_ that it is safe to do so may bypass this restriction with the `clearGroupedCommand()` method in the `CommandGroupBase` class.

