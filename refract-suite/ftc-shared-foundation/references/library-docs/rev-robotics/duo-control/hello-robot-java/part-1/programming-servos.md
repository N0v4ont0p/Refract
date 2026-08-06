> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos.md).

# Programming Servos

## What is a Servo?

{% hint style="info" %}
This section is considering the Smart Robot Servo in its default mode. If your servo has been changed to function in continuous mode or with angular limits it will not behave the same using the code examples below. You can learn more about the [Smart Robot Servo](https://docs.revrobotics.com/rev-crossover-products/servo/srs) or changing the Servo's mode via the [SRS Programmer](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer) by clicking the hyperlinks.&#x20;
{% endhint %}

A servo is a form of actuator, or a device designed for moving. With a typical servo, you can specify a target position. The servo will turn its motor shaft to move to the target position, and then maintain that position, even if moderate forces are applied to try and disturb its position.

For Hello Robot we will be using the [Smart Robot Servo](https://www.revrobotics.com/rev-41-1097/), which is able to switch between a **continuous** and **angular** mode.

* **Continuous mode** allows for the servo to rotate a full 360°, either direction, indefinitely similar to a standard motor.
* **Angular mode** sets the servo to move to specified positions within a 270° range of motion.

Let's take a look at how to program our servo while it is on angular mode:

<figure><img src="/files/aF94KUD3kEW4hcAvyk1f" alt=""><figcaption></figcaption></figure>

While most common servos have a range of 180° for motion, the Smart Robot Servo has a range of 270° due to its ability to switch between modes. When programming this means our 0 and 1 position might be a little different than what you'd expect.

Looking at the image above we can see that on **default** when asking our servo to move to its position 0 it will be at -135° . On the opposite end, moving to its position 1 takes our servo to +135° . Therefore if we wanted to return to 0°  we would need to program it to move to its position 0.5.

{% hint style="warning" %}
A servo horn attachment connected to your Smart Robot Servo may effect where 0° appears. We recommend using a SRS programmer to set the servo to zero before adding attachments. This may also be done using the code learned in this section!
{% endhint %}

### Quick Check

Let's review quick our basic positions:

| Programmed Position | Degrees |
| ------------------- | ------- |
| 0                   | -135°   |
| 0.5                 | 0°      |
| 1                   | 135°    |

Based on what we've learned so far, think about the follow two questions:

1. If we wanted our servo to move to -67.5° what **position** would we program it move to?
2. If we have programmed our servo to move to position 0.7, what would that equal in **degrees**?

<details>

<summary>Click to reveal the answers</summary>

1. Breaking it down we can see that -67.5° would be half of our movement between 0°  and -135° . Therefore, we will set our position to halfway between 0 and 0.5 equaling 0.25.&#x20;
2. This second question requires a little more math. Let's think about how far our servo would move for each 0.1 of a position. Our total movement is 270° so if divided by 10 we know 0.1 = 27°. Going from there we can do the math starting from the 0° we know position 0.5 brings us to. Therefore, moving to position 0.7 should be 54°.&#x20;

</details>

{% hint style="info" %}
For Hello Robot we will only be programming using positions. Understanding their translation to degrees is still important, however, to help think through designing a mechanism. Degrees may also be preferred when using a direct [pulse input](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer/switching-operating-modes#switching-operation-modes) to program the servo.&#x20;
{% endhint %}

## Let's get Programming!

In the next few sections, we will be learning to program our servo to first move automatically to different requested positions then in response to our gamepad's input.&#x20;

***

<table data-header-hidden><thead><tr><th width="247"></th><th></th><th></th></tr></thead><tbody><tr><td><a href="/pages/qjU3MdvmhtCfUOguxckB">Programming Servo Basics</a></td><td><a href="/pages/MUC7z5JU4ZHnvqahvvZN">Using a Gamepad with a Servo</a></td><td><a href="/pages/sRz305kEgXnDrJEOqCut">Programming Servo Telemetry</a></td></tr></tbody></table>

Below is a sneak peek of our final full code:

```java
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
        
        test_servo.setPosition(0);

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            if (gamepad1.y){
                //move to position 0
                test_servo.setPosition(0);
    
            } else if (gamepad1.x || gamepad1.b) {
                //move to position 0.5
                test_servo.setPosition(0.5);

            } else if (gamepad1.a) {
                //move to position 1
                test_servo.setPosition(1);
                        }
            telemetry.addData("Servo Position", test_servo.getPosition());
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
    }
```
