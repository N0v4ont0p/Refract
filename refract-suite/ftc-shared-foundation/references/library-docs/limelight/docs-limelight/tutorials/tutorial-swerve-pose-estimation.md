> Source: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-swerve-pose-estimation · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Localization with MegaTag | Limelight Documentation

 Skip to main content

# Localization with MegaTag

- Ensure a field map is uploaded to your Limelight.

- Configure pipeline 0 as an Apriltag Pipeline and enable 3D functionality

- Configure the pose of your Limelight relative to the center of your robot in the Limelight UI

- See the code below. We only incorporate Limelight's estimates when more than one tag is visible. We set the stdev of the measured rotation to a large number
because we can trust our IMU to give us the correct robot heading.

- We always read the botpose_wpiblue measurement because common pathplanning tools have adopted a blue-corner-always field origin strategy.

- Use megatag 2 if possible.

See the full example project here

 public void updateOdometry() {
 m_poseEstimator.update(
 m_gyro.getRotation2d(),
 new SwerveModulePosition[] {
 m_frontLeft.getPosition(),
 m_frontRight.getPosition(),
 m_backLeft.getPosition(),
 m_backRight.getPosition()
 });

 boolean useMegaTag2 = true; //set to false to use MegaTag1
 boolean doRejectUpdate = false;
 if(useMegaTag2 == false)
 {
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
 }
 else if (useMegaTag2 == true)
 {
 LimelightHelpers.SetRobotOrientation("limelight", m_poseEstimator.getEstimatedPosition().getRotation().getDegrees(), 0, 0, 0, 0, 0);
 LimelightHelpers.PoseEstimate mt2 = LimelightHelpers.getBotPoseEstimate_wpiBlue_MegaTag2("limelight");
 if(Math.abs(m_gyro.getRate()) > 720) // if our angular velocity is greater than 720 degrees per second, ignore vision updates
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
 }
 }