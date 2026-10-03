# Pedro Pathing 3.0 — API surface (tier-1 vendor source)

> Source: https://github.com/Pedro-Pathing/Quickstart @ `2df96463753dba59271df3f71c1619fb5f9da65a`
> (master, 2026-09-30), `TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedro/**` and
> `build.dependencies.gradle`. Fetched 2026-10-03. Only what that source shows is stated here;
> anything it does not show is marked NOT IN SOURCE — do not fill it in from the 2.x docs.
>
> **Which docs apply:** read the team's `build.dependencies.gradle`.
> `com.pedropathing:ftc:2.x` → `../pedro-pathing/` (2.x: `FollowerBuilder`, `FollowerConstants`,
> `MecanumConstants`, `PinpointConstants`). `com.pedropathing:revhub:3.x` → this file. The two APIs
> do not mix; none of the 2.x class names exist in this source.

## Dependencies

```groovy
repositories { maven { url 'https://repo.dairy.foundation/releases/' } }
dependencies {
    implementation 'com.pedropathing:revhub:3.0.1'
    implementation 'com.pedropathing:tuning:1.0.1'   // tuner procedures (com.pedropathing.tuning.autotune)
}
```

## Follower

```java
new Follower(Localizer localizer, Drivetrain drivetrain, Algorithm algorithm)   // Tests.java:71
```

Argument order is **localizer, drivetrain, algorithm**. The Quickstart's `Constants.java` comment
(`// return new Follower(Drivetrain, Localizer, Foresight);`) lists a different order and is wrong —
`Tests.java:71` is the compiled call. `Constants.create(HardwareMap)` ships returning `null`; the team
fills it in.

| Call | Source |
|---|---|
| `follower.setPose(Pose)` | Tests.java:143,146 |
| `follower.update()` — every loop | Tests.java:147,150 |
| `follower.hold(Pose)` | Tests.java:148 |
| `follower.follow(Path)` | Tests.java:181 |
| `follower.atParametricEnd()` — end-of-path check | Tests.java:185 |

Types: `com.pedropathing.follower.Follower`, `com.pedropathing.algorithm.Algorithm`,
`com.pedropathing.drivetrain.Drivetrain`, `com.pedropathing.localization.Localizer`.

## Pose — `com.pedropathing.math.Pose`

`new Pose(x, y)`, `new Pose(x, y, heading)`, `Pose.zero()`, accessors `pose.x()`, `pose.y()`,
`pose.heading()` (Tests.java:174, 216, 359). Heading is radians (the tests compare total heading
against `2 * Math.PI`, Tests.java:425). NOT `com.pedropathing.geometry.Pose` (2.x).

## Paths — `com.pedropathing.api.Paths`

```java
import static com.pedropathing.api.Paths.line;
import static com.pedropathing.api.Paths.curve;

Path a = line(Pose.zero(), new Pose(48, 0, 0)).constant(0);                     // Tests.java:174
Path b = curve(Pose.zero(), new Pose(48, 0), new Pose(48, 48)).tangent();        // Tests.java:216
Path c = curve(p0, p1, p2).heading((curve, t) -> Math.PI);                        // Tests.java:258
Path d = curve(p0, p1, p2).heading(Interpolator.piecewise()
        .until(0.5, Interpolator.tangent).until(1.0, Interpolator.constant(0)));  // Tests.java:259
```

`Path` = `com.pedropathing.paths.Path`; `Interpolator` = `com.pedropathing.paths.interpolator.Interpolator`.
Path chains / builder: NOT IN SOURCE.

## Drivetrain and localizer (direct use)

- `drivetrain.drive(new DrivePowers(forward, strafe, turn), boolean)` — `com.pedropathing.drivetrain.DrivePowers`;
  teleop test passes `(-left_stick_y, -left_stick_x, -right_stick_x)` with `true` (Tests.java:304).
  The meaning of the boolean is NOT IN SOURCE.
- `localizer.setPose(Pose)`, `localizer.update()`, `localizer.pose()` (Tests.java:297-306).
- Localizers (`com.pedropathing.revhub.localizers.*`), each `new X(hardwareMap, config)`:
  `PinpointLocalizer`/`PinpointConfig`, `OTOSLocalizer`/`OTOSConfig`, `OctoQuadLocalizer`/`OctoQuadConfig`,
  `TwoWheelLocalizer`/`TwoWheelConfig`, `ThreeWheelLocalizer`/`ThreeWheelConfig`,
  `ThreeWheelIMULocalizer`/`ThreeWheelIMUConfig`.
