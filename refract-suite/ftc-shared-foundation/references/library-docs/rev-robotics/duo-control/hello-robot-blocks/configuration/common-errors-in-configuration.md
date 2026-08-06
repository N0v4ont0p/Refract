> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/configuration/common-errors-in-configuration.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/configuration/common-errors-in-configuration.md).

# Common Errors in Configuration

While there are many errors one may run into in the programming and software world we're going to focus for now on the two major errors that may occur when hardware mapping.

* **Interface Errors** - errors between how an interface should work and how it actually behaves
* **Runtime Errors** - errors that occur when a program is being executed                                                 &#x20;

## Interface Errors

**Interface errors** occur in the SDK when the parameters of the SDK interface are not met. In the hardware mapping process, the most common interface error occurs within the Blocks Programming Tool.&#x20;

Blocks is designed to simplify the user experience by automatically handling the conversation of the hardwareMap to pre-named blocks. This means while no configuration is active the applicable block options are removed from the dropdown menu on the side. Similarly, if there are only sensors configured in your file then Blocks will not show the blocks used for motors to minimize the sidebar.&#x20;

For this reason it is important to create a configuration file BEFORE trying to code!

Below you can see a comparison of Blocks when a configuration file is not selected (left) versus when one is active (right):

<figure><img src="/files/ZQscAMu3G0qP2LmKE9zM" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you have started a program before configuring or have the wrong configuration selected, activate the correct configuration file on the Driver Hub then reopen your Blocks program after the Robot Controller has restarted.
{% endhint %}

## Runtime Errors

Within the SDK **runtime errors** occur during initialization or run. One of the most common runtime errors within the Control Hub can be seen below:

<figure><img src="/files/CIn86a45OD8AZeJFs11X" alt=""><figcaption></figcaption></figure>

&#x20;There are a few different reasons this error typically occurs:

* No configuration file is currently active or created
* The incorrect configuration file is active
* There is a mismatched name between the configuration file and code (ex: rightmotor vs right\_motor)

What results is when the program begins the robot is forced to stop running when the first hardware device is not properly identified. That first hardware device is the one indicated in the error. If there are multiple issues the next will show once the initial is fixed.&#x20;

Because Blocks handles importing the hardwareMap for you it will additionally show an error when opening a saved OpMode while the wrong configuration file is selected:

<figure><img src="/files/A0284FTNHsVuX5KEDKz1" alt=""><figcaption></figcaption></figure>
