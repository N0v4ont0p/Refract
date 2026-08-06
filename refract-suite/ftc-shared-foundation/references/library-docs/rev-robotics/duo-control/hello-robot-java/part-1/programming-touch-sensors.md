> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-touch-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-touch-sensors.md).

# Programming Touch Sensors

{% hint style="danger" %}
This section applies to the use of the REV [Touch Sensor](https://www.revrobotics.com/rev-31-1425/) or [Limit Switch](https://www.revrobotics.com/rev-31-1462/). Requirements may vary when using other 3rd party touch sensors.&#x20;

The REV Touch Sensor must be configured to digital port 1, 3, 5, or 7.
{% endhint %}

## Touch Sensor Basics

{% hint style="info" %}
The following example code's file name is: HelloRobot\_TouchSensor
{% endhint %}

Let's start by breaking down how a touch sensor works at its core!

The information collected by a touch sensor comes in two states, also known as binary states. This information is perfect to use with a conditional statement like an `if/else` statement.&#x20;

The line `test_touch.isPressed();` collects the binary `TRUE/FALSE` state from the touch sensor and acts as the condition for the `if/else` statement.&#x20;

```java
if (test_touch.isPressed()){
    //Touch Sensor is pressed 
} else {
    //Touch Sensor is not pressed 
        }
```

The code above highlights the basics structure of the `if/else`*s*tatement for a touch sensor. We could read this line of code as "If the touch sensor is pressed do \_\_\_\_, else if the touch sensor is not pressed do \_\_\_\_\_."&#x20;

So with this in mind:

* Touch sensor pressed = true
* Touch sensor NOT pressed = false

### Adding Telemetry

It's always helpful for us to be able to see what the robot thinks its doing on our Driver Hub's screen. To do this let's request the robot shares some telemetry data while our program is active.&#x20;

Within our if/else statement we'll add a telemetry.addData for whether the touch sensor is pressed or not.

```java
            if (test_touch.isPressed()){
                //Touch Sensor is pressed.
                telemetry.addData("Touch Sensor", "Is Pressed");
            } else {
                //Touch Sensor is not pressed 
                telemetry.addData("Touch Sensor", "Is Not Pressed");
                        }
```

How our robot displays this data back to our Driver Hub is up to us to define. In this case we would see something similar to the following when the touch sensor is pressed:&#x20;

<figure><img src="/files/AvUI3Sa5GHY2lfEmYiWu" alt=""><figcaption></figcaption></figure>

The blue text within our quotation marks controls what will show on the Driver Hub. With that in mind we could have the robot say "Hello World!" when the button is pressed:

<figure><img src="/files/x7VCG0AQ3w238B0wqVUS" alt=""><figcaption></figcaption></figure>

To finish our program before testing we need to add a telemetry.update(); after our if/else statement to request our robot updates the telemetry each time it loops:

<pre class="language-java"><code class="lang-java">        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
        
            if (test_touch.isPressed()){
                //Touch Sensor is pressed.
                telemetry.addData("Touch Sensor", "Is Pressed");
            } else {
                //Touch Sensor is not pressed 
                telemetry.addData("Touch Sensor", "Is Not Pressed");
                        }
<strong>        telemetry.update();
</strong>}
</code></pre>

### Touch Sensor as a Limit Switch

At the moment, our robot does not have any senses to help navigate the world around it like you might. However, that's the key advantage to adding sensors to our design.&#x20;

For the touch sensor, one of the most common uses is for it to act as a [limit switch](/duo-control/sensors/digital.md#applications). This will help the robot know when it needs to halt the movement of a mechanism, like an arm or lift, that's at its limit similar to how your nerves help to tell your brain to do the same.

We can test this idea by adding on to our existing if/else statement. This time we are going to ask our motor to move until our sensor is pressed:

```java
 if (test_touch.isPressed()){
    //Touch Sensor is pressed  
     test_motor.setPower(0);
     telemetry.addData("Touch Sensor", "Is Pressed");
    
} else {
    //Touch Sensor is not pressed 
    test_motor.setPower(0.3);
    telemetry.addData("Touch Sensor", "Is Not Pressed");
                        }
```

Test it out! What happens when you test your program?&#x20;

You'll learn more about how to use this with a completed arm in Part 2: Robot Control!

<details>

<summary>Click to view full code!</summary>

<pre class="language-java"><code class="lang-java">import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

<strong>@TeleOp
</strong>
public class HelloRobot_TouchSensor extends LinearOpMode {
    TouchSensor test_touch;  // Touch sensor Object
    private DcMotor test_motor = null;
    private Servo test_servo = null;
    
    @Override
public void runOpMode() {
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_servo = hardwareMap.get(Servo.class, "test_servo");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
        
            if (test_touch.isPressed()){
                //Touch Sensor is pressed.
                test_motor.setPower(0);
                telemetry.addData("Touch Sensor", "Is Pressed");
            } else {
                //Touch Sensor is not pressed 
                test_motor.setPower(0.3);
                telemetry.addData("Touch Sensor", "Is Not Pressed");
                        }
        telemetry.update();
        }
    }
}
</code></pre>

</details>

### Reversing it

In the above example the *if/else* is checking first for if the touch sensor is pressed. The full statement could be read as "If the touch sensor is pressed set the motor's power to 0 else, if it is not pressed, set the power to 0.3". This statement can be reversed by adding a ! before test\_touch.isPressed().&#x20;

```java
   if (!test_touch.isPressed()){
            //Touch Sensor is not pressed  
           test_motor.setPower(0.3);
           telemetry.addData("Touch Sensor", "Is Not Pressed");
    
          } else {
            //Touch Sensor is pressed 
            test_motor.setPower(0);
            telemetry.addData("Touch Sensor", "Is Pressed");
                        }
```

In OnBot Java the operator ! tells the code to look for the opposite or to "not" be what is being called. So in this instance our if/else statement is checking if the touch sensor is NOT pressed first.&#x20;

Give it a try!
