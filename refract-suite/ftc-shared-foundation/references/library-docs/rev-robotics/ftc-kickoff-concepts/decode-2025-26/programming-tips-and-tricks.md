> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-tips-and-tricks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-tips-and-tricks.md).

# Programming Tips & Tricks

This page aims to provide some additional options for fine-tuning the program for the Starter Bot that are not included in the original example code. The variety of options provided here are intended to meet different team skill levels and offer additional flexibility in how teams approach the DECODE game.&#x20;

## Fine-tuning the Core Hex Feeder&#x20;

Let's first review the existing code for our Core Hex Feeder in the function to auto feed balls to the flywheel:

<figure><img src="/files/m5MgOXFxULi537e1t7Gk" alt=""><figcaption></figcaption></figure>

Currently, the Core Hex will wait until the flywheel is at least 50 ticks below the target velocity before it will start releasing the artifacts to be launched. However, there is no check for if the flywheel is too far above the target velocity. In this tutorial we'll add a max for this check to help further prevent the feeder from starting too soon.

To start, we can right click our blocks containing the check for the velocity and select "Duplicate". This will save us a couple steps of resetting up this portion of code when we are only making minor changes.

<figure><img src="/files/O9rSihudDchGtxL3Xb7K" alt=""><figcaption></figcaption></figure>

Next, we want to change this statement to check if the velocity is currently less than or equal to a value. Additionally, we can need to change the value to be bankVelocity plus a range. We can set this range a little higher to start.

<figure><img src="/files/diEAuN6CIApPL7JxUHNn" alt=""><figcaption></figcaption></figure>

Your team will want to use the telemetry on your Driver Hub to determine the appropriate window for both below and above the target velocity!

We can now add our two checks to an "and" statement. By right clicking the block, we can select to change the blocks's format to "External Inputs". This may help the final statement be easier to visually read.

<figure><img src="/files/DCEdRsKiZMmQuOr3ItxV" alt=""><figcaption></figcaption></figure>

Drag the existing check from the if/else statement to snap too this new "and" statement along with the new check.&#x20;

<figure><img src="/files/h86xrGHglQu4rT7XkBsR" alt=""><figcaption></figcaption></figure>

Lastly, we'll add this back to the if/else statement. Now the robot will check IF the flywheel's velocity is currently ABOVE or EQUAL TO 50 ticks below bankVelocity **and** BELOW or EQUAL TO 100 ticks above bankVelocity before allowing the Core Hex feeder to spin.&#x20;

<figure><img src="/files/6UFtdp6fhmqqQR46QORX" alt=""><figcaption></figcaption></figure>

This can be repeated for the farPowerAuto if desired. We recommend testing with your robot to further decide the appropriate range for the flywheel.&#x20;

## Using ElapsedTime with the Flywheel

When the flywheel first spins up, you may notice the first ball launched is stronger than those that follow, assuming the button is continuously held, or that the velocity of the flywheel jumps far above the set target. If the flywheel is set to spin without any balls being fed, the velocity will drop to be closer to the target once it has a couple seconds to adjust.&#x20;

By using ElapsedTime, we can build that buffer into our program to create more consistent launches. This may be especially beneficial during autonomous.&#x20;

### Creating a Launch Timer

{% hint style="success" %}
If you are modifying the example program that includes autonomous, this timer is already created!
{% endhint %}

First, under the "Variables" menu create a new variable called "autoLaunchTimer".&#x20;

<figure><img src="/files/usLLHslQcqWNA31ohxT1" alt=""><figcaption></figcaption></figure>

A "set autoLaunchTimer to" block will be snapped into our intialization section below the velocity targets.&#x20;

<figure><img src="/files/mIE8yB3qOZ1ywp3X86bP" alt=""><figcaption></figcaption></figure>

Under the "ElapsedTime" menu in the "Utilities" dropdown, grab a "new ElapsedTime" block to add to this variable.

<figure><img src="/files/rSVnIYfmjjASWkMwrfDW" alt=""><figcaption><p>ElapsedTime blocks location</p></figcaption></figure>

