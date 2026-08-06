> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/setting-velocity.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/setting-velocity.md).

# Setting Velocity

## Setting Velocity in our Program

Velocity is a closed loop control within the [SDK](https://docs.revrobotics.com/duo-control/hello-robot-blocks/where-to-program/what-is-an-opmode) that uses the encoder counts to determine the approximate power/speed the motors need to go in order to meet the set velocity.

To set a velocity, its important to understand the maximum velocity in RPM your motor is capable of. For the Class Bot V2 the motors are capable of a maximum RPM of 300. With a drivetrain, you are likely to get better control by setting velocity lower than the maximum. In this case, lets set the velocity to 175 RPM!

Since RPM is the amount of revolutions per minute, a conversion needs to be made from RPM to ticks per second (TPS). To do this, divide the RPM by 60 to get the amount of rotations per second.

Rotations per second can then be multiplied by `COUNTS_PER_WHEEL_REV`, to get the amount of ticks per second.

$$
TPS = \frac{175}{60} \* CPWR
$$

### Adding Ticks per Second as a Variable

Create a new double variable called `TPS`. Add`TPS` the to the OpMode under where `rightTarget` is defined:

```java
public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        
        rightmotor.setDirection(DcMotor.Direction.REVERSE);
        
        leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        int leftTarget = (int)(610 * COUNTS_PER_MM);
        int rightTarget = (int)(610 * COUNTS_PER_MM);
        double TPS = (175/60) * COUNTS_PER_WHEEL_REV;
        
        waitForStart();
```

### Changing from Power to Velocity

Exchange the `setPower();`functions for `setVelocity();`

Add `TPS` as the parameter for `setVelocity();`

```java
waitForStart();

leftmotor.setTargetPosition(leftTarget);
rightmotor.setTargetPosition(rightTarget);

leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);

leftmotor.setVelocity(TPS);
rightmotor.setVelocity(TPS);

while (opModeIsActive() && (leftmotor.isBusy() && rightmotor.isBusy())){
        
        }
```

With the velocity set, let's give our program a test run after building!

### DcMotor vs. DcMotorEx

With the current state of the code you are likely to get errors similar to the ones pictured below:

<figure><img src="/files/GfBwO9SLsGgkTDZBVH3S" alt=""><figcaption></figcaption></figure>

This is because the `setVelocity();`function is a function of the`DcMotorEx` Interface. The `DcMotorEx` Interface is an extension of the `DcMotor` Interface, that provides enhanced motor functionality, such as access to closed loop control functions.&#x20;

To use `setVelocity();` the motor variables need to be changed to `DcMotorEx` as seen below:

```java
public class HelloRobot_Encoder extends LinearOpMode {
    private DcMotorEx leftmotor;
    private DcMotorEx rightmotor;
```

```java
public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotorEx.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotorEx.class, "rightmotor");
```

{% hint style="info" %}
Since `DcMotorEx` is an extension of `DcMotor`, `DcMotor` specific functions can be used by variables defined as `DcMotorEx`.&#x20;
{% endhint %}

### Full Program&#x20;

```java
@Autonomous

public class HelloRobot_Encoder extends LinearOpMode {
    private DcMotorEx leftmotor;
    private DcMotorEx rightmotor;
    
    static final double     COUNTS_PER_MOTOR_REV    = 28.0; 
    static final double     DRIVE_GEAR_REDUCTION    = 30.24;   
    static final double     WHEEL_CIRCUMFERENCE_MM  = 90.0 * 3.14;
    
    static final double     COUNTS_PER_WHEEL_REV    = COUNTS_PER_MOTOR_REV * DRIVE_GEAR_REDUCTION;
    static final double     COUNTS_PER_MM           = COUNTS_PER_WHEEL_REV / WHEEL_CIRCUMFERENCE_MM;
    
    @Override
    public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotorEx.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotorEx.class, "rightmotor");
        
        rightmotor.setDirection(DcMotor.Direction.REVERSE);

        leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        
        int leftTarget = (int)(610 * COUNTS_PER_MM);
        int rightTarget = (int)(610 * COUNTS_PER_MM);
        double TPS = (175/ 60) * COUNTS_PER_WHEEL_REV;
        
        waitForStart();
        
        
        leftmotor.setTargetPosition(leftTarget);
        rightmotor.setTargetPosition(rightTarget);
        
        leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        
        leftmotor.setVelocity(TPS);
        rightmotor.setVelocity(TPS);
        
        while (opModeIsActive() && (leftmotor.isBusy() && rightmotor.isBusy())) {
        }
    }
}
```
