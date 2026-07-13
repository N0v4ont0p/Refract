package org.firstinspires.ftc.teamcode.drivetrain;

import com.qualcomm.robotcore.hardware.HardwareMap;

/**
 * Every drivetrain the team ever builds -- mecanum this season, maybe swerve
 * later -- implements this instead of an OpMode reaching into hardwareMap for
 * "front_left"/"front_right"/etc directly.
 *
 * Why this exists: known-failure-modes.md's highest-leverage structural
 * failure is the God-OpMode / silo pattern (a single 500+ line TeleOp mixing
 * drivetrain, shooter, turret, and intake logic together). An interface this
 * thin gives an OpMode nothing to reach past -- it can call drive()/stop(),
 * full stop. There's no seam for "just quickly read the left encoder here
 * too" to sneak into an OpMode instead of into the drivetrain implementation
 * that owns that hardware.
 *
 * Swapping drivetrains (mecanum -> swerve, or a new robot's wheel layout) is a
 * new class implementing this interface, not a rewrite of every OpMode that
 * drives.
 */
public interface Drivetrain {

    /** Acquire hardware (motors, IMU, encoders) from the hardware map. */
    void init(HardwareMap hardwareMap);

    /**
     * Robot-centric drive input, each axis in [-1.0, 1.0].
     *
     * @param strafe  positive = right
     * @param forward positive = forward
     * @param turn    positive = clockwise
     */
    void drive(double strafe, double forward, double turn);

    /** Zero all drive outputs. Always safe to call, including before init(). */
    void stop();
}
