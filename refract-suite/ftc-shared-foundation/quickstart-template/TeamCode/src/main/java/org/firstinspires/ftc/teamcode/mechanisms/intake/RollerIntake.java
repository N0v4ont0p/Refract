package org.firstinspires.ftc.teamcode.mechanisms.intake;

import com.arcrobotics.ftclib.command.SubsystemBase;
import com.arcrobotics.ftclib.hardware.motors.Motor;

import com.qualcomm.robotcore.hardware.HardwareMap;

import org.firstinspires.ftc.teamcode.RobotConstants;

/**
 * Roller-type {@link Intake}: a single motor spun one way to pick up game
 * pieces, the other way to clear a jam. A claw-type intake implements the
 * same interface with intake()/reverse()/stop() mapped to grip/release/
 * neutral instead.
 */
public class RollerIntake extends SubsystemBase implements Intake {

    private Motor roller;

    @Override
    public void init(HardwareMap hardwareMap) {
        roller = new Motor(hardwareMap, "intake");
    }

    @Override
    public void intake() {
        roller.set(RobotConstants.INTAKE_POWER);
    }

    @Override
    public void reverse() {
        roller.set(-RobotConstants.INTAKE_POWER);
    }

    @Override
    public void stop() {
        roller.stopMotor();
    }
}
