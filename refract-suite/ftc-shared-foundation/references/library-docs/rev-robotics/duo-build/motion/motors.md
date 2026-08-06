> Source: https://docs.revrobotics.com/duo-build/motion/motors.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/motors.md).

# Motors

## Motor Basics

Electric motors are the core power plant of most robots. There are two types of motors in the REV DUO Build System: the Core Hex Motor ([REV-41-1300](https://www.revrobotics.com/rev-41-1300/)) and the HD Hex Motor ([REV-41-1291](https://www.revrobotics.com/REV-41-1291/)). Both motors are brushed DC motors. The image below showcases the common elements of a bushed DC motor.&#x20;

#### Elements of a Brushed DC Motor

![](/files/-M8MhYlMn7b3u0xtE-Zr)

Brushed DC motors without a gear box can be estimated to be \~80% efficient, meaning if a motor is drawing 60 watts of power \~48 watts will be turned into mechanical energy and \~12 watts will become heat. Once a gear box is added the overall efficiency of the system goes down.

### Key Metrics&#x20;

DC brushed motors can be described by some key metrics:

{% tabs %}
{% tab title="Stall Torque" %}
**Stall Torque** is measured when the motors RPM is zero and the motor is drawing its full **Stall Current**. This value is the maximum torque the motor is ever capable of outputting. Keep in mind the motor is not capable of outputting this torque for an indefinite period of time. Waste energy will be released into the motor as heat. When the motor is producing more waste heat than the motor body is capable of dissipating the motor will eventually overheat and fail.
{% endtab %}

{% tab title="Stall Current" %}
**Stall Current** is the maximum amount of current the motor will draw. The stall current is measured at the point when the motor has torque that the RPM goes down to zero. This is also the point at which the most waste heat will be dissipated into the motor body.
{% endtab %}

{% tab title="Free Speed" %}
**Free Speed** is the **angular velocity** that a motor will spin at when powered at the **Operating Voltage** with zero load on the motor’s output shaft. This RPM is the fastest **angular velocity** the motor will ever spin at. Once the motor is under load its **angular velocity** will decrease.

{% hint style="info" %}
*Learn more about angular velocity in the* [*Core Concepts*](/duo-build/motion/motors.md#core-concepts) *section*
{% endhint %}
{% endtab %}

{% tab title="Operating Voltage" %}
**Operating Voltage** is the expected voltage that the motor will experience during operation. If a robot is built using a 12 volt battery the **Operating Voltage** of the motor will be 12 volts. When controlling the RPM of the motor the DC speed controller will modulate the effective voltage seen by the motor. The lower the voltage seen by the motor the slower it will spin. DC motors have a maximum rated voltage if this voltage is exceeded the motor will fail prematurely.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The key metrics defined above are interrelated. Take some time to familiarize yourself with the definitions and how they connect together.  &#x20;
{% endhint %}

![](/files/-M8MjbITl7U1Z3GF12lg)

The prototypical performance graph of a Brushed DC motor can be used to estimate the performance of a motor. In most cases amperage, the unit of measurement for current, is the easiest value to find as it can be reported by the REV Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)).

### Preventing Premature Motor Failure&#x20;

In order to ensure that an electric motor lasts as long as possible a few rules of thumb should be kept in mind:

* **Smooth loading** - large torque spikes or sudden changes in direction can cause the wear and premature failure of gear box components. This is only an issue when the torque spike exceeds the rated stall torque of the motor. When shock loading is necessary, it is best to utilize mechanical braking or a hard stop that absorbs the impact instead of the motor.
* **Overheating** - when a motor is loaded at near its maximum operating torque it will produce more waste heat than when operating at a lower operating torque. If this heat this allowed to build up the motor can wear out prematurely or fail spontaneously.

{% hint style="info" %}
The Core Hex motor can run for approximately 4 hours continuously before overheating at near maximum torque loading.
{% endhint %}

![](/files/-MkxTx7rWGPS61t1vhRb)

* **Poorly supported output shaft**, most motor output shafts are not designed to take large thrust forces or forces normal to the shaft. Bearings need to be used to support the axle when loads in these directions are expected.

![](/files/-M8MhYlSbdgM5CBTcLsw)

{% hint style="info" %}
*To learn more about how to properly support motion visit the* [*supporting motion*](/duo-build/building/supporting-motion.md) *page*
{% endhint %}

## REV Motor Specifications

REV DUO Robotics motors come in two types, [HD Hex Motors](/duo-build/motion/motors/hd-hex-motor.md) and [Core Hex Motors](/duo-build/motion/motors/core-hex-motor.md). All REV DUO Motors have a Hex Shaft or female hex coupler as the output from its gearbox. The Hex Shaft is extremely reliable at transmitting torque without being reliant on set screws that can come loose or not be tightened sufficiently. REV DUO motors also include keyed locking connectors for both the motor power and the built-in encoder.&#x20;

{% hint style="info" %}
*For more information on the encoder see the Control System Guide*
{% endhint %}

![](/files/-M8N2tQzyjYft6IXAWR3)

![](/files/-M8MhYlWc2lieDE0X1Fg)
