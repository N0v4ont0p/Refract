> Source: https://pedropathing.com/docs/pathing/tuning/swerve/swerve-setup · Fetched: 2026-07-12

# Pedro Pathing — Swerve Drivetrain Setup & Tuning

> Source: https://pedropathing.com/docs/pathing/tuning/swerve/swerve-setup · Fetched: 2026-07-12

## Swerve Setup

### Swerve Constants

Next, we will create our drivetrain constants and construct our pods.

```java title="Constants.java"
public static SwerveConstants swerveConstants = new SwerveConstants()
        .maxPower(1) //determines the max power of the drivetrain
//      .zeroPowerBehavior(SwerveConstants.ZeroPowerBehavior.IGNORE_ANGLE_CHANGES)
        //the above disables x locking for swerve, which can be useful for tuning pod offsets
```

### Constructing Pods

Now we will construct our `SwervePod` instances (`SwervePod` is an interface).
Pedro has two built-in implementations of `SwervePod`, `CoaxialPod` and `DiffyPod`.
To set up your drivetrain, you will need to create a method to construct each of your pods, which you
will then pass into the swerve drivetrain.

An example of a method creating a `CoaxialPod` is shown below.

```java title="Constants.java"
private static CoaxialPod leftFront(HardwareMap hardwareMap) {
    CoaxialPod pod = new CoaxialPod(
            hardwareMap,
            "leftFrontMotor", //the name of your motor in your config
            "leftFrontServo", //the name of your servo in your config
            "leftFrontEncoder", // the name of your analog encoder in your config
            new PIDFCoefficients(0.3, 0, 0.005, 0.01), //pod PIDF coefficients
            DcMotorSimple.Direction.FORWARD, //the direction of your motor
            DcMotorSimple.Direction.FORWARD, //the direction of your servo
            Math.toRadians(353.1), //your pod's angle offset, in radians
            new Pose(dtLength, dtWidth), //your pods x and y offsets,
                                         // in pedro coordinates (like with deadwheels)
            0 //analog min voltage
            3.3, //analog max voltage
            false); //encoder inverted
//  uncomment the below lines to change caching thresholds (by default 0.01)
//  pod.setMotorCachingThreshold(0.05);
//  pod.setServoCachingThreshold(0.05);
    return pod;
}
```
Now we can update the createFollower method to take in our SwerveConstants and each `SwervePod` (you need to create a method for each pod).

```java title="Constants.java"
public static Follower createFollower(HardwareMap hardwareMap) {
        return new FollowerBuilder(followerConstants, hardwareMap)
                .pathConstraints(pathConstraints)
                .swerveDrivetrain(swerveConstants,
                    leftFront(hardwareMap),
                    rightFront(hardwareMap),
                    leftBack(hardwareMap),
                    rightBack(hardwareMap))
                .build();
}
```

---

> Source: https://pedropathing.com/docs/pathing/tuning/swerve/swerve-tuning · Fetched: 2026-07-12

## Swerve Tuning

### Analog Encoder Min / Max Voltage

> **Note:**
> For this opmode, and this one only, you will need to modify the `Tuning.java` file to match your encoder names to your config.
> Modify the `encoderNames` array on line 1440.

To get the best performance out of your drivetrain, you need to be able to get the angle of your servos to high precision.
Most coaxial swerve drivetrains in FTC use the analog encoders on their rotation servos to get the angle. In theory, the analog
values should vary between 0 and 3.3V, but in practice the min and max voltages are often close but not exactly those.

To get the most precision out of your pods, you want to get the actual minimum and maximum voltages of your encoders.
To do this, run `Analog Min / Max Tuner` in the swerve section of the `Tuning` opmode. After you press start, slowly rotate each
pod four to five full rotations. The min and max voltages of each pod should be printed to telemetry.

Once you have the values for each pod, put them into your each of your pod creation methods in `Constants.java`.

### Angle Offset Tuning
Next, we need to tune the angle offset of each pod. After you have tuned the min and max voltages, a full rotation of each pod should map to
exactly 360 degrees. However, the code still needs to know the precise angle at a specific position. To do this, you add angle offsets to each pod,
which is the raw angle of the pod in radians when they are at your desired zero position (facing forward).

To tune this, first temporarily disable x lock for the drivetrain (set the zero power behavior to IGNORE_ANGLE_CHANGES). Then, run `LocalizationTest`
in the `Tuning` opmode, making sure to enable the drivetrain debug string by pressing a on the gamepad when prompted. Then, manually line up each pod
to your zero position, facing the pod forward. The raw angle of each pod will be printed to telemetry. Insert the raw angle (in radians) when the pod
is at the zero position as the angle offset for that pod.

