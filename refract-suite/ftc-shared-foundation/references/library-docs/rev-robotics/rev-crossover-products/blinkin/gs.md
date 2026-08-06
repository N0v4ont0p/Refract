> Source: https://docs.revrobotics.com/rev-crossover-products/blinkin/gs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/blinkin/gs.md).

# Blinkin Getting Started

## Connections

<figure><img src="/files/-ME3jRDKotCAfcx2XKIs" alt="Image of Blinkin LED Driver pointing to locations of buttons and ports listed in the table below"><figcaption></figcaption></figure>

| **Mode/Up Button**           | Switch between normal running mode and set-up mode.                                                                                                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Strip Select/Down Button** | Switch which kind of LED strip is being controlled.                                                                                                                                                                                   |
| **XT30 Power Input**         | Connect to a 12V nominal battery or other equivalent power source.                                                                                                                                                                    |
| **PWM Input**                | Provide a standard servo-style PWM signal to control the LED output pattern/color.                                                                                                                                                    |
| **Status Indicator**         | RGB LED mode indicator. See Setup and Configuration for colors and meanings.                                                                                                                                                          |
| **Setup and Adjustment**     | Three potentiometers are used to set customer color palette colors and addressable strip length in set-up mode, and are used to adjust brightness and other pattern properties like speed and pattern density during normal operation |
| **5V/12V LED Indicators**    | Indicate which kind of strip is currently selected as the output type                                                                                                                                                                 |
| **LED Strip Connection**     | Use the included JST PH, 7-pin to JST SM pigtail connector to connect to LED strip(s).                                                                                                                                                |

## Setup and Configuration

1. Connect 12V power to the Blinkin using an XT30 Cable
2. Select either a 12V or 5V Addressable LED strip and connect it to the 7-Pin JST PH Port using a [Blinkin LED Cable Adapter (REV-11-1196)](https://www.revrobotics.com/rev-11-1196/)
3. If the LED output indicator for the 12V/5V strip which is connected is not lit, press and hold the Strip Select button until the corresponding strip indicator LED is lit. Your LED strip should now be displaying the default pattern (29 - Color Waves, Party Palette), or the user programmed default pattern.

![](/files/-MlGRGZTtqyDwm-O_Z0W)

![](/files/-MlGRKln21pkFSMm3xLA)

4. With no input PWM active (blue blinking Status LED), clicking (short press) the Up (Mode) and Down (Strip Select) buttons will change the pattern being displayed (See[ LED Pattern Tables](/rev-crossover-products/blinkin/gs/patterns.md)). This pattern will reset to the default after a power cycle unless the default is changed using the setup mode.

![](/files/-MlGRQ2rQdeDllSsKLVE)

## Setup Mode

In addition to the pre-programmed fixed color palette patterns, the Blinkin can be customized to use user selected colors and strip length to create more unique look. These settings can be saved in to permanent memory so they persist through power cycles.

#### Setup Mode Features

* **Addressable Strip Length** - Up to 240 WS2812 LEDs
* **Team Colors** - Select two of 22 different color options to represent your team
* **Default No Signal Pattern** - Select which pattern is displayed with there is not PWM input

### Setup Mode Steps

1. Power up the Blinkin as described in [Getting Started.](/rev-crossover-products/blinkin/gs.md#getting-started) The LED strip selected cannot be changed during setup mode, so ensure that the desired strip is connected and running before continuing.

![](/files/-MlGRh5CTO_tmoQclb1O)

2. To enter Setup Mode, press and hold the Mode button for \~6 seconds, the Status LED will change from blue to yellow. The LED strip will automatically display pattern 75 (Color 1 and Color 2: no blending) which uses Color 1 and Color 2 to aid in configuration.

![](/files/-MlGRkShn9bYuODj7k_h)

3. Use a small screwdriver, like the one included, to adjust the Color 1, Color 2, and Length potentiometers
   * Left: Color 1 – Primary Pattern Color
   * Middle: Color 2 – Secondary Pattern Color
   * Right: Addressable Strip Number of LEDs (1-240)

![](/files/-MlGRvetCfgtO5u4RHnU)

4. With no input PWM signal (yellow blinking Status LED), select the default no signal pattern by clicking (short press) the Up (Mode) and Down (Strip Select) buttons until the desired pattern is displayed.

![](/files/-MlGS8tss1mDnm1v5e3V)

{% hint style="success" %}
Leave the displayed pattern on the test pattern (75) on exit to leave the default no signal pattern unchanged.
{% endhint %}

### Exiting Setup Mode

* **Save and Exit:** Press and hold the Mode and Strip Select buttons for \~6 seconds. colors, strip length and new default no signal pattern values are permanently saved in EEPROM and will persist between power cycles.

![](/files/-MlGSD5qjhGHQU1M1lZU)

* **Exit without Saving:** press and hold the Mode button. Nothing is saved and Blinkin will return to its previously saved state after power cycle.

![](/files/-MlGSNtqrI-4BlVE558-)

{% hint style="success" %}
The **Status LED** will return to blue when Setup Mode has been exited
{% endhint %}

## PWM Control

The Blinkin can be controlled via software using a standard servo-style PWM signal. The Blinkin measures the width of the incoming pulse from the PWM signal, and then based on that value selects a pattern from a corresponding pattern table. Valid input pulse widths are from 1000us to 2000us.

1.) Connect the Blinkin to a PWM control port on the robot controller, such as a Control Hub or roboRIO, using a standard PWM cable.

2.) Using the programming language of your choice, generate a PWM signal.

{% hint style="info" %}
For use with the FRC Control System and WPILib, create a motor of type SPARK. (Other Motor and Servo types will work, but might change the values associated with specific patterns)
{% endhint %}

3.) In your main robot code where motor (or servo) output power is normally updated, set your output power to the value corresponding to the pattern desired (see [The LED Pattern Tables](/rev-crossover-products/blinkin/gs/patterns.md)).&#x20;

## Pattern Adjustments

All of the LED strips and patterns can have their overall brightness adjusted and many of the patterns can be adjusted to change the pattern density and speed. The[ LED Pattern Table](/rev-crossover-products/blinkin/gs/patterns.md) details what patterns have which adjustments.

1. While your Blinkin is not in Setup Mode, select a pattern which is adjustable
2. Use a small screwdriver, like the one included, to adjust the Adj. 1, Adj. 2, and Brightness potentiometers

<img src="/files/-MlGT3pwPpQv4dFNckFp" alt="" width="375">

{% hint style="info" %}
Generally, the three potentiometers will adjust the following during Normal Operation:

* Adj. 1  - Pattern Density, Pattern Width, or Dimming
* Adj. 2 - Speed
* Brightness - Brightness of the whole LED Strip
  {% endhint %}
