> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/tbe/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/tbe/application-examples.md).

# Application Examples

The REV Through Bore Encoder uses the Monolithic Power Systems MA600, a precision high-bandwidth magnetic angle sensor that detects the absolute angular position of a permanent magnet and geared to the through bore shaft hole. The MPS MA600 uses precision tunnel magnetoresistance technology to measure changes in the magnetic field as the shaft and magnet rotates.

A major benefit of the REV Through Bore Encoder is the flexibility of measuring any shaft in your system. Directly measuring the rotation of an output shaft allow users to read encoders without having to calculate gear ratios.&#x20;

## Cable Options

<table data-header-hidden><thead><tr><th width="151">Cable</th><th>Output Connector</th><th>Intended System</th><th>Output Signals</th></tr></thead><tbody><tr><td>Cable</td><td>Output Connector</td><td>Intended System</td><td>Output Signals</td></tr><tr><td><a href="https://www.revrobotics.com/rev-11-1275/">REV-11-1275</a></td><td>6-Pin JST PH</td><td>SPARK MAX Brushed Motor Mode</td><td>A, B, I, ABS</td></tr><tr><td><a href="https://www.revrobotics.com/rev-11-1817/">REV-11-1817</a></td><td>3-pin 0.1" Connector (PWM/Dupont) (4x)</td><td>roboRIO DIO</td><td>A, B, I, ABS</td></tr><tr><td><a href="https://www.revrobotics.com/rev-31-1815/">REV-31-1815</a></td><td>4-Pin JST PH</td><td>Control/Expansion Hub Encoder Port</td><td>A, B</td></tr></tbody></table>

## Wiring Examples

The Through Bore Encoder comes with several different cables making it easier to connect to different devices. Below are a few wiring examples for the more commonly used devices with the Through Bore Encoder.

### Control Hub (REV-31-1595)

To connect the Through Bore Encoder to a Control Hub, use the included JST PH 6-pin to JST PH 4-pin cable. The Through Bore Encoder plugs into the Encoder ports on the Control Hub.

<figure><img src="/files/fXaDWQTnynG2ILfwJ3LY" alt=""><figcaption></figcaption></figure>

### SPARK MAX (REV-11-2158)

Wiring of the Through Bore Encoder to a SPARK MAX changes depending on the motor type being used with the SPARK MAX. Both motor types use the included JST PH 6-pin cable.

#### Brushed Motors

When using a brushed motor with SPARK MAX, the Through Bore Encoder is connected directly to the Encoder Port on the front of the SPARK MAX.

<figure><img src="/files/8nmQiNzSIWLZYnD7m1ZL" alt=""><figcaption></figcaption></figure>

#### Brushless Motors

When using a brushless motor with SPARK MAX, the Through Bore Encoder is used as an Alternate Encoder. Using the Alternate Encoder Adapter (REV-11-1881) with the SPARK MAX allows for the JST PH 6-pin cable to connect directly to the adapter and the Through Bore Encoder.

{% hint style="danger" %}
Make sure to check the [Alternate Encoder Mode bring up in the SPARK MAX documentation](https://docs.revrobotics.com/brushless/spark-max/encoders/alternate-encoder) before connecting the Through Bore Encoder.
{% endhint %}

<figure><img src="/files/LAnNY1wpOYlfIciWnnFY" alt=""><figcaption></figcaption></figure>

### NI roboRIO

NI's roboRIO supports both quadrature and duty cycle encoders. There are slight differences in wiring depending on what mode is desired. Both wiring setups use the included JST PH 6-pin to 4 Channel PWM Cable.

#### Quadrature Encoder (Relative)

When using the Through Bore Encoder as a quadrature encoder, plug the ENC A (blue) and ENC B (yellow) signal lines into the DIO ports on the roboRIO.

<figure><img src="/files/pARZaaBgLAxYAmE3oRZV" alt=""><figcaption></figcaption></figure>

#### Duty Cycle Encoder (Absolute)

When using the Through Bore Encoder as a duty cycle encoder plug the ABS (white) signal line into a DIO port on the roboRIO.

<figure><img src="/files/Wj8idAuyybrlql6dSepI" alt=""><figcaption></figcaption></figure>

## Shaft Options&#x20;

### 1/2” Hex

This is the default shaft configuration that comes with the encoder out of the box.

<figure><img src="/files/oiawFRM6ImGhfadYgBgC" alt=""><figcaption></figcaption></figure>

### 3/8” Hex

When using the 3/8” Hex insert, press the insert into the 1/2” Hex hole.

If you are having difficulty pressing the insert into the encoder, try flipping the insert over and press it in. There is a slight taper in the insert, so it is recommended to press the insert with the smaller end first. When removing, it is recommended to push the insert out in the reverse order (larger end first).

<figure><img src="/files/NwKKWf9AgfDFvBdfooUE" alt=""><figcaption></figcaption></figure>

### 5mm Hex

When using the 5mm Hex insert, press the insert into the 1/2” Hex hole.

If you are having difficulty pressing the insert into the encoder, try flipping the insert over and press it in. There is a slight taper in the insert, so it is recommended to press the insert with the smaller end first. When removing, it is recommended to push the insert out in the reverse order (larger end first).

<figure><img src="/files/L91MDdHss2HK90Aavhkm" alt=""><figcaption></figcaption></figure>

### 1/4" Round

When using the 1/4” round insert, press the insert onto the shaft first and then place the encoder onto the insert.

This adapter fits the encoder shaft on common gearboxes like the Toughbox Mini, which is traditionally included in the FRC Kit of Parts Chassis.

<figure><img src="/files/YBMNUDlB5Gj4XQTiXIXH" alt=""><figcaption></figcaption></figure>

## Switch Options

There is a switch on the side of the encoder and with two options: ‘A’ and ‘S’. ‘A’ is the ABI encoder output mode which outputs the incremental and absolute encoder signals. ‘S’ is the SSI/SPI mode used in the manufacturing stage and potential future features. Currently, only the ‘A’ mode is supported. Make sure that the switch is in the ‘A’ position when using this encoder.

## AM14U KOP Chassis – Encoder Install

The REV Through Bore Encoder is specifically designed with the end user in mind, allowing teams to place sensors in the locations closest to the rotation that they wish to measure. Using the ¼” round insert allows teams to easily attach the Through Bore Encoder to the output shaft of the ToughBox Mini with the AM14U series kit of parts chassis. This guide is to show the process for attaching the Through Bore Encoder to the ToughBox Mini gearbox

* [AM14U KOP Chassis – Encoder Install](https://www.revrobotics.com/content/docs/REV-11-1271-AE.pdf)

{% hint style="info" %}
These instructions show the Through Bore Encoder (REV-11-1271) but the steps are the same for the Through Bore Encoder (REV-11-3174)
{% endhint %}

## Additional Resources

Additional information about the MPS MA600, its capabilities, and its features can be found in the following datasheet:

* [MPS MA600 Datasheet](https://www.mouser.com/pdfDocs/MA600GQ.pdf)
