> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-robot-localization-megatag2 · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Robot Localization with MegaTag2 | Limelight Documentation

 Skip to main content

 On this page

# Robot Localization with MegaTag2

Introduced in 2024, Megatag2 is a precise and ambiguity-free AprilTag-based localizer for mobile robots. It was built with the following goals:

- Eliminate the pose ambiguity problem and increase robustness against image/corner noise.

- Provide excellent pose estimates given a single tag, no matter the perspective.

- Increase robustness against physical AprilTag placement inaccuracies

- Reduce the amount of filtering necessary for good pose estimation results

Megatag2 provides excellent results at any distance given a single tag.
This means it is perfectly viable to focus only on tags that are both relevant and within tolerance, and filter out all other tags. If a tag is not in the correct location, filter it out with
the dynamic filter feature introduced alongside MegaTag2.

int[] validIDs = {3,4};
LimelightHelpers.SetFiducialIDFiltersOverride("limelight", validIDs);

Unlike MT1, MT2 assumes that you know your robot's heading (yaw). Optionally, Megatag2 accepts a complete robot orientation and angular velocities.

Requirements:

- Your Limelight's robot-space pose has been configured in the webUI or via the API

- A field map (.fmap) has been uploaded

- LimelightHelpers.SetRobotOrientation(robotYawInDegrees,0,0,0,0,0) is called every frame in robot-side code

- SetRobotOrientation assumes a centered (see the map generator) or blue-corner origin. CCW-positive, 0 degrees -> facing red alliance wall in FRC.

NetworkTables Keys:

- botpose_orb_wpiblue

- botpose_orb_wpired

- botpose_orb

JSON Keys:

- botpose_orb_wpiblue

- botpose_orb_wpired

- botpose_orb

- (Per fiducial target) t6r_fs_orb - robot pose in field space using megatag2 based on this tag alone (no multitag)

Notice the difference between MegaTag2 (red robot) and Megatag (blue robot)
in this highly ambiguous single-tag case

- Gold Cylinder / Red Robot: Unfiltered Megatag2 botpose

- Yellow Cylinders: Unfiltered single-tag Megatag2 botposes

- White Cylinder/Blue Robot: MegaTag1 Botpose

- Green Cylinder: Individual per-tag bot pose (MT1)

- Blue Cylinder: Average of individual per-tag bot poses (MT1)

 info
In 2024, most of the WPILib Ecosystem transitioned to a single-origin coordinate system.
In 2023, your coordinate system origin changed based on your alliance color.
For 2024 and beyond, the origin of your coordinate system should always be the "blue" origin. FRC teams should always use botpose_orb_wpiblue for pose-related functionality

## Using WPILib's Pose Estimator​

 LimelightHelpers.SetRobotOrientation("limelight", m_poseEstimator.getEstimatedPosition().getRotation().getDegrees(), 0, 0, 0, 0, 0);
 LimelightHelpers.PoseEstimate mt2 = LimelightHelpers.getBotPoseEstimate_wpiBlue_MegaTag2("limelight");
 
 // if our angular velocity is greater than 360 degrees per second, ignore vision updates
 if(Math.abs(m_gyro.getRate()) > 360)
 {
 doRejectUpdate = true;
 }
 if(mt2.tagCount == 0)
 {
 doRejectUpdate = true;
 }
 if(!doRejectUpdate)
 {
 m_poseEstimator.setVisionMeasurementStdDevs(VecBuilder.fill(.7,.7,9999999));
 m_poseEstimator.addVisionMeasurement(
 mt2.pose,
 mt2.timestampSeconds);
 }

## Configuring your Limelight's Robot-Space Pose​

LL Forward, LL Right, and LL Up represent distances along the Robot's forward, right, and up vectors if you were to embody the robot. (in meters).
LL Roll, Pitch, and Yaw represent the rotation of your Limelight in degrees. You can modify these values and watch the 3D model of the Limelight change in the 3D viewer.
Limelight uses this configuration internally to go from the target pose in camera space -> robot pose in field space.

