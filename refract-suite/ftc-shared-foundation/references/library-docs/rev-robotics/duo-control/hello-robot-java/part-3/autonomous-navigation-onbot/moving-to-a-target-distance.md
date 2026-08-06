> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/moving-to-a-target-distance.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot/moving-to-a-target-distance.md).

# Moving to a Target Distance

Now that you have created the constant variables needed to calculate the amount of ticks per mm moved, you can use this to set a target distance. For instance, if you would like to have the robot move forward two feet, converting from feet to millimeters and multiplying by the `COUNTS_PER_MM` will give you the amount of counts (or ticks) needed to reach that distance!

Create two more variables called `leftTarget` and`rightTarget`.&#x20;

These variables can be fluctuated and edited in your code to tell the motors what positions to go to, rather than place them with the constant variables, create these variables within the OpMode but above the `waitForStart();` command.&#x20;

```java
public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        
        rightmotor.setDirection(DcMotor.Direction.REVERSE);
        
        leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        int leftTarget;
        int rightTarget;
        
        waitForStart();
```

{% hint style="info" %}
The `setTargetPosition();`function takes in a integer (or **int)** data type as its parameter, rather than a double. Since both the `leftTarget` and `rightTarget`will be used to set the target position, create both variables as int variables.&#x20;
{% endhint %}

## Converting from mm to Feet

Right now the main distance factor is `COUNTS_PER_MM` , however you may want to go a distance that is in the imperial system, such as 2 feet (or 24 inches). The target distance in this case will need to be converted to mm.

To convert from feet to millimeters use the following formula:

$$
d\_{(mm)} = d\_{(ft)} × 304.8
$$

If you convert 2 feet to millimeters, it comes out the be 609.6 millimeters. For the purpose of this guide, lets go ahead an round this to be 610 millimeters.

## Converting Feet to Ticks

Next, multiply 610 millimeters by the `COUNTS_PER_MM` variable to get the number of ticks needed to move the robot 2 feet. Since the intent is to have the robot move in a straight line, set both the `leftTarget` and `rightTarget`, to be equal to 610 \* `COUNTS_PER_MM`

As previously mentioned the `setTargetPosition();` function requires that its parameter must be an **integer data type**. The `leftTarget`and `rightTarget`variables have been set to be integers, however the`COUNTS_PER_MM` variable is a double. Since these are two different data types, a conversion of data types needs to be done.&#x20;

In this case the `COUNTS_PER_MM` needs to be converted to an integer. This is as simple as adding the line (int) in front of the double variable. However, you need to be cautious of potential rounding errors. Since `COUNTS_PER_MM` is part of an equation it is recommended that you convert to an integer AFTER the result of the equation is found.&#x20;

```java
int leftTarget = (int)(610 * COUNTS_PER_MM);
int rightTarget = (int)(610 * COUNTS_PER_MM);
```

Lastly, edit the `setTargetPosition();` lines so that both motors are set to the appropriate target position. To do this add the `leftTarget` and  `rightTarget` variables to their respective motor:&#x20;

```java
leftmotor.setTargetPosition(leftTarget);
rightmotor.setTargetPosition(rightTarget);
```
