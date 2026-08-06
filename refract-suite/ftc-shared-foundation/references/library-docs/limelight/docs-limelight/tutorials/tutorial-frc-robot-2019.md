> Source: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-frc-robot-2019 · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

2019 Deep Space Robot | Limelight Documentation

 Skip to main content

# 2019 Deep Space Robot

The 2019 FRC game Deep Space had vision targets above many of the goals.
Below you can find complete example programs in Java and Labview that implement a simple method for automatically
driving toward a goal in Deep Space.

These are very simple programs and only meant to show the concept of using limelight tracking data to control your robot.
In each program, you can drive your robot with a gamepad.
If you hold the ‘A’ button down, and the limelight sees a valid target
(depending on the settings in your pipeline) then the robot will automatically drive towards the target.
Be careful to tune the various constants in the code for your particular robot.
Some robots turn or drive more easily than others, so tuning the proportional control constants must be done on a case-by-case basis.
Make sure the robot drives correctly using the gamepad controller before enabling the limelight seeking behavior.

- Java
- LabView
package frc.robot;

import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
import edu.wpi.first.wpilibj.VictorSP;
import edu.wpi.first.wpilibj.SpeedControllerGroup;
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.GenericHID.Hand;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;
import edu.wpi.first.networktables.*;

public class Robot extends TimedRobot {

 private static final String kDefaultAuto = "Default";
 private static final String kCustomAuto = "My Auto";
 private String m_autoSelected;
 private final SendableChooser<String> m_chooser = new SendableChooser<>();

 private VictorSP m_Left0 = new VictorSP(0);
 private VictorSP m_Left1 = new VictorSP(1);
 private VictorSP m_Right0 = new VictorSP(2);
 private VictorSP m_Right1 = new VictorSP(3);
 private SpeedControllerGroup m_LeftMotors = new SpeedControllerGroup(m_Left0,m_Left1);
 private SpeedControllerGroup m_RightMotors = new SpeedControllerGroup(m_Right0,m_Right1);
 private DifferentialDrive m_Drive = new DifferentialDrive(m_LeftMotors,m_RightMotors);

 private XboxController m_Controller = new XboxController(0);

 private boolean m_LimelightHasValidTarget = false;
 private double m_LimelightDriveCommand = 0.0;
 private double m_LimelightSteerCommand = 0.0;

 @Override
 public void robotInit() {
 m_chooser.setDefaultOption("Default Auto", kDefaultAuto);
 m_chooser.addOption("My Auto", kCustomAuto);
 SmartDashboard.putData("Auto choices", m_chooser);
 }

 @Override
 public void robotPeriodic() {
 }

 @Override
 public void autonomousInit() {
 m_autoSelected = m_chooser.getSelected();
 }

 @Override
 public void autonomousPeriodic() {
 }

 @Override
 public void teleopPeriodic() {

 Update_Limelight_Tracking();

 double steer = m_Controller.getX(Hand.kRight);
 double drive = -m_Controller.getY(Hand.kLeft);
 boolean auto = m_Controller.getAButton();

 steer *= 0.70;
 drive *= 0.70;

 if (auto)
 {
 if (m_LimelightHasValidTarget)
 {
 m_Drive.arcadeDrive(m_LimelightDriveCommand,m_LimelightSteerCommand);
 }
 else
 {
 m_Drive.arcadeDrive(0.0,0.0);
 }
 }
 else
 {
 m_Drive.arcadeDrive(drive,steer);
 }
 }

 @Override
 public void testPeriodic() {
 }

 /**
 * This function implements a simple method of generating driving and steering commands
 * based on the tracking data from a limelight camera.
 */
 public void Update_Limelight_Tracking()
 {
 // These numbers must be tuned for your Robot! Be careful!
 final double STEER_K = 0.03; // how hard to turn toward the target
 final double DRIVE_K = 0.26; // how hard to drive fwd toward the target
 final double DESIRED_TARGET_AREA = 13.0; // Area of the target when the robot reaches the wall
 final double MAX_DRIVE = 0.7; // Simple speed limit so we don't drive too fast

 double tv = NetworkTableInstance.getDefault().getTable("limelight").getEntry("tv").getDouble(0);
 double tx = NetworkTableInstance.getDefault().getTable("limelight").getEntry("tx").getDouble(0);
 double ty = NetworkTableInstance.getDefault().getTable("limelight").getEntry("ty").getDouble(0);
 double ta = NetworkTableInstance.getDefault().getTable("limelight").getEntry("ta").getDouble(0);

 if (tv < 1.0)
 {
 m_LimelightHasValidTarget = false;
 m_LimelightDriveCommand = 0.0;
 m_LimelightSteerCommand = 0.0;
 return;
 }

 m_LimelightHasValidTarget = true;

 // Start with proportional steering
 double steer_cmd = tx * STEER_K;
 m_LimelightSteerCommand = steer_cmd;

 // try to drive forward until the target area reaches our desired area
 double drive_cmd = (DESIRED_TARGET_AREA - ta) * DRIVE_K;

 // don't let the robot drive too fast into the goal
 if (drive_cmd > MAX_DRIVE)
 {
 drive_cmd = MAX_DRIVE;
 }
 m_LimelightDriveCommand = drive_cmd;
 }
}

Here is a block diagram for a LabView VI which reads tracking data from a Limelight and generates drive and steer commands. This image is a “LabView Snippet”.
Just save the image file to your computer and then drag it into a labview VI and the block diagram will be reproduced.

You can also download the entire labview source code from this link