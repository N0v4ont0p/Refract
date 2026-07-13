> Source: https://rr.brott.dev/docs/v1-0/tuning/ · Fetched: 2026-07-12

# Road Runner — Tuning (v1.0.x)

**LEGACY REFERENCE.** RoadRunner 1.0.x. Not the primary recommended
path-following library in this project anymore.

The whole tuning process "shouldn't take more than a few hours." It runs a
series of OpModes while you record robot behavior and feed values back into
the drive class. Read the source docs carefully — per the docs, "most
details are only mentioned once and you don't want to miss them."

## Initial setup

Pick `MecanumDrive` or `TankDrive` and set the correct hardware names.
Positive power on all wheels should move the robot forward. Verify motor
encoder directions with `MecanumDirectionDebugger` or
`DeadWheelDirectionDebugger` (encoder direction is independent of motor
power direction, so both must be checked separately).

### Supported localization options

- Drive encoders (default)
- Two dead wheels
- Three dead wheels
- Pinpoint Odometry Computer
- SparkFun OTOS sensor

If using two parallel dead wheels, the docs recommend wiring them to ports
0 and 3 on the REV hub.

## Tuning sequence

1. **`ForwardPushTest`** — push the robot forward across field tiles by
   hand and record ticks traveled, to determine `inPerTick` empirically:
   `inPerTick = real distance traveled / ticks traveled`. Set this in your
   drive class.

2. **`LateralPushTest`** (mecanum with drive encoders only) — same idea,
   pushed sideways, to determine `lateralInPerTick`.

3. **`ForwardRampLogger`** (dead wheels only) — ramps power up 0.1/second to
   0.9 to determine static and velocity feedforward, `kS` and `kV`. Analyze
   the resulting data via FTC Dashboard at
   `http://192.168.43.1:8080/tuning/forward-ramp.html`, excluding outlier
   points from the regression.

4. **`LateralRampLogger`** (mecanum with dead wheels) — same as above but for
   strafing, to determine `lateralInPerTick`. Note: a single multiplicative
   factor doesn't fully capture most robots' strafing behavior.

5. **`AngularRampLogger`** — in-place rotation ramp to determine track width
   and angular feedforward.
   - Drive encoders: analyze at
     `http://192.168.43.1:8080/tuning/drive-encoder-angular-ramp.html`
   - Dead wheels: analyze at
     `http://192.168.43.1:8080/tuning/dead-wheel-angular-ramp.html` (you'll
     need to input the `kS`/`kV` from step 3 here).

6. **`ManualFeedforwardTuner`** — robot repeats a forward/backward move over
   a fixed distance; graph `vref` against `v0` and adjust `kA` until they
   track well.

7. **`ManualFeedbackTuner`** — tunes feedback (PID-like) gains on top of the
   feedforward. Tune one parameter at a time; start small (e.g. `1`) and
   increase from there.

8. **`SplineTest`** — robot follows a basic spline as an end-to-end
   validation of the prior tuning steps.

## OTOS-specific pre-tuning

If using the SparkFun OTOS sensor, run these four steps before the standard
sequence above:

1. **`OTOSAngularScalarTuner`** — robot spins 10 full revolutions to
   calibrate angular accuracy.
2. **`OTOSLinearScalarTuner`** — forward-motion test to calibrate linear
   distance accuracy.
3. **`OTOSHeadingOffsetTuner`** — wall-based test to correct heading bias.
4. **`OTOSPositionOffsetTuner`** — corner-based test to determine position
   offset on both axes.

## Practical notes

- Avoid wheel slip during every test — it corrupts the data.
- Motor encoder direction and motor power direction are independent; check
  both.
- Re-run tuning if the robot's weight distribution or drivetrain changes
  meaningfully mid-season.
