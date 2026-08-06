> Source: https://docs.revrobotics.com/duo-build/motion/motors/hd-hex-motor.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/motors/hd-hex-motor.md).

# HD Hex Motor

## HD Hex Motor Basics&#x20;

The HD Hex Motor ([REV-41-1291](https://www.revrobotics.com/REV-41-1291/)) features an integrated encoder and power that plug right into the REV Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)). The gearbox options feature 5mm Hex output or coupler making it easy to connect gears, sprockets, wheels, etc. Encoder and power cables are always included with motor. The HD Hex Motor is similar in size and power to other brushed 550 class motors with more convenient output options and connectors.

![](/files/-M95JnKjgsxv73CPT0aB)

The HD Hex Motor matches the design flexibility of other REV products with a series of compatible gearboxes to choose from. Gearbox options include the UltraPlanetary Gearbox ([REV-41-1600](https://www.revrobotics.com/rev-41-1600/)), Spur Gearboxes, Planetary Gearbox, and no gearbox.&#x20;

This section will focus on general HD Hex Motor information such as motor specifications and mounting techniques.

{% hint style="info" %}
*To learn more about gears and how they work with the HD Hex Motor visit the* [*gears*](/duo-build/motion/gears.md#gear-basics) *page.*&#x20;
{% endhint %}

### Pinout

The HD Hex Motor uses a 2-pin JST-VH Connector for motor power and a 4-pin JST-PH for sensor feedback from the built-in encoder. For more information on using the cables and connectors included with the HD Hex Motor, see the [REV Control System - Cable and Connectors documentation](https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors). The image below has the pinout for the motor power and the encoder.

![](/files/-M_MCcUszaBq8eeo9Rmp)

## HD Hex Motor (No Gearbox)

Why would you get a motor without a gearbox? Lets consider a few scenarios:

* [**Motors Can Fail**](/duo-build/motion/motors.md#preventing-premature-motor-failure) - If you have a motor that has failed but the gearbox is still in good condition, it is typically cheaper to buy the bare motor and attach the gearbox you already have.
* [**Customization**](/duo-build/motion/gears.md#metal-gears) - If you want to make your own gearbox, having the No Gearbox version of the motor will make that easier.

{% hint style="info" %}
If you are planning to make a custom gearbox keep in mind that the bare HD Hex motor comes pre-pressed with a pinion for the spur gearboxes.
{% endhint %}

### Product Specifications

* Weight: 234g
* Body Diameter: 37mm
* Voltage: 12V DC
* No-Load Current: 400mA
* Stall Current: 8.5A
* Free Speed: 6000 rpm
* Stall Torque: .105 Nm
* Max Output Power: 15W
* Encoder Counts per Revolution
  * At the motor - 28 counts/revolution

{% hint style="info" %}
If you are creating a custom gearbox or using the UltraPlanetary Gearbox, the specifications for the bare motor will help you calculate key metrics for your actuator.
{% endhint %}

## Planetary Gearboxes

Planetary gearboxes are designed for increased robustness when compared to Spur gearboxes, and are generally less susceptible to damaging shock loads due to more gear teeth being engaged to carry the load. There are a two planetary gearbox options from REV, the 20:1 Planetary gearbox ([REV-41-1211](https://www.revrobotics.com/rev-41-1301/)) and the UltraPlanetary gearbox. The 20:1 Planetary gearbox has a set gear ratio where the UltraPlanetary allows for swapping out of cartridges to adjust the final gear ratio.

### UltraPlanetary Gearbox

The UltraPlanetary System is a cartridge based modular gearbox designed to handle the rigors of the competition and the classroom. The UltraPlanetary System includes an input stage and pinion gear that works with the REV HD Hex Motor and other 550 class motors. Building on the ability to iterate and adjust designs easily using the REV Building System, the UltraPlanetary System consists of pre-assembled and lubricated cartridges allowing for swapping gear ratios on the fly and with ease. Users can configure a single-stage planetary using one of three different reduction cartridges, build multi-stage gearboxes through stacking individual cartridges together, and choose two different ways for transferring power: either through face mounting directly on the output stage or choosing the length of 5mm hex shaft best suited for the application.

The UltraPlanetary system has a variety of options for mounting with four different brackets available for mounting to[ REV 15mm Extrusion](https://www.revrobotics.com/ftc/structure/15mm-extrusion/), [REV C Channel](https://www.revrobotics.com/competition/ftc/structure/channel/?sort=featured), or [REV U Channel](https://www.revrobotics.com/competition/ftc/structure/channel/?sort=featured).

{% hint style="info" %}
For more information, including assembly tips, mounting options, and more in the [UltraPlanetary Gearbox System User's Manual](/rev-crossover-products/ultraplanetary/up-gearbox.md)!
{% endhint %}

![](/files/-M95HrIOql0y5Mtpa_5D)

#### Sample Gearbox Choices&#x20;

A wide range of gear ratios are possible with the three included cartridges. When combining up to three cartridges, just multiply each cartridge gear ratio to find the overall gear ratio. For example, a combination of the 4:1 and 5:1 cartridges would make a 20:1 overall gear ratio. The table below shows the common use cases for all possible ratios that can be created with the included UltraPlanetary kit.

![](/files/-MJXXXABPEZRY9rex8B5)

Below are the specifications for a small sample of the options available with the UltraPlanetary Gearbox Kit.

| Nominal Gear Ratio | Actual Gear Ratio | Free Speed | Stall Torque | Weight              |
| ------------------ | ----------------- | ---------- | ------------ | ------------------- |
| 5:1                | 5.23:1            | 1147 RPM   | 0.55 Nm      | 371 g (0.818 lbs)   |
| 20:1               | 18.9:1            | 317 RPM    | 1.98 Nm      | 405 g (0.893 lbs)   |
| 60:1               | 54.8:1            | 109.5 RPM  | 5.75 Nm      | 441.5 g (0.973 lbs) |

{% embed url="<https://www.youtube.com/watch?v=tmB8c-cCHd8>" %}

### 20:1 Planetary&#x20;

The 20:1 Planetary gearbox features mounting holes on a 14mm bolt circle. The gearbox is compatible with the Planetary Gearbox Flat and Bent motor mounting brackets. To mount the 20:1 Planetary directly to the Extended Motion Pattern on REV Channel use a HD Hex Planetary Facemount Spacer.

![](/files/-MC8mx1n0nJNcMAHrpn0)

#### 20:1 Planetary Specs&#x20;

* Weight: 436g (including motor)
* Output Shaft: 5mm hex
* Output Shaft Length: 40mm
* Free Speed: 300 rpm (31.4 rad/s)
* Stall Torque: 297.4 oz-in (2.1 Nm)

## Spur Gearboxes

The Spur gearboxes feature the REV Motion Pattern that is compatible with REV Motion Brackets and the Extended Motion Pattern on REV Channel. There is a second mounting pattern that is standard for most spur gearboxes. This pattern is featured on the flat and bent motor mounting brackets for Spur Gearboxes.

![](/files/-MBu5lpsWhnIbueBwrjm)

#### 20:1 Spur Specs&#x20;

* Product SKUs
  * Gearbox ([REV-41-1064](https://www.revrobotics.com/rev-41-1064/))
  * Motor with gearbox ([REV-41-1298](https://www.revrobotics.com/rev-41-1301/))
* Weight: 350g (including motor)
* Output Shaft: 5mm hex
* Output Shaft Length: 40mm
* Mounting Holes: 10 - M3 tapped - use a 5mm length or shorter bolt
* Free Speed: 300 rpm (31.4 rad/s)
* Stall Torque: 297.4 oz-in (2.1 Nm)

#### 40:1 Spur Specs&#x20;

* Product SKUs
  * Gearbox ([REV-41-1065](https://www.revrobotics.com/rev-41-1065/))
  * Motor with gearbox ([REV-41-1301](https://www.revrobotics.com/rev-41-1301/))
* Weight: 350g (including motor)
* Output Shaft: 5mm hex
* Output Shaft Length: 40mm
* Mounting Holes: 10 - M3 tapped - use a 5mm length or shorter bolt
* Free Speed: 150 rpm (15.7 rad/s)
* Stall Torque: 594.7 oz-in (4.2 Nm)
