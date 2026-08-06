> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/channel-power.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/channel-power.md).

# Channel Power

## Channel Power

The REV Servo Hub allows each servo channel to be powered individually. This lets users power only the channels they need at any given time. A channel can have power without a signal, or vice versa, depending on the configuration.

### FTC SDK with Control Hub

The FTC SDK does not currently support runtime control of channel power.

* Channels are always powered when enabled.
* When disabled, channels follow the configured Disable Behavior.

***

### REVLib for FRC and other Controllers

REVLib provides complete runtime control over channel power.

* Enabled channels can be turned on or off at any time via the robot program.
* Disabled channels always adhere to their Disable Behavior configuration, regardless of runtime settings.

## Disable Behavior

A program can dynamically control whether a channel is powered. However, some users may want a channel to supply power even when it’s disabled. To address this, the Disable Behavior configuration is provided. Each channel has its own Disable Behavior configuration, allowing fine-grained control.

{% hint style="warning" %}
**Important**: Ensure you understand your servo's behavior when it has power but no signal, as this may vary between models.
{% endhint %}

* **`kSupplyPower`**: Power is provided to the servo while disabled, but no signal is sent.
  * **Note**: The `kSupplyPower` setting is most similar to the behavior of the REV Servo Power Module, while the `kDoNotSupplyPower` setting is closer to the behavior of the Control Hub's servo ports. However, neither of these configurations is an exact match to these devices.
* **`kDoNotSupplyPower`**: Power is not provided to the servo while disabled.

### When to Use Each Disable Behavior

Selecting the appropriate Disable Behavior depends on your team's specific needs and the use case for each servo channel. Below are some scenarios where each behavior may be advantageous in **FIRST Tech Challenge (FTC)** or **FIRST Robotics Competition (FRC)**.

By carefully choosing the appropriate Disable Behavior for each servo channel, teams can optimize their robot’s performance and ensure reliable operation under various conditions. Testing your configuration during practice is highly recommended to avoid surprises during competition.

#### `kSupplyPower`

**When maintaining servo position is critical**: Use this behavior if your servo must hold its position even when disabled. For example:

* Keeping a gripper closed around a game element while the robot is temporarily disabled.
* Ensuring a mechanism like an arm or elevator stays in place when the robot is disabled during testing or a match pause.

**When transitioning from disabled to enabled needs to be seamless**: If the servo should maintain a consistent state (e.g., avoid sudden movements) when re-enabled, supplying power ensures the servo remains stable.

**When you know the servo behavior with no signal**: Servos behave differently when powered without a signal. Some may hold their position, while others may drift or "go limp", and others may return to the center position. Ensure you test your servos and understand their behavior in this mode.

***

#### `kDoNotSupplyPower`

**When the servo model exhibits undesirable behavior with power but no signal**: Some servo models behave unpredictably when powered but not receiving a signal. For example, certain servos may jitter or drift uncontrollably in this state, and others return to center position. In such cases, using `kDoNotSupplyPower` ensures that the servo does not power on until a valid signal is present.

**When servo movement while disabled is acceptable**: If the mechanism attached to the servo does not require precise positioning or locking, removing power can reduce wear on the servo.

* Example: Allowing an intake arm to fall into a "neutral" position when not powered.

**When protecting servos from overuse**: In some cases, continually powering a servo when disabled may contribute to overheating or wear. Use this mode to prolong servo lifespan.

***
