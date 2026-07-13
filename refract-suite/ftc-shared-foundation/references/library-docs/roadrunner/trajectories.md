> Source: https://rr.brott.dev/docs/v1-0/actions/, https://rr.brott.dev/docs/v1-0/builder-ref/ · Fetched: 2026-07-12

# Road Runner — Trajectory & Action Building (v1.0.x)

**LEGACY REFERENCE.** RoadRunner 1.0.x. Not the primary recommended
path-following library in this project anymore.

## Actions — the core execution unit

Actions are the fundamental behavioral unit for robot subsystems in
RoadRunner 1.0. They let you break complex autonomous routines into
reusable, composable pieces. The pattern is similar to command-based
systems in WPILib and FTCLib, though RoadRunner uses its own terminology.

Each subsystem defines methods that return `Action` objects:

```java
public class Drive {
    public Action followTrajectory(Trajectory t) {
        return new TodoAction();
    }

    public Action turn(double angle) {
        return new TodoAction();
    }

    public Action moveToPoint(double x, double y) {
        return new TodoAction();
    }
}
```

Actions run via `Actions.runBlocking()`. Despite the name, it remains
interruptible (so the stop button still works).

### Composing actions

- **`SequentialAction`** — runs actions one after another, in order.
- **`ParallelAction`** — runs multiple actions at once, until all finish.

```java
Actions.runBlocking(new SequentialAction(
        drive.turn(Math.PI / 2),
        new ParallelAction(
                drive.followTrajectory(shootingTraj),
                new SequentialAction(
                        shooter.spinUp(),
                        shooter.fireBall()
                )
        )
));
```

### Built-in actions

- `SleepAction` — pause for a specified duration
- `SequentialAction` — ordered execution
- `ParallelAction` — concurrent execution
- `FollowTrajectoryAction` — trajectory following (tank/mecanum variants)
- `TurnAction` — in-place rotation (tank/mecanum variants)

### Writing a custom action

Implement the `Action` interface's `run()` method. Return `true` while the
action is still executing, `false` when it's done. Calls to `run()` should
complete quickly — delays over ~100ms degrade parallel-action performance,
since actions are polled cooperatively, not run on separate threads.

```java
public class Shooter {
    private DcMotorEx motor;

    public Shooter(HardwareMap hardwareMap) {
        motor = hardwareMap.get(DcMotorEx.class, "shooterMotor");
    }

    public Action spinUp() {
        return new Action() {
            private boolean initialized = false;

            @Override
            public boolean run(@NonNull TelemetryPacket packet) {
                if (!initialized) {
                    motor.setPower(0.8);
                    initialized = true;
                }

                double vel = motor.getVelocity();
                packet.put("shooterVelocity", vel);
                return vel < 10_000.0;
            }
        };
    }
}
```

The `TelemetryPacket` parameter lets an action push live values to FTC
Dashboard while it runs.

## Building trajectories — path/spline primitives

These are the builder methods used to construct a `Trajectory` /
`TrajectoryActionBuilder` chain. Examples below assume a start pose at the
origin.

### Position primitives

- **`.lineToX(48)`** — move to a target x-coordinate, holding y constant.
- **`.lineToY(36)`** — move to a target y-coordinate, holding x constant.
- **`.splineTo(new Vector2d(48, 48), Math.PI / 2)`** — spline to a target
  position with a specified end tangent heading.

### Heading primitives

RoadRunner 1.0 supports four heading interpolation modes while following a
spline:

- **Tangent heading (default)** — heading follows the tangent of the spline
  curve.
  ```java
  .setTangent(0)
  .splineTo(new Vector2d(48, 48), Math.PI / 2)
  ```
- **Constant heading** — heading stays fixed throughout the segment.
  ```java
  .setTangent(0)
  .splineToConstantHeading(new Vector2d(48, 48), Math.PI / 2)
  ```
- **Linear heading** — heading interpolates linearly from start to end.
  ```java
  .setTangent(0)
  .splineToLinearHeading(new Pose2d(48, 48, 0), Math.PI / 2)
  ```
- **Spline heading** — heading interpolates via spline between start and end
  angles.
  ```java
  .setTangent(0)
  .splineToSplineHeading(new Pose2d(48, 48, 0), Math.PI / 2)
  ```

Note: RoadRunner 1.0 removed the old continuity-violation exceptions —
builders now automatically split a chain into multiple paths/trajectories
where needed instead of throwing.
