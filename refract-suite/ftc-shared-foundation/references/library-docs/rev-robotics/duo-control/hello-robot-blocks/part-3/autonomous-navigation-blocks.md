> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks.md).

# Drivetrain Encoders - Blocks

Moving the motors to a specific position, using the encoders, removes any potential inaccuracies or inconsistencies from using Elapsed Time. The focus of this section is to move the robot to a target position using encoders.&#x20;

## Setting up the Drivetrain Encoders

{% hint style="info" %}
For this tutorial, our OpMode is named HelloRobot\_Encoder!
{% endhint %}

Before diving in too far, recall that for certain [drivetrains](/duo-control/hello-robot-blocks/part-2.md), like the [Class Bot V2](https://docs.revrobotics.com/duo-build/ftc-starter-kit-class-bot), one of the motors needs to be reversed as the motors are mirrored. In our example, we are adding the <img src="/files/-MW6L1g4Y8GSBICwwFHF" alt="" data-size="original"> block under the <img src="/files/-MVRzzz2RWu0i_oNzqo3" alt="" data-size="original">.&#x20;

<figure><img src="/files/gNQlbMUdnj5xcAQdU4Ml" alt=""><figcaption><p>Setting the rightmotor to run in reverse</p></figcaption></figure>

### RUN\_TO\_POSITION

As introduced in [Using Encoders](/duo-control/hello-robot-blocks/part-3/using-encoder.md#using-run_to_position), using `RUN_TO_POSITION` mode requires a three step process.&#x20;

The **first step** is setting target position. To do so, grab the <img src="/files/-MYGpj87ESnvB0Mbaqbo" alt="" data-size="original">  block and add it to under the <img src="/files/-MWPfpmWuWVqh1EweC06" alt="" data-size="original"> comment. For this example, we are setting our position after pressing Initialize, but before we hit Play on the Driver Hub.

<figure><img src="/files/ABzpOU42OoOs5UcqDbNA" alt=""><figcaption></figcaption></figure>

If we want our robot to travel a specific distance we will need to do a bit of math beforehand to calculate the TargetPosition. But for now let's start simple by setting the target position to 1000 ticks.&#x20;

<figure><img src="/files/JVUcjbhuwfr3haFXVJvD" alt=""><figcaption><p>Adding TargetPosition for the drivetrain motors</p></figcaption></figure>

The next step is to set both motors to the `RUN_TO_POSITION` mode. Place the <img src="/files/-MYGpV5c0A6R6UP0YKgC" alt="" data-size="original"> block beneath the <img src="/files/-MYGq13GHps2CyeLWbZt" alt="" data-size="original"> block.

<figure><img src="/files/UAK7Eaq3b26PVsqFAbVA" alt=""><figcaption><p>Changing the motors to RUN_TO_POSITION</p></figcaption></figure>

{% hint style="info" %}
Order matters! The TargetPosition block must come before RUN\_TO\_POSITION mode is set or it will result in an error.&#x20;
{% endhint %}

As mentioned, normally there would be more math involved to help determine how fast the motors should move to reach the desired position. But for testing purposes, we are going to start by keeping it simple!

&#x20;Add the <img src="/files/-MVwRA9auYOOqnGmzAX7" alt="" data-size="original"> block beneath the <img src="/files/-MYGpV5c0A6R6UP0YKgC" alt="" data-size="original"> block. Let's go ahead and change the duty cycle (or power) of both motors to 0.8, instead of 1.&#x20;

<figure><img src="/files/e4EChAgQq2cWtlYQJrhe" alt=""><figcaption><p>Setting the power for the motors</p></figcaption></figure>

### Quick Check!

Save your OpMode and give it a test. What happens once you press play? What happens if you stop the program then start it again?&#x20;

<details>

<summary>What happens when testing?</summary>

Likely your motors turned on when testing out the code to spin until they've reached the set position.&#x20;

Some may have turned off once the position was reached, but you may also experience the motors twitching or making small adjustments in an attempt to reach the position. Then when starting the code again, the motor either continued twitching or did not move at all.

Recall we may need to reset our encoder to zero before running a program! The motor will continuously try to adjust until it hits the set position, but if it's already there it won't move!

Adjusting the power may help prevent the motor from overshooting the position and needing to repeatedly adjust.&#x20;

</details>

### STOP\_AND\_RESET\_ENCODERS

For our demo code we will want to request our motors reset their encoders during the initialization process of the program.&#x20;

<figure><img src="/files/mMET2W1BUNu4kA798lkz" alt=""><figcaption><p>Adding a block to STOP_AND_RESET_ENCODER</p></figcaption></figure>

## Setting up the whileLoop

Let's say we want our program to run only for however long it takes for the motors to reach designated position. Or maybe we intend for the robot to do something else after reaching the destination. For this we will need to edit our whileLoop block!

<figure><img src="/files/wx5RE04jv3jSPakyRIaR" alt=""><figcaption><p>In this section we will edit our whileLoop</p></figcaption></figure>

{% hint style="info" %}
Even though we are ending a new exit case for our loop, we must always have our call to check opModeIsActive or our program will instantly timeout!
{% endhint %}

Grab an <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block from the logic menu and add it to the while loop. On the left side of the <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block add the <img src="/files/-MYLqJ0o25l0qXexhQAN" alt="" data-size="original">block. On the right side add the <img src="/files/-MYprDjxWilLiLPAqPut" alt="" data-size="original"> block.&#x20;

<figure><img src="/files/fmP3XfV5iMRZVOuDugZx" alt=""><figcaption><p>The call motor block is under the DcMotor menu</p></figcaption></figure>

Embed the <img src="/files/-MYprs4f0C8BmAp0-ukL" alt="" data-size="original"> in another <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block. Place the <img src="/files/-MYprs4f0C8BmAp0-ukL" alt="" data-size="original"> on the right side of the <img src="/files/-MW9yJdVdzRolyWei1gK" alt="" data-size="original"> block. Our call for the OpMode will go in the lefthand side slot.

<figure><img src="/files/qFqieLKikhQ03n3WT4HR" alt=""><figcaption><p>Full logic statement for the whileLoop</p></figcaption></figure>

Save your OpMode and give it a try!&#x20;

As soon as the motors hit the desired position the program will end instead of continuously run in the event they do not perfectly hit the position.&#x20;

{% hint style="info" %}
Right now the while loop is waiting for the right and left motors to reach their respective targets. There may be occasions when you want to wait for both motors to reach their target position, in this case the <img src="/files/-MWB9-FbRpvUKsRz3Tbi" alt="" data-size="original"> can be used such as:  <img src="/files/-MYpwslGYPymyht-7Rwu" alt="" data-size="original">
{% endhint %}
