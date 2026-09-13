## Short answer: no. Don't use HIVE AprilTags to reset odometry in BIOBUZZ, and definitely not on every loop.

In BIOBUZZ the AprilTags sit on the underside of the HIVE's CELLs, and the HIVE moves. The FTC SDK v12.0 README says these tags are "not suitable for absolute Field Localization". That's recorded in `season-extensions/biobuzz-2026-27.yaml` as code constraint `no-apriltag-absolute-localization`. Refract's SDK docs note adds that in the v12.0 library, BIOBUZZ clusters carry no field pose (origin 0,0,0, identity rotation). So `robotPose` from a HIVE tag isn't a field pose. Each TIP flips the HIVE and changes which tags face the floor (manual §9.9 plus the season file). Resetting odometry to that value every loop replaces drift you can measure with a position that jumps whenever the HIVE tips.

Two things to know before relying on this:
- The call site that resets "every loop" isn't in the files I was given. `HiveRelocalizer.fieldPose()` only returns a pose. My comment about per-loop resets is based on your description, not on code I've read.
- `no-apriltag-absolute-localization` has no detect pattern, so the linter doesn't catch it. It came from reading the season file, not from a script.

Season checked: biobuzz-2026-27, from your config's `_meta.season`. The rules corpus is up to date through Team Update 00 (`check_freshness.py`: CURRENT).

## 1. Script findings (confirmed by the linters)

**`config_lint.py`**
- **`HiveRelocalizer.java:11-12`, SDK v12.0 AprilTag API change** (source: SDK v12.0 README, Breaking Changes; not a manual rule). The loop reads `detection.id` from the base `AprilTagDetection`. According to the season file, SDK 12.0.0 removed `id`, `metadata` and `center` from that type, which is a compile error; this was verified 2026-09-13 by compiling against the 12.0.0 libraries. `robotPose` still compiles. Tag identity now needs an `instanceof AprilTagSingleDetection` / `AprilTagClusterDetection` check and a cast. I haven't compiled this myself; the claim comes from the season file.
- **`TelemetryHelper.java:3-9`, rule R704.** `MultipleTelemetry` plus `FtcDashboard.getInstance().getTelemetry()` runs every time, with no way to turn it off.
  - I checked the rule: `rules.py verify R704` passes and `lookup` returns the text.
  - Verdict: illegal as written for a competition build.
  - Citation: R704.D, "Additional logging/streaming services, such as those hosted by third party plugins and tools such as FTC Dashboard, FTControl Panels, and others are prohibited."
  - Reasoning: the wrapper streams to Dashboard with no switch. Using it at practice is fine, but it has to be removed or disabled for events.
- **`TurretAim.java`, possible config mismatch.** Your config says `turret: none`, but this code references a turret. Current config doesn't use it. Either the code is stale or the config is wrong; I'm not assuming which.
- **`aim_vision` wasn't checked.** Its token list is deliberately empty because vision classes serve other purposes too. So seeing no `aim_vision` findings proves nothing. Note that your config says `aim_vision: none` while the code uses an `AprilTagProcessor`. The config has no field for "vision used for localization", which may be a gap for ftc-team-config to handle.

**`failure_mode_lint.py`**
- **bus_factor (high):** 16 of 16 commits have one author. The script's own caveat: this measures how concentrated commit authorship is, not proof of a single author. It's also weak here because the fixture lives inside the Refract repo, so the history isn't really the team's. Treat it as something to look into, not a settled finding.
- 0 OpModes and 0 PID or tuning-constant files were scanned. No OpMode, auto or localizer/`Constants` file was provided, so the telemetry, god-OpMode and default-tuning checks found nothing because there was nothing to check.

## 2. Review against your robot (mecanum drivetrain, Pedro Pathing, raw LinearOpMode)

- **Corpus pattern `19043-C-ekf-localizer`** (team 19043, `subsystems/drive/localizers/nMergeLocalizer.java:78-215`). Stored confidence: medium. Provenance: independently-derived. Seen in DECODE (decode-2025-26).
  - What it does: odometry predicts the pose every loop. Pinpoint corrections either hard-reset or soft-correct depending on a distance gate. AprilTag corrections compare against a time-interpolated past pose so camera lag isn't read as a position jump.
  - Stored season scope: the AprilTag update step "relies on DECODE fixed field tags, which BIOBUZZ lacks."
  - Notes carried from the corpus: author-flagged as interim ("now kalman filter exists, hopefully it works??"), and the covariance constants are season- and robot-specific tuning.
  - What carries over to BIOBUZZ is the structure, not the tag source: odometry is the main pose, outside corrections are gated and soft, and camera lag is compensated. An ungated, unlagged hard reset every loop is the opposite of that structure, even for a source that would be valid.
- **Failure mode "mechanism state chained to a sensor-fusion result"** (`known-failure-modes.md`). If your auto's steps wait on a HIVE-tag pose being valid, a tag that's out of view or flipped stalls everything after it. Only gate what the estimate actually describes.
- **Where the drift probably comes from.** With Pedro Pathing, drift usually comes from the localizer and its constants, not from missing vision corrections. Pedro's library ships default physical constants taken from another robot, such as `mass = 10.65` and pod offsets. These apply silently if never overridden (standing-principles §13). The linter can check for this, but I couldn't run that check without your `Constants.java`.

## 3. Judgment calls (my read, not a verdict)

- **`HiveRelocalizer.java:12`** takes the first detection with id 30-45 and a non-null `robotPose`. It doesn't check alliance, which CELL, pose uncertainty, or whether the HIVE has tipped. Even if HIVE tags could give a field pose, whichever cluster happens to be visible wins.
- The class name and doc comment ("Reset odometry from the robot's field pose computed off the HIVE tags") put a DECODE-era idea into BIOBUZZ code. The season file says not to port goal-AprilTag assumptions from DECODE.
- Using a tag pose relative to a cluster, for targeting, is the use the season file describes as supported. It's not a field reset, and your config says `aim_vision: none`.

## Questions I would ask (no one was available to answer)

1. **Which SDK version is on the Robot Controller?**
   - 12.0 or later: this file shouldn't compile, so the auto you're running isn't this code. I'd ask for the version that actually runs.
   - Earlier than 12.0: the game tag library isn't BIOBUZZ's. I expect `robotPose` would be null for ids 30-45, which would make the relocalizer do nothing and leave pure odometry drift. I haven't checked that; I'd confirm it against that SDK's source before saying so.
2. **What does the auto use for localization?** Pinpoint, three-wheel odometry, or drive encoders, and please share `Constants.java` or the localizer file. Then I'd run the default-tuning-constant check and look at pod offsets and ticks-per-inch as the likely real cause.
3. **Where does the per-loop reset happen?** Please share the auto OpMode so I can review the actual reset path, gating and telemetry, not just the helper.
4. **Is `TurretAim` stale code, or does the robot now have a turret?** If stale, flag it for removal. If there's a turret, hand back to ftc-team-config to fix the config. I won't edit the config here.
5. **Is `TelemetryHelper` used in your competition build?** If yes, it has to come out or be put behind a switch before events (R704.D). If practice only, keep it but make sure it's off at events.

Once I have answers 1-3, my recommendation would be: drop HIVE-tag field resets, tune the Pedro localizer so the drift is fixed where it starts, and add outside corrections only as gated, soft updates from a source that doesn't move. I haven't named a specific BIOBUZZ relocalization source, because I don't have one from the corpus or the manual. A new approach like that should go through corpus construction, not be invented in this review.

No files were created or modified.