> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/where-to-program/what-is-an-opmode.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/where-to-program/what-is-an-opmode.md).

# What is an OpMode?

## OpModes

**OpModes** (or operational modes) are computer programs that are used to customize or specify the behavior of a robot. Simply put, these are the programs we create!

The Robot Controller on the Control Hub stores and executes the OpModes. The Driver Hub then allows us to initialize, start, or stop these OpModes.&#x20;

In the SDK, there are two types of op modes: **autonomous (Auto)** and **teleoperation (TeleOp)**. Both types of op modes have initialization, start, and stop features on the Driver Hub.&#x20;

<figure><img src="/files/6pYiAbeYYfYsf1etl5C8" alt=""><figcaption></figcaption></figure>

You can see in the image above that the left arrow (green) allows for the selection of Auto programs while the right arrow (blue) shows the TeleOp list.&#x20;

Below shows an example of how your list of programs may appear:

<figure><img src="/files/RWtV16YiQg6WaFr3kU7E" alt=""><figcaption></figcaption></figure>

### Autonomous Timer

When an Auto mode is selected, a 30 second timer will appear next to the play button to count down while this program is active. This can be toggle off for testing!

<figure><img src="/files/YHec5FoOXrO86xxGEb3O" alt=""><figcaption><p>Countdown timer enabled</p></figcaption></figure>

<figure><img src="/files/QXXtCxEkIy7Y3oh3O8uf" alt=""><figcaption><p>Countdown timer disabled</p></figcaption></figure>

While an autonomous program is running, the robot will act independently without input from a gamepad. At the end of the 30 second timer the robot will automatically stop the code. If needed, a program can also be stopped early same as while running a TeleOp program.

<figure><img src="/files/gLRFZ0o4KotNMqtVK7yr" alt=""><figcaption></figcaption></figure>

### Selecting Auto vs. TeleOp When Making a Program:

For OnBot Java, what type of OpMode you are creating is selected while making a new file.

**Robot Controller App Version 10.2 and earlier:**

<figure><img src="/files/kxC95L4rGDjIxK6XLZRJ" alt=""><figcaption><p>Pre-10.3 menu for creating a new program</p></figcaption></figure>

**Robot Controller App Version 10.3 and newer:**&#x20;

<figure><img src="/files/n9kToRlkBy9iDZIadJbg" alt=""><figcaption><p>Version 10.3 and newer menu for creating a new program</p></figcaption></figure>

{% hint style="info" %}
As of version 10.3, when using a sample code in OnBot Java the "OpMode Type" may be automatically selected. This can still be changed before creating the OpMode.
{% endhint %}
