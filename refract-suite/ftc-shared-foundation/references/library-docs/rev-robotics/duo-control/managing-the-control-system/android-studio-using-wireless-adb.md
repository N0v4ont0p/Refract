> Source: https://docs.revrobotics.com/duo-control/managing-the-control-system/android-studio-using-wireless-adb.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/managing-the-control-system/android-studio-using-wireless-adb.md).

# Android Studio - Deploying Code Wirelessly

Android Debug Bridge (ADB) utility is the tool used by Android Studio to connect and control Android devices, like the Control Hub. Android Studio, using ADB, allows users to build and install the Robot Controller app onto their Control Hub. &#x20;

{% embed url="<https://youtu.be/yFbMWZbwuhQ>" %}

By default ADB supports using a hardwire connection via USB to deploy code to Android Devices. ADB does support a wireless mode where the build and install process is sent over Wi-Fi. The Control Hub is configured to support ADB wireless connections on port 5555. To deploy code over the Wi-Fi connection the user will need to set up Wireless ADB.

## Setting Up Wireless ADB using the REV Hardware Client

To set up wireless ADB using the REV Hardware Client you will need a laptop or PC with both [Android Studio](https://ftc-docs.firstinspires.org/en/latest/programming_resources/android_studio_java/Android-Studio-Tutorial.html) and the [REV Hardware Client](/duo-control/managing-the-control-system/rev-hardware-client.md) installed.

<table data-header-hidden><thead><tr><th width="324"></th><th></th></tr></thead><tbody><tr><td></td><td></td></tr><tr><td>Power on the Control Hub, by plugging the 12V Slim Battery (<a href="https://www.revrobotics.com/rev-31-1302/">REV-31-1302</a>) into the XT30 connector labeled “BATTERY” on the Control Hub.</td><td><img src="/files/-M8N18gHM0EmnJzRcHEz" alt="C:\Users\Rachel\AppData\Local\Microsoft\Windows\INetCache\Content.Word\g20714.png"></td></tr><tr><td>The Control Hub is ready to connect with a PC when the LED turns from blue to green. </td><td><img src="/files/awmuvXt3wbS34NrmRIkU" alt="" data-size="original"></td></tr><tr><td><p>Connect to the Wi-Fi Network created by the Control Hub</p><p></p><p>Note: <a href="/pages/-M8N-OOVK_yoj-t3tsS8#rev-hardware-client">Connect to the REV Hardware Client over USB if the password needs resetting.</a></p></td><td> <img src="/files/-MIZrXbjd5yr9egrBTwf" alt="" data-size="original"></td></tr><tr><td>Open the REV Hardware Client and confirm the Control Hub is connected over Wi-Fi</td><td><img src="/files/-MI_4GBeR33Ryw8vzUdF" alt="" data-size="original"> </td></tr></tbody></table>

{% hint style="success" %}
The Control Hub should be listed in the Android Studio devices dropdown
{% endhint %}

![](/files/-MI_mTZHnTHdt43I7yrx)
