## BIOBUZZ code review: pre-scrimmage

I read all 5 attached files: `team-config.yaml` plus 4 classes in `TeamCode/`. I checked the rules and SDK points against the BIOBUZZ Competition Manual V1 and the FTC SDK v12.0 release notes (links at the bottom). There are no OpModes in what you sent, so I couldn't check TeleOp or Auto themselves. I didn't compile anything and didn't change any files.

**Short version:** two things will stop you at the scrimmage (a rules problem and a build error), and one class is based on an idea that won't work this season. Fix those three before you go.

---

### 1. BLOCKER (rules): FTC Dashboard is banned this season. File: `TelemetryHelper.java`
`wrap()` sends your telemetry to FTC Dashboard through `MultipleTelemetry`. Rule R704.D in the BIOBUZZ manual says robot data may only be streamed through the FTC Driver Station app. It says extra logging or streaming tools "such as FTC Dashboard, FTControl Panels, and others are prohibited." R704.C also says laptops must be off the Robot Controller Wi-Fi during matches.

**Fix:** delete `TelemetryHelper.java` and use plain `telemetry` wherever `TelemetryHelper.wrap(telemetry)` is called.
**Also remove the Dashboard library** (`com.acmerobotics.dashboard`) from your gradle dependencies. As far as I know, Dashboard starts its own web server when the Robot Controller app launches, even if no code calls it. So deleting the import alone may not be enough. Check this by rebuilding and confirming the Dashboard page no longer loads.

### 2. BLOCKER (won't compile on SDK 12): `HiveRelocalizer.java` line 12
SDK 12.0 (released Sept 7, 2026, the BIOBUZZ SDK) changed AprilTag detections. Each detection is now either an `AprilTagSingleDetection` or an `AprilTagClusterDetection`, and you have to cast to the right one. The updated `ConceptAprilTag` sample only reads `.id` after casting to `AprilTagSingleDetection`. So `detection.id` on the base `AprilTagDetection` should fail to compile. (This comes from the release notes and sample; I didn't compile it myself.) If this file is in the project, the whole build fails, including your working OpModes.

### 3. DESIGN BUG: the HIVE tags can't tell you where the robot is. File: `HiveRelocalizer.java`
The class takes the robot's field position from the HIVE AprilTags. That doesn't work in BIOBUZZ:
- Manual section 9.6: each HIVE sits on a pivot and tips over as game pieces are launched in. The AprilTag clusters are stuck to the bottom of the CELLs, so they move with it.
- The SDK 12.0 notes say directly: "since BIOBUZZ AprilTags move, they are not suitable for absolute Field Localization."

Even after fixing the compile error, `robotPose` would push your Pedro odometry to a wrong position whenever the HIVE has tipped. Other smaller problems:
- It returns only x and y, no heading.
- It gives no units.
- It uses `null` to mean "no tag seen".
- IDs 30–45 cover both alliances' CELLs.

**Fix:** delete the class and let Pedro odometry handle position. If you later want vision to aim at a CELL, use the cluster detection's `ftcPose`. That's the position relative to the camera, and the SDK puts each cluster's origin at the center of the CELL opening for this purpose. That also means changing your config, see question B.

### 4. CONFIG MISMATCH: turret code on a robot with no turret. File: `TurretAim.java`
Your confirmed config says `turret: none`, but this class exists. Nothing in the attached files uses it. Also, `Math.atan2(dy, dx)` alone isn't turret aiming: it ignores the robot's heading, doesn't handle angle wraparound, and doesn't know the turret's range limits. **Default:** delete it. See question A.

### 5. `LauncherSubsystem.java`: no bugs, three optional hardening steps
Ranked by value; all are optional:
- In the constructor, call `flywheel.setMode(DcMotor.RunMode.RUN_USING_ENCODER)`. Motor modes stay set on the hub between OpModes (for example, Auto leaves it in `STOP_AND_RESET_ENCODER`), so setting it explicitly is cheap insurance for velocity control.
- `setZeroPowerBehavior(FLOAT)` so the flywheel coasts down instead of braking hard.
- Add `public double getVelocity() { return flywheel.getVelocity(); }` so TeleOp and Auto can wait until the flywheel is up to speed before feeding.
- Check that the configured motor name `"launcher"` matches the name on the Robot Controller.

---

### Questions I'd ask (no one was available to answer)
**A. Did you add a turret, or is `TurretAim` leftover code?**
- If leftover: delete it (my default above).
- If you added a turret: update `team-config.yaml` first (turret type, motor or servo, angle limits). Then I'd rewrite `TurretAim` to use robot heading, wraparound, and limits.

**B. Do you want vision this season?** Your config says `aim_vision: none`, but `HiveRelocalizer` uses a camera.
- If no: delete it and remove the camera/VisionPortal setup.
- If yes, for aiming at CELLs: change the config to add aim vision. Then I'd write cluster-based aiming with `AprilTagClusterDetection.ftcPose`, never field-position resets.

**C. Can you send your OpModes (TeleOp, Auto) and `build.dependencies.gradle`?**
- I'd use them to find every call to `TelemetryHelper.wrap`, confirm Dashboard is really gone from the build, and check that `HiveRelocalizer` and `TurretAim` are not used anywhere before deleting them.
- I'd also check loop timing, bulk reads, and which SDK version you're on (these classes need 12.0).

**D. What version is the SDK and Robot Controller app on your robot right now?** If it's older than 12.0, the compile error won't appear yet, but it will as soon as you update. Update first, then apply the fixes above.

### Before the scrimmage
1. Remove Dashboard (the class and the gradle dependency), rebuild, and confirm the Dashboard page doesn't load.
2. Delete `HiveRelocalizer` and `TurretAim`, or fix them per A and B, then do a clean build on SDK 12.0.
3. Run TeleOp and check the flywheel reaches its target speed, watching the velocity on the Driver Station.
4. No laptops on the robot Wi-Fi during matches (R704.C).

Sources:
- [BIOBUZZ Competition Manual V1 (R704, sections 9.6 and 9.9)](https://ftc-resources.firstinspires.org/ftc/game/manual)
- [FtcRobotController README, v12.0 release notes](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/README.md)
- [ConceptAprilTag.java sample (SDK 12)](https://raw.githubusercontent.com/FIRST-Tech-Challenge/FtcRobotController/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptAprilTag.java)