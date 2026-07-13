> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/pidfs/tuning · Fetched: 2026-07-12

# Pedro Pathing — PIDF & Predictive Braking Tuning

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/pidfs/tuning · Fetched: 2026-07-12

## Tuning Overview

> **PIDFs vs. Predictive Braking:**
> You may either use PIDs or Predictive Braking to control your robot.
> However, swerve is currently not compatible with Predictive Braking.
> All further steps in the PIDFs section are for PIDFs users only.

Pedro Pathing relies on **Proportional-Integral-Derivative (PID)
controllers** to ensure precise path-following performance. The following pages
will walk you through tuning the various PID controllers for translational,
heading, and drive.

### Single vs. Dual PID System

In Pedro Pathing, you can choose between using one or two PID controllers for
each correction type (translational, heading, and drive).

#### Single PID System

In a single PID system, a single PID is responsible for managing all errors.
This is the simplest option and is the quickest to get started with.

Since a single PID system is the default, you don't have to do anything
special to use it.

#### Dual PID System

In a dual PID system, there is a **main PID** that handles larger errors and
a **secondary PID** for smaller corrections.

Advantages to using a dual PID system are:

- Better correction
- Scalable error thresholds
- Allows for more aggressive tuning

If you want to try using a dual PID system, it is recommended that you start
with drive, as it will contribute the most to a better auto.

To enable a dual PID system, set any of the following to `true` in
`FollowerConstants` in the
`Constants` file.

```java title="Constants.java"
.useSecondaryTranslationalPIDF(true)
.useSecondaryHeadingPIDF(true)
.useSecondaryDrivePIDF(true)
```

Then, tune both the main and secondary PIDs. The main PID should move the
error into the secondary PID's range without causing overshoot, and the
secondary PID should correct for small errors quickly and minimize oscillations.

### Tuning PIDs

