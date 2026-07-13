> Source: https://rr.brott.dev/docs/v1-0/installation/, https://github.com/acmerobotics/road-runner, https://github.com/acmerobotics/road-runner-quickstart · Fetched: 2026-07-12

# Road Runner — Installation (v1.0.x)

**LEGACY REFERENCE.** RoadRunner is documented here for teams maintaining
existing RoadRunner code. It is not the primary recommended path-following
library in this project anymore.

**Version covered:** RoadRunner **1.0.1** (core/actions modules), FTC bindings
`com.acmerobotics.roadrunner:ftc:0.1.25` — the current version as of this
fetch (GitHub tag v1.0.1, released 2025-01-05). RoadRunner 0.5.x also has a
docs tree (`/docs/v0-5/`) still online for older projects, but 1.0.x is the
actively maintained line and is **not backwards compatible** with 0.5.x.

Repos:
- Core library: https://github.com/acmerobotics/road-runner
- FTC quickstart project: https://github.com/acmerobotics/road-runner-quickstart
- Docs source: https://github.com/acmerobotics/road-runner-docs

## Quickstart method (recommended starting point)

The fastest way to begin is using the quickstart project — a full FTC Android
Studio project with RoadRunner, FTC Dashboard, and tuning utilities
preinstalled.

```
git clone https://github.com/acmerobotics/road-runner-quickstart.git
```

Open it as an FTC project in Android Studio, then proceed to the tuning
guide (see `tuning.md` in this folder).

## Installing into an existing project

**If upgrading from 0.5.x:** remove all references to RoadRunner from your
Gradle files and project first. RoadRunner 1.0.x is **not** backwards
compatible with 0.5.x.

**Step 1 — add the Maven repository.** In `TeamCode/build.gradle`, add this
block between the `android` and `dependencies` sections:

```gradle
repositories {
   maven {
      url = 'https://maven.brott.dev/'
   }
}
```

**Step 2 — add dependencies** at the end of the `dependencies` block:

```gradle
implementation "com.acmerobotics.roadrunner:ftc:0.1.25"
implementation "com.acmerobotics.roadrunner:core:1.0.1"
implementation "com.acmerobotics.roadrunner:actions:1.0.1"
implementation "com.acmerobotics.dashboard:dashboard:0.5.1"
```

**Step 3 — Gradle sync.**

**Step 4 — copy quickstart source files.** Download the quickstart project
from GitHub and copy everything under its `teamcode` folder (including the
`messages` and `tuning` subdirectories) into your project's
`TeamCode/src/main/java/org/firstinspires/ftc/teamcode`.

After this, proceed to tuning (`tuning.md`) or review what changed in 1.0
(`core-concepts.md`).
