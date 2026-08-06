> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/test-bed-onbot-java.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1/test-bed-onbot-java.md).

# Creating an OpMode - OnBot

The time has come to create our first OpMode. We want to make sure to choose a clear and unique name each time we make a program. This will help us to find it again later or to communicate with teammates who may also be driving the robot.&#x20;

In the programming world, there are common naming conventions that have been established to denote variables, classes, functions, etc. OpModes share some similarities to classes, a program-code-templat&#x65;**.** Thus the naming convention for OpModes tends to follow the naming convention for classes, which has the first letter of every word is capitalized.&#x20;

{% hint style="info" %}
While there are standardized naming conventions in programming, at the end of the day you will want to pick something that makes sense to YOU or your team. This might include having your name, team name, a school class period, or similar in your name.

Your OpMode name should not be the same as a created variable name.
{% endhint %}

To start, let's take a look at the OnBot Java layout in the REV Hardware Client:

![](/files/-MO3EovLwi7VQLDCRl2t)

1. **Create New OpMode** - The plus sign button opens up a window to create a new OpMode.
2. **Project Browser Pane** - This pane shows all the Java project files on the Robot Controller.&#x20;
3. **Source Code Editing Pane** - This is the main code editing area
4. **Message Pane** - This pane provides information on the success or failure of code builds, as well as where to check for errors after attemping a build
5. **Build Everything** - Builds ALL of the .java files on a Robot Controller.&#x20;

{% hint style="info" %}
Selecting to "Build Everything" will attempt to compile ALL your OnBot Java files. Errors may appear for incomplete or test files along with the active file.

To temporarily disable an OpMode, right click the file name and select "Disable / Comment":

![](/files/Qa1zdylpbkoNPwCNpx6n)&#x20;

OpModes may be reenable the same way!
{% endhint %}

Select the **Create New OpMode** button. This will open the **New File** window.&#x20;

{% hint style="info" %}
The 10.3 version of the Robot Controller App/Driver Station App released in June 2025 introduces a new interface for creating an OnBot Java file. Both versions are available to reference in the tabs before, but double check your version number before proceeding!
{% endhint %}

{% tabs %}
{% tab title="Pre-10.3 Creating an OnBot Java File" %}
There are a lot of things we can modify while setting up our OpMode, such as the name, sample in use, and kind of OpMode. For Hello Robot, use the following settings for reference:

<figure><img src="/files/Qr141jHY3CIARcMUo7ge" alt=""><figcaption></figcaption></figure>

* **File Name:** HelloRobot\_TeleOp
* **Sample:** BlankLinearOpMode&#x20;
* **OpMode Type:** TeleOp
* **Setup for Configured Hardware:** on

**Setup Code for Configured Hardware** is an incredibly useful tool that allows for OnBot to help create the hardwareMap based on the current active configuration!&#x20;

Your intended configuration file should be active BEFORE creating an OpMode using this feature.&#x20;

<figure><img src="/files/tFiz27TcROg23ByF1uJJ" alt=""><figcaption><p>HelloRobot_TeleOp created with the Setup Code for Configured Hardware active</p></figcaption></figure>

Once the proper settings have been choose, select "OK" to create the OpMode!
{% endtab %}

{% tab title="Creating an OnBot Java File 10.3" %}
There are a lot of things we can modify while setting up our OpMode, such as the name, sample in use, and kind of OpMode. For Hello Robot, use the following settings for reference:

<figure><img src="/files/vCS6HFxB7Da6n9PyJBHQ" alt=""><figcaption><p>OnBot Java new file menu in 10.3</p></figcaption></figure>

* **File Location:** org/firstinspires/ftc/teamcode
* **File Type:** Blank OpMode - Linear OpMode
* **File Name:** HelloRobot\_TeleOp.java
* **OpMode Type:** TeleOp
* **Add generated code for configured hardware:** on

**Note:** There is a known bug in v10.3 preventing the "Add generated code for configured hardware" option from working as expecte&#x64;**.**&#x20;

The following will need to be manually added to match Hello Robot's tutorial:

<figure><img src="/files/NjOkqBfqGcxg5syK1OKI" alt=""><figcaption><p>Hardware mapping in OnBot Java</p></figcaption></figure>

**Sample Codes:**

In the 10.3 version of the Robot Controller App, samples and blank templates have been separated to make navigation easier.&#x20;

To use a sample code change "File Type" to "Example OpMode" then select the desired sample from the dropdown. This will autofill the "File Name" and "OpMode type", but will disable the option to "Add generated code for configured hardware".

<figure><img src="/files/i44HVIWhExilkE6JkmP8" alt=""><figcaption><p>Using a sample code in 10.3 OnBot Java</p></figcaption></figure>
{% endtab %}
{% endtabs %}
