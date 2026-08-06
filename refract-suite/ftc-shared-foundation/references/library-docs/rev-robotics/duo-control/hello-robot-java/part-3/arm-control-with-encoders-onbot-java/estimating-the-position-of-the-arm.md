> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/estimating-the-position-of-the-arm.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/arm-control-with-encoders-onbot-java/estimating-the-position-of-the-arm.md).

# Estimating the Position of the Arm

For this tutorial, our OpMode is named HelloRobot\_ArmEncoder!

## Estimating the Position of the Arm using Telemetry

Let's start by creating a simple program for moving our robot's arm. The one below will look very similar to the code created during [Part 2: Robot Control](/duo-control/hello-robot-java/part-2/arm-control-onbot-java.md)!

```java
if(gamepad1.dpad_up){
       arm.setPower(0.2);         
            }
else if (gamepad1.dpad_down){
       arm.setPower(-0.2); 
            }   
else { 
       arm.setPower(0); 
            } 
```

### Adding Telemetry

Within the while loop add the lines `telemetry.addData("Arm Test", arm.getCurrentPosition());` and `telemetry.update();`&#x20;

```java
while(opModeIsActive){
    if(gamepad1.dpad_up){
       arm.setPower(0.2);         
            }
     else if (gamepad1.dpad_down){
       arm.setPower(-0.2); 
            }   
     else { 
       arm.setPower(0); 
            } 
     telemetry.addData("Arm Test", arm.getCurrentPosition());
     telemetry.update();
          
 }
```

### Finding the Position with Telemetry

Build the OpMode and run it.

Use the gamepad commands to move the arm to the 90 degree position. Once you have the arm properly positioned read the telemetry off the Driver Hub to determine the encoder count relative to the position of the arm.

<figure><img src="/files/mzCjQkOdsPAnqp1xoevZ" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Remember that the encoder position is set to 0 each time the Control Hub is turned on! This means that if your arm is in a position other than the starting position when the Control Hub is turned on, that position becomes zero instead of the starting position.
{% endhint %}

### Adding RUN\_TO\_POSITION to the Program

To add the `RUN_TO_POSITION` code, the `if/else` statement must first have the following three lines of code need to be added:

```java
arm.setTargetPosition(0);
arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
arm.setPower(0);
```

When `DpadUp` is pressed, the arm should move to the the 90 degree position. When`DpadDown` is pressed the arm should move back to the starting position. To do this set the first`arm.setTargetPosition(0);` equal to the number of ticks it took your arm to get to 90 degrees, for this example we will use 83 ticks.&#x20;

Since we want `DpadDown` to return the arm to the starting position, keeping the  `arm.setTargetPosition(0);` set to 0 will allow us to accomplish this. Set both `arm.setPower(0);` equal to 0.5.&#x20;

```java
if(gamepad1.dpad_up){
     arm.setTargetPosition(83);
     arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
     arm.setPower(0.5);
            }
else if (gamepad1.dpad_down){
      arm.setTargetPosition(0);
      arm.setMode(DcMotor.RunMode.RUN_TO_POSITION);
      arm.setPower(0.5);
            } 
```

Despite our power being a positive value for both directions, the arm will move up or down based on the set position!

### Testing the Program

If you try running this code you may notice that the arm oscillates around the 90 degree position. When this behavior is present you should also notice the telemetry output for the encoder counts fluctuating.

Recall `RUN_TO_POSITION` is a **Closed Loop Control**, which means that if the arm does not perfectly reach the target position, the motor will continue to fluctuate until it does. When motors continue to oscillate and never quite reach the target position this may be a sign that the factors determining tolerances and other aspects of the closed loop are not tuned to this particular motor or mechanism.

There are ways to tune the motor, or ways to have the [program exit once the position is reached](/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot.md#setting-up-the-whileloop), but for now we want to focus on working with the arm and expanding on how limits and positions work with regards to the mechanism.
