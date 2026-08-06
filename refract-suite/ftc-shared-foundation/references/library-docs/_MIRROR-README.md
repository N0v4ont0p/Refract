> Written: 2026-08-06 (I2 exhaustive documentation sweep)

# How to read this directory

Each library directory now holds **two kinds of file**, and they are not redundant with each other.

## Flat files — curated syntheses

`pedro-pathing/tuning.md`, `ftclib/drivebases.md`, `rev-robotics/…` and their siblings at the top
level of each library directory. These are distilled, human-reviewed summaries written across
earlier phases. They carry things the upstream source does not: known-gap notes, completeness-audit
findings, "this was fetched from the GitHub source because the docs site 403s automated fetches",
and warnings about what a page does *not* cover. **The skills reference these by name** — they are
the entry point, not a legacy artifact.

## Nested subdirectories — exhaustive verbatim mirror

`pedro-pathing/docs/pathing/…`, `ftc-sdk/apriltag/…`, `ftclib/features/…`, etc. These mirror the
upstream documentation tree one-for-one: **every reachable file, not a selection.** Content is
verbatim; only a source-and-fetch-date header is prepended. Use these when the curated file does not
answer the question, or to confirm a curated summary against its source.

Two capture methods, and the difference matters:

- **Repo-backed** (Pedro Pathing, FTC SDK, FTC Dashboard, EasyOpenCV, FTCLib, TickTree) — copied
  from a `git clone` at a pinned commit, recorded in each file's header. Lossless.
- **Publisher markdown** (REV Robotics) — REV serves a `.md` variant of every page (plus an
  `llms.txt` index), so these are the publisher's own markdown, not a conversion. Clean.
- **HTML capture** (Limelight, RoadRunner) — no doc repo and no `.md` endpoint (both probed and
  404), so pages were retrieved as rendered HTML and converted to text. **Formatting is lossier**;
  code blocks and tables survive less cleanly. Each such file says so in its own header.

## Scope boundaries, stated rather than left implicit

Exhaustive means every reachable file *within the library's FTC documentation*. Three boundaries
were drawn on product scope, not on perceived value:

- **REV Robotics** — `docs.revrobotics.com` is a combined FRC + FTC + education site (731 sitemap
  URLs). Sections for a different competition or product (`brushless/` FRC SPARK+NEO, `revlib/`,
  `ion-build/`, `ion-control/`, `frc-kickoff-concepts/`, `first-global/`, the professional-development
  tracks) are out of scope for an FTC suite. FTC-relevant sections are taken in full.
- **RoadRunner** — `rr.brott.dev/docs/v1-0/**` only. The `v0-5` tree on the same site, and the
  `acmerobotics/road-runner-docs` repo (last commit 2022-01), are superseded. Importing them would
  inject outdated API documentation, which is worse than a gap.
- **TickTree** — `docs/` and `README.md`. `PLAN.md` and `RELEASING.md` are the project's internal
  build-process files, not library documentation.

Completeness is no longer checked by hand: `corpus-input-scan.py` compares each library's stored
file count against its live upstream source and reports a gap the same way it reports staleness.