## Using Limelight 4's Built-In IMU with "imumode_set" / SetIMUMode()​

Limelight 4 has a built-in IMU. You can use this with MT2 to get even more accurate pose estimates while turning.
You must seed the initial orientation of the IMU before this will work. This is called "seeding". Once your limelight knows your robot's initial orientation, it wil be able to update your robot's orientation on its own to perform MT2 calculations.

To use the LL4 IMU, currently your LL must be mounted in "landscape" mode.

The flow looks like this:

- Call SetRobotOrientation() with your "external" IMU such as a Pigeon or a NavX. You can continue to call this method as often as you would like.

- Call SetIMUMode() to configure how your Limelight utilizes IMU data from internal and external IMUs.

- In general, use mode 1 while your robot is waiting for the autonomous period to begin. Switch to mode 3 or 4 while enabled or while enabled and turning.

### Zeroing / Seeding​

- To reset the internal IMU's fused robot yaw to the yaw submitted via SetRobotOrientation(), set your Limelight's IMU mode to 1 with LimelightHelpers.SetIMUMode().

- While seeding, MegaTag2 will continue to use the yaw value submitted via SetRobotOrientation().

### Using the Internal IMU with MegaTag2​

To allow LL4 to use its internal IMU for MT2 localization, set set your Limelight's IMU mode to 2 with LimelightHelpers.SetIMUMode().

### IMU Modes​

ModeNameMT2 Yaw SourceInternal IMU Behavior
0EXTERNAL_ONLYExternal (NT/HTTP)No internal IMU processing. MT2 uses interpolated yaw from robot's gyro sent via SetRobotOrientation().
1EXTERNAL_SEEDExternal (NT/HTTP)Internal IMU offset is calibrated to match external yaw each frame (seeding). MT2 still uses external yaw for botpose.
2INTERNAL_ONLYInternal IMUUses internal IMU's fused yaw only. No external input required.
3INTERNAL_MT1_ASSISTInternal IMU + MT1Complementary filter fuses internal IMU with MT1 vision yaw. When MT1 gets a valid pose, it slowly corrects internal IMU drift.
4INTERNAL_EXTERNAL_ASSISTInternal IMU + External IMUComplementary filter fuses internal IMU with external yaw from SetRobotOrientation(). This is the recommended mode, as the internal IMU's 1khz update rate is utilized for frame-by-frame motion while the robot's IMU corrects for any drift over time.

The assist modes are designed to very gently "tug" the internal IMU toward the chosen reference without hurting responsiveness during rapid movements.

### Complementary Filter Alpha​

For modes 3 and 4, the imuassistalpha_set parameter (default 0.001) controls the correction speed:

- Lower values (e.g., 0.001): Smoother, slower drift correction. The internal IMU is trusted more.

- Higher values (e.g., 0.01): Faster tracking of the reference source (MT1 or external IMU).

// Set the complementary filter alpha (optional, default is 0.001)
LimelightHelpers.SetIMUAssistAlpha("limelight", 0.001);

### Recommended Usage​

- Pre-match / Disabled: Use mode 1 to continuously seed the internal IMU with your external gyro

- Enabled: Use mode 3 or 4 if you want the internal IMU with gentle corrections from your external gyro

// In disabledPeriodic or before match starts
LimelightHelpers.SetIMUMode("limelight", 1); // Seed internal IMU

// When enabled
LimelightHelpers.SetIMUMode("limelight", 3); // Use internal IMU + MT1
or 
LimelightHelpers.SetIMUMode("limelight", 4); // Use internal IMU + external IMU

- Using WPILib's Pose Estimator
- Configuring your Limelight's Robot-Space Pose
- Using Limelight 4's Built-In IMU with "imumode_set" / SetIMUMode()- Zeroing / Seeding
- Using the Internal IMU with MegaTag2
- IMU Modes
- Complementary Filter Alpha
- Recommended Usage