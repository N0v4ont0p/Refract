> Source: https://docs.revrobotics.com/duo-control/menu/control-hub-gs/updating-wifi-settings.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/control-hub-gs/updating-wifi-settings.md).

# Updating Wi-Fi Settings

One of the first recommendations made to users of the REV Control System is to update Wi-Fi settings, specifically the name and the password.&#x20;

All Control Hub's come with a default network name and password. It is useful to change the name and password especially in environments where there are multiple Control Hubs running like at an event or in a classroom. Changing from the default adds an element of network security to the Hub by reducing the potential for access from outside sources. &#x20;

The Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) can utilize either the 2.4 GHz or 5 GHz Wi-Fi band. REV Robotics advises that during competition teams utilize a 5 GHz channel for robot communication. Consult the table below for Driver Station devices that can operate on the 5 GHz band.&#x20;

<details>

<summary>Legacy Information on Wi-Fi Settings</summary>

With the release of Robot Controller Application 5.5 there have been some major changes to the process of changing Control Hub name, password, Wi-Fi Channel, and Wi-Fi band. Previously changes to the name and password had to be made separately. Each change would reset the network and require users to reconnect to the network in order to change anything else. With 5.5 all changes can be made at once.&#x20;

The Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) can utilize either the 2.4 GHz or 5 GHz Wi-Fi band. In OS versions 1.1.1 and older the Control hub defaults to a channel on the 2.4 GHz band.

</details>

## Supported Android Devices and Wi-Fi Band Capabilities

As of the 2024-2025 FTC season, Android phones must be running Android 7 (Nougat) or newer to be compatible with the Driver Station App. Please check the [game manual for full rules](https://www.firstinspires.org/resource-library/ftc/game-and-season-info).&#x20;

<table data-header-hidden><thead><tr><th width="265.3333333333333">Phone</th><th></th><th>WiFi Band</th></tr></thead><tbody><tr><td>Device</td><td>Notes</td><td>Wi-Fi Band</td></tr><tr><td>REV Driver Hub </td><td><a href="https://www.revrobotics.com/rev-31-1596/">REV-31-1596</a></td><td>2.4 GHz &#x26; 5 GHz (Dual Band)</td></tr><tr><td>Moto G4 /4th Generation</td><td></td><td>2.4 GHz (Single Band)</td></tr><tr><td>Moto G5</td><td></td><td>2.4 GHz &#x26; 5 GHz (Dual Band)</td></tr><tr><td>Moto G5 Plus</td><td></td><td>2.4 GHz &#x26; 5 GHz (Dual Band)</td></tr><tr><td>Moto E4</td><td>USA Versions only, includes SKUs XT1765, XT1765PP, XT1766, and XT1767</td><td>2.4 GHz &#x26; 5 GHz (Dual Band)</td></tr><tr><td>Moto E5</td><td>XT1920</td><td>2.4 GHz &#x26; 5 GHz (Dual Band)</td></tr><tr><td>Moto E5 Play</td><td>XT1921</td><td>2.4 GHz &#x26; 5 GHz (Dual Band)</td></tr></tbody></table>

The following section will highlight how to access and make changes within the Wi-Fi settings. This section will use the REV Hardware Client to showcase how to make these changes. Once a user has connected to the Robot Controller Console, either via the Hardware Client or a web browser, the steps for accessing Wi-Fi settings are the same.&#x20;

{% hint style="warning" %}
The following steps assume that users have already connected to the Robot Controller Console. Please go to the [Connect to the Robot Controller Console](/duo-control/menu/control-hub-gs/connect-to-the-control-hub-robot-control-console.md) if this is not the case.&#x20;
{% endhint %}

## Steps to Updating Wi-Fi Settings

While in the Robot Controller Console select the menu button. In the image below the menu button is highlighted by an orange square in the upper right-hand corner.&#x20;

![](/files/-MGiWtKw2qnPRcb0-SUj)

When the menu opens, select Manage.&#x20;

![](/files/-MGiXVPe5NHwUoYHWID-)

The Manage page is where the Wi-Fi Settings live. The following steps will show and discuss each change as it is made. Please keep in mind the following warning while moving through the steps:

You will need to reconnect to the new Wi-Fi network after changing the name and/or password. This is true for any Wi-Fi connection, but if you are accessing the REV Hardware Client via a USB connection the Hub will stay connected. Though, you may need to close and reopen the Hardware Client in order to see the changes.&#x20;

{% hint style="info" %}
Not all aspects of the Wi-Fi settings need to be changed. If you need to change name and password and do not need to mess with the Wi-Fi band or channel, leave those settings at default, and click **Apply Wi-Fi Settings**.
{% endhint %}

![](/files/-MGiYK1O8HCxJlCjDn6L)

### Changing Control Hub Name

Under Wi-Fi Settings, there is an option to change the name of the Control Hub.&#x20;

{% hint style="info" %}
It is useful to change the Control Hub name to something unique, especially in environments where there are multiple Control Hubs running like at an event or in a classroom.&#x20;
{% endhint %}

For FTC teams you will want to change the name from the default to team number - RC.  (i.e. 99999-RC)

### Changing the Control Hub Password

Under Wi-Fi Settings, there is an option to change the password of the Control Hub. There are not any restrictions on the password. Changing it from the default is advised but it does not have to change to anything complicated.&#x20;

{% hint style="info" %}
The default password 'password' is a well know password by Control Hub users, since it is the default for all Control Hubs. Staying with the default password significantly reduces network security. Changing from the default adds the element of network security back to the Hub by reducing the potential for access from outside sources.&#x20;
{% endhint %}

### Changing the Wi-Fi Band and Channel&#x20;

The Control Hub is capable of utilizing either the 2.4 GHz or 5 GHz Wi-Fi band. This change is also made within the Wi-Fi Settings.

![](/files/-MGjUCQkBBEkktEfsBTx)

The Robot Controller Console makes it easy to change between the 2.4 GHz an 5GHz bands. It is advised to check the [Legal Android and Wi-Fi Band Capabilities](/duo-control/menu/control-hub-gs/updating-wifi-settings.md#legal-android-devices-and-wifi-band-capabilites) table to determine which band to operate in.&#x20;

Once a Wi-Fi band is chosen there are two options for dealing with Wi-Fi channels. One option is to let the Control Hub auto default on a channel. The other is to set a specific channel. Both options can be accessed via the drop down menu under the Wi-Fi channel section of the Wi-Fi settings.&#x20;

It is valuable to know how to change the Wi-Fi Band and Channel as technical staff at an event can request to change those settings.&#x20;

{% hint style="info" %}
The Wi-Fi band and channel can be changed via the Driver Station Application. For more information on how to make these changes from the Driver Station please see [Managing the Wi-Fi Network ](/duo-control/managing-the-control-system/ch-wifi.md)section.
{% endhint %}
