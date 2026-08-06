> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/color-sensor/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/color-sensor/application-examples.md).

# Application Examples

## Application Information&#x20;

The REV Robotics Color Sensor has two sensing elements: color and proximity.

Color measurements consist of Red, Green, Blue, and Alpha (clear) values. The white LED on the sensor has a slide switch to turn the LED on or off. Unlit targets are best illuminated with the build-in LED while bright or light-emitting targets may not require the build-in LED. Color data is best collected within 2cm of the target for the strongest color differentiation.

Proximity measurements are based on IR reflectance and can vary depending on lighting conditions and target reflectivity. The proximity sensor is ideally used to determine if something is in front of the sensor. While you can receive rough distance data, we recommend using the [2m Distance Sensor](http://www.revrobotics.com/rev-31-1505/) or similar time-of-flight sensor for accurate distance measurement.

### FTC Application&#x20;

#### Configuring for the Control System

{% hint style="warning" %}
**Note to users transitioning from Color Sensor V2 to V3:** Color values will not be consistent between V2 and V3 sensors and there are minor changes to the FTC SDK. Be sure to update to the latest SDK.
{% endhint %}

When working with the Color Sensor V3 configure your robot to use the "REV Color Sensor V3" as shown in the image below. &#x20;

<figure><img src="/files/OXILAe5Wl0tEfOuYdmCV" alt=""><figcaption></figcaption></figure>

In this example, the Color Sensor V3 is configured on I2C bus 1. The Color Sensor V3 can be configured on any of the I2C busses as long as a 2m Distance Sensor is not configured to the same bus.

{% hint style="info" %}
Recall that I2C sensors must have different addresses in order to operate on the same bus. The Color Sensor V3 and 2m Distance Sensor share the same address.&#x20;
{% endhint %}

#### Programming Example&#x20;

This program shows a readout of values from the Color Sensor on your Driver Hub's screen while the program runs. "Light Detected" shows the amount of light detected between 0 and 1.&#x20;

"Blue", "Red", and "Green" each show the amount of that "component" in the color the sensor is pointed at. If pointed at a red color, for example, it will likely have the highest amount shown.&#x20;

{% hint style="info" %}
To learn more about programming a Color Sensors check out Hello Robot for [Blocks ](/duo-control/hello-robot-blocks/part-1/programming-color-sensors.md)and [OnBot Java](/duo-control/hello-robot-java/part-1/programming-color-sensors.md)!
{% endhint %}

{% tabs %}
{% tab title="Blocks" %}

<figure><img src="/files/QoCM4jkXVU1ZYAJr6BcB" alt=""><figcaption><p>Example Blocks Code for the Color Sensor</p></figcaption></figure>
{% endtab %}

{% tab title="OnBot Java" %}
{% hint style="info" %}
The code assumes that the Color Sensor was configured with the name “test\_color.”
{% endhint %}

```java
@TeleOp
public class ColorSensorTest extends LinearOpMode {
    private NormalizedColorSensor test_color;
    
    @Override
    public void runOpMode() {
        test_color = hardwareMap.get(NormalizedColorSensor.class, "test_color");

        waitForStart();

        while (opModeIsActive()) {
            telemetry.addData("Light Detected", ((OpticalDistanceSensor) test_color).getLightDetected());
            NormalizedRGBA colors = test_color.getNormalizedColors();
    
    //Determining the amount of red, green, and blue
            telemetry.addData("Red", "%.3f", colors.red);
            telemetry.addData("Green", "%.3f", colors.green);
            telemetry.addData("Blue", "%.3f", colors.blue);
            telemetry.update();
        }
    }
}

```

{% endtab %}
{% endtabs %}

### FRC Application

{% embed url="<https://www.youtube.com/watch?v=KWw2hyv4rfQ>" %}

{% hint style="warning" %}
​When using the Color Sensor V3 on the navX’s I2C Interface, you will need to make sure that the Voltage Select Jumper on the navX is set to 3.3V. The Color Sensor V3 has a max operating voltage of 3.3V and applying 5V can damage the sensor.&#x20;
{% endhint %}

#### Software Libraries

* [Latest REVLib Installation Information](https://docs.revrobotics.com/brushless/revlib/revlib-overview)

#### API Documentation&#x20;

* [Online REVLib Java Documentation](https://codedocs.revrobotics.com/java/com/revrobotics/package-summary.html)
* [Online REVLib C++ Documentation ](https://codedocs.revrobotics.com/cpp/namespacerev.html)

#### REV Color Sensor V3 Example Code

* [C++ Examples](https://github.com/REVrobotics/Color-Sensor-v3-Examples/tree/master/C%2B%2B)
* [Java Examples](https://github.com/REVrobotics/Color-Sensor-v3-Examples/tree/master/Java)
* [LabVIEW Examples](https://github.com/REVrobotics/Color-Sensor-v3-Examples/tree/master/LabVIEW)

## Additional Resources

Additional information about the APDS-9151, its capabilities, and its features can be found in the following datasheet:

* [APDS-9151 Datasheet](https://docs.broadcom.com/docs/APDS-9151-DS)
