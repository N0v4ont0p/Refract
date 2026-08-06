> Source: https://docs.revrobotics.com/rev-hardware-client/ion/pneumatic-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/ion/pneumatic-hub.md).

# Pneumatic Hub

{% hint style="danger" %}
Those using REV ION products on REVLib 2026 or newer must use [REV Hardware Client 2](https://docs.revrobotics.com/rev-hardware-client-2).
{% endhint %}

The REV Hardware Client has three tabs to manage different features of the Client. The Hardware Tab is where supported hardware devices are managed. The Downloads Tab allows for the downloading of supported device software for updating when offline. The About Tab has information on what devices are supported, updating the REV Hardware Client, and having issue reporting.&#x20;

## Basic Tab

The Basic Tab is used to set the most common parameters for the Pneumatic Hub. You can also view and clear sticky faults here.

<figure><img src="/files/uj8rQzMkBKZU2gHi2ySA" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Sticky Fault - an indicator there was a fault that will stay until the fault has been cleared manually.&#x20;
{% endhint %}

<figure><img src="/files/LTae2TyWBLTT1HjGjInr" alt=""><figcaption></figcaption></figure>

## Operating your pneumatics system without a roboRIO&#x20;

Using the REV Hardware Client, you can completely operate and test your pneumatic system without needing a roboRIO or software. Here are some useful applications that can help your team:&#x20;

* Testing your pneumatic system in a bench top setting&#x20;
* Testing the pneumatic system on your robot without the need for software support (e.g. allowing your build team to test the pneumatics while your programmers are busy).&#x20;
* Using pneumatics in your quick and early prototypes during the beginning of the build season&#x20;
* Using the telemetry tab on the Hardware Client, you can see if you have leaks in your systems or check how much pressure you lose during normal operation without needing to write extra software. (An analog pressure sensor is needed).
