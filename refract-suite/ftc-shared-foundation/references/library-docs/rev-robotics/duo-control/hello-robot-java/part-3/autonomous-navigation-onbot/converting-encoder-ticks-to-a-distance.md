> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/converting-encoder-ticks-to-a-distance.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/converting-encoder-ticks-to-a-distance.md).

# Converting Encoder Ticks to a Distance

In the previous section, the basic structure needed to use `RUN_TO_POSITION`was created. The placement of `leftmotor.setTargetPosition(1000);` and `rightmotor.setTargetPosition(1000);` within the code, set the target position to 1000 ticks.&#x20;

But how far is a tick and how can we use them to help our robot navigate an area? We could attempt to estimate the distance the robot moves per tick or we can convert the amount of ticks per revolution of the encoder into a unit like millimeters or inches! For instance, if you work through the conversion process and find out that a drivetrain takes 700 ticks to move an inch, this can be used to find the total number of ticks need to move the robot 24 inches.

{% hint style="warning" %}
Reminder that the basis for this guide is the [Class Bot V2](https://docs.revrobotics.com/duo-build/ftc-starter-kit-class-bot). The REV DUO Build System is a metric system. Since part of the conversion process references the diameter of the wheels, this section will convert to ticks per mm.
{% endhint %}

## What's Needed for the Conversion <a href="#whats-needed-for-the-conversion" id="whats-needed-for-the-conversion"></a>

This process will take a bit of math to achieve so let's break it down.

When using encoders built into motors, converting from ticks per revolution to ticks per unit of measure moved requires the following information:

* [x] Ticks per revolution of the encoder shaft
* [x] Total gear reduction on the motor
  * Including gearboxes and motion transmission components like gears, sprockets and chain, or belts and pulleys
* [x] Circumference of the driven wheels

### Ticks per Revolution

The amount of ticks per revolution of the encoder shaft is dependent on the motor and encoder. Manufacturers of motors with built-in encoders will have information on the amount of ticks per revolution.

For HD Hex Motors the encoder counts 28 ticks per revolution of the motor shaft.

{% hint style="info" %}
Visit the manufacturers website for your motor or encoders for more information on encoder counts. For HD Hex Motors or Core Hex Motors visit our [Motor](https://docs.revrobotics.com/duo-build/actuators/motors) documentation.&#x20;
{% endhint %}

### Total Gear Reduction

Since ticks per revolution of the encoder shaft is before any gear reduction calculating the total gear reduction is needed. This includes the gearbox and any addition reduction from motion transmission components. To find the total gear reduction use the [Compound Gearing formula](https://docs.revrobotics.com/duo-build/actuators/gears/gears-advanced#compound-gearing).

For the Class Bot V2 there are two UltraPlanetary Cartridges, 4:1 and 5:1, and an additional gear reduction from the UltraPlanetary Output to the wheels, 72T:45T ratio.

{% hint style="info" %}
The UltraPlanetary Cartridges use the nominal gear ratio as a descriptor. The actual gear ratios can be found in the [UltraPlanetary Users Manual's Cartridge Details](https://docs.revrobotics.com/ultraplanetary/cartridge-details#actual-cartridge-gear-ratios).&#x20;
{% endhint %}

Using the compound gearing formula for the Class Bot V2 the total gear reduction is:

$$
\frac{3.61}{1} \* \frac{5.23}{1} \* \frac{72}{45} = 30.21
$$

{% hint style="info" %}
Unlike the the spur gears used to transfer motion to the wheels, the UltraPlanetary Gearbox Cartridges are planetary gear systems. To make calculations easier the gear ratios for the Cartridges are already reduced.&#x20;
{% endhint %}

### Circumference of the Wheel

The Class Bot V2 uses the 90mm Traction Wheels. 90mm is the diameter of the wheel. To get the appropriate circumference use the following formula

$$
circumference = diameter \* \pi
$$

You can calculate this by hand, but for the purpose of this guide, this can be calculated within the code.

{% hint style="info" %}
Due to wear and manufacturing tolerances, the diameter of some wheels may be nominally different. For the most accurate results consider measuring your wheel to confirm that the diameter is accurate.&#x20;
{% endhint %}

To summarize, for the Class Bot V2 the following information is true:&#x20;

| Ticks per revolution       | 28 ticks        |
| -------------------------- | --------------- |
| Total gear reduction       | 30.21           |
| Circumference of the wheel | $$90mm \* \pi$$ |

## Translating the Conversion to Code

### Setting up Variables

Each of these pieces of information will be used to find the number of encoder ticks (or counts) per mm that the wheel moves. Rather than worry about calculating this information by hand, these values can be added to the code as constant variables. To do this create three variables:

* `COUNTS_PER_MOTOR_REV`
* `DRIVE_GEAR_REDUCTION`
* `WHEEL_CIRCUMFERENCE_MM`

{% hint style="info" %}
The common naming convention for constant variables is known as CONSTANT\_CASE, where the variable name is in all caps and words are separated by and underscore.&#x20;
{% endhint %}

We'll add the [variables](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks) to the initialization section of the OpMode:

To ensure variables are referenceable they are set as `static final double` variables. **Static** allows references to the variables anywhere within the class. **Final** dictates that these variables are constant and unchanged elsewhere within the code.&#x20;

Since these variables are not integers they are classified as **double** variables.&#x20;

```java
public class HelloRobot_EncoderAuton extends LinearOpMode {
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    
    static final double     COUNTS_PER_MOTOR_REV    = 28.0; 
    static final double     DRIVE_GEAR_REDUCTION    = 30.21;   
    static final double     WHEEL_CIRCUMFERENCE_MM  = 90.0 * Math.PI;
```

Now that these three variables have been defined, we can use them to calculate two other variables: the **amount of encoder counts per rotation of the wheel** and **the number of counts per mm that the wheel moves**.

```java
public class HelloRobot_EncoderAuton extends LinearOpMode {
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    
    static final double     COUNTS_PER_MOTOR_REV    = 28.0; 
    static final double     DRIVE_GEAR_REDUCTION    = 30.24;   
    static final double     WHEEL_CIRCUMFERENCE_MM  = 90.0 * 3.14;
    
    static final double     COUNTS_PER_WHEEL_REV    =
    static final double     COUNTS_PER_MM =
```

### Calculating COUNTS\_PER\_WHEEL\_REV

To calculate counts per wheel revolution multiple `COUNTS_PER_MOTOR_REV` by `DRIVE_GEAR_REDUCTION` Use the following formula:

$$
y = a
\*b
$$

Where:

* $$a$$ = `COUNTS_PER_MOTOR_REV`
* $$b$$ = `DRIVE_GEAR_REDUCTION`&#x20;
* $$y$$ = `COUNTS_PER_WHEEL_REV`

```java
public class HelloRobot_EncoderAuton extends LinearOpMode {
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    
    static final double     COUNTS_PER_MOTOR_REV    = 28.0; 
    static final double     DRIVE_GEAR_REDUCTION    = 30.24;   
    static final double     WHEEL_CIRCUMFERENCE_MM  = 90.0 * 3.14;
    
    static final double     COUNTS_PER_WHEEL_REV    = COUNTS_PER_MOTOR_REV * DRIVE_GEAR_REDUCTION
    static final double     COUNTS_PER_MM = 
```

### Calculating COUNTS\_PER\_MM

Once `COUNTS_PER_WHEEL_REV` is calculated, use it to calculate the counts per mm that the wheel moves. To do this divide the `COUNTS_PER_WHEEL_REV` by the `WHEEL_CIRCUMFERENCE_MM`. Use the following formula.

$$
x = \frac{(a\*b)}{c} = \frac{y}{c}
$$

Where,

* $$a$$ = `COUNTS_PER_MOTOR_REV`
* $$b$$ = `DRIVE_GEAR_REDUCTION`
* $$c$$ = `WHEEL_CIRCUMFERENCE_MM`
* $$y$$ = `COUNTS_PER_WHEEL_REV`
* $$x$$ = `COUNTS_PER_MM`

```java
public class HelloRobot_EncoderAuton extends LinearOpMode {
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    
    static final double     COUNTS_PER_MOTOR_REV    = 28.0; 
    static final double     DRIVE_GEAR_REDUCTION    = 30.24;   
    static final double     WHEEL_CIRCUMFERENCE_MM  = 90.0 * 3.14;
    
    static final double     COUNTS_PER_WHEEL_REV    = COUNTS_PER_MOTOR_REV * DRIVE_GEAR_REDUCTION;
    static final double     COUNTS_PER_MM           = COUNTS_PER_WHEEL_REV / WHEEL_CIRCUMFERENCE_MM;
```

{% hint style="warning" %}
`COUNTS_PER_WHEEL_REV`will be created as a separate variable from`COUNTS_PER_MM` as it is used in calculating a target velocity.&#x20;
{% endhint %}

#### Program thus far:

<pre class="language-java"><code class="lang-java">package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;

@Autonomous //sets the op mode as an autonomous op mode 

public class HelloWorld_Encoder extends LinearOpMode {
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    
    static final double     COUNTS_PER_MOTOR_REV    = 28.0; 
    static final double     DRIVE_GEAR_REDUCTION    = 30.24;   
    static final double     WHEEL_CIRCUMFERENCE_MM  = 90.0 * 3.14;
    
    static final double     COUNTS_PER_WHEEL_REV    = COUNTS_PER_MOTOR_REV * DRIVE_GEAR_REDUCTION;
    static final double     COUNTS_PER_MM           = COUNTS_PER_WHEEL_REV / WHEEL_CIRCUMFERENCE_MM;
   
     @Override
    public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        
        rightmotor.setDirection(DcMotor.Direction.REVERSE);
        
        leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        leftmotor.setTargetPosition(1000);
<strong>        rightmotor.setTargetPosition(1000);
</strong><strong>        
</strong><strong>        leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
</strong>        rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        
        leftmotor.setPower(0.8);
<strong>        rightmotor.setPower(0.8);
</strong>
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive() &#x26;&#x26; (leftmotor.isBusy() &#x26;&#x26; rightmotor.isBusy())) {

}
    }
}
</code></pre>
