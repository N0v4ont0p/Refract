> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/channel-pulse.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/channel-pulse.md).

# Channel Pulse

## Servo Pulse Width Control

Servo Motors are controlled using a technique called **Pulse Width Modulation (PWM)**, where the width of a pulse determines the servo's behavior. The pulse is typically sent to the servo every 20 milliseconds, and the duration of the pulse (measured in microseconds) communicates the desired position or speed.

## Angular Servos

For **angular servo motors**, the pulse width directly corresponds to the target position of the servo arm. The **Servo Hub** allows users to customize the pulse width range to suit their specific servo with a configurable minimum, maximum, and center position. Users can adjust these values to match the servo's capabilities or desired behavior.

* A shorter pulse width, typically either **1,000 µs (1 ms)**, or **500 µs (0.5ms)**, moves the servo to its minimum position (e.g., fully counterclockwise).
* A longer pulse width, typically either **2,000 µs (2 ms)**, or **2500 µs (2.5ms)**, moves the servo to its maximum position (e.g., fully clockwise).
* A pulse width near the midpoint, typically **1,500 µs (1.5 ms)**, positions the servo arm at the center.

#### Example Range:

| Pulse Width (µs) | Position               |
| ---------------- | ---------------------- |
| 500 µs           | Fully Counterclockwise |
| 1,500 µs         | Center                 |
| 2,500 µs         | Fully Clockwise        |

## Continuous Rotation Servos

For **continuous rotation servos**, the pulse width determines the direction and speed of rotation rather than position. The Servo Hub's configurable minimum, maximum, and center settings can also help calibrate continuous rotation servos. Fine adjustments can be made to the **center pulse width** to ensure the servo stops accurately at the neutral point.

* A pulse width of **1,500 µs (1.5 ms)** typically stops the servo (no movement).
* Shorter pulse widths (e.g., **1,000 µs**) cause the servo to rotate in one direction, with speed increasing as the pulse width decreases.
* Longer pulse widths (e.g., **2,000 µs**) cause the servo to rotate in the opposite direction, with speed increasing as the pulse width increases.

### Example Range (Typical):

| Pulse Width (µs) | Action                        |
| ---------------- | ----------------------------- |
| 500 µs           | Full Speed (Clockwise)        |
| 1,500 µs         | Stop                          |
| 2,500 µs         | Full Speed (Counterclockwise) |

***

### Tips and Tricks

Understanding how pulse width controls your servo and leveraging the REV Servo Hub's features can help optimize your servo’s performance for your robot. Test each servo to confirm its behavior and supported pulse width range before integrating it into your system. We suggest the following as a good place to start understanding your servo motors:

* **Servo Variations**: Always check the documentation for your specific servo, as pulse width ranges and behavior may vary.
* **Signal Integrity**: Ensure the PWM signal is clean and consistent to avoid jittering or erratic behavior.

***
