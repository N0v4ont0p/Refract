package org.firstinspires.ftc.teamcode.mechanisms.turret;

import com.arcrobotics.ftclib.command.SubsystemBase;
import com.arcrobotics.ftclib.hardware.SimpleServo;

import com.qualcomm.robotcore.hardware.HardwareMap;

import org.firstinspires.ftc.teamcode.RobotConstants;

/**
 * Single-axis {@link Turret} on a positional servo, via FTCLib's
 * {@link SimpleServo}. For a motor-driven (continuous, multi-turn) turret,
 * write a sibling class against the same {@link Turret} interface -- an
 * OpMode calling setAngle()/getCurrentAngle() doesn't need to know which.
 */
public class SingleAxisTurret extends SubsystemBase implements Turret {

    private SimpleServo servo;
    private double targetAngle = 0.0;

    @Override
    public void init(HardwareMap hardwareMap) {
        servo = new SimpleServo(
                hardwareMap,
                "turret",
                RobotConstants.TURRET_MIN_ANGLE_DEG,
                RobotConstants.TURRET_MAX_ANGLE_DEG
        );
    }

    @Override
    public void setAngle(double degrees) {
        targetAngle = degrees;
        servo.turnToAngle(degrees);
    }

    @Override
    public double getCurrentAngle() {
        return servo.getAngle();
    }

    @Override
    public boolean atTargetAngle() {
        return Math.abs(getCurrentAngle() - targetAngle) <= RobotConstants.TURRET_ANGLE_TOLERANCE_DEG;
    }

    @Override
    public void stop() {
        // Positional servos hold their last commanded angle on their own;
        // nothing to actively stop. A motor-driven turret implementation
        // would zero power here instead.
    }
}
