// Snippet only -- NOT applied to the real quickstart-template/RobotConstants.java.
// This task's scope guardrail restricts writes to this outputs/ directory, and a
// real ftc-construct run would add these fields to RobotConstants.java's existing
// @Config class, next to TURRET_MIN_ANGLE_DEG / TURRET_MAX_ANGLE_DEG, following the
// same "soft limit as a live-tunable field" idiom already used there.

// -- Intake slide (mechanisms/intake/IntakeSlide.java) --
// SLIDE_MAX_TICKS: encoder count at full physical extension, MEASURED on the
// actual robot (see IntakeSlide.java's header for why: neither the goBILDA
// Viper-Slide build guide nor ftc-hardware-lookup's catalogs publish a net
// travel-distance number for this kit). Left at 0 so an un-calibrated robot
// soft-limits to "cannot extend at all" -- fails safe -- rather than silently
// allowing an unbounded target.
public static int SLIDE_MAX_TICKS = 0; // TODO calibrate -- see IntakeSlide.java header for the 3-step procedure:
                                        // 1. zero the encoder with the slide fully retracted
                                        // 2. drive to the true mechanical hard stop, read getCurrentPosition()
                                        // 3. set this field to that reading minus SLIDE_SOFT_LIMIT_MARGIN_TICKS' margin
public static int SLIDE_SOFT_LIMIT_MARGIN_TICKS = 30; // ponytail: flat tick margin, not %-of-range; revisit if re-geared
public static int SLIDE_POSITION_TOLERANCE_TICKS = 20;
public static double SLIDE_POWER = 0.8;
