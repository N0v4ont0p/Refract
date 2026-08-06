> Source: https://docs.revrobotics.com/duo-control/sensors/i2c/adding-an-external-imu-to-your-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/sensors/i2c/adding-an-external-imu-to-your-hub.md).

# Adding an External IMU to your Hub

{% hint style="info" %}
All Control Hubs feature an internal IMU. If your Expansion Hub was purchased *BEFORE* December 2021, it has an internal IMU installed.
{% endhint %}

## **Configuring the 9-Axis IMU (**&#x52;EV-31-3332)

{% hint style="info" %}
To use the 9-Axis IMU the Control Hub must be running Robot Controller App v10.0 or newer.
{% endhint %}

{% hint style="success" %}
[A full configuration walkthrough is available here.](/duo-control/hello-robot-blocks/configuration.md)
{% endhint %}

The 9-Axis IMU is configured similar to other I2C devices. First, navigate to the Control Hub Portal or Expansion Hub where it is connected in the configuration menu.

<figure><img src="/files/sTEr2BmchChAXUrDrSLW" alt=""><figcaption><p>Configuration menu on the Driver Hub</p></figcaption></figure>

Next, scroll to find the option to add something to the I2C Bus. **Note:** The internal IMU appears in I2C Bus 0. For this example, we are adding the 9-Axis IMU to I2C Bus 1.

<figure><img src="/files/jRz22fsTLm3hCRHA8Azr" alt=""><figcaption><p>I2C Bus options in the configuration menu</p></figcaption></figure>

Once in the menu, click "Add". This will show the option to add a new sensor to this I2C Bus.&#x20;

<figure><img src="/files/2iaUyycjXevN9AfonrYP" alt=""><figcaption><p>Option to add a new I2C device to the bus</p></figcaption></figure>

Scroll to select the REV 9-Axis IMU from the dropdown menu.

<figure><img src="/files/Ql6HSjWfKKHBlwcEXSwa" alt=""><figcaption><p>9-Axis IMU within the available dropdown menu</p></figcaption></figure>

Name the IMU something relevant that will be easy to identify later. Remember the built-in IMU, if applicable, may also appear as an option while programming.

<figure><img src="/files/qTwDe10nTMQi1YpJivS9" alt=""><figcaption><p>Naming the IMU to identify it while programming</p></figcaption></figure>

Finally, select "Done" and complete the remainder of your configuration process.

<figure><img src="/files/4Mm6Y5noSDMnf3oOhy39" alt=""><figcaption><p>The "Done" option will save the added sensor</p></figcaption></figure>

### **9-Axis IMU in Blocks**

Once configured, the 9-Axis IMU will appear as an option under "Sensors" in the Blocks menu.

<figure><img src="/files/PMzh9E3qg3yYIH7zusVH" alt=""><figcaption><p>The IMU listing in the Blocks side menu</p></figcaption></figure>

When calling the IMU, the configured 9-Axis IMU will appear as the assigned name in the dropdown option on the individual block.

<figure><img src="/files/5mCPEvXPJrpt84eTNSx9" alt=""><figcaption><p>IMU selection dropdown</p></figcaption></figure>

### 9-Axis IMU in OnBot Java

When "Setup Code for Configured Hardware" is checked while creating a new OpMode in OnBot Java, the IMU will automatically be added to the hardwareMap using the assigned name from configuration.

An internal IMU, if applicable, will retain its default name based on the version of IMU (BNO055 or BHI260AP).

<figure><img src="/files/ielpJiTWAgmfy9DSLKCV" alt=""><figcaption><p>The configured IMU appearing in OnBot's hardwareMap</p></figcaption></figure>

## **Other Compatible External IMUs**

There are a few options that will work for giving your Hub Gyro/IMU function.

1. [navX2 Sensor Bundle](https://www.andymark.com/products/navx2-micro-navigation-sensor-bundle) - Also supported in the FTC programming environment. Code examples are listed on AndyMark's page, and this product includes the correct cables to use within FTC. &#x20;
2. [Adafruit 9-DOF Absolute Orientation IMU](https://www.adafruit.com/product/4646) - This is the same IMU as in Control Hubs from before 2022, but will require you to either create an adapter cable or solder a cut [sensor cable](https://www.revrobotics.com/jst-ph-4-pin-sensor-cable-4-pack/) to the board. Plugging this in and configuring the IMU on I2C port zero will allow you to use and program the same as an internal IMU.
3. [Integrating Gyro](https://modernroboticsinc.com/product/integrating-gyro/) with our [Logic Level Converter](https://www.revrobotics.com/rev-31-1389/) and [Sensor Cable Adapter](https://www.revrobotics.com/rev-31-1384/) - This is supported in the FTC Programing environment but is just a single-axis gyro, not a full IMU.
