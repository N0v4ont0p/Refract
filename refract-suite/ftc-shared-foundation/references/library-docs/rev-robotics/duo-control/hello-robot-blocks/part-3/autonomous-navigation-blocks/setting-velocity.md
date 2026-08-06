> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/setting-velocity.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/setting-velocity.md).

# Setting Velocity

## Setting Velocity in our Program

Velocity is a closed loop control within the [SDK](/duo-control/hello-robot-blocks/where-to-program/what-is-an-opmode.md) that uses the encoder counts to determine the approximate power/speed the motors need to go in order to meet the set velocity.&#x20;

To set a velocity, its important to understand the maximum velocity in RPM your motor is capable of. For the Class Bot V2 the motors are capable of a maximum RPM of 300. With a drivetrain, you are likely to get better control by setting velocity lower than the maximum. In this case, lets set the velocity to 175 RPM!

Since RPM is the amount of revolutions per minute, a conversion needs to be made from RPM to ticks per second (TPS). To do this, divide the RPM by 60 to get the amount of rotations per second.&#x20;

Rotations per second can then be multiplied by `COUNTS_PER_WHEEL_REV`, to get the amount of ticks per second.&#x20;

$$
TPS = \frac{175}{60} \* CPWR
$$

### Adding Ticks per Second as a Variable

Create a new variable called TPS. Add the <img src="/files/-MYfxnoZpHQV4V7dyiqS" alt="" data-size="original">  to the beginning of the if/then statement above the target variables.&#x20;

<figure><img src="/files/uAbW7ExReh2CcewPxM02" alt=""><figcaption><p>Adding the TPS variable</p></figcaption></figure>

Add a <img src="/files/-MYRS32ax0_5fhPWNou9" alt="" data-size="original"> block to the <img src="/files/-MYfxnoZpHQV4V7dyiqS" alt="" data-size="original"> block. On the right side of the <img src="/files/-MYRS32ax0_5fhPWNou9" alt="" data-size="original"> block add the <img src="/files/-MYey5fLzndMDfYs7HdW" alt="" data-size="original">. One the left side of the <img src="/files/-MYRS32ax0_5fhPWNou9" alt="" data-size="original"> add the<img src="/files/-MYepPimZMwCPPARot8P" alt="" data-size="original"> block.&#x20;

Add the chosen RPM (175 in this example) to the left side of the <img src="/files/-MYepPimZMwCPPARot8P" alt="" data-size="original"> block and 60 to the right side.&#x20;

![](/files/-MYfzugs_ZuQcMfIRTGE)

### Changing from Power to Velocity

Now that the target ticks per second has been set, swap the <img src="/files/-MYg1RLiF3aIU-PaJgah" alt="" data-size="original">block for a <img src="/files/-MYg1WJmbeYlb5XsxdAI" alt="" data-size="original"> block. Add the <img src="/files/-MYg2807btHlLi-Ew5MN" alt="" data-size="original"> to both motors.&#x20;

<figure><img src="/files/BSJP344nOJWgBMJuJZvu" alt=""><figcaption><p>Setting our motors to run the specific velocity</p></figcaption></figure>

With the velocity set, let's give our program a test run after saving!&#x20;

### Full Program

<figure><img src="/files/zbYgzCPevIkW41EIsDoH" alt=""><figcaption><p>Full encoder demo Blocks program</p></figcaption></figure>
