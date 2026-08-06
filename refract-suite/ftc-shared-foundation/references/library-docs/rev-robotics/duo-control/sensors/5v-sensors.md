> Source: https://docs.revrobotics.com/duo-control/sensors/5v-sensors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/5v-sensors.md).

# Using 3rd Party Sensors

The Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) are 3.3V logic level devices. Many 3rd party sensors, including ones that teams have previously purchased through vendors such as Modern Robotics, are 5V logic level devices.  Many of these legacy sensors are used with the REV system by using a logic level converter. REV Robotics offers a Logic Level Converter ([REV-31-1389](https://www.revrobotics.com/rev-31-1389/)) and an optional Sensor Adapter Cable ([REV-31-1384](https://www.revrobotics.com/rev-31-1384/)) so teams can more easily use their legacy sensors with the REV Control System.&#x20;

### Wiring a Limit Switch or Micro Switch

Limit switches are common 3rd Party sensor type used with the REV Control System and require a custom wiring harness.  Each of the digital inputs on the Control and Expansion Hub have a pull-up resistor making the digital inputs pulled "high" by default. Incorrect wiring of a limit switch to a digital input can create a conflict making the Control or Expansion Hub unresponsive.

The recommended wiring is to connect the signal wire (n, n+1) to the common pin (COM), the ground wire to the normally closed (NC) pin, and not connect to the normally open pin (NO) of the limit switch. With this wiring when the switch is in its normal state (not pressed), the switch is closed connecting the signal to ground (reporting `FALSE`in code). When pressed, the switch is open and disconnects the signal from ground (reporting `TRUE`in code).&#x20;

{% hint style="danger" %}
The power wire and the unused signal wire will not be used in this set up process.&#x20;
{% endhint %}

![](/files/-Md4CM_hm02aFjD6rs7p)

{% hint style="info" %}
If you need the opposite behavior (`FALSE`for pressed, and `TRUE`for not pressed) switch the ground (black) wire to the NO position instead of NC. Alternatively changing the logic in code will have a similar effect.&#x20;
{% endhint %}

### Logic Level Converter

The REV Robotics Logic Level Converter is a circuit board which generates a 5V output from the 3.3V input and uses a MOSFET on each signal line to create a bidirectional communication appropriate for a variety of digital signals include I2C communication.  For more information on how bidirectional level shifting communication is accomplished, please reference the [NXP Application Note AN10441](http://www.nxp.com/documents/application_note/AN10441.pdf).

![](/files/-M8MYdRGwpxcTFDtq3Zt)

{% hint style="warning" %}
The Logic Level Converter is only needed for the Digital and I2C senor ports on the Control or Expansion Hub when using a 5V device.
{% endhint %}

### Connecting 5V Encoder

The Logic Level Converter ([REV-31-1389](https://www.revrobotics.com/rev-31-1389/)) pinout directly matches the encoder cable pin out for FTC legal 3rd party motors. Encoder cables plug directly into the Logic Level Converter board and then the 4-pin JST PH Cable ([REV-31-1407](https://www.revrobotics.com/jst-ph-4-pin-sensor-cable-4-pack/)), which is included with the Logic Level Converter, is plugged into the appropriate Control Hub  ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/))  Encoder Port. Motors which are terminated with Anderson Power Pole style connectors use the JST VH to Anderson Power Pole Style ([REV-31-1381](https://www.revrobotics.com/rev-31-1381/)) cable to connect to the motor output port on the Control Hub.

![](/files/-M8MZ9iOENEtlJZ-mDQt)

{% hint style="info" %}
All REV Robotics Motors work directly with the REV Control and Expansion Hubs. No Logic Level Converter is needed for REV Motors.
{% endhint %}

### Connecting a 5V Sensor

A variety of 5V sensors are usable with the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) when used with a Logic Level Converter ([REV-31-1389](https://www.revrobotics.com/rev-31-1389/)). For some Modern Robotics I2C sensors a Logic Level Converter, and a change in wiring to match the pinout of the Control Hub are needed. Teams can either purchase a Sensor Cable as an add on to the Logic Level Converter Kit which will cross over the correct wires, or they can carefully rearrange the pin order on the sensor cable. If using the Sensor Cable, connect the sensor to the Control Hub as shown below.  It is recommended to zip tie the connection between the sensor and the sensor cable to prevent accidental disconnects.  See the [Sensor Compatibility Chart](/duo-control/sensors/5v-sensors/sensor-compatibility-chart.md) for more information on hardware required for other sensors.

![](/files/-MYHQWuaQXDYKS3YZYfG)
