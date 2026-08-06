> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system.md).

# General Troubleshooting

One of the key aspects of troubleshooting is understanding the most common issues that occur in a system. Once those problems, and their indicators, are defined a flow has to be created. For example, a check engine light in a car indicates any number of issues. When a cars check engine light comes on, a mechanic pulls the codes from the car to narrow down the issue to a specific part of the engine. Even if the code leads to a specific part of the engine, like the transmission, it is not always indicative of the exact problem. However, there is a process flow. Each step narrows down the problem to a potential solution. Troubleshooting the REV Control system is no different!&#x20;

{% hint style="warning" %}
The status LED is the REV Control System equivalent to the check engine light mentioned in the example. *Visit the* [*LED Blink Code*](/duo-control/troubleshooting-the-control-system/led-blink-codes.md) *section to understand what each code is and what it indicates.*&#x20;
{% endhint %}

Many issues can be solved by systematic troubleshooting without needing to contact REV Support. Take a look at the troubleshooting tips below for help in determining the cause of the issue you are seeing. Should you need to contact us, describing the steps you've taken in detail will help us get you up and running quickly. The section is divided into general best practices, Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) troubleshooting and Expansion Hub ([REV-31-1153](https://www.revrobotics.com/rev-31-1153/)) troubleshooting.&#x20;

## General Best Practices &#x20;

Before diving into common troubleshooting paths its important to understand the general guidelines, or best practices, for Control System Health.

* **Charge the Battery** - While a charged battery and phone are crucial to a healthy control system in general; it is also helpful to ensure batteries and phones are charged before a match.&#x20;
* **Update** -  The applications, firmware, and operating system have periodic updates to improve the control system. Keeping the control system up to date ensures the best performance!
* **Isolate the Issue -** This is key to effective troubleshooting. Many issues can show the same symptom, so eliminating failure points one at a time is critical to finding the root cause.

{% hint style="danger" %}
DO NOT plug a battery charger into either the Control Hub or Expansion Hub. It will damage the Hub and cause eventual device failure
{% endhint %}

Maintaining and taking care of the 12V Slim Battery is also important for troubleshooting purposes. All rechargeable batteries have a finite lifespan however following the [best practices for the 12V Slim Battery](/duo-control/menu/control-hub-gs/configuration.md#slim-battery-best-practices) can extend the lifespan of the battery.

### ESD Mitigation Techniques <a href="#esd-mitigation-techniques" id="esd-mitigation-techniques"></a>

During Match Play or practice on a competition field, some FTC teams may encounter Electrostatic Discharge (ESD) between the foam tiles and the robots. Below are some methods to help mitigate the effects that any ESD may have on your robot.

1. Ensure that you plug USB devices, such as a Camera, into USB 3.0 Port on your Control Hub. Using the USB 2.0 Port may cause ESD to affect your Control Hub's Wi-Fi Chip
2. Add a [Resistive Grounding Strap](https://www.revrobotics.com/rev-31-1269/), the 470Ω resistor will help minimize high discharge events from robot electronics and the frame
3. Treat the practice area with an anti-static spray
4. Other ESD mitigation strategies can be found within the documentation provided by *FIRST*: [Managing Electrostatic Discharge Effects](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html)

### USB Port Care

Regular maintenance of your DUO Control System's USB ports will help prevent issues in the future. Here are a few tips to make sure your hardware stays in good shape.

* When plugging in USB cables, don't force the connector too roughly. This can push the USB port into the Control Hub or Driver Hub
* Be sure to keep all ports clean and free of debris. Before cleaning with compressed air, be sure to turn off your device&#x20;
* When transporting or storing a Driver Hub, remove all USB cables from the ports

{% hint style="warning" %}
Don't wrap USB cables that are plugged in around the Driver Hub! This will put stress on the USB ports and is the most common cause of USB port damage
{% endhint %}
