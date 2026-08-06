> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system.md).

# Updating Operating System

The Control Hub’s Operating System is field upgradable. New updates are released to incorporate fixes, improvements, and new features as they are developed. &#x20;

There are two ways you can update the Operating System. It is recommended to use the [REV Hardware Client](/duo-control/managing-the-control-system/updating-operating-system.md#using-the-rev-hardware-client), as it will automatically notify the user if the Hub's Operating System is out of date, download the latest OS, and install the OS on the device. The second way utilizes the FIRST Robot Controller Console.  For using the FIRST Robot Control Console, you will need to download the latest Operating System.

<p align="center"><a href="https://github.com/REVrobotics/REV-Software-Binaries/releases/download/chos-1.1.6/controlHubOS-1.1.6.zip" class="button primary" data-icon="download">Download the Control Hub OS Version 1.1.6</a></p>

{% hint style="info" %}
Updating the Operating System can take some time depending on the size of the update. Expect the update to take approximately 5 minutes to fully complete, and keep the Control Hub powered during this process.
{% endhint %}

{% hint style="warning" %}
The following procedure works with Control Hubs with the part number REV-31-1595. For support using the REV-31-1152 Control Hub v0, please reach out to REV support (<support@revrobotics.com>).
{% endhint %}

## Using the REV Hardware Client&#x20;

| Steps                                                                                                                                                                                                                                                                                     |                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Power on the Control Hub, by plugging the 12V Slim Battery ([REV-31-1302](https://www.revrobotics.com/rev-31-1302/)) into the XT30 connector labeled “BATTERY” on the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)).                                              | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png](/files/-M8N18gHM0EmnJzRcHEz)    |
| <p>The Control Hub is ready to connect with a PC when the LED turns green. </p><p></p><p><strong>Note:</strong> With Robot Controller Application versions 5.5 and below the light will blink blue every \~5 seconds. Please<a href="/pages/-M7xOwF2OY_xo7GdiC1I"> update </a>to 6.0.</p> | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\rect22073.png](/files/-MIym3ENg0UyQJ60AUhH) |
| Plug the Control Hub into the PC using a USB-A to USB-C Cable ([REV-11-1232](https://www.revrobotics.com/rev-11-1232/))                                                                                                                                                                   |                                                                                                                      |

Start up the REV Hardware Client. Once the hub is fully connected, it will show up on the front page of the UI under the **Hardware Tab**. Select the Control Hub.&#x20;

![](/files/-MGJhqYWj4hhfVFI930Y)

After selecting the Connected Hardware, the Update tab will pop up.  Under **Control Hub Operating System** select Download.

![](/files/-MGJhz2RYl00wfxKPaX7)

Once the OS has downloaded, select Update.&#x20;

![](/files/-MGJlEbvs2GJpS16ZJjD)

Keep the Control Hub powered on while the upload finishes.

![](/files/-MGJlMj8Sj7-1kTxzO26)

A successful upload will be denoted by the "Update Verification Succeeded" message highlighted in the image below. Once the upload is successful, the install will begin.&#x20;

Keep the Control Hub powered while the update is installed. The Control Hub will reboot to complete the update.

![](/files/-MGJlToDh6Ol9qOTBemV)

When the OS update has completed, a status message "Operating System update complete." The status for the Control Hub Operation System will also change to "Up-to-Date."

{% hint style="warning" %}
When using OS 1.1.2 or newer, the Control Hub operates by default on the 5Ghz band. You may need to update the [Wi-Fi settings](/duo-control/menu/control-hub-gs/updating-wifi-settings.md) depending on what [Driver Station device](/duo-control/menu/control-hub-gs/updating-wifi-settings.md#legal-phones-and-wifi-band-capabilites) you are using.
{% endhint %}

![](/files/-MGJlXfS-UACbHjrq00g)

## Using the Robot Controller Console&#x20;

<p align="center"><a href="https://github.com/REVrobotics/REV-Software-Binaries/releases/download/chos-1.1.6/controlHubOS-1.1.6.zip" class="button primary" data-icon="download">Download the Latest REV Control Hub Operating System - Version 1.1.6</a></p>

{% hint style="warning" %}
When updating from OS 1.1.1 or earlier to OS 1.1.2 or later, the Control Hub will switch to the 5 GHz band, regardless of the previous Wi-Fi band setting. Some devices do not support 5 GHz Wi-Fi, and will not be able to connect to the Control Hub wirelessly while it is using the 5 GHz Wi-Fi band. To switch to the 2.4 GHz band without needing a computer, see the [Changing Wi-Fi Band section](/duo-control/managing-the-control-system/ch-wifi.md#changing-wi-fi-band).
{% endhint %}

| Step                                                                                                                                                                                                                                         | Image                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Power on the Control Hub, by plugging the 12V Slim Battery ([REV-31-1302](https://www.revrobotics.com/rev-31-1302/)) into the XT30 connector labeled “BATTERY” on the Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)). | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png](/files/-M8N18gHM0EmnJzRcHEz)    |
| The Control Hub is ready to connect with a PC when the LED turns green. Note: the light blinks blue every \~5 seconds to indicate that the Control Hub is healthy.                                                                           | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\rect22073.png](/files/-M8N18gICw6_gms8beSs) |
| Connect to the Control Hub’s Wi-Fi Network. If it is not renamed, the name will begin with either “FIRST-“ or “FTC-“.                                                                                                                        | ![A picture containing computer, white&#xA;&#xA;Description automatically generated](/files/-M8N18gJvq-glVmBeshZ)    |
| Open a browser and navigate to the FIRST Robot Controller Console (type 192.168.43.1:8080 in the navigation bar). Select the Manage Tab.                                                                                                     | ![A picture containing drawing, knife&#xA;&#xA;Description automatically generated](/files/-M8N18gK8YnBXOaVMPqJ)     |
| Scroll down to “Update Control Hub Operating System” and press the “Select Update File” button.                                                                                                                                              | ![A screenshot of a cell phone&#xA;&#xA;Description automatically generated](/files/-M8N18gLcSHx-f_DO4M7)            |
| Choose the latest version downloaded in Step 1 and press the “Update & Reboot” button.                                                                                                                                                       | ![](/files/-M8N18gMBdooY7y_JfmB)                                                                                     |
| Keep the Control Hub powered while the upload finishes.                                                                                                                                                                                      | ![A screenshot of a cell phone&#xA;&#xA;Description automatically generated](/files/-M8N18gNlaiDDZx-afiL)            |
| Keep the Control Hub powered while the update is installed. The Control Hub will reboot to complete the update.                                                                                                                              | ![A screenshot of a cell phone&#xA;&#xA;Description automatically generated](/files/-M8N18gOtZlha2zV0M1h)            |
| When the OS update has completed, the Control Hub LED will switch from blue, back to its normal blink pattern.                                                                                                                               | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\rect22073.png](/files/-M8N18gP0Mwe-Yzn3xRm) |
| Reconnect your computer to the Control Hub network and verify that the update was a success.                                                                                                                                                 | ![A screenshot of a cell phone&#xA;&#xA;Description automatically generated](/files/-M8N18gQaAA6Yvu7Ry0a)            |