> **Tip:**
> Be consistent with how you define "forward" for each pod, flipping the pod 180 degrees changes the offset. While it doesn't strictly matter, being
> consistent (for example having all your bevel gears face left) will make debugging easier if problems arise.

### Motor Directions
After you put your angle offsets in, we need to confirm that they are correct and that the motors are reversed correctly. First, if you haven't already,
put in the placeholder pod PIDF coefficients for each pod (kP = 0.3, kI = 0, kD = 0.005, kF = 0).
Then, run `Swerve Offsets Test` in the `Tuning` opmode (do this off the ground, the servos and motors will spin). This opmode will attempt to drive each pod to its zero position. However, there are a few
expected reasons for this to fail. Follow these debug steps for each type of failure:
1. **The pods oscillate a lot**: By far the most common issue here is that your servos (not encoders) need to be reversed. Reverse your servos
and try again. If the issue persists, try turning down the default PIDF coefficients and see if that helps.
2. **The servos move to the wrong position**: First, check that the servos are holding their positions. It's possible that they are trying to move
to the zero position but the default PIDF coefficients aren't strong enough to get them there. Give them a nudge towards their zero positions and see
if they move easily towards it. If so, turn up the PIDF coefficients and try again. Otherwise, you probably set up bad angle offsets. Repeat the Angle
Offset Tuning steps above to make sure they are correct. If neither of those steps work, it's likely that the servos are not plugged in correctly to their
corresponding encoders. Ensure that the servo and encoder ports match up.
3. **The servos don't move at all**: If the servos don't move at all, it's possible that the servos aren't plugged in correctly or that the pod PIDF
coefficients are too low. Make sure that they are plugged in correctly, and then try turning up the PIDF coefficients and see if that helps.

If none of the above steps get the servos move to their zero positions, then you probably have an issue with wiring. Go through and make sure
that all of your servo, encoder, and motor wires are plugged in to the correct ports.

Once all your servos move to their zero positions, now you can check the directions of your motors. The pods should all be rotating to move the robot forward
(regardless of whether the pods are facing forward or backward). Reverse all the motors in pods that are turning the wrong direction.

If you have completed all of the above steps correctly, when running `Swerve Offsets Test`, the robot should drive forward slowly when you put it on the ground.

### Lateral Offsets
Now you need to find in your lateral offset (as a Pose). These not tuned, but found through measurement on the robot or CAD. Lateral offsets represent
the relative position of the pod to the center of the robot using pedro's coordinate system (positive x is forward, positive y is left). The nice thing
about these is that the offsets are normalized, meaning only the relative x and y values matter (i.e. `new Pose(1,1)` and `new Pose(1000, 1000)` are
the same). Thus, I've found that the easiest way to do these is to measure the length and width of your robot drivetrain. If you do that and store
the values in two variables `dtLength` and `dtWidth`, your offsets will be as follows (assuming your swerve is rectangular):
* Front Left: `new Pose(dtLength, dtWidth)`
* Front Right: `new Pose(dtLength, -dtWidth)`
* Back Left: `new Pose(-dtLength, dtWidth)`
* Back Right: `new Pose(-dtLength, -dtWidth)`

I'm super specific with these is because these are easy to get right if you're appropriately careful but annoying to debug if you mess them up.

### Encoder Directions
Next, we need to confirm that the encoders are reversed correctly. First, take your robot off of the ground such that you can see the wheels:
then, run `Swerve Turn Test` in the `Tuning` opmode's swerve section. Your pods should turn to be perpendicular to the center of the robot, forming
an "O" shape so the robot can turn. If your pods all turn towards the center and form an "X" shape, then reverse all of your encoders (flip the boolean
parameter) and try again.

Once your pods face the correct direction, ensure that the motors are all running the correct direction to turn the robot counterclockwise. If any of
the motors are running the wrong direction, but they are all correct for the `Swerve Offsets Test` to move your robot forward, then you almost certainly
have a wiring issue. Make sure that all of your motors correctly match up with their corresponding servos and encoders in your config. If that still
doesn't work, check your lateral offsets.

### Pod PIDF Tuning
Finally, you need to tune your pod PIDF coefficients. You can do this using whatever method you prefer to tune your PIDFs. What I've found to work
best is to use LocalizationTest to set target positions, and first tune P and D while the robot is off the ground. Once you've tuned to your satisfaction,
move the robot onto the ground and tune F to account for the friction with the tiles and fine tuning P and D. For my bot, I've used the same P and D
for all four pods, but I have separate F values for the front and back pods because my robot is back heavy. You should adjust this for your robot's
weight distribution, and some teams prefer to tune the P, D, and F values for each pod individually.

