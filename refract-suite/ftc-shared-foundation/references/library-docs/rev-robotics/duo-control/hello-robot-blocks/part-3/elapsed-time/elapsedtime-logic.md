> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-logic.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-logic.md).

# ElapsedTime Logic

For now our goal will be to have the motors move forward for 3 seconds. To accomplish this we need to edit our main **While Loop** so that it triggers when the OpMode is active AND the ElapsedTime timer is less than or equal to 3 seconds.&#x20;

## Setting a Time Limit

Lets start by creating our less than or equal to condition. Grab the <img src="/files/-MW6NHckRVPOzOmTIXSr" alt="" data-size="original"> from the **Logic** menu.&#x20;

![](/files/-MS9j0TzPCtzilrte9jz)

Next select the ![](/files/qvOgxpF6XZZVrWfYdrrH) block from the **ElapsedTime** menu. Snap the block into the left side of the <img src="/files/-MW6NHckRVPOzOmTIXSr" alt="" data-size="original"> block. Using the dropdown menu, change the generic ![](/files/H7aPvfhCSOeCTc55HRfn) to the <img src="/files/-MWQgYaPEaq9DOao9riu" alt="" data-size="original"> variable we established earlier.

On the other side of our equation, we need to add a <img src="/files/-MW9tTS01Grlc87QDdhk" alt="" data-size="original"> block from the **Math** menu. Change the number block to 3.&#x20;

![](/files/-MSE064eO7zln0pxWMKH)

Right now the <img src="/files/-MWA26bM2CihY0G3zhg3" alt="" data-size="original"> is equal to three. Use the arrow next to the equal sign to choose the less than or equal to sign from the dropdown menu.

![](/files/-MSDzQ7kK6Qdxa-ru6_q)

With our time condition ready, we can set it aside for a moment.

## Modifying Our While Loop

Now let's set up our logic to modify our While Loop.&#x20;

First, grab an <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block from the **Logic** menu. The ![](/files/QTp1P2C9zW3sNsYomSef) block we currently have as part of our loop will be moved to the lefthand side.

On the other side, add the <img src="/files/-MWA0ZnQRJp7_PnmCnog" alt="" data-size="original"> block:

<figure><img src="/files/jGRVMbPMsBrv7FNxkmQU" alt=""><figcaption></figcaption></figure>

This block set will connect where the ![](/files/fTd6DoMjHYTvfoF9XYKW) block originally was. Now the w**hile loop** will now activate when both conditions of the *AND* block are true.&#x20;

<figure><img src="/files/WAIko2p1krELXTZTkmCl" alt=""><figcaption></figcaption></figure>

### Quick Check!

Let's give our OpMode a try and test the following scenarios:

* What happens when hitting play quickly after the initialization button is pressed?
* What happens when hitting play 2 seconds after the initialization button is pressed?
* What happens when hitting play 10 seconds after the initialization button is pressed?

<details>

<summary>What happens while testing?</summary>

You may notice the robot moves different distances depending on how long the wait is between INITIALIZATION and PLAYING the program. But why is that?

Remember our timer starts counting when created. Currently, our program creates our timer during initialization meaning it's counting up before Play is ever pressed. If we wait too long our robot may not do anything at all when clicking Play!

</details>

## Resetting the Timer

Not being able to pause between initialization and pressing Play is probably not ideal in most situations. It certainly makes tracking how far the robot will travel more challenging, the opposite of what we'd like ElapsedTime to help us do.&#x20;

To keep this from happening the timer should be reset once the OpMode is active. Grab the call ![](/files/1ktnrbt1WRhQ35W5wpnr) block from the ElapsedTime menu and switch it to our runtime variable.

![](/files/-MSEjra212WRenTZaPaH)

This will be added to our program BELOW the <img src="/files/-MWACAqNiP66tvS4fGxc" alt="" data-size="original"> comment and ABOVE the while loop.

<figure><img src="/files/JSHzXXlSTNyQVXyPdysr" alt=""><figcaption></figcaption></figure>

Since this is before our loop our robot will complete it once when Play is pressed. Then will complete the check for our while loop.

Test your program again with this change!&#x20;

{% hint style="success" %}
Now let's explore what happens when we change our time limit to different amounts. You can adjust your time limit by changing the 3 in our ![](/files/lfGInpSK5I3OeHK8Jq8k) block to a different number.&#x20;

Consider marking different goals on the floor with tape to practice determining how much time the robot needs to reach it.
{% endhint %}

## Adding Telemetry

In previous parts, we've looked at adding telemetry as a way for the robot to communicate with us. In this situation, it would be helpful for the robot to be able to tell us how much time it has counted so we can make adjustments to our program!&#x20;

Recall we can find our telemetry block under the utilities menu:&#x20;

<figure><img src="/files/cpzczWVGfTISN3csFxJ4" alt=""><figcaption></figcaption></figure>

Our ![](/files/miY6x9sG1WNVlgDnzpUp) block will snap into our number slot.

<figure><img src="/files/jOnyUCraRC233p0FuXHo" alt=""><figcaption></figcaption></figure>

For our **key** let's call it "Number of Seconds in Phase 1" for now. This will be useful for distinguishing where in our program our robot is during the next section.

Save your OpMode and give it a try!
