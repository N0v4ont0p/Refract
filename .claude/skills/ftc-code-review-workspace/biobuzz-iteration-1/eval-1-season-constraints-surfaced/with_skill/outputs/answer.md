## BIOBUZZ robot code review (before your first scrimmage)

**What I reviewed:** the 4 files in `evals/fixtures/biobuzz-robot/TeamCode/` (LauncherSubsystem, TurretAim, HiveRelocalizer, TelemetryHelper), checked against your confirmed `team-config.yaml`. That config is season biobuzz-2026-27, mecanum drive, raw LinearOpMode, Pedro Pathing, roller intake, flywheel launcher, and **turret: none, aim_vision: none**.

**Bottom line:** 2 problems will stop you at the scrimmage and 1 is a real mismatch with your config.
1. `HiveRelocalizer` won't compile on SDK 12.0, and what it's trying to do can't work in BIOBUZZ.
2. `TelemetryHelper` sends data to FTC Dashboard, which rule R704 bans at events.
3. `TurretAim` is turret code, but your config says the robot has no turret.

---

### Tier 1: script findings (authoritative)
I ran `failure_mode_lint.py` and `config_lint.py`. The config check found 3 things (`clean: false`).

**F1. SDK 12 AprilTag change breaks `HiveRelocalizer.java` (compile error).**
- Line 12 reads `detection.id` straight off the base `AprilTagDetection`.
- In SDK v12.0 (Breaking Changes) the base type no longer has `.id`, `.metadata` or `.center`. Refract confirmed this by compiling the 11.1 samples against the 12.0.0 libraries. `.robotPose` still compiles.
- Source: season file `code_constraints: sdk-12-apriltag-cluster-api`, and the SDK VERSION SCOPE note in the mirrored ftc-sdk `apriltag-id-code.md`. This comes from the SDK README, not a game-manual rule.
- **Fix:** check `instanceof AprilTagSingleDetection` or `AprilTagClusterDetection` and cast before reading the tag ID.

**F1b. Even once it compiles, HIVE tags can't give you a field position (same file, lines 9–13).**
- The Javadoc says "Reset odometry from the robot's field pose computed off the HIVE tags."
- Season file (`no-apriltag-absolute-localization`, citing the SDK v12.0 README): BIOBUZZ tags sit on the tipping HIVE, so they "are not suitable for absolute Field Localization". Which tags face the floor changes every time the HIVE tips.
- The mirrored `apriltag-localization.md` note adds that BIOBUZZ clusters carry no field pose (origin 0,0,0). So `robotPose` can't place the robot on the field.
- Resetting odometry from this would, at best, do nothing and, at worst, make your position jump.
- **Fix:** delete it as a relocalizer. Aiming relative to a tag cluster is the supported use. For drift, rely on Pedro odometry tuning.
- Tag IDs 30–45 match the season file, so the ID range itself is correct.

**F2. FTC Dashboard streaming in `TelemetryHelper.java` breaks R704.**
- Lines 3–4 and 9: `new MultipleTelemetry(ds, FtcDashboard.getInstance().getTelemetry())`.
- I re-checked the rule before calling this. `check_freshness.py --season biobuzz-2026-27` returned CURRENT (Team Update 00 is the latest, live and stored). `rules.py verify R704` passed (`all_valid: true`).
- Legality result (§5 of the review skill):
  - **verdict:** illegal in any OpMode you run at an event.
  - **citation:** R704.D, "Additional logging/streaming services, such as those hosted by third party plugins and tools such as FTC Dashboard, FTControl Panels, and others are prohibited." Section 12.7 Control, Command & Signals System. R704 has no one-hop cross-references.
  - **reasoning:** `wrap()` sends every telemetry line to FTC Dashboard in addition to the Driver Station. R704.D only allows telemetry "using the FTC Driver Station Application."
- **Fix:** use the plain `telemetry` for competition builds.
- You can still use Dashboard in practice. Per the season file's `applies_to` note, it has to be removable or disabled for events. That note is Refract's reading of the rule, not rule text.
- Still open: the rule doesn't say whether having the Dashboard library installed but unused counts. I can't see whether any OpMode calls `wrap()`.

**F3. Turret code on a robot with no turret: `TurretAim.java`.**
- Config says `turret: none` (confirmed), but this class exists.
- It isn't referenced by your current config. I can't tell whether the code is left over or the config is out of date, and I'm not assuming either (see Q1).

