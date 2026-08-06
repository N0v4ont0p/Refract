> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-robot-localization · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Robot Localization with MegaTag | Limelight Documentation

 Skip to main content

 On this page

# Robot Localization with MegaTag

If your Limelight's robot-space pose has been configured in the web ui, and a field map has been uploaded via the web ui, then the robot's location in field space
will be available via the getBotpose() and the "botpose" networktables array (x,y,z in meters, roll, pitch, yaw in degrees).

Our robot localization algorithm is called MegaTag. If more than one tag is in view, it is resilient to individual tag ambiguities and noise in the image.
If all keypoints are coplanar, there is still some risk of ambiguity flipping.

- Green Cylinder: Individual per-tag bot pose

- Blue Cylinder: Old BotPose

- White Cylinder: MegaTag Botpose

Note the obvious pose ambiguity here:

Notice how the new botpose (white cylinder) is extremely stable compared to the old botpose (blue cylinder). You can watch the tx and ty values as well.

This is not restricted to planar tags. It scales to any number of tags in full 3D and in any orientation. Floor tags and ceiling tags work perfectly.

Here’s a diagram demonstrating one aspect of how this works with a simple planar case.
The results are actually better than what is depicted, as the MegaTag depicted has a significant error applied to three points instead of one point.
As the 3D combined MegaTag increases in size and in keypoint count, its stability increases.

## Using WPILib's Pose Estimator​

 info
In 2024, most of the WPILib Ecosystem transitioned to a single-origin coordinate system.
In 2023, your coordinate system origin changed based on your alliance color.
For 2024 and beyond, the origin of your coordinate system should always be the "blue" origin. FRC teams should always use botpose_wpiblue for pose-related functionality

 LimelightHelpers.PoseEstimate mt1 = LimelightHelpers.getBotPoseEstimate_wpiBlue("limelight");
 
 if(mt1.tagCount == 1 && mt1.rawFiducials.length == 1)
 {
 if(mt1.rawFiducials[0].ambiguity > .7)
 {
 doRejectUpdate = true;
 }
 if(mt1.rawFiducials[0].distToCamera > 3)
 {
 doRejectUpdate = true;
 }
 }
 if(mt1.tagCount == 0)
 {
 doRejectUpdate = true;
 }

 if(!doRejectUpdate)
 {
 m_poseEstimator.setVisionMeasurementStdDevs(VecBuilder.fill(.5,.5,9999999));
 m_poseEstimator.addVisionMeasurement(
 mt1.pose,
 mt1.timestampSeconds);
 }

## Configuring your Limelight's Robot-Space Pose​

LL Forward, LL Right, and LL Up represent distances along the Robot's forward, right, and up vectors if you were to embody the robot. (in meters).
LL Roll, Pitch, and Yaw represent the rotation of your Limelight in degrees. You can modify these values and watch the 3D model of the Limelight change in the 3D viewer.
Limelight uses this configuration internally to go from the target pose in camera space -> robot pose in field space.

- Using WPILib's Pose Estimator
- Configuring your Limelight's Robot-Space Pose