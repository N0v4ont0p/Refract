> Source: https://docs.revrobotics.com/duo-control/sensors/encoders/motor-based-encoders.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/encoders/motor-based-encoders.md).

# REV Motor Encoders

‌REV Robotics HD Hex Motors ([REV-41-1291](https://www.revrobotics.com/rev-41-1301/)) and the Core Hex Motors ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) come with a magnetic quadrature encoder already installed and an appropriate cable for connecting the encoder output to the REV Robotics Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) or Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)). See Table 1 and Table 2 for relevant encoder details.‌&#x20;

### Core Hex Motor (REV-41-1300) Encoder Specifications

| **Core Hex Motor (REV-41-1300) Reduction**   | 72:1                        |
| -------------------------------------------- | --------------------------- |
| **Free Speed (RPM)**                         | 125                         |
| **Cycles per Rotation of the Encoder Shaft** | 4 (1 Rise of Channel A)     |
| **Counts per Rotation of the Output Shaft**  | 288 (72 Rises of Channel A) |

#### Pinout

The Core Hex Motor uses a 2-pin JST-VH Connector for motor power and a 4-pin JST-PH for sensor feedback from the built-in encoder. For more information on using the cables and connectors included with the Core Hex Motor, see the [REV Control System - Cable and Connectors documentation](https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors). The image below has the pinout for the motor power and the encoder.

<figure><img src="/files/GptNQMC5XgquKgdXrXze" alt=""><figcaption></figcaption></figure>

### ‌HD Hex Motor (REV-41-1291) Encoder Specifications

| **HD Hex Motor Reduction**                   | Bare Motor                | 40:1                          | 20:1                         |
| -------------------------------------------- | ------------------------- | ----------------------------- | ---------------------------- |
| **Free Speed (RPM)**                         | 6000                      | 150                           | 300                          |
| **Cycles per Rotation of the Encoder Shaft** | 28 (7 Rises of Channel A) | 28 (7 Rises of Channel A)     | 28 (7 Rises of Channel A)    |
| **Counts per Rotation of the Output Shaft**  | 28 (7 Rises of Channel A) | 1120 (280 Rises of Channel A) | 560 (140 Rises of Channel A) |

#### Pinout

The HD Hex Motor uses a 2-pin JST-VH Connector for motor power and a 4-pin JST-PH for sensor feedback from the built-in encoder. For more information on using the cables and connectors included with the HD Hex Motor, see the [REV Control System - Cable and Connectors documentation](https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors). The image below has the pinout for the motor power and the encoder.

<figure><img src="/files/GptNQMC5XgquKgdXrXze" alt=""><figcaption></figcaption></figure>
