> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/configuration/common-errors-in-configuration.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/configuration/common-errors-in-configuration.md).

# Common Errors in Configuration

While there are many errors one may run into in the programming and software world we're going to focus for now on the two major errors that may occur when hardware mapping.

* **Interface Errors** - errors between how an interface should work and how it actually behaves
* **Runtime Errors** - errors that occur when a program is being executed                                                 &#x20;

## Interface Errors

**Interface errors** occur in the SDK when the parameters of the SDK interface are not met. These errors are more common in Blocks due to it handling much of the hardwareMapping process for the user.

Below you can see a comparison of Blocks when a configuration file is not selected (left) versus when one is active (right):

<figure><img src="/files/ZQscAMu3G0qP2LmKE9zM" alt=""><figcaption></figcaption></figure>

## Runtime Errors

Within the SDK **runtime errors** occur during initialization or run. One of the most common runtime errors within the Control Hub can be seen below:

<figure><img src="/files/CIn86a45OD8AZeJFs11X" alt=""><figcaption></figcaption></figure>

&#x20;There are a few different reasons this error typically occurs:

* No configuration file is currently active or created
* The incorrect configuration file is active
* There is a mismatched name between the configuration file and code (ex: rightmotor vs right\_motor)

What results is when the program begins the robot is forced to stop running when the first hardware device is not properly identified. That first hardware device is the one indicated in the error. If there are multiple issues the next will show once the initial is fixed.&#x20;

A similar error may occur when using OnBot Java, which will appear like the following:

<figure><img src="/files/viWaVtrBAnw1dytOKFJD" alt=""><figcaption></figcaption></figure>

Similarly, this error is likely due to a typo or mismatched name between the program and configuration file. I can see in the error that I've accidentally set my motor to be named "test\_moto" instead of "test\_motor"!

### Compiling Errors:

There are many errors that could appear while compiling, however let's look at a common one for the hardwareMap.

<figure><img src="/files/tM2ahUmkaqTuDxQO0KhB" alt=""><figcaption></figcaption></figure>

Looking at line 48 of the program we can see the following:

<figure><img src="/files/82d1AFYKJvjyJyPd6PaR" alt=""><figcaption></figcaption></figure>

In this scenario, the name from the configuration file is correct within the string, however the variable name is wrong.&#x20;

{% hint style="success" %}
Remember to click the "Build Everything" button to compile your program after making changes!

![](/files/0qDGb0fOEU7ujW8tZKZO)
{% endhint %}
