> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/potentiometer/specifications.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/potentiometer/specifications.md).

# Specifications

## Specifications <a href="#specifications" id="specifications"></a>

### General Specifications <a href="#general-specifications" id="general-specifications"></a>

| **Parameter**       | **Value and Units**              |
| ------------------- | -------------------------------- |
| Sensor Type         | Analog                           |
| Signal Port Mapping | n                                |
| Output Shaft        | Female 5mm Hex                   |
| Mounting Holes      | REV Motion Pattern(6x M3 tapped) |
| Range of Motion     | 270°                             |
| Taper               | Linear (B)\*                     |

{% hint style="warning" %}
\*The linear taper of this potentiometer means that the resistance changes linearly with the angle of the shaft. However, the linearity can be significantly affected by connected circuitry. Please see the Application Examples for more information.
{% endhint %}

### Electrical Specifications <a href="#electrical-specifications" id="electrical-specifications"></a>

| **Parameter**    | **Min** | **Typ** | **Max** | **Units** |
| ---------------- | ------- | ------- | ------- | --------- |
| Total Resistance | -       | 10      | -       |           |

## Mechanical Drawing

{% hint style="info" %}
All dimensions are in millimeters
{% endhint %}

<figure><img src="/files/76VLjPnnvpiLztr2bQlf" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/KN91EGEfymi6f9HLIbMk" alt=""><figcaption></figcaption></figure>

## Pinout and Schematic&#x20;

The Potentiometer only sends signal to the hub through the **n** port, which means during configuration the potentiometer will need to be assigned to port 0 or port 2. This limitation means that two potentiometers can not be hosted on the same physical port using the sensor splitter cable.&#x20;

<figure><img src="/files/8f6vnDFVzfGrrpN1veUB" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/koeOQrqTBb3Dptove1jW" alt=""><figcaption></figcaption></figure>
