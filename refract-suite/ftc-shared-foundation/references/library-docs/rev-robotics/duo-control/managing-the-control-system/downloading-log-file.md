> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/downloading-log-file.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/downloading-log-file.md).

# Accessing Log Files

When troubleshooting problems with the REV Control System log files provide indicators of what the status of the Control Hub or Expansion Hub were during an event. Often the first log that is considered is the Robot Controller log, as they are relatively easy to decipher and can be pulled from the Control Hub or Robot Controller. While working through the [troubleshooting process](/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system.md) looking through the XML files, Wi-Fi Log, or Updater Logs in addition to the Robot Controller logs help to paint a full picture.

There are a few ways to access the log files depending on if you are looking to troubleshoot or downloading the log files for REV support to help. &#x20;

## Log Viewer - REV Hardware Client

The REV Hardware Client has a Log Viewer that makes it easier to parse overall log files. Through a series of filters, tags, and a search function makes it easy to see what is happening on the Control Hub or Driver Hub during any OpMode run.

To access the Log Viewer, head to the Utilities Tab.&#x20;

![](/files/-MgHV9aAwLZOuFlhM7uS)

From there you can select and open log files for connected devices or for ones downloaded onto the computer.

![](/files/-MgHVwfKsz160zA1qObL)

{% hint style="info" %}
For more information on the Log Viewer check out the [REV Hardware Client User's Manual](https://docs.revrobotics.com/rev-hardware-client/).
{% endhint %}

## Downloading Log Files

When sending logs to REV Support use the REV Hardware Client. The Client will zip all relevant log files, collect some additional information from a form, and then send them to REV for diagnosis. When running through the troubleshooting process at an event, physically connecting to a Control Hub ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) and using the file search of the computer allows access to the files. Alternatively connecting to the Robot Controller Console allows downloading the logs through the manage tab.&#x20;

### REV Hardware Client

1. Provide 12v Power to the Control Hub.
2. Plug the USB-C Cable into the top board of the Control Hub and into a PC with the [REV Hardware Client](/duo-control/managing-the-control-system/rev-hardware-client.md) installed.
3. Select the Control Hub from the Connect Hardware.
4. Click the "Send Diagnostics to REV" Button

![](/files/-MVSK6Ib3beH565LQCEg)

{% hint style="info" %}
There is a short form to fill out with additional information to help REV Support troubleshoot the issue.
{% endhint %}

### File Search&#x20;

#### Using a PC

{% hint style="warning" %}
Mac computers do not support MTP natively; the protocol used to browse files on Android devices. You need to use the Android File Transfer app: <https://www.android.com/filetransfer/>

Windows devices will operate without the need for an additional application.
{% endhint %}

1\. Provide 12V power to the Control Hub.\
2\. Plug the USB-C Cable into the top board of the Control Hub and into a PC\
3.Navigate to This PC\Control Hub v1.0\Internal shared storage. Robot Controller, Wi-Fi, and Updater logs can be found on this level of the file hierarchy.&#x20;

{% hint style="info" %}
The logs are all text files that can either be open via Notepad++ and looked over or sent to REV Support via an email to be further troubleshot. &#x20;
{% endhint %}

4\. While in the This PC\Control Hub v1.0\Internal shared storage location, navigate to a folder called "FIRST." The folder should have XML files with a naming convention that mirrors the names of the robot configuration.&#x20;

#### Using a Mac

1\. Download the Android File Transfer App on your MAC\
2\. Open Android File Transfer.dmg \
3\. Drag Android File Transfer to Applications \
4\. Use the USB-C to USB-A cable that came with your Control Hub (or other relevant Android Device)\
5\. Double-click Android File Transfer\
6\. Navigate to Control Hub v1.0\Internal shared storage. Robot Controller, Wi-Fi, and Updater logs can be found on this level of the file hierarchy.&#x20;

{% hint style="info" %}
The logs are all text files that can either be open via Notepad++ and looked over or sent to REV Support via an email to be further troubleshot. &#x20;
{% endhint %}

7\. While in the Control Hub v1.0\Internal shared storage location, navigate to a folder called "FIRST." The folder should have XML files with a naming convention that mirrors the names of the robot configuration.&#x20;

### Robot Controller Console&#x20;

1\. Open the [Robot Controller Console](/duo-control/menu/control-hub-gs/connect-to-the-control-hub-robot-control-console.md#web-browser) \
2\. Select the **Manage** page \
3\. Press the Download Logs button

![](https://github.com/FIRST-Tech-Challenge/SkyStone/wiki/images/Managing-a-Control-Hub/downloadLogs.jpg)

4\. Check for the robotControllerLog.txt in the Downloads Directory of the Computer \
5\. Open the Logs via a text editor, like Notepad++, to view the contents of the log or send the logs to REV Support

![](https://github.com/FIRST-Tech-Challenge/SkyStone/wiki/images/Managing-a-Control-Hub/notepadplusplus.jpg)
