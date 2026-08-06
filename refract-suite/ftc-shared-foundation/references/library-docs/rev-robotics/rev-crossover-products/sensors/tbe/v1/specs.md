> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/tbe/v1/specs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/tbe/v1/specs.md).

# Specifications

## General Specifications

| **Parameter**  | **Value and Units** |
| -------------- | ------------------- |
| Sensor Type    | Digital, Encoder    |
| Connector      | JST-PH 6-pin        |
| Mounting Holes | #10 Clearance       |

## Electrical Specifications

<table data-header-hidden><thead><tr><th width="174">Parameter</th><th align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units </th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong> </td></tr><tr><td>Input Voltage</td><td align="center">3.3</td><td align="center">-</td><td align="center">5.0</td><td align="center">V</td></tr><tr><td>Logic Level </td><td align="center">-</td><td align="center">3.3</td><td align="center">5.0</td><td align="center">V</td></tr><tr><td>Maximum RPM</td><td align="center">-</td><td align="center">-</td><td align="center">10000</td><td align="center">RPM</td></tr></tbody></table>

### Incremental Output

| **Parameter**         | **Min** | **Typ** | **Max** |    **Units**    |
| --------------------- | :-----: | :-----: | :-----: | :-------------: |
| Quadrature Resolution |    -    |   2048  |    -    | Cycles per Rev. |
|                       |    -    |   8192  |    -    | Counts per Rev. |
| Index Pulse Frequency |    -    |    1    |    -    |  Pulse per Rev. |
| Index Pulse Width     |    -    |    90   |    -    |        °e       |

### Absolute Pulse Output (Duty Cycle)

<table data-header-hidden><thead><tr><th width="221">Parameter</th><th align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units </th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong> </td></tr><tr><td>Period</td><td align="center">-</td><td align="center">1025</td><td align="center">-</td><td align="center">μs</td></tr><tr><td>Frequency</td><td align="center">-</td><td align="center">975.6</td><td align="center">-</td><td align="center">Hz</td></tr><tr><td>Minimum Pulse (0°)</td><td align="center">-</td><td align="center">1</td><td align="center">-</td><td align="center">μs</td></tr><tr><td>Maximum Pulse (360°)</td><td align="center">-</td><td align="center">1024</td><td align="center">-</td><td align="center">μs</td></tr><tr><td>Pulse Resolution</td><td align="center">-</td><td align="center">10</td><td align="center">-</td><td align="center">bit</td></tr></tbody></table>

## Mechanical Drawings

<figure><img src="/files/bXeesVcwwC9tP5iJtZ54" alt=""><figcaption></figcaption></figure>

## Pinout

<figure><img src="/files/G2zL3ewzJq9D58pgqOqe" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
With the switch in the S position, the SSI pins on the AEAT-8800 Magnetic Encoder are exposed on the 6-pin JST PH connector instead of the quadrature and absolute signals (A, B, I, Abs.). Details about the SSI protocol for the sensor can be found in the [AEAT-8800 datasheet](http://docs.broadcom.com/docs/pub-005892)
{% endhint %}
