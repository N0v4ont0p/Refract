> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/2m-distance/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/2m-distance/application-examples.md).

# Application Examples

## Application Examples

While the REV 2m Distance Sensor produces a significantly more accurate and reliable measurement than other types of ranging sensors, the following tips will help minimize errors.

A major benefit to time-of-flight measurements is that the target’s surface reflectance does not significantly impact the calculated distance. However, the smallest errors and farthest measurements are achieved with more reflective targets. Similarly, larger targets are easier to detect because they fill more of the sensors 25° field of view.

Ambient infrared (IR) interference can also affect the measurement distance and quality. The sensor can produce accurate measurements in sunlit environments, but the maximum distance will be reduced. The following table outlines the typical ranging capabilities of the sensor:

| **Target Reflectance** | **Indoor** | **Outdoor (overcast)** |
| ---------------------- | ---------- | ---------------------- |
| White (88%)            | 200 cm †   | 80 cm                  |
| Grey (17%)             | 80 cm      | 50 cm                  |

|                                                                 |
| --------------------------------------------------------------- |
| † Using long range API profile; default profile range is 120cm. |

### FTC Applications

#### Configuring in the Control System&#x20;

Configure the 2m Distance Sensor as "REV 2M Distance Sensor," shown in the image below.&#x20;

<div><figure><img src="/files/KNNQHhtbLUnpdq03PAig" alt=""><figcaption></figcaption></figure> <figure><img src="/files/DrpfL0hM1v7pe8phjL0M" alt=""><figcaption></figcaption></figure></div>

{% hint style="info" %}
The Robot Controller Application currently only supports the default profile for the sensor.
{% endhint %}

In this example, the 2m Distance Sensor is configured on I2C bus 1. The 2m Distance Sensor can be configured on any of the I2C busses as long as a Color Sensor V3 is not configured to the same bus.

{% hint style="info" %}
Recall that I2C sensors must have different addresses in order to operate on the same bus. The Color Sensor V3 and 2m Distance Sensor share the same address.&#x20;
{% endhint %}

#### Programming Applications

This program moves a motor if there is an object less than 10 centimeters from the distance sensor, and stops it if there is no object within that range.

{% tabs %}
{% tab title="Blocks" %}

<figure><img src="/files/v7USygdQQBYWsVM1BYwC" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="OnBot Java" %}
{% hint style="info" %}
The Java version of this program is pasted below. It assumes that the Distance Sensor was configured with the name “test\_distance” and that a motor was configured with the name “test\_motor.”
{% endhint %}

```java
package org.firstinspires.ftc.teamcode;
 
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit;
import com.qualcomm.robotcore.hardware.DistanceSensor;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
 
@TeleOp
public class DistanceTest extends LinearOpMode {
    DistanceSensor test_distance;
    DcMotor test_motor;
    
    @Override
    public void runOpMode() {
        // Get the distance sensor and motor from hardwareMap
        test_distance = hardwareMap.get(DistanceSensor.class, "test_distance");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        
        // Loop while the Op Mode is running
        waitForStart();
        while (opModeIsActive()) {
            // If the distance in centimeters is less than 10, set the power to 0.3
            if (test_distance.getDistance(DistanceUnit.CM) < 10) {
                test_motor.setPower(0.3);
            } else {  // Otherwise, stop the motor
                test_motor.setPower(0);
            }
        }
    }
}
```

{% endtab %}
{% endtabs %}

### FRC Applications

For use with WPILib and the roboRIO the [proper library will need installation](https://github.com/REVrobotics/2m-Distance-Sensor). Utilize the roboRIO's I2C port and a 4-pin JST PH to 4-pin roboRIO I2C Cable ([REV-11-1729](https://www.revrobotics.com/rev-11-1729/)) to easily connect the sensor to the roboRIO.

* Example Code
  * [Java](https://github.com/REVrobotics/2m-Distance-Sensor/tree/master/Examples/Java)
  * [C++](https://github.com/REVrobotics/2m-Distance-Sensor/tree/master/Examples/C%2B%2B)
  * [Labview](https://github.com/REVrobotics/2m-Distance-Sensor/tree/master/LabVIEW)

## Additional Resources

Additional information about the VL53L0X, its capabilities, and the ST Application Programming Interface (API) can be found through the ST website:

* [VL53L0X Datasheet](http://www.st.com/resource/en/datasheet/vl53l0x.pdf)
* [VL53L0X API and Documentation](http://www.st.com/content/st_com/en/products/embedded-software/proximity-sensors-software/stsw-img005.html)
