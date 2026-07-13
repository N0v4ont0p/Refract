package org.firstinspires.ftc.teamcode.mechanisms.turret;

import com.qualcomm.robotcore.hardware.HardwareMap;

/**
 * DECODE mechanism interface: aims a {@link org.firstinspires.ftc.teamcode.mechanisms.shooter.Shooter}
 * independently of drivetrain heading (season-extensions/decode-2025-26.yaml's
 * {@code turret: [none, single_axis, multi_axis]} axis; this interface fits
 * single_axis, the case this template ships an example for). A turret only
 * ever makes sense paired with a shooter -- see the season yaml's
 * constraints_on_mechanisms entry ("a turret aims a shooter; a turret with no
 * shooter is incoherent").
 */
public interface Turret {

    /** Acquire hardware from the hardware map. */
    void init(HardwareMap hardwareMap);

    /** Command an absolute turret angle, in degrees, relative to robot-forward. */
    void setAngle(double degrees);

    /** Current turret angle, in degrees. */
    double getCurrentAngle();

    /** True once measured angle is within tolerance of the last commanded target. */
    boolean atTargetAngle();

    /** Hold current position (servo turrets don't need an explicit "off"; motor ones may). */
    void stop();
}
