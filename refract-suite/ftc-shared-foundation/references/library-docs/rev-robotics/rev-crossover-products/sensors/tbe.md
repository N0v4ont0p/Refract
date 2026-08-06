> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/tbe.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/tbe.md).

# Through Bore Encoder V2

The REV Through Bore Encoder V2 provides precise, reliable shaft position measurement with both incremental (ABI quadrature) and absolute (pulse-width) outputs

The Through Bore Encoder V2 delivers higher measurement accuracy—up to ±0.5°—while maintaining strong performance in environments where dust or debris may affect optical encoders. The magnetic sensing design offers consistent feedback without the need for complex alignment or maintenance.

<figure><img src="/files/Nbi4IBTIPsJO2fX1tZCD" alt=""><figcaption></figcaption></figure>

### Features

* Incremental and absolute magnetic encoder
  * Built-in magnet
  * Quadrature output - A, B, and Index
  * Absolute output - Pulse Width (Duty Cycle)
  * MPS MA600
* Factory calibrated zero-position
  * Zero calibrated to notch in case
* Through-bore design
  * Easily mounted to any shaft with optional bore inserts
  * 1/2in Hex (default)
  * 3/8in Hex
  * 5mm Hex
  * 1/4in Round
* Mounting holes
  * Hole spacing matches common 0.5in pitch (MAXTube, MAXPlanetary, etc.)<br>

{% hint style="warning" %}
The FTC Control System currently only supports Incremental Encoder input through the motor encoder ports. Absolute pulse input is not supported.
{% endhint %}

{% hint style="danger" %}
**Do not disassemble the sensor.** Disassembling the Through Bore Encoder will dereference the zero position with the physical case notch. It is not possible to recalibrate the zero position as it is permanently saved inside the sensor at the factory
{% endhint %}

### Kit Contents

|                       Part Number                       | Description                                       | Qty |
| :-----------------------------------------------------: | ------------------------------------------------- | :-: |
| [REV-11-1271](https://www.revrobotics.com/rev-11-1271/) | Through Bore Encoder V2                           |  1  |
| [REV-25-1870](https://www.revrobotics.com/REV-25-1870/) | Through Bore Encoder Insert Pack                  |  1  |
|                            -                            | 3/8" Hex Insert                                   |  1  |
|                            -                            | 5mm Hex Insert                                    |  1  |
|                            -                            | 1/4" Round Insert                                 |  1  |
| [REV-11-1275](https://www.revrobotics.com/rev-11-1275/) | JST-PH 6-pin to JST-PH 6-pin Cable                |  1  |
| [REV-11-1817](https://www.revrobotics.com/rev-11-1817/) | JST-PH 6-pin to 4 x 3-pin 0.1" (PWM/Dupont) Cable |  1  |
| [REV-31-1815](https://www.revrobotics.com/rev-31-1815/) | JST-PH 6-pin to JST-PH 4-pin Cable                |  1  |
