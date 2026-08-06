> Source: https://docs.revrobotics.com/rev-hardware-client-2/guides/swerve-calibration.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client-2/guides/swerve-calibration.md).

# Swerve Calibration

1. Verify you have completely assembled your MAXSwerve or EasySwerve Module and have the Steering Motor’s SPARK Flex or SPARK MAX connected to the Module's Through Bore Encoder
2. [Install and open the latest version of the REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client/gs/install)&#x20;
3. Connect the Steering Motor’s SPARK Motor Controller directly to your computer via the included USB-C to USB-A cable
4. Select the Steering SPARK from the list of Connected Devices and navigate to the **Update Tab** to verify your Firmware is up to date.
5. Ensure the Steering SPARK is still selected, and then navigate to **Absolute Encoder** under the **Utilities Tab**.

   <figure><img src="/files/OCxsMuj9eKxAcaxVzB8p" alt=""><figcaption></figcaption></figure>
6. Then, follow the steps below for the Swerve Module that you are calibrating to ensure that the zero position is set correctly.&#x20;

{% tabs %}
{% tab title="EasySwerve Calibration" %}

1. Insert a 1/8in or 3mm Hex Key into the calibration on the top of the EasySwerve Module. You will feel the Hex Key reach the azimuth gear inside of the top cover.

   <figure><img src="/files/5EglVw7D3Pz5kyQ1TU3F" alt="" width="375"><figcaption></figcaption></figure>
2. Rotate the module's wheel manually while applying light pressure to the hex key until it slots into the alignment pocket. The Hex key will travel about 1/4in further into the swerve module when it has aligned.

   <figure><img src="/files/02xE0nIHeLQscsbrgzEH" alt=""><figcaption></figcaption></figure>
3. Click the Zero Encoder button to calibrate the zero position of the absolute encoder to this position.

<figure><img src="/files/KqPZGP9sHRodliz9lqKc" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="MAXSwerve Calibration" %}

1. Put the Calibration Tool on the MAXSwerve module.

   * The Calibration Tool needs to be placed on the MAXSwerve module with the lip facing the module.
   * The MAXSwerve Wheel will only fit in one orientation because of the placement of the wheel's bevel gear. The Calibration Tool is not symmetrical, so you will need to align the bevel gear with the side of the cutout indicated with the orange dot in this image.
   * ![MAXSwerve Calibration tool with an orange dot indicating the side of the cutout that the bevel gear slots into. This part of the cutout is a more complex shape with more corners and curves than the other half of the cutout.](https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=660379553/https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fe0CWwhMSoCEH7NLVoLhF%2Fblobs%2Fn84mZDOOGds2etrx37U2%2FIMG_9306.jpg)![MAXSwerve Calibration tool correctly mounted to a MAXSwerve Module](https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=1860580575/https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fe0CWwhMSoCEH7NLVoLhF%2Fblobs%2FF4f4HMVMC4w9vDDm7xxS%2FIMG_9307.jpg)

   <figure><img src="/files/PhnsK3jAwZtY4r52j27X" alt="" width="563"><figcaption><p>MAXSwerve Drivetrain with all four calibration tools properly installed.</p></figcaption></figure>
2. Rotate the wheel along with the Calibration Tool until the tool's lip firmly drops into place around the MAXSwerve module's edges. Once this happens, the wheel and Calibration Tool will be unable to rotate freely until the tool's lip has been lifted above the edges of the module.
3. Click the Set Zero Offset button to calibrate the zero position of the absolute encoder to this position.

<figure><img src="/files/KqPZGP9sHRodliz9lqKc" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}
