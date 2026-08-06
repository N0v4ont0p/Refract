> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-1.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-1.md).

# Part 1: Tackling the Basics

Now that we have our Control System all set up and ready to program it's time to get a full robot running, right?&#x20;

While we will be getting motors moving and sensors sensing during this section, it's important that we first start small. In this section, we'll be working with a simple test bed as we breakdown how to program some of the components that can be connected to the Control Hub.&#x20;

By tackling these components individually we'll be able to explore more of their capabilities, common uses, and discuss errors that may occur while working with a full robot.&#x20;

{% hint style="info" %}
During Hello Robot you will encounter sections called **"Quick Check!"** These pauses are intend to be moments to think deeper on a topic or to self-check your understanding as you progress. It's is expected that the completion of Hello Robot may take multiple days, meetings, or classes.
{% endhint %}

## Quick Check!

As mentioned, during this section we will be focus first on the concept of testing. Why do you think testing might be important in robotics?

<details>

<summary>Why do you think testing might be important in robotics?</summary>

Testing before a design is put into use, or as it is being constructed, helps to proactively identify, isolate, and correct potential issues.&#x20;

**Think about it this way:**

Imagine spending all day working on building an arm for your robot so it can climb. The design is a little complex, but after an hour or so you have it connected to your robot and everything program.&#x20;

You go to turn it on for the first time and.... the motor does not move. You can't tell because of where the motor sits if it is damaged or if something is tightened too much preventing it from moving. The rest of the day is spent taking the arm back off to check and repair.

Now think about how things may have gone if we tested the arm before it was attached to the robot. We don't need everything else to move, just a test code to move its motor. Might save us some time right?

</details>

## Building a Test Bed&#x20;

One of the best practices to get into the routine of is testing all your components individually when they are first received. That's where out test bed comes into play. For our test bed we will be sticking to the basics with our components connected directly to our Control Hub rather than something like a Servo Power Module or Expansion Hub. If desired, we could add some mechanical parts, such as a servo horn or wheel, to aid with visualizing our testing, but this is not required.&#x20;

in this tutorial we'll be using our test bed to learn about programming basics, however it is highly encourage to maintain a test bed for future testing.

{% hint style="info" %}
Remember when testing a component there may be multiple points of failure such as the port, wire, program, or device itself. Utilizing a test bed helps to narrow down those failure points by making it easier to test and compare in a system's simplest state.
{% endhint %}

<details>

<summary>Click to learn more about how a test bed may used in real world applications!</summary>

A **test bed** is a testing environment for hardware and software components, commonly used in the engineering world. Test bed applications includes a broad range of different equipment and measurement testing. In some cases a test bed is a piece of equipment for testing a specific product, in other cases it is a system of components that create a testing environment. Regardless, the end goal of a test bed is to ensure a component is working before it is used for its intended purpose.&#x20;

</details>

To create our test bed for this tutorial you will need the following. The names we used in our configuration are included:

<table><thead><tr><th width="104"></th><th>Component</th><th>Configuration Name</th></tr></thead><tbody><tr><td>1</td><td>Control Hub</td><td></td></tr><tr><td>2</td><td>Core Hex Motor</td><td>test_motor</td></tr><tr><td>3</td><td>Smart Robot Servo</td><td>test_servo</td></tr><tr><td>4</td><td>REV Touch Sensor</td><td>test_touch</td></tr><tr><td>5</td><td>Color Sensor V3</td><td>test_color</td></tr><tr><td>6</td><td>Battery</td><td></td></tr></tbody></table>

<figure><img src="/files/a6cIUhD2JixwBMG4yMZb" alt=""><figcaption></figcaption></figure>

The design of a test bed depends on the use case and available resources. For instance, one of the design requirements for the test bed featured here was accessibility. Notice that the placement of the hardware components on the Extrusion allows for the actuators, sensors, and Control Hub to be removed or swapped out with ease.&#x20;

{% hint style="success" %}
Be sure to complete your configuration on the Driver Hub once you have assembled your test bed.
{% endhint %}

There are other minor, but important, design considerations to make for a test bed. For example, when adding an actuator to a test bed consider the following questions:

* **What level of constraint does the actuator need?** One of the benefits of creating a test bed for motors, or other actuators, is that the motors can be properly constrained during the testing process. In this case providing basic motion support and constraint is valuable.&#x20;
* **How will you be able to tell the behavior of the actuator?** The example test bed uses a wheel with a zip tie to help users visualize the behavior of the motor. Tape or other markers can be used, as well.&#x20;

{% hint style="info" %}
Well a test bed is recommended, in the case of time restrictions, space, or other limitations, individual components may be added or removed during each section of Hello Robot. Make sure moving components, such as motors or servos are ALWAYS secured while running, even at low speeds.
{% endhint %}
