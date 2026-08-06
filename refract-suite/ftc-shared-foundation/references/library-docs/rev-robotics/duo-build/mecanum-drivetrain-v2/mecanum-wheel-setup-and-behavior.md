> Source: https://docs.revrobotics.com/duo-build/mecanum-drivetrain-v2/mecanum-wheel-setup-and-behavior.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/mecanum-drivetrain-v2/mecanum-wheel-setup-and-behavior.md).

# Mecanum Wheel Setup and Behavior

Mecanum wheels, when properly set up on a drivetrain, allow for omni-directional movement. Each Mecanum Wheel Set ([REV-45-1655](https://www.revrobotics.com/rev-45-1655/)) comes with a two right (REV-41-1656) and two left (REV-41-1657) mecanum wheels. This is determined by the direction of the leading edge of the rollers. If the rollers point left it is a left wheel and if they point right it is a right wheel.&#x20;

<figure><img src="/files/dCIEZW9lXt4iIquANpbS" alt=""><figcaption></figcaption></figure>

Each side of the chassis needs one left and one right wheel. Mecanum Chassis also require four motors for operation.‌

<figure><img src="/files/9JgsqlIJ1CLVOKs65HMa" alt=""><figcaption></figcaption></figure>

To know if your Mecanum Wheels are properly configured look from the top down on the drivetrain. Following diagonal lines created from the angle of the rollers should form an "X" as shown above.‌

### Mecanum Wheel Drivetrain Behavior

Running all four wheels in the same direction at the same speed will result in a forward/backward movement, as the longitudinal force vectors add up but the transverse vectors cancel each other out, as shown below.‌

![](/files/-MGElkhKXVl-5E9PyleO)

When both wheels on one side of the drivetrain are moving in one direction while the other side is moving in the opposite direction results in stationary rotation of the drivetrain. The transverse vectors cancel out but the longitudinal vectors combine to generate rotation around the central vertical axis of the drivetrain, as shown below.‌

![](/files/-MGElp8x9TzAzBG5F_NH)

When the right mecanum wheels run in one direction while the left mecanum wheels run in the opposite direction allows for a strafing movement, as the transverse vectors add up but the longitudinal vectors cancel out.‌

![](/files/gNzSu1SN7D97wxkSp9ng)

Using the above concepts in tandem through varying motor power to each wheel type allows for the drivetrain to move in different, angled vectors.

![](/files/-MGEy5xLE0nUJxvnvdtc)

{% hint style="info" %}
Need help programming your mecanum drivetrain? Check out our [Mecanum Drive Example Code Template and Configuration](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/programming-mecanum-refined) page!
{% endhint %}
