> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/touch-sensor/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/touch-sensor/application-examples.md).

# Application Examples

## Application Information

The REV Touch Sensor features an off-center button. Because this sensor requires a contact interface; the sensor must be mounted with regards to the location of the button and the object, or mechanism, intended to trigger the sensor.&#x20;

Common applications for the Touch Sensor, such as limit switches, require consideration for unconstrained, or twisting motion. Limit switches limit the range of motion for a mechanism. If the mechanism is not properly [constrained](https://docs.revrobotics.com/15mm/building-techniques/constraining-motion), there is a risk that the contact interface will not trigger the Touch Sensor.

### FTC Applications&#x20;

#### Configuring in the Control System&#x20;

Configure the Touch Sensor as "REV Touch Sensor" as shown in the image below.&#x20;

<figure><img src="/files/cDmyM5GrOJJyNNeCHZRH" alt=""><figcaption></figcaption></figure>

In this example, the Touch Sensor is configured on port one. It is touched on briefly in the[ Pinout Section ](/rev-crossover-products/sensors/touch-sensor/specs.md#pinout-and-schematic)that the Touch Sensor only sends a signal to the Control Hub through the n+1 communication channel. Because of this limitation, the Touch Sensor will only work when configured on the odd-numbered digital ports.&#x20;

#### Programming Applications&#x20;

The code blocks below give a basic example of how to use the Touch Sensor to limit the motion range of a motor using if/else logic. If the button is pressed then the motor stops. Otherwise, the motor is allowed to move.&#x20;

{% hint style="info" %}
To learn more about programming Touch Sensors check out Hello Robot for [Blocks ](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-touch-sensors#touch-sensor-basics)and [OnBot Java](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-touch-sensors)!
{% endhint %}

{% tabs %}
{% tab title="Blocks" %}

<figure><img src="/files/53wKFhUugzbBgtSIA3gY" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="OnBot Java" %}
{% hint style="info" %}
The code assumes the sensor has been named "test\_touch" and the motor has been named "test\_motor" in configuration.&#x20;
{% endhint %}

```java
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

@TeleOp

public class HelloRobot_TouchSensor extends LinearOpMode {
    TouchSensor test_touch;  // Touch sensor Object
    private DcMotor test_motor = null;
    private Servo test_servo = null;
    
    @Override
public void runOpMode() {
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        test_touch = hardwareMap.get(TouchSensor.class, "test_touch");
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
        
            if (touchSensor.isPressed()){
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
```

{% endtab %}
{% endtabs %}
