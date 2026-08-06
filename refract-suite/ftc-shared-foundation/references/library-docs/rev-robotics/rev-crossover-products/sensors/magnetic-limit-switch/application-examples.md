> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/magnetic-limit-switch/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/magnetic-limit-switch/application-examples.md).

# Application Examples

## Application Information&#x20;

The REV Magnetic Limit Switch comes with two mountable magnets. Because this sensor does not require a contact interface, the magnet can also be soft-mounted almost anywhere with just tape or glue.

The strength of the magnetic field determines the maximum distance the magnet can be from the sensor and still be detected. Alternate (stronger or weaker) magnets can easily be used to change the trigger range of this sensor.

#### Hysteresis

<figure><img src="/files/DSleTKVqM1ygIANd7icC" alt=""><figcaption></figcaption></figure>

When designing a system using the REV Magnetic Limit Switch, it is important to consider the impact of hysteresis. When the magnetic field approaches the Magnetic Limit Switch, the sensor triggers after the field strength increases enough to cross the rising trigger point (Bop). As the magnet is then moved away from the sensor, the magnetic field strength falls, but the sensor remains in the triggered state until the field falls below the falling trigger level (BRP). The difference between these two points is the hysteresis.

For a simple system like stopping an arm at the end of range of motion, the hysteresis might not play much of a role, but for creating one or more stop points on a linear elevator, this may factor into the software design.

### FTC Applications&#x20;

#### Configuring in the Control System&#x20;

It is recommended that the Magnetic Limit Switch be configured as a "REV Touch Sensor" as shown below:

<figure><img src="/files/M2PoRCi5dU8zA5arMkXa" alt=""><figcaption></figcaption></figure>

In this example, the Magnetic Limit Switch is configured on port 3 as a "REV Touch Sensor". It is touched on briefly in the [Pinout Section](/rev-crossover-products/sensors/potentiometer/specifications.md#pinout-and-schematic) that the Magnetic Limit Switch is capable of sending a signal to the Control Hub through the n+1 and n communication channels. The channel the sensor communicates through is decided by which port it is configured on. In this case, the Magnetic Limit Switch communicates through the n channel.&#x20;

#### Programming Applications&#x20;

The code blocks below gives a basic example of how to use the Magnetic Limit Switch to limit the motion range of a motor using if/else logic. If the magnet is within range of the sensor, then the motor stops. Otherwise, the motor is allowed to move. When triggered by proximity to a magnet, the sensor is considered **pressed**.&#x20;

{% hint style="info" %}
To learn more about programming Touch and Limit Sensors check out Hello Robot for [Blocks ](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-touch-sensors#touch-sensor-basics)and [OnBot Java](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-touch-sensors)!
{% endhint %}

{% tabs %}
{% tab title="Blocks" %}

<figure><img src="/files/mEBk9ZqRTzEFxFRSWF6N" alt=""><figcaption><p>Certain blocks will not appear if the Magnetic Limit Switch is configured as just a "Digital Device"</p></figcaption></figure>
{% endtab %}

{% tab title="OnBot Java" %}
{% hint style="info" %}
The code assumes the sensor has been named "test\_magnetic" and the motor has been named "test\_motor" in configuration.&#x20;
{% endhint %}

```java
package org.firstinspires.ftc.teamcode;
 
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
 
@TeleOp
public class LimitSwitchTest extends LinearOpMode {
    // Define variables for our touch sensor and motor
    TouchSensor test_magnetic;
    DcMotor test_motor;
 
    @Override
    public void runOpMode() {
        // Get the touch sensor and motor from hardwareMap
        test_magnetic = hardwareMap.get(TouchSensor.class, "test_magnetic");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        
        // Wait for the play button to be pressed
        waitForStart();
 
        // Loop while the Op Mode is running
        while (opModeIsActive()) {
            // If the Magnetic Limit Swtch is pressed, stop the motor
            if (test_magnetic.isPressed()) {
                test_motor.setPower(0);
            } else { // Otherwise, run the motor
               test_motor.setPower(0.3);
            }
            
        telemetry.addData("Arm Motor Power:", test_motor.getPower());
        telemetry.update();
            }
    }
}
```

{% endtab %}
{% endtabs %}
