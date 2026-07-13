> Source: https://pedropathing.com/docs/pathing/custom/curve · Fetched: 2026-07-12

# Pedro Pathing — Custom Curves, Drivetrains & Localizers

> Source: https://pedropathing.com/docs/pathing/custom/curve · Fetched: 2026-07-12

## Custom Curve

The Pedro Pathing follower is capable of following custom curves external to the library-provided ones.
You can create your own curve by extending the abstract class `CustomCurve`.
Custom Curves **must** be twice differentiable, parameterized on the interval [0,1], and non-degenerate (meaning the curve must never satisfy $$x'(t) = y'(t) = 0$$ for $$t \in [0,1]$$).
There is an optional `initialization()` method that can be overridden to do something on the creation of the curve.
For example, the BezierCurve class stores the end tangent at this time.

Here is a simple example of a LinearSpline:

```java
import com.pedropathing.geometry.CustomCurve;
import com.pedropathing.geometry.Pose;
import com.pedropathing.math.Vector;
import com.pedropathing.paths.PathConstraints;
import java.util.Arrays;

public class LinearSpline extends CustomCurve {
    private Pose startPose;
    private Pose endPose;
    private Pose diffPose;

    public LinearSpline(Pose startPoint, Pose endPoint) {
        super(startPoint, endPoint);
    }

    public LinearSpline(FuturePose startPoint, FuturePose endPoint) {
        super(startPoint, endPoint);
    }

    public LinearSpline(Pose startPoint, Pose endPoint, PathConstraints constraints) {
        super(Arrays.asList(startPoint, endPoint), constraints);
    }

    @Override
    public String pathType() {
        return "Linear Spline";
    }

    @Override
    public LinearSpline getReversed() {
        LinearSpline curve = new LinearSpline(getControlPoints().get(1), getControlPoints().get(0), this.getPathConstraints());
        curve.initialize();
        return curve;
    }

    @Override
    public Vector getDerivative(double t) {
        return diffPose.getAsVector();
    }

    @Override
    public Pose getPose(double t) {
        if (startPose == null) init();

        double x = t * diffPose.getX() + startPose.getX();
        double y = t * diffPose.getY() + startPose.getY();

        return new Pose(x, y);
    }

    public void init() {
        startPose = getControlPoints().get(0);
        endPose = getControlPoints().get(1);
        diffPose = endPose.minus(startPose);
    }

    @Override
    public Vector getSecondDerivative(double t) {
        return new Vector();
    }
}
```

---

> Source: https://pedropathing.com/docs/pathing/custom/drivetrain · Fetched: 2026-07-12

## Custom Drivetrain

You can create your own drivetrain by extending the `Drivetrain` class.
This allows you to implement custom drivetrain logic or different drivetrains that are not natively supported by the existing drivetrains.

#### Hardware
All hardware should remain in your Drivetrain class.
This includes motors, servos, and any other control hardware.
This ensures that the localizer can access the necessary hardware components directly.
For example, if you are doing a coaxial swerve, you would initialize the motors and servos in the constructor of your drive class and then save them in an array or list.
Then, you can use these motors and servos in your drivetrain methods to control the robot's movement.

#### Constants
It is suggested that you create a Constants class for your drivetrain.
This allows for easy configuration and modification of the localizer's parameters without changing the Drivetrain itself, although not required.
So, for a `CustomDrivetrain`, you would create a `CustomDrivetrainConstants` class.
In the `Constants` file, you would then create a `CustomDrivetrainConstants` object and pass it to your drivetrain through the constructor.

#### Methods

##### calculateDrive
This abstract method is used to get the drive powers for the drivetrain.
It returns a double array, which can be used to power the motors or servos in your drivetrain.
It specifically takes in the correctiveVector (centripetal and translational), headingVector, pathingPower, and the current heading of the robot.
This method is essential for implementing the drivetrain's movement logic, allowing you to control how the robot moves based on the pathing and heading information.

##### runDrive
This abstract method is used to run the hardware using the output of calculate drive.
This could be moving servos to positions or directions but also powering motors to a certain speed.

##### runDrive
There is an overloaded version of runDrive that takes in the correctiveVector, headingVector, pathingPower, and currentHeading.
It combines the functionality of calculateDrive and runDrive into one method.
This is useful if you want to simplify the process of calculating and running the drivetrain in one method call.

> **Note:**
> You must implement the runDrive method that takes in the double array from calculateDrive, as it is abstract, while the overloaded version already calls the two methods, so it cannot be modified.

---

> Source: https://pedropathing.com/docs/pathing/custom/localizer · Fetched: 2026-07-12

## Custom Localizer

You can create your own localizer by extending the `Localizer` class.
This allows you to implement custom localization logic or different localization hardware that is not supported by the existing localizers.

#### Hardware
All hardware should remain in the Localizer class.
This ensures that the localizer can access the necessary hardware components directly.
For example, if you are using a custom sensor, you would initialize it in the constructor of your localizer class.

#### Constants
It is suggested that you create a Constants class for your localizer.
This allows for easy configuration and modification of the localizer's parameters without changing the Localizer itself, although not required.
So, for a `CustomLocalizer`, you would create a `CustomLocalizerConstants` class.
In the `Constants` file, you would then create a `CustomLocalizerConstants` object and pass it to your localizer through the constructor.

