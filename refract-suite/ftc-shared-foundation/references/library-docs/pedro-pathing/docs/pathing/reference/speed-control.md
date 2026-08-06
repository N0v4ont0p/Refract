> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/speed-control.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Speed Control
description: Controlling the speed that Pedro Pathing follows at
---

import { Callout } from 'fumadocs-ui/components/callout'
import {Accordions, Accordion} from "fumadocs-ui/components/accordion";

## Overview
Pedro Pathing has no built in movement speed or velocity limiter. 
The best method currently is limiting motor powers.
There are 3 main ways you can limit the motor power that Pedro Pathing can use.

## Methods
<Accordions type="single">
    <Accordion title="Global">
      This method is recomended if you never want Pedro Pathing to exceed a certain motor power.
      The global default max power is stored in the `Constants` class, 
      Specificaly, the `driveConstants` variable.
      <Callout title="Note" type="info">
        This is only garunteed to work on mecanum drivetrains using the `MecanumConstants`
      </Callout>
      Simply change the value in `.maxPower(1)` (0 to 1).
    </Accordion>
    <Accordion title="Per Path">
      This method is recomended if you want to slow down a particular path.
      When following a path, you can use `follower.followPath(pathChain, maxPower, holdEnd)`.
      <Callout title="Note" type="warning">
        When using the `maxPower` parameter, you must also include the `holdEnd` parameter.
        The default for this value is `true`.
      </Callout>
      `maxPower` is a number from 0 to 1.
    </Accordion>
    <Accordion title="Multiple Paths">
      `follower.setMaxPower(maxPower)` will set the speed of the follower until you change it again.
      `maxPower` is a number from 0 to 1.
    </Accordion>
</Accordions>