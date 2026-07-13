> Source: https://pedropathing.com/docs/pathing/tuning · Fetched: 2026-07-12

# Pedro Pathing — Tuning Overview

> Source: https://pedropathing.com/docs/pathing/tuning · Fetched: 2026-07-12

## Tuning

#### Setup

In this step, you set constants for your follower.

#### Swerve

In this step, you set constants such as your motor names and directions for swerve (if using swerve).

#### Localization

This allows for your robot to know its location on the field.

#### Velocity Tuners

 Determines the forward vs lateral velocity of your robot.

#### Heading Tuner

The heading PIDF corrects for the robot's heading while following the path.

After setting up, you have to decide which following algorithm you would like to use.

##### New **predictive braking**

Which automatically tunes in a few minutes and has faster but less customizable braking. Only requires running the automatic PredictiveBrakingTuner and determining a P value.
Tuning process is here: [Tuning Predictive Braking](https://pedropathing.com/docs/pathing/tuning/drive-algorithm/predictive/configuration)

#### OR

##### **PIDFs** of translational, drive, and centripetal

Which requires 3 manual tuners and two more automatic tuners.
Allows for more control of the robot's behavior.
These are the steps for tuning the PIDFs:

#### Zero Power Acceleration Tuners

These tuners automatically determine the natural deceleration behavior of your robot.

#### PIDF Tuners

This step is where you tune translational and drive PIDFs.

#### Centripetal Force Tuner

This step consists of tuning a constant that accounts for
centripetal force.

---

> Source: https://pedropathing.com/docs/pathing/tuning/setup · Fetched: 2026-07-12

## Setup

### Setting your robot's mass

Your robot's mass is used to compensate for centripetal force. To set the
mass, simply add `.mass` in `FollowerConstants`. Note that the mass **must
be in kilograms**.

```java title="Constants.java"
public static FollowerConstants followerConstants = new FollowerConstants()
        .mass(5);
```

> **Tip:**
> If you don't have a large enough scale to weigh your robot, you can stand on
> the scale while holding your robot and then subtract your own weight.

### Adding drivetrain constants

Next, we will add our drivetrain constants. These include motor names, motor
directions, and the max power. The max power must be a number from 0 to 1.

#### Swerve
If you have a swerve drivetrain, please refer to the dedicated [swerve page](/docs/pathing/tuning/swerve/swerve-setup)
for tuning instructions.

#### Mecanum

If you have a mecanum drivetrain, add the following to your `Constants` class.

```java title="Constants.java"
public static MecanumConstants driveConstants = new MecanumConstants()
        .maxPower(1)
        .rightFrontMotorName("rf")
        .rightRearMotorName("rr")
        .leftRearMotorName("lr")
        .leftFrontMotorName("lf")
        .leftFrontMotorDirection(DcMotorSimple.Direction.REVERSE)
        .leftRearMotorDirection(DcMotorSimple.Direction.REVERSE)
        .rightFrontMotorDirection(DcMotorSimple.Direction.FORWARD)
        .rightRearMotorDirection(DcMotorSimple.Direction.FORWARD);
```

> **Important:**
> Make sure that your motor names and directions are correct. It's likely
> that you will have to reverse one side!

Then, add the mecanum drivetrain to the follower builder in `createFollower`:

```java title="Constants.java"
public static Follower createFollower(HardwareMap hardwareMap) {
        return new FollowerBuilder(followerConstants, hardwareMap)
                .pathConstraints(pathConstraints)
                .mecanumDrivetrain(driveConstants)
                .build();
}
```

---

> Source: https://pedropathing.com/docs/pathing/tuning/heading · Fetched: 2026-07-12

## Heading

#### Setup

1. Open Panels. If you haven't used Panels before, you can read the documentation on the [Panels Configurables](https://panels.bylazar.com/docs/com.bylazar.configurables/).
2. On your Driver Hub or Driver Station, select the `Tuning` Opmode and then choose `HeadingTuner`.
3. Ensure that the timer for autonomous OpModes is **disabled.** Otherwise, the OpMode will automatically stop after 30 seconds.
4. Run the `HeadingTuner` autonomous OpMode.

**Note that while running the `Heading Tuner` OpMode, the robot will stay in place. This is intentional.**

### Tuning Process
Follow this video to help you tune the PIDF(s):

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/-7M8puRdnfA?si=3jmMW5fJTCw5hOr_" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>

1. Turn the robot left or right at varying amounts and observe how the robot turns back to its starting heading.
2. Adjust the PIDF constants (`coefficientsHeadingPIDF`) in the `Tuning`-> `Follower` -> `Constants` section of Panels Configurables to ensure that the robot can **accurately correct** back to its starting position with **minimal oscillations.** For example, if the robot has too many oscillations while correcting back to its starting position, lower the P value. On the other hand, if the robot corrects back to its starting location too slowly, increase the P value.
**If you do not have prior experience with tuning PIDFs, we recommend that you check out the resources provided at the bottom of the PIDF Tuners page to learn more about tuning these.**

**If you have a dual PIDF system enabled,** it is recommended to first tune the main PIDF, `coefficientsHeadingPIDF`, to ensure that the robot can smoothly correct back from large errors. Then, tune the secondary PIDF, `coefficientsSecondaryHeadingPIDF`, so the robot can smoothly correct from smaller errors.

> **Warning!:**
> After adjusting a value in Panels, **hit "enter"** in order to save it and cause the robot to correct differently. However, any values you modify through Panels **are not saved into your code!** In order to transfer the values you just tuned on Panels into your code, go to the **Update Tuned Values** section to learn more.

#### Feedforward Adjustments (Optional)

If additional feedforward is needed, use the feedforward term directly in the `coefficientsHeadingPIDF` and/or `coefficientsSecondaryHeadingPIDF` if
you are using dual PID.

- The feedforward term applies a minimum power output to the motors to compensate for the friction between the motors, wheels, and the ground.
- To tune the feedforward, set all other PIDF values to 0 and increase the Feedforward value up until the robot starts moving/jittering.

#### Update Tuned values Into Your Code
1. Once you are satisfied with your headingPIDF values, head over to the `Constants` file, and navigate to the `FollowerConstants` instantiation.
2. Navigate to or add the line `.headingPIDFCoefficients(new PIDFCoefficients(0.1, 0, 0.01, 0))`
3. Update the parameters in `new PIDFCoefficients(0.1, 0, 0.01, 0)` with the `headingPIDFCoefficients` values, `P, I, D, F`, you tuned on Panels in that order.
4. If you are using the dual PIDF system, **add the line** `.secondaryHeadingPIDFCoefficients(new PIDFCoefficients(0.1,0,0.01,0))` and update the `secondaryHeadingPIDF` values you tuned on Panels.

### Troubleshooting
If you encounter a problem while tuning the heading PIDF, check out the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/velocity · Fetched: 2026-07-12

## Velocity Tuners

### Forward Velocity Tuner

> **Purpose:**
> The Forward Velocity Tuner determines the velocity of your robot when moving forward at full power.
> This value is used for accurate path-following calculations in Pedro Pathing.

First, make sure you have enough room. By default, the robot moves 48 inches forward, but this can be
changed by navigating to the `ForwardVelocityTuner` class in `Tuning.java`. Typically larger numbers yield
better results. Then, in the Tuning OpMode, under automatic, select and start Forward Velocity Tuner. The
robot speed should ramp up until it reaches full power. It will continue moving until it has reached the set distance,
then it will abruptly stop.

Once the robot stops moving at maximum speed, one number will be displayed on telemetry:

- Velocity: The final velocity the robot achieved before stopping; this is what we want

Add the velocity to `MecanumConstants` by adding or editing the following.

```java title="Constants.java"
.xVelocity(velocity)
```

### Lateral Velocity Tuner

> **Purpose:**
> The Lateral Velocity Tuner determines the velocity of your robot when moving sideways at full power.
> This value is used for accurate path-following calculations in Pedro Pathing.

First, make sure you have enough room. By default, the robot moves 48 inches to the left, but this can be
changed by navigating to the `LateralVelocityTuner` class in `Tuning.java`. Typically larger numbers yield
better results. Then, in the Tuning OpMode, under automatic, select and start Lateral Velocity Tuner. The
robot speed should ramp up until it reaches full power. It will continue moving until it has reached the set distance,
then it will abruptly stop.

Once the robot stops moving at maximum speed, one number will be displayed on telemetry:

- Velocity: The final velocity the robot achieved before stopping; this is what we want

Add the velocity to `MecanumConstants` by adding or editing the following.

```java title="Constants.java"
.yVelocity(velocity)
```

---

> Source: https://pedropathing.com/docs/pathing/tuning/tests · Fetched: 2026-07-12

## Tests

To validate your tuning, it is prudent to try running at least one of these tests.
They are runnable via the Tuning class and using the gamepad to the `Tests` folder.

### Line
Line Test is used to analyze the follower's capability of driving with all of the PIDFs active at once.
This helps determine if any PIDF(s) need adjusting.
The follower will drive 48 inches forward (two tiles) and then back to the initial position. It will loop this action.

### Triangle
Triangle Test is used to ensure that the follower is capable of straight line interpolation.
This helps determine if any PIDF(s) need adjusting.
The follower will drive in a triangle path, looping infinitely.

### Circle
Circle Test is used to ensure that the follower is capable of curved path following.
This helps determine if any PIDF(s) or if the Centripetal Scaling needs adjusting.
The follower will drive in a circle path always facing the center, looping infinitely.

### Troubleshooting
If you encounter a problem while tuning, check out the [troubleshooting page](/docs/pathing/troubleshooting) and [FAQ](/docs/pathing/faq).

---

> Source: https://pedropathing.com/docs/pathing/tuning/automatic · Fetched: 2026-07-12

## Automatic Tuners

### Forward Velocity Tuner

> **Purpose:**
> The Forward Velocity Tuner determines the velocity of your robot when moving forward at full power.
> This value is used for accurate path-following calculations in Pedro Pathing.

First, make sure you have enough room. By default, the robot moves 48 inches forward, but this can be
changed by navigating to the `ForwardVelocityTuner` class in `Tuning.java`. Typically larger numbers yield
better results. Then, in the Tuning OpMode, under automatic, select and start Forward Velocity Tuner. The
robot speed should ramp up until it reaches full power. It will continue moving until it has reached the set distance,
then it will abruptly stop.

Once the robot stops moving at maximum speed, one number will be displayed on telemetry:

- Velocity: The final velocity the robot achieved before stopping; this is what we want

Add the velocity to `MecanumConstants` by adding or editing the following.

```java title="Constants.java"
.xVelocity(velocity)
```

### Lateral Velocity Tuner

> **Purpose:**
> The Lateral Velocity Tuner determines the velocity of your robot when moving sideways at full power.
> This value is used for accurate path-following calculations in Pedro Pathing.

First, make sure you have enough room. By default, the robot moves 48 inches to the left, but this can be
changed by navigating to the `LateralVelocityTuner` class in `Tuning.java`. Typically larger numbers yield
better results. Then, in the Tuning OpMode, under automatic, select and start Lateral Velocity Tuner. The
robot speed should ramp up until it reaches full power. It will continue moving until it has reached the set distance,
then it will abruptly stop.

Once the robot stops moving at maximum speed, one number will be displayed on telemetry:

- Velocity: The final velocity the robot achieved before stopping; this is what we want

Add the velocity to `MecanumConstants` by adding or editing the following.

```java title="Constants.java"
.yVelocity(velocity)
```

### Forward Zero Power Acceleration

> **Purpose:**
> Measures how your robot decelerates when moving forward and power is cut from the drivetrain.
> This value is critical for improving motion accuracy in Pedro Pathing.

First, make sure you have enough space to accelerate 30 in/s forward (roughly 1 tile). You can adjust this constraint
by navigating to `ForwardZeroPowerAccelerationTuner` in `Tuning.java`. Typically values closer to your
max forward velocity yield better results. Then, in the Tuning OpMode, under automatic, select and start Forward
Zero Power Acceleration Tuner. The robot will speed up until it reaches the commanded velocity, then cut power and measure the deceleration rate.

Once the robot stops moving, one number will be displayed on telemetry:

- Forward Zero Power Acceleration (Deceleration): The deceleration rate of the robot; this is what we want

Add the above number to `FollowerConstants` by adding or editing the following.

```java title="Constants.java"
.forwardZeroPowerAcceleration(deceleration)
```

### Lateral Zero Power Acceleration

> **Purpose:**
> Measures how your robot decelerates when moving lateral and power is cut from the drivetrain.
> This value is critical for improving motion accuracy in Pedro Pathing.

First, make sure you have enough space to accelerate 30 in/s to the left (roughly 1 tile). You can adjust this constraint
by navigating to `LateralZeroPowerAccelerationTuner` in `Tuning.java`. Typically values closer to your
max lateral velocity yield better results. Then, in the Tuning OpMode, under automatic, select and start `Lateral
Zero Power Acceleration Tuner`. The robot will speed up until it reaches the commanded velocity, then cut power and measure the deceleration rate.

Once the robot stops moving, one number will be displayed on telemetry:

- Lateral Zero Power Acceleration (Deceleration): The deceleration rate of the robot; this is what we want

Add the above number to `FollowerConstants` by adding or editing the following.

```java title="Constants.java"
.lateralZeroPowerAcceleration(deceleration)
```

Congratulations, you've completed all of the automatic tuners!

### Troubleshooting

If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

