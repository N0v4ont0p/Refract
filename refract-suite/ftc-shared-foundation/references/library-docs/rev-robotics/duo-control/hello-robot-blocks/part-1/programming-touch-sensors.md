> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-touch-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-touch-sensors.md).

# Programming Touch Sensors

{% hint style="danger" %}
This section applies to the use of the REV [Touch Sensor](https://www.revrobotics.com/rev-31-1425/) or [Limit Switch](https://www.revrobotics.com/rev-31-1462/). Requirements may vary when using other 3rd party touch sensors.&#x20;

The REV Touch Sensor must be configured to digital port 1, 3, 5, or 7.
{% endhint %}

{% hint style="warning" %}
It is recommended to create a new OpMode while following this tutorial. Ours is named HelloRobot\_TouchSensor!

The touch sensor block is now found under the "Sensors" dropdown as seen below:

<img src="/files/OngPcaG9OtBotNSCmdvj" alt="" data-size="original">
{% endhint %}

## Touch Sensor Basics

Let's start by breaking down how a touch sensor works at its core!

{% hint style="info" %}
Remember what sensors and motors are available in your program are determined by your configuration! Double check the correct configuration is active if you do not see a device list.
{% endhint %}

The information collected by a touch sensor comes in two states, also known as binary states. This information is perfect to use with a conditional statement like an `if/else` statement.&#x20;

The block ![](/files/tAdNI82YODFLdZjS3g10) collects the binary `TRUE/FALSE` state from the touch sensor and acts as the condition for the `if/else` statement.&#x20;

Let's take a look at our touch sensor block paired with our ![](/files/1zrcAjuGcQjm23V4jBT4) block:

<figure><img src="/files/lCSDcRzRocZrv14XUA0u" alt=""><figcaption></figcaption></figure>

Take a moment to think what this code is asking the robot to do. We could read this line of code as "If the touch sensor is pressed do \_\_\_\_, else if the touch sensor is not pressed do \_\_\_\_\_."&#x20;

### Adding Telemetry

It's always helpful for us to be able to see what the robot thinks its doing on our Driver Hub's screen. To do this, let's request the robot shares some telemetry data while our program is active.&#x20;

We can access the "Telemetry" blocks under our "Utilities" dropdown on the menu. Look for the ![](/files/stQsBRfRww9S5pROJQ3I)block to be added in each section of the if/else statement.&#x20;

<figure><img src="/files/04Gs3rI8b1pWau0pFeXu" alt=""><figcaption></figcaption></figure>

What happens if you run the program right now?

When on the default "Telemetry" block the information provided is not helpful for the robot to communicate with us. Therefore we need to change "key" and "text" to match the desired information.

<figure><img src="/files/Yy0OnDu6w2oO0BXEjVej" alt=""><figcaption></figcaption></figure>

The "key" should be something related to which sensor, motor, or other device we are receiving information from. Meanwhile "text" will tell us what is happening based on the state of our touch sensor and our if/else statement.&#x20;

Let's give our code another try to see what happens on the Driver Hub's Screen. Did you see something like the following?

<figure><img src="/files/7I1Qy4G1hOCI8dWPRRjM" alt=""><figcaption></figcaption></figure>

Remember its up to us to decide what our telemetry readout says. With that in mind we could change it so our robot says "Hello World" when the button is pressed:

<figure><img src="/files/pQ7nSvboa0dqE6wdWihl" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Take a moment to think about how else telemetry data could be used with your robot before moving on to the next section!
{% endhint %}

### Touch Sensor as a Limit Switch

At the moment, our robot does not have any senses to help navigate the world around it like you might. However, that's the key advantage to adding sensors to our design.&#x20;

For the touch sensor, one of the most common uses is for it to act as a [limit switch](/duo-control/sensors/digital.md#applications). This will help the robot know when it needs to halt the movement of a mechanism, like an arm or lift, that's at its limit similar to how your nerves help to tell your brain to do the same.

We can test this idea by adding on to our existing if/else statement. This time we are going to ask our motor to move until our sensor is pressed using the ![](/files/WwOqlD4U4KH2fIbMXknp) block:

<figure><img src="/files/pyzjJyCG9l31EddBymPG" alt=""><figcaption></figcaption></figure>

### Reversing it

In the above example the if/else is checking first for if the touch sensor is pressed. The full statement could be read as "If the touch sensor is pressed set the motor's power to 0 else, if it is not pressed, set the power to 0.3".

There may be situations where we want our program to read if the touch is NOT pressed first. Let's take a quick look at how that would function using the ![](/files/eflAt4g0DoBWZyquPoW4) block from the "Logic" menu.

<figure><img src="/files/Gz0uWycBu7E5CZb9DEaj" alt=""><figcaption></figcaption></figure>

Give it a try!
