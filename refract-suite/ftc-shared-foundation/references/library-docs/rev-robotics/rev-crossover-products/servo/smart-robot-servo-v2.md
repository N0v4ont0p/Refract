> Source: https://docs.revrobotics.com/rev-crossover-products/servo/smart-robot-servo-v2.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/smart-robot-servo-v2.md).

# Smart Robot Servo V2

The REV Robotics [Smart Robot Servo V2](https://www.revrobotics.com/Smart-servo-v2) (SRS V2) is a configurable metal-geared servo that takes the guesswork out of aligning and adjusting servo-based mechanisms. One SRS V2 can be used as a standard angular servo, a custom angular servo, and a continuous rotation servo by simply changing its settings with the [SRS Programmer](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer).

<figure><img src="/files/7r47TN7GXxu3ce8OQcyt" alt=""><figcaption></figcaption></figure>

## Smart Robot Servo V2 Basics

The Smart Robot Servo V2 has a 25T output spline. A spline is a specific groove pattern cut into the shaft, which allows the rotation of the servo motor to be transmitted to the attached Aluminum Servo Horn ([REV-41-1363](https://www.revrobotics.com/rev-41-1363/)) or [Servo Adapter](https://www.revrobotics.com/ftc/motion/wheels-hubs-adapters/). Splines are like keys, so only matched types will fit together.

<figure><img src="/files/w9kw11DDBunfkHN1JsLG" alt=""><figcaption></figcaption></figure>

## Operating Modes

### Default Operation

Out of the box, the SRS V2 operates as a 270° servo. However, the REV [SRS Programmer](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer) can reconfigure the SRS V2 to set angular limits or switch it into a continuous rotation mode.

{% hint style="info" %}
For more information on how to use the SRS programmer to change the servo modes, see the [Switching Operation Modes](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer/switching-operating-modes) section
{% endhint %}

The default range for the SRS V2 is 270°. This range is mapped to an input pulse range of 500μs to 2500μs with 1500μs as the center point. The image below describes the pulse-to-angle relationship.

<figure><img src="/files/vi1Rg8tjIo87XmYm9eKM" alt=""><figcaption></figcaption></figure>

### Continuous Rotation

The SRS V2 can be configured with the SRS Programmer to operate in a continuous rotation mode. In this mode, the same input pulse range is mapped to direction and speed. The table below lists the pulse mapping for direction and speed.

<figure><img src="/files/kOfOWSJFdYjUew07Bwff" alt=""><figcaption></figcaption></figure>

### Angular Limits

The SRS V2 can be easily configured with the SRS Programmer to limit right and left motion at two user-defined angles. Input pulses that occur past the limits will be ignored, and the SRS V2 will hold the limit angle. Any two angles can be set as limits as long as the left limit is left of the center dead band and the right limit is to the right of the center dead band. The table below shows the valid regions for left and right limits.

<figure><img src="/files/aTa386QEMRMN7fdReqbq" alt=""><figcaption></figcaption></figure>

Once valid limits are programmed, the SRS V2 will ignore any pulses that exceed the limits and hold the limit angle. For example, the image below exhibits what would happen a left limit of -30° and a right limit of +60° was set.

<figure><img src="/files/1X6Dpkfot5w57CnqeDDg" alt=""><figcaption></figcaption></figure>

## Servo Accessories / Adapters

REV Robotics Servo Adapters fit 25T spline servos like the REV Robotics Smart Robot Servo V2. In addition to the variety pack of generic servo horns that come with the Smart Robot Servo V2, there are five other custom servo adapters that make using servos with the REV ION Build System easy.

**Aluminum Servo Shaft Adapters** ([REV-41-1558](https://www.revrobotics.com/rev-41-1558/)) convert a 25T spline servo output shaft into a female 5mm hex socket. This adapter can be used to drive a hex shaft directly.

**Aluminum Servo Horns** ([REV-41-1828](https://www.revrobotics.com/rev-41-1828/)) have a tapped hole pattern that can be directly mounted to any of the REV Robotics gears, wheels, or sprockets with the Motion Pattern.

**Aluminum Double Servo Arms** ([REV-41-1820](https://www.revrobotics.com/rev-41-1820/)) have two tapped holes that can be directly mounted to any of the REV Robotics extrusion, channel, or brackets.

**Aluminum 1/2in Rounded Hex Servo Shaft** ([REV-21-2892](https://www.revrobotics.com/ION-Servo-Accessories/#REV-21-2892)) converts a servo to a 1/2in Hex shaft for use with all other ION mechanical system components.

**Plastic 1/2in Hex Linkage Arm** ([REV-21-2895](https://www.revrobotics.com/ION-Servo-Accessories/#REV-21-2895)) used to control a linkage, flap, lever or pushrod.

**Plastic Face Mount Bracket** The ION Servo Face Mount Bracket ([REV-21-2896](https://www.revrobotics.com/ION-Servos/)) allows for easy integration of Servo Motors into the ION System.

<figure><img src="/files/bJd8ARW9eKcrQiGITOSd" alt=""><figcaption></figcaption></figure>
