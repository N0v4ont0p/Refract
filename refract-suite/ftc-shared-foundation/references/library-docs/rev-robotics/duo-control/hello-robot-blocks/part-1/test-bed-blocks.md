> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/test-bed-blocks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-1/test-bed-blocks.md).

# Creating an OpMode - Blocks

The time has come to create our first OpMode. We want to make sure to choose a clear and unique name each time we make a program. This will help us to find it again later or to communicate with teammates who may also be driving the robot.&#x20;

In the programming world, there are common naming conventions that have been established to denote variables, classes, functions, etc. OpModes share some similarities to classes, a program-code-templat&#x65;**.** Thus the naming convention for OpModes tends to follow the naming convention for classes, which has the first letter of every word is capitalized.&#x20;

{% hint style="info" %}
While there are standardized naming conventions in programming, at the end of the day you will want to pick something that makes sense to YOU or your team. This might include having your name, team name, a school class period, or similar in your name.

Your OpMode name should not be the same as a created variable name.
{% endhint %}

To start, in the REV Hardware Client, select the "Program and Manage" menu tab. In the upper left-hand corner of there is a "Create New OpMode" button, click it:

<figure><img src="/files/Y2HNYDp35PuWOESu1uMp" alt=""><figcaption></figcaption></figure>

Clicking the "Create New OpMode" button will open a new window to name and, if applicable, select a sample template for a program. For this guide use the default "BasicOpMode" sample and name the OpMode **HelloRobot\_TeleOp** as shown in the image below.&#x20;

<figure><img src="/files/WyNRPxIdAvEwRVUQewlo" alt=""><figcaption></figcaption></figure>

Once the OpMode has been named click 'OK' to proceed forward.&#x20;

Creating an OpMode will open up the main Blocks programming page. Before moving on to programming, take some time to learn and understand the following key components of Blocks featured in the image below:&#x20;

<figure><img src="/files/fwhwBJfkLKsm7Wi8OdfU" alt=""><figcaption></figcaption></figure>

1. **Save OpMode** - Click this button to save an OpMode to the robot. It is important to save the OpMode any time you stop working on a code, so that progress is not lost. Blocks **does not** have an autosave feature!
2. **TeleOp/Autonomous** - This section of blocks allows users to change between the two types of OpMode: teleop and autonomous.&#x20;
3. **Categorized Blocks** - This section of the screen is where the programming blocks are categorized and accessible. For instance, clicking **Logic** will open access to programming blocks like if/else statements.&#x20;
4. **Programming Space** - This space is where blocks are added to build programs. Blocks not currently in the use may be dragged off to the side to be clicked back in later or deleted.
5. **Greeting Message** - This intro information message may appear when creating a new, empty OpMode. Clicking the ? icon will close this message.

{% hint style="danger" %}
Remember a [configuration](/duo-control/hello-robot-blocks/configuration.md) needs to be completed first before programming! Some blocks or dropdown menus may be hidden from the side menu until a configuration is made active.
{% endhint %}

## Opening Java Viewer:

Blocks includes a nifty tool to view how our code would appear if converted to Java. You can click the button on the far right side to open or close this viewer.

<figure><img src="/files/0Q4cOfEoYHcoeWeQLUPJ" alt=""><figcaption></figcaption></figure>

While this feature is designed to aid in the transition between programming platforms, some edits may be required for the Java code to properly compiled if added to an OnBot Java OpMode.
