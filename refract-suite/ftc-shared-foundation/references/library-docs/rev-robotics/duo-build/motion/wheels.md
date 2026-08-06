> Source: https://docs.revrobotics.com/duo-build/motion/wheels.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/wheels.md).

# Wheels

## Wheel Basics&#x20;

REV Robotics offers four types of wheels: [DUO Traction](https://www.revrobotics.com/rev-for-ftc/motion/wheels-hubs-adapters/wheels/), [DUO Omni](https://www.revrobotics.com/rev-for-ftc/motion/wheels-hubs-adapters/wheels/), DUO Mecanum ([REV-45-1655](https://www.revrobotics.com/rev-45-1655/)), and [DUO Compliant](https://www.revrobotics.com/2in-compliant-wheel-5mm-hex-bore/). There are two different DUO traction wheels available: the standard DUO Traction Wheel and the DUO Grip Wheel ([REV-41-1267](https://www.revrobotics.com/rev-41-1267/)).  The traction wheels resemble standard wheels, like what you might see on a car or a bike. The main focus of the traction wheels is to pull a robot (or create traction) in a forward/backwards motion.&#x20;

Omni and Mecanum wheels, however, are **omnidirectional wheels**. Omnidirectional wheels give additional flexibility to a drive train by adding an additional vector of motion, known as **strafing**.&#x20;

This section will walk through the different kind of wheels available through REV and best practices for utilizing them.&#x20;

## DUO Traction Wheels&#x20;

The DUO Traction Wheel comes in three different sizes to allow flexibility in design and usage of the wheels.&#x20;

![](/files/-M9Pu8aJ77yRaOhUrh80)

### Product Specs:&#x20;

* Hub Material: Nylon (PA66)
* Tread Material: TPU
* Width: 15mm
* Hole Diameter: M3 clearance
* Hole Spacing: 8mm
* Weight:[ Various weights ](https://www.revrobotics.com/rev-for-ftc/motion/wheels-hubs-adapters/wheels/)

## DUO Grip Wheels&#x20;

DUO Grip Wheels are wider than standard DUO Traction Wheels, offering traction while still being lightweight in specific drivetrain applications, like driving on soft foam tiles. These wheels are designed for optimal grip in situations where the material the wheel is interacting with is compliant like soft foam tiles, carpet, or foam balls.

![](/files/-MBoEW8qRJzJ4gLRxgUG)

### Product Specs:

* Diameter: 90mm
* Width: 25mm
* Hub Material: Nylon (PA66)
* Hub Bore: 5mm Hex
* Tread Material: TPU
* Tread Durometer: 65A
* Hole Diameter: M3 Clearance
* Hole Spacing: 8mm
* Weight (single wheel): 88g (3.10oz)

## DUO Omni Wheels&#x20;

DUO Omni wheels are a special kind of wheel that has smaller rollers around the circumference of the wheel. These rollers can passively roll perpendicularly to the direction the wheel is driven. This wheel makes it easier for a robot to turn in a [differential drivetrain](/duo-build/channel-drivetrain-build-guide.md). Using DUO Omni wheels in conjunction with each other can create more maneuverable robots in advanced drivetrain applications.

![](/files/-MlBkBhHcRPXRaeToqdk)

A single omni wheel is the same thickness, 15mm, as all other motion components. In some applications, it might be desirable to stack two omni wheels, with one rotated by 60° from the other, as shown below. By setting your wheels in this configuration you ensure that a roller is always in contact with the ground. This results in smoother and more consistent operation.

![](/files/-MlBkFNv2cV8u9BC6wUD)

### Product Specs:

* Hub Material: Nylon (PA66)
* Roller Material: TPU
* Thickness: 15mm
* Hole Diameter: M3 clearance
* Hole Spacing: 8mm
* Weight (single wheel): [Various Weights ](https://www.revrobotics.com/rev-for-ftc/motion/wheels-hubs-adapters/wheels/)

## Mecanum Wheels <a href="#mecanum-wheels" id="mecanum-wheels"></a>

‌REV DUO Mecanum Wheels have a similar functionality to the Omni Wheel. The Mecanum Wheels have rollers around the whole circumference of the steel plate rim, set at a 45° angle. The full set of rollers present on the Mecanum Wheel remove the need to stack two wheels together like is required with the omni wheel.‌

Tested for the rigors of competition, REV DUO Mecanum Wheels are steel plates with rollers supported by ball bearings allowing for the perfect combination of wheel rigidity and roller movement. Included in the set of wheels are Universal Hex Adapter making mounting to 5mm hex shaft easy. With a 75mm diameter these wheels allow for a lower profile giving more space for building mechanisms and space for game elements.‌

![](/files/-METr0i8LZ6RynVYmAQ6)

### Product Specs: <a href="#product-specs-3" id="product-specs-3"></a>

* Hub Material: Steel
* Roller Material: NBR
* Diameter: 75mm
* Width: 40mm
* Weight (single wheel without Universal Hex Adapter): 179 g (0.395 lbs)
* Durometer: 77 ± 2, Type C

When using [mecanum wheels it is important to orient them correctly](/duo-build/ftc-starter-kit-mecanum-drivetrain/mecanum-wheel-setup-and-behavior.md) for optimal performance.

## DUO Compliant Wheels

The 2in Compliant Wheels are used for intakes and conveyor systems. Featuring a solid 5mm Hex Hub molded into the wheel making sure more power is driven by the wheel, combined with the “hurricane” cutouts to ensure even compliance across the rotation of the wheel. These wheels come in two different durometers, Soft - Light Gray 30A and Medium - Gray 45A. As the tread durometer increases the compliant wheel gets harder which will change traction, wear, and compliance of the wheel.

![](/files/tqEXYjfuMKFVufmW3e2T)

### Product Specs

* Diameter: 2in (50.8mm)
* Width: 0.5in (12.7mm)
* Hub Material: Polypropylene
* Hub Bore: 5mm Hex
* Tread Material: Thermoplastic Rubber
* Weight (single wheel): 18.1g (0.64oz)
* RPM Rating: 5,500 RPM

### Durometer Specs:

| Hardness                        | Color      | Durometer |
| ------------------------------- | ---------- | --------- |
| **Medium** like a pencil eraser | Gray       | 45A       |
| **Soft** like a rubber band     | Light Gray | 30A       |

## DUO Flap Wheels

Flap Wheels are used for intakes and conveyor systems to pick up irregular gamepieces, playing a similar role to compliant wheels. DUO Flap wheels feature cut marks every 3.2mm on the flaps for consistent cutting, allowing for versatility and adaptability for unique game pieces. The DUO Flap wheels have a solid 5mm Hex Hub molded into the wheel making sure more power is driven by the wheel. These wheels come in three different durometers, Soft - Light Gray 30A, Medium - Dark Gray 40A, and Hard - Black 60A. As the tread durometer increases the compliant flap gets harder which will change traction, wear, and compliance of the flap.

<figure><img src="/files/RSljI0zXgRgnpFSjx3F0" alt="" width="375"><figcaption></figcaption></figure>

### Product Specs

* Length: 4in (101.6mm)
* Width: 0.44in (11.1mm)
* Material: Polypropylene & TPR
* Hub Bore: 5mm Hex
* Hub Width: 0.59in (15.0mm)
* Weight (single wheel): 9.07g (0.03lb)

### Durometer Specs:

| Hardness                        | Color      | Durometer |
| ------------------------------- | ---------- | --------- |
| **Soft** like a rubber band     | Light Gray | 30A       |
| **Medium** like a pencil eraser | Dark Gray  | 40A       |
| **Hard** like a tire tread      | Black      | 60A       |
