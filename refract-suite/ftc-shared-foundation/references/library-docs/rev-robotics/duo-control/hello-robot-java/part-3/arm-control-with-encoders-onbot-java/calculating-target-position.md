> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/calculating-target-position.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/calculating-target-position.md).

# Calculating Target Position

Now that we have an estimate for our target position let's see if we can refine it to be more precise using similar methods to what we covered during the [Drivetrain Encoders section](/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot.md).

## What's Needed for the Conversion

### Ticks per Revolution

Recall, that ticks per revolution of the encoder shaft is different than the ticks per revolution of the shaft that is controlling a mechanism, such as what we determined on our [Drivetrain](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/converting-encoder-ticks-to-a-distance#whats-needed-for-the-conversion).

{% hint style="info" %}
For more information on the effect of motion transmission across a mechanism check out the [Compound Gearing](https://docs.revrobotics.com/duo-build/actuators/gears/gears-advanced#compound-gearing) section.
{% endhint %}

The amount of ticks per revolution of the encoder shaft is dependent on the motor and encoder. Manufacturers of motors with built-in encoders will have information on the amount of ticks per revolution.

{% hint style="info" %}
Visit the manufacturers website for your motor or encoders for more information on encoder counts. For HD Hex Motors or Core Hex Motors visit the [Motor](https://docs.revrobotics.com/duo-build/actuators/motors) documentation.
{% endhint %}

In the [Core Hex Motor specifications ](https://docs.revrobotics.com/duo-build/actuators/motors/core-hex-motor#product-specs)there are two different Encoder Counts per Revolution numbers:

* At the motor - 4 counts/revolution
* At the output - 288 counts/revolution

At the motor is the number of encoder counts on the shaft that encoder is on. This number is equivalent to the 28 counts per revolution we used for the HD Hex Motor.

The 288 counts "at the output" accounts for the change in resolution after the motion is transmitted from the motor to the built in 72:1 gearbox.

Lets use the **288 as ticks per revolution** so that we do not have to account for the gearbox in our total gear reduction variable.

### Total Gear Reduction

Since we built the the gear reduction from the motor gearbox into the ticks per revolution the main focus of this section is calculating the gear reduction of the arm joint.

The motor shaft drives a 45 tooth gear that transmits motion to a 125 tooth gear. The total gear ratio is 125T:45T. To calculate the gear reduction for this gear train, we can simply divide 125 by 45.

$$
\frac{125}{45} = 2.777778
$$

To summarize, for the Class Bot V2 the following information is true:&#x20;

| Ticks per revolution | 288 ticks |
| -------------------- | --------- |
| Total gear reduction | 2.777778  |

## Adding Arm Encoders to the Program

### Establishing Initialization Variables

Now that we have this information let's create two constant variables:&#x20;

* `COUNTS_PER_MOTOR_REV`
* `GEAR_REDUCTION`

Add the `COUNTS_PER_MOTOR_REV` and `GEAR_REDUCTION` variables to the OpMode beneath where the hardware variables are created.&#x20;

```java
public class HelloRobot_ArmEncoder extends LinearOpMode {
    private DcMotor arm;
    
    static final double     COUNTS_PER_MOTOR_REV    = 288; 
    static final double     GEAR_REDUCTION    = 2.7778;   
```

Now that these two variables have been defined, we can use them to calculate two other variables: the amount of encoder counts per rotation of the 125T driven gear and the number of counts per degree moved.

### Adding Calculations to the Variables

Calculating counts per revolution of the 125T gear (or `COUNTS_PER_GEAR_REV`)is the same formula used in [Converting Encoder Ticks](/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/converting-encoder-ticks-to-a-distance.md) for our `COUNTS_PER_WHEEL_REV` variable.&#x20;

So to get this variable we can multiply `COUNTS_PER_MOTOR_REV` by `GEAR_REDUCTION`.

```java
static final double  COUNTS_PER_GEAR_REV    = COUNTS_PER_MOTOR_REV * GEAR_REDUCTION;
```

To calculate the number of counts per degree or moved or `COUNTS_PER_DEGREE` divide the `COUNTS_PER_GEAR_REV` variable by 360.&#x20;

```java
static final double     COUNTS_PER_DEGREE    = COUNTS_PER_GEAR_REV/360;
```

Add both these variables to the OpMode:

```java
public class HelloRobot_ArmEncoder extends LinearOpMode {
    private DcMotor arm;
    
    static final double     COUNTS_PER_MOTOR_REV    = 288; 
    static final double     GEAR_REDUCTION    = 2.7778;   
    static final double     COUNTS_PER_GEAR_REV    = COUNTS_PER_MOTOR_REV * GEAR_REDUCTION;
    static final double     COUNTS_PER_DEGREE    = COUNTS_PER_GEAR_REV/360;
```

### Adjusting our If/Else Statement

We need to create one more non-constant variable that will act as our position. This will be called `armPosition`.

```java
public void runOpMode() {
        arm = hardwareMap.get(DcMotor.class, "arm");
        
        int armPosition;
        
        waitForStart();
```

Add this variable to the `if(gamepad1.dpad_up)` section of the `Target Position if/else`  statement.

To get to the 90 degree position, the arm needs to move roughly 45 degrees, therefore set arm position equal to `COUNTS_PER_DEGREE` times 45.

```java
while (opModeIsActive()) {

   if(gamepad1.dpad_up){
         armPosition = (int)(COUNTS_PER_DEGREE * 45);
         arm.setTargetPosition(83);
         arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
         arm.setPower(0.4);
                 }
```

Change the target position to `armPosition`.

```java
if(gamepad1.dpad_up){
     armPosition = (int)(COUNTS_PER_DEGREE * 45);
     arm.setTargetPosition(armPosition);
     arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
     arm.setPower(0.4);
            }
else if (gamepad1.dpad_down){
      arm.setTargetPosition(0);
      arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      arm.setPower(0.4);
            } 
```

{% hint style="warning" %}
We could change what `armPosition` is equal to in the `gamepad1.dpad_down` portion of the `if/else if` statement such as:&#x20;

```java
else if (gamepad1.dpad_down){
      armPosition = (int)(COUNTS_PER_DEGREE * 0);
      arm.setTargetPosition(armPosition);
      arm.setMode(DcMotorEx.RunMode.RUN_TO_POSITION);
      arm.setPower(0.4);
            } 
```

In this case we would consistently redefine `armPosition` to match the needs of whatever positions we want to create.&#x20;

Since our only two positions at the moment are our starting position and our 90 degree position it isn't necessary. However, it is a good practice to create a variable in situations like this. If we want to add another position later, we can easily edit the variable to fit our needs.
{% endhint %}
