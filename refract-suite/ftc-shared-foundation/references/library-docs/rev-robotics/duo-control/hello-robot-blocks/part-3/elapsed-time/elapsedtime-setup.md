> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-setup.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-setup.md).

# ElapsedTime Setup

### Locating ElapsedTime Blocks:

Before getting started, let's quickly identify where we will find our ElapsedTime blocks. This menu can be found under the Utilities dropdown on our side toolbar.

<figure><img src="/files/CfSDCUGNdI27vSz8Zzmj" alt="" width="152"><figcaption></figcaption></figure>

### Setting up the Basics:

For this section, let's start by creating a new OpMode named HelloRobot\_ElapsedTime using the BasicOpMode sample.&#x20;

<figure><img src="/files/U7laEu4aLNZcjDIv4k54" alt=""><figcaption></figcaption></figure>

Recall when we [created variables while programming our drivetrain](/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks.md). We will be using them again during this part to help with calculations! To start create a variable called **runtime**.

<img src="/files/-MRQE2gij3X-3R0XTgtw" alt="" width="563">

From the variable menu, add the <img src="/files/-MW6E-QPblWZt1LMlC9-" alt="" data-size="original"> block to the OpMode below the <img src="/files/-MVRzzz2RWu0i_oNzqo3" alt="" data-size="original"> comment block.&#x20;

<figure><img src="/files/Y7H2q8mhkzw8dO4YOhst" alt=""><figcaption></figcaption></figure>

In order to utilize elements of the ElapsedTime, runtime will act as the **ElapsedTime** variable.  Add the <img src="/files/-MW6Id3RUFs-McuyZkjF" alt="" data-size="original"> block to the <img src="/files/-MW6E-QPblWZt1LMlC9-" alt="" data-size="original"> block.&#x20;

![](/files/-MRRF-G8F9erACtpn8C1)

Before moving on to the rest of the ElapsedTime structure lets go ahead and add the motor related blocks. Add <img src="/files/-MVwRA9auYOOqnGmzAX7" alt="" data-size="original"> to the op mode to the while loop.

<figure><img src="/files/QisBk0VjuqWIJgGI9oA2" alt=""><figcaption></figcaption></figure>

Remember that on a drivetrain one of our motors will need to be set to run in reverse to prevent the robot from spinning in place! Add the <img src="/files/-MW6L1g4Y8GSBICwwFHF" alt="" data-size="original"> block under the the <img src="/files/-MWA6F39D-6nHYXTbLoY" alt="" data-size="original"> block set.&#x20;

<figure><img src="/files/IdhHdNOLfvI36AZtWvvc" alt=""><figcaption></figcaption></figure>
