"""
ponytail: one runnable check for the one branch that matters in IntakeSlide —
the soft-limit clamp in setTargetPosition(). Mirrors the Java formula exactly
(lowerBound=0, upperBound=SLIDE_MAX_TICKS-SLIDE_SOFT_LIMIT_MARGIN_TICKS,
clamp(ticks, lowerBound, upperBound)) so a future edit to the Java can be
sanity-checked here without a full FTC SDK build.
"""


def clamp_target(ticks: int, slide_max_ticks: int, margin_ticks: int) -> int:
    lower_bound = 0
    upper_bound = slide_max_ticks - margin_ticks
    return max(lower_bound, min(ticks, upper_bound))


def demo():
    # un-calibrated robot (SLIDE_MAX_TICKS still 0): must fail safe to 0, never negative
    assert clamp_target(1000, slide_max_ticks=0, margin_ticks=30) == 0

    # calibrated robot: normal in-range command passes through unchanged
    assert clamp_target(500, slide_max_ticks=2000, margin_ticks=30) == 500

    # over-extension request gets clamped to max minus margin, never past it
    assert clamp_target(5000, slide_max_ticks=2000, margin_ticks=30) == 1970

    # negative/retract-past-zero request clamped to 0, never negative
    assert clamp_target(-500, slide_max_ticks=2000, margin_ticks=30) == 0

    print("all clamp checks passed")


if __name__ == "__main__":
    demo()
