> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-color-sensors/color-sensor-telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-color-sensors/color-sensor-telemetry.md).

# Color Sensor Telemetry

We are going to add several telemetry sections within our program, but let's start by having our robot tell us how much red, green, or blue it sees when looking at an object with our Color Sensor.

```java
telemetry.addData("Red", "%.3f", colors.red);
telemetry.addData("Green", "%.3f", colors.green);
telemetry.addData("Blue", "%.3f", colors.blue);
```

For each telemetry line we are specifying first the label to be displayed on the Driver Hub's screen, "Red", "Green", or "Blue". Then we are setting our output to only be 3 decimal places using `"%.3f"`.&#x20;

Finally we ask the color sensor to report the amount seen of each color using `colors.red`, `colors.green,` or `colors.blue`.&#x20;

## Adding Hue, Saturation, and Value Telemetry <a href="#adding-hue-saturation-and-value-telemetry" id="adding-hue-saturation-and-value-telemetry"></a>

To add telemetry for hue, saturation, and value we will be using the class `JavaUtil` and matching method for the information we wish to add: `colorToHue`, `colorToSaturation`, or `colorToValue`.&#x20;

```java
telemetry.addData("Hue", JavaUtil.colorToHue(colors.toColor()));
telemetry.addData("Saturation", "%.3f", JavaUtil.colorToSaturation(colors.toColor()));
telemetry.addData("Value", "%.3f", JavaUtil.colorToValue(colors.toColor()));
```

Because we are using `NormalizedRGBA`  for our class of normalized color values, we need to take an extra step to be able to collect HSV components. By calling `toColor()` we are converting from a "FTC SDK RGBA Color Object"  to an "Android HSV Color Object".

Similarly to our individual colors, we use `"%.3f"` to show 3 decimal places for the value reported. While we can add this to Hue as well, this value should report as a much larger whole number. We'll look at this more closely in the next section!

### Quick Check! <a href="#quick-check" id="quick-check"></a>

Save your OpMode and give it a try! How do the values change depending on what color object the sensor is looking at?

{% hint style="info" %}
This feature requires the Color Sensor's LED to be switched on!
{% endhint %}

## Alpha Telemetry <a href="#alpha-telemetry" id="alpha-telemetry"></a>

While working on your code, you may have noticed something called "alpha". The alpha value of a surface tells how transparent or opaque it may be.

Using a similar method as before, we can add a telemetry call for the alpha value to see on our Driver Hub.

```java
telemetry.addData("Alpha", "%.3f", colors.alpha);
```

## Code Checkpoint

Here is how our OnBot Java code should look after setting up our color sensor to collect all the information!

```java
@TeleOp
public class HelloRobot_ColorSensor extends LinearOpMode {
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
     
     //Determining HSV and alpha 
            telemetry.addData("Hue", JavaUtil.colorToHue(colors.toColor()));
            telemetry.addData("Saturation", "%.3f", JavaUtil.colorToSaturation(colors.toColor()));
            telemetry.addData("Value", "%.3f", JavaUtil.colorToValue(colors.toColor()));
            telemetry.addData("Alpha", "%.3f", colors.alpha);
            telemetry.update();
        }
    }
}
```
