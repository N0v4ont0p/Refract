> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-essentials.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-essentials.md).

# Programming Essentials

During the process of creating an OpMode the OnBot Java tool prompted the selection of a sample code. In OnBot these samples act as templates; providing the outline and logical structure for different robotics use cases. In the previous section the sample code **BlankLinearOpMode** was selected. This sample code, seen in below, is the structural shell needed in order to have a working Linear OpMode.

{% hint style="info" %}
If using Robot Controller App v10.3 or newer the way templates are used has changed. [More information is available here](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/test-bed-onbot-java#tab-creating-an-onbot-java-file-10.3).&#x20;
{% endhint %}

```java
/*
Copyright 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.Blinker;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.util.ElapsedTime;

@TeleOp

public class HelloRobot_TeleOp extends LinearOpMode {
    private Blinker control_Hub;
    private DcMotor test_motor;
    private Servo test_servo;
    private TouchSensor test_touch;


    @Override
public void runOpMode() {
        control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");
        
        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
}
```

Throughout Hello Robot we will primarily be focusing on modifying the code found during our initialization process and **while loop** that runs when the **Play** button is pressed on the Driver Hub. As such, most examples will begin at `public void runOpMode()`.&#x20;

{% hint style="info" %}
When utilizing the samples provided in this tutorial, double check that the correct number of brackets and file names are added to your final program!
{% endhint %}

Let's take a quick tour of this template!

## Initialization:

Our first section of code is our hardwareMap. This is where our attached components are called and defined between the program and the configuration file

```java
        control_Hub = hardwareMap.get(Blinker.class, "Control Hub");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");
```

Within this area of our OpMode is anything we want to run BEFORE we press Play on the Driver Hub, but AFTER we press to initialize. This might include defining variables, motor directions, or servo positions!

## waitForStart();

```java
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
```

Any code following this our waitForStart(); but before our while loop begins will be read ONCE when our play button is pressed! This might be used for resetting timers.

## opModeIsActive()

```java
        while (opModeIsActive()) {
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
```

Last is our while loop! This is where any code we want to actively run and/or repeat until we press STOP is entered.&#x20;

You will complete the majority of your program here.

## Adding Comments

**Comments** are lines of code intended to help you the programmer.&#x20;

They can be used to explain the function of a section of code. This is especially helpful in collaborative programming environments. If code is handed from one programmer to another, comments communicate the intent of the code to the other programmer.&#x20;

You can see a few premade comments already in our template written by the FIRST Tech Team to help get started!

To create a comment add `//` before the comment to be made. This can also be used to temporarily remove a line of code as the robot will not read comments!

```java
       // Wait for the game to start (driver presses PLAY)
       // run until the end of the match (driver presses STOP)
```

## Common Errors

### Bracket Mismatch

OnBot Java will attempt to notify you if there are either TOO MANY brackets within your code or NOT ENOUGH brackets by highlighting the final line in red as seen below:

<figure><img src="/files/4bfOvJ01FEeNemVsXI0P" alt=""><figcaption></figcaption></figure>

The build errors may appear as below:

<figure><img src="/files/w3aw5fS5Wv3wXxuCArCb" alt=""><figcaption><p>A bracket appears to be missing from the program!</p></figcaption></figure>

<figure><img src="/files/mnmVvtDvfn6iZ4i1QNx4" alt=""><figcaption><p>There appears to be an extra bracket in the program!</p></figcaption></figure>

Keep in mind while checking your brackets that the error may be on a **different** line than the one reported! Take a look at the following example:

<figure><img src="/files/RAgmVqiv3299WHhnwHyB" alt=""><figcaption></figcaption></figure>

In this case, the missing bracket is on line 75 where my loop begins and should match with line 84's bracket. Once I have this corrected I can see the error clears:

<figure><img src="/files/DDKYyhVlXI2VNV9CyN0p" alt=""><figcaption></figcaption></figure>

### Mismatched File/Class Names

<figure><img src="/files/mRkkPNvLfQXnwfiZWlcv" alt=""><figcaption><p>Click to enlarge error image</p></figcaption></figure>

While building your program you may encounter an error stating the class name is public and needs to be declared. This error can be common while copying and pasting from an example or tutorial and is the result of a mismatched name between the file name and public class.&#x20;

Looking at the above example I can see my file is named "HelloRobot\_TeleOp.java", but my class is "HelloWorld\_TeleOp"!

<figure><img src="/files/O6UdsNMm5O6vRusArWQa" alt=""><figcaption></figcaption></figure>

To remedy this error, I could change my class name to match OR my file name. Which option is more ideal can be dependent on your end goal and how all your programs interact.

To change the name of a file, right click it on the list:

<figure><img src="/files/Vt1mm0ScyXvD0JhMABOg" alt=""><figcaption></figcaption></figure>

When renaming an OnBot Java file, the name is case sensitive and requires .java to be added to the end:

<figure><img src="/files/eHPABoQFYc5bVIk58BFU" alt=""><figcaption></figcaption></figure>

Alternatively, as previously mentioned, the public class name can be updated before building again to clear the error:

<figure><img src="/files/DOIuLtqGVlVRbjV2KM9w" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Always remember to Build your program after making major changes and before testing with your robot!&#x20;

![](/files/Iak8TjEMhAxhIsVERp2i)
{% endhint %}
