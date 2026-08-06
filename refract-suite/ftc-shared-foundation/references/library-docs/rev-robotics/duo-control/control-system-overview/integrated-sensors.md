> Source: https://docs.revrobotics.com/duo-control/control-system-overview/integrated-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/control-system-overview/integrated-sensors.md).

# Integrated Sensors

The REV Robotics Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) integrate a number of feedback sensors. Some of these are user accessible in the latest FTC Android Studio SDK, but others are not yet directly user accessible. These sensors are in some cases also used by the Control Hub and Expansion Hub for internal safety monitoring.&#x20;

* Battery Voltage Monitoring \[**Accessible**]
* Integrated 6-axis IMU \[**Accessible**]
  * Bosch BHI260AP 6-axis absolute orientation sensor
    * Control Hubs shipped before September 2022 instead feature a BNO055 9-axis IMU
    * Expansion Hubs shipped before December 2021 include a BNO055 9-axis IMU
    * Expansion Hubs shipped AFTER December 2021 do not have an IMU
  * Internally connected to I2C port 0 and configured to address 0x28
* Current Monitoring
  * Battery \[**Accessible**]
  * I2C Bus \[**Accessible**]
  * Digital Power Bus \[**Accessible**]
  * Servo Power Bus \[Not Accessible]
* Per Motor Channel Current Monitoring \[**Accessible**]
