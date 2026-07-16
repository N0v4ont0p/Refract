package org.firstinspires.ftc.teamcode.opmodes;

// Suite-generated code: written by ftc-construct against team-config.yaml
// (team 99901, season decode-2025-26, season_mechanisms.shooter = flywheel).
// See team-config.yaml `_meta.suite_generated_code` for the lineage marker.

import com.arcrobotics.ftclib.command.InstantCommand;
import com.arcrobotics.ftclib.gamepad.GamepadEx;
import com.arcrobotics.ftclib.gamepad.GamepadKeys;

import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

import org.firstinspires.ftc.teamcode.mechanisms.shooter.FlywheelShooter;
import org.firstinspires.ftc.teamcode.mechanisms.shooter.Shooter;

/**
 * TeleOp for the shooter mechanism only (config: season_mechanisms.shooter = flywheel,
 * adapted directly from the quickstart template's FlywheelShooter example -- no new
 * shooter class needed). Drivetrain/turret/intake are declared in team-config.yaml but
 * were not part of this request, so no code for them lives in this file (per this
 * skill's rule: only build what's asked, on top of what's confirmed -- not the whole
 * robot every time a single mechanism's teleop is requested).
 *
 * Operator (gamepad2) controls:
 *   RIGHT_BUMPER held -> spin flywheel to RobotConstants.SHOOTER_TARGET_RPM (placeholder,
 *     see RobotConstants.java) -- see this file's own TODO if that constant isn't set yet.
 *   released -> spin down.
 *
 * R59 (ftc-hardware-lookup ask-don't-guess parity): this template ships no stored flywheel
 * launch-speed spec for this team's specific mechanism, so the target RPM is a placeholder
 * constant, not a generated number -- tune it against the real mechanism before competition.
 *
 * G416 (LAUNCH ZONE only): this OpMode does not enforce field position -- G416 is a
 * driver/strategy rule about where the robot is on the field when it launches, not
 * something the shooter subsystem's setTargetVelocity/stop API can detect or gate. Spinning
 * the flywheel up is legal anywhere; it's the drive team's responsibility to only be inside
 * a LAUNCH ZONE / overlapping a LAUNCH LINE when a SCORING ELEMENT actually leaves the
 * mechanism. No enforcement code added here -- flagged, not guessed at.
 */
@TeleOp(name = "Shooter TeleOp", group = "Generated")
public class ShooterTeleOp extends TeamOpMode {

    private Shooter shooter;
    private GamepadEx operatorGamepad;

    @Override
    protected void onInit() {
        shooter = new FlywheelShooter();
        shooter.init(hardwareMap);

        operatorGamepad = new GamepadEx(gamepad2);

        // TODO: RobotConstants has no SHOOTER_TARGET_RPM field yet (only
        // SHOOTER_VELOCITY_TOLERANCE_RPM) -- ftc-hardware-lookup's catalog has no stored
        // flywheel-speed spec for this team's specific launcher, so this is a fail-safe
        // placeholder per standing-principles' ask-don't-guess rule, not a generated number.
        // Add the real tuned value as a RobotConstants @Config field before competition.
        final double PLACEHOLDER_TARGET_RPM = 3000.0;

        operatorGamepad.getGamepadButton(GamepadKeys.Button.RIGHT_BUMPER)
                .whenPressed(new InstantCommand(() -> shooter.setTargetVelocity(PLACEHOLDER_TARGET_RPM)))
                .whenReleased(new InstantCommand(shooter::stop));
    }

    @Override
    protected void onRun() {
        telemetry.addData("shooter rpm", shooter.getCurrentVelocity());
        telemetry.addData("shooter at target", shooter.atTargetVelocity());
        // telemetry.update() is called for us by TeamOpMode.run() -- no need to call it here.
    }
}
