package org.firstinspires.ftc.teamcode.opmodes;

import com.arcrobotics.ftclib.command.RunCommand;
import com.arcrobotics.ftclib.gamepad.GamepadEx;
import com.arcrobotics.ftclib.gamepad.GamepadKeys;

import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

import org.firstinspires.ftc.teamcode.drivetrain.Drivetrain;
import org.firstinspires.ftc.teamcode.drivetrain.MecanumDrivetrain;
import org.firstinspires.ftc.teamcode.mechanisms.intake.Intake;
import org.firstinspires.ftc.teamcode.mechanisms.intake.RollerIntake;

/**
 * Example TeleOp showing what an OpMode built on this template looks like:
 * construct one subsystem per mechanism, bind gamepad input to them, done.
 *
 * It wires only the drivetrain and an intake -- mechanisms every recent season
 * has used. Season mechanisms (a DECODE shooter/turret, a BIOBUZZ HIVE launcher,
 * ...) are added ONLY when the team's confirmed config declares them; the
 * shooter/ and turret/ packages are DECODE (2025-26) example implementations,
 * not something every robot gets.
 * There is deliberately no drivetrain/intake LOGIC here -- that
 * lives in the subsystem classes. This file should stay small forever; if
 * you're tempted to add a mechanism's control logic here instead of in its
 * own class, that's the God-OpMode pattern this template's structure exists
 * to prevent.
 *
 * Adjust to your real driver station layout / preset values before
 * competition.
 */
@TeleOp(name = "Example TeleOp", group = "Template")
public class ExampleTeleOp extends TeamOpMode {

    private Drivetrain drivetrain;
    private Intake intake;

    private GamepadEx driverGamepad;
    private GamepadEx operatorGamepad;

    @Override
    protected void onInit() {
        drivetrain = new MecanumDrivetrain();
        drivetrain.init(hardwareMap);

        intake = new RollerIntake();
        intake.init(hardwareMap);

        driverGamepad = new GamepadEx(gamepad1);
        operatorGamepad = new GamepadEx(gamepad2);

        // Drivetrain runs every loop by default from the driver's sticks --
        // this is what "no drive code in the OpMode loop" looks like.
        // (setDefaultCommand is a SubsystemBase/CommandScheduler feature, not
        // part of the Drivetrain contract itself -- the cast is for that, not
        // for anything drive-specific. Program against Drivetrain everywhere
        // else; this is the one place the concrete class's scheduler wiring
        // is needed.)
        ((MecanumDrivetrain) drivetrain).setDefaultCommand(new RunCommand(
                () -> drivetrain.drive(
                        driverGamepad.getLeftX(),
                        driverGamepad.getLeftY(),
                        driverGamepad.getRightX()
                ),
                (MecanumDrivetrain) drivetrain
        ));

        // Operator bindings -- each button owns exactly one mechanism call.
        operatorGamepad.getGamepadButton(GamepadKeys.Button.A)
                .whileHeld(() -> intake.intake())
                .whenReleased(intake::stop);

        operatorGamepad.getGamepadButton(GamepadKeys.Button.B)
                .whileHeld(() -> intake.reverse())
                .whenReleased(intake::stop);
    }
}
