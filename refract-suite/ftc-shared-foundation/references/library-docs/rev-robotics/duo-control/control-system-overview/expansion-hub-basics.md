> Source: https://docs.revrobotics.com/duo-control/control-system-overview/expansion-hub-basics.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/control-system-overview/expansion-hub-basics.md).

# Expansion Hub Specifications

The REV Robotics Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) is a low-cost educational device that can communicate with any computer (commonly the [REV Robotics Control Hub](/duo-control/control-system-overview/control-hub-basics.md) or an Android Phone) to provide the interfaces required for building robots and other mechatronics. The Expansion Hub was purpose built to stand up to the rigors of the classroom and competition field. It features a mature firmware designed for basic and advanced use cases with the ability to be field upgraded in the future. &#x20;

The IO ports of the Expansion Hub are identical in specification to the Control Hub. Within this documentation, many sections may refer to the Control Hub, but the connections are the same for the Expansion Hub.

The REV Robotics Expansion Hub is an approved device for use in the FIRST Tech Challenge and FIRST Global.

![](/files/-M8MS9GTmSyQytKMtbo8)

<table data-header-hidden><thead><tr><th>Port Label</th><th width="144" align="center">Qty</th><th align="center">Connector</th><th>Description</th></tr></thead><tbody><tr><td><strong>Port Label</strong></td><td align="center"><strong>Qty</strong></td><td align="center"><strong>Connector</strong></td><td><strong>Description</strong></td></tr><tr><td>Battery</td><td align="center">2</td><td align="center">XT30</td><td>Connect one 12V NiMh battery, add an Expansion Hub with second port</td></tr><tr><td>Motor</td><td align="center">4</td><td align="center">JST VH, 2-pin</td><td>Motor power output</td></tr><tr><td>Encoder</td><td align="center">4</td><td align="center">JST PH, 4-pin</td><td>Quadrature encoder input</td></tr><tr><td>Servo</td><td align="center">6</td><td align="center">0.1” Header</td><td>Extended range 5V servo output (500-2500ms)</td></tr><tr><td>5V Aux Power</td><td align="center">2</td><td align="center">0.1” Header</td><td>Auxiliary device 5V/2A</td></tr><tr><td>Analog</td><td align="center">4</td><td align="center">JST PH, 4-pin</td><td>Analog input 0-5.0V measurement range with two channels per connector. 3.3V provided on the connector power pin.</td></tr><tr><td>Digital</td><td align="center">8</td><td align="center">JST PH, 4-pin</td><td>Digital Input/Output with two channels per connector</td></tr><tr><td>I2C</td><td align="center">4</td><td align="center">JST PH, 4-pin</td><td>Four separate I2C busses, 100kHz/400kHz bus speed</td></tr><tr><td>RS485</td><td align="center">2</td><td align="center">JST PH, 3-pin</td><td>Serial communication port to add a Hub (Control or Expansion)</td></tr><tr><td>UART</td><td align="center">2</td><td align="center">JST PH, 3-pin</td><td>Debugging only</td></tr><tr><td>MINI USB</td><td align="center">1</td><td align="center">USB Mini-B</td><td>Connect directly to the Robot Controller Android device or PC</td></tr></tbody></table>

## Specifications

The following tables provide the operating and mechanical specifications for the Expansion Hub.

{% hint style="danger" %}
DO NOT exceed the absolute maximum electrical specifications. Doing so will cause permanent damage to the Expansion Hub and will void the warranty.
{% endhint %}

### Input Power Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="153" align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Operating voltage range (<span class="math">V_{IN}</span>)</td><td align="center">8</td><td align="center">12</td><td align="center">15</td><td align="center">V</td></tr><tr><td>Absolute maximum supply voltage</td><td align="center">-</td><td align="center">-</td><td align="center">15</td><td align="center">V</td></tr></tbody></table>

### Motor Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="133" align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Continuous output current †</td><td align="center">-</td><td align="center">-</td><td align="center">10</td><td align="center">A</td></tr><tr><td>Absolute maximum output current ‡</td><td align="center">-</td><td align="center">-</td><td align="center">20</td><td align="center">A</td></tr></tbody></table>

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| † | Exceeding the continuous current maximum depends on many thermal factors. The outputs will self protect once they approach their thermal limit. |
| ‡ | Maximum current is ultimately limited by the in-line battery fuse.                                                                              |

### Encoder Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="159">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Encoder port input voltage</td><td>0</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Encoder port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Encoder port total supply current</td><td>-</td><td>-</td><td>500</td><td>mA</td></tr></tbody></table>

