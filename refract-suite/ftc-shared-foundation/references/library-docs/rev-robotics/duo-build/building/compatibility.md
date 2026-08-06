> Source: https://docs.revrobotics.com/duo-build/building/compatibility.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/building/compatibility.md).

# Compatibility

## Compatibility Basics&#x20;

Increase the reliability of any robot system by switching from set screws to transmit motion to [hex shaft](/duo-build/motion/intro/shaft.md). Set screws can become loose and damage your shafts over time but using a hex shaft to transmit torque doesn’t require any set screws or keys, it just simply works.

Converting part of an existing design, or using already purchased parts, with hex is easy. The simplest option is to change to the HD Hex Motor ([REV-41-1291](https://www.revrobotics.com/REV-41-1291/)) and directly drive [REV DUO Build System Wheels](/duo-build/motion/wheels.md), or use a High Strength Hex Hub ([REV-41-1147](https://www.revrobotics.com/rev-41-1147/)) with an existing 4-hole pattern wheel. Use a shaft color to secure the wheel from sliding off the shaft.

![](/files/p0m36No5Kd3ewU6Jdlbe)

For a system with more shafts, the easiest way to couple between Hex and non-hex shafts is to use #25 pitch chain ([REV-41-1365](https://www.revrobotics.com/rev-41-1365/)) because it’s common to all systems. In designs with multiple chain stages it’s possible to change any number of the shafts over to hex. The more shafts converted, the less risk of a set-screw skipping and causing a failure. Starting from the motor and then changing subsequent shafts will provide the most benefit, but any shaft that’s converted to hex will reduce a point of failure.

The HD Hex Motor is used with either a REV DUO [Sprocket](https://www.revrobotics.com/ftc/motion/gears-sprockets-chain/) or a Hex Hub with any 4-hole pattern sprocket. Connected by chain to the next shaft which can either be another REV Robotics based hex shaft or can connect to any existing #25 pitch chain solution a team already owns.

![](/files/sk2UxBAceTztdlw9CTGa)

The High Strength Hex Hub and the Universal Hex Hub ([REV-41-1833](https://www.revrobotics.com/rev-41-1833/)) are specifically designed to help teams use the parts they already have with the reliability and convenience of a hex drive shaft. The High Strength Hex Hub is used below to convert an AndyMark Stealth Wheel to Hex Shaft. The extended part of the High Strength Hex Hub is sized to pilot the hub into the wheel keeping it centered.

![](/files/ykohXqkfiRtnqv1w76zz)

The REV DUO [Plastic Brackets](https://www.revrobotics.com/15mm-Plastic-Brackets/) have mounting holes on an 8mm spacing which is compatible with other building systems. When mounting a Plastic Bracket to flat channels, turn the bracket so that the alignment ribs on the bracket face out from the channel as shone below.

![](/files/-M9PO_4G71swldCiY5PK)

Tetrix channels also use an 8mm hole spacing so almost all REV DUO brackets can mount directly to the channel. There are several ways to mount motion brackets and a structural bracket to the Tetrix Channel. The motion brackets accept a 9mm bearing so they can be used to add hex shaft to a Tetrix robot.

![](/files/-M9POYqH3DOK07ap5ph6)

The 90 degree bracket  above is one way to mount extrusion to Tetrix channel. A stronger method would be to miter the end of the extrusion as needed and then bolt it directly to the Tetrix channel as shown in below. Install M3 hex cap bolts and nylocs in the Tetrix channel with the heads on the side the extrusion will be installed on. Slide the extrusion into place with the bolt heads in the extrusion channel and tighten. This method will also work with Actobotics channel.

![](/files/-M9POzbAMyy9mEFH5bAf)

To use the REV DUO [Delrin Bearings](https://www.revrobotics.com/ftc/motion/bearings-linear-slides-pillow-blocks/) directly in place of the Tetrix bushing, it’s recommended to drill out one of the Tetrix pattern 8mm holes to 3/8” (larger than 9mm) and then install a motion bracket over the clearance hole. Depending on which 8mm hole in the Tetrix pattern is used it’s possible to match drill and add more fasteners to secure the bracket. The Delrin bearings a designed specifically to run in the nylon brackets for low friction and long wear. If using a Delrin bearing directly in the metal channel checking the bearing for wear is recommended.

![](/files/-M9PP7YNyfTNCXrFOSYY)
