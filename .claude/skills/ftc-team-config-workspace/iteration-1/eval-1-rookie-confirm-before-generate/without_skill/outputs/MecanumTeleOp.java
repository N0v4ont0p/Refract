/*
 * Team 99902 - Mecanum TeleOp
 * ---------------------------
 * Drive OpMode for the goBILDA Strafer Chassis Kit (4 mecanum wheels,
 * 4x goBILDA 5203 Yellow Jacket motors) running on a REV Control Hub.
 *
 * CONTROLS (gamepad 1):
 *   Left stick Y  -> drive forward / backward
 *   Left stick X  -> strafe left / right
 *   Right stick X -> turn left / right
 *   Right bumper (hold) -> slow mode (30% speed) for fine control
 *
 * ROBOT CONFIGURATION (on the Driver Station app):
 *   Create a configuration with these four DC motors, all "GoBILDA 5202/3/4 series":
 *     Control Hub motor port 0 -> "frontLeft"
 *     Control Hub motor port 1 -> "backLeft"
 *     Control Hub motor port 2 -> "frontRight"
 *     Control Hub motor port 3 -> "backRight"
 *   (If you plugged motors into different ports, that's fine — just make sure
 *   each name matches the physical motor it's wired to.)
 *
 * FIRST TEST CHECKLIST (robot on blocks, wheels off the ground!):
 *   1. Push left stick forward -> all 4 wheels should spin so the robot would go forward.
 *      If ONE wheel spins the wrong way, flip that motor's direction below.
 *   2. Then place on the floor and check strafe: left stick right should move the robot right.
 */

package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;

@TeleOp(name = "Mecanum TeleOp (99902)", group = "Drive")
public class MecanumTeleOp extends LinearOpMode {

    // Speed multipliers
    private static final double NORMAL_SPEED = 1.0;
    private static final double SLOW_SPEED   = 0.3;

    @Override
    public void runOpMode() {
        // --- Hardware map: names must match your robot configuration exactly ---
        DcMotor frontLeft  = hardwareMap.get(DcMotor.class, "frontLeft");
        DcMotor backLeft   = hardwareMap.get(DcMotor.class, "backLeft");
        DcMotor frontRight = hardwareMap.get(DcMotor.class, "frontRight");
        DcMotor backRight  = hardwareMap.get(DcMotor.class, "backRight");

        // On the Strafer kit the left-side motors face the opposite direction
        // from the right side, so reverse the left side. If your robot drives
        // backwards or a wheel fights the others, flip the direction of that motor.
        frontLeft.setDirection(DcMotorSimple.Direction.REVERSE);
        backLeft.setDirection(DcMotorSimple.Direction.REVERSE);
        frontRight.setDirection(DcMotorSimple.Direction.FORWARD);
        backRight.setDirection(DcMotorSimple.Direction.FORWARD);

        // Brake when the sticks are released (robot stops instead of coasting)
        frontLeft.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        backLeft.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        frontRight.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        backRight.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);

        telemetry.addLine("Initialized - waiting for start");
        telemetry.addLine("Hold RIGHT BUMPER for slow mode");
        telemetry.update();

        waitForStart();

        while (opModeIsActive()) {
            // --- Read gamepad ---
            // Gamepad Y axis is negative when pushed forward, so negate it.
            double drive  = -gamepad1.left_stick_y;   // forward / backward
            double strafe =  gamepad1.left_stick_x;   // left / right
            double turn   =  gamepad1.right_stick_x;  // rotation

            // Slow mode while holding right bumper
            double speed = gamepad1.right_bumper ? SLOW_SPEED : NORMAL_SPEED;

            // --- Standard mecanum mixing ---
            double flPower = drive + strafe + turn;
            double blPower = drive - strafe + turn;
            double frPower = drive - strafe - turn;
            double brPower = drive + strafe - turn;

            // Scale so no wheel power exceeds 1.0 (keeps steering proportional)
            double max = Math.max(1.0, Math.max(Math.abs(flPower),
                         Math.max(Math.abs(blPower),
                         Math.max(Math.abs(frPower), Math.abs(brPower)))));

            frontLeft.setPower(flPower / max * speed);
            backLeft.setPower(blPower / max * speed);
            frontRight.setPower(frPower / max * speed);
            backRight.setPower(brPower / max * speed);

            // --- Telemetry for the Driver Station screen ---
            telemetry.addData("Mode", gamepad1.right_bumper ? "SLOW (30%)" : "NORMAL");
            telemetry.addData("Drive", "%.2f", drive);
            telemetry.addData("Strafe", "%.2f", strafe);
            telemetry.addData("Turn", "%.2f", turn);
            telemetry.update();
        }
    }
}
