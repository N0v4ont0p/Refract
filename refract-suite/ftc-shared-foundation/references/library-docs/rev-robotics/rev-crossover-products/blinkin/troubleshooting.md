> Source: https://docs.revrobotics.com/rev-crossover-products/blinkin/troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/blinkin/troubleshooting.md).

# Blinkin Troubleshooting

## Status LED Patterns

<figure><img src="/files/I0BSlD2kHfZ5bVgoUrFi" alt="" width="563"><figcaption></figcaption></figure>

| LED Status                       | LED Description                          | Blinkin Status                           |
| -------------------------------- | ---------------------------------------- | ---------------------------------------- |
| ![](/files/SJuy4DPgmeib8Zr2xcId) | Status - Solid Blue                      | Normal Operation, PWM Signal Detected    |
| ![](/files/pW15E1KFDmczE8hLGnbG) | Status - Blinking Blue                   | Normal Operation, No PWM Signal Detected |
| ![](/files/sLaZacxTcryZPXGNv2uA) | Status - Solid Yellow                    | Setup Mode, PWM Signal Detected          |
| ![](/files/gOrBcVId6gIqrBcsIVH8) | Status - Blinking Yellow                 | Setup Mode, No PWM Signal Detected       |
| ![](/files/7jKJLpsyrsPFFGuPDwmP) | Status - Solid Blue with Magenta Blink † | Command Signal Detected                  |
| ![](/files/SJuy4DPgmeib8Zr2xcId) | 12V Output - Solid Blue ††               | 12V LED Strip Selected                   |
| ![](/files/SJuy4DPgmeib8Zr2xcId) | 5V Output - Solid Blue ††                | 5V Addressable LED Strip Selected        |

| †  | With some commands, the Magenta Blink may last until the next LED Pattern Command Signal has been received                   |
| -- | ---------------------------------------------------------------------------------------------------------------------------- |
| †† | If the 12V Output and 5V Output LEDs are on at the same time, please proceed to completing a [Factory Reset](#factory-reset) |

## **General Troubleshooting**

### LEDs near the end of a strip are dimmer, off color, or behaving erraticall&#x79;**.**

**Possible Cause:** LEDs are exceeding Blinkin current supply.

**Solution**: Turn down the strip brightness, shorten the strip, or use a pattern with less LEDs lit at the same time.

**Possible Cause:** There is too much voltage drop over the length of the strip so LEDs near the end don’t have enough voltage to operate properly.

**Solution:** Shorten the LED strip or if more LEDs are needed shorten the strip and run the remaining strip in parallel to the other strip

### Programmed pattern changing on robot start up/temporary power loss

**Possible Cause:** A spurious pulse when some robots start up or shut down matching a command code used when factory testing the Blinkin.

**Solution:**&#x20;

1. **Send the pulse (listed below) for the necessary strip type.** The Status LED should turn to solid magenta and the Strip Select LED will remain the same as it was before the command was sent.
   * 5V Strip = 2125 μs
   * 12V Strip = 2145 μs
2. **Send the pulse for a pattern different than the pattern that the Blinkin was originally displaying.** At this time the LEDs should change to the new strip and be set with the pattern you chose. The Status LED will go back to solid blue and the Strip Select LED will switch to the strip type you selected in Step 1.
3. **Send the pulse for the original desired pattern to your Blinkin.**

{% hint style="success" %}
We recommend having a button programmed on your controller to reset the pattern in the case of a temporary power loss.&#x20;
{% endhint %}

### Unable to Control via PWM

If a Blinkin LED Driver is able to run the pre-installed light sequences and is unable to be controlled via a standard PWM Signal, like those that control a Servo Motor, make sure the Blinkin and your Control Hub or roboRIO both share a power source or **have a shared electrical ground.** Most of the time, fixing the power input for your Blinkin will resolve this issue!

## Factory Reset

The Blinkin can store custom user settings in its Memory so that they persist through power cycles. To restore the Blinkin to factory default settings using the following procedure:

{% hint style="warning" %}
A factory reset will cause your Blinkin to reload the default values will into its permanent memory. All current settings will be deleted.
{% endhint %}

1. Power off the Blinkin
2. Press and hold the Mode and Strip Select buttons

![](/files/-MlGTcrtTLR5o4qNKrlK)

3. Power on the Blinkin

![](/files/-MlGTg7cxJNq8-d-4ONT)

4. Wait for \~2 Seconds
5. Release the Mode and Strip Select buttons
