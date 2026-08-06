> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/welcome.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/welcome.md).

# Welcome to Hello Robot!

{% hint style="info" %}
The first few pages of Hello Robot are an introduction to the programming tools, configuration, and using a gamepad. Ready to jump right into building and programming? Click here to jump to the [Blocks Tutorial](/duo-control/hello-robot-blocks/part-1.md) or [here for the OnBot Java Tutorial](/duo-control/hello-robot-java/part-1.md)!
{% endhint %}

{% hint style="success" %}
The examples and screenshots for this tutorial are completed using a Windows computer, however the Control Hub can be programmed using a Chromebook or a Macbook. Check out "[Where to Program"](/duo-control/hello-robot-blocks/where-to-program.md) for more information on getting started.
{% endhint %}

## Hello Robot - Choosing Your Path

In almost every programming class for the last 50 years, the first program students learn how to write is "Hello World". This program, and its variations, teach the basics of a new programming language, resulting in code that when run outputs the text "Hello World". Through this basic exercise structure and syntax, or formatting, are taught in a simple code to get students up and running quickly!

While we could display "Hello World!", or in this case "Hello Robot!", on our Driver Hub it may not be enough to help you and your team to get started. Instead, Hello Robot is intended to act as an introduction to the REV Control System. Through this tutorial you will learn the basics of configuration, programming, and utilizing sensors, motors, and servos.&#x20;

There are two major sections of this tutorial:

* Part 1: Building a Test Bed- This section makes use of a basic test bed built of a Control Hub, motor, servo, and touch sensor. Together we will take a look at how to program these devices and discuss the basics of Blocks and OnBot Java!
* Part 2: Robot Control- In this section we will be working to get a robot up and moving using a controller, as well as a more detailed look at sensors and encoders.

{% hint style="info" %}
If you are new to programming or the REV Control System we recommend that you follow through the whole guide to learn how to properly utilize the system.&#x20;

This guide is intended to be used with the Control Hub and Driver Hub.
{% endhint %}

Before diving in, let's discuss the two program language options available for Hello Robot!

## Programming Tools&#x20;

There are two programming languages available to use directly on the Control Hub through either the REV Hardware Client or when using the web browser interface. Additionally, the Control Hub is compatible with Android Studio for those interested in more advanced programming options.&#x20;

Choosing the appropriate programming tool or language can be one of the most crucial decisions a programmer can make. Thankfully the Software Development Kit (SDK) of the Control Hub has been designed to help new programmers find a starting point and transition to new levels when they're ready.&#x20;

The following is a breakdown comparison of the available languages and tools:

|  Basic | Intermediate |    Advanced    |
| :----: | :----------: | :------------: |
| Blocks |  Onbot Java  | Android Studio |

Take some time to read through the following sections comparing each option to help determine the best option for you or your team:

### Blocks&#x20;

The Blocks Programming Tool is a drag-and-drop programming tool available directly through the Control Hub. You may recognize it as being similar to other Scratch-based programming languages, such as the blocks coding used in *FIRST* LEGO League.&#x20;

<figure><img src="/files/T5nrhfOxGuheO1RGHAmj" alt=""><figcaption></figcaption></figure>

Blocks was created to cater to users who have little to no experience programming. Like other visual programming tools, Blocks is a collection of preset code snippets that users can drag-and-drop into the appropriate code line.  As you gain more confidence and familiarity with programming, there is a built in option to show the Blocks code in Java's syntax by clicking the "Show Java" button.&#x20;

### OnBot Java

OnBot Java is a text-based programming tool based on a modified version of Java that is accessible directly through the Control Hub!

<figure><img src="/files/EWAQH3m1TLOz3XsIskpx" alt=""><figcaption></figcaption></figure>

OnBot Java is great for programmers with basic to advanced Java skills who would like to write text-based op modes. OnBot Java shares some of insulative properties of Blocks, but gives you access to the more complicated elements of the SDK libraries. For instance, OnBot requires users to make calls to classes like the hardwareMap, which are hidden within the Blocks code snippets.&#x20;

### Android Studio

{% hint style="info" %}
Hello Robot is not available for Android Studio, but it is important to be aware of all the options available!
{% endhint %}

An advanced integrated development environment for creating Android apps. This tool is the same tool that professional Android app developers use. Android Studio is only recommended for advanced users who have extensive Java programming experience.

![](/files/-MA1mKiPnGaeWa4lqwFP)

Android Studio allows programmer with an advanced understanding of Java a more powerful development environment to work in. It offers enhanced editing and debugging features not available with OnBot Java or Blocks. It also allows programmers the ability to work with 3rd Party libraries not included within the SDK. However, Android Studio is not a web-based software and will need a dedicated laptop to run on.&#x20;

To learn about how to properly download and work with Android Studio please visit the [FTC Wiki. ](https://ftc-docs.firstinspires.org/programming_resources/android_studio_java/Android-Studio-Tutorial.html)

## Blocks or OnBot Java?

Once you've decided which programming tool you would like to use you can click the link below to go to the appropriate start for Hello Robot!

|  [Hello Robot - Blocks](/duo-control/hello-robot-blocks/where-to-program.md)  |
| :---------------------------------------------------------------------------: |
| [Hello Robot - OnBot Java](/duo-control/hello-robot-java/where-to-program.md) |