{% hint style="info" %}
See [Sensors - Encoders](/duo-control/sensors/encoders.md) for more information on encoders and using the encoder ports. For using non-REV motor encoders see [Using 3rd Party Sensors - Encoders](/duo-control/sensors/5v-sensors.md#connecting-5v-encoder) for more details.
{% endhint %}

### Digital Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="139">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Digital port input voltage</td><td>0</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Digital port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Digital port total supply current</td><td>-</td><td>-</td><td>1</td><td>A</td></tr></tbody></table>

{% hint style="info" %}
See [Sensors - Digital](/duo-control/sensors/digital.md) for more information on using the digital ports. See [Using 5V Sensors](/duo-control/sensors/5v-sensors.md) for information on using 5V logic level devices with the digital ports.
{% endhint %}

### Analog Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="141">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Analog port input voltage range †</td><td>0</td><td>-</td><td>5</td><td>V</td></tr><tr><td>Analog port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>Analog port total supply current </td><td>-</td><td>-</td><td>500</td><td>mA</td></tr></tbody></table>

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| † | The analog input will accept up to 5V. When using 5V analog sensors, a custom wiring harness is needed to provide 5V of power for the sensor as the power pin provides 3.3V. |

{% hint style="info" %}
See [Sensors - Analog](/duo-control/sensors/analog.md) for more information on using the analog ports.
{% endhint %}

### I2C Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="137">Min</th><th>Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>I2C port input voltage range</td><td>0</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>I2C port supply voltage</td><td>-</td><td>-</td><td>3.3</td><td>V</td></tr><tr><td>I2C port total supply current</td><td>-</td><td>-</td><td>500</td><td>mA</td></tr><tr><td>Bus speed</td><td>-</td><td>100/400</td><td>-</td><td>kHz</td></tr><tr><td>I2C pull-up resistor</td><td>-</td><td>2.49</td><td>-</td><td>kΩ</td></tr></tbody></table>

{% hint style="info" %}
**Expansion Hubs purchased AFTER December 2021 no longer include an internal IMU**
{% endhint %}

{% hint style="info" %}
See [Sensors - I2C](/duo-control/sensors/i2c.md) for more information on using the I2C ports. See [Using 5V Sensors](/duo-control/sensors/5v-sensors.md) for information on using 5V logic level devices with the I2C ports.
{% endhint %}

### Servo Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="132">Min</th><th align="center">Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>Servo output signal voltage</td><td>0</td><td align="center">-</td><td>5</td><td>V</td></tr><tr><td>Servo port supply voltage</td><td>-</td><td align="center">5</td><td>-</td><td>V</td></tr><tr><td>Servo port pair total supply current †</td><td>-</td><td align="center">-</td><td>2</td><td>A</td></tr><tr><td>Absolute maximum total supply current ‡</td><td>-</td><td align="center">-</td><td>5</td><td>A</td></tr><tr><td>Servo port output pulse range</td><td>500</td><td align="center">-</td><td>2500</td><td>μs</td></tr></tbody></table>

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
| † | Total supply is shared across pairs of ports (0-1, 2-3, 4-5)                   |
| ‡ | The 5A total supply current for all servo ports and +5V power ports is shared. |

### +5V Power Port Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="142">Min</th><th align="center">Typ</th><th>Max</th><th>Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td><strong>Max</strong></td><td><strong>Units</strong></td></tr><tr><td>+5V power port output voltage</td><td>-</td><td align="center">5</td><td>-</td><td>V</td></tr><tr><td>+5V power port pair total supply current †</td><td>-</td><td align="center">-</td><td>2</td><td>A</td></tr><tr><td>Absolute maximum total supply current ‡</td><td>-</td><td align="center">-</td><td>5</td><td>A</td></tr></tbody></table>

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
| † | Total supply current is shared across both ports                               |
| ‡ | The 5A total supply current for all servo ports and +5V power ports is shared. |

### Mechanical Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="134" align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Body length</td><td align="center">-</td><td align="center">103</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Body width</td><td align="center">-</td><td align="center">143</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Body height</td><td align="center">-</td><td align="center">29.5</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Weight</td><td align="center">-</td><td align="center">209</td><td align="center">-</td><td align="center">g</td></tr><tr><td>Mounting hole pitch</td><td align="center">-</td><td align="center">16</td><td align="center">-</td><td align="center">mm</td></tr></tbody></table>
