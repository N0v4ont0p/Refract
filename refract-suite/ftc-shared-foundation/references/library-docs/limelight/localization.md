> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-coordinate-systems · Fetched: 2026-07-12
> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-robot-localization · Fetched: 2026-07-12
> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-robot-localization-megatag2 · Fetched: 2026-07-12
> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-map-specification · Fetched: 2026-07-12

> Note: These four pages are shared between Limelight's FRC and FTC documentation. The core concepts (MegaTag, MegaTag2, coordinate systems, `.fmap` format) and the FTC-relevant Java calls (`getBotpose()`, `getBotpose_MT2()`, `uploadFieldmap()` — see [java-api.md](./java-api.md)) apply to FTC. The `LimelightHelpers` / WPILib `PoseEstimator` code samples below are FRC-specific (WPILib is not used in FTC) and are included only for conceptual reference on the vision-measurement-rejection pattern; do not port them directly into FTC OpModes.

# 3D Coordinate Systems In Detail

## Limelight Camera Space

3D Cartesian Coordinate System with (0,0,0) at the camera lens.

- X+ → Pointing to the right (if you were to embody the camera)
- Y+ → Pointing downward
- Z+ → Pointing out of the camera

## Target Space

3D Cartesian Coordinate System with (0,0,0) at the center of the target.

