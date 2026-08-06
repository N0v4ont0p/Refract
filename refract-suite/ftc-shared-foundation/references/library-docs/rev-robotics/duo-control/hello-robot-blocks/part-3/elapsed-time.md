> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time.md).

# ElapsedTime - Blocks

## Introduction to ElapsedTime

When using our gamepad, we can actively communicate with our robot while our program runs. Our robot waits for our input and acts accordingly until a different command is issued. However, this may not always be the case, such as during the autonomous period of a FTC competition.&#x20;

Our robot is smart enough to navigate some on its own, however we need to help it along to know what to look for. Eventually, you could work up to your robot being able to navigate using a camera and machine learning or its IMU to sense direction, but for now let's start with one of the built in features of the SDK: **ElapsedTime**

***

What do you think of when you think of a timer? A stopwatch? Your phone? Maybe the timer on a microwave or oven? Timers commonly consist of two main categories: **count up** and **count down**. You can think about the differences of these two by a comparison like keeping track of how fast a runner did a 100m dash vs. needing to know how much longer our food should cook.

**ElapsedTime** is a count up timer. Registering the amount of time elapsed from the start of a set event, like the starting of a stopwatch. In this situation, it is the amount of time passed from when the timer is created or reset within the code.&#x20;

### Quick Links:

| [ElapsedTime Setup](/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-setup.md) | [ElapsedTime Logic](/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-logic.md) | [ElapsedTime - Multiple Movements](/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-multiple-movements.md) |
| :-------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------: |

### Sneak Peek of Our Full Code:

<figure><img src="/files/8zVr817jQy61HsE0p9Wr" alt=""><figcaption></figcaption></figure>
