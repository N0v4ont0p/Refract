package org.firstinspires.ftc.teamcode.mechanisms.intake;

import com.arcrobotics.ftclib.command.SubsystemBase;

import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.HardwareMap;

import org.firstinspires.ftc.teamcode.RobotConstants;

/*
 * SUITE-GENERATED FILE -- refract-suite / ftc-construct (Phase D regression re-test).
 * Generated against team-config.yaml (team 99901, veteran-swerve-turret fixture):
 * season_mechanisms.intake = roller. This class is the vertical/horizontal travel
 * actuator carrying the roller intake on a goBILDA Viper-Slide -- NOT the roller
 * intake motor itself (see RollerIntake.java for that).
 *
 * GROUNDING GAP -- READ BEFORE TUNING (do not delete this notice):
 * The request was for a soft limit "based on the viper slide's real travel range."
 * That number is deliberately NOT filled in below with a spec figure, per
 * standing-principles.md Sections 2 (abstention) and 4 (ask, don't guess), and per
 * SKILL.md Section 3's explicit instruction on this exact file:
 *
 *   "goBILDA build guides (gobilda-build-guides/) are a known, permanent partial
 *   exception: they are physical assembly instructions, not code/API references,
 *   and even the closest-fit file (viper-slide-linear-slide-build.md) has been
 *   confirmed to lack the derived numbers (net travel distance) generation
 *   actually needs -- a corpus-completeness gap, not a wiring one. Treat a miss
 *   here as an ask-don't-guess abstention (ship a fail-safe placeholder with a
 *   TODO, per standing-principles), not something to keep searching the guide for."
 *
 * viper-slide-linear-slide-build.md was re-read in full for this generation. It is
 * an assembly/wiring guide (kit contents, screw sizes, stage-stacking order). Its
 * only length figure is the raw per-segment slide length -- "Covers both the
 * 4-Stage ... and 2-Stage ... belt-driven Viper-Slide kits, 336mm slide length" --
 * which is one Viper-Slide segment's length, not the assembled kit's net usable
 * extension (shorter than segment_length x stage_count once the overlap each stage
 * needs for rigidity at full extension is subtracted). No net-travel figure is
 * anywhere in that file. ftc-hardware-lookup's catalogs (motors.json, servos.json)
 * were also checked -- no linear-slide travel-distance entry exists there either.
 * So SLIDE_MAX_TICKS below stays an explicit calibration TODO, not a guessed
 * number -- see RobotConstants-additions.java for the placeholder value and the
 * fail-safe reasoning.
 */
public class IntakeSlide extends SubsystemBase {

    private DcMotorEx slideMotor;

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
     * Every caller (teleop button, autonomous step) routes through here so the
     * clamp can't be bypassed by a caller that forgets it. While
     * SLIDE_MAX_TICKS is uncalibrated (still 0, its shipped placeholder), the
     * upper bound collapses to a negative number and the clamp pins every
     * target to 0 -- the slide fails safe to "cannot extend" rather than
     * silently honoring an unbounded target.
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
