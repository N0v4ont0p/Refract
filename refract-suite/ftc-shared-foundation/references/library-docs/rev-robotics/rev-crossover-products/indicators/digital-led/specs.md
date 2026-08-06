> Source: https://docs.revrobotics.com/rev-crossover-products/indicators/digital-led/specs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/indicators/digital-led/specs.md).

# Specifications

## Electrical Specifications <a href="#electrical-specifications" id="electrical-specifications"></a>

| ​**Parameters**        | ​**Value and Units**                                           |
| ---------------------- | -------------------------------------------------------------- |
| Operating Voltage      | 3.3V                                                           |
| Current Draw (at 3.3V) | 20mA - single LED40mA - both LEDs                              |
| Input Type             | DIO (Active Low)                                               |
| Color Modes            | Red (Single LED on) Green (Single LED on) Amber (both LEDs on) |
| Forward Voltage        | 2.2V (Green)2.1V (Red)                                         |
| Viewing Angle          | 170 degrees                                                    |
| Dimensions             | 28mm x 13.5mm                                                  |
| Mounting Hole Diameter | 3.81mm (0.15")                                                 |

## Output Modes <a href="#output-modes" id="output-modes"></a>

| **n Digital Input** | **n+1 Digital Input** | **LED Mode** |
| ------------------- | --------------------- | ------------ |
| High                | High                  | Off          |
| High                | Low                   | Green        |
| Low                 | High                  | Red          |
| Low                 | Low                   | Amber        |

## Pinout

<figure><img src="/files/bq9q1yfXVYrs72Q8ad4u" alt=""><figcaption></figcaption></figure>

## Mechanical Drawing

<figure><img src="/files/YqCYl5DcpGz2SF63L3Qx" alt=""><figcaption></figcaption></figure>
