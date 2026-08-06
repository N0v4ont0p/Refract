> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/tbe/specs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/tbe/specs.md).

# Specifications

## General Specifications

| **Parameter**  | **Value and Units**                  |
| -------------- | ------------------------------------ |
| Sensor Type    | Digital, Encoder                     |
| Connector      | JST-PH 6-pin                         |
| Mounting Holes | #10 Clearance                        |
| Accuracy       | Factory Calibrated to +/- 0.5 degree |
| Weight         | 23.0g (0.05lbs)                      |

## Electrical Specifications

<table data-header-hidden><thead><tr><th width="174">Parameter</th><th align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units </th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong> </td></tr><tr><td>Input Voltage</td><td align="center">3.3</td><td align="center">-</td><td align="center">5.0</td><td align="center">V</td></tr><tr><td>Logic Level </td><td align="center">-</td><td align="center">3.3</td><td align="center">5.0</td><td align="center">V</td></tr><tr><td>Maximum RPM</td><td align="center">-</td><td align="center">-</td><td align="center">10000</td><td align="center">RPM</td></tr></tbody></table>

### Incremental Output

| **Parameter**         | **Min** | **Typ** | **Max** |    **Units**    |
| --------------------- | :-----: | :-----: | :-----: | :-------------: |
| Quadrature Resolution |    -    |   2048  |    -    | Cycles per Rev. |
|                       |    -    |   8192  |    -    | Counts per Rev. |
| Index Pulse Frequency |    -    |    1    |    -    |  Pulse per Rev. |
| Index Pulse Width     |    -    |   0.04  |    -    |      Degree     |

### Absolute Pulse Output (Duty Cycle)

<table data-header-hidden><thead><tr><th width="221">Parameter</th><th align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units </th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong> </td></tr><tr><td>Period</td><td align="center">-</td><td align="center">1000</td><td align="center">-</td><td align="center">μs</td></tr><tr><td>Frequency</td><td align="center">-</td><td align="center">1</td><td align="center">-</td><td align="center">kHz</td></tr><tr><td>Minimum Pulse (0°)</td><td align="center">-</td><td align="center">3.884</td><td align="center">-</td><td align="center">μs</td></tr><tr><td>Maximum Pulse (360°)</td><td align="center">-</td><td align="center">998.06</td><td align="center">-</td><td align="center">μs</td></tr><tr><td>Pulse Resolution</td><td align="center">-</td><td align="center">12</td><td align="center">-</td><td align="center">bit</td></tr></tbody></table>

## Mechanical Drawings

<figure><img src="/files/lQwUfe4OTWhcyXKGXJ3S" alt=""><figcaption></figcaption></figure>

## Pinout

<figure><img src="/files/G2zL3ewzJq9D58pgqOqe" alt=""><figcaption></figcaption></figure>
