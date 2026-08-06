> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arm-control-onbot-java.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arm-control-onbot-java.md).

# Arm Control - OnBot Java

Now that our robot is able to drive around let's get our arm up and moving!

## Introduction to Arm Control&#x20;

![](/files/-Mbh_RZjnHpZbvvDsZ8H)

Controlling an arm requires a different thought process than the one you used to control the drivetrain. While the drivetrain uses the rotation motion of the motors to drive along a linear distance, an arm rotates along a central point, or joint.&#x20;

Unlike our drivetrain, our arm has physical limitations for how far it can rotate. We don't want our robot to damage itself so we'll be making use of our touch sensor to act as a limit switch.

## Basics of Programming an Arm

For this section, we will start by creating a new program called HelloRobot\_ArmControl. We will be able to add this to our drivetrain OpMode later, but for now keeping it separate will help us to focus just on the arm.

To control our arm we will be using the Dpad on our gamepad. While our joystick provides a range of possible values or float data, our Dpad will only be read as 1 or 0. To us these numbers translate to true, the button has been pressed, or false, the button has not been pressed.&#x20;

<details>

<summary>Click to Review Boolean vs. Float Data Types!</summary>

#### Boolean  (Dpad, a/b/y/x buttons, bumpers)

Boolean data has two possible values: **True and False**. These two values can also be represented by **On and Off** or **1 and 0**.&#x20;

The buttons, bumpers, and triggers on the gamepad provide boolean data to our robot! For example, a button that is not pressed will return a value of False (or 0) and a button that is pressed will return the value True (or 1).&#x20;

#### Float (Joysticks and triggers)

Float data is a number that can include decimal places and positive or negative values.&#x20;

On the gamepad, the float data returned will be between 1 and -1 for the joystick's position on each axis. Some examples of possible values are 0.44, 0, -0.29, or -1.&#x20;

</details>

To begin we can set up our If/else if statement for our Dpad Up and Dpad Down buttons inside our loop:

```java
while (opModeIsActive()) {
   if(gamepad1.dpad_up){
                
                }
   else if (gamepad1.dpad_down){
            
                } 
     }            
```

### Adding Motion

For now, our easiest path is to have our arm move up with DpadUp and down with DpadDown. You may decide later to change which buttons are being used, but the logic found here should be similar.

Let's add an `arm.setPower();` to each "do" section of our statement. While testing our movement we will want to reduce the power to a more manageable range. For now, we will set our up to 0.2 and down to -0.2.&#x20;

```java
if(gamepad1.dpad_up){
       arm.setPower(0.2);         
            }
else if (gamepad1.dpad_down){
       arm.setPower(-0.2); 
            }   
```

### Quick Check!

Save your OpMode and give it a go! Consider the following as test your program:

* What happens if you press up on the Dpad?
* What happens if you press down on the Dpad?
* What happens when neither button is actively pressed?

Did the robot move as you expected?

<details>

<summary>What happened while testing your program?</summary>

Likely, you noticed even when no button is pressed the motor continues to try to move the last direction inputted. This is more obvious when pressing the DpadUp button, but if you listen closely you'll be able to hear the motor trying to move downward once DpadDown is pressed as well.

Stalled movement such as this is not healthy for our motors nor is it the easiest to control. We'll want to fix this before we continue testing!

</details>

### Establishing an "Else"

The current if/else if statement tells the robot when the motor should move and in what direction, but nothing tells the motor to stop, thus the arm is continuing to run without limits. Ideally, we want our arm to move ONLY when a button is pressed.&#x20;

To fix this we can make our statement longer by adding an "else" at the end. This "else" will be checked last and let the robot know what to do when niether Dpad button is pressed!

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

With this change in place, save your program and give it another test!
