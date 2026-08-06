> Source: https://docs.revrobotics.com/rev-crossover-products/blinkin/duo.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/blinkin/duo.md).

# REV DUO Application Examples

## FIRST Tech Challenge Programming    &#x20;

One of the most common requests from Control Hub users is how to use the Blinkin to signal to a driver different actions the robot is performing. The basic code below walks through how to use the SDK to code the Blinkin to different actions. When a certain gamepad button is pressed the LED turns a solid color, if no buttons are pressed the LED defaults to the Beats Per Minute pattern with a Forest Pallette.&#x20;

{% hint style="info" %}
For information on the different patterns visit the [LED Pattern Tables](/rev-crossover-products/blinkin/gs/patterns.md).&#x20;
{% endhint %}

{% tabs %}
{% tab title="Blocks" %}
![](/files/-Mbm_U4BIMyHd3LsUNxI)
{% endtab %}

{% tab title="OnBot Java" %}
{% hint style="info" %}
In Java the Blinkin LED pattern is assigned by using the CONSTANT\_CASE naming convention. For instance, if you would like to utilize the [Custom Color Pattern, Color Gradient](/rev-crossover-products/blinkin/gs/patterns.md#custom-color-patterns) the constant variable name is:

`CP1_2_COLOR_GRADIENT`
{% endhint %}

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.hardware.rev.RevBlinkinLedDriver;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.util.ElapsedTime;


@TeleOp

public class BlinkInTest extends LinearOpMode {
    RevBlinkinLedDriver blinkinLedDriver;
    RevBlinkinLedDriver.BlinkinPattern pattern;

    @Override
    public void runOpMode() {
        blinkinLedDriver = hardwareMap.get(RevBlinkinLedDriver.class, "blinkin");
        waitForStart();


        while (opModeIsActive()) {
            if(gamepad1.x){
                pattern = RevBlinkinLedDriver.BlinkinPattern.BLUE;
                blinkinLedDriver.setPattern(pattern);
            }
            else if(gamepad1.y){
                pattern = RevBlinkinLedDriver.BlinkinPattern.ORANGE;
                blinkinLedDriver.setPattern(pattern);
            }
            else if (gamepad1.b){
                pattern = RevBlinkinLedDriver.BlinkinPattern.WHITE;
                blinkinLedDriver.setPattern(pattern);
            }
            else if (gamepad1.a){
                pattern = RevBlinkinLedDriver.BlinkinPattern.VIOLET;
                blinkinLedDriver.setPattern(pattern);
            }
            else{
                pattern = RevBlinkinLedDriver.BlinkinPattern.BEATS_PER_MINUTE_FOREST_PALETTE;
                blinkinLedDriver.setPattern(pattern);
            }
            
            
        }
    }
}
```

{% endtab %}
{% endtabs %}

## Stand-Alone Wiring&#x20;

The Blinkin can run in a stand-alone operation mode when there is no way to generate a PWM signal, or a single output pattern is all that is needed. In this mode the Blinkin will be operating in Normal Mode with no input signal (blue blinking LED) and will default to the programmed no input signal pattern (factory setting is pattern 29 – Color Waves, Party Palette).

The currently displayed pattern can be changed at any time by pressing the up and down buttons to scroll through the [pattern list](/rev-crossover-products/blinkin/gs/patterns.md). Unless a new default no signal test pattern is saved in memory by completing the setup mode process, the Blinkin will default back to the last saved pattern after a power cycle.

![](/files/dZ7EOl5zEBbFgoblxLLR)

1. Connect to a 12V power source which can supply up to 5amps.&#x20;
2. Select either a 12V or 5V LED strip.
3. Follow through[ Setup and Configuration](/rev-crossover-products/blinkin/gs.md) to program to a default pattern.&#x20;

## Competition Robotics Application Ideas

Adding LEDs to your robot (or other project) can do more than just make them look cool, you can use LEDs to provide critical visual feedback. Here are some examples:

* Program a controller button to change the LED output pattern (e.g. 85 – Solid Yellow) and the drive can use the LEDs to communicate to the human player at a portal station across the field that the robot is ready to receive a game object.
* If the driver has poor visibility to see if the robot has acquired a game object, add a sensor to the intake and the LED strip can be programmed to automatically display a new pattern when the object is acquired. The driver never has to take their eyes off the robot to check the dashboard because the robot will clearly display its status.
* Using the match time value available in software, the LEDs can be changes to a time warning pattern (e.g. – Solid Red) with X seconds left in a match.
* The robot can display a different pattern when enabled vs disabled which provides a more visible indicator of the state of the robot than the RSL.