<figure><img src="/files/vvjW2YXfiO9UvgJFx0xb" alt=""><figcaption></figcaption></figure>

### Adding the Timer to the Launcher Functions

For this example, we'll start by adding the timer to our "bankShotAuto" function. Teams may consider adding it to their "farPowerAuto" function by repeating the process.

First, from the "ElapsedTime" menu add a call to reset the timer to the beginning of the function. The timer will need to be changed to "autoLaunchTimer" from the default.&#x20;

<figure><img src="/files/E2NUbKcyqBX2937acwaS" alt=""><figcaption></figcaption></figure>

When using "ElapsedTime" the timer begins at the start of the program when the timer is created. Because of this, we need it to reset when we want to use it since it may at different times or repeatedly through the program.&#x20;

### Adding a Timer Check to the Launcher Function

Right now there's a check in place for the Core Hex feeder to wait until the the velocity of the flywheel is at least within 50 ticks below the target velocity to release balls. We'll add the timer here as an additional check for the Core Hex to begin spinning.&#x20;

First we'll pull this check to the side to add to it for our if/else statement. To help with clarity, we can right click on the logic block and select "External Inputs" to change how this statement appears. It will not effect how the statement reads.

<figure><img src="/files/aHYYhgMdHEuReABwU2vN" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/H7mCghUhEjbysCAkGFIt" alt=""><figcaption><p>After changing to "external inputs"</p></figcaption></figure>

This statement can now be snapped into the beginning of an "And" logic block.&#x20;

<figure><img src="/files/NyjdtSYzhOl9PXVdBSCK" alt=""><figcaption></figcaption></figure>

On the otherside of our statement, another "greater than or equal to" logic block can be added an edited to appear the same as the first.

<figure><img src="/files/uVfhNr2JmxnQiax4OPSy" alt=""><figcaption></figcaption></figure>

On top, we'll add the "autoLaunchTimer" in milliseconds and below we'll add a number block to be filled in.

<figure><img src="/files/3l3mmGVWnu0N1E5YJk8H" alt=""><figcaption></figcaption></figure>

Adjusting the length of the timer will take some trialing to determine what is best. We recommend starting with 2 seconds (2000 milliseconds) to test.

This statement can be snapped back into the if/else statement and is ready to test.

<figure><img src="/files/WjEVlM0054r96FmBCfFQ" alt=""><figcaption></figcaption></figure>

## Using PID with the Flywheel

{% hint style="info" %}
When using the velocity blocks from the FTC SDK there is already PID calculations in place. This is intended for further fine tuning.&#x20;
{% endhint %}

{% hint style="warning" %}
This tutorial assumes teams are already comfortable with navigating Blocks in order to replicate the example provided. It is based off the example code that does not have autonomous.
{% endhint %}

### What is PID?

A PID controller is a common feedback controller. It's made up of three parts: proportional, integral, and derivative terms. The different terms can be used to aid with fine tuning movement depending on the end goal.

<details>

<summary>What is a feedback controller?</summary>

When powering a motor with just a specified voltage, this is called open loop control. In this situation, the motor gets power and there is no data received back from the motor to help us control it.  Open loop control is what we may use for a drivetrain, for example, since we are actively controlling and changing the motor's power with the joysticks.

Alternatively, if our goal is for the motor to go to a specific velocity or position, then we need some type of "feedback" from it. This is where the motor's built in sensors, or external sensors, come into play. They record data related to the motor's current actions then sends that information back to us. This let's us decide whether to apply more or less voltage, depending on what we want to achieve, to make more refined adjustments.&#x20;

This is called closed loop control or a feedback controller.

</details>

PID control may be used for a number of applications in robotics, from controlling elevators to precise arm movements.&#x20;

In this case, we want to use PID, specifically PIDF with F meaning feed-forward, to help our flywheel better reach the target velocity and reduce fluctuating in that velocity between launches.

### Proportional and Feed-Forward

