> Source: https://docs.revrobotics.com/rev-crossover-products/gamepad/remapping-guide.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/gamepad/remapping-guide.md).

# Remapping Guide

## Getting Started

### Default Assignment

<figure><img src="/files/XZPOVfko6pknZ3Qgmowr" alt=""><figcaption><p>M1 and M2 buttons on the back of the gamepad</p></figcaption></figure>

Before the M1 and M2 buttons are mapped, they default to the following functions:

| Button | Default Function |
| ------ | ---------------- |
| M1     | Circle Button    |
| M2     | Cross Button     |

### Buttons for Remap can be set to be the following:

The following buttons can be mapped to M1 and M2:

* D-Pad Up, D-Pad Down, D-Pad Left, D-Pad Right
* Triangle, Circle, Square, Cross
* Right Trigger, Right Bumper, Right Joystick Button
* Left Trigger, Left Bumper, Left Joystick Button

## Remapping the M1 and M2 Buttons

### Enabling the M1 and M2 Buttons:

Before setting up the new function of your M1 and M2 Buttons, make sure that they are enabled!

<figure><img src="/files/DrEs1e0YchoAUBw6mx2c" alt=""><figcaption><p>Programming button on the back of the gamepad</p></figcaption></figure>

To enable or disable the M1/M2 Buttons press and hold the programming button for 3 seconds or until the indicator light blinks orange. The number of blinks will let you know what the&#x20;

* Two quick orange blinks – M1 and M2 Buttons are now **Disabled**
* One long orange blink – M1 and M2 Buttons are now **Enabled**

<figure><img src="/files/kqV12FWL7Lw1xLP8A9pL" alt=""><figcaption><p>Indicator light on the top of the gamepad</p></figcaption></figure>

### Steps to Remap the M1/M2 Buttons:

{% hint style="warning" %}
Once the M Buttons are remapped if the gamepad is reset or the mappings cleared the M Buttons will no longer act as active buttons until they are remapped again.
{% endhint %}

1. First, press and hold either the M1 or M2 button.&#x20;
2. While continuing to hold the M button, press the programming button. When the gamepad successfully enters remapping mode, the indicator light will turn orange.
3. Release the M button.
4. Press the button you would like to map. To map a M button as multiple buttons, press all desire buttons at the same time.&#x20;
5. Finally press the M button you selected in Step 1 to exit remapping mode. The indicator light will return to its original color.

### Clear M1/M2 Button Mapping:

1. First, press and hold the M  button you wish to clear.&#x20;
2. While continuing to hold the M button, press the programming button. When the gamepad successfully enters remapping mode, the indicator light will turn orange.
3. Release the M button.
4. Press the same M button again to exit remapping mode and clear the assigned mapping.&#x20;

## Example Program for Testing Mapping:

After remapping your M buttons, we recommend testing them with a simple program to ensure they are mapped as expected and in a way that is comfortable for the driver. This example outputs a letter to the Driver Hub's screen in response to the gamepad button pressed or when multiple buttons are pressed.&#x20;

<figure><img src="/files/isqycGeD828EwsY0kh1o" alt=""><figcaption><p>Example program for testing button mapping</p></figcaption></figure>

Here M1 has been mapped to act as both Square and Triangle while M2 is assigned to DpadRight. When M1 is pressed, the Driver Hub will show A on the screen. When M2 is pressed, B will be reported.

Finally, if Circle is pressed the output will be C. This is to act as a control for using a regular button on the gamepad.&#x20;

{% hint style="success" %}
When using our example below,  first click "Save OpMode" after uploading and opening it on your Control Hub. Update the gamepad buttons in code using the dropdown to match how you have remapped your M buttons.
{% endhint %}

{% file src="/files/WLUdAD5Bcnm9S6JqmEeW" %}
Test program for the gamepad
{% endfile %}
