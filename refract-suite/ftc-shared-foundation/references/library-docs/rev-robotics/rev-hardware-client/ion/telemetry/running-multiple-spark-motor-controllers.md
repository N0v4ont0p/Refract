> Source: https://docs.revrobotics.com/rev-hardware-client/ion/telemetry/running-multiple-spark-motor-controllers.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/ion/telemetry/running-multiple-spark-motor-controllers.md).

# Running Multiple SPARK Motor Controllers

{% hint style="danger" %}
Those using REV ION products on REVLib 2026 or newer must use [REV Hardware Client 2](https://docs.revrobotics.com/rev-hardware-client-2).
{% endhint %}

This guide will help illustrate how to use the REV Hardware Client to run multiple ION motor controllers and motor pairs over CAN using various modes, including position, velocity, and duty cycle.

### Running One SPARK Motor Controller

1. Connect your SPARK to the REV Hardware Client via a USB-C cable plugged into the SPARK itself or another device on the CAN network. If available, other CAN Devices will appear on the left under "Connected Hardware". In our example, we have plugged into the Power Distribution Hub. \
   \
   Then, click the "Telemetry" tab to continue.\
   \
   *Note: For best results, ensure all devices have the latest firmware installed.*<br>

{% hint style="danger" %}
As a safety precaution, USB control is disabled on all REV Devices if a roboRIO has been detected at any time while the control system is on. To resolve the lockout, power cycle your control system after disconnecting the roboRIO.
{% endhint %}

<figure><img src="/files/u4UWGmDQEKQTzyKKSR0h" alt=""><figcaption></figcaption></figure>

2. Here, all available devices should be visible on the left. Click the first device you wish to configure.

<figure><img src="/files/TlZ2tKn4TyReA8uCpq50" alt=""><figcaption></figcaption></figure>

3. While the motor is running, you can select different signals to display on the graph, providing valuable telemetry data for prototyping or troubleshooting. To track key metrics, select Voltage, Primary Encoder Position, and Primary Encoder Velocity to visualize these signals on the graph during operation.

<figure><img src="/files/ZWLQc250RIxcXVaSHF0T" alt=""><figcaption></figcaption></figure>

4. After selecting your signals, click the "Start Graph" button to begin data collection before clicking the "Run Motor" button.

{% hint style="warning" %}
Below "Run Motor," you'll find the Mode and Setpoint settings, which determine the motor's behavior while running. For this guide, leave the Mode at Percent and the Setpoint at 0.05. Ensure the motor is securely fastened before clicking "Run Motor."
{% endhint %}

5. Congratulations, you've successfully run your SPARK MAX through the REV Hardware Client!

<figure><img src="/files/pxZW2TMDomV3MINJ0QUh" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you are only using multiple SPARK MAXs and a power source, you can terminate both ends of your CAN Bus with 120Ω resistors!
{% endhint %}

### Running Multiple SPARKs

1. With the Power Distribution Hub and all SPARK devices wired, updated, and connected via CAN, plug the provided orange USB-C cable into the Power Distribution Hub. You should then see all the respective hardware appear on the left. Click the "Telemetry" tab to continue.

{% hint style="danger" %}
A roboRIO lockout can occur when it is active on the CAN bus while the REV Hardware Client is connected. To resolve this issue, power cycle all SPARK motor controllers after disconnecting the roboRIO.
{% endhint %}

<figure><img src="/files/2MkvJ5TeZmDLPCWcgMTi" alt=""><figcaption></figcaption></figure>

2. Here, all available devices should be visible on the left. Click the first device you wish to configure.

<figure><img src="/files/MZXqFJdImkVvOkAF5KSr" alt=""><figcaption></figcaption></figure>

3. After selecting your desired signals, click on the "Run Multiple" tab. You'll notice that our SPARK Flex is checked, meaning that it's ready to run. We need to check off the SPARK MAX so that both run at the same time. When you're done, click on the back button highlighted in orange to return to the Telemetry Devices tray.&#x20;

<figure><img src="/files/tZvEaDv8wLElI3WMM1yY" alt=""><figcaption></figcaption></figure>

4. In the previous step, we selected the signals for our SPARK Flex. The same needs to be done for our SPARK MAX, click on it to continue.

<figure><img src="/files/mMfj3Fu1KZfIWCpMO0U2" alt=""><figcaption></figcaption></figure>

5. After selecting your signals for the second motor controller, click on the *Run Multiple* tab.

<figure><img src="/files/ELK0Sa7y9lZf6a4ZhDRv" alt=""><figcaption></figcaption></figure>

6. After selecting your signals, click the "Start Graph" button to begin data collection before clicking the "Run Motor" button.

{% hint style="danger" %}
Below "Run Motor," you'll find the Mode and Setpoint settings, which determine the motor's behavior while running. For this guide, leave the Mode at Percent and the Setpoint at 0.03. Ensure the motor is securely fastened before clicking "Run Motor."
{% endhint %}

7. Congratulations, you've successfully run multiple SPARK Motor Controllers through the REV Hardware Client!

<figure><img src="/files/G9w2d5xYnRaJvQPJ2Y0Q" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you are only using multiple SPARK MAXs and a power source, you can terminate both ends of your CAN Bus with 120Ω resistors!
{% endhint %}
