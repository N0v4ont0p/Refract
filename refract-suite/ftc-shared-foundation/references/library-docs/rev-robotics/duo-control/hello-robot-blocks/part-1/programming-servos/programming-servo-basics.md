> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-servos/programming-servo-basics.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/programming-servos/programming-servo-basics.md).

# Programming Servo Basics

### Locating the Servo Blocks

Let's start by reviewing how to access servos within Blocks. At the top of the Categorize Blocks section there is a drop down menu for **Actuators**. When the menu is selected it will drop down two choices: **DcMotor** or **Servo**. Selecting Servo will open a side window filled with various servo related blocks.

<figure><img src="/files/XEiaAAKFCuQsl2VRdMjY" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The block above will change names depending on the name of the servo in a configuration file. If there are multiple servos in a configuration file the arrow next to test\_servo will drop down a menu of all the servos in a configuration.&#x20;

Different block options will appear when using a continuous rotation servo.
{% endhint %}

### Programming Position Movements

Let's start by programming our servo to rotate to the default 1 position!

From the Servo menu, we will primarily be using the block![](https://files.gitbook.com/v0/b/gitbook-legacy-files/o/assets%2F-M4_pJHI8HTuZFQTNfcy%2F-MWACJyDlnpPjKwQvDeW%2F-MWAc8IF4-_ItJzHXisV%2FServo%20-%20set%20to%200.svg?alt=media\&token=e58e949a-a8a7-4917-9427-4e737208328b)

Add this block to the op mode code within the ![](/files/tY0TC7HYPK1aLfK3tHbJ) **.**&#x20;

Click on the number block to change from <img src="/files/-MWAc8IF4-_ItJzHXisV" alt="" data-size="original"> to <img src="/files/-MWAcLYKFQSC3PM2Cbef" alt="" data-size="original"> **.**

<figure><img src="/files/Np2W5jpWPDrQxv3a2jh8" alt=""><figcaption></figcaption></figure>

Select **Save OpMode** in the upper lefthand corner in the programming interface.

### Quick Check!

Let's give our program a try. Take a moment to observe what happens.&#x20;

When running our program for the first time, we should have seen our servo move itself to position 1 and maintain that position. But what happens if we run it again? Does the servo move?

<details>

<summary>Running our program a second time</summary>

Likely, on a second run our servo did not move since it is already at the correct position. Now check what happens if you first manually rotate the servo while the robot is disabled. Once the code is activated again by pressing play we should see it move again!

**Note:** Servos are designed to maintain their position so long as the robot's program is enabled. Trying to forcibly move the servo while ON may damage it and is not recommended.

</details>

{% hint style="info" %}
If your servo did not move as expected, double check your wiring and port are correct compared to your configuration.
{% endhint %}

### Resetting Back to Zero

The intent of the <img src="/files/-MWAcLYKFQSC3PM2Cbef" alt="" data-size="original"> is to set the position of the servo. If the servo is already in the set position when a code is run, it will not change positions. Lets try adding another <img src="/files/-MWAc8IF4-_ItJzHXisV" alt="" data-size="original"> block and see what change&#x73;*.*&#x20;

In this case, we do not want our servo to reset to 0 every time our code repeats. Because of this where do you think we would snap in our  <img src="/files/-MWAc8IF4-_ItJzHXisV" alt="" data-size="original"> block?

Recall when we discussed the section marked by the <img src="/files/-MVRzzz2RWu0i_oNzqo3" alt="" data-size="original"> comment during [Programming Essentials](/duo-control/hello-robot-blocks/part-1/programming-essentials.md#comments). Since we only want our servo to reset ONCE we will request it do so during the initialization process when the code is first activated, but before play is pressed.&#x20;

Go ahead and click a ![](/files/UxxmWLcUAO6LZlEFvhDH) block into place to match the code below:

<figure><img src="/files/ZisPcqzIF4x01pbfJEpJ" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Try running this op mode on the test bed and consider the following question:

* What is different from the previous run?
  {% endhint %}

In many applications starting the servo in a **known state**, like at position zero, is beneficial to the operation of a mechanism. Setting the servo to the known state in the initialization ensures it is in the correct position when the OpMode runs.&#x20;

Take a moment to think about where setting the servo to a known state during initialization may be helpful before moving to the next section!
