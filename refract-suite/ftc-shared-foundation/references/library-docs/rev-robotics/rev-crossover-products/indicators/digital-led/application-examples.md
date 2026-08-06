> Source: https://docs.revrobotics.com/rev-crossover-products/indicators/digital-led/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/indicators/digital-led/application-examples.md).

# Application Examples

The Digital LED Indicator produces light that is usable as visual feedback for a human user. Using the Digital LED Indicator to show what state the robot is in is useful for debugging autonomous and teleoperated programs. Other sensors used with the LED Indicator can let robot operators know a variety of things, from if the robot has game elements to the robot being blocked from completing an action.&#x20;

### FIRST Tech Challenge

#### Configuring in the Control System

Configure the green LED on port 0 as "green." Configure the red LED on port 1 as "red."

<figure><img src="/files/gTXdQVVPh0ZwYssvsB2z" alt=""><figcaption></figcaption></figure>

Each digital port on the Control (or Expansion) Hub is capable of acting as two separate ports, thanks to the two channels of communication. This is why the ports are marked as 0-1, 2-3, etc. The n+1 channel operates on odd-numbered ports 1-7 and the n channel operates on the even number ports 0-6. Due to the two channels of communication, the green and red LED must be configured on the ports that correspond with their respective channel of communication.&#x20;

{% hint style="info" %}
More information on digital ports and the channels of of communication on the Control and Expansions Hubs can be found in the Digital Sensor documentation. More information on the communication channels that the LED Indicator uses can be found in the [pinout](broken://spaces/-MQJfSTb0sZZYk8WELUn/pages/-MQJfczdO3Ji2uAj5iJO#pinout).&#x20;
{% endhint %}

#### Programming Examples

The sample code below changes the color of the Digital LED Indicator based on the state of a Touch Sensor ([REV-31-1425](https://www.revrobotics.com/rev-31-1425/)).

{% tabs %}
{% tab title="Blocks" %}

<figure><img src="/files/xaJsTNesWJF2WPtxiOfJ" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="OnBot Java" %}

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.LED;
import com.qualcomm.robotcore.hardware.DigitalChannel;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.util.ElapsedTime;

@TeleOp

public class LEDCode extends LinearOpMode {
    private DigitalChannel touch;
    private DigitalChannel redLED;
    private DigitalChannel greenLED;


    @Override
    public void runOpMode() {
        // Get the LED colors and touch sensor from the hardwaremap
        redLED = hardwareMap.get(DigitalChannel.class, "red");
        greenLED = hardwareMap.get(DigitalChannel.class, "green");
        touch = hardwareMap.get(DigitalChannel.class, "touch");
        
        // Wait for the play button to be pressed
        waitForStart();
        
            // change LED mode from input to output
            redLED.setMode(DigitalChannel.Mode.OUTPUT);
            greenLED.setMode(DigitalChannel.Mode.OUTPUT);

        // Loop while the Op Mode is running
            while (opModeIsActive()) {
                if (touch.getState()){
                //Touch Sensor is not pressed 
                    greenLED.setState(false);
                    redLED.setState(true);
                
                } else {
                    //Touch Sensor is pressed
                    redLED.setState(false);
                    greenLED.setState(true);
            }
        
        }
    }
}
```

{% endtab %}
{% endtabs %}
