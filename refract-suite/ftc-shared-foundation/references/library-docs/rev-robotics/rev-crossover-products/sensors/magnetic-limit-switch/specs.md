> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/magnetic-limit-switch/specs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/magnetic-limit-switch/specs.md).

# Specifications

## Specifications&#x20;

### General Specifications&#x20;

| **Parameter**        | **Value and Units**            |
| -------------------- | ------------------------------ |
| Sensor Type          | Digital, Active-low            |
| Sensor Configuration | Normally Open (N.O.)           |
| Signal               | n & n+1                        |
| Magnetic Polarity    | Omnipolar (both north & south) |

### Electrical Specifications

<table data-header-hidden><thead><tr><th width="295">Parameter</th><th width="121" align="center">Min</th><th width="105" align="center">Typ</th><th width="122" align="center">Max</th><th align="center">Units </th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong> </td></tr><tr><td>Operating Voltage Range ( <span class="math">V_{IN}</span> )</td><td align="center">3.3</td><td align="center">-</td><td align="center">5.0</td><td align="center">V</td></tr><tr><td>Top Trigger Distance †</td><td align="center">-</td><td align="center">10</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Side Trigger Distance †</td><td align="center">-</td><td align="center">5</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Hysteresis</td><td align="center">-</td><td align="center">5</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Included Magnet Strength </td><td align="center">-</td><td align="center">4300</td><td align="center">-</td><td align="center">G</td></tr></tbody></table>

| † | Using the included magnet |
| - | ------------------------- |

## Mechanical Drawings

### Magnetic Limit Switch

{% hint style="info" %}
All dimensions are in millimeters
{% endhint %}

<figure><img src="/files/YBG6sVxTLoIC3OdjKYWj" alt=""><figcaption></figcaption></figure>

### Mountable Magnet&#x20;

{% hint style="info" %}
All dimensions are in millimeters
{% endhint %}

<figure><img src="/files/rOj6xzLuxMfJA7zb7nuI" alt=""><figcaption></figcaption></figure>

## Pinout and Schematic&#x20;

The Magnetic Limit Switch can send signal from either the **n+1** or **n** ports.

<figure><img src="/files/q0tu4KVZmQZKixOjGHfm" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This schematic illustrates that the Magnetic Limit Switch is NO "Normally Open".&#x20;
{% endhint %}
