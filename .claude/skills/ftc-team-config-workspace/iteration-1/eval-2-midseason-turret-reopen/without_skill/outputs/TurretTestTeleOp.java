package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

/**
 * TurretTestTeleOp — minimal test opmode for the Turret subsystem skeleton.
 *
 * Raw LinearOpMode style, matching the team's opmode_style in team-config.yaml.
 *
 * Controls (gamepad2):
 *   right stick X  -> manual aim (left/right)
 *   Y              -> preset: forward (0 deg)
 *   X              -> preset: left (+45 deg)
 *   B              -> preset: right (-45 deg)
 *   A              -> stop and hold
 *
 * SAFETY: line the turret up pointing straight ahead BEFORE pressing INIT —
 * that position becomes 0 degrees (there is no absolute encoder yet).
 * Start with MANUAL_MAX_POWER low in Turret.java until limits are verified.
 */
@TeleOp(name = "Turret Test", group = "Test")
public class TurretTestTeleOp extends LinearOpMode {

    @Override
    public void runOpMode() {
        Turret turret = new Turret();
        turret.init(hardwareMap);

        telemetry.addLine("Turret initialized. Zero = current heading.");
        telemetry.update();

        waitForStart();

        while (opModeIsActive()) {
            // Manual aiming (negated so pushing right turns right; flip if needed).
            turret.setManualPower(-gamepad2.right_stick_x);

            // Presets
            if (gamepad2.y) turret.goToForwardPreset();
            if (gamepad2.x) turret.goToLeftPreset();
            if (gamepad2.b) turret.goToRightPreset();
            if (gamepad2.a) turret.stop();

            turret.update();

            telemetry.addData("Mode", turret.getMode());
            telemetry.addData("Angle (deg)", "%.1f", turret.getCurrentAngleDeg());
            telemetry.addData("Target (deg)", "%.1f", turret.getTargetAngleDeg());
            telemetry.addData("On target", turret.isOnTarget());
            telemetry.update();
        }
    }
}
