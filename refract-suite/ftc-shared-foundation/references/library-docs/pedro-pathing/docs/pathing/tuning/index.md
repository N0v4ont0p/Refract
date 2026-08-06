> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/index.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Tuning
---

import {Step, Steps} from "fumadocs-ui/components/steps";
import Link from "next/link";

<Steps>
    <Step>
        <h3><Link href="/docs/pathing/tuning/setup">Setup</Link></h3>

        In this step, you set constants for your follower.
    </Step>
    <Step>
        <h3><Link href="/docs/pathing/tuning/swerve/swerve-setup">Swerve</Link></h3>

        In this step, you set constants such as your motor names and directions for swerve (if using swerve).
    </Step>
    <Step>
        <h3>
            <Link href="/docs/pathing/tuning/localization">Localization</Link>
        </h3>

        This allows for your robot to know its location on the field.
    </Step>
    <Step>
        <h3><Link href="/docs/pathing/tuning/velocity">Velocity Tuners</Link></h3>

         Determines the forward vs lateral velocity of your robot.
    </Step>
    <Step>
        <h3><Link href="/docs/pathing/tuning/heading">Heading Tuner</Link></h3>

        The heading PIDF corrects for the robot's heading while following the path.
    </Step>
    
</Steps>

After setting up, you have to decide which following algorithm you would like to use.

#### New **predictive braking**

Which automatically tunes in a few minutes and has faster but less customizable braking. Only requires running the automatic PredictiveBrakingTuner and determining a P value.
Tuning process is here: <Link href="/docs/pathing/tuning/drive-algorithm/predictive/configuration">Tuning Predictive Braking</Link>

### OR

#### **PIDFs** of translational, drive, and centripetal

Which requires 3 manual tuners and two more automatic tuners.
Allows for more control of the robot's behavior.
These are the steps for tuning the PIDFs:  

<Steps>
    <Step>
        <h3><Link href="/docs/pathing/tuning/drive-algorithm/pidfs/zero-power-accel">Zero Power Acceleration Tuners</Link></h3>

        These tuners automatically determine the natural deceleration behavior of your robot.
    </Step>
    <Step>
        <h3><Link href="/docs/pathing/tuning/drive-algorithm/pidfs/tuning">PIDF Tuners</Link></h3>

        This step is where you tune translational and drive PIDFs.
    </Step>
    <Step>
        <h3><Link href="/docs/pathing/tuning/drive-algorithm/pidfs/centripetal">Centripetal Force
            Tuner</Link></h3>

        This step consists of tuning a constant that accounts for
        centripetal force.
    </Step>
</Steps>
