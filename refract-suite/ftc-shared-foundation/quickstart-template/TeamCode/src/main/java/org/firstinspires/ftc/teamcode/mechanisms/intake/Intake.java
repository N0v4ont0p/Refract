package org.firstinspires.ftc.teamcode.mechanisms.intake;

import com.qualcomm.robotcore.hardware.HardwareMap;

/**
 * Intake interface: brings game pieces into the robot. Every season file so far
 * declares an {@code intake} mechanism (DECODE: roller/claw/other; BIOBUZZ:
 * roller/other/none -- read the ACTIVE season-extensions file, not this comment);
 * this interface fits roller, the case this template ships an example for. A claw-type intake implements the same three verbs (intake/reverse/
 * stop map to open/close/hold, or grip/release/neutral) rather than getting a
 * different interface shape per hardware choice.
 */
public interface Intake {

    /** Acquire hardware from the hardware map. */
    void init(HardwareMap hardwareMap);

    /** Run the intake inward (pick up game pieces). */
    void intake();

    /** Run the intake outward (clear a jam / eject). */
    void reverse();

    /** Stop the intake. */
    void stop();
}
