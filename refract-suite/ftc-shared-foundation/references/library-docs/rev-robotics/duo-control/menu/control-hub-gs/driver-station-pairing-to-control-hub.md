> Source: https://docs.revrobotics.com/duo-control/menu/control-hub-gs/driver-station-pairing-to-control-hub.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/menu/control-hub-gs/driver-station-pairing-to-control-hub.md).

# Connecting Driver Station to Control Hub

When you first receive your Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)), you will have to connect it to a supported Android Device, like a Driver Hub. The following section of the page will walk through how to pair a Driver Hub or Driver Station phone to a Control Hub. &#x20;

{% hint style="info" %}
This section assumes you have already gone through the process of setting up your Driver Station device. If you have not please go through the following guides for more information on getting started with a Driver Station:

* [Supported Android Devices and Wi-Fi Band Capabilities](/duo-control/menu/control-hub-gs/updating-wifi-settings.md#supported-android-devices-and-wifi-band-capabilities) - To know what supported Android Devices can be used as a Driver Station
* [Getting Started with Driver Hub](/duo-control/menu/driver-hub-gs.md) - To setup a Driver Hub
* [Configuring Your Android Devices](/duo-control/legacy/configuring-a-driver-station-android-device.md) - To setup a non Drive Hub supported Android Devices as a Driver Station
  {% endhint %}

## **Connecting the Driver Station with the Control Hub**

{% embed url="<https://youtu.be/NcOK_JPGil8>" %}

{% hint style="info" %}
The procedure for pairing the Driver Hub and the Control Hub only needs to be performed once for each set of hardware. If you replace your Driver Hub or Control Hub, this procedure will need to be repeated.&#x20;
{% endhint %}

| Power on the Control Hub by plugging the 12V Slim Battery into the XT30 connector labeled “BATTERY” on the Control Hub. You may also choose to include a switch between the Battery and Control Hub, if you prefer. | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png](/files/-M8N18fh9nQ19htszfI5) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| The Control Hub is ready to pair with the Driver Station when the LED turns green.                                                                                                                                  | <img src="/files/vOSaSv1n72Qq3oHUPV9r" alt="" data-size="original">                                               |

Once you have powered on your Control Hub follow through the process for connection to either a Driver Hub or a Driver Station phone.&#x20;

{% tabs %}
{% tab title="Driver Hub" %}
{% hint style="danger" %}
This section assumes you have gone through the process of setting up your Driver Hub. If this is not the case please go to [Getting Started with the Driver Hub](/duo-control/menu/driver-hub-gs.md) and go through the process of bringing up your Driver Hub.
{% endhint %}

|                                                                                                                                                                                                                                                                                                                    |                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Open the Driver Station application from the HOME Screen.                                                                                                                                                                                                                                                          | ![](/files/-M_gnt3pX9ISxeiEf0OQ)                                    |
| In the Driver Station application, click the three dots in the upper right corner to open the drop down menu.                                                                                                                                                                                                      | <img src="/files/-M_goEZZ5I1YN4p6UduF" alt="" data-size="original"> |
| In the drop down menu select **Settings.**                                                                                                                                                                                                                                                                         | ![](/files/-M_go_GL2cFFxOtx8I_C)                                    |
| Select, “Pair with Robot Controller”.                                                                                                                                                                                                                                                                              | ![](/files/-M_gp62zDjiO84ZRcX3e)                                    |
| <p>Select <strong>Wi-Fi Settings.</strong> </p><p></p><p><strong>Note:</strong> In initial bring up for the Driver Hub you are asked to connect to a Wi-Fi network with internet, which is why this Driver Hub is already connected to a network. However, now the focus is on connecting to the Control Hub. </p> | ![](/files/-M_gpRgDw3ovkfkluuWY)                                    |
| Select the name of the Wi-Fi network generated by your Control Hub. The default SSID name starts with either “FIRST-“ or “FTC-“. In this example we want to choose our REV-DEMO Control Hub.                                                                                                                       | ![](/files/-M_gqGk9-lt7AIL8rVWs)                                    |
| <p>Enter the password to the Wi-Fi network in the password field. This defaults to “password”. Press <strong>CONNECT</strong>.</p><p><br>After pressing connect, press the back arrow at the bottom of the display until you return to the main driver station screen.</p>                                         | ![](/files/-M_gq_TVruZkGvhkuwAh)                                    |
| After a couple of seconds, the Driver Station page will indicate the network name, a ping time, and battery voltage.                                                                                                                                                                                               | ![](/files/-M_gqpSMiDx_RYjRMo8b)                                    |

**Your Driver Hub is now paired with your Control Hub!**
{% endtab %}

{% tab title="Other Supported Android Device" %}
{% hint style="danger" %}
This section assumes you have gone through the process of setting up your Driver Station Android Device. If this is not the case please go to [Configuring Your Android Device ](/duo-control/legacy/configuring-a-driver-station-android-device.md)and go through the process of configuring an Android Device to act as the Driver Station.
{% endhint %}

|                                                                                                                                                                                                                                                                           |                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Power on your Android Device by holding down the power button.                                                                                                                                                                                                            | ![Image result for zte phone](/files/-M8N18fjvFjbjJcnANDz) |
| Open the Driver Station application from the HOME Screen.                                                                                                                                                                                                                 | ![](/files/-M8N18fk5uDSGC7DT5LD)                           |
| On the Driver Station page, open the menu from the top right corner, then select **Settings.**                                                                                                                                                                            | ![](/files/-M8N18floDDo2RnX2__D)                           |
| Select, **Pairing Method.**                                                                                                                                                                                                                                               | ![](/files/-M8N18fmOemGCZnRJ3us)                           |
| Select, **Control Hub**.                                                                                                                                                                                                                                                  | ![](/files/-M8N18fnRrs7xOrlFg6e)                           |
| Select, **Pair with Robot Controller**.                                                                                                                                                                                                                                   | ![](/files/-M8N18fohtmbyAHd97NI)                           |
| Select **Wifi Settings**.                                                                                                                                                                                                                                                 | ![](/files/-M8N18fpDdgNWw-6v0lx)                           |
| Select the name of the Wifi network generated by your Control Hub. The default SSID name starts with either “FIRST-“ or “FTC-“.                                                                                                                                           | ![](/files/-M8N18fqsH_qbCzgV4My)                           |
| <p>Enter the password to the Wifi network in the password field. This defaults to “password”. Press <strong>CONNECT</strong>.</p><p><br>After pressing connect, press the back arrow at the bottom of the display until you return to the main driver station screen.</p> | ![](/files/-M8N18fr7vKbXDYOweH1)                           |
| After a couple of seconds, the Driver Station page will indicate the network name, a ping time, and battery voltage.                                                                                                                                                      | ![](/files/-M8N18fssUOJGLpjTTGG)                           |

**Your Driver Station is now paired with your Control Hub!**
{% endtab %}
{% endtabs %}
