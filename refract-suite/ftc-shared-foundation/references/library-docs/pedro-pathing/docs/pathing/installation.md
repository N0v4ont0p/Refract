> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/installation.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Installation
---

import PedroImplementation from "@/app/PedroImplementation";

There are two ways to install Pedro Pathing.

## Using the Quickstart

The quickstart is the easiest way to install Pedro Pathing.

1. In Android Studio, go to `Main Menu -> File -> New -> Project from
Version Control`. For the URL, enter
`https://github.com/Pedro-Pathing/Quickstart.git`.
2. **OR** run `git clone https://github.com/Pedro-Pathing/Quickstart.git`.
Make sure you have [git](https://git-scm.com/) installed first.

That's it! You have now installed Pedro Pathing.

## Manually

In your `build.dependencies.gradle`, add the following to the `repositories
{ }` block:

```groovy
maven { url = "https://mymaven.bylazar.com/releases" }
```

Then, add the following to the `dependencies { }` block:

<PedroImplementation/>
```groovy
implementation 'com.bylazar:fullpanels:1.0.12'
```

Next, perform a Gradle sync by pressing "sync now" in the blue banner that
has appeared.

Then, navigate to `File > Project Structure > Modules` and change the `Compile Sdk Version` to 34 for `FtcRobotController` and `TeamCode`.
Then press `Apply` and `OK`.

Lastly, copy the files from the [`pedroPathing` package in the quickstart](https://github.com/Pedro-Pathing/Quickstart/tree/master/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedroPathing)
into your code.
