> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-servos/using-a-gamepad-with-a-servo.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-servos/using-a-gamepad-with-a-servo.md).

# Using a Gamepad with a Servo

## Programming a Servo with a Gamepad

Having our robot able to rotate the servo automatically can be incredibly useful, especially when writing an autonomous program, but what if I want to control the positions with my gamepad?&#x20;

Let's take a look at how we can add input commands to our code!

For this example the known state will stay at position 0, so that after initialization the servo will be a the -135 degree position of the servo range. The following list shows what buttons correspond with which servo position:

{% hint style="info" %}
If you are using a PS4 Controller, selecting the appropriate button from the dropdown in Blocks may be easier to follow when looking back at your code. The buttons are also interchangeable when programming in Blocks. (ex: Y  in code = Triangle pressed on controller)
{% endhint %}

| **Button** | Degree Position | Code Position |
| ---------- | --------------- | ------------- |
| Y/Triangle | -135            | 0             |
| X/Square   | 0               | 0.5           |
| B/Circle   | 0               | 0.5           |
| A/Cross    | 135             | 1             |

Blocks for adding controller inputs can be found in the "Gamepad" menu:

<figure><img src="/files/ppJIqw5mbANisuP57MEK" alt=""><figcaption></figcaption></figure>

## Introducing If/Else Statements

One of the most common logic statements used in programming is an **if/else** statement, also known as an **if/then** statement. This block can be found under the "Logic" menu in Blocks:

<figure><img src="/files/nrilPlzr357SgK1QFrfB" alt=""><figcaption></figcaption></figure>

In its most simple format we will be asking our robot to check **IF** something is happening and if the answer is yes, or true in our robot's mind, **THEN** it will **DO**  what has been asked.&#x20;

### Quick Check!

During this section we are going to be asking "If the Y button is pressed on our controller then move our servo to position 0."&#x20;

<figure><img src="/files/3wMhIBOsTAZk8uSJ7fdI" alt=""><figcaption></figcaption></figure>

If our servo will move to position 0 when the previous statement is TRUE, what do expect to happen when the answer is FALSE (or the Y button is not pressed)?

<details>

<summary>What will happen when the answer is FALSE?</summary>

At the moment, we have not asked our robot to do anything specific when our statement is false. This means for now our servo will not move or change while our Y button is not pressed.&#x20;

</details>

## If/Else If Statements

Our **if/else** statement can come in many forms that includes multiple different conditional statements. Blocks allows for our base ![](/files/HEGf0SlCQv0phOhx1pEU) block to be easily added to add as many conditional statements as we need by clicking the blue gear on our block.

<figure><img src="/files/r1QD4T6HGDYVwuElRgio" alt=""><figcaption></figcaption></figure>

Adding an ![](/files/KozLQYwdgC6Sne0QM8hy) block by clicking and dragging to our existing **if** statement converts it into becoming an **if/else if** statement. Using our previous example we can see how this may look in Blocks:

<figure><img src="/files/WxTR3AelDeK2ymoxHsK6" alt=""><figcaption></figcaption></figure>

Now our statement is checking first **if** Y is being pressed to move to position 0, but has added now the option to look for something **else**, such as another button being pressed.

### Quick Check!

Let's add to our existing logic statement the ability to move our servo to position 1 when A is pressed on our controller. Give it a try first before revealing the answer below!

How would our full logic statement be read once our new blocks are added?

<details>

<summary>Reveal the answer!</summary>

Programming our servo to move to position 1 when A is pressed will look very similar to our existing code:

![](/files/bqQ7H3jQgtHkO0hdyhJV)

Now our statement reads: "If the Y button is pressed then move the servo to position 0, else if the A button is pressed then move the servo to position 1."

</details>

{% hint style="success" %}
If you have not already, test the code we have written thus far! Our logic statement should be added to our ![](/files/kiJyPre40E0OoA4OYcum) and previous ![](/files/OqOsq5LBmJUDyY9md7H3) removed.

* What happens when both buttons are pressed at the same time?
  {% endhint %}

## Adding Logic Operators

To add all of our gamepad inputs we need to further extend our i**f/else if** statement:

<figure><img src="/files/8GuSq2b4g5lcrZXMLDuA" alt=""><figcaption></figcaption></figure>

Now there are three different paths in our **if/else if** block that our robot may follow based on each input request. We've previously added our ability to move to position 0 and 1, but what about 0.5?&#x20;

You may have noticed in our gamepad chart at the beginning of this section that we are going to have two buttons able to move our servo to position 0.5. This is so we can practice using a **logical operator** like the ![](/files/3wMbI9EPBhL4SHewcMCZ) block in our program!

{% hint style="info" %}
The logical operator **or** considers two operands if either (or both) are true the **or** statement is true. If both operands are false the *or* statement is false.&#x20;

Similar the logical operator **and** considers two operands requiring both to be true for the whole statement to be true.&#x20;
{% endhint %}

From the **Logic** Menu in Blocks select the <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block.&#x20;

<figure><img src="/files/SPxe05R4qTPbHSbIM4pK" alt=""><figcaption></figcaption></figure>

Add this block to the **if/else if** block, as shown in the image below. Use the dropdown menu on the block to change it from an <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block to an <img src="/files/-MWB9-FbRpvUKsRz3Tbi" alt="" data-size="original"> block.&#x20;

{% hint style="info" %}
Our previously added blocks for A and Y inputs can be temporarily moved to the side in the workspace to be readded as applicable.
{% endhint %}

<figure><img src="/files/GrBK6jgxLIZbYV3hZxS1" alt=""><figcaption></figcaption></figure>

Add each button block to the **if/else if** block as seen in the image below.&#x20;

<figure><img src="/files/Q001DgrsHsosv4pvhBw0" alt=""><figcaption></figcaption></figure>

Now to finish by adding our <img src="/files/-MWAcLYKFQSC3PM2Cbef" alt="" data-size="original"> blocks to each section of the **If/else if** block. Set the servo position to correspond with the assigned gamepad button.&#x20;

<figure><img src="/files/u7iBVEwAYkDKTjSN46Ab" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Click Save OpMode and give your program a try!
{% endhint %}

There are three different paths in this **if/else if** statement. If the first conditional statement is true (the Y button is pressed) the servo moves to code position 0 and the other conditional statements are ignored.&#x20;

If the first condition is false (the Y button is not pressed) the second condition is analyzed. This means the order we add our pathways DOES matter. If  X and A are pressed at the same time, the robot will will try to prioritize the X button first.&#x20;

Give it a try!

## Full Program

<figure><img src="/files/8tMaHBkqgsm1etkbkhAu" alt=""><figcaption></figcaption></figure>
