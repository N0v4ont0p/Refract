> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot.md).

# Drivetrain Encoders - OnBot Java

Moving the motors to a specific position, using the encoders, removes any potential inaccuracies or inconsistencies from using Elapsed Time. The focus of this section is to move the robot to a target position using encoders.

## Setting up the Drivetrain Encoders

{% hint style="info" %}
For this tutorial, our OpMode is named HelloRobot\_Encoder!
{% endhint %}

The OpMode structure below is simplified and only includes the necessary components needed to create the encoder based code.&#x20;

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;

@Autonomous //sets the op mode as an autonomous op mode 

public class HelloRobot_Encoder extends LinearOpMode {
    private DcMotor leftmotor;
    private DcMotor rightmotor;
    
    @Override
    public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()){
        
        }
    }
}

```

Before diving in too far, recall that for certain [drivetrains](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2), like the [Class Bot V2](https://docs.revrobotics.com/duo-build/ftc-starter-kit-class-bot), one of the motors needs to be reversed as the motors are mirrored.

In our example, we are adding`rightmotor.setDirection(DcMotor.Direction.REVERSE);` to the code as seen below:

```java
public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        
        rightmotor.setDirection(DcMotor.Direction.REVERSE);
        
        waitForStart();
```

### RUN\_TO\_POSITION

As introduced in [Using Encoders](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/using-encoder#using-run_to_position), using `RUN_TO_POSITION` mode requires a three step process.

The **first step** is setting target position. To do so, add the lines `leftmotor.setTargetPosition(1000);` and `rightmotor.setTargetPosition(1000);` to the OpMode after the `waitForStart();` command. &#x20;

```java
waitForStart();

leftmotor.setTargetPosition(1000);
rightmotor.setTargetPosition(1000);

while (opModeIsActive()){
        
        }
```

If we want our robot to travel a specific distance we will need to do a bit of math beforehand to calculate the TargetPosition. But for now let's start simple by setting the target position to 1000 ticks.

The next step is to set both motors to the `RUN_TO_POSITION`mode. Add the lines `leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);`and `rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);`to your code, beneath the `setTargetPosition` code lines.&#x20;

```java
waitForStart();

leftmotor.setTargetPosition(1000);
rightmotor.setTargetPosition(1000);

leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);

while (opModeIsActive()){
        
        }
```

{% hint style="info" %}
Order matters! The TargetPosition block must come before RUN\_TO\_POSITION mode is set or it will result in an error.
{% endhint %}

As mentioned, normally there would be more math involved to help determine how fast the motors should move to reach the desired position. But for testing purposes, we are going to start by keeping it simple! Since the `setPower` function was covered in [previous sections](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-motor-basics#spinning-a-motor) and will communicate to the system what relative speed (or in this case duty cycle) is needed to get to the target, this can be used in the place of `setVelocity` for now.&#x20;

Add the lines to set the power of both motors to 80% of duty cycle.&#x20;

```java
waitForStart();

leftmotor.setTargetPosition(1000);
rightmotor.setTargetPosition(1000);

leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
rightmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);

leftmotor.setPower(0.8);
rightmotor.setPower(0.8);

while (opModeIsActive()){
        
        }
```

### Quick Check!

Build your OpMode and give it a test. What happens once you press play? What happens if you stop the program then start it again?

<details>

<summary>What happens when testing?</summary>

Likely your motors turned on when testing out the code to spin until they've reached the set position.

Some may have turned off once the position was reached, but you may also experience the motors twitching or making small adjustments in an attempt to reach the position. Then when starting the code again, the motor either continued twitching or did not move at all.

Recall we may need to reset our encoder to zero before running a program! The motor will continuously try to adjust until it hits the set position, but if it's already there it won't move!

Adjusting the power may help prevent the motor from overshooting the position and needing to repeatedly adjust.

</details>

### STOP\_AND\_RESET\_ENCODERS

For our demo code we will want to request our motors reset their encoders during the initialization process of the program.

Right before `waitForStart();` we can add `leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);` and `rightmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);` to our OpMode.

```java
public void runOpMode() {
        leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
        rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
        
        rightmotor.setDirection(DcMotor.Direction.REVERSE);
        
        leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        waitForStart();
```

## Setting up the whileLoop

Let's say we want our program to run only for however long it takes for the motors to reach designated position. Or maybe we intend for the robot to do something else after reaching the destination. For this we will need to edit our whileLoop block!

{% hint style="info" %}
Recall that, within a linear OpMode, a whileLoop must always have the `opModeIsActive()`  Boolean as a condition. This condition ensures that the whileLoop will terminate when the stop button is pressed.&#x20;
{% endhint %}

To the whileLoop let's add the  `leftmotor.isBusy()` and `righmotor.isBusy()`functions. This will check if the left motor and right motor are busy running to a target position. Once either motor reaches the target position the program will stop.

```java
while (opModeIsActive() && (leftmotor.isBusy() && rightmotor.isBusy())) {

}
```

Build your OpMode and give it a try!

As soon as the motors hit the desired position the program will end instead of continuously run in the event they do not perfectly hit the position.

{% hint style="info" %}
Right now the whileLoop is waiting for either motor to reach the target. There may be occasions when you want to wait for both motors to reach their target position. In this case the following loop can be used: &#x20;

`while (opModeIsActive() && (leftmotor.isBusy() || rightmotor.isBusy()))`
{% endhint %}
