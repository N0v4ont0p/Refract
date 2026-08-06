> Source: https://docs.revrobotics.com/rev-hardware-client/ion/telemetry.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/ion/telemetry.md).

# Telemetry Tab

{% hint style="danger" %}
Those using REV ION products on REVLib 2026 or newer must use [REV Hardware Client 2](https://docs.revrobotics.com/rev-hardware-client-2).
{% endhint %}

### Connected Devices

Devices available in the REV Hardware Client are shown on the left side of the window. The device that the USB C Cable is connected to will be listed first, followed by any devices connected over CAN.

<div><figure><img src="/files/hp5iY0HkfmHB5Mf2JQZl" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="/files/1DiTe0ASYG3L39eh5jte" alt="" width="375"><figcaption></figcaption></figure></div>

### Available Devices

The below devices are able to provide telemetry and allow the Telemetry Tab to be used.&#x20;

* SPARK MAX
* SPARK Flex
* Power Distribution Hub&#x20;
* Pneumatic Hub
* Devices Connected to the SPARK MAX or SPARK Flex Motor Controllers:
  * NEO Vortex
  * NEO Brushless Motor V1.1
  * NEO 550
  * Brushed DC Motor
  * Through Bore Encoder&#x20;
  * Other inputs connected to the Data Port

## Telemetry Settings

### Signals and Graph

<figure><img src="/files/m9bgtzB9Ek8skkwRwg2C" alt=""><figcaption></figcaption></figure>

1. **Run Motor:** Choose setpoints to run a motor connected to a SPARK MAX using various modes, including position, velocity, and duty cycle.
2. **Signals:** Select the different signals from the SPARK MAX you want to monitor here
3. **Start & Restart Graph:** Start initiates recording of telemetry. Restart will erase the data and start again
4. **Time Span:** Change the time span shown on the x-axis of the graph
5. **Scales:** Different Signals will have different scales for the y-axis. You can change which are shown by clicking the arrows here
6. **Signal Key and Scale Adjustment:** Signals you choose to monitor will be shown here. Click **X** to delete a signal from the graph and **>** to adjust the scale of the signal's graph y-axis
7. **Save Data:** Save your data as a .CSV or image using this menu

### Tuning

<figure><img src="/files/msMoKlsw4QcgKmkZi8ET" alt=""><figcaption></figcaption></figure>

Update PIDF parameters on the fly to tune control loops on the SPARK MAX.

### Parameters

<figure><img src="/files/q9JKFCvvXYobNla77KWt" alt=""><figcaption></figcaption></figure>

Select the arrow to show all configurable parameters within a specific group. For more information on each parameter type see [Configuration Parameters](https://docs.revrobotics.com/brushless/spark-max/parameters).

## Editing the Y-Axis Scale

<figure><img src="/files/BhUkYh0L1k8apBhhAtUP" alt=""><figcaption></figcaption></figure>

1. **Y-Axis Labels:** Select the label you want to view by clicking the arrow at the bottom of the label. In this image the Power Distribution Hub Channel Currents are selected.
2. **Y-Axis Scale:** Use the drop down arrow next to the parameter you would like to change the scale for. Be sure to un-check the "use defaults" box to apply your changes.&#x20;

## Example

<figure><img src="/files/cE08LzwC20ALtmyxtS6s" alt=""><figcaption></figcaption></figure>

In this example the SPARK MAX and NEO Motor were run at 30% power, switching between forwards and backwards several times. The first switch in direction occurs near t=5s where you can see the Applied Output, Position, and Velocity change.&#x20;

## Exporting Data

### Exporting as a Image

This will export a .png image of the of the graph. The whole Time Span x-axis will be exported regardless of the time information was collected. The image below exported a 30 second graph while only 8 seconds of data was recorded.&#x20;

<figure><img src="/files/inBdYwCub69hrFwOKvJo" alt=""><figcaption></figcaption></figure>

### Exporting as a .CSV

This will export a .csv file of the of the values and timestamps.

<figure><img src="/files/bOke6TwqBDNl2DU9JHKQ" alt=""><figcaption></figcaption></figure>

1. **Timestamp:** This is the timestamp that the data was record for each signal in Unix time. Note that different signals may have their data recorded at different times than other signals.&#x20;
2. **Signal Name:** The Label of signal selected when creating your Telemetry graph.
3. **Device Name:** The name of the device and the randomly generated ID assigned to each device when connected to the REV Hardware Client. This is randomly generated each time the device is connected to the REV Hardware Client.
4. **Signal Value:** The value recorded for each Signal Name.

### Record to .CSV

This allows you to select an existing .csv file prior to starting your graph and record the data straight to the .csv file. This allows you export additional data to a previously exported telemetry file without headers to seamlessly add to your existing columns.&#x20;

## Troubleshooting

### roboRio Lockout

**Please be aware of the CAN lockout feature of the ION Control System.** If it has been connected to the roboRIO's CAN bus, a safety feature within all ION Control System Devices and will lock out USB communication. You may be able to change some parameters on select devices but in order to run motors through the telemetry tab disconnecting from the CAN bus and power-cycling the device will release the lock.

## PID Set Up Guide

{% hint style="warning" %}
As of REV Hardware Client version 1.7.0, "Burn Flash" has been renamed to "Persist Perimeters"!
{% endhint %}

1. Under the device list, select your SPARK motor controller.<br>

   <figure><img src="/files/BQDgfHZegBlGMOIyzEYi" alt=""><figcaption></figcaption></figure>
2. Click the "Advanced" tab.<br>

   <figure><img src="/files/ZG3FSuCyNoYKLG3rbbnj" alt=""><figcaption></figcaption></figure>
3. For a SPARK MAX, under the "Alternate Encoder" section, make sure "kDataPortConfig" is set to "Default".<br>

   <figure><img src="/files/EqLQO2KeviTC5QN3Ge4f" alt=""><figcaption></figcaption></figure>
4. Under the "Closed Loop" section, set "kCtrlType" to "Position".<br>

   <figure><img src="/files/HAEIBEhC5q8AUP4Z1tZ1" alt=""><figcaption></figcaption></figure>
5. Under the same section, set "kFeedbackSensorPID0" to "Duty Cycle".<br>

   <figure><img src="/files/ginuGJQRi3wRBueIK3UT" alt=""><figcaption></figcaption></figure>
6. Click "Burn Flash" at the bottom of the page. (Burn Flash has been renamed to Persist Perimeters in v 1.7.0) <br>

   <figure><img src="/files/QPBNQh4BCjBLNStHFwVc" alt=""><figcaption></figcaption></figure>
7. To tune your PID gains, click the "Telemetry" tab.<br>

   <figure><img src="/files/K8X2tChWSjyPHyeX3m2E" alt=""><figcaption></figcaption></figure>
8. Set the "Mode" to "Position".<br>

   <figure><img src="/files/MVA0A7HS9nH16gGBSRrV" alt=""><figcaption></figcaption></figure>
9. Under the "Signals" tab, select "Run Setpoint" and "Duty Cycle Position".<br>

   <figure><img src="/files/2r48M5qfT8Nh1ppaud3T" alt=""><figcaption></figcaption></figure>
10. Click the "Tuning" tab.<br>

    <figure><img src="/files/RmpmiEtrLvvbz4Thyybs" alt=""><figcaption></figcaption></figure>
11. Begin tuning your PID gains! Note that the setpoint in Hardware Client only allows whole numbers, so it would be helpful to set the Duty Cycle Position Factor parameter to something like 360 for degrees.

## Frequently Asked Questions

<details>

<summary>Do I need to use a special type of USB cable?</summary>

You need to use a USB-A to USB-C cable data capable cable. The orange USB cable that comes with most ION devices fits this description.&#x20;

</details>

<details>

<summary>Does the SPARK Flex offer more options than the SPARK MAX?</summary>

As of the 2024 FRC season the SPARK Flex and SPARK MAX offer the same options. New features will become available with future updates to the SPARK Flex that will be free to SPARK Flex owners forever.

</details>

<details>

<summary>Can the units of the telemetry channels be changed?</summary>

No, not at this time. We recommend exporting the data as a .csv file and converting to fit your specific needs.

</details>