**Script findings I'm withdrawing or limiting:**
- **Bus factor ("N0v4ont0p authored 16/16 commits"): withdrawn.**
  - The fixture has no git repo of its own, so `git -C <dir> shortlog --all` read the whole Refract suite repo's history.
  - I confirmed this: `git rev-parse --show-toplevel` returns the suite root. The finding describes Refract, not your team.
  - This is a bug in the linter: it doesn't check that the target folder is its own git repo.
- **The other lint checks passed only because there was nothing to check.** They found 0 OpModes, 0 PID files and 0 tuning-constant files. That tells us nothing about your OpModes.
- **Blind spot in `config_lint`:**
  - `aim_vision` is `none` in your config, and its `code_tokens` list in the season file is empty (`[]`).
  - Line 72 of `config_lint.py` drops it from `declared_absent` and line 74 keeps it out of `unchecked_mechanisms`. So it disappears from the output without a word, and `unchecked_mechanisms: []` looks clean.
  - The season file says `[]` should mean "not lintable by name, rather than silently skipped", so this is a second linter bug.
  - It matters here: `HiveRelocalizer` is camera code on a robot whose config says no aiming vision (see Q4).

### Tier 2: checks against your config and the corpus
**Launcher (`hive_launcher: flywheel`).** `LauncherSubsystem` is correctly declared in your config and matches it.
- The closest corpus finding is `shooter-empirical-vs-physics`: confidence **high**, but seen only in decode-2025-26.
- Its own cross-season note: "Evidence is DECODE-only (5 in Artifact, fixed goals); BIOBUZZ launches smaller, different balls (2.8 in POLLEN, 3.6 in NECTAR) into a moving, tipping HIVE - treat as a hypothesis to re-verify, not current-season evidence."
- So I'm not recommending a DECODE-style distance-to-power table. Any velocity numbers you use have to be measured on your robot.

**Can't check yet (I'd need more files):**
- **Pedro constants:** no `Constants.java` / `FollowerConstants` was included. Pedro silently uses its built-in defaults (for example `mass = 10.65`, measured on someone else's robot) when you don't set a value. I need your constants file to check that.
- **Starting and transition rules:** with no OpModes, I can't check R102 (flywheel or rollers spinning before START) or G403 (no powered movement during the 8 s transition).
- **SDK integrity:** there's no `libs/` folder in what was submitted, so I can't confirm nothing in the SDK was modified.

### Tier 3: judgment calls (heuristic, not verdicts)
The skill normally hands these to a Sonnet subagent, and step 4 hands the pre-competition pass to the `full-review` subagent. **I couldn't run either:** this session has no way to start subagents. So the notes below are my own inline observations, and **the full pre-competition review hasn't been done.**
- **`LauncherSubsystem.java:9`:** `setVelocity(double ticksPerSecond)` only sets a target. Nothing reads it back (`getVelocity`), there's no "at speed" check, and there's no telemetry. That makes intermittent launch problems hard to debug at a scrimmage. Adding an at-speed check and telemetry line is worth considering.
- **`TelemetryHelper.java:8`:** `wrap()` is a `public static` helper shared by every OpMode. Switching it off for competition builds in one place is easier than editing each OpMode.

---

### Questions I'd ask you (no one was available to answer)
1. **Is `TurretAim` left over, or did you add a turret?** If left over, delete it. If you added one, the config is out of date: I'd hand back to ftc-team-config to change `turret` (and check that aiming still goes with the launcher) instead of editing the config here.
2. **Does any OpMode call `TelemetryHelper.wrap()`?** Please share your OpModes. If any competition OpMode calls it, F2 blocks the scrimmage. Either way, I'd run the lint checks and the R102/G403 checks against those OpModes.
3. **Which SDK version are you building with?** If 12.0, F1 is a compile error today. If older, the code builds but the older SDK doesn't carry the BIOBUZZ tag library (the season file says only v12.0 does), so update to 12.0 and apply the F1 fix.
4. **Is there a camera on the robot, and is `aim_vision: none` correct?** If you have a camera for aiming at the HIVE, the config needs updating via ftc-team-config (`upward_apriltag`). If there's no camera, delete `HiveRelocalizer`.
5. **Can you share your Pedro `Constants.java` and the real team repo, with its own git history?** I'd check for Pedro's silent default constants and re-run the bus-factor check on your actual commits.

### Refract bugs found during this review
Not fixed; no repo files were changed.
- `/Users/georgehu/Desktop/FTC Training AI/.claude/skills/ftc-code-review/scripts/failure_mode_lint.py`: it reads the git history of whatever repo *contains* the target folder.
- `/Users/georgehu/Desktop/FTC Training AI/.claude/skills/ftc-code-review/scripts/config_lint.py` lines 72–74: a mechanism set to `none` with an empty token list is dropped from the output without being reported.