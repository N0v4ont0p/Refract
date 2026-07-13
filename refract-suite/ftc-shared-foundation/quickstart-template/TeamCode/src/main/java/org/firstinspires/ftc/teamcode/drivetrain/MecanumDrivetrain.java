package org.firstinspires.ftc.teamcode.drivetrain;

import com.arcrobotics.ftclib.command.SubsystemBase;
import com.arcrobotics.ftclib.drivebase.MecanumDrive;
import com.arcrobotics.ftclib.hardware.motors.Motor;

import com.qualcomm.robotcore.hardware.HardwareMap;

/**
 * Standard four-wheel mecanum drivetrain, built on FTCLib's
 * {@link MecanumDrive} (com.arcrobotics.ftclib.drivebase). This is the example
 * concrete {@link Drivetrain} -- a team on swerve or tank/differential instead
 * writes a sibling class, not a fork of every OpMode.
 *
 * Extends {@link SubsystemBase} (not required by the {@link Drivetrain}
 * interface itself) so it can be registered with the FTCLib CommandScheduler
 * via {@code register(...)} in {@code TeamOpMode.onInit()} -- that's what lets
 * a default (or button-bound) drive Command run every loop without the
 * OpMode's run() method touching drivetrain code at all.
 *
 * Motor names below ("front_left", "front_right", "back_left", "back_right")
 * must match the Driver Station's Robot Configuration exactly -- update them
 * (or make them constructor parameters) to match your actual config.
 */
public class MecanumDrivetrain extends SubsystemBase implements Drivetrain {

    private Motor frontLeft, frontRight, backLeft, backRight;
    private MecanumDrive mecanumDrive;

    @Override
    public void init(HardwareMap hardwareMap) {
        frontLeft = new Motor(hardwareMap, "front_left");
        frontRight = new Motor(hardwareMap, "front_right");
        backLeft = new Motor(hardwareMap, "back_left");
        backRight = new Motor(hardwareMap, "back_right");

        frontLeft.setInverted(true);
        backLeft.setInverted(true);

        mecanumDrive = new MecanumDrive(frontLeft, frontRight, backLeft, backRight);
    }

    @Override
    public void drive(double strafe, double forward, double turn) {
        mecanumDrive.driveRobotCentric(strafe, forward, turn);
    }

    @Override
    public void stop() {
        if (mecanumDrive != null) {
            mecanumDrive.stop();
        }
    }
}
