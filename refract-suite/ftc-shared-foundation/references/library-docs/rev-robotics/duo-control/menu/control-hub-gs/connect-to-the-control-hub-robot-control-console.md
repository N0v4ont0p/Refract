> Source: https://docs.revrobotics.com/duo-control/menu/control-hub-gs/connect-to-the-control-hub-robot-control-console.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/control-hub-gs/connect-to-the-control-hub-robot-control-console.md).

# Connect to the Robot Controller Console

In order to manage the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) or programming using the onboard programming languages, a computer or other Wi-Fi enabled device will need to connect to the Control Hub's Robot Controller Console. The Robot Control Console is a local network created by the Control Hub to program and manage the device. &#x20;

{% hint style="info" %}
This example assumes the user uses Windows 10 as their operating system. If you are not using a Windows 10, the procedure to connect to the network will differ. Refer to your device’s documentation for details on how to connect to a Wi-Fi network.
{% endhint %}

By default, the Control Hub has a name that begins with "FTC-" or "FIRST-" followed by four characters that are assigned randomly. The default password for the network is "password". If either of these is forgotten, there are a [few ways to recovery or reset the password on the Control Hub](/duo-control/managing-the-control-system/ch-wifi.md)[.](/duo-control/managing-the-control-system/ch-wifi.md)

There are two ways to access the Robot Controller Console. The first will cover how to access the Robot Controller Console with the REV Hardware Client. It is recommended to use the [REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client/) as it will allow the user to access the Robot Controller Console over a wired connection.&#x20;

The second will run through accessing the [Robot Controller Console via a web browser](/duo-control/menu/control-hub-gs/connect-to-the-control-hub-robot-control-console.md#web-browser).

## REV Hardware Client&#x20;

{% hint style="info" %}
You are able to connect to a Control Hub over Wi-Fi or directly through USB-C when using the REV Hardware Client! We recommend connecting via USB to reduce the chance of disconnects.
{% endhint %}

[Download the latest version of the REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client/) and install on a Windows PC.&#x20;

| Steps                                                                                                                                                                              |                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Power on the Control Hub, by plugging the 12V Slim Battery ([REV-31-1302](https://www.revrobotics.com/rev-31-1302/)) into the XT30 connector labeled “BATTERY” on the Control Hub. | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png](/files/-M8N18gHM0EmnJzRcHEz) |
| The Control Hub is ready to connect with a PC when the LED turns from blue to green.                                                                                               | <img src="/files/AavR7ZE9ktdQjsWamRUx" alt="" data-size="original">                                               |
| Plug the Control Hub into the PC using a USB-A to USB-C Cable ([REV-11-1232](https://www.revrobotics.com/rev-11-1232/))                                                            |                                                                                                                   |

Startup the REV Hardware Client. Once the hub is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Control Hub.&#x20;

![](/files/-MGiVDNfFRESoYAwBz8s)

After selecting the Connected Hardware the Update tab will pop up.  Select the Program and Manage tab. This will take you to the Robot Controller Console build into the REV Hardware Client.&#x20;

![](/files/-MGiVq2dC15lP3XjXlZg)

{% hint style="info" %}
At this point it is useful to update the [Control Hub Operating System](/duo-control/managing-the-control-system/updating-operating-system.md#using-the-rev-hardware-client), [Robot Controller App](/duo-control/managing-the-control-system/updating-robot-controller-application.md#using-the-rev-hardware-client), and the [Hub Firmware](/duo-control/managing-the-control-system/updating-firmware.md#using-the-rev-hardware-client).&#x20;
{% endhint %}

Once in the Robot Controller Console, the homepage of the console will appear. In the upper right corner is the navigation menu which will allow users to access the Blocks, OnBot Java, and Manage pages within the console.&#x20;

![](/files/-MGiWtKw2qnPRcb0-SUj)

## Web Browser

{% hint style="success" %}
When using a Chromebook or Macbook with a Control Hub follow the steps below.
{% endhint %}

With the Control Hub powered, access the Wi-Fi network selector. For Windows 10 devices, click the Wi-Fi Network icon in the lower right corner of the desktop.

![](/files/-M_b-AsOKjBNvaLfutRw)

Look for the Wi-Fi that matches the naming protocol of the device.&#x20;

{% hint style="info" %}
To ensure you are able to locate the correct device, it is recommended that you first connect in a location without other active Control Hubs or significant Wi-Fi connections.
{% endhint %}

![](/files/-M_b0S35_75GS5oQxrjB)

{% hint style="info" %}
Depending on your version of Windows or other theme settings your Wi-Fi Networks list may vary in appearance.
{% endhint %}

Once you have found the target network in the list, click on it to select it then press connect.

![](/files/-M_b1LU2DCjFY1E31Cfe)

Provide the network password (in this example “password”) and press “Next” to continue.

![](/files/-M_b1qEvHy1YdPruZwa1)

{% hint style="warning" %}
Passwords are case sensitive. Make sure that your spelling and capitalization matches the original spelling and capitalization for the password.
{% endhint %}

Once a wireless connection is established, the status is displayed in the wireless settings for the device.

![](/files/-M_b2SOCPhXMyAkVAaZo)

{% hint style="danger" %}
When connected to the Control Hub, the connected device will not have access to the Internet. It only has direct access to the Control Hub.
{% endhint %}

Open a web browser (Chrome, Firefox, Edge, Internet Explorer) and navigate to "192.168.43.1:8080" through the address bar.

![](/files/-M_b2zPuip_ollQIVXvu)

From the Robot Controller Console users can[ update the Wi-Fi settings](/duo-control/menu/control-hub-gs/updating-wifi-settings.md), upgrade the [operating system](/duo-control/managing-the-control-system/updating-operating-system.md) and [firmware](/duo-control/managing-the-control-system/updating-firmware.md), as well as[ program ](/duo-control/hello-robot-blocks/welcome.md)the device. It is strongly recommended that you go through all steps above before you begin programming.

## Videos

**Using the REV Hardware Client**&#x20;

{% embed url="<https://youtu.be/YdgaknRQvKQ?feature=shared>" %}

**Using a Web Browser**&#x20;

{% embed url="<https://youtu.be/fyxpptqQumw?feature=shared>" %}