For our flywheel, we'll be only using two components of PIDF: Proportional (P) and Feed-forward (F).

P, the **proportional gain**, is the primary factor of the control loop. This is multiplied by the error and that gain is added to the output. This does the heavy lifting of the motion, pushing the motor in the direction it needs to go.

F, **velocity feed-forward**, is used when using PID for velocity-based control rather than positional. The F parameter is multiplied by the velocity setpoint to achieve more consistent velocity control.

In short, our F value will help the flywheel motor reach our target velocity more precisely, compared to what you may see where its several ticks off. Meanwhile our P value will help the motor spin up faster to that target velocity between ball launches!

{% hint style="info" %}
If you're curious to learn more about PID and the math behind it, check out [WPILib's guide](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html)!
{% endhint %}

### PID Variables

In our program, we need to set up variables for our P and F during initialization. We will leave them set to 0 for now.&#x20;

<figure><img src="/files/PPIQ3YERMKkzMWkzl8oG" alt="" width="499"><figcaption><p>Adding the variables for PID</p></figcaption></figure>

### PID Math

Let's take a look at how the math appears in Blocks within our bankShotAuto function.&#x20;

<figure><img src="/files/fBO6k8zKZxoMGhxQTba4" alt=""><figcaption></figcaption></figure>

Notice our flywheel motor is now set to use "power" instead of "velocity". A "targetPower" has also been added here as a variable, but is not called during initialization.&#x20;

There are two parts to the calculation deciding the final power for the flywheel. Keep in mind this power will change as the robot launches balls since the goal of the feedback controller is to change the voltage provided.&#x20;

<figure><img src="/files/4hrn0lkPXn4h3AuM3m2F" alt=""><figcaption></figcaption></figure>

On the top line, once our feed-forward is set it will multiply with our determined bankVelocity.&#x20;

<figure><img src="/files/oaS8ygtrghM3PfEHGgoq" alt=""><figcaption></figcaption></figure>

On the bottom, our proportional value multiplies with the set bankVelocity minus the CURRENT velocity of the flywheel.&#x20;

These are then added together to determine the final targetPower to set the motor to.&#x20;

This same math can be used within the farPowerAuto function with the farVelocity target.&#x20;

<figure><img src="/files/r0IXEBiRxP7CeMTbLfYn" alt=""><figcaption></figcaption></figure>

### Tuning PID

With our math in place, it's time to determine our "f" and "p" values. Because of the nature of these motors and the SDK, this value will be very very small!

#### F Value

Start with "f" first. In our testing, we set ours to 0.0004 before making adjustments.&#x20;

<figure><img src="/files/6PDaEiC89HrAqJxqOhg6" alt=""><figcaption></figcaption></figure>

Save and test spinning the flywheel up to the bankVelocity using the auto feed option. Watch the telemetry on the Driver Hub screen to determine if this value should be changed. Once the velocity is consistently within 10 ticks of your target velocity, or what your team decides to be an acceptable range, you can move on to adding "p".&#x20;

#### P Value

For "p" we can also start with 0.0004. This is being used to help the flywheel get back up to speed after a disturbance or load so, after saving, set the robot up to launch a series of artifact balls.&#x20;

<figure><img src="/files/Jjo2nX64zscb3xLoYebC" alt=""><figcaption></figcaption></figure>

Tuning "p" may take more time. You should slowly increase the value until the flywheel accelerates quickly, returning to the desired velocity, but doesn't overshoot or oscillate too badly. If the flywheel fluctuates too much, it may feed balls too early for launch!

How quickly a team wants the flywheel to reach target velocity again may vary as more time may be safer to prevent overshooting, but too slow means longer cycle times. Once "p" has been set your PID is ready to go.

### Manual Control

If desired, teams may opt to use PID with their manual flywheel spin up as well. It's recommended to add an additional function when doing so as seen in the example below:

<figure><img src="/files/QxqgSdquBz9TUeMnUk47" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/V2okQWyptYo76goCfJdv" alt=""><figcaption></figcaption></figure>
