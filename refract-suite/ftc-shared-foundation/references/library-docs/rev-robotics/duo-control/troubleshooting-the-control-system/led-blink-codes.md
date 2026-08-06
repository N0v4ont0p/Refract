> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/led-blink-codes.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/led-blink-codes.md).

# Status LED Blink Codes

The RGB LED located on the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) near the RS485 ports and on the bottom of the Driver Hub ([REV-31-1956](#control-hub)) provide user feedback regarding the status of the Hub. Below is a Table of the Blink Codes.&#x20;

## Control Hub&#x20;

{% hint style="info" %}
All Control Hub Blink Codes assume the latest [Control Hub Operating System](/duo-control/managing-the-control-system/updating-operating-system.md) is running on the device
{% endhint %}

### Robot Controller Application 6.0 or Higher&#x20;

If a Control Hub is running Robot Controller Application 5.5 or lower the LED Blink Codes for the Hub will be the same as an [Expansion Hub running Firmware Version 1.7.0 or higher](/duo-control/troubleshooting-the-control-system/led-blink-codes.md#firmware-version-1-7-0-or-higher).&#x20;

<table data-header-hidden><thead><tr><th width="181">LED Status</th><th>LED Description</th><th>When</th><th>Hub Status</th></tr></thead><tbody><tr><td><strong>LED Status</strong></td><td><strong>LED Description</strong></td><td><strong>When</strong></td><td><strong>Hub Status</strong></td></tr><tr><td><img src="/files/-M8N18gTUs6f_i1L-cEQ" alt=""></td><td>Solid Blue</td><td>At Boot</td><td>Control Hub has power; Battery is >7V and is waiting to initialize communications.</td></tr><tr><td><img src="/files/-M8N18gUxP3oImsccuCM" alt=""></td><td>Solid Blue</td><td>Anytime</td><td><p>Hub is waiting for communication with the Driver Station Host.</p><p>Control Hub has power; Battery is >7V.</p></td></tr><tr><td><img src="/files/-MIz6EtgaDw3bcbe6ZKC" alt=""></td><td>Solid Green </td><td>Anytime</td><td>Hub has power and active communication with the Android Platform.</td></tr><tr><td><img src="/files/-M8N18gXhpjQ3WIQI9_M" alt=""></td><td>Blinking Blue</td><td>Anytime</td><td>Keep alive has timed out. Fault will clear when communication resumes.</td></tr><tr><td><img src="/files/-M8N18gYOL7YboxKfFeO" alt=""></td><td>Blinking Orange</td><td>Anytime</td><td><p>Battery Voltage is lower than 7V. Either the 12V battery needs to be charged, or the Expansion Hub is running on USB power only. This fault will clear when battery voltage is raised above 7V.</p><p>This will not be overwritten by the keep alive timeout pattern.</p></td></tr><tr><td><img src="/files/-MOhizyMHL9yNcExH3Wp" alt="" data-size="original"> </td><td>Blinking Magenta</td><td><a href="/pages/-M8N-OOVK_yoj-t3tsS8#changing-wifi-band">During Wi-Fi Reset</a></td><td>Control Hub changed Wi-Fi Band to 5GHz after pressing the button</td></tr><tr><td><img src="/files/-MOhj9MgOLMUtsvlUEbv" alt="" data-size="original"> </td><td>Blinking Yellow</td><td><a href="/pages/-MGj0B6AujUJikuEdUHj#changing-the-wifi-band-and-channel">During Wi-Fi Reset</a></td><td>Control Hub changed Wi-Fi Band to 2.4GHz after pressing the button</td></tr></tbody></table>

## Driver Hub

{% hint style="info" %}
All Driver Hub Blink Codes assume the latest [Driver Hub Software](/duo-control/managing-the-control-system/updating-the-driver-hub.md) is running on the device
{% endhint %}

#### LED A

<table><thead><tr><th width="246.62075134168157">LED Status</th><th width="252">LED Description</th><th width="242">Hub Status</th></tr></thead><tbody><tr><td><img src="/files/9KN8mWc6zCJvL2PI33hz" alt=""></td><td>Blinking White</td><td>Operating System is Booting</td></tr></tbody></table>

#### LED B

| LED Status                       | LED Description | Hub Status   |
| -------------------------------- | --------------- | ------------ |
| ![](/files/ZAYk0Yxx2J7YHVaW4SfW) | Solid Green     | Device is on |

#### Battery Status LED

| LED Status                       | LED Description | Hub Status       |
| -------------------------------- | --------------- | ---------------- |
| ![](/files/ogPbG23Slu3IgA4rPrAi) | Blinking Red    | Battery Charging |
| ![](/files/Wz2uK26nSqjZKqjwsJT9) | Solid Red       | Battery Charged  |

## Expansion Hub

### Firmware Version 1.7.0 or Higher&#x20;

| **LED Status**                   | **LED Description**                                                     | **When** | **Hub Status**                                                                                                                                                                                                                                                               |
| -------------------------------- | ----------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](/files/-M8N18gTUs6f_i1L-cEQ) | Solid Blue                                                              | At Boot  | Hub has power; Battery is >7V and is waiting to initialize communications.                                                                                                                                                                                                   |
| ![](/files/-M8N18gUxP3oImsccuCM) | Solid Blue                                                              | Anytime  | <p>Hub is waiting for communication with the Robot Controller.</p><p>Hub has power; Battery is >7V.</p>                                                                                                                                                                      |
| ![](/files/-M8N8UYa5t0kzRXp0G4I) | <p>Solid Green with one or more blue blinks every</p><p>\~5 Seconds</p> | Anytime  | <p>Hub has power and active communication with the Android Platform. The number of blue blinks is the same as the Expansion Hub’s address.</p><p>The factory default address is 2 (<img src="/files/-M8N18gWZ_ijZcjG3K9F" alt="">).</p>                                      |
| ![](/files/-M8N18gXhpjQ3WIQI9_M) | Blinking Blue                                                           | Anytime  | Keep alive has timed out. Fault will clear when communication resumes.                                                                                                                                                                                                       |
| ![](/files/-M8N18gYOL7YboxKfFeO) | Blinking Orange                                                         | Anytime  | <p>Battery Voltage is lower than 7V. Either the 12V battery needs to be charged, or the Expansion Hub is running on USB power only. This fault will clear when battery voltage is raised above 7V.</p><p>This will not be overwritten by the keep alive timeout pattern.</p> |
