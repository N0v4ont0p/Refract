> Source: https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics.md).

# Control Hub Specifications

The REV Robotics Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) is an affordable all in one educational robotics controller that provides the interfaces required for building robots, as well as other mechatronics, with multiple programming language options. The Control Hub was designed and built as an easy to use, dependable, and durable device for use in classroom and the competition. It features an Android operating system, built-in dual band Wi-Fi (802.11 ac/b/g/n/w), and a mature software package designed for both basic and advanced use cases. When the Control Hub software is updated with new features, the controller can receive a "field upgrade," through an update process that is fast and simple.&#x20;

The Control Hub is an approved device for use in FIRST® Global and FIRST Tech Challenge.

![](/files/-M7xwqJwuFVOnDDc6Tu2)

<table data-header-hidden><thead><tr><th>Port Label</th><th width="133" align="center">Qty</th><th align="center">Connector</th><th>Description</th></tr></thead><tbody><tr><td><strong>Port Label</strong></td><td align="center"><strong>Qty</strong></td><td align="center"><strong>Connector</strong></td><td>Description</td></tr><tr><td>Battery</td><td align="center">2</td><td align="center"><a href="/pages/-M7x8SnkDLzg7OEDjJnB">XT-30</a></td><td>Connect one 12V NiMh battery, add an Expansion Hub with second port</td></tr><tr><td>Motor</td><td align="center">4</td><td align="center"><a href="/pages/-M7x8XPRiSZR3VbXBSOF">JST VH, 2-pin</a></td><td>Motor power output</td></tr><tr><td>Encoder</td><td align="center">4</td><td align="center"><a href="/pages/-M7x8XiR_srXQksyoL62">JST PH, 4-pin</a></td><td>Quadrature encoder input</td></tr><tr><td>Servo</td><td align="center">6</td><td align="center">0.1” Header</td><td>Extended range 5V servo output</td></tr><tr><td>+5V Power</td><td align="center">2</td><td align="center">0.1” Header</td><td>Power for auxiliary device(s)</td></tr><tr><td>Analog</td><td align="center">4</td><td align="center"><a href="/pages/-M7x8XiR_srXQksyoL62">JST PH, 4-pin</a></td><td>Analog input with two channels per connector.</td></tr><tr><td>Digital</td><td align="center">8</td><td align="center"><a href="/pages/-M7x8XiR_srXQksyoL62">JST PH, 4-pin</a></td><td>Digital Input/Output with two channels per connector</td></tr><tr><td>I2C</td><td align="center">4</td><td align="center"><a href="/pages/-M7x8XiR_srXQksyoL62">JST PH, 4-pin</a></td><td>Four separate I2C busses</td></tr><tr><td>RS485</td><td align="center">2</td><td align="center"><a href="/pages/-M7x8XiR_srXQksyoL62">JST PH, 3-pin</a></td><td>Use this serial communication port to add an Expansion Hub</td></tr><tr><td>UART</td><td align="center">2</td><td align="center"><a href="/pages/-M7x8XiR_srXQksyoL62">JST PH, 3-pin</a></td><td>Debugging only</td></tr><tr><td>USB C</td><td align="center">1</td><td align="center">USB C</td><td>Connect directly to the Control Hub via PC, USB 2.0</td></tr><tr><td>USB 2.0</td><td align="center">1</td><td align="center">USB A</td><td>Connect USB cameras and other USB peripherals to the Control Hub</td></tr><tr><td>USB 3.0</td><td align="center">1</td><td align="center">USB A</td><td>Connect USB cameras and other USB peripherals to the Control Hub</td></tr><tr><td>HDMI</td><td align="center">1</td><td align="center">HDMI A</td><td>Supports 4k @ 60Hz</td></tr></tbody></table>

## Specifications

The following tables provide the operating and mechanical specifications for the Control Hub.

### General Specifications

| Feature type | Description                                                                     |
| ------------ | ------------------------------------------------------------------------------- |
| Processor(s) | <p>RK3328 Quad-core ARM® Cortex-A53</p><p>Texas Instruments ARM® Cortex®-M4</p> |
| Memory       | 1GB LPDDR3                                                                      |
| Storage†     | 8GB eMMC 4.51                                                                   |
| Wireless     | <p>802.11 ac/b/g/n/w Wi-Fi; Dual Band 2.4 & 5 GHz</p><p>Bluetooth 4.1</p>       |
| Graphics‡    | <p>GPU - ARM® Mali 450MP4</p><p>HDMI 2.0 support for 4k @ 60Hz</p>              |

|   |                                                                  |
| - | ---------------------------------------------------------------- |
| † | Supports expandable storage through the SD Card slot             |
| ‡ | Display graphics supported through an external display over HDMI |

{% hint style="danger" %}
DO NOT exceed the absolute maximum electrical specifications. Doing so will cause permanent damage to the Control Hub and will void the warranty.
{% endhint %}

