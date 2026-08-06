> Source: https://docs.revrobotics.com/duo-control/menu/adding-more-motors/sparkmini-motor-controller.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/adding-more-motors/sparkmini-motor-controller.md).

# SPARKmini Motor Controller

The SPARKmini Motor Controller ([REV-31-1230](https://www.revrobotics.com/rev-31-1230/)) is an inexpensive in-line brushed DC motor controller designed to give *FIRST®* Tech Challenge teams more bang for their buck. It offers the same performance characteristics as the REV Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) or Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) motor ports in a small 60mm x 22mm footprint. Now FTC teams can add a SPARKmini Motor Controller to utilize more than four DC motors from a single Hub in a space-efficient package.&#x20;

### Power and Motor Connections

The SPARKmini has three integrated wires with connectors dedicated to power, control, and the motor; one [XT30 connector ](/duo-control/control-system-overview/cables-and-connectors/xt-30-power-cable.md)for power, one 3-wire servo-PWM connector for control, and one [JST-VH ](/duo-control/control-system-overview/cables-and-connectors/jst-vh-motor-power.md)connector for the motor. The figure below shows each of these connections.

![](/files/-M8S6x4RlQpD17v6ojlt)

Connect the power wire to a free XT30 port on the REV Control Hub , REV Expansion Hub (REV-31-1153), or through an XT30 Power Distribution Block (REV-31-1293) that is connected to a free Control/Expansion Hub XT30 port. Connect the control wire to an open servo port on the hub and the motor wire to a JST-VH port on a motor, like the REV HD Hex Motor ([REV-41-1301](https://www.revrobotics.com/rev-41-1301/)) or the REV Core Hex Motor ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)).

{% hint style="danger" %}
DO NOT reverse polarity on the power input connections. The SPARKmini does not contain reverse polarity protection. This can permanently damage the SPARKmini and will void the warranty.
{% endhint %}

{% hint style="danger" %}
DO NOT swap the motor and power connections. This can result in uncontrolled motor operation and can permanently damage the SPARKmini, voiding the warranty.
{% endhint %}

### &#x20;Servo-PWM Input

A motor’s speed is controlled by varying the voltage that is applied to it. The SPARKmini’s output voltage can be controlled by sending it an extended-range servo-PWM pulse. The extended 500µs to 2500µs servo-pulse corresponds to full-reverse and full-forward rotation with 1500µs as the neutral position (no rotation). The pulses are proportionally related to the motor output duty cycle, therefore variable speed can be achieved with pulses in between the extremes. The following table describes the pulse ranges in more detail.

Table - Control Signal Pulse Ranges

<table data-header-hidden><thead><tr><th>Pulse Width (p in µs)</th><th></th><th width="148"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Pulse Width (</strong><em><strong>p</strong></em><strong> in µs)</strong></td><td></td><td></td><td></td><td></td></tr><tr><td><strong>Full Reverse</strong></td><td><strong>Prop. Reverse</strong></td><td><strong>Neutral</strong></td><td><strong>Prop. Forward</strong></td><td><strong>Full Forward</strong></td></tr><tr><td><em>p</em> ≤ 500</td><td>500 &#x3C; <em>p</em> &#x3C; 1490</td><td>1490 ≤ <em>p</em> ≤ 1510</td><td>1510 &#x3C; <em>p</em> &#x3C; 2500</td><td>2500 ≤ <em>p</em></td></tr></tbody></table>

### Zero-Power Behavior

When the SPARKmini is receiving a neutral command it will not provide any power to the attached motor. There are two options for how the SPARKmini handles this zero-power state:

**Brake** - Motor terminals are shorted to each other to dissipate electrical energy, effectively braking the motor.\
**Coast** - Motor terminals are disconnected, allowing the motor to spin down at its own rate.

The zero-power behavior can be selected via a switch located towards the center of the SPARKmini housing, shown in Figure 2. Each mode can be selected by sliding the switch to either the Brake (B) or Coast (C) positions.

![Coast/Brake Switch](/files/-M8S6x4SV5pOuTuqJEl4)

The SPARKmini will indicate whether it is in Brake or Coast mode via the Status LED, located in the center of the housing, whenever it is outputting zero-power. Solid or flashing blue indicates Brake Mode while solid or flashing yellow indicates Coast Mode. See the LED Status Codes section for more details.

### LED Status Codes

![](/files/-MBpVtluQt88S1r89S-z)

### Specifications

| **Parameter**                   | **Min** |    **Typ**   | **Max** | **Unit** |
| ------------------------------- | :-----: | :----------: | :-----: | :------: |
| Supply voltage range (VIN)      |   6.0   |      12      |    20   |     V    |
| Supply voltage absolute maximum |    -    |       -      |    25   |     V    |
| Continuous output current       |    -    |       -      |    15   |     A    |
| Peak output current             |    -    |       -      |    20   |     A    |
| Output voltage range            |  - VIN  |       -      |  + VIN  |     V    |
| Output frequency                |    -    |      10      |    -    |    kHz   |
| Input pulse width range         |   500   |       -      |   2500  |    µs    |
| Input frequency                 |    16   |      50      |   200   |    Hz    |
| Input timeout                   |    -    |     65.5     |    -    |    ms    |
| Input deadband                  |    -    |      ±10     |    -    |    µs    |
| Input low-level voltage         |   -0.3  |       -      |   0.8   |     V    |
| Input high-level voltage        |   2.0   |      5.0     |   5.3   |     V    |
| Weight                          |    -    |     0.87     |    -    |    oz    |
| Dimensions (excluding wires)    |    -    | 60 x 22 x 12 |    -    |    mm    |
