> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/using-limits-to-control-range-of-motion.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/using-limits-to-control-range-of-motion.md).

# Using Limits to Control Range of Motion

In [Part 2: Robot Control](/duo-control/hello-robot-java/part-2/arm-control-onbot-java/adding-a-limit-switch.md) the idea of creating a limit switch was introduced using a physical sensor, like a touch sensor. We can make use of our motor's built-in encoder to do something similar. While a physical sensor would be described as a hard limit, using the built-in encoder is called a soft limit.

To set the soft limits we will build off the program created in the last sections (HelloRobot\_ArmEncoder)!

```java
@TeleOp

public class HelloRobot_ArmEncoder extends LinearOpMode {
    private DcMotor  arm;

    static final double     COUNTS_PER_MOTOR_REV    = 288; 
    static final double     GEAR_REDUCTION    = 2.7778;   
    static final double     COUNTS_PER_GEAR_REV    = COUNTS_PER_MOTOR_REV * GEAR_REDUCTION;
    static final double     COUNTS_PER_DEGREE    = COUNTS_PER_GEAR_REV/360;
    
    @Override
    public void runOpMode() {
        arm = hardwareMap.get(DcMotor.class, "arm");
        
        
        waitForStart();
    
        while (opModeIsActive()) {
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
}
```

## Creating minPosition and maxPosition

To start, we need to create our upper and lower limits. Create two new variables one called `minPosition` and one called `maxPosition` to be added to initialization.

Add both of these to the in the initialization section of the OpMode above the `waitForStart()`; command.&#x20;

```java
public void runOpMode() {
        arm = hardwareMap.get(DcMotor.class, "arm");
        
        int minPostion;
        int maxPosition;
        waitForStart();
    
```

For now we want the `minPosition` set as our starting position and the `maxPosition` set to our 90 degree position. Set `minPosition` equal to 0 and set `maxPosition` equal to `COUNTS_PER_DEGREE` times 45.&#x20;

{% hint style="info" %}
Remember you need to make a data type conversion!
{% endhint %}

```java
int minPostion = 0;
int maxPosition = (int)(COUNTS_PER_DEGREE *45);
```

## Adjusting our If/Else Statement

To start, our If/Else Statement will be changed back to a simplified format like we had at the beginning of [estimating the position of the arm](/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/estimating-the-position-of-the-arm.md).

```java
while(opModeIsActive()){
     if(gamepad1.dpad_up){
            arm.setPower(0.5);         
            }
     else if (gamepad1.dpad_down){
            arm.setPower(-0.5); 
            }   
     else { 
            arm.setPower(0); 
            }   
     } 
```

To set the limit we need to edit our `if/else` statement to include our limits:

* If up on the Dpad is pressed and the position of the arm is less than the `maxPosition`, then the arm will move to the `maxPosition`.
* If down on the Dpad is pressed and the position of the arm is greater than the `minPosition` then the arm will move towards the `minPosition`.

```java
while (opModeIsActive()) {
    if (gamepad1.dpad_up && arm.getCurrentPosition() < maxPosition) {
            arm.setPower(0.5);
            } 
    else if (gamepad1.dpad_down && arm.getCurrentPosition() > minPosition) {
            arm.setPower(-0.5);
            } 
    else {
            arm.setPower(0);
            }
    }
```

{% hint style="success" %}
The current code configuration will stop the motor at any point that the conditions to power the motor are not met. Depending to factors like the weight of the mechanism and any load that it is bearing, when the motor stops the arm may drop below the `maxPosition`.  Take time to test out the code and confirm that it behaves in the way you expect it to.&#x20;
{% endhint %}

## Overriding Limits

One of the benefits of having a soft limit is being able to exceed that limit.

Remember that the encoders zero tick position is determined by the position of the arm when the Control Hub powers on! So if we aren't careful to reset the arm before powering on our robot this will effect the arm's range of motion. For instance, if we have to reset the Control Hub while the arm is in the 90 degree position, the 90 degree position will become equal to 0 encoder ticks.

As a back up, we can create an override for the range of motion. There are a few different ways an override can be created, but in our case we are going to use the "A" button and touch sensor to help reset our range.

### Adding a Gamepad Override

Start by editing the `if/else if` statement  to add another `else if`  condition. Use the line `gamepad1.a` as the condition. Add a the line `arm.setPower(-0.5);`  as the action item.

```java
while (opModeIsActive()) {
    if (gamepad1.dpad_up && arm.getCurrentPosition() < maxPosition) {
            arm.setPower(0.5);
            } 
    else if (gamepad1.dpad_down && arm.getCurrentPosition() > minPosition) {
            arm.setPower(-0.5);
            } 
    else if(gamepad1.a){
            arm.setPower(-0.5);
    else {
            arm.setPower(0);
            }
    }
```

Now that we have this change in place, when the "A" button is pressed the arm will move toward the starting position.

### Adding a Touch Sensor Limit

When the arm reaches and presses the touch sensor we want to `STOP_AND_RESET_ENCODER`.

We can create another `if` statement that focuses on performing this stop and reset when the Touch Sensor is pressed.&#x20;

```java
if (touch.isPressed()) {
          arm.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        }
```

So, if the Touch Sensor returns `true` (or is pressed) the motor run mode `STOP_AND_RESET_ENCODER` will be activated causing the motor encoder to reset to 0 ticks.&#x20;

Now that this code is done, try testing it!&#x20;

```java
@TeleOp

public class HelloRobot_ArmEncoder extends LinearOpMode {
    private DcMotor arm;
    private Servo claw;
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    private TouchSensor touch;
    
    static final double     COUNTS_PER_MOTOR_REV    = 288; 
    static final double     GEAR_REDUCTION    = 2.7778;   
    static final double     COUNTS_PER_GEAR_REV    = COUNTS_PER_MOTOR_REV * GEAR_REDUCTION;
    static final double     COUNTS_PER_DEGREE    = COUNTS_PER_GEAR_REV/360;


    @Override
    public void runOpMode() {
        arm = hardwareMap.get(DcMotor.class, "arm");
        claw = hardwareMap.get(Servo.class, "claw");
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        touch = hardwareMap.get(TouchSensor.class, "touch");
        
        int minPostion = 0;
        int maxPosition = (int)(COUNTS_PER_DEGREE *45);
        
        waitForStart();
            
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            if (gamepad1.dpad_up && arm.getCurrentPosition() < maxPosition) {
                arm.setPower(0.5);
                    } 
            else if (gamepad1.dpad_down && arm.getCurrentPosition() > minPosition) {
                arm.setPower(-0.5);
                    } 
            else if (gamepad1.a) {
                arm.setPower(-0.5);
                    } 
            else {
                arm.setPower(0);
                }
            if (touch.isPressed()) {
              arm.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    }
        telemetry.addData("Arm Test", arm.getCurrentPosition());
        telemetry.update(); 
        }
    }
}
```
