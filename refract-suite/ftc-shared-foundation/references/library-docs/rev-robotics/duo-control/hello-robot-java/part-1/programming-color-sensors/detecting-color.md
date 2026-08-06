> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-color-sensors/detecting-color.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/programming-color-sensors/detecting-color.md).

# Detecting Color

We've asked our robot to gather a lot of data with the color sensor. Now let's have it use that information to output an actual color name rather than just a value!

## Adding a Hue Variable

To determine the final color we will be using the reported hue value from `JavaUtil.colorToHue(colors.toColor())`. Because we'll be using hue repeatedly, let's establish it as a variable to help keep our code clean.&#x20;

First we will set up "hue" as a number data type  during initialization:

```java
@TeleOp
public class HelloRobot_ColorSensor extends LinearOpMode {
    private NormalizedColorSensor test_color;
    double hue; // <------ New code
```

Next, we'll define "hue" while our `opModeIsActive` using the same method as before:

```java
while (opModeIsActive()) {
            telemetry.addData("Light Detected", ((OpticalDistanceSensor) test_color).getLightDetected());
            NormalizedRGBA colors = test_color.getNormalizedColors();
            hue = JavaUtil.colorToHue(colors.toColor()); // <------ New code
```

With our variable added, our current code should appear as follows:

```java
@TeleOp
public class HelloRobot_ColorSensor extends LinearOpMode {
    private NormalizedColorSensor test_color;
    double hue; // <------ New code
    
    @Override
    public void runOpMode() {
        test_color = hardwareMap.get(NormalizedColorSensor.class, "test_color");
​
        waitForStart();
​
        while (opModeIsActive()) {
            telemetry.addData("Light Detected", ((OpticalDistanceSensor) test_color).getLightDetected());
            NormalizedRGBA colors = test_color.getNormalizedColors();
            hue = JavaUtil.colorToHue(colors.toColor()); // <------ New code
    
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

## Detecting Common Colors <a href="#detecting-common-colors" id="detecting-common-colors"></a>

Recall when we learned about using [`if/else` statements while working with the touch sensor.](/duo-control/hello-robot-java/part-1/programming-touch-sensors.md#touch-sensor-basics)

Let's first set up the skeleton of our if/else statement for determining different colors:

```java
if(hue < 30){
          
  }
  else if (hue < 60) {
          
  }
  else if (hue < 90){
          
  }
  else if (hue < 150){
          
  }
  else if (hue < 225){
          
  }
  else if (hue < 350){
          
  }
  else{
          
      }
```

Each check will be for a certain color that is within the specified range. For example, a color that's hue is between 90-149 should appear as green.&#x20;

Within each statement let's add a `telemetry.addData` and the color for that range:

```java
 if(hue < 30){
          telemetry.addData("Color", "Red");
  }
  else if (hue < 60) {
          telemetry.addData("Color", "Orange");
  }
  else if (hue < 90){
          telemetry.addData("Color", "Yellow");
  }
  else if (hue < 150){
          telemetry.addData("Color", "Green");
  }
  else if (hue < 225){
          telemetry.addData("Color", "Blue");
  }
  else if (hue < 350){
          telemetry.addData("Color", "Purple");
  }
  else{
          telemetry.addData("Color", "Red");
  }
```

The exact hue values may need to be adjusted slightly, but those used above are based on the default conversion of HSV to RGB when using hue to identify color.

You'll notice that "red" is detected for values under 30 and above 350. This is intentional as red is the beginning and end of the RGB spectrum!

## Full Color Sensor Program

```java
@TeleOp
public class HelloRobot_ColorSensor extends LinearOpMode {
    private NormalizedColorSensor test_color;
    double hue; 
    
    @Override
    public void runOpMode() {
        test_color = hardwareMap.get(NormalizedColorSensor.class, "test_color");
        
        waitForStart();
        
        while (opModeIsActive()) {
            telemetry.addData("Light Detected", ((OpticalDistanceSensor) test_color).getLightDetected());
            NormalizedRGBA colors = test_color.getNormalizedColors();
            hue = JavaUtil.colorToHue(colors.toColor()); 
    
    //Determining the amount of red, green, and blue
            telemetry.addData("Red", "%.3f", colors.red);
            telemetry.addData("Green", "%.3f", colors.green);
            telemetry.addData("Blue", "%.3f", colors.blue);
     
     //Determining HSV and alpha 
            telemetry.addData("Hue", JavaUtil.colorToHue(colors.toColor()));
            telemetry.addData("Saturation", "%.3f", JavaUtil.colorToSaturation(colors.toColor()));
            telemetry.addData("Value", "%.3f", JavaUtil.colorToValue(colors.toColor()));
            telemetry.addData("Alpha", "%.3f", colors.alpha);
       
       //Using hue to detect color
         if(hue < 30){
                 telemetry.addData("Color", "Red");
                 }
          else if (hue < 60) {
                 telemetry.addData("Color", "Orange");
                 }
          else if (hue < 90){
                 telemetry.addData("Color", "Yellow");
                }
          else if (hue < 150){
                 telemetry.addData("Color", "Green");
                }
          else if (hue < 225){
                 telemetry.addData("Color", "Blue");
                }
          else if (hue < 350){
                 telemetry.addData("Color", "Purple");
                }
          else{
                 telemetry.addData("Color", "Red");
                }
            telemetry.update();
        }
    }
}
```

Build your OpMode and give it a try! You can adjust the values as you need to better reflect the colors available or changes due to lighting in the room.
