package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.hardware.HardwareMap;
import com.qualcomm.robotcore.util.Range;

/**
 * Turret — single-axis turret aiming subsystem (skeleton).
 *
 * Matches team-config.yaml:
 *   - REV Control Hub only (no Expansion Hub) — turret motor plugs into a Control Hub port.
 *   - Raw LinearOpMode style — this is a plain helper class, NOT command-based.
 *     Construct it in runOpMode(), call update() every loop.
 *   - No vision and no odometry on the robot yet, so there is no auto-aim here.
 *     Aiming is manual (driver stick) plus preset positions. The goToAngle() hook
 *     is where auto-aim would plug in later if vision/odometry is added.
 *
 * ======================== TODO BEFORE FIRST RUN ========================
 * 1. Add the motor to the Robot Controller configuration with the name in
 *    HARDWARE_NAME below (or change the constant to match your config).
 * 2. Set TICKS_PER_MOTOR_REV for your motor (goBILDA 5203 values below).
 * 3. Set GEAR_RATIO to (turret gear teeth) / (motor gear teeth) — how many
 *    motor revolutions per one full turret revolution multiplier.
 * 4. Verify MIN_ANGLE_DEG / MAX_ANGLE_DEG against the real mechanical travel
 *    (wire harness wrap is usually the real limit — check it!).
 * 5. Decide the zero position: this skeleton assumes the turret is pointed
 *    straight ahead (0 degrees) when init runs, since there is no absolute
 *    encoder or limit switch yet.
 * =======================================================================
 */
public class Turret {

    // ---------- Tunable constants (all TODO: verify on the real robot) ----------

    /** Name of the turret motor in the RC hardware configuration. */
    public static final String HARDWARE_NAME = "turret";

    /** Encoder ticks per motor output-shaft revolution.
     *  goBILDA 5203 examples: 19.2:1 -> 537.7, 13.7:1 -> 384.5, 5.2:1 -> 145.1 */
    public static final double TICKS_PER_MOTOR_REV = 537.7;   // TODO: match your motor

    /** Motor revolutions per one turret revolution (external reduction).
     *  e.g. 100T turret gear driven by a 20T pinion -> 5.0 */
    public static final double GEAR_RATIO = 5.0;              // TODO: measure your gearing

    /** Derived: encoder ticks per degree of turret rotation. */
    public static final double TICKS_PER_DEGREE =
            (TICKS_PER_MOTOR_REV * GEAR_RATIO) / 360.0;

    /** Soft limits so the turret never over-rotates and wraps its wiring.
     *  0 = straight ahead; + is counter-clockwise viewed from above (adjust to taste). */
    public static final double MIN_ANGLE_DEG = -90.0;         // TODO: confirm travel
    public static final double MAX_ANGLE_DEG =  90.0;         // TODO: confirm travel

    /** Max power for manual aiming (keep low while testing!). */
    public static final double MANUAL_MAX_POWER = 0.4;

    /** Max power used when running to a preset/target angle. */
    public static final double GOTO_MAX_POWER = 0.6;

    /** Considered "on target" when within this many degrees. */
    public static final double TOLERANCE_DEG = 1.0;

    /** Deadband on the driver stick so the turret doesn't creep. */
    public static final double STICK_DEADBAND = 0.05;

    // Preset angles (degrees). TODO: tune at the field.
    public static final double PRESET_FORWARD_DEG = 0.0;
    public static final double PRESET_LEFT_DEG    = 45.0;
    public static final double PRESET_RIGHT_DEG   = -45.0;

    // ---------- State ----------

    private DcMotorEx motor;

    /** What the subsystem is currently doing. */
    public enum Mode {
        IDLE,        // holding position, no input
        MANUAL,      // driver stick controls power directly
        GO_TO_ANGLE  // running to targetAngleDeg (preset or future auto-aim)
    }

    private Mode mode = Mode.IDLE;
    private double targetAngleDeg = 0.0;
    private double manualPower = 0.0;