> **Note:**
> Remember to reenable x-lock after you are done if you want it (recommended). Just comment out the `IGNORE_ANGLE_CHANGES` line in `Tuning.java`,
> or you can explicitly set the zero power behavior to `X_LOCK`.

### Tips for Tuning
Congratulations! You've now completed the swerve-specific tuning steps. You can now move onto [localization tuning](/docs/pathing/tuning/localization)
and the rest of standard pedro tuning.

Some tips for the getting the most out of tuning:
1. When you get to the `ForwardVelocityTuner` and `ForwardZeroPowerAccelerationTuner` tuners, you don't need to do the lateral variants because with swerve
they are equivalent. You can just use the same values for both.
2. You need to retune your zero power acceleration if you switch from using X-lock to not using it and vice versa. When using X-lock, the robot can decelerate
much faster than without (the difference was about -200 vs -130 in my case), and this affects the robot's ability to stop at the correct position. I would
recommend using X-lock unless you have a reason not to.
3. Swerve is currently not compatible with predictive braking; predictive braking is too aggressive and causes oscillations because swerve pods cannot
instantaneously change direction like mecanum wheels can. We are looking into potential solutions to this, but predictive braking also isn't as needed for swerve
because of the much higher natural deceleration as compared to mecanum, especially when using X-lock.
4. When tuning your heading and translational PIDs, I would highly recommend **NOT** using F values. Like with predictive braking, F values tend to cause
oscillations in swerve because swerve pods cannot change direction instantaneously.
5. In general, stay conservative with your heading and translational PIDs. While slightly higher values can make the robot more responsive, oscillations
when driving slow down the robot **significantly**, so I've found that getting decent responsiveness while minimizing oscillations is the most effective
tuning strategy. On that note, I would highly recommend using secondary PIDs for all three pathing PIDs. If your secondaries are decently less aggressive
than your primaries, you can significantly improve responsiveness while minimizing oscillations.
6. I've found that a very low centripetal scaling value (like 0.0005) can also helps minimize oscillations when following splines (I think the improved
traction compared to mecanum means the centripetal friction on swerve is higher, meaning less compensation is needed)

There is also a [swerve constants reference page](/docs/pathing/tuning/swerve/swerve-constants-example) that you can use to see a fully setup `Constants`
file using swerve. Finally, if you have any other questions, please feel free to reach out to me (@_kubar) on discord through the Pedro discord server
(preferred) or DMs.

---

> Source: https://pedropathing.com/docs/pathing/tuning/swerve/swerve-constants-example · Fetched: 2026-07-12

## Swerve Constants Example

