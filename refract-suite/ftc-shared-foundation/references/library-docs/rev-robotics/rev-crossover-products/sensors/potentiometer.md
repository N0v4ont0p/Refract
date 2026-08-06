> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/potentiometer.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/potentiometer.md).

# Potentiometer

The REV Potentiometer ([REV-31-1155](https://www.revrobotics.com/rev-31-1155/)) converts the angular position of a shaft into an analog voltage signal. A potentiometer acts as an adjustable resistor, fluctuating resistance as the shaft is turned. As the wiper (the knob) moves up and down along the coils of the resistor and the resistance and voltage output change proportionally at each new position.‌&#x20;

<figure><img src="/files/Rhg8uW17hrtJB3BCb0y4" alt=""><figcaption></figcaption></figure>

The Potentiometer has a 270° limit to rotation. The sensor detects how much rotational motion has occurred in a mechanism. A specific limit is set in code to ensure rotation stops at a certain point. This is helpful when building simple arm joints because if properly applied it can prevent a mechanism from damaging itself or other parts of the robot.

{% hint style="warning" %}
It is important to install the Potentiometer so that it will not be forced beyond its 270° range of motion.
{% endhint %}

### Kit Contents

|                                  Part Number                                 | Description                      | Qty |
| :--------------------------------------------------------------------------: | -------------------------------- | :-: |
|            [REV-31-1155](https://www.revrobotics.com/rev-31-1155/)           | 2m Distance Sensor               |  1  |
| [REV-31-1407](https://www.revrobotics.com/jst-ph-4-pin-sensor-cable-4-pack/) | JST PH 4-pin Sensor Cable - 30cm |  1  |
