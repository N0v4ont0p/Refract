> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware.md).

# Updating Firmware

## Updating the Expansion Hub Firmware

There are two boards within the Control Hub: an Expansion Hub and an Android controller. The Expansion Hub board built into the Control Hub, facilitates a line of communication between the built in Robot Controller and the motors, servos, and sensors. In order to improve the quality of the Hubs, REV Robotics will release firmware updates for the Expansion Hub. When a firmware release occurs, both Control Hub and Expansion Hub users will need to update their Expansion Hub firmware to the newest version. &#x20;

There are two ways to update the Expansion Hub Firmware. It is recommended to use the [REV Hardware Client](/duo-control/managing-the-control-system/updating-firmware.md#using-the-rev-hardware-client) as it will automatically notify the user if the Hub's firmware is out of date, download the latest firmware, and install on the device. The second set of steps utilizes the FIRST Robot Controller Console.&#x20;

To use the FIRST Robot Controller Console, the *Manage* interface is needed to upload the firmware file to the Control Hub. You can then use a Driver Station that is connected to the Control Hub to initiate the firmware update. You can download the latest firmware below.

## Using the REV Hardware Client

### Control Hub

{% hint style="warning" %}
In order to use the REV Hardware Client for firmware updates, the Robot Controller Application must first be updated to version 5.5. After updating the application you may need to close out of the REV Hardware Client in order for the firmware update to be available.&#x20;
{% endhint %}

| Steps                                                                                                                                                                                                                                                                                     |                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Power on the Control Hub, by plugging the 12V Slim Battery ([REV-31-1302](https://www.revrobotics.com/rev-31-1302/)) into the XT30 connector labeled “BATTERY” on the Control Hub.                                                                                                        | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png](/files/-M8N18gHM0EmnJzRcHEz)    |
| <p>The Control Hub is ready to connect with a PC when the LED turns green. </p><p></p><p><strong>Note:</strong> With Robot Controller Application versions 5.5 and below the light will blink blue every \~5 seconds. Please<a href="/pages/-M7xOwF2OY_xo7GdiC1I"> update </a>to 9.0.</p> | ![C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\rect22073.png](/files/-MIym3ENg0UyQJ60AUhH) |
| Plug the Control Hub into the PC using a USB-A to USB-C Cable ([REV-11-1232](https://www.revrobotics.com/rev-11-1232/))                                                                                                                                                                   |                                                                                                                      |

Startup the REV Hardware Client. Once the Control Hub is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Control Hub.&#x20;

![](/files/-MGL2APuY8U4fo3t11-e)

After selecting the Connected Hardware the Update tab will pop up.  Under **Hub Firmware** select Download.

![](/files/-MGP0lCsoWn6-eXFK0Mb)

Once the firmware has downloaded, select Update.&#x20;

![](/files/-MGP16QS_9wDJdsaoslU)

When the firmware update has completed a status message "Firmware successfully updated" The status for the Hub Firmware will also change to "Up-to-Date."

![](/files/-MGOzmNjvHbkulV0CcZ-)

### Expansion Hub&#x20;

{% embed url="<https://youtu.be/pCNbb050D7c>" %}

Plug the Expansion Hub into a PC using a USB-A to Mini USB Cable.&#x20;

Startup the REV Hardware Client. Once the hub is fully connected it will show up on the front page of the UI under the **Hardware Tab**. Select the Expansion Hub.&#x20;

![](/files/-MGQCMIJLF3ht3rX3HfL)

After selecting the Connected Hardware the Update tab will pop up.  Under **Hub Firmware** select Download.

![](/files/-MGQCJfKeWakIibCEHXK)

Once the firmware has downloaded, select Update.&#x20;

![](/files/-MGQD1sC5d_TUcdhHEDr)

When the firmware update has completed a status message "Firmware successfully updated" The status for the Hub Firmware will also change to "Up-to-Date."

![](/files/-MGQDgXCpQFBAcDaQt-p)

## Using the Robot Controller Console

### Control Hub

<p align="center"><a href="https://www.revrobotics.com/content/sw/REVHubFirmware_1_08_02.bin" class="button primary" data-icon="download">Download the Latest REV Hub Firmware - Version 1.8.2</a></p>

| <p>1. Download the latest firmware from the above link then <a href="/pages/-M8HQ3AqFTANiB9pLkYj#web-browser">connect the computer via Wi-Fi </a>to the Control Hub or RC phone. Follow the instructions to open the Robot Controller Console in your web browser.<br></p>                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>2. Click on the Manage tab, scroll down to Update REV Hub Firmware.<br><img src="/files/cicgKNdajLojzVE5bSkI" alt=""></p><p>See if the grey box (see green arrow, above) offers the latest firmware version, included or bundled with the RC app.</p>                                                                                                                                                                                          |
| <p>3. If not, click the “Select Firmware…” box. Navigate to the desired firmware file stored on the computer, and select it.</p><p></p><p>As part of the update process, that selected firmware file will be stored on the Control Hub or RC phone, in a subfolder called FIRST/updates/Expansion Hub Firmware.</p><p>Current and older firmware files can be found on the <a href="/pages/-M7xOlEpyBhGY37DIukW">Firmware Changelog page</a>.</p> |
| <p>4. Now click the box called “Update to…” or “Update using…” (see green arrow).</p><p><img src="/files/JtaOKFXp3jP06M5P3MDc" alt="" data-size="original"></p><p></p>                                                                                                                                                                                                                                                                            |
| 5. At the confirmation prompt, click the blue box “Update Hub Firmware”. Wait for the process to finish; do not unplug the Hub or restart the robot.                                                                                                                                                                                                                                                                                              |

### Expansion Hub&#x20;

{% hint style="info" %}
To update an Expansion Hub with the Robot Controller Console, you will follow the same steps as the Control Hub, but you will need to connect the Expansion Hub to the Control Hub via a USB-A to USB Mini cable. Connecting over an RS485 cable will not allow the Expansion Hub to update. &#x20;
{% endhint %}

<p align="center"><a href="https://www.revrobotics.com/content/sw/REVHubFirmware_1_08_02.bin" class="button primary" data-icon="download">Download the Latest REV Hub Firmware - Version 1.8.2</a></p>

| 1. Connect the Expansion Hub to the Control Hub via a USB-A to USB Mini cable, making sure to disconnect the RS485 cable. You should never have a Control Hub and Expansion Hub connected via USB and RS485 at the same time.                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2. Download the latest firmware from the above link then [connect the computer via Wi-Fi](/duo-control/menu/control-hub-gs/connect-to-the-control-hub-robot-control-console.md#web-browser) to the Control Hub or RC phone. Follow the instructions to open the Robot Controller Console in your web browser                                                                                                                                      |
| <p>3. Click on the Manage tab, scroll down to Update REV Hub Firmware.<br><img src="/files/cicgKNdajLojzVE5bSkI" alt=""></p><p>See if the grey box (see green arrow, above) offers the latest firmware version, included or bundled with the RC app.</p>                                                                                                                                                                                          |
| <p>4. If not, click the “Select Firmware…” box. Navigate to the desired firmware file stored on the computer, and select it.</p><p></p><p>As part of the update process, that selected firmware file will be stored on the Control Hub or RC phone, in a subfolder called FIRST/updates/Expansion Hub Firmware.</p><p>Current and older firmware files can be found on the <a href="/pages/-M7xOlEpyBhGY37DIukW">Firmware Changelog</a> page.</p> |
| <p>5. You can confirm that both the Control Hub and the Expansion Hub will be updated to the firmware version you selected. (see orange box)<br><br>Now click the box called “Update to…” or “Update using…” (see green arrow).</p><p></p><p><img src="/files/gPVbfqxzQfm2npQMUUne" alt=""></p>                                                                                                                                                   |
| 6. At the confirmation prompt, click the blue box “Update Hub Firmware”. Wait for the process to finish; do not unplug the Hub or restart the robot.                                                                                                                                                                                                                                                                                              |
