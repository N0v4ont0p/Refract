> Source: https://docs.revrobotics.com/duo-control/control-system-overview/protection-features.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/control-system-overview/protection-features.md).

# Protection Features

The Control ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/))  were designed with a number of protection features built into the device. These include the following:  &#x20;

* Reverse battery input protection
* Electrostatic discharge (ESD) protection on all connections
* Over-current protection  &#x20;on all power buses
  * Digital I/O bus
  * I2C bus
  * Analog bus
  * USB
  * Servo bus per pair (0-1, 2-3, 4-5)
  * Encoder bus
* Over-current monitoring for individual Motor Channels
* Keyed and locking connectors
* Fail-safe mode at communication loss