### Input Power Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="133" align="center">Min</th><th width="111" align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Operating voltage range (<span class="math">V_{IN}</span>)</td><td align="center">8</td><td align="center">12</td><td align="center">15</td><td align="center">V</td></tr><tr><td>Absolute maximum supply voltage</td><td align="center">-</td><td align="center">-</td><td align="center">15</td><td align="center">V</td></tr></tbody></table>

### Motor Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="157" align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Continuous output current †</td><td align="center">-</td><td align="center">-</td><td align="center">10</td><td align="center">A</td></tr><tr><td>Absolute maximum output current ‡</td><td align="center">-</td><td align="center">-</td><td align="center">20</td><td align="center">A</td></tr></tbody></table>

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| † | Exceeding the continuous current maximum depends on many thermal factors. The outputs will self protect once they approach their thermal limit. |
| ‡ | Maximum current is ultimately limited by the in-line battery fuse.                                                                              |

### Encoder Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="139">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Encoder port input voltage</td><td>0</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Encoder port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Encoder port total supply current</td><td>-</td><td>-</td><td>500</td><td>mA</td></tr></tbody></table>

{% hint style="info" %}
See [Sensors - Encoders](/duo-control/sensors/encoders.md) for more information on encoders and using the encoder ports. For using non-REV motor encoders see [Using 5V Sensors - Encoders](/duo-control/sensors/5v-sensors.md) for more details.
{% endhint %}

### Digital Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="123">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Digital port input voltage</td><td>0</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Digital port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Digital port total supply current</td><td>-</td><td>-</td><td>1</td><td>A</td></tr></tbody></table>

{% hint style="info" %}
See [Sensors - Digital](/duo-control/sensors/digital.md) for more information on using the digital ports. See [Using 5V Sensors](/duo-control/sensors/5v-sensors.md) for information on using 5V logic level devices with the digital ports.
{% endhint %}

### Analog Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="173">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Analog port input voltage range †</td><td>0</td><td>-</td><td>5</td><td>V</td></tr><tr><td>Analog port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Analog port total supply current </td><td>-</td><td>-</td><td>500</td><td>mA</td></tr></tbody></table>

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| † | The analog input will accept up to 5V. When using 5V analog sensors, a custom wiring harness is needed to provide 5V of power for the sensor as the power pin provides 3.3V. |

{% hint style="info" %}
See [Sensors - Analog](/duo-control/sensors/analog.md) for more information on using the analog ports.
{% endhint %}

### I2C Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="136">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>I2C port input voltage range</td><td>0</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>I2C port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>I2C port total supply current</td><td>-</td><td>-</td><td>500</td><td>mA</td></tr><tr><td>Bus speed</td><td>-</td><td>100/400</td><td>-</td><td>kHz</td></tr></tbody></table>

{% hint style="info" %}
See [Sensors - I2C](/duo-control/sensors/i2c.md) for more information on using the I2C ports. See [Using 5V Sensors](/duo-control/sensors/5v-sensors.md) for information on using 5V logic level devices with the I2C ports.
{% endhint %}

### Servo Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="150">Min</th><th align="center">Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Servo output signal voltage</td><td>0</td><td align="center">-</td><td>5</td><td>V</td></tr><tr><td>Servo port supply voltage</td><td>-</td><td align="center">5</td><td>-</td><td>V</td></tr><tr><td>Servo port pair total supply current †</td><td>-</td><td align="center">-</td><td>2</td><td>A</td></tr><tr><td>Absolute maximum total supply current ‡</td><td>-</td><td align="center">-</td><td>5</td><td>A</td></tr><tr><td>Servo port output pulse range</td><td>500</td><td align="center">-</td><td>2500</td><td>μs</td></tr></tbody></table>

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
| † | Total supply is shared across pairs of ports (0-1, 2-3, 4-5)                   |
| ‡ | The 5A total supply current for all servo ports and +5V power ports is shared. |

### +5V Power Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="136">Min</th><th align="center">Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>+5V power port output voltage</td><td>-</td><td align="center">5</td><td>-</td><td>V</td></tr><tr><td>+5V power port pair total supply current †</td><td>-</td><td align="center">-</td><td>2</td><td>A</td></tr><tr><td>Absolute maximum total supply current ‡</td><td>-</td><td align="center">-</td><td>5</td><td>A</td></tr></tbody></table>

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
| † | Total supply current is shared across both ports                               |
| ‡ | The 5A total supply current for all servo ports and +5V power ports is shared. |

### Mechanical Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="131" align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Body length</td><td align="center">-</td><td align="center">103</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Body width</td><td align="center">-</td><td align="center">143</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Body height</td><td align="center">-</td><td align="center">29.5</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Weight</td><td align="center">-</td><td align="center">209</td><td align="center">-</td><td align="center">g</td></tr><tr><td>Mounting hole pitch</td><td align="center">-</td><td align="center">16</td><td align="center">-</td><td align="center">mm</td></tr></tbody></table>
