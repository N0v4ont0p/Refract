> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting/dc-motor-port-voltage-testing.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting/dc-motor-port-voltage-testing.md).

# DC Motor Port Voltage Testing

There may come a time when you need to determine if connection ports on either the Control or Expansion Hub are shorted. This section will walk you through how to use a common digital multimeter to see if Voltage is still being pushed through the device.

{% stepper %}
{% step %}
Consult your user's manual to make sure the lead connections are plugged into the correct terminals for DC voltage measurement.&#x20;

<figure><img src="/files/Zw36HoeThKlYlW6e22aA" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
In our case, we needed to turn the rotary dial to Hz V and press Function to start measuring for Voltage.

<figure><img src="/files/Iz9LBllPafQ9MgPXTlTr" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Make sure to run your code so the motor ports turn on, then touch your leads to the motor port prongs to get a voltage measurement. Since the code is asking the Control Hub to run port 0 at 100% power, if there is no damage, then we should be able to measure output voltage similar to the battery's supplied voltage.

<figure><img src="/files/9VedJ4C44jsZqVEyvCOy" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Since a 12V Slim Battery powers the Control System, you should read a range of voltages.
{% endhint %}
{% endstep %}

{% step %}
Running the same code, the Control Hub runs port 1 at 100% power; if there is no damage, we should be able to measure output voltage similar to the battery's supplied voltage. However, when measuring motor port 1, even though my 12V battery is charged and my code is running, the multimeter isn't reading anything significant. This motor port is likely damaged, and you should contact support or purchase the [Control Hub Repair Service](https://www.revrobotics.com/rev-31-1595-rfb/?searchid=5390587\&search_query=control+hub+repair).

<figure><img src="/files/C9DgSCU8K5ujdBkgWdwL" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Identifying a motor port that does not output voltage on a Control Hub means that something within the port's internal motor controller has been damaged. Since this port is no longer functional, it is recommended to use the [Control Hub Repair Service](https://www.revrobotics.com/rev-31-1595-rfb/?searchid=5360143\&search_query=control+hub+repair) or to fix your Hub.
{% endhint %}
{% endstep %}
{% endstepper %}
