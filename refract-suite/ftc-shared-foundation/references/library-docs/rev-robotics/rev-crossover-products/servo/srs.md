> Source: https://docs.revrobotics.com/rev-crossover-products/servo/srs.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/srs.md).

# Smart Robot Servo V1

The REV Robotics Smart Robot Servo (SRS) ([REV-41-1097](https://www.revrobotics.com/rev-41-1097/)) is a configurable metal-geared servo that takes the guesswork out of aligning and adjusting servo based mechanisms. One SRS can be used as a standard angular servo, a custom angular servo, and a continuous rotation servo by simply changing its settings with the [SRS Programmer](/rev-crossover-products/servo/srs-programmer.md).&#x20;

<figure><img src="/files/czgfzx7OhxfwdQK1ldMD" alt=""><figcaption></figcaption></figure>

## Smart Robot Servo Basics

The Smart Robot Servo has a 25T output spline. A **spline** is a specific groove pattern cut into the shaft, which allows the rotation of the servo motor to be transmitted to the attached Aluminum Servo Horn ([REV-41-1363](https://www.revrobotics.com/rev-41-1363/)) or [Servo Adapter](https://www.revrobotics.com/ftc/motion/wheels-hubs-adapters/). Splines are like keys, so only matched types will fit together. If the internal gears or spline of the REV Robotics Smart Robot Servo become damaged, they are replaceable using a Replacement Gear Set ([REV-41-1168](https://www.revrobotics.com/rev-41-1168/)).&#x20;

<figure><img src="/files/t36FeAqBV2av4cVnZqOS" alt=""><figcaption></figcaption></figure>

## Product Specifications&#x20;

The REV Robotics Smart Robot Servo includes the following features:

* Default operation:&#x20;
  * 270° motion over full input pulse range
* Metal gears
* Smart features
  * Programmable with REV SRS Programmer ([REV-31-1108](https://www.revrobotics.com/rev-31-1108/))
  * Servo Limit Mode
    * Set right and left angular limits
    * SRS will not move past limits
  * Continuous Mode
    * SRS spins continuously
    * Speed and direction set by input pulse

### Mechanical Specifications

| **Parameter**         | **Value and Units**      |
| --------------------- | ------------------------ |
| Stall torque (at 6V)  | 13.5 kg-cm / 187.8 oz-in |
| Speed (at 6V)         | 0.13s/60º                |
| Maximum angular range | 270º                     |
| Gear Material         | Brass                    |
| Spline Type           | 25T                      |
| Dimensions            | 40.2mm x 20.0mm x 38.0mm |
| Weight                | 2.05oz.                  |

#### Electrical Specifications

| **Parameter**         | **Min** | **Typ** | **Max** | **Units** |
| --------------------- | :-----: | :-----: | :-----: | :-------: |
| Voltage Rating        |   4.8   |   6.0   |   7.4   |     V     |
| Stall Current (at 6V) |    -    |    -    |   2.0   |     A     |
| Input Pulse           |   500   |   1500  |   2500  |     μs    |

## Kit Contents&#x20;

The REV Robotics SRS comes with the following:

* REV Smart Robot Servo
* Servo horn (arm) assortment
* Servo horn mounting hardware

## Operating Modes

### Default Operation&#x20;

Out of the box, the SRS operates as a 270° servo. However, the REV [SRS Programmer](/rev-crossover-products/servo/srs-programmer.md) can reconfigure the SRS to set angular limits or switch it into a continuous rotation mode.

{% hint style="info" %}
*For more information on how to use the SRS programmer to change the servo modes, see the* [*Switching Operation Modes*](/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md) *section*
{% endhint %}

The default range for the SRS is 270°. This range is mapped to an input pulse range of 500μs to 2500μs with 1500μs as the center point. The image below describes the pulse-to-angle relationship.

<figure><img src="/files/dEkn8bvfyx7iPaCkolnc" alt=""><figcaption></figcaption></figure>

### Continuous Rotation&#x20;

The SRS can be configured with the SRS Programmer to operate in a continuous rotation mode. In this mode, the same input pulse range is mapped to direction and speed. The table below lists the pulse mapping for direction and speed.

<figure><img src="/files/N72xu0DsCNKeyF13Roe8" alt=""><figcaption></figcaption></figure>

### Angular Limits&#x20;

The SRS can be easily configured with the SRS Programmer to limit right and left motion at two user-defined angles. Input pulses that occur past the limits will be ignored, and the SRS will hold the limit angle. Any two angles can be set as limits as long as the left limit is left of the center dead band and the right limit is to the right of the center dead band. The table below shows the valid regions for left and right limits.

<figure><img src="/files/RGgvz798l0nfC4eXEH12" alt=""><figcaption></figcaption></figure>

Once valid limits are programmed, the SRS will ignore any pulses that exceed the limits and hold the limit angle. For example, the image below exhibits what would happen a left limit of -30° and a right limit of +60° was set.

<figure><img src="/files/8RCVP1S3ROtdP1ehL6XW" alt=""><figcaption></figcaption></figure>

## Servo Accessories / Adapters

REV Robotics Servo Adapters fit 25T spline servos like the REV Robotics Smart Robot Servo. In addition to the variety pack of generic servo horns that come with the Smart Robot Servo, there are five other custom servo adapters that make using servos with the REV ION Build System easy.&#x20;

**Aluminum Servo Shaft Adapters** ([REV-41-1558](https://www.revrobotics.com/rev-41-1558/)) convert a 25T spline servo output shaft into a female 5mm hex socket.  This adapter can be used to drive a hex shaft directly.

**Aluminum Servo Horns** ([REV-41-1828](https://www.revrobotics.com/rev-41-1828/)) have a tapped hole pattern that can be directly mounted to any of the REV Robotics gears, wheels, or sprockets with the Motion Pattern.

**Aluminum Double Servo Arms** ([REV-41-1820](https://www.revrobotics.com/rev-41-1820/)) have two tapped holes that can be directly mounted to any of the REV Robotics extrusion, channel, or brackets.

**Aluminum 1/2in Rounded Hex Servo Shaft** ([REV-21-2892](https://www.revrobotics.com/ION-Servo-Accessories/#REV-21-2892)) converts a servo to a 1/2in Hex shaft for use with all other ION mechanical system components.

**Plastic 1/2in Hex Linkage Arm** ([REV-21-2895](https://www.revrobotics.com/ION-Servo-Accessories/#REV-21-2895)) used to control a linkage, flap, lever or pushrod.

**Plastic Face Mount Bracket** The ION Servo Face Mount Bracket ([REV-21-2896](https://www.revrobotics.com/ION-Servos/)) allows for easy integration of Servo Motors into the ION System.

<figure><img src="/files/N5ljOMnK8JY1hEiJypyZ" alt=""><figcaption></figcaption></figure>
