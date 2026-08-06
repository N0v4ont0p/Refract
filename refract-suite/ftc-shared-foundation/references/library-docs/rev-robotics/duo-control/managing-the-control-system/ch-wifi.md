> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/ch-wifi.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/ch-wifi.md).

# Managing Wi-Fi on the Control Hub

The Control Hub creates a Wi-Fi access point to connect a Driver Station device or laptop to the Control Hub for programming and operation. Settings for the Control Hub access point are managed through the Robot Controller Console or the User Button on the Control Hub.

Before making changes to the Control Hub's Wi-Fi network checking what Wi-Fi bands are supported by the devices being used is important to ensure they will work as expected. Below are the Android Devices that are officially supported:&#x20;

#### Supported Android Devices and Wi-Fi Band Capabilities

As of the 2024-2025 FTC season, Android phones must be running Android 7 (Nougat) or newer to be compatible with the Driver Station App. Please check the [game manual for full rules](https://www.firstinspires.org/resource-library/ftc/game-and-season-info).

| Device                  | Notes                                                                 | Wi-Fi Band                  |
| ----------------------- | --------------------------------------------------------------------- | --------------------------- |
| REV Driver Hub          | [REV-31-1596](https://www.revrobotics.com/rev-31-1596/)               | 2.4 GHz & 5 GHz (Dual Band) |
| Moto G4 /4th Generation |                                                                       | 2.4 GHz (Single Band)       |
| Moto G5                 |                                                                       | 2.4 GHz & 5 GHz (Dual Band) |
| Moto G5 Plus            |                                                                       | 2.4 GHz & 5 GHz (Dual Band) |
| Moto E4                 | USA Versions only, includes SKUs XT1765, XT1765PP, XT1766, and XT1767 | 2.4 GHz & 5 GHz (Dual Band) |
| Moto E5                 | XT1920                                                                | 2.4 GHz & 5 GHz (Dual Band) |
| Moto E5 Play            | XT1921                                                                | 2.4 GHz & 5 GHz (Dual Band) |

The following page is split into two sections. The first will cover how to access the Wi-Fi Settings through the Robot Controller Console. It is recommended to use the [REV Hardware Client](/duo-control/managing-the-control-system/ch-wifi.md#rev-hardware-client) as it will allow the user to access the Wi-Fi settings over a wired connection. The second will run through the steps for using the Control Hub's User Button to preform a Wi-Fi reset or Wi-Fi band change.&#x20;

{% hint style="info" %}
If you run into any problems trying to use the Hardware Client or when resetting the Wi-Fi, please contact <support@revrobotics.com>
{% endhint %}

## Using the Robot Controller Console

The Robot Controller Console gives access to the Wi-Fi settings of the Control Hub. Below are the steps to access the Robot Controller Console through the [REV Hardware Client](/duo-control/managing-the-control-system/ch-wifi.md#rev-hardware-client) and the [Driver Station ](/duo-control/managing-the-control-system/ch-wifi.md#driver-station-application)application for updating Wi-Fi settings.

### REV Hardware Client&#x20;

The REV Hardware Client allows teams access to the Hub's Wi-Fi Settings information through a wired connection. The information is visible through the main page of the Robot Control Console and updated through the Program and Manage tab.

[Download the latest version of the REV Hardware Client ](https://github.com/REVrobotics/REV-Software-Binaries/releases/download/rhc-1.5.3/REV-Hardware-Client-Setup-1.5.3.exe)and install on a Windows PC. Skip this step if completed already.

| Steps                                                                                                                                                                              |                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Power on the Control Hub, by plugging the 12V Slim Battery ([REV-31-1302](https://www.revrobotics.com/rev-31-1302/)) into the XT30 connector labeled “BATTERY” on the Control Hub. | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png](/files/-M8N18gHM0EmnJzRcHEz) |
| The Control Hub is ready to connect with a PC when the LED turns from blue to green.                                                                                               | <img src="/files/fC8VwD4edjI1IouWn4mN" alt="" data-size="original">                                               |
| Plug the Control Hub into the PC using a USB-A to USB-C Cable ([REV-11-1232](https://www.revrobotics.com/rev-11-1232/))                                                            |                                                                                                                   |

Startup the REV Hardware Client. Once the hub is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Control Hub.&#x20;

![](/files/-MGiVDNfFRESoYAwBz8s)

After selecting the Connected Hardware the Update tab will pop up.  Select the Program and Manage tab. This will take you to the Robot Controller Console build into the REV Hardware Client.&#x20;

![](/files/-MGiVq2dC15lP3XjXlZg)

Once in the Robot Controller Console, there are two options.&#x20;

If just the Wi-Fi Access Point name and password need to be found, they can be seen on the main page of the Robot Controller Console.&#x20;

If any of the Wi-Fi Access Point information needs to be changed, select the menu button in the upper right-hand corner of the page, indicated in the image below.&#x20;

![](/files/-MGiWtKw2qnPRcb0-SUj)

When the menu opens, select Manage.&#x20;

![](/files/-MGiXVPe5NHwUoYHWID-)

The Manage page is where the Wi-Fi Access Point information for the Hub can be viewed and changed. In the image below, the Hub's Wi-Fi name, password, band, and channel can be changed. Editing these settings can help when the Hub is not showing up as a potential connection point from a computer or Driver Station device.&#x20;

Once changes have been made select **Apply Wi-Fi Settings**.&#x20;

![](/files/-MGiYK1O8HCxJlCjDn6L)

{% hint style="warning" %}
Once updates are made to the network reconnection  to the new Wi-Fi network is needed. When accessing the REV Hardware Client via a USB connection the Control Hub will stay connected to the REV Hardware Client. Rescanning for devices is necessary for changes to show in the Hardware Client.&#x20;
{% endhint %}

### Driver Station Application&#x20;

The Manage page of the Robot Controller Console can also be accessed via the Driver Station Application. This is helpful in event environments, where Field Technical Staff may request that you change Wi-Fi bands or channels to mitigate disconnections.&#x20;

Select the three horizontal dots in the upright corned of the Driver Station Application&#x20;

![](/files/-M_genai4ratvTaqPPuW)

In the drop down menu select **Program & Manage**.&#x20;

![](/files/-M_gfMg9ITaC6n5bq6aV)

Once in the Robot Controller Console, there are two options.&#x20;

If just the Wi-Fi Access Point name and password need to be found, they can be seen on the main page of the Robot Controller Console.&#x20;

If any of the Wi-Fi Access Point information needs to be changed, select the menu button in the upper right-hand corner of the page, indicated in the image below.&#x20;

![](/files/-M_gfs3aelJh-9QKEp5_)

When the menu opens, select Manage.&#x20;

![](/files/-M_ggQJ9xEkQShZvamBU)

The Manage page is where the Wi-Fi Access Point information for the Hub can be viewed and changed. In the image below, the Hub's Wi-Fi name, password, band, and channel can be changed.&#x20;

Once changes have been made select **Apply Wi-Fi Settings**.&#x20;

![](/files/-M_ggsCk28dyRHR1BInM)

{% hint style="danger" %}
You will need to reconnect to the new Wi-Fi network after changing the name/and or password.
{% endhint %}

## Using the User Button

The Control Hub has a user button underneath the LED on the right side of the device. This button allows for a [Wi-Fi reset](/duo-control/managing-the-control-system/ch-wifi.md#wifi-reset) or [changing the Wi-Fi band](/duo-control/managing-the-control-system/ch-wifi.md#changing-wifi-band) currently being used on the Control Hub.

### Wi-Fi Reset

If you are unable to connect to the Control Hub's Wi-Fi after switching to the 5 GHz band, you can perform a Wi-Fi factory reset. The Wi-Fi network name and password will be reset to their default values, and the Wi-Fi band will be set to 2.4 GHz. To perform a Wi-Fi reset, please follow the steps below.&#x20;

{% hint style="info" %}
The Wi-Fi reset can take several minutes to complete.&#x20;
{% endhint %}

| Step                                                                                                                                                                            | Image                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Press and hold the button on the front of the Control Hub.                                                                                                                      | ![A picture containing remote, monitor, black, electronics&#xA;&#xA;Description automatically generated](/files/-M8N18gRI0-TiCIKyOqh) |
| While pressing the button, power on the Control Hub.                                                                                                                            | ![](/files/-M8N18gSDiif0kH2u05j)                                                                                                      |
| Release button when the Control Hub LED begins to flash a multitude of colors. When the Control Hub flashes Blue then Green it has completed the reset and is ready to connect. |                                                                                                                                       |

{% hint style="success" %}
When the Control Hub flashes Blue then Green it has completed the reset and is ready to connect. The Wi-Fi network will reset back to the default name and password.
{% endhint %}

### Changing Wi-Fi Band

When running version 1.1.2 or later of the Operating System, the Control Hub can switch between the 2.4GHz and 5GHz Wi-Fi bands without access to the REV Hardware Client or the Robot Controller Console. This will only change the Wi-Fi band. When switching to a Wi-Fi band this way, the most recent channel selected on that band will be used (defaulting to auto).

| Step                                                                                                                  | Image                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| While pressing the button, power on the Control Hub.                                                                  | ![](/files/-M8N18gSDiif0kH2u05j)                                                                                                      |
| Press and hold the button on the front of the Control Hub after the Control Hub has fully booted (LED is solid green) | ![A picture containing remote, monitor, black, electronics&#xA;&#xA;Description automatically generated](/files/-MIym3ENg0UyQJ60AUhH) |
| Release button when the Control Hub LED flashes MAGENTA or YELLOW.                                                    |                                                                                                                                       |

{% hint style="info" %}
The Control Hub's LED blinks magenta when the band is switched to 5 GHz and yellow when the band is switched to 2.4 GHz.
{% endhint %}
