package org.firstinspires.ftc.teamcode.mechanisms.shooter;

import com.arcrobotics.ftclib.command.SubsystemBase;
import com.arcrobotics.ftclib.hardware.motors.Motor;

import com.qualcomm.robotcore.hardware.HardwareMap;

import org.firstinspires.ftc.teamcode.RobotConstants;

/**
 * Single-flywheel {@link Shooter}, built on FTCLib's {@link Motor} in
 * {@link Motor.RunMode#VelocityControl}.
 *
 * PID/feedforward coefficients are FTCLib's defaults here. known-failure-modes.md
 * flags "PID instability" as its own root cause -- constants tuned for one
 * robot state don't survive mechanical changes -- so expect to call
 * {@code flywheel.setVeloCoefficients(...)} / {@code setFeedforwardCoefficients(...)}
 * once you have a real flywheel to tune against; don't ship untuned defaults
 * to competition.
 */
public class FlywheelShooter extends SubsystemBase implements Shooter {

    private Motor flywheel;
    private double targetRpm = 0.0;

    @Override
    public void init(HardwareMap hardwareMap) {
        flywheel = new Motor(hardwareMap, "shooter");
        flywheel.setRunMode(Motor.RunMode.VelocityControl);
    }

    @Override
    public void setTargetVelocity(double rpm) {
        targetRpm = rpm;
        flywheel.set(rpm / flywheel.getMaxRPM());
    }

    @Override
    public double getCurrentVelocity() {
        // encoder rate is in ticks/sec; convert to RPM via counts-per-revolution
        return flywheel.getRate() * 60.0 / flywheel.getCPR();
    }

    @Override
    public boolean atTargetVelocity() {
        return Math.abs(getCurrentVelocity() - targetRpm) <= RobotConstants.SHOOTER_VELOCITY_TOLERANCE_RPM;
    }

    @Override
    public void stop() {
        targetRpm = 0.0;
        flywheel.stopMotor();
    }
}
