> Source: https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_intro/apriltag-intro.html · Fetched: 2026-07-17
> Source: https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_localization/apriltag-localization.html · Fetched: 2026-07-17
> Completeness-audit addition: the entire `apriltag/vision_portal/*` section of the official FTC SDK
> docs was absent from this corpus before this pass — not stale, never fetched. This file covers
> the two highest-value pages (intro/concepts, localization); the rest of that section
> (camera-calibration, advanced-use, pose, reference-frame, multiportal, cpu-and-bandwidth,
> webcams, id-code, metadata, library reference) remains a known, lower-priority gap — logged, not
> silently dropped.

# AprilTag and VisionPortal — Overview and Localization

## What AprilTag is

A camera-based fiducial marker technology (comparable to a 2D barcode/QR code), bundled directly
into the FTC SDK since v8.2 — no separate download needed. Beyond simple ID recognition, AprilTag
detection gives **pose estimation**: position (X/Y/Z distance from camera lens to tag) and
orientation (pitch/roll/yaw), not just "which tag is this."

The `36h11` family is the FTC-standard tag family: 10×10 pixel grids with an outer white border and
inner black border, supporting up to 587 unique IDs. Tag size is measured across the outer edge of
the inner black border.

**Axis convention** (aligns with the robot coordinate system when the camera is upright and
forward-facing): Y points outward from the camera lens, X points rightward, Z points upward.

**Requirements**: camera calibration data matching the actual resolution used, tags mounted flat
(not curved), an Android RC phone camera or a compatible webcam, FTC SDK 8.2+.

Sample OpModes: `RobotAutoDriveToAprilTagOmni.java`, `RobotAutoDriveToAprilTagTank.java`. Both Java
and Blocks support full functionality.

## AprilTag localization — determining the robot's own field pose

Combines a tag's pose relative to the camera with stored global metadata about that tag's known
field location, to compute the camera's (and therefore the robot's) global position and
orientation.

**Setup**: configure a USB webcam in the robot configuration (default name `"Webcam 1"`); for an RC
phone camera instead, set `USE_WEBCAM` to `false`. Reference sample: `ConceptAprilTagLocalization`.

**Runtime**: aim the camera at a field AprilTag, INIT to preview via the Driver Station, Start to
begin localization — telemetry reports camera position/orientation.

**Camera-offset parameters** the OpMode accepts: position offsets in inches (left/right,
forward/back, height) and orientation angles (pitch/roll/yaw) describing where the camera sits
relative to the robot's own reference point.

**Data access, Java**: detection object properties, e.g. `detection.robotPose.getPosition()` and
the corresponding orientation accessors.

**Important caveat, stated directly in the official docs, not softened here**: this localization
method's reference frame differs from standard FTC field axes, IMU conventions, and odometry
systems — reconciling them needs manual adjustment. The docs explicitly recommend testing
thoroughly and combining this with other navigation systems (odometry, IMU) rather than relying on
it alone.
