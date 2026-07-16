// Snippet only — NOT applied to the real quickstart-template/RobotConstants.java
// (this task's scope guardrail restricts writes to this outputs/ directory).
// Add these fields to RobotConstants.java's existing @Config class, next to
// the existing TURRET_MIN_ANGLE_DEG / TURRET_MAX_ANGLE_DEG pair, following
// the same "soft limit as a live-tunable field" idiom already used there.

// -- Intake slide (mechanisms/intake/IntakeSlide.java) --
// SLIDE_MAX_TICKS: encoder count at full physical extension, MEASURED on
// the actual robot (see IntakeSlide.java's header comment for the 3-step
// calibration procedure) — NOT a spec value, because neither the goBILDA
// Viper-Slide build guide nor ftc-hardware-lookup's catalogs contain a
// travel-distance number for this kit. Left at 0 so an un-calibrated robot
// soft-limits to "cannot extend at all" (fails safe) rather than silently
// allowing full range with no real limit.
public static int SLIDE_MAX_TICKS = 0; // TODO calibrate — see IntakeSlide.java header
public static int SLIDE_SOFT_LIMIT_MARGIN_TICKS = 30; // ponytail: flat tick margin, not %-of-range; revisit if slide is re-geared
public static int SLIDE_POSITION_TOLERANCE_TICKS = 20;
public static double SLIDE_POWER = 0.8;