    // ---------- Lifecycle ----------

    /** Call once in runOpMode() before waitForStart(). Assumes turret is
     *  physically at 0 degrees (straight ahead) when this runs. */
    public void init(HardwareMap hardwareMap) {
        motor = hardwareMap.get(DcMotorEx.class, HARDWARE_NAME);

        // TODO: flip this if positive power turns the turret the wrong way.
        motor.setDirection(DcMotorSimple.Direction.FORWARD);

        // BRAKE so the turret holds its heading when power is zero.
        motor.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);

        // Zero the encoder here — this defines "0 degrees = wherever the
        // turret is pointing at init". Line the turret up before pressing INIT.
        motor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        motor.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
    }

    /** Call every loop iteration in your opmode's while(opModeIsActive()) loop. */
    public void update() {
        switch (mode) {
            case MANUAL:
                // Block manual power that would push past a soft limit.
                double power = manualPower;
                double angle = getCurrentAngleDeg();
                if ((angle >= MAX_ANGLE_DEG && power > 0)
                        || (angle <= MIN_ANGLE_DEG && power < 0)) {
                    power = 0.0;
                }
                motor.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                motor.setPower(power);
                break;

            case GO_TO_ANGLE:
                motor.setTargetPosition(angleToTicks(targetAngleDeg));
                motor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
                motor.setPower(GOTO_MAX_POWER);
                if (isOnTarget()) {
                    mode = Mode.IDLE; // arrived; RUN_TO_POSITION keeps holding
                }
                break;

            case IDLE:
            default:
                // If we were in manual, stop; if RUN_TO_POSITION, it self-holds.
                if (motor.getMode() == DcMotor.RunMode.RUN_USING_ENCODER) {
                    motor.setPower(0.0);
                }
                break;
        }
    }

    // ---------- Commands (call these from your opmode) ----------

    /** Manual aiming from a gamepad stick, e.g. setManualPower(-gamepad2.right_stick_x). */
    public void setManualPower(double stick) {
        if (Math.abs(stick) < STICK_DEADBAND) {
            // Stick released: if we were in manual, go idle and hold.
            if (mode == Mode.MANUAL) {
                mode = Mode.IDLE;
                manualPower = 0.0;
            }
            return;
        }
        mode = Mode.MANUAL;
        manualPower = Range.clip(stick, -1.0, 1.0) * MANUAL_MAX_POWER;
    }

    /** Send the turret to an absolute angle (degrees, clamped to soft limits).
     *  This is also the hook for future auto-aim: a vision/odometry targeting
     *  routine would compute an angle and call this. */
    public void goToAngle(double angleDeg) {
        targetAngleDeg = Range.clip(angleDeg, MIN_ANGLE_DEG, MAX_ANGLE_DEG);
        mode = Mode.GO_TO_ANGLE;
    }

    public void goToForwardPreset() { goToAngle(PRESET_FORWARD_DEG); }
    public void goToLeftPreset()    { goToAngle(PRESET_LEFT_DEG); }
    public void goToRightPreset()   { goToAngle(PRESET_RIGHT_DEG); }

    /** Immediately stop and hold whatever heading the turret is at. */
    public void stop() {
        mode = Mode.IDLE;
        manualPower = 0.0;
        motor.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        motor.setPower(0.0);
    }

    // ---------- Telemetry / status ----------

    public double getCurrentAngleDeg() {
        return motor.getCurrentPosition() / TICKS_PER_DEGREE;
    }

    public double getTargetAngleDeg() {
        return targetAngleDeg;
    }

    public boolean isOnTarget() {
        return Math.abs(getCurrentAngleDeg() - targetAngleDeg) <= TOLERANCE_DEG;
    }

    public Mode getMode() {
        return mode;
    }

    // ---------- Helpers ----------

    private int angleToTicks(double angleDeg) {
        return (int) Math.round(angleDeg * TICKS_PER_DEGREE);
    }
}
