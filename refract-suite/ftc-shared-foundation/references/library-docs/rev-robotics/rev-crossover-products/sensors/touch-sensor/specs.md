> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/touch-sensor/specs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/touch-sensor/specs.md).

# Specifications

### General Specifications&#x20;

| **Parameter** | **Value and Units** |
| ------------- | ------------------- |
| Sensor Type   | Digital, Active-low |
| Signal        | n+1                 |

### Electrical Specifications

<table data-header-hidden><thead><tr><th width="274">Parameter</th><th width="105" align="center">Min</th><th width="100" align="center">Typ</th><th width="124" align="center">Max</th><th align="center">Units </th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong> </td></tr><tr><td>Operating Voltage Range</td><td align="center">-</td><td align="center">-</td><td align="center">3.3</td><td align="center">V</td></tr></tbody></table>

### Output States&#x20;

| **Button**  | **n+1 Voltage** | **LED State** | **FTC SDK Logic** |
| ----------- | --------------- | ------------- | ----------------- |
| Not Pressed | 3.3V            | Off           | TRUE              |
| Pressed     | 0V              | On            | FALSE             |

{% hint style="warning" %}
The button is directly in-line with the LED and signal. So if the light is operating correctly, the button is working.
{% endhint %}

## Mechanical Drawings&#x20;

<figure><img src="/files/D21TZaxQt972CK81EgWD" alt=""><figcaption></figcaption></figure>

## Pinout and Schematic&#x20;

In the image below, is the key for the wired connection between the touch sensor and the robot controller. The touch sensor does not use or pick up a signal from the **n** (blue) wire. This is not a problem if there is one digital sensor per port. However, If you intend to connect more than one digital sensor to the same port using the sensor splitter cable, make sure that the **n+1** (white) wire portion of the splitter cable is plugged into the touch sensor.&#x20;

<figure><img src="/files/DVP2k1Iusv19eQAXt7OP" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/TyP66N4e173h8VZR5FZc" alt=""><figcaption></figcaption></figure>
