> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/9-axis-imu/configuring-the-9-axis-imu.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/9-axis-imu/configuring-the-9-axis-imu.md).

# Configuring the 9-Axis IMU

{% hint style="info" %}
To use the 9-Axis IMU the Control Hub must be running Robot Controller App v10.0 or newer.
{% endhint %}

{% hint style="success" %}
[A full configuration walkthrough is available here.](https://docs.revrobotics.com/duo-control/hello-robot-blocks/configuration)
{% endhint %}

The 9-Axis IMU is configured similar to other I2C devices. First, navigate to the Control Hub Portal or Expansion Hub where it is connected in the configuration menu.

<figure><img src="/files/ZmOA1luT2nRPj8P2KjgI" alt=""><figcaption><p>Configuration menu on the Driver Hub</p></figcaption></figure>

Next, scroll to find the option to add something to the I2C Bus. **Note:** The internal IMU appears in I2C Bus 0. For this example, we are adding the 9-Axis IMU to I2C Bus 1.

<figure><img src="/files/35kscIhyNiyCM0wZX6Lw" alt=""><figcaption><p>I2C Bus options in the configuration menu</p></figcaption></figure>

Once in the menu, click "Add". This will show the option to add a new sensor to this I2C Bus.&#x20;

<figure><img src="/files/Rksz1psG7uSJFEmbIWM0" alt=""><figcaption><p>Option to add a new I2C device to the bus</p></figcaption></figure>

Scroll to select the REV 9-Axis IMU from the dropdown menu.

<figure><img src="/files/GK4BMw4yTPgDbQ2G0urC" alt=""><figcaption><p>9-Axis IMU within the available dropdown menu</p></figcaption></figure>

Name the IMU something relevant that will be easy to identify later. Remember the built-in IMU, if applicable, may also appear as an option while programming.

<figure><img src="/files/0SXQy0Quxij9cUTjwDI4" alt=""><figcaption><p>Naming the IMU to identify it while programming</p></figcaption></figure>

Finally, select "Done" and complete the remainder of your configuration process.

<figure><img src="/files/UeQ3wEKQIWNb1WvuzbHs" alt=""><figcaption><p>The "Done" option will save the added sensor</p></figcaption></figure>

### **9-Axis IMU in Blocks**

Once configured, the 9-Axis IMU will appear as an option under "Sensors" in the Blocks menu.

<figure><img src="/files/p84snCeoXXwzHLydetyh" alt=""><figcaption><p>The IMU listing in the Blocks side menu</p></figcaption></figure>

When calling the IMU, the configured 9-Axis IMU will appear as the assigned name in the dropdown option on the individual block.

<figure><img src="/files/QBqOtgK0nF2u2GAlVXlr" alt=""><figcaption><p>IMU selection dropdown</p></figcaption></figure>

### 9-Axis IMU in OnBot Java

When "Setup Code for Configured Hardware" is checked while creating a new OpMode in OnBot Java, the IMU will automatically be added to the hardwareMap using the assigned name from configuration.

An internal IMU, if applicable, will retain its default name based on the version of IMU (BNO055 or BHI260AP).

<figure><img src="/files/KxfmlD1yC7mjrcWxuCdZ" alt=""><figcaption><p>The configured IMU appearing in OnBot's hardwareMap</p></figcaption></figure>
