> Source: https://docs.revrobotics.com/duo-build/mecanum-drivetrain-v2.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/mecanum-drivetrain-v2.md).

# Mecanum Drivetrain V2

This section outlines the steps required to build a mecanum drivetrain using the Mecanum Drivetrain Kit V2 ([REV-45-2470](https://www.revrobotics.com/rev-45-2470/)). The Mecanum Drivetrain Kit V2 uses UltraPlanetary Gearboxes and Ultra 90 Degree Gearboxes for a direct drive rather than one driven with belts or chain. For instructions on how to build a mecanum drivetrain with belts and pulleys check out the [Mecanum Drivetrain Kit](/duo-build/mecanum-drivetrain-kit-mecanum-drivetrain.md) or for a mecanum drivetrain with sprockets and chain see the [Channel Drivetrain - Mecanum Upgrade](/duo-build/ftc-starter-kit-mecanum-drivetrain.md).&#x20;

This design is a great starting point. However, modification may be required to address the specific needs of the robot being designed.&#x20;

The assembly of this drivetrain can be broken into a few sections. This allows for a team of people to work on different tasks to complete the build quicker. Each Section Begins with what parts and the quantity of parts needed to complete the steps in that section. A list of all required materials for the drivetrain is listed below.

|                                                                                     Full Onshape Assembly                                                                                    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Mecanum Drivetrain Kit V2](https://cad.onshape.com/documents/fe4ddc04acb2fe07e7615d35/w/99b93940e1575fb04acb47d4/e/f34759ef6ea954e463811068?renderMode=0\&uiState=63332124bf3b523d61ddca27) |

<figure><img src="/files/LkONOkWArEKmrJl0GV2w" alt=""><figcaption></figcaption></figure>

### Kit Options

This drivetrain can be built out of the following options:

#### FTC Starter Kit V3.1

| Part Number                                                         | Description                               | QTY.  |
| ------------------------------------------------------------------- | ----------------------------------------- | ----- |
| [REV-45-3529](https://www.revrobotics.com/rev-45-3529/)             | FTC Starter Kit V3.1                      | 1     |
| [REV-41-2080](https://www.revrobotics.com/rev-41-2080/)             | Ultra 90 Degree Gearbox                   | 4     |
| [REV-41-1600](https://www.revrobotics.com/rev-41-1600/)             | UltraPlanetary Gearbox Kit & HD Hex Motor | 1     |
| [REV-45-1655](https://www.revrobotics.com/rev-45-1655/)             | 75mm Mecanum Wheel Set                    | 1 set |
| [REV-41-1713-PK100](https://www.revrobotics.com/M3-Hex-Cap-Screws/) | M3 x 6mm HexCap Screws 100 Pack           | 1     |

#### Mecanum Drivetrain Kit V2&#x20;

<table><thead><tr><th>Part Number</th><th width="249">Description</th><th>QTY.</th></tr></thead><tbody><tr><td><a href="https://www.revrobotics.com/rev-45-2470/">REV-45-2470</a></td><td>Mecanum Drivetrain Kit V2</td><td>1</td></tr></tbody></table>

### Full Bill of Materials

<table><thead><tr><th>Part Number</th><th width="249">Description</th><th>QTY.</th></tr></thead><tbody><tr><td><a href="https://www.revrobotics.com/15mm-Plastic-Brackets/">REV-41-1305</a></td><td>15mm Plastic 90 Degree Bracket - 8 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/5mm-Hex-Spacers/">REV-41-1323</a></td><td>15mm Spacer - 12 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/5mm-Hex-Spacers/">REV-41-1324</a></td><td>3mm Spacer - 16 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/rev-41-1327-pk10/">REV-41-1327</a></td><td>Shaft Collars - 10 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/5mm-Hex-Shafts/">REV-41-1348</a></td><td>5mm x 90mm Hex Shaft - 4 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/M3-Hex-Cap-Screws/">REV-41-1359</a></td><td>M3 x 8mm Hex Cap Screws - 100 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/M3-Hex-Cap-Screws/">REV-41-1713-PK100</a></td><td>M3 x 6mm Hex Cap Screws - 100 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/rev-41-1361-pk100/">REV-41-1361</a></td><td>M3 Nyloc Nuts - 100 Pack</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/rev-41-1600/">REV-41-1600</a></td><td>UltraPlanetary Gearbox Kit &#x26; HD Hex Motor</td><td>4</td></tr><tr><td><a href="https://www.revrobotics.com/rev-41-1762/">REV-41-1762</a></td><td>45mm x 15mm C Channel - 408mm</td><td>4</td></tr><tr><td><a href="https://www.revrobotics.com/rev-41-1767/">REV-41-1767</a></td><td>45mm x 15mm C Channel - 248mm</td><td>2</td></tr><tr><td><a href="https://www.revrobotics.com/rev-45-1655/">REV-45-1655</a></td><td>75mm Mecanum Wheel Set</td><td>1</td></tr><tr><td><a href="https://www.revrobotics.com/rev-41-2080/">REV-41-2080</a></td><td>Ultra 90 Degree Gearbox</td><td>4</td></tr></tbody></table>

### Required Tools

| Part Number                                             | Description              | QTY Included in Kit |
| ------------------------------------------------------- | ------------------------ | ------------------- |
| [REV-41-1377](https://www.revrobotics.com/rev-45-1882/) | 2mm Allen Wrench         | 1                   |
| [REV-41-1376](https://www.revrobotics.com/rev-45-1882/) | 1.5mm Allen Wrench       | 1                   |
| [REV-41-1374](https://www.revrobotics.com/rev-41-1374/) | 5.5mm Combination Wrench | 1                   |
| [REV-41-1119](https://www.revrobotics.com/rev-41-1119/) | 5.5mm Nut Driver         | 1                   |
