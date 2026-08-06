> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub.md).

# Servo Hub

## Servo Hub Overview

The REV Servo Hub is compatible with both the REV ION and REV DUO systems. Over a single communication interface, it can provide advanced control of up to six (6) servos. This means that the Servo Hub needs no additional PWM cabling between it and your robot controller, greatly simplifying wiring.

<figure><img src="/files/NC2T4mvvDGa3Q7ZrBvJn" alt=""><figcaption></figcaption></figure>

The Servo Hub is easy to update and configure over the USB-C connection utilizing the REV Hardware Client. With a total current output of 15A shared across all channels, the Servo Hub will give you the power you need to succeed on the field!

### Features

* Connectivity
  * USB
  * RS485
  * CAN
* Advanced Servo Channels
  * Status LED indicates PWM signal status and faults
  * Individual channel current measurement†
  * Individually switchable channel output power†
* Configurable output voltage††
* Over-current protection
* Reverse polarity protection
* ESD protection

|  †  | Features accessible through REV Hardware Client 2 and REVLib. Not accessible through the FTC SDK. |
| :-: | ------------------------------------------------------------------------------------------------- |
|  †† | Features available after future software updates.                                                 |

## Main Electrical Specifications&#x20;

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td>Operating Voltage Range</td><td>7</td><td>-</td><td>15</td><td>V</td></tr><tr><td>Output Voltage</td><td>0.5</td><td>-</td><td>7.4</td><td>V</td></tr><tr><td>Max Total Output </td><td>-</td><td>-</td><td>15</td><td>A</td></tr><tr><td>Channel Max Output Current †</td><td>-</td><td>-</td><td>3</td><td>A</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td><strong>Latching WAGO Connectors</strong></td><td></td><td></td><td></td><td></td></tr><tr><td>Supported Wire Gauge (Bare Solid/Stranded)</td><td>26</td><td></td><td>14</td><td>AWG</td></tr><tr><td>Bare Wire Strip Length</td><td>0.31</td><td>0.33</td><td>0.355</td><td>in</td></tr><tr><td>Supported Wire Gauge (Stranded, with ferrule)</td><td>24</td><td></td><td>18</td><td>AWG</td></tr><tr><td><strong>Servo Connectors</strong></td><td></td><td></td><td></td><td></td></tr><tr><td>Input</td><td>-</td><td>PWM cable (standard 3-wire 0.1” pitch)</td><td>-</td><td>-</td></tr><tr><td>Output</td><td>-</td><td>PWM cable (standard 3-wire 0.1” pitch)</td><td>-</td><td>-</td></tr></tbody></table>

| † | Please see the notes [About the Max. Current Specifications](#about-the-max.-current-specifications) for more information. |
| - | -------------------------------------------------------------------------------------------------------------------------- |

#### About the Maximum Current Specifications <a href="#about-the-max.-current-specifications" id="about-the-max.-current-specifications"></a>

Each of the Servo Hub's individual port pins are rated for approximately 3 A. This rating, of the port itself, highly depends on the quality of the connection between the Servo Hub and the connector of the servo it is driving.

The Servo Hub has been designed with powerful servos in mind.  Many of REV's customers' favorite servos have a stall current of 4 Amps or more. While we don't believe the 4 A stall current will produce enough heat to cause problems with a properly seated and quality connection, a poor connection can cause overheating and thermal runaway that can lead to damage.

The best way to ensure you are making the most of your Servo Power Module's output, is to check that all input and output connections are fully seated with no gaps.

#### **Output Current Calculations** <a href="#output-current-calculations" id="output-current-calculations"></a>

It is important to ensure that you do not exceed the maximum total output current of your Servo Power Module. To do this, add together the stall current of each servo being powered by the Servo Power Module. If the total stall current is higher than 15A, you risk triggering the overcurrent protection. Consider reducing the number of servos connected to prevent triggering the overcurrent protections.

## Mechanical Specifications

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Min</th><th>Typ</th><th>Max</th><th>Unit</th></tr></thead><tbody><tr><td>Number of Servo Channels</td><td>-</td><td>6</td><td>-</td><td>-</td></tr><tr><td>Length</td><td>-</td><td>85.7 (3.374)</td><td>-</td><td>mm(in)</td></tr><tr><td>Width</td><td>-</td><td>47.6 (1.874)</td><td>-</td><td>mm(in)</td></tr><tr><td>Height</td><td>-</td><td>18.3 (0.72)</td><td>-</td><td>mm(in)</td></tr><tr><td>Mounting Hole Diameter</td><td>-</td><td>#10 Clearance</td><td>-</td><td>-</td></tr><tr><td>Mounting Hole Pattern</td><td>-</td><td>3 by 1.5</td><td>-</td><td>in</td></tr></tbody></table>
