> Source: https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications.md).

# Driver Hub Specifications

The REV Robotics Driver Hub ([REV-31-1596](https://docs.revrobotics.com/duo-control/control-system-overview/www.revrobotics.com/rev-31-1596)) is a compact mobile computing device designed for interfacing with the Control Hub (REV-31-1595). The Driver Hub was designed and built as an easy to use, dependable, and durable device for use in classroom and the competition. It features an Android operating system, built-in dual band Wi-Fi (802.11 ac/b/g/n/w), and support for many off-the-shelf gamepads and HID devices connected through built-in USB ports. When the Driver Hub software is updated with new features, the device can receive a "field upgrade," through a fast and simple update through the [REV Hardware Client](/duo-control/managing-the-control-system/rev-hardware-client.md).&#x20;

The Driver Hub is an approved device for use in FIRST® Global and FIRST Tech Challenge.&#x20;

![](/files/-Ma4Bemcm0_JOuf0gCK7)

<table data-header-hidden><thead><tr><th>Label</th><th width="151" align="center">Qty</th><th align="center">Interface</th><th>Description</th></tr></thead><tbody><tr><td><strong>Label</strong></td><td align="center"><strong>Qty</strong></td><td align="center"><strong>Interface</strong></td><td><strong>Description</strong></td></tr><tr><td>Power</td><td align="center">1</td><td align="center">Button</td><td>Turns the device on and off</td></tr><tr><td>USB C</td><td align="center">1</td><td align="center">USB C</td><td><p>Connect directly to the Driver Hub via PC, USB 2.0</p><p>Supports fast charging the Driver Hub over USB PD</p></td></tr><tr><td>USB 2.0</td><td align="center">3</td><td align="center">USB A</td><td>Connect USB controllers and other HID devices to the Driver Hub</td></tr><tr><td>Ethernet</td><td align="center">1</td><td align="center">RJ45</td><td>10/100 base-T<br>Supports 12V DC passive POE</td></tr></tbody></table>

## Specifications

The following tables provide the mechanical specifications for the Driver Hub.

### General Specifications

| Feature type | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| Processor    | RKPX30 Quad-core ARM A35                                                  |
| Memory       | 1GB LPDDR3                                                                |
| Storage†     | 8GB eMMC 4.51                                                             |
| Wireless     | <p>802.11 ac/b/g/n/w Wi-Fi; Dual Band 2.4 & 5 GHz</p><p>Bluetooth 4.1</p> |
| Graphics     | ARM® Mali 450MP4                                                          |

|   |                                                      |
| - | ---------------------------------------------------- |
| † | Supports expandable storage through the SD Card slot |

### Mechanical Specifications

<table data-header-hidden><thead><tr><th>Parameter</th><th width="140" align="center">Min</th><th align="center">Typ</th><th align="center">Max</th><th align="center">Units</th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td align="center"><strong>Min</strong></td><td align="center"><strong>Typ</strong></td><td align="center"><strong>Max</strong></td><td align="center"><strong>Units</strong></td></tr><tr><td>Body length</td><td align="center">-</td><td align="center">3.375</td><td align="center">-</td><td align="center">in</td></tr><tr><td>Body width</td><td align="center">-</td><td align="center">5.25</td><td align="center">-</td><td align="center">in</td></tr><tr><td>Body height</td><td align="center">-</td><td align="center">1.0</td><td align="center">-</td><td align="center">in</td></tr><tr><td>Weight</td><td align="center">-</td><td align="center">9.8</td><td align="center">-</td><td align="center">oz</td></tr><tr><td>Mounting hole pitch</td><td align="center">-</td><td align="center">16</td><td align="center">-</td><td align="center">mm</td></tr><tr><td>Screen size (diagonal)</td><td align="center"></td><td align="center">5</td><td align="center"></td><td align="center">in</td></tr><tr><td>Screen resolution</td><td align="center"></td><td align="center">800 x 600</td><td align="center"></td><td align="center">px</td></tr></tbody></table>

### Charger Specifications

Please refer to the following guidelines in the event the Driver Hub charger must be replaced:

| Charging Type                           | Wattage      |
| --------------------------------------- | ------------ |
| Standard USB charger (original charger) | 10W (5V, 2A) |
| USB PD Charger                          | At least 15W |
