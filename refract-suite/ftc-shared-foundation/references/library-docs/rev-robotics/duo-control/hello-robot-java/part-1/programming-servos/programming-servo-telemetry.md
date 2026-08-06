> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/programming-servo-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-servos/programming-servo-telemetry.md).

# Programming Servo Telemetry

## &#x20;What is Telemetry?

**Telemetry** is the process of collecting and transmitting data.  In robotics ,telemetry is used to output internal data from the actuators and sensors to the Driver Hub. It is a way for the robot to communicate back to you the programmer what the robot thinks its doing or seeing. This information can then be used to improve your code, make adjustments to a mechanism, or to strategize when driving around the field if competing.&#x20;

For OnBot Java we can use the following to request the servo's position:

```java
test_servo.getPosition();
```

We already have a couple lines of telemetry within our code to let us know what state our program is in: "Initialized" or "Running". Below our if/else if statement we can add another `telemetry.addData();`.

First, we need to add a "string" or the text that we want to appear on our Driver Hub. For now we will enter this as `"Servo Position"`. After our comma, we will add the data we want outputted to the Driver Hub, which is `test_servo.getPosition();` .

```java
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
            
            telemetry.addData("Servo Position", test_servo.getPosition());
            telemetry.addData("Status", "Running");
            telemetry.update();

        }
```
