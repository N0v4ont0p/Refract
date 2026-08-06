> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/where-to-program.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/where-to-program.md).

# Where to Program - Client vs. Browser

When using Blocks or OnBot Java there are two primary ways to access the Robot Controller App on the Control Hub for programming.&#x20;

{% hint style="info" %}
The [Robot Controller App](https://ftc-docs.firstinspires.org/en/latest/ftc_sdk/updating/rc_app/Updating-the-RC-App.html) is the application from the SDK that communicates with the Driver Station App to control the robot. It also contains the programming environments for Blocks and OnBot Java allowing these programs to be saved directly on the Control Hub.

This software is developed and managed by *FIRST.*
{% endhint %}

The first way is through the [REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client) (RHC), the same software you use to update the Control and Driver Hub! This application makes it easy to navigate, manage, update, and program with the Control Hub. Additionally, the RHC allows for programming while connected via USB or Wi-Fi. However, the REV Hardware Client is currently only available  for Windows.&#x20;

{% hint style="warning" %}
As of April 12, 2024 Windows 10 or later is required for the latest version of the REV Hardware Client. [Please use 1.6.4 if you are on an older version of Windows.](https://github.com/REVrobotics/REV-Software-Binaries/releases/download/rhc-1.6.4/REV-Hardware-Client-Setup-1.6.4.exe)
{% endhint %}

As an alternate option, the Robot Controller App can be accessed via Wi-Fi allowing programming through a web browser. This is the perfect option for those using Chromebooks or who may have restrictions on installing applications.&#x20;

{% hint style="info" %}
The Hello Robot tutorial focuses on the use of the REV Hardware Client for programming. If you are using the Web Browser to program you will still be able to follow along, but you may see some slight variation in screenshots.&#x20;
{% endhint %}

## REV Hardware Client

[Download the latest version of the REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client/) and install on a Windows PC.&#x20;

<table data-header-hidden><thead><tr><th></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Steps</td><td></td><td></td></tr><tr><td>Power on the Control Hub, by plugging the 12V Slim Battery (<a href="https://www.revrobotics.com/rev-31-1302/">REV-31-1302</a>) into the XT30 connector labeled “BATTERY” on the Control Hub.</td><td><img src="/files/-M8N18gHM0EmnJzRcHEz" alt="C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png"></td><td></td></tr><tr><td>The Control Hub is ready to connect with a PC when the LED turns green. Note: the light blinks blue every ~5 seconds to indicate that the Control Hub is healthy.</td><td><img src="/files/-M8N18gICw6_gms8beSs" alt="C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\rect22073.png"></td><td></td></tr><tr><td>Plug the Control Hub into the PC using a USB-A to USB-C Cable (<a href="https://www.revrobotics.com/rev-11-1232/">REV-11-1232</a>)</td><td></td><td></td></tr></tbody></table>

Startup the REV Hardware Client. Once the hub is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Control Hub.&#x20;

<figure><img src="/files/PXU3qk6832zDzxESfPuD" alt=""><figcaption></figcaption></figure>

After selecting the Connected Hardware the Update tab will pop up.  Select the Program and Manage tab. This will take you to the Robot Controller Console build into the REV Hardware Client.&#x20;

<figure><img src="/files/3kUdqd1qtedaYCgGhes2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
At this point it is useful to update the [Control Hub Operating System](/duo-control/managing-the-control-system/updating-operating-system.md#using-the-rev-hardware-client), [Robot Controller App](/duo-control/managing-the-control-system/updating-robot-controller-application.md#using-the-rev-hardware-client), and the [Hub Firmware](/duo-control/managing-the-control-system/updating-firmware.md#using-the-rev-hardware-client).&#x20;
{% endhint %}

Once in the Robot Controller Console, the homepage of the console will appear. You will see the option for "Blocks" and "OnBot Java" along the top tool bar. "Manage" provides access to changing the Control Hub's network settings!

<figure><img src="/files/vuq2D6eEGnAEXpjezRwh" alt=""><figcaption></figcaption></figure>

## Web Browser

{% hint style="success" %}
When using a Chromebook or Macbook with a Control Hub follow the steps below.
{% endhint %}

With the Control Hub powered, access the Wi-Fi network selector. For Windows 10 devices, click the Wi-Fi Network icon in the lower right corner of the desktop.

<figure><img src="/files/YsXfuv5AFowB70NrMk4a" alt=""><figcaption></figcaption></figure>

Look for the Wi-Fi that matches the naming protocol of the device.&#x20;

{% hint style="info" %}
To ensure you are able to locate the correct device, it is recommended that you first connect in a location without other active Control Hubs or significant Wi-Fi connections.
{% endhint %}

<figure><img src="/files/fVMhvmQqF90Fyg334U1Z" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Depending on your version of Windows or other theme settings your Wi-Fi Networks list may vary in appearance.
{% endhint %}

Once you have found the target network in the list, click on it to select it then press connect.

<figure><img src="/files/RcbzORjT4Rym3xQbZNsC" alt=""><figcaption></figcaption></figure>

Provide the network password (in this example “password”) and press “Next” to continue.

<figure><img src="/files/VecnFCUlwDJyT31tcABb" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Passwords are case sensitive. Make sure that your spelling and capitalization matches the original spelling and capitalization for the password.
{% endhint %}

Once a wireless connection is established, the status is displayed in the wireless settings for the device.

<figure><img src="/files/ZrKlQxgmEi3nuA2iy6u9" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
When connected to the Control Hub, the connected device will not have access to the Internet. It only has direct access to the Control Hub.
{% endhint %}

Open a web browser (Chrome, Firefox, Internet Explorer) and navigate to "192.168.43.1:8080" through the address bar.

<figure><img src="/files/AfYpwomDwPD89FwFDaIN" alt=""><figcaption></figcaption></figure>
