> Source: https://docs.revrobotics.com/duo-build/ftc-starter-kit-mecanum-drivetrain.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/ftc-starter-kit-mecanum-drivetrain.md).

# Channel Drivetrain - Mecanum Upgrade

This section outlines the steps required to build a mecanum drivetrain using parts from the FTC Starter Kit V3.1 ([REV-45-3529](https://www.revrobotics.com/rev-45-3529/)), the 75mm Mecanum Wheel Set ([REV-45-1655](https://www.revrobotics.com/rev-45-1655/)), and two additional UltraPlanetary Gearbox Kit & HD Hex Motors ([REV-41-1600](https://www.revrobotics.com/rev-41-1600/)).&#x20;

REV also offers a Mecanum Drivetrain Kit V2 ([REV-45-2470](https://www.revrobotics.com/rev-45-2470/)) which contains the parts needed to build this drivetrain using Belts and Pulleys to transmit motion from the motors to wheels, rather than Chain and Sprockets.

This design is a good starting point. However, modification maybe required to address the specific needs of the robot being designed.&#x20;

The assembly of this drivetrain is broken into a few sections. This allows for a team of people to work on different tasks to complete the build quicker. Each section begins with what parts and the quantity of parts needed to complete the steps in that section. A list of required materials for all sections is listed below.

|                                            Full Assembly CAD File - STEP Format                                            |
| :------------------------------------------------------------------------------------------------------------------------: |
| [Starter Kit Mecanum Drivetrain](https://store-t3eo8vwp22.mybigcommerce.com/content/cad/Starter_Kit_Mecanum_Assembly.STEP) |

![](/files/-MG9xCmHMs7lOaWz8hsH)

### Video Build Guide

{% embed url="<https://www.youtube.com/playlist?list=PLFAaHLNVWKvyuNWeYdRc1epoX7UQ81NKl>" %}

### Kit Options

The Channel Drivetrain - Mecanum Upgrade is intended as an upgrade to the FTC Starter Kit V3. This drivetrain can be built out of the following kits:

#### FTC Starter Kit Base

| Part Number                                             | Description                                | QTY. |
| ------------------------------------------------------- | ------------------------------------------ | ---- |
| [REV-45-3529](https://www.revrobotics.com/rev-45-3529/) | FTC Starter Kit V3.1                       | 1    |
| [REV-45-1655](https://www.revrobotics.com/rev-45-1655/) | 75mm Mecanum Wheel Set                     | 1    |
| [REV-41-1600](https://www.revrobotics.com/rev-41-1600/) | UltraPlanetary Gearbox Kit & HD Hex Motors | 2    |

#### Mecanum Drivetrain Kit Base

When using the Mecanum Drivetrain Kit, REV recommends building the [Mecanum Drivetrain Kit](/duo-build/mecanum-drivetrain-kit-mecanum-drivetrain.md) chassis as all the need parts are included with the kit. If you are looking to build this drivetrain you will need the following:

| Part Number                                             | Description              | QTY. |
| ------------------------------------------------------- | ------------------------ | ---- |
| [REV-45-1877](https://www.revrobotics.com/rev-45-1877/) | Mecanum Drivetrain Kit   | 1    |
| [REV-41-1338](https://www.revrobotics.com/rev-41-1338/) | 10 TOOTH #25 SPROCKET    | 4    |
| [REV-41-1365](https://www.revrobotics.com/rev-41-1365/) | #25 ROLLER CHAIN - 10 FT | 1    |
| [REV-41-1442](https://www.revrobotics.com/rev-41-1442/) | #25 CHAIN TOOL           | 1    |

### Full Bill of Materials

| **PART NUMBER**                                         | **DESCRIPTION**                           | **QTY.** |
| ------------------------------------------------------- | ----------------------------------------- | -------- |
| [REV-41-1762](https://www.revrobotics.com/rev-41-1762/) | 45MM X 15MM C CHANNEL - 408MM             | 4        |
| [REV-41-1767](https://www.revrobotics.com/rev-41-1767/) | 45MM X 15MM C CHANNEL - 248MM             | 1        |
| [REV-41-1687](https://www.revrobotics.com/rev-41-1687/) | U CHANNEL ENDCAP                          | 4        |
| [REV-41-1432](https://www.revrobotics.com/rev-41-1432/) | 15MM EXTRUSION - 420MM                    | 2        |
| [REV-41-1347](https://www.revrobotics.com/rev-41-1347/) | 5MM X 75MM HEX SHAFT                      | 2        |
| [REV-41-1348](https://www.revrobotics.com/rev-41-1348/) | 5MM X 90MM HEX SHAFT                      | 4        |
| [REV-41-1324](https://www.revrobotics.com/rev-41-1324/) | 3MM SPACER                                | 16       |
| [REV-41-1323](https://www.revrobotics.com/rev-41-1323/) | 15MM SPACER                               | 8        |
| [REV-41-1326](https://www.revrobotics.com/rev-41-1326/) | THROUGH BORE BEARING - SHORT              | 12       |
| [REV-41-1329](https://www.revrobotics.com/rev-41-1329/) | THROUGH BORE BEARING - LONG               | 4        |
| [REV-41-1338](https://www.revrobotics.com/rev-41-1338/) | 10 TOOTH #25 SPROCKET\*                   | 4        |
| [REV-41-1365](https://www.revrobotics.com/rev-41-1365/) | #25 ROLLER CHAIN - 10 FT\*                | 1        |
| [REV-41-1492](https://www.revrobotics.com/rev-41-1492/) | M3 STANDOFF - 40MM                        | 4        |
| [REV-41-1702](https://www.revrobotics.com/rev-41-1702/) | TENSIONING BUSHING - 39MM                 | 4        |
| [REV-41-1327](https://www.revrobotics.com/rev-41-1327/) | SHAFT COLLAR                              | 8        |
| [REV-41-1600](https://www.revrobotics.com/rev-41-1600/) | ULTRAPLANETARY GEARBOX KIT & HD HEX MOTOR | 4        |
| [REV-41-1621](https://www.revrobotics.com/rev-41-1621/) | ULTRAPLANETARY OUTSIDE MOUNTING BRACKET   | 4        |
| [REV-41-1305](https://www.revrobotics.com/rev-41-1305/) | 15MM PLASTIC 90 DEGREE BRACKET            | 12       |
| [REV-45-1655](https://www.revrobotics.com/rev-45-1655/) | 75MM MECANUM WHEEL SET                    | 1        |
| [REV-41-1359](https://www.revrobotics.com/rev-41-1359/) | M3 X 8MM HEX CAP SCREWS - 100 PACK        | 2        |
| [REV-41-1361](https://www.revrobotics.com/rev-41-1361/) | M3 NYLOC NUTS - 100 PACK                  | 1        |
