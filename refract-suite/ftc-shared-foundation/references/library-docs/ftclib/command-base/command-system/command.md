> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/command-base/command-system/command.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: import com.arcrobotics.ftclib.command.Command
---

# Command

Commands are simple state machines that perform high-level robot functions using the methods defined by subsystems. Commands can be either idle, in which they do nothing, or scheduled, in which the scheduler will execute a specific set of the command’s code depending on the state of the command. The `CommandScheduler` recognizes scheduled commands as being in one of three states: initializing, executing, or ending. Commands specify what is done in each of these states through the `initialize()`, `execute()` and `end()` methods. Commands are represented in the command-based library by the `Command` interface.

## Creating Commands

Similarly to subsystems, the recommended method for most users to create a command is to subclass the abstract `CommandBase` class, as seen in the command-based template.

```java
import com.arcrobotics.ftclib.command.CommandBase;

/**
 * An example command that uses an example subsystem.
 */
public class ExampleCommand extends CommandBase {
  @SuppressWarnings({"PMD.UnusedPrivateField", "PMD.SingularField"})
  private final ExampleSubsystem m_subsystem;

  /**
   * Creates a new ExampleCommand.
   *
   * @param subsystem The subsystem used by this command.
   */
  public ExampleCommand(ExampleSubsystem subsystem) {
    m_subsystem = subsystem;
    // Use addRequirements() here to declare subsystem dependencies.
    addRequirements(subsystem);
  }
}
```

As before, this contains several convenience features. It automatically overrides the `getRequirements()` method for users, returning a list of requirements that is empty by default, but can be added to with the `addRequirements()` method.

Also as before, advanced users seeking more flexibility are free to simply create their own class implementing the `Command` interface.

To schedule a command to the scheduler, you will need to call the `schedule()` method of the command instance.

```java
m_command.schedule();
```

## The Structure of  a Command

While subsystems are fairly freeform, and may generally look like whatever the user wishes them to, commands are quite a bit more constrained. Command code must specify what the command will do in each of its possible states. This is done by overriding the `initialize()`, `execute()`, and `end()` methods. Additionally, a command must be able to tell the scheduler when \(if ever\) it has finished execution - this is done by overriding the `isFinished()` method. All of these methods are defaulted to reduce clutter in user code: `initialize()`, `execute()`, and `end()` are defaulted to simply do nothing, while `isFinished()` is defaulted to return false \(resulting in a command that never ends\).

### Initialization

The `initialize()` method is run exactly once per time a command is scheduled, as part of the scheduler’s `schedule()` method. The scheduler’s `run()` method does not need to be called for the `initialize()` method to run. The initialize block should be used to place the command in a known starting state for execution. It is also useful for performing tasks that only need to be performed once per time scheduled, such as setting motors to run at a constant speed.

### Execution

The `execute()` method is called repeatedly while the command is scheduled, whenever the scheduler’s `run()` method is called. The execute block should be used for any task that needs to be done continually while the command is scheduled, such as updating motor outputs to match joystick inputs, or using the output of a control loop.

### Ending

The `end()` method is called once when the command ends, whether it finishes normally \(i.e. `isFinished()` returned true\) or it was interrupted \(either by another command or by being explicitly canceled\). The method argument specifies the manner in which the command ended; users can use this to differentiate the behavior of their command end accordingly. The end block should be used to “wrap up” command state in a neat way, such as setting motors back to zero or reverting a solenoid actuator to a “default” state.

### Specifying End Conditions

The `isFinished()` method is called repeatedly while the command is scheduled, whenever the scheduler’s `run()` method is called. As soon as it returns true, the command’s `end()` method is called and it is unscheduled. The `isFinished()` method is called _after_ the `execute()` method, so the command _will_ execute once on the same iteration that it is unscheduled.

### Simple Command Example

Taking the gripper example from the [Subsystem](subsystems.md) page, we can develop the following action to grab a stone from the quarry:

```java
import com.arcrobotics.ftclib.command.CommandBase;

/**
 * A simple command that grabs a stone with the
 * {@link GripperSubsystem}.  Written explicitly for
 * pedagogical purposes. Actual code should inline a
 * command this simple with {@link
 * com.arcrobotics.ftclib.command.InstantCommand}.
 */
public class GrabStone extends CommandBase {

    // The subsystem the command runs on
    private final GripperSubsystem m_gripperSubsystem;

    public GrabStone(GripperSubsystem subsystem) {
        m_gripperSubsystem = subsystem;
        addRequirements(m_gripperSubsystem);
    }

    @Override
    public void initialize() {
        m_gripperSubsystem.grab();
    }

    @Override
    public boolean isFinished() {
        return true;
    }

}
```

Notice that, here, the gripper subsystem is passed into the constructor in order to produce the command action. This is called [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection), and allows users to avoid declaring their subsystems as global variables. This is widely accepted as a best-practice.

Notice also that the above command calls the subsystem method once from initialize, and then immediately ends \(as `isFinished()` simply returns true\).

Below is a more complex example of a custom command.

```java
import com.arcrobotics.ftclib.command.CommandBase;

import java.util.function.DoubleSupplier;

/**
 * A command to drive the robot with joystick input
 * (passed in as {@link DoubleSupplier}s). Written
 * explicitly for pedagogical purposes.
 */
public class DefaultDrive extends CommandBase {

    private final DriveSubsystem m_drive;
    private final DoubleSupplier m_forward;
    private final DoubleSupplier m_rotation;

    /**
     * Creates a new DefaultDrive.
     *
     * @param subsystem The drive subsystem this command will run on.
     * @param forward The control input for driving forwards/backwards
     * @param rotation The control input for turning
     */
    public DefaultDrive(DriveSubsystem subsystem,
        DoubleSupplier forward, DoubleSupplier rotation) {
        m_drive = subsystem;
        m_forward = forward;
        m_rotation = rotation;
        addRequirements(m_drive);
    }

    @Override
    public void execute() {
        m_drive.drive(
            m_forward.getAsDouble(),
            m_rotation.getAsDouble()
        );
    }

}
```

Notice that this command does not override `isFinished()`, and thus will never end.

