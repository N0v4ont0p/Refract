> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-multiple-movements.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-multiple-movements.md).

# ElapsedTime - Multiple Movements

Right now our robot should move forward 3 seconds then stop. What if we wanted our robot to do something else after those 3 seconds? How do we request our program to continue?&#x20;

To start let's duplicate our existing loop. We can right click on a block to duplicate it. In this case, since our block is a loop, it will duplicate everything within the loop.

<figure><img src="/files/EzjLZkWD3fG0zu0Ma0fR" alt=""><figcaption></figcaption></figure>

We can snap our second loop below the original, however something is still missing. If we want our second loop to start we need our timer to first reset! We can add a <img src="/files/-MWAAooN8dw_8N49YaIo" alt="" data-size="original"> block between our two loops.

<figure><img src="/files/Trkxd4OieGxvxsy5RDlR" alt=""><figcaption></figcaption></figure>

Notice our second loop also has a call for telemetry data, however the name is the same! Let's edit it to be "Number of Seconds in Phase 2". Keep the names in mind if you duplicate additional loops.

## Quick Check!

Give your program a test to see what happens. Think about the following while testing:

* How long does the robot move?
* Could you tell when the robot switched between Phase 1 and 2?
* What happens if we change the power in the second loop?

## Reversing Movement

Having multiple loops with different amounts of time can give us a lot of power to help our robot navigate an area. For now let's have our robot complete it's first movement forward for 3 seconds, then reverse back to the start.&#x20;

This simply requires changing our power in the second loop to -1 !

<figure><img src="/files/8zVr817jQy61HsE0p9Wr" alt=""><figcaption></figcaption></figure>