```java title="Constants.java"
package org.firstinspires.ftc.teamcode.pedroPathing;

import com.pedropathing.VectorCalculator;
import com.pedropathing.control.FilteredPIDFCoefficients;
import com.pedropathing.control.PIDFCoefficients;
import com.pedropathing.control.PredictiveBrakingCoefficients;
import com.pedropathing.follower.Follower;
import com.pedropathing.follower.FollowerConstants;
import com.pedropathing.ftc.FollowerBuilder;
import com.pedropathing.ftc.drivetrains.CoaxialPod;
import com.pedropathing.ftc.drivetrains.SwerveConstants;
import com.pedropathing.ftc.localization.constants.PinpointConstants;
import com.pedropathing.geometry.Pose;
import com.pedropathing.paths.PathConstraints;
import com.qualcomm.hardware.gobilda.GoBildaPinpointDriver;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.hardware.HardwareMap;

import org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit;

public class PedroConstants {
    public static FollowerConstants followerConstants = new FollowerConstants()
            .forwardZeroPowerAcceleration(-197.1)
            .lateralZeroPowerAcceleration(-197.1)
            .useSecondaryDrivePIDF(true).useSecondaryHeadingPIDF(true)
            .useSecondaryTranslationalPIDF(true)

            .translationalPIDFCoefficients(new PIDFCoefficients(0.125, 0, 0.008, 0))
            .secondaryTranslationalPIDFCoefficients(new PIDFCoefficients(0.0825, 0, 0.008, 0))

            .headingPIDFCoefficients(new PIDFCoefficients(1.75, 0, 0.003, 0))
            .secondaryHeadingPIDFCoefficients(new PIDFCoefficients(0.8, 0, 0.015, 0))

            .drivePIDFCoefficients(new FilteredPIDFCoefficients(0.005, 0, 0.00003, 0.6, 0.13))
            .secondaryDrivePIDFCoefficients(
                    new FilteredPIDFCoefficients(0.004, 0, 0.000002, 0.6, 0.13))

            // .drivePIDFCoefficients(new FilteredPIDFCoefficients(0,0,0,0,0))
            // .secondaryDrivePIDFCoefficients(new FilteredPIDFCoefficients(0,0,0,0,0))

            // .predictiveBrakingCoefficients(new PredictiveBrakingCoefficients(
            // 0.05, //0.05 to 0.3
            // 0,//0.38735914623969386,
            // 0.002)
            // )
            .centripetalScaling(0.0005).
            mass(13.732);

    public static PinpointConstants localizerConstants = new PinpointConstants()
            .forwardPodY(-2.9350393701) //-74.5mm
            .strafePodX(-5.9133858268) //-150.2
            .distanceUnit(DistanceUnit.INCH).hardwareMapName("pinpoint")
            .encoderResolution(GoBildaPinpointDriver.GoBildaOdometryPods.goBILDA_4_BAR_POD)
            .forwardEncoderDirection(GoBildaPinpointDriver.EncoderDirection.FORWARD)
            .strafeEncoderDirection(GoBildaPinpointDriver.EncoderDirection.REVERSED);

    public static SwerveConstants swerveConstants = new SwerveConstants()
            .velocity(73.9)
//            .zeroPowerBehavior(SwerveConstants.ZeroPowerBehavior.IGNORE_ANGLE_CHANGES)
            .useBrakeModeInTeleOp(true);

    private static double kP = 0.0055 * 180 / Math.PI;
    private static double kD = 0.00015 * 180 / Math.PI;
    private static double kFFront = 0.0130;
    private static double kFBack = 0.0190;

    private static double dtLength = 271.148;
    private static double dtWidth = 270.7;

    private static CoaxialPod leftFront(HardwareMap hardwareMap) {
        CoaxialPod pod = new CoaxialPod(hardwareMap, "sm2", "ss2", "se2",
                new PIDFCoefficients(kP, 0, kD, kFFront), DcMotorSimple.Direction.REVERSE,
                DcMotorSimple.Direction.REVERSE, Math.toRadians(353.1), new Pose(dtLength, dtWidth),
                0.025, 3.290, false);
        pod.setMotorCachingThreshold(0.05);
        pod.setServoCachingThreshold(0.05);
        return pod;
    }

    private static CoaxialPod rightFront(HardwareMap hardwareMap) {
        CoaxialPod pod = new CoaxialPod(hardwareMap, "sm1", "ss1", "se1",
                new PIDFCoefficients(kP, 0, kD, kFFront), DcMotorSimple.Direction.FORWARD,
                DcMotorSimple.Direction.REVERSE, Math.toRadians(348.2), new Pose(dtLength, -dtWidth),
                0.018, 3.288, false);
        pod.setMotorCachingThreshold(0.05);
        pod.setServoCachingThreshold(0.05);
        return pod;
    }

    private static CoaxialPod leftBack(HardwareMap hardwareMap) {
        CoaxialPod pod = new CoaxialPod(hardwareMap, "sm3", "ss3", "se3",
                new PIDFCoefficients(kP, 0, kD, kFBack), DcMotorSimple.Direction.REVERSE,
                DcMotorSimple.Direction.REVERSE, Math.toRadians(179.3), new Pose(-dtLength, dtWidth),
                0.029, 3.307, false);
        pod.setMotorCachingThreshold(0.05);
        pod.setServoCachingThreshold(0.05);
        return pod;
    }

    private static CoaxialPod rightBack(HardwareMap hardwareMap) {
        CoaxialPod pod = new CoaxialPod(hardwareMap, "sm0", "ss0", "se0",
                new PIDFCoefficients(kP, 0, kD, kFBack), DcMotorSimple.Direction.FORWARD,
                DcMotorSimple.Direction.REVERSE, Math.toRadians(289.5), new Pose(-dtLength, -dtWidth),
                0.014, 3.301, false);
        pod.setMotorCachingThreshold(0.05);
        pod.setServoCachingThreshold(0.05);
        return pod;
    }

    // public static PathConstraints pathConstraints = new PathConstraints(0.95, 100, 1, 1);
    public static PathConstraints pathConstraints =
            new PathConstraints(0.9, 2, 2, 0.03, 50, 1, 10, 1);

    // default
    // public static PathConstraints defaultConstraints = new PathConstraints(0.995, 0.1, 0.1,
    // 0.007, 100, 1, 10, 1);
    public static Follower createFollower(HardwareMap hardwareMap) {
        return new FollowerBuilder(followerConstants, hardwareMap).pathConstraints(pathConstraints)
                .swerveDrivetrain(swerveConstants, leftFront(hardwareMap), rightFront(hardwareMap),
                        leftBack(hardwareMap), rightBack(hardwareMap))
                .pinpointLocalizer(localizerConstants).build();
    }
}
```

