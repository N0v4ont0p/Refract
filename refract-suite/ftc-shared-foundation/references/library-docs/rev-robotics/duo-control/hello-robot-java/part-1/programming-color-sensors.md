> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-color-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-color-sensors.md).

# Programming Color Sensors

{% hint style="info" %}
It is recommended to create a new OpMode while following this tutorial. Ours is named HelloRobot\_ColorSensor!
{% endhint %}

## Color Sensor Basics: <a href="#color-sensor-basics" id="color-sensor-basics"></a>

While a touch sensor features a physical switch to gather information, a color sensor makes use of reflected light. By doing so it collects different data to determine how much light it is seeing, the distance to a surface, and of course what color is in front of it.

### But what makes up a color? <a href="#but-what-makes-up-a-color" id="but-what-makes-up-a-color"></a>

For our robot we're going to focus on a few key components: hue, saturation, and value. With these we can use something known as the HSV color model to have the robot translate what its seeing into a recognizable color.

HSV is a form of a cylindrical RGB color model used to do things like create color pickers for digital painting programs, to edit photos, and for programming vision code.

Hue, saturation, and value all will play a part in helping our robot tell us what color it detects and allow us to make adjustments for something like a uniquely colored game piece!

### Detecting Light vs. Dark <a href="#detecting-light-vs.-dark" id="detecting-light-vs.-dark"></a>

Before we tackle colors, let's start with having our robot use the color sensor to tell us how much light is being reflected.

To do this we need to ask our color sensor to act as a light sensor, specifically an [OpticalDistanceSensor](https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/com/qualcomm/robotcore/hardware/OpticalDistanceSensor.html).

```java
 while (opModeIsActive()) {
            telemetry.addData("Light Detected", ((OpticalDistanceSensor) test_color).getLightDetected());
            telemetry.update();
   }
```

For this use case, we will use `getLightDetected()` to have the sensor report the amount of light detected in a range of 0-1.&#x20;

### Quick Check!

Time to test your program to see what your color sensor detects! While testing think about the following questions:

* Is the number higher when less or more light is detected?
* What happens when the color sensor looks at different color surfaces?
* Does the value change when turning the color sensor's LED light on or off?
* Does the value change if there is a shadow or if the lighting in the room changes?

<details>

<summary>What happened?</summary>

Likely, the numbers and differences you saw while testing are different than those we'd see ourselves. There are many factors that might change the color sensor's readings including the lighting in the room and surface material.

However, one thing that is the same is that 1 should be the least amount of light, such as when your hand is covering the sensor, and 0 is the most amount of light being seen.

</details>

## Normalized Colors <a href="#establishing-variables" id="establishing-variables"></a>

When using the option to "[Setup Code for Configured Hardware](/duo-control/hello-robot-java/part-1/test-bed-onbot-java.md)" while creating a new OpMode, the color sensor will be established similar to the following:&#x20;

```java
public class HelloRobot_ColorSensor extends LinearOpMode {
    private ColorSensor test_color;

    @Override
    public void runOpMode() {
        test_color = hardwareMap.get(ColorSensor.class, "test_color");
```

However, for this tutorial we want to set our color sensor up as a NormalizedColorSensor.&#x20;

Color Normalization is another technique within vision programming intended to help compensate for differences caused by lighting and shadows when looking at colors. This also affects shades of a color. For example, there are a ton of different shades of blue, such as cyan, navy, and aquamarine, but to our robot these will all be referenced as blue.

```java
public class HelloRobot_ColorSensor extends LinearOpMode {
    private NormalizedColorSensor test_color;
    
    @Override
    public void runOpMode() {
        test_color = hardwareMap.get(NormalizedColorSensor.class, "test_color");
```

With our color sensor now set for normalized colors, we'll add a call for `NormalizedRGBA` colors before we add telemetry for each individually.&#x20;

```java
while (opModeIsActive()) {
            telemetry.addData("Light Detected", ((OpticalDistanceSensor) test_color).getLightDetected());
            
            NormalizedRGBA colors = test_color.getNormalizedColors(); 
            telemetry.update();
        }
```

Now we're ready to collect more data from our color sensor!
