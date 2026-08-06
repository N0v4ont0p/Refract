> Source: https://docs.revrobotics.com/rev-hardware-client-2/guides/run-motor.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client-2/guides/run-motor.md).

# Make it Spin!

## Power On

Now that the device is wired and the connections carefully checked, power on the robot. You should see the SPARK Flex slowly blinking its light for a new device; the color will be Magenta. If the LED is dark or you see a different blink pattern, refer to the [Status LED](https://docs.revrobotics.com/brushless/spark-max/status-led) guide for troubleshooting.

{% hint style="info" %}
If you are using a brushed motor, you may see a sensor error. This is expected until you configure the device to accept a brushed motor in the following steps.
{% endhint %}

## Connect to the SPARK Flex

<figure><img src="/files/AZ10zzZBKlnzjZqtO7qR" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you can not see the SPARK Flex, make sure that the SPARK Flex is not being used by another application. Then unplug the SPARK Flex from the computer and plug it back in.
{% endhint %}

## Basic Setup and Configuration

Before any parameters can be changed, you **must** first assign a unique CAN ID to the device. This can be any number between 1 and 63. After setting a unique CAN ID, the user interface will refresh and allow you to change other parameters.

<figure><img src="/files/rNsEZ8t2uWGPiHoyOZrY" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Eventually, you may set up a CAN network on your test bench or robot. Be sure each device on the network has a unique CAN ID. It is helpful to label each device with its ID number to aid in troubleshooting.
{% endhint %}

## Set the Motor Type

If you are using a NEO or NEO 550, verify that the motor type is set to **REV NEO Brushless**, Sensor Type is **Hall Effect**, and the LED is blinking Magenta or Cyan.

<figure><img src="/files/wwv6fHtPCpGpUm7Nte9p" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you see a *Sensor Fault* blink code, make sure the encoder cable is plugged in completely.
{% endhint %}

## Limiting Current

There are two ways to protect your robot’s motors from electrical damage in high-current situations: Circuit Breakers and the SPARK Flex’s Smart Current Limit Setting. To protect your motors from currents that are too high, it is best practice to limit your current both with the SPARK Flex’s Smart Current Limit **and** an appropriately rated circuit breaker.

Circuit breakers, while an extremely important part of a robot's wiring and safety, are only designed to trip at a specific temperature, after a set amount of time, to protect the electrical system from fire or other electrical hazards. Due to this, we recommend setting a Smart Current Limit to protect your motors from damage due to high currents.

The SPARK Flex Motor Controller includes a Smart Current Limit feature that can adjust the applied output to the motor to maintain a constant phase current.

Out of the box, the SPARK Flex's Smart Current Limit default setting is 80A for any motor that you use. We recommend utilizing our[ Locked Rotor Testing documentation](/brushless/neo/locked-rotor-testing.md) or the table below to decide what to set your Smart Current Limit to for your robot.

{% hint style="danger" %}
Remember that some settings, like Smart Current Limit, must be burned to flash via code or the Hardware Client in order to be retained through a power cycle of the SPARK Flex.
{% endhint %}

### Suggested Current Limits

Your ideal current limit may vary based on your specific application, but these values can be used as a starting point to reduce the chance of an overload on your motor as you begin tuning your specific mechanism's Smart Current Limit.

| Motor Type                                                        | Current Limit Range |
| ----------------------------------------------------------------- | ------------------- |
| NEO [(REV-21-1650)](https://www.revrobotics.com/rev-21-1650/)     | 40A - 60A           |
| NEO 550 [(REV-21-1651)](https://www.revrobotics.com/rev-21-1651/) | 20A - 40A           |

{% hint style="warning" %}
Warning: Setting current limits outside of the suggested ranges listed above may cause unintended overload and severe damage to components that are not covered by warranty.
{% endhint %}

<figure><img src="/files/jhXu5TUCetFKzvbU7MS5" alt=""><figcaption></figcaption></figure>

## Save the Settings

The settings must be saved for the SPARK Flex to remember its new configuration through a power cycle. To do this, press the *Persist Parameters* button at the bottom right of the page. It will take a few seconds to save, indicated by the loading symbol on the button.

<figure><img src="/files/JPnzZgBdhYqNjx45Iwdk" alt=""><figcaption></figcaption></figure>

Any settings saved this way will be remembered when the device is powered back on. You can always restore the factory defaults if you need to reset the device.

## Spin the Motor

{% hint style="danger" %}
Before running any motor, make sure all components are in a safe state, that the motor is secured, and that anyone nearby is aware. FRC motors are very powerful and can quickly cause damage to people and property.
{% endhint %}

{% hint style="warning" %}
If the SPARK's CAN ID is still set to 0 when you attempt to run the motor, it will not spin. Ensure that the CAN ID has been properly set and that you have clicked the persist parameters button after [configuration](#basic-setup-and-configuration).&#x20;
{% endhint %}

{% hint style="info" %}
Keep the CAN cable disconnected throughout the test. For safety reasons, the REV Hardware Client will not run the motor if the roboRIO is connected. If the roboRIO was connected, power cycle the SPARK Flex.
{% endhint %}

To spin the motor, go to the Run tab, keep all of the default settings, and press *Run Motor*. The *setpoint* is 0 by default, meaning that the motor is being commanded to **idle** (0% power). When you press *Run* you should see the LED go from slow blinking to solid, indicating that the motor is idling.

<figure><img src="/files/brbEH2CdtPEuxZbjV12t" alt=""><figcaption></figcaption></figure>

**Slowly** ramp the setpoint slider up. The motor should start to spin, and you should see a green blink pattern proportional to the speed you have set for the motor. Slowly ramp the slider down. The motor should spin in reverse, and you should see a red blink pattern proportional to the speed you have set for the motor.

If you are unable to spin the motor, visit our [troubleshooting guide](https://docs.revrobotics.com/brushless/spark-max/troubleshooting).
