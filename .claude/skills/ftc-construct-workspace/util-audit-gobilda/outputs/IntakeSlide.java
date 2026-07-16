package org.firstinspires.ftc.teamcode.mechanisms.intake;

import com.arcrobotics.ftclib.command.SubsystemBase;

import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.HardwareMap;
import com.qualcomm.robotcore.hardware.DcMotor;

import org.firstinspires.ftc.teamcode.RobotConstants;

/*
 * SUITE-GENERATED FILE — refract-suite / ftc-construct.
 * Generated against team-config.yaml (team 99904): drivetrain=mecanum,
 * season_mechanisms.intake=roller. This class is the vertical-travel actuator
 * that carries that roller intake on a goBILDA Viper-Slide, NOT the roller
 * intake itself (see RollerIntake.java for the roller motor).
 *
 * GROUNDING GAP — READ BEFORE TUNING (do not delete this notice):
 * This request asked for soft limits "based on [the slide's] actual maximum
 * travel distance." Per standing-principles.md §2 (abstention) and §4
 * (ask, don't guess), that number is NOT filled in below with a spec figure,
 * because no source in this repo actually contains one:
 *   - refract-suite/ftc-shared-foundation/references/library-docs/
 *     gobilda-build-guides/viper-slide-linear-slide-build.md was read in
 *     full. It is an assembly/wiring guide (screws, brackets, stage stacking
 *     order) and states each raw slide segment is 336 mm long — but it never
 *     states the assembled kit's total usable stroke/extension, which is
 *     shorter than (stage count x 336mm) once inter-stage overlap needed for
 *     structural rigidity at full extension is accounted for. Nothing in
 *     that file is a travel-distance spec.
 *   - ftc-hardware-lookup's catalogs (references/catalogs/motors.json,
 *     servos.json) have no linear-slide entry at all.
 * So SLIDE_MAX_TICKS below is left as an explicit calibration TODO, not a
 * guessed number. Filling it with an invented figure (e.g. some inches
 * pulled from memory of goBILDA's product page) is exactly the "plausible
 * filled gap" standing-principles.md warns costs more than an admitted one
 * — a wrong soft limit here is the one thing standing between a real slide
 * and the "snap" this request is trying to prevent.
 *
 * HOW TO FILL IT IN (5 minutes, once, per robot):
 *   1. With the slide fully retracted, zero the encoder (RUN_WITHOUT_ENCODER
 *      -> STOP_AND_RESET_ENCODER -> RUN_USING_ENCODER, or power-cycle after
 *      init).
 *   2. Manually (motor unpowered) or at low power, extend the slide to its
 *      true mechanical hard stop and read getCurrentPosition() off telemetry
 *      or FTC Dashboard.
 *   3. Set SLIDE_MAX_TICKS to that reading MINUS a safety margin (this file
 *      already reserves SLIDE_SOFT_LIMIT_MARGIN_TICKS below — don't zero it
 *      out). Re-check after any spool, motor, or stage-count change.
 */
public class IntakeSlide extends SubsystemBase {

    private DcMotorEx slideMotor;

    @Override
    public void periodic() {
        // Clamp is enforced in setTargetPosition() below, not here — no
        // separate "current position" polling needed for a soft limit that
        // only gates commanded targets.
    }

    public void init(HardwareMap hardwareMap) {
        slideMotor = hardwareMap.get(DcMotorEx.class, "intakeSlide");
        slideMotor.setDirection(DcMotorEx.Direction.FORWARD);
        slideMotor.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        slideMotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        slideMotor.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
    }

    /**
     * Command the slide to an absolute encoder-tick position, clamped to the
     * soft-limit range [0, SLIDE_MAX_TICKS - SLIDE_SOFT_LIMIT_MARGIN_TICKS].
     * This is the only path that should ever call setTargetPosition() on the
     * underlying motor — every caller (teleop button, autonomous step) routes
     * through here so the clamp cannot be bypassed by a caller that forgets.
     */
    public void setTargetPosition(int ticks) {
        int lowerBound = 0;
        int upperBound = RobotConstants.SLIDE_MAX_TICKS - RobotConstants.SLIDE_SOFT_LIMIT_MARGIN_TICKS;
        int clamped = Math.max(lowerBound, Math.min(ticks, upperBound));

        slideMotor.setTargetPosition(clamped);
        slideMotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
        slideMotor.setPower(RobotConstants.SLIDE_POWER);
    }

    public void retract() {
        setTargetPosition(0);
    }

    public int getCurrentPosition() {
        return slideMotor.getCurrentPosition();
    }

    public boolean isAtTarget() {
        return Math.abs(slideMotor.getTargetPosition() - slideMotor.getCurrentPosition())
                < RobotConstants.SLIDE_POSITION_TOLERANCE_TICKS;
    }

    public void stop() {
        slideMotor.setPower(0);
    }
}
