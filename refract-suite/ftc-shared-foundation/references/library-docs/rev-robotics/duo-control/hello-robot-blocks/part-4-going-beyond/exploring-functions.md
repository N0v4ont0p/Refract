> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/exploring-functions.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-4-going-beyond/exploring-functions.md).

# Exploring Functions

## What is a Function? <a href="#what-is-a-function" id="what-is-a-function"></a>

Functions act similar to a [variable](/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks.md#what-is-a-variable) in that we are using one thing to represent another. However, where a variable typically is used in place of something short, such as a number, a function can take the place of several lines of code.

This can be incredibly useful if there is a section of code we know will be repeated or to break apart our code into chunks for easy editing.

## Creating a new Function in Blocks <a href="#creating-a-new-function-in-blocks" id="creating-a-new-function-in-blocks"></a>

If we want to create a new function in our Blocks program, we start by pulling a ![](https://docs.revrobotics.com/~gitbook/image?url=https%3A%2F%2F268621232-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MHCAE012xNfg1h3SM9v%252Fuploads%252FjNRY9VTnip2Vc8wSaLGj%252Fimage.png%3Falt%3Dmedia%26token%3Dedb065d4-91c9-49f0-a3db-98a366076b28\&width=300\&dpr=4\&quality=100\&sign=8f32c37b\&sv=1)block from the Functions menu:

<figure><img src="/files/R44fr4Wa2vpoFEebyn1a" alt="" width="280"><figcaption><p>Functions menu in Blocks showing the functions from the 2024-25 Starter Bot</p></figcaption></figure>

Next we will replace "do something" with an appropriate name. Maybe in this case we are adding a new function for climbing:

<figure><img src="/files/Sxr19fkXNFemJgW3GJzj" alt="" width="203"><figcaption><p>Example function for climbing</p></figcaption></figure>

Once our function is named it will appear in the "Functions" menu to be added to the main loop or wherever we need it within our code!

<figure><img src="/files/qnVYHj4QW1KXYRrLQfBl" alt="" width="278"><figcaption><p>New function block</p></figcaption></figure>

<figure><img src="/files/gpCqTEWvYY4ZF6fo5UVY" alt="" width="218"><figcaption><p>New function added to our main code</p></figcaption></figure>

All that's left is to add whatever code we'd like to be within this function:

<figure><img src="/files/LyvwBy37cyttTdKf1yos" alt="" width="256"><figcaption><p>Example of a simple code within our function</p></figcaption></figure>

If the ![](https://docs.revrobotics.com/~gitbook/image?url=https%3A%2F%2F268621232-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MHCAE012xNfg1h3SM9v%252Fuploads%252Fk7zr0SUBNrnWyrt3X2EY%252Fimage.png%3Falt%3Dmedia%26token%3D3bd23c18-a128-4b5c-bbcb-4dcc179e8063\&width=300\&dpr=4\&quality=100\&sign=41933077\&sv=1) block is deleted this will remove the function from the "Functions" menu.

## When to use Functions - Example

{% hint style="info" %}
This example was originally created as part of the [2024-25 FTC Starter Bot](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/starter-bot-into-the-deep) program, but can be followed on a different robot!&#x20;

After [configuring](/duo-control/hello-robot-blocks/configuration.md), create a new [OpMode](/duo-control/hello-robot-blocks/part-1/test-bed-blocks.md) to begin. Ours is named `FunctionsDemo`.&#x20;
{% endhint %}

Let's say we are working on an autonomous code where we want our robot to drive roughly in a square. Remember that autonomous means this code will move the robot on its own when play is pressed:

<figure><img src="/files/TlNHjXbynvXh6wGNVEST" alt="" width="291"><figcaption><p>Simple program for driving in a square</p></figcaption></figure>

Next, let's say we need the robot to do something between one of the turns, such as move its arm or open a servo's claw. There's a couple of ways we could approach this without functions:

<figure><img src="/files/NZuBZkYmOHPcICXpmJGE" alt="" width="164"><figcaption><p>Full code with claw opening after driving two sides</p></figcaption></figure>

Already our code is getting a little long so let's move our side motion and turn into a function:

<figure><img src="/files/Area5Up7hDbLJwX5Fqre" alt="" width="235"><figcaption><p>Function containing the code for driving and turning</p></figcaption></figure>

Now our loop may look like this:

<figure><img src="/files/ActG56xZl8sTNAdAoe0e" alt="" width="417"><figcaption><p>Using functions to drive in a square</p></figcaption></figure>

When we test our code we may notice our robot isn't exactly driving in a square shape. Thankfully with our function in place we only need to change the needed value in one place:

<figure><img src="/files/agyk00pUsghQ97ai11qH" alt="" width="235"><figcaption><p>Code for controlling the robot's turn</p></figcaption></figure>

This change to the function will be reflected anywhere `DRIVE_AND_TURN` used.

Give it a try by changing the right motor's power or the timer to refine your square!
