package org.firstinspires.ftc.teamcode.opmodes;

// Suite-generated (ftc-construct) — team-config.yaml: shooter=flywheel, opmode_style=ftclib_command_based.
// Adapted from quickstart-template's ExampleTeleOp (its shooter binding), scoped to shooter control only.

import com.arcrobotics.ftclib.command.InstantCommand;
import com.arcrobotics.ftclib.gamepad.GamepadEx;
import com.arcrobotics.ftclib.gamepad.GamepadKeys;

import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

import org.firstinspires.ftc.teamcode.mechanisms.shooter.FlywheelShooter;
import org.firstinspires.ftc.teamcode.mechanisms.shooter.Shooter;

/**
 * Operator control for the flywheel shooter only — this team's drivetrain
 * (swerve, 4 modules, custom-fabricated) has no example in the quickstart
 * template yet, so it is intentionally left out of this OpMode rather than
 * guessed at. This is a shooter-only TeleOp; wire it up alongside a drive
 * OpMode (or merge the two once a swerve Drivetrain implementation exists)
 * before running it standalone at a driver station.
 *
 * Same rule as the template's ExampleTeleOp: no shooter PID/velocity logic
 * here, that lives in {@link FlywheelShooter}. This OpMode only binds gamepad
 * buttons to the {@link Shooter} interface's four methods and reports
 * telemetry every loop (via TeamOpMode).
 */
@TeleOp(name = "Shooter TeleOp", group = "Shooter")
public class ShooterTeleOp extends TeamOpMode {

    // ponytail: placeholder preset, not a hardware spec — FlywheelShooter's own
    // javadoc already flags this: tune against the real flywheel before competition,
    // don't ship this number as-is.
    private static final double SHOOT_TARGET_RPM = 3000.0;

    private Shooter shooter;
    private GamepadEx operatorGamepad;

    @Override
    protected void onInit() {
        shooter = new FlywheelShooter();
        shooter.init(hardwareMap);

        operatorGamepad = new GamepadEx(gamepad2);

        // Two dedicated buttons (spin / stop) rather than the template example's
        // hold-a-bumper binding — a flywheel needs to stay spun up between shots,
        // not just while a finger is on the bumper.
        operatorGamepad.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
                .whenPressed(new InstantCommand(() -> shooter.setTargetVelocity(SHOOT_TARGET_RPM)));

        operatorGamepad.getGamepadButton(GamepadKeys.Button.LEFT_BUMPER)
                .whenPressed(new InstantCommand(shooter::stop));
    }

    @Override
    protected void onRun() {
        telemetry.addData("shooter target rpm", SHOOT_TARGET_RPM);
        telemetry.addData("shooter rpm", shooter.getCurrentVelocity());
        telemetry.addData("shooter at target", shooter.atTargetVelocity());
        // telemetry.update() is called for us by TeamOpMode.run() -- no need to call it here.
    }
}
