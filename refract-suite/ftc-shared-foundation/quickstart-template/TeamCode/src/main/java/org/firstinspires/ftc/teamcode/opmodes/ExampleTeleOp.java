package org.firstinspires.ftc.teamcode.opmodes;

import com.arcrobotics.ftclib.command.InstantCommand;
import com.arcrobotics.ftclib.command.RunCommand;
import com.arcrobotics.ftclib.gamepad.GamepadEx;
import com.arcrobotics.ftclib.gamepad.GamepadKeys;

import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

import org.firstinspires.ftc.teamcode.RobotConstants;
import org.firstinspires.ftc.teamcode.drivetrain.Drivetrain;
import org.firstinspires.ftc.teamcode.drivetrain.MecanumDrivetrain;
import org.firstinspires.ftc.teamcode.mechanisms.intake.Intake;
import org.firstinspires.ftc.teamcode.mechanisms.intake.RollerIntake;
import org.firstinspires.ftc.teamcode.mechanisms.shooter.FlywheelShooter;
import org.firstinspires.ftc.teamcode.mechanisms.shooter.Shooter;
import org.firstinspires.ftc.teamcode.mechanisms.turret.SingleAxisTurret;
import org.firstinspires.ftc.teamcode.mechanisms.turret.Turret;

/**
 * Example TeleOp showing what an OpMode built on this template looks like:
 * construct one subsystem per mechanism, bind gamepad input to them, done.
 * There is deliberately no drivetrain/shooter/turret/intake LOGIC here -- that
 * lives in the subsystem classes. This file should stay small forever; if
 * you're tempted to add a mechanism's control logic here instead of in its
 * own class, that's the God-OpMode pattern this template's structure exists
 * to prevent.
 *
 * Adjust to your real driver station layout / preset values before
 * competition -- the RPM/angle presets below are placeholders.
 */
@TeleOp(name = "Example TeleOp", group = "Template")
public class ExampleTeleOp extends TeamOpMode {

    private Drivetrain drivetrain;
    private Shooter shooter;
    private Turret turret;
    private Intake intake;

    private GamepadEx driverGamepad;
    private GamepadEx operatorGamepad;

    @Override
    protected void onInit() {
        drivetrain = new MecanumDrivetrain();
        drivetrain.init(hardwareMap);

        shooter = new FlywheelShooter();
        shooter.init(hardwareMap);

        turret = new SingleAxisTurret();
        turret.init(hardwareMap);

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

        operatorGamepad.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
                .whenPressed(new InstantCommand(() -> shooter.setTargetVelocity(3000)))
                .whenReleased(new InstantCommand(shooter::stop));

        operatorGamepad.getGamepadButton(GamepadKeys.Button.DPAD_LEFT)
                .whenPressed(new InstantCommand(() -> turret.setAngle(RobotConstants.TURRET_MIN_ANGLE_DEG)));
        operatorGamepad.getGamepadButton(GamepadKeys.Button.DPAD_RIGHT)
                .whenPressed(new InstantCommand(() -> turret.setAngle(RobotConstants.TURRET_MAX_ANGLE_DEG)));
    }

    @Override
    protected void onRun() {
        telemetry.addData("shooter rpm", shooter.getCurrentVelocity());
        telemetry.addData("shooter at target", shooter.atTargetVelocity());
        telemetry.addData("turret angle", turret.getCurrentAngle());
        // telemetry.update() is called for us by TeamOpMode.run() -- no need to call it here.
    }
}