Read the
[PID tuning page on CTRL ALT FTC](https://www.ctrlaltftc.com/the-pid-controller/tuning-methods-of-a-pid-controller)
to learn how to tune a PID controller. Addtionally, the following videos
demonstrate how to tune a PID.

<iframe className="mb-5" width="560" height="315"
        src="https://www.youtube-nocookie.com/embed/qKy98Cbcltw?si=8HYnqB9XWWTazdMe"
        title="YouTube video player" frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen></iframe>

<iframe width="560" height="315"
        src="https://www.youtube-nocookie.com/embed/uXnDwojRb1g?si=Zy53je8jd2naUW7a"
        title="YouTube video player" frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen></iframe>

---

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/pidfs/translational · Fetched: 2026-07-12

## Translational

#### Purpose

The translational PIDF ensures the robot follows a straight path without lateral deviation.

### Setup

1. Open Panels. If you haven't used Panels before, you can read the documentation on the [Panels](https://panels.bylazar.com/docs/com.bylazar.configurables/).
2. On your Driver Hub or Driver Station, and connect a gamepad to it. Make sure to press "start" + "a" on the gamepad.
3. Select the `Tuning` Opmode. Use your gamepad to select the `Manual` folder. Then, select `Translational Tuner`.
4. Run the run the OpMode.

**Note that while running the `Translational Tuner` OpMode, the robot will stay in place. This is intentional.**

### Tuning Process

Follow this video to help you tune the PIDF(s):

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/qe2eo_Mhtes?si=DMqud3FSZ2j5AmPu" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>

1. Push the robot left or right at varying amounts and observe how the robot corrects back to its starting position.
2. Adjust the PIDF constants (`coefficientsTranslationalPIDF`) in the `Tuning`-> `Follower` -> `Constants` section of Panels Configurables to ensure that the robot can **accurately correct** back to its starting position with **minimal oscillations.** For example, if the robot has too many oscillations while correcting back to its starting position, try lowering the P value. On the other hand, if the robot corrects back to its starting location too slowly, increase the P value.
**If you do not have prior experience with tuning PIDFs, we recommend that you check out the resources provided at the bottom of the PIDF Tuners page to learn more about tuning these.**

**If you have a dual PIDF system enabled,** it is recommended to first tune the main PIDF, `coefficientsTranslationalPIDF`, to ensure that the robot can correct from large errors and bring it within the secondary PID's range. Then, tune the secondary PIDF, `coefficientsSecondaryTranslationalPIDF`, so the robot can smoothly correct from smaller errors and minimize oscillations.

> **Tuning Tips:**
> Don't worry if the robot does not correct its heading. We are only tuning translational PIDF: whether the robot corrects left/right appropriately.

> **Warning!:**
> After adjusting a value in Panels, **hit "enter"** in order to save it and cause the robot to correct differently. However, any values you modify through Panels **are not saved into your code!** In order to transfer the values you just tuned on Panels into your code, go to the **Update Tuned Values** section.

#### Feedforward Adjustments (Optional)

If additional feedforward is needed, use the feedforward term directly in the `coefficientsTranslationalPIDF` and/or `coefficientsSecondaryTranslationalPIDF` if
you are using dual PID.

- The feedforward term applies a minimum power output to the motors to compensate for the friction between the motors, wheels, and the ground.
- To tune the feedforward, set all other PIDF values to 0 and increase the Feedforward value up until the robot starts moving/jittering.

#### Update Tuned values Into Your Code

1. Once you are satisfied with your translationalPIDF values, head over to the `Constants` file, and navigate to the `FollowerConstants` instantiation.
2. Navigate to or add the line `.translationalPIDFCoefficients(new PIDFCoefficients(0.1, 0, 0.01, 0))`
3. Update the parameters in `new PIDFCoefficients(0.1, 0, 0.01, 0)` with the `translationalPIDFCoefficients` values, `P, I, D, F`, you tuned on Panels in that order.
4. If you are using the dual PIDF system, **add the line** `.secondaryTranslationalPIDFCoefficients(new PIDFCoefficients(0.1,0,0.01,0))` and update the `secondaryTranslationalPIDF` values you tuned on Panels.

### Troubleshooting

If you encounter a problem while tuning the translational PIDF, check out the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/pidfs/centripetal · Fetched: 2026-07-12

## Centripetal

#### Purpose

The centripetal force correction enables the robot to accurately follow curved paths.

#### Setup

1. Set your robot's mass
Your robot's mass is used to compensate for centripetal force. To set the
mass, simply add `.mass` in `FollowerConstants`. Note that the mass **must
be in kilograms**.

```java title="Constants.java"
public static FollowerConstants followerConstants = new FollowerConstants()
        .mass(5);
```
2. Open Panels. If you haven't used Panels before, you can read the documentation on [Panels Configurables](https://panels.bylazar.com/docs/com.bylazar.configurables/).
3. On your Driver Hub or Driver Station, select the `Tuning` Opmode, navigate to `Manual` and then choose `CentripetalTuner`.
4. Ensure that the timer for autonomous OpModes is **disabled.** Otherwise, the OpMode will automatically stop after 30 seconds.
5. Run the run the `CentripetalTuner` autonomous OpMode.

> **Warning!:**
> - Immediately after running the `Centripetal Tuner` Opmode, the robot will move forward and left 20 inches in a curved path. Make sure you have enough space before running this opmode.
> - You can adjust the distance the robot drives back and forth through Panels.

### Tuning Process
Follow this video to help you tune the centripetal scalar:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/728GLkqy9yY?si=YFZ0iWha6KqztOsH" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>

Observe the robot’s path:

- If the robot corrects towards the inside of the curve, decrease `centripetalScaling`.
- If the robot corrects towards the outside of the curve, increase `centripetalScaling`.
Adjust the value of `centripetalScaling` within the `Tuning`-> `Follower` -> `Constants` section in Panels.

#### Update Tuned values Into Your Code
1. Once you are satisfied with your `centripetalScaling`, head over to the `Constants` file.
2. Navigate to the line `.centripetalScaling(0.005)` under `followerConstants`. If you don't have this line, feel free to add it yourself.
3. Update the parameters in `.centripetalScaling(0.005)` with the `centripetalScaling` value you tuned.

### Troubleshooting
If you have any problems, see the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/pidfs/drive · Fetched: 2026-07-12

## Drive

#### Purpose

The Drive PIDF manages acceleration and braking along a path, ensuring smooth motion and minimizing overshoot.

### Setup

1. Open Panels. If you haven't used Panels before, you can read the documentation on the [Panels Configurables](https://panels.bylazar.com/docs/com.bylazar.configurables/).
2. On your Driver Hub or Driver Station, and connect a gamepad to it. Make sure to press "start" + "a" on the gamepad.
3. Select the `Tuning` Opmode. Use your gamepad to select the `Manual` folder. Then, select `Drive Tuner`.
4. Run the run the OpMode.

> **Warning!:**
> - **Immediately after running the `Drive Tuner` Opmode, the robot will move straight back and forth 40 inches. Make sure you have enough space before running this opmode.** You can adjust the distance the robot drives back and forth through Panels.
> - **The robot WILL move laterally and/or change its heading. This is expected behavior since the translational and heading PIDFs are not activated.** If both translational and heading PIDFs are tuned, consider using the `Line Tuner` to ensure the robot stays on the line.

### Tuning Process

#### Setting the BrakingStrength

Before tuning the Drive PIDF, we will need to set the BrakingStrength. Head over to the [deceleration page](/docs/pathing/reference/deceleration) to learn more about it.

The BrakingStrength you set in the `Constants` class will be the default BrakingStrength for all paths the robot follows.

1. Observe how the robot moves back and forth through its path.
2. Adjust the PIDF constants (`coefficientsDrivePIDF`) in the `Tuning`-> `Follower` -> `Constants` tab of Panels Configurables to ensure that the robot smoothly and accurately drives straight back and forth.

> **Tuning Tips:**
> -  PedroPathing does not activate heading and translational PIDF correction for drive tuning. If you would like to test all three of them, navigate yourself to the `Line Tuner` in the `Manual` folder. Use it to adjust `BrakingStrength`, path constraints and making sure all PIDFs are working well together.
> - Increasing your drive PIDF will make the robot move more quickly along the path, at the risk of more overshoot at the end of the path.
> - Decreasing your drive PIDF will make the robot move more slowly and reduce the overshoot at the end of the path.
> - Adjusting the `BrakingStrength` can significantly help manage how smoothly the robot decelerates as it reaches the end of its path.
> - If the robot drives quickly during the middle of the path but abruptly slows down as it reaches the end of the path, this may be caused by the transition between the main and secondary PIDs. This problem may also be addressed through lowering the BrakingStrength.

**If you do not have prior experience with tuning PIDFs, we recommend that you check out the resources provided at the bottom of the PIDF Tuners page to learn more about tuning these.**

**If you have a dual PIDF system enabled,** it is recommended to first tune the main PIDF, `coefficientsDrivePIDF` before tuning the secondary PIDF, `coefficientsSecondaryDrivePIDF`.

> **Warning!:**
> After adjusting a value in Panels, **hit `Enter`** in order to save it and cause the robot to correct differently. However, any values you modify through Panels **are not saved into your code!** In order to transfer the values you just tuned on Panels into your code, go to the **Update Tuned Values** section to learn more.

#### Braking Start (Optional)

Braking Start determines when the robot starts braking when global deceleration (deceleration upon the entire PathChain) is active.
Braking Start can be adjusted just like BrakingStrength.

#### Feedforward Adjustments (Optional)

If additional feedforward is needed, use the feedforward term directly in the `coefficientsDrivePIDF` and/or `coefficientsSecondaryDrivePIDF` if
you are using dual PID.

- The feedforward term applies a minimum power output to the motors to compensate for the friction between the motors, wheels, and the ground.
- To tune the feedforward, set all other PIDF values to 0 and increase the Feedforward value up until the robot starts moving/jittering.

#### Kalman Filter Adjustments (Optional)

The drive PID uses a Kalman filter to smooth error responses:

- Model Covariance: Default is `6`.
- Data Covariance: Default is `1`.
- A higher model covariance to data covariance ratio will cause the filter to rely on the previous output rather than the data (raw drive error).
- A lower model covariance to data covariance ratio will cause the filter to rely on the data rather than the previous output
- To modify these values, add the line `FollowerConstants.driveKalmanFilterParameters(6, 1)` in your `Constants` file and replace the parameters with the desired ones.

The drive PID also has a filter such that the derivative term is a weighted average of the
  current derivative and the previous derivative.

- The default time constant `T` for the
  drive filtered PID is 0.6, meaning that the derivative output is 0.6 times the previous derivative plus 0.4
  times the current derivative.
- You can modify this value by changing the **fourth** parameter in the `drivePIDFCoefficients(P, I, D, T, F)`.

Feel free to experiment with these settings for optimal performance.

#### Update Tuned values Into Your Code

1. Once you are satisfied with your drivePIDF values, head over to the `Constants` file, and navigate to the `FollowerConstants` instantiation.
2. Navigate to or add the line `.drivePIDFCoefficients(new FilteredPIDFCoefficients(0.1,0.0,0.01,0.6,0.0))`
3. Update the parameters in `new FilteredPIDFCoefficients(P, I, D, T, F)` with the `drivePIDFCoefficients` values, `P, I, D, F`, you tuned on Panels.
4. If you are using the dual PIDF system, **add the line** `.secondaryDrivePIDFCoefficients(new FilteredPIDFCoefficients(0.1,0,0.01,0.6,0.01))` and update the `secondaryDrivePIDF` values you tuned on Panels.

### Troubleshooting

If you encounter a problem while tuning the Drive PIDF, check out the [troubleshooting page](/docs/pathing/troubleshooting).

---

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/pidfs/zero-power-accel · Fetched: 2026-07-12

## Zero Power Acceleration

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

---

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/predictive/about · Fetched: 2026-07-12

## What is Predictive Braking?

Instead of relying on a manually tuned derivative term to prevent overshoot, this controller predicts how far the robot will slide if it brakes using a small negative voltage. It uses the predicted braking distance to anticipate positional error, effectively treating it as reaction time. This allows the robot to brake precisely when needed, maximizing deceleration and accuracy.

Learn more about Predictive Braking: http://pedropathing.com/docs/pathing/reference/predictive

## Why use Predictive Braking?

Using this method, a world-record autonomous was achieved, and many other teams' autos were also sped up by **~15%**, all while automatically tuning in a few minutes.

Predictive Braking is a new, optional algorithm for following paths that replaces the old translational and drive PIDFs.

The old PIDFs are still supported, but predictive braking is much easier to tune because the algorithm automatically tunes and maximizes the deceleration speed and accuracy of your robot.

#### Predictive Braking Autonomous Example
<iframe
  width="560"
  height="315"
  src="https://www.youtube-nocookie.com/embed/CcmMqLvqVk4"
  title="Predictive Braking Autonomous Example"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

---

> Source: https://pedropathing.com/docs/pathing/tuning/drive-algorithm/predictive/configuration · Fetched: 2026-07-12

## Tuning Predictive Braking

> **PIDFs vs. Predictive Braking:**
> You may either use PIDFs or Predictive Braking to control your robot.
> However, swerve and tank are currently not compatible with Predictive Braking.
> All further steps are for Predictive Braking users only.

1. Run the Tuning.java OpMode -> Automatic -> PredictiveBrakingTuner. This will give you values for `kQuadratic` and `kLinear`. In FollowerConstants, add `.predictiveBrakingCoefficients(new PredictiveBrakingCoefficients(kP, kLinear, kQuadratic))`. Insert the values given from the tuner into the method. Use a starting kP value around `0.1`.
 - `kQuadratic` represents the braking distance proportional to velocity squared. This is caused by constant forces such as braking power and sliding friction.
 - `kLinear` represents braking distance roughly proportional to velocity. This is caused by velocity-proportional forces such as back-EMF, torque delay, and viscous friction.

<iframe
  width="560"
  height="315"
  src="https://www.youtube-nocookie.com/embed/4JbpJi-8MOQ"
  title="PredictiveBrakingTuner"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

Do not be worried if the robot's heading turns while braking in the tuner. This is expected and does not hurt the results. Consider making a more balanced center of mass to combat this. In the future, the tuner will have heading correction.

Also do not be worried if your robot lifts off the ground while braking. This is normal as long as odometry can still get accurate measurements.

2. Run LineTest and adjust kP to your liking. kP usually ranges from `0.05-0.3`. kP changes are harder to notice and have minimal effects due to kP accounting for predicted error. However, tune kP as high as possible to maximize holding strength and accuracy, without jittering the robot. If you want smoother or sooner deceleration, try experimenting with kP of 0.05 or lower and increasing the kQuadratic term, as this will act more like a motion profile.

3. Currently, it is recommended to turn **off centripetal** forces in auto, as predictive braking naturally accounts for this. This can be done by adding the following in FollowerConstants.
```java title="Constants.java"
.centripetalScaling(0)
```

4. **Lower the parametric end constraint**. Set it to a value like 0.97 or 0.95. PIDFs often overshoot and hit the parametric end early, but predictive braking fully stops in time, delaying when actions can trigger. Lowering the constraint lets actions trigger sooner and speeds up overall execution. However, do not set the parametric value very low (\<0.9) or predictive braking will not work as intended because it will end the path before braking.

At the end of tuning, you should have at least this in FollowerConstants.
```java title="Constants.java"
 public static FollowerConstants followerConstants = new FollowerConstants()
     .headingPIDFCoefficients(new PIDFCoefficients(1.5, 0, 0.1, 0)) // tuned constants
     .predictiveBrakingCoefficients(new PredictiveBrakingCoefficients(0.1, 0.04, 0.0016)) // (kP, kLinear, kQuadratic)
     .centripetalScaling(0)
```

#### After tuning, the LineTest should look like this video
<iframe
  width="560"
  height="315"
  src="https://www.youtube-nocookie.com/embed/4g8-_Toy388"
  title="Predictive Braking LineTest"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

### Effective Predictive Braking with Pathing
If you run a previously constructed autonomous, you will see that predictive braking effectively eliminates overshoot, but it may slow down your auto if you do not continue pathchains. This is because predictive braking comes to a complete stop when using individual paths. If you instead use pathchains wherever you do not need to fully stop, the robot will maintain its momentum. Future updates will allow smooth handling of sharp angles without stopping by predicting the next path automatically.

