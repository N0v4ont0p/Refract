> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/localization/index.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Localization
---

import { Card, Cards } from "fumadocs-ui/components/card";
import { Callout } from "fumadocs-ui/components/callout";


There are many localizers for you to choose from. If you don't have any, you
can use your drive motor encoders.

All localizers except for the OTOS localizer
use a pose exponential method of localization, a way of turning movements
from the robot's coordinate frame to the global coordinate frame.

## Localizers

**Select your localizer below and follow the instructions to tune it. Once
your localizer is tuned, come back to this page.**

<Cards>
  <Card href="/docs/pathing/tuning/localization/drive-encoder" title="Drive
    Encoder
    Localizer"
        description="A localizer that uses the drive motor encoders."/>
  <Card href="/docs/pathing/tuning/localization/two-wheel" title="Two Wheel
    Localizer" description="A localizer that uses two odometry wheels."/>
  <Card href="/docs/pathing/tuning/localization/three-wheel"
        title="Three Wheel Localizer"
        description="A localizer that uses three odometry wheels."/>
  <Card href="/docs/pathing/tuning/localization/three-wheel-imu"
        title="Three Wheel + IMU Localizer"
        description="A localizer that uses three odometry wheels and an IMU."/><Card
  href="/docs/pathing/tuning/localization/pinpoint" title="Pinpoint Localizer"
  description="A localizer that uses the goBILDA Pinpoint Odometry Computer."/><Card
  href="/docs/pathing/tuning/localization/otos" title="OTOS Localizer"
  description="A localizer that uses the SparkFun Optical Tracking Odometry
    Sensor."/>
</Cards>

## Localization Test

After completing the tuning steps described in your localizer, you can test the accuracy of it.

1. Run the `Tuning` OpMode, then navigate under to `Localization Test`
2. On your computer, connect to your robot's Wi-Fi, and navigate to Panels or the FTC Dashboard. Panels is accessible at the ip address `192.168.43.1:8001` when connected to robot wifi.
3. You should see the robot's position on the field.
4. Observe the movements, make sure moving forward increases `x` and strafing left increases `y`.
