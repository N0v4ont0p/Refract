> Source: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-swerve-aiming-and-ranging · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Aiming and Ranging With Swerve | Limelight Documentation

 Skip to main content

# Aiming and Ranging With Swerve

See the full example project here

 // simple proportional turning control with Limelight.
 // "proportional control" is a control algorithm in which the output is proportional to the error.
 // in this case, we are going to return an angular velocity that is proportional to the 
 // "tx" value from the Limelight.
 double limelight_aim_proportional()
 { 
 // kP (constant of proportionality)
 // this is a hand-tuned number that determines the aggressiveness of our proportional control loop
 // if it is too high, the robot will oscillate around.
 // if it is too low, the robot will never reach its target
 // if the robot never turns in the correct direction, kP should be inverted.
 double kP = .035;

 // tx ranges from (-hfov/2) to (hfov/2) in degrees. If your target is on the rightmost edge of 
 // your limelight 3 feed, tx should return roughly 31 degrees.
 double targetingAngularVelocity = LimelightHelpers.getTX("limelight") * kP;

 // convert to radians per second for our drive method
 targetingAngularVelocity *= Drivetrain.kMaxAngularSpeed;

 //invert since tx is positive when the target is to the right of the crosshair
 targetingAngularVelocity *= -1.0;

 return targetingAngularVelocity;
 }

 // simple proportional ranging control with Limelight's "ty" value
 // this works best if your Limelight's mount height and target mount height are different.
 // if your limelight and target are mounted at the same or similar heights, use "ta" (area) for target ranging rather than "ty"
 double limelight_range_proportional()
 { 
 double kP = .1;
 double targetingForwardSpeed = LimelightHelpers.getTY("limelight") * kP;
 targetingForwardSpeed *= Drivetrain.kMaxSpeed;
 targetingForwardSpeed *= -1.0;
 return targetingForwardSpeed;
 }

 private void drive(boolean fieldRelative) {
 // Get the x speed. We are inverting this because Xbox controllers return
 // negative values when we push forward.
 var xSpeed =
 -m_xspeedLimiter.calculate(MathUtil.applyDeadband(m_controller.getLeftY(), 0.02))
 * Drivetrain.kMaxSpeed;

 // Get the y speed or sideways/strafe speed. We are inverting this because
 // we want a positive value when we pull to the left. Xbox controllers
 // return positive values when you pull to the right by default.
 var ySpeed =
 -m_yspeedLimiter.calculate(MathUtil.applyDeadband(m_controller.getLeftX(), 0.02))
 * Drivetrain.kMaxSpeed;

 // Get the rate of angular rotation. We are inverting this because we want a
 // positive value when we pull to the left (remember, CCW is positive in
 // mathematics). Xbox controllers return positive values when you pull to
 // the right by default.
 var rot =
 -m_rotLimiter.calculate(MathUtil.applyDeadband(m_controller.getRightX(), 0.02))
 * Drivetrain.kMaxAngularSpeed;

 // while the A-button is pressed, overwrite some of the driving values with the output of our limelight methods
 if(m_controller.getAButton())
 {
 final var rot_limelight = limelight_aim_proportional();
 rot = rot_limelight;

 final var forward_limelight = limelight_range_proportional();
 xSpeed = forward_limelight;

 //while using Limelight, turn off field-relative driving.
 fieldRelative = false;
 }

 m_swerve.drive(xSpeed, ySpeed, rot, fieldRelative, getPeriod());
 }