- Building a `Drivetrain` from `MecanumConfig` and an `Algorithm` from `ForesightConfig`: NOT IN SOURCE.

## Lambda configs (as emitted by the tuners)

```java
public static MecanumConfig drivetrainConfig = new MecanumConfig(c -> {          // MecanumTuner.java
    c.frontLeftName.set("..."); c.frontRightName.set("...");
    c.backLeftName.set("...");  c.backRightName.set("...");
    c.frontLeftDirection.set(DcMotorSimple.Direction.FORWARD);   // and frontRight/backLeft/backRight
});

public static PinpointConfig localizerConfig = new PinpointConfig(c -> {         // PinpointTuner.java:59-68
    c.name.set("pinpoint");
    c.podType.set(GoBildaPinpointDriver.GoBildaOdometryPods.goBILDA_4_BAR_POD);  // or c.ticksPerUnit.set(OptionalDouble.of(..)) for custom pods
    c.xPodOffset.set(..); c.yPodOffset.set(..);
    c.xPodDirection.set(GoBildaPinpointDriver.EncoderDirection.FORWARD);
    c.yPodDirection.set(GoBildaPinpointDriver.EncoderDirection.FORWARD);
    c.globalDistanceUnit.set(DistanceUnit.INCH);
    c.offsetUnits.set(DistanceUnit.INCH);
});

public static ForesightConfig foresightConfig = new ForesightConfig(c -> {      // ForesightTuner.java:96-121
    c.forwardTranslational.set(Controller.piecewise(Controller.proportional(secondary)).put(2.5, Controller.proportional(primary)));
    c.strafeTranslational.set(/* same shape, strafe gains */);
    c.coast.set(Controller.proportionalFeedforward(coastKV));
    c.brake.set(Controller.proportionalFeedforward(brakeKV));
    c.headingFeedback.set(Controller.proportional(headingKP));
    c.headingBrakeCoefficients.set(Vector2D.cartesian(headingLinear, headingQuadratic));
    c.linearBrakeCoefficients.set(Matrix.diag(forwardLinear, strafeLinear));
    c.quadraticBrakeCoefficients.set(Matrix.diag(forwardQuadratic, strafeQuadratic));
    c.maxAchievableForwardVelocity.set(..); c.maxAchievableStrafeVelocity.set(..);
    c.naturalForwardDeceleration.set(..);   c.naturalStrafeDeceleration.set(..);
});
```

Every number above is a **tuner output for one specific robot** — record each as
`origin: measured` only after running the tuner on this robot, otherwise `origin: untuned, value: null`
(standing-principles §13).

## Tuner result keys (`result(...)` names — use these when recording tuning_constants)

| Procedure | Keys |
|---|---|
| Mecanum Tuner | `frontLeftName`, `frontRightName`, `backLeftName`, `backRightName`, `frontLeftDirection`, `frontRightDirection`, `backLeftDirection`, `backRightDirection` |
| Pinpoint Tuner | `name`, `podType`, `ticksPerUnit` (custom pods only), `xPodDirection`, `yPodDirection`, `xPodOffset`, `yPodOffset` |
| Foresight Tuner (ForesightTuner.java:78-94) | `maxAchievableForwardVelocity`, `maxAchievableStrafeVelocity`, `naturalForwardDeceleration`, `naturalStrafeDeceleration`, `headingBrakingLinearCoefficient`, `headingBrakingQuadraticCoefficient`, `heading kP`, `forwardBrakingLinearCoefficient`, `forwardBrakingQuadraticCoefficient`, `strafeBrakingLinearCoefficient`, `strafeBrakingQuadraticCoefficient`, `forwardTranslational Primary kP`, `forwardTranslational Secondary kP`, `strafeTranslational Primary kP`, `strafeTranslational Secondary kP`, `coast kV`, `brake kV` |
| Tests | `Completed` (Hold / Line / Curve / Interpolation / Localization / Odometry / Driving / Pose tests) |

Procedure order implied by dependencies: drivetrain (Mecanum Tuner) and localizer (e.g. Pinpoint
Tuner) first — the Foresight Tuner takes both as constructor arguments; `Tests` needs all three.
How procedures are registered (`Tuning.java` ships as `// Tuners go here`): NOT IN SOURCE.
