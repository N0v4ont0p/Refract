> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-flywheel-control.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-flywheel-control.md).

# Programming - Flywheel Control

All the flywheel controls are contained to the function setFlywheelVelocity.

<figure><img src="/files/rLRyIrSGFXZIdWDr71Wf" alt=""><figcaption><p>Flywheel if/else statement for auto and manual controls</p></figcaption></figure>

The flywheel has two main forms of operation:

* **Manual Control-** This will spin up ONLY the flywheel to the target velocity. The driver can then manually spin the Core Hex to feed balls.
* **Auto Control**- This will spin up the flywheel and activate the agigtator servo. Once the flywheel is in a specified range of the target velocity, the Core Hex will being to feed balls automatically. This is intended to be for a fully loaded robot to be able to make multiple shots in quick succession

Let's take a look at our entire if/else statement before exploring our Auto Control options.&#x20;

### Flywheel Control

<figure><img src="/files/euZofH6iM1grfYtTYE0L" alt=""><figcaption><p>Breakdown of flywheel buttons</p></figcaption></figure>

When holding the **"option" button** on the gamepad, the flywheel will spin in reverse at half power. This is intended to help with freeing stuck balls if needed.&#x20;

<figure><img src="/files/6skviwXlTWhIpYVsEtxc" alt=""><figcaption><p>Reversing the flywheel</p></figcaption></figure>

The **left bumper** or **right bumper** on the gamepad will request their specified function to run. We'll discuss these more below!

<figure><img src="/files/tNx3eenE6vbPuCITc3sm" alt=""><figcaption><p>Activating the flywheel launcher's "auto" modes</p></figcaption></figure>

When pressing the **"circle" button**, the flywheel will spin up to the set velocity for a "bank shot". This is the velocity for launching into the goal while against the goal or a couple inches back.&#x20;

When pressing the **"square" button**, the flywheel will spin up to the set "max" velocity. This may be used for launching balls at the goal with adjustments to the deflector, however is intended mostly for teams wanting to explore working with the flywheel and differences in velocity.&#x20;

<figure><img src="/files/LHntwuTY7dsT4fg7PkGe" alt=""><figcaption><p>Manual control for the flywheel</p></figcaption></figure>

{% hint style="info" %}
Be aware that launching balls at higher velocity can launch them to ceiling height. We do not recommend using this velocity option in rooms with low ceilings or hanging lights.&#x20;
{% endhint %}

### Turning off Actuators

<figure><img src="/files/TYb102TAU0XSZ7dpdoks" alt=""><figcaption><p>Setting all actuators to 0 power or velocity</p></figcaption></figure>

If no button is actively pressed on the gamepad, the flywheel, Core Hex feeder, and servo are told to set power or velocity to 0.&#x20;

The servo has an additional check to allow manual control on the Dpad to override this function and prevent stuttering in the movements.

<figure><img src="/files/Iec4kEawSvSNco8FND2x" alt=""><figcaption><p>Check to prevent the servo from stuttering</p></figcaption></figure>

## Auto Launching with the Flywheel

While a bumper is pressed on the gamepad, the servo, Core Hex feeder, and flywheel will all activate with the intent to launch multiple balls in succession.&#x20;

### Bank "Near" Shot Auto

<figure><img src="/files/rPnsMSRd6bHkndM65vBG" alt=""><figcaption><p>Code for the bank or "near" shot launching</p></figcaption></figure>

When **right bumper** is held, the above sequence will run until release. This is intended for launching balls into the goal from against the goal or a couple inches back.

The flywheel is set to spin to the preset "bankVelocity" continously and the agigtator servo will activate.&#x20;

Lastly, the robot will check first if the velocity of the flywheel is within 50 ticks below the "bankVelocity" before it will allow balls to fire. This value can be adjusted to be a bigger or tighter window if you notice the Core Hex is not feeding as expected.&#x20;

<figure><img src="/files/JlBHLZejIi8YxNcWgglx" alt=""><figcaption><p>Check to allow the flywheel to reach velocity between launches</p></figcaption></figure>

### "Far" Power Auto

<figure><img src="/files/9qjGPgNwHREvU3d3AHJF" alt=""><figcaption><p>Far power autonomous launching code</p></figcaption></figure>

When the left bumper is held, the above sequence will run until release. This is intended for launching balls into the goal from a few feet back from the goal. This may require adjustments to the deflector if teams prefer this approach.&#x20;

The flywheel is set to spin to the preset "farVelocity" continously and the agigtator servo will activate.

Similar to the bank auto, the robot will run a check to see if the flywheel velocity is currently within a specified window of the target "farVelocity" before it begins feeding. The default range is higher due to the increased velocity, but may be adjusted for further refinement.

{% hint style="info" %}
In the default code example, there is not a check for if the flywheel's velocity is above the "bankVelocity" or "farVelocity"  targets. Teams may consider adding this for additional refinement. Keep an eye out on our upgrades page for more information!
{% endhint %}
