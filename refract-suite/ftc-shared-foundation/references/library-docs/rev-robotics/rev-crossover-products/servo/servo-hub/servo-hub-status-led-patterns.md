> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/servo-hub-status-led-patterns.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/servo-hub-status-led-patterns.md).

# Servo Hub Status LED Patterns

## LED Indicators

The REV Servo Hub uses LEDs to provide visual feedback about the device's status and individual channel states. Understanding these indicators helps diagnose issues and monitor system performance.

{% hint style="info" %}
**Important**: These led patterns only apply to firmware version 24.0.0 and later
{% endhint %}

***

## General Status LED&#x20;

The main Status LED on the Servo Hub communicates the overall state of the device. Below is a table explaining the various patterns and their meanings:

<table><thead><tr><th width="180">LED Status</th><th width="229">LED Description</th><th width="142">When</th><th width="183">Hub Status</th></tr></thead><tbody><tr><td><img src="/files/EaIbJqI32Tm126YPvhut" alt="" data-size="line"></td><td>Magenta Blinking</td><td>Anytime</td><td>The Servo Hub is powered on but not connected to a controller or the REV Hardware Client.</td></tr><tr><td><img src="/files/6C99ZfyYnDuo3CEDGbJV" alt="" data-size="line"></td><td>Solid Cyan</td><td>Anytime</td><td>The Servo Hub is connected to the REV Hardware Client.</td></tr><tr><td><img src="/files/yAmWuZqOswVleDch8ddZ" alt="" data-size="line"></td><td>Green Solid</td><td>Anytime</td><td>The Servo Hub is connected to a roboRIO, Control Hub or other RS-485 controller. The number of blue blinks is the same as the Servo Hub's address. The factory default address is 3. †</td></tr><tr><td><img src="/files/tLJiUikWDHm6OB5tdp7t" alt="" data-size="line"></td><td>Orange/Cyan Blinking</td><td>Anytime</td><td>Battery Voltage is lower than 5.5V. Please check the Servo Hub's Power Supply. This fault will clear when the input voltage is raised above 6.5V.</td></tr><tr><td><img src="/files/otWTyKYmRG7Jfp8K0d5f" alt="" data-size="line"></td><td>Orange/Yellow Blinking</td><td>Anytime</td><td>A CAN fault has been detected. Verify CAN bus wiring and connections.</td></tr><tr><td><img src="/files/XQC41bTPGiOhSR2KnK0R" alt="" data-size="line"></td><td>Orange/Magenta Blinking</td><td>Anytime</td><td>An overcurrent fault has occurred. Check the connected servos and reduce the load if necessary.</td></tr></tbody></table>

| † | Faults are not reported to logs when the Servo Hub is connected via RS485. |
| - | -------------------------------------------------------------------------- |

***

## Channel Status LEDs

Each servo channel on the REV Servo Hub has its own dedicated LED, which provides feedback about the channel’s state and current PWM signal. Below is the meaning of each LED pattern:

#### Notes:

* Channel LEDs reflect the current state of the PWM signal, helping users verify servo behavior in real-time.
* Disabled channels still show feedback via a blinking amber LED, making it easy to differentiate inactive channels.

### Angular Servos<br>

<table><thead><tr><th>LED Status</th><th width="232">LED Description</th><th width="126">When</th><th>Hub Status</th></tr></thead><tbody><tr><td><img src="/files/YBuXnekFa6jjlDpsA4JQ" alt=""></td><td>Amber Solid</td><td>Anytime</td><td>The channel is at the center position (typically 1,500 µs pulse width).</td></tr><tr><td><img src="/files/jPtHhYgRmq6c7Rn5aCqf" alt="" data-size="line"></td><td>Green  Blinking</td><td>Anytime</td><td>The pulse width is between center and maximum (e.g., 1,500–2,000 µs).</td></tr><tr><td><img src="/files/otQbRiBvjSHuuMB5TIjU" alt="" data-size="line"></td><td>Green Solid</td><td>Anytime</td><td>The channel is at the maximum position (e.g., 2,000 µs).</td></tr><tr><td><img src="/files/pRoI2VRZkEM3I5Nu2k5j" alt="" data-size="line"></td><td>Red Blinking</td><td>Anytime</td><td>The pulse width is between center and minimum (e.g., 1,500–1,000 µs).</td></tr><tr><td><img src="/files/vF4Tz1S5AlgStIMnT8dK" alt="" data-size="line"></td><td>Red Solid</td><td>Anytime</td><td>The channel is at the minimum position (e.g., 1,000 µs).</td></tr><tr><td><img src="/files/0eKkceky097wsomAJAgc" alt=""></td><td>Amber Blinking</td><td>Anytime</td><td>The channel is disabled. The signal pin is pulled low, and no PWM signal is being sent.</td></tr><tr><td><img src="/files/xpyaKmRsFYYdjc1meval" alt="" data-size="line"></td><td>Quick Amber Blinking</td><td>Anytime</td><td>The channel is faulted. This can mean that either the device does not have sufficient power, neither the RoboRIO nor the Control Hub heartbeat is present, or the channel is experiencing an overcurrent event.</td></tr></tbody></table>

### Continuous Rotation Servos

<table><thead><tr><th>LED Status</th><th width="232">LED Description</th><th width="126">When</th><th>Hub Status</th></tr></thead><tbody><tr><td><img src="/files/YBuXnekFa6jjlDpsA4JQ" alt=""></td><td>Amber Solid</td><td>Anytime</td><td>The servo is stopped (typically 1,500 µs pulse width).</td></tr><tr><td><img src="/files/jPtHhYgRmq6c7Rn5aCqf" alt="" data-size="line"></td><td>Green  Blinking</td><td>Anytime</td><td>The servo is running forward (e.g., 1,500–2,000 µs).</td></tr><tr><td><img src="/files/otQbRiBvjSHuuMB5TIjU" alt="" data-size="line"></td><td>Green Solid</td><td>Anytime</td><td>The servo is running forward at maximum speed (e.g., 2,000 µs).</td></tr><tr><td><img src="/files/pRoI2VRZkEM3I5Nu2k5j" alt="" data-size="line"></td><td>Red Blinking</td><td>Anytime</td><td>The servo is running in reverse (e.g., 1,500–1,000 µs).</td></tr><tr><td><img src="/files/vF4Tz1S5AlgStIMnT8dK" alt="" data-size="line"></td><td>Red Solid</td><td>Anytime</td><td>The servo is running in reverse at full speed (e.g., 1,000 µs).</td></tr><tr><td><img src="/files/0eKkceky097wsomAJAgc" alt=""></td><td>Amber Blinking</td><td>Anytime</td><td>The channel is disabled. The signal pin is pulled low, and no PWM signal is being sent.</td></tr><tr><td><img src="/files/3cQulkczpF8Xvwv0TA6V" alt="" data-size="line"></td><td>Quick Amber Blinking</td><td>Anytime</td><td>The channel is faulted. This can mean that either the device does not have sufficient power, neither the RoboRIO nor the Control Hub heartbeat is present, or the channel is experiencing an overcurrent event.</td></tr></tbody></table>
