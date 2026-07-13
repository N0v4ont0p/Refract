package org.firstinspires.ftc.teamcode.mechanisms.shooter;

import com.qualcomm.robotcore.hardware.HardwareMap;

/**
 * DECODE mechanism interface: a scoring mechanism that launches game pieces at
 * a commanded speed (season-extensions/decode-2025-26.yaml lists
 * {@code shooter: [flywheel, elastic_catapult, none]}; this interface fits the
 * flywheel case, the one this template ships an example for).
 *
 * Same rationale as {@link org.firstinspires.ftc.teamcode.drivetrain.Drivetrain}:
 * an OpMode talks to a Shooter through these four methods, never through a raw
 * DcMotorEx. That's what keeps a TeleOp from growing shooter-specific PID/hood
 * logic inline.
 */
public interface Shooter {

    /** Acquire hardware from the hardware map. */
    void init(HardwareMap hardwareMap);

    /** Command a target flywheel speed, in RPM. Pass 0 to spin down. */
    void setTargetVelocity(double rpm);

    /** Current measured flywheel speed, in RPM. */
    double getCurrentVelocity();

    /** True once measured speed is within tolerance of the last commanded target. */
    boolean atTargetVelocity();

    /** Cut power immediately. */
    void stop();
}
