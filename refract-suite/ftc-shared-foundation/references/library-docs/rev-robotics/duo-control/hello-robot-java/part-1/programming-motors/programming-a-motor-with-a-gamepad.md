> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-a-motor-with-a-gamepad.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-motors/programming-a-motor-with-a-gamepad.md).

# Programming a Motor with a Gamepad

## Driving Motors with the Gamepad&#x20;

In the previous section you learned how to set the motor to run at a specific power level in a specific direction. However, in most applications, it will be necessary to control the motor with a gamepad, to easily change the direction or power level of a mechanism.&#x20;

We are able to use a button to set the motor to a specific power or we can program it so it changes based on the direction of one of the gamepad's joysticks!

Using our existing `test_motor.setPower(1);` we can replace the value of 1 with `this.gamepad1.left_stick_y;`&#x20;

```java
// run until the end of the match (driver presses STOP)
 
while (opModeIsActive()) {
            test_motor.setPower(this.gamepad1.left_stick_y);
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
```

Now the power of our motor will be set in response to the position of the gamepad's left joystick as it along the y-axis!

### Quick Check!

Build your OpMode and test it out with your gamepad! Think about the following questions while testing:

* What happens when you move the left joystick up a small amount versus a large amount?
* What happens if you move the joystick to the left or right along the X-axis?
* What happens if you move the joystick at a diagonal or rotate it 360 degrees?

You may notice that when moving along the X-axis nothing happens at the moment. However, once the joystick hits an angle near the Y-axis vertices the motor may start to jitter and spin.

## Adjusting Y-axis Direction

When you tested your program, did the motor spin the expected direction while moving the joystick up or down?&#x20;

In the FTC SDK for most controllers the Y value of a joystick ranges from -1 when a joystick is in its **topmost** position, to +1 when a joystick is in its **bottommost** position.&#x20;

That may be a little confusing to control, but we can add a **negative symbol**, or negation operator, to the line of code to change the direction of the motor in relation to the gamepad.&#x20;

```java
// run until the end of the match (driver presses STOP)
 
while (opModeIsActive()) {
            test_motor.setPower(-this.gamepad1.left_stick_y);
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
```