- X+ → Pointing to the right of the target (if you are looking at the target)
- Y+ → Pointing downward
- Z+ → Pointing out of the target (orthogonal to target's plane)

## Robot Space

3D Cartesian Coordinate System with (0,0,0) located at the center of the robot's frame projected down to the floor.

- X+ → Pointing forward (Forward Vector)
- Y+ → Pointing toward the robot's right (Right Vector)
- Z+ → Pointing upward (Up Vector)

## Field Space (FTC)

3D Cartesian Coordinate System with (0,0,0) located at the center of the field.

![FTC field space diagram](https://ftc-docs.firstinspires.org/en/latest/_images/image3.jpg)

## Field Space (FTC Diamond)

3D Cartesian Coordinate System with (0,0,0) located at the center of the field.

![FTC diamond field space diagram](https://ftc-docs.firstinspires.org/en/latest/_images/image2.jpg)

## Field Space (FRC) (Used by map generator)

3D Cartesian Coordinate System with (0,0,0) located at the center of the field.

- X+ → Points along the long side of the field
- Y+ → Points up the short side of the field
- Z+ → Points towards the sky

Right-handed. Positive theta results in counterclockwise rotation from positive outside perspective.

## Field Space (FRC WPIBlue) (Preferred Field Space for all FRC Teams)

Just like the standard FRC coordinate system, but with (0,0,0) at the blue-alliance origin.

## Field Space (FRC WPIRed) (Do not use this)

Just like the standard FRC coordinate system, but with (0,0,0) at the red-alliance origin and rotated 180 degrees.

---

# Robot Localization with MegaTag

If your Limelight's robot-space pose has been configured in the web UI, and a field map has been uploaded via the web UI, then the robot's location in field space will be available via `getBotpose()` (FTC Java API) and the "botpose" NetworkTables array (x, y, z in meters; roll, pitch, yaw in degrees).

Limelight's robot localization algorithm is called MegaTag. If more than one tag is in view, it is resilient to individual tag ambiguities and noise in the image. If all keypoints are coplanar, there is still some risk of ambiguity flipping.

This is not restricted to planar tags — it scales to any number of tags in full 3D and in any orientation. Floor tags and ceiling tags work perfectly.

As the 3D combined MegaTag pose increases in tag count, its stability increases.

![MegaTag botpose example](https://downloads.limelightvision.io/documents/MEGATAG.png)

## Using WPILib's Pose Estimator (FRC only)

In 2024, most of the WPILib ecosystem transitioned to a single-origin coordinate system. For 2024 and beyond, the origin of the FRC coordinate system should always be the "blue" origin; FRC teams should always use `botpose_wpiblue` for pose-related functionality.

```java
LimelightHelpers.PoseEstimate mt1 = LimelightHelpers.getBotPoseEstimate_wpiBlue("limelight");

if (mt1.tagCount == 1 && mt1.rawFiducials.length == 1) {
    if (mt1.rawFiducials[0].ambiguity > .7) {
        doRejectUpdate = true;
    }
    if (mt1.rawFiducials[0].distToCamera > 3) {
        doRejectUpdate = true;
    }
}
if (mt1.tagCount == 0) {
    doRejectUpdate = true;
}

if (!doRejectUpdate) {
    m_poseEstimator.setVisionMeasurementStdDevs(VecBuilder.fill(.5, .5, 9999999));
    m_poseEstimator.addVisionMeasurement(
        mt1.pose,
        mt1.timestampSeconds);
}
```

## Configuring your Limelight's Robot-Space Pose

LL Forward, LL Right, and LL Up represent distances along the robot's forward, right, and up vectors if you were to embody the robot (in meters). LL Roll, Pitch, and Yaw represent the rotation of your Limelight in degrees. You can modify these values and watch the 3D model of the Limelight change in the 3D viewer. Limelight uses this configuration internally to go from the target pose in camera space → robot pose in field space.

(This same configuration also applies to MegaTag2, below.)

---

# Robot Localization with MegaTag2

Introduced in 2024, MegaTag2 is a precise and ambiguity-free AprilTag-based localizer for mobile robots. It was built with the following goals:

- Eliminate the pose ambiguity problem and increase robustness against image/corner noise.
- Provide excellent pose estimates given a single tag, no matter the perspective.
- Increase robustness against physical AprilTag placement inaccuracies.
- Reduce the amount of filtering necessary for good pose estimation results.

MegaTag2 provides excellent results at any distance given a single tag. This means it is perfectly viable to focus only on tags that are both relevant and within tolerance, and filter out all other tags. If a tag is not in the correct location, filter it out with the dynamic filter feature introduced alongside MegaTag2:

```java
int[] validIDs = {3,4};
LimelightHelpers.SetFiducialIDFiltersOverride("limelight", validIDs);
```

Unlike MegaTag (MT1), MegaTag2 (MT2) assumes that you know your robot's heading (yaw). Optionally, MegaTag2 accepts a complete robot orientation and angular velocities. In the FTC Java API this is `limelight.updateRobotOrientation(robotYaw)` followed by `result.getBotpose_MT2()` — see [java-api.md](./java-api.md).

Requirements:

- Your Limelight's robot-space pose has been configured in the web UI or via the API
- A field map (`.fmap`) has been uploaded
- Robot orientation/yaw is submitted every frame (FTC: `limelight.updateRobotOrientation(yawDegrees)`; FRC: `LimelightHelpers.SetRobotOrientation(...)`)

### NetworkTables / JSON Keys (FRC)

- `botpose_orb_wpiblue`
- `botpose_orb_wpired`
- `botpose_orb`
- Per-fiducial-target: `t6r_fs_orb` — robot pose in field space using MegaTag2 based on this tag alone (no multi-tag)

## Using WPILib's Pose Estimator (FRC only)

```java
LimelightHelpers.SetRobotOrientation("limelight", m_poseEstimator.getEstimatedPosition().getRotation().getDegrees(), 0, 0, 0, 0, 0);
LimelightHelpers.PoseEstimate mt2 = LimelightHelpers.getBotPoseEstimate_wpiBlue_MegaTag2("limelight");

// if our angular velocity is greater than 360 degrees per second, ignore vision updates
if (Math.abs(m_gyro.getRate()) > 360) {
    doRejectUpdate = true;
}
if (mt2.tagCount == 0) {
    doRejectUpdate = true;
}
if (!doRejectUpdate) {
    m_poseEstimator.setVisionMeasurementStdDevs(VecBuilder.fill(.7, .7, 9999999));
    m_poseEstimator.addVisionMeasurement(
        mt2.pose,
        mt2.timestampSeconds);
}
```

## Using Limelight 4's Built-In IMU with `imumode_set` / `SetIMUMode()`

Limelight 4 has a built-in IMU. You can use this with MT2 to get even more accurate pose estimates while turning. You must seed the initial orientation of the IMU before this will work ("seeding"). Once your Limelight knows your robot's initial orientation, it will be able to update your robot's orientation on its own to perform MT2 calculations. To use the LL4 IMU, your LL must currently be mounted in "landscape" mode.

The flow looks like this:

1. Call `SetRobotOrientation()` with your "external" IMU (such as a Pigeon, NavX, or the Control/Expansion Hub's built-in IMU on FTC). You can continue to call this method as often as you would like.
2. Call `SetIMUMode()` to configure how your Limelight utilizes IMU data from internal and external IMUs.
3. In general, use mode 1 while your robot is waiting for the autonomous period to begin. Switch to mode 3 or 4 while enabled, or while enabled and turning.

### Zeroing / Seeding

- To reset the internal IMU's fused robot yaw to the yaw submitted via `SetRobotOrientation()`, set your Limelight's IMU mode to 1 with `LimelightHelpers.SetIMUMode()`.
- While seeding, MegaTag2 will continue to use the yaw value submitted via `SetRobotOrientation()`.

### Using the Internal IMU with MegaTag2

To allow LL4 to use its internal IMU for MT2 localization, set your Limelight's IMU mode to 2 with `LimelightHelpers.SetIMUMode()`.

### IMU Modes

| Mode | Name | MT2 Yaw Source | Internal IMU Behavior |
|----|----|----|----|
| 0 | EXTERNAL_ONLY | External (NT/HTTP) | No internal IMU processing. MT2 uses interpolated yaw from robot's gyro sent via `SetRobotOrientation()`. |
| 1 | EXTERNAL_SEED | External (NT/HTTP) | Internal IMU offset is calibrated to match external yaw each frame (seeding). MT2 still uses external yaw for botpose. |
| 2 | INTERNAL_ONLY | Internal IMU | Uses internal IMU's fused yaw only. No external input required. |
| 3 | INTERNAL_MT1_ASSIST | Internal IMU + MT1 | Complementary filter fuses internal IMU with MT1 vision yaw. When MT1 gets a valid pose, it slowly corrects internal IMU drift. |
| 4 | INTERNAL_EXTERNAL_ASSIST | Internal IMU + External IMU | Complementary filter fuses internal IMU with external yaw from `SetRobotOrientation()`. Recommended mode — the internal IMU's 1kHz update rate is used for frame-by-frame motion while the robot's IMU corrects for any drift over time. |

The assist modes are designed to very gently "tug" the internal IMU toward the chosen reference without hurting responsiveness during rapid movements.

### Complementary Filter Alpha

For modes 3 and 4, the `imuassistalpha_set` parameter (default 0.001) controls the correction speed:

- **Lower values** (e.g., 0.001): Smoother, slower drift correction. The internal IMU is trusted more.
- **Higher values** (e.g., 0.01): Faster tracking of the reference source (MT1 or external IMU).

```java
// Set the complementary filter alpha (optional, default is 0.001)
LimelightHelpers.SetIMUAssistAlpha("limelight", 0.001);
```

### Recommended Usage

1. **Pre-match / Disabled**: Use mode 1 to continuously seed the internal IMU with your external gyro.
2. **Enabled**: Use mode 3 or 4 to use the internal IMU with gentle corrections from your external gyro.

```java
// In disabledPeriodic or before match starts
LimelightHelpers.SetIMUMode("limelight", 1); // Seed internal IMU

// When enabled
LimelightHelpers.SetIMUMode("limelight", 3); // Use internal IMU + MT1
// or
LimelightHelpers.SetIMUMode("limelight", 4); // Use internal IMU + external IMU
```

---

# AprilTag Map Specification

Limelight's field-space localization feature uses `.fmap` files to compute a robot pose. Fmap files support maps comprised of different target sizes and different families. You can use fmaps to define "environments" such as competition fields, or "objects" that have several attached AprilTags. To use an fmap, upload it to your Limelight using the web interface or the REST upload API (in FTC Java, see `limelight.uploadFieldmap()` in [java-api.md](./java-api.md)).

The `.fmap` file is a JSON file containing a single "fiducial" array. Each entry in the fiducial array has the following structure:

| Field | Meaning |
|----|----|
| family | AprilTag/Fiducial family |
| id | Tag ID |
| size | Tag size in mm |
| transform | 4x4 matrix transform of the target. Row-major, SI units. |
| unique | Specifies whether the target is unique in this map or featured multiple times |

In addition, the top-level object has a "type" string specifying the map type:

| Field | Meaning |
|----|----|
| type | Field type, e.g. `frc`, `ftc`, `ftcd` (FTC diamond) |

Example AprilTag map (FRC 2024 Crescendo field, credit: Kevin Hjelstrom) — shown for the JSON structure; FTC maps use `"type": "ftc"` or `"type": "ftcd"` with FTC tag families/sizes/positions instead:

```json
{
    "type": "frc",
    "fiducials": [
        {
            "family": "apriltag3_36h11_classic",
            "id": 1,
            "size": 165.1,
            "transform": [
                -0.5, -0.866025, 0, 6.808597,
                0.866025, -0.5, 0, -3.859403,
                0, 0, 1, 1.355852,
                0, 0, 0, 1
            ],
            "unique": 1
        }
    ]
}
```

(See the source page for the full 16-tag Crescendo example; truncated here since it is FRC-field-specific and not FTC content.)
