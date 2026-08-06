> Source: https://docs.revrobotics.com/rev-hardware-client/duo/control-hub/update.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/duo/control-hub/update.md).

# Updating a Control Hub

## Update All

Once one or more supported REV Hardware devices are connected that require updates, the **Update All** button will appear.

![](/files/-MGjCjVW_dHNAmAXN9Wd)

Once Update All is selected the REV Hardware Client will confirm the updates for all connected devices. Select Update to download and update all devices.

![](/files/-MGjErceGjEr8KvY2cW_)

## Individual Updates

### Operating System

After selecting the Connected Hardware the Update tab will pop up.  Under **Control Hub Operating System** select Download.

![](/files/-MGixyjaDWTgVUj1s0Bn)

Once the OS has downloaded, select Update.&#x20;

![](/files/-MGiy6TWvvXWgiyo--nA)

Keep the Control Hub powered while the upload finishes.

![](/files/-MGiy9KzwuqCTQEXgeb4)

A successful upload will be denoted by the "Update Verification Succeeded" message highlighted in the image below. Once the upload is successful the install will begin.&#x20;

Keep the Control Hub powered while the update is installed. The Control Hub will reboot to complete the update.

![](/files/-MGiyDVzN2DcbkqtzzC_)

When the OS update has completed a status message "Operating System update complete." The status for the Control Hub Operation System will also change to "Up-to-Date."

![](/files/-MGiyGk02pXKpunN6mkF)

### Firmware

There are two boards within the Control Hub: an Expansion Hub and an Android controller. The Expansion Hub board built into the Control Hub, facilitates a line of communication between the built in Robot Controller and the motors, servos, and sensors. In order to improve the quality of the Hubs, REV Robotics will release firmware updates for the Expansion Hub. When a firmware release occurs, both Control Hub and Expansion Hub users will need to update their Expansion Hub firmware to the newest version.&#x20;

{% hint style="warning" %}
In order to use the REV Hardware Client for firmware updates, the Robot Controller Application must first be updated to version 5.5. After updating the application you may need to close out of the REV Hardware Client in order for the firmware update to be available.&#x20;
{% endhint %}

After selecting the Connected Hardware the Update tab will pop up.  Under **Hub Firmware** select Download.

![](/files/-MGj0qAzTc7Mr6g4o0R-)

Once the firmware has downloaded, select Update.&#x20;

![](/files/-MGj0sS2EGfbxMbyDrMn)

When the firmware update has completed a status message "Firmware successfully updated" The status for the Hub Firmware will also change to "Up-to-Date."

![](/files/-MGj0wC2eXTeO-xE_gP1)

### Robot Controller Application

After selecting the Connected Hardware the Update tab will pop up.  Under **Robot Controller App** select Download.

Once the app has downloaded, select Update.&#x20;

![](/files/-MGj17vo51urYuPTAcKs)

When the Robot Controller Application update has completed a status message "Robot Controller app update complete." The status of the **Robot Controller App** will also change to "Up-to-Date."

![](/files/-MGj19el2_C2inWXlxlO)

##
