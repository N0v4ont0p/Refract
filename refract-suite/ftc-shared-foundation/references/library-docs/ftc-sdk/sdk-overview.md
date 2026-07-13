> Source: https://ftc-docs.firstinspires.org/en/latest/ftc_sdk/overview/index.html · Fetched: 2026-07-12

# FIRST Tech Challenge Software Development Kit — Overview

## Purpose and Components

The FTC SDK is "the collection of tools for developing software and executing it on a _FIRST_ Tech Challenge robot." It encompasses multiple applications and resources:

**Core applications:**
- Driver Station App (includes Self-Inspect and Robot Configuration features)
- Robot Controller App (supporting Blocks and OnBot Java programming environments)
- Android Studio Project for advanced development

**Additional resources:**
- Javadoc reference documentation
- Season-specific assets (TensorFlow models, Vuforia databases)

## Development and Release Structure

The Technology Team maintains SDK development within a private GitHub repository to safeguard future game details and features in progress. Upon release readiness, the SDK is exported and published to the public [FtcRobotController repository](https://github.com/FIRST-Tech-Challenge/FtcRobotController).

**Release components:**
- Built APK files for the Driver Station and Robot Controller
- Android Studio project source code (zip and tar.gz formats)
- Documentation and seasonal assets

The public repository is one-way distribution only — pull requests aren't accepted, though teams may fork or clone the code and submit issues for consideration.

## Release Schedule

- **Kickoff Release** — deployed shortly after season kickoff.
- **Update/Patch Releases** — released during the season for critical fixes.
- **Offseason Release** — prepares teams for architectural changes.

## Release Notes Components

- **Breaking Changes** — API or architectural modifications affecting existing implementations.
- **Enhancements** — new capabilities or improvements with user impact.
- **Bug Fixes** — resolved issues, particularly ones that previously required workarounds.
