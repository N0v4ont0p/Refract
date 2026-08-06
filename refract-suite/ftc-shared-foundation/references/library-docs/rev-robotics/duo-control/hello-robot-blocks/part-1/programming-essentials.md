> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-essentials.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-essentials.md).

# Programming Essentials

During the process of creating an OpMode, the Blocks tool prompted the selection of a sample code. In Blocks, these samples act as templates, providing the blocks and logical structure for different robotics use cases. In the previous section, the sample code **BasicOpMode** was selected. This sample code, seen in the image below, is the structural shell needed in order to have a working OpMode.

<figure><img src="/files/QgTQRrUhYdBZqitcZ29y" alt=""><figcaption></figcaption></figure>

An OpMode can often be considered a set of instructions for a robot to follow in order to understand the world around it. The BasicOpMode provides the initial set of instructions that are needed in order for an OpMode to properly function.&#x20;

Though this sample is given to users to reduce some of the complexities of programming as they learn; it introduces some of the most important code blocks. Let's take a closer look at some of them!

## Key OpMode Blocks

<figure><img src="/files/AuxH8VWLxlGMAbRPtytg" alt=""><figcaption></figcaption></figure>

### Comments

**Comments** are blocks of code intended to help you the programmer.&#x20;

They can be used to explain the function of a section of code. This is especially helpful in collaborative programming environments. If code is handed from one programmer to another, comments communicate the intent of the code to the other programmer.&#x20;

Pre-added blocks like <img src="/files/-MVRzzz2RWu0i_oNzqo3" alt="" data-size="original"> are comments written by the FIRST Tech Team to help with getting started using the provided template.&#x20;

When using the BasicOpMode template we can see there are three comments already clicked into place:&#x20;

* ![](/files/zhdaKNVOJvBpUoa8ce4O) shows us where we will be establishing **variables**, resetting encoders, setting motor directions, and anything else that needs to happen when the code is first activated.&#x20;
* ![](/files/e3IykVOyCn1zaDQWnAG0) is where anything that will be used when hitting the play button on our Driver Hub should be added.&#x20;
* "Put loop blocks here" is similar to our last comment, but is for anything that needs to be repeated the entire time our program is running and will be halted when pressing the stop button.&#x20;

{% hint style="info" %}
A **variable** is a storage location with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value. Variables can be numbers, characters, or even motors and servos.
{% endhint %}

Take a moment to think where else comment blocks may be useful in a program or to communicate with others.&#x20;

<details>

<summary>Where else could we use comment blocks?</summary>

Below is an example of comment blocks used in our 2023-24 Starter Bot Programming Demo:

<img src="/files/Zcrf8BgczBTMbhjkMU6h" alt="" data-size="original">

Here you can see a comment block has been added to label where the code for the drivetrain is AND to help instruct a driver on how to control the robot!

</details>

### Call waitForStart

When the Robot Controller reaches the block ![](/files/9at5DqlgQX7bAWYC4Lxx) it will stop and wait until it receives a Start command from the Driver Hub.  Any code after this block will get executed only after the Start button has been pressed.

### Call opModeIsActive

After the ![](/files/DXkcMBGajM3pZl0qeQWd)*,* there is a conditional **if** block  ![](/files/tPMY5vrgCRjVweRIenIj) that only gets executed if the OpMode is still active (i.e., a stop command hasn't been received).

<figure><img src="/files/jNYikORNPXkM3hRZFKRi" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**If-then** (if-else) statements are similar to the concept of cause and effect. If cause (or condition) happens, then perform effect.&#x20;

In this case it could be read as "If the OpMode is active (or running) then do the following code."&#x20;
{% endhint %}

You may notice there are two insistences of "opModeIsActive". This allows us to have two options at the start of our program becoming active. The first option has anything that needs to be run only ONCE to be added before our repeat. Then the ![](/files/tswXoJa5ZOPjvhNKJdaP) that follows these blocks is an **iterative or looping** control structure.

<figure><img src="/files/PmYDJrWVpw3og6oq0s1W" alt=""><figcaption></figcaption></figure>

As long as ![](/files/NJ8ZkOmUPbzXDjgaeryv) is true those blocks within our loop will remain active when applicabl&#x65;*.* This is where we will add a majority of our code!

Once the you press the Stop button, the ![](/files/FMX1AqT0h4HVxhU9Exl3) clause is no longer true and the loop will exit.
