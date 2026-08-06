> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/drive-algorithm/predictive/configuration.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: "Tuning Predictive Braking"
---

<Callout type='warn' title="PIDFs vs. Predictive Braking">
You may either use PIDFs or Predictive Braking to control your robot.  
However, swerve and tank are currently not compatible with Predictive Braking.
All further steps are for Predictive Braking users only.  
</Callout>

1. Run the Tuning.java OpMode -> Automatic -> PredictiveBrakingTuner. This will give you values for `kQuadratic` and `kLinear`. In FollowerConstants, add `.predictiveBrakingCoefficients(new PredictiveBrakingCoefficients(kP, kLinear, kQuadratic))`. Insert the values given from the tuner into the method. Use a starting kP value around `0.1`.
 - `kQuadratic` represents the braking distance proportional to velocity squared. This is caused by constant forces such as braking power and sliding friction.
 - `kLinear` represents braking distance roughly proportional to velocity. This is caused by velocity-proportional forces such as back-EMF, torque delay, and viscous friction.

<iframe
  width="560"
  height="315"
  src="https://www.youtube-nocookie.com/embed/4JbpJi-8MOQ"
  title="PredictiveBrakingTuner"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

Do not be worried if the robot's heading turns while braking in the tuner. This is expected and does not hurt the results. Consider making a more balanced center of mass to combat this. In the future, the tuner will have heading correction.

Also do not be worried if your robot lifts off the ground while braking. This is normal as long as odometry can still get accurate measurements. 

2. Run LineTest and adjust kP to your liking. kP usually ranges from `0.05-0.3`. kP changes are harder to notice and have minimal effects due to kP accounting for predicted error. However, tune kP as high as possible to maximize holding strength and accuracy, without jittering the robot. If you want smoother or sooner deceleration, try experimenting with kP of 0.05 or lower and increasing the kQuadratic term, as this will act more like a motion profile.

3. Currently, it is recommended to turn **off centripetal** forces in auto, as predictive braking naturally accounts for this. This can be done by adding the following in FollowerConstants.
```java title="Constants.java"
.centripetalScaling(0)
```

4. **Lower the parametric end constraint**. Set it to a value like 0.97 or 0.95. PIDFs often overshoot and hit the parametric end early, but predictive braking fully stops in time, delaying when actions can trigger. Lowering the constraint lets actions trigger sooner and speeds up overall execution. However, do not set the parametric value very low (\<0.9) or predictive braking will not work as intended because it will end the path before braking.

At the end of tuning, you should have at least this in FollowerConstants.
```java title="Constants.java"
 public static FollowerConstants followerConstants = new FollowerConstants()
     .headingPIDFCoefficients(new PIDFCoefficients(1.5, 0, 0.1, 0)) // tuned constants
     .predictiveBrakingCoefficients(new PredictiveBrakingCoefficients(0.1, 0.04, 0.0016)) // (kP, kLinear, kQuadratic)
     .centripetalScaling(0)
```

### After tuning, the LineTest should look like this video
<iframe
  width="560"
  height="315"
  src="https://www.youtube-nocookie.com/embed/4g8-_Toy388"
  title="Predictive Braking LineTest"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

## Effective Predictive Braking with Pathing
If you run a previously constructed autonomous, you will see that predictive braking effectively eliminates overshoot, but it may slow down your auto if you do not continue pathchains. This is because predictive braking comes to a complete stop when using individual paths. If you instead use pathchains wherever you do not need to fully stop, the robot will maintain its momentum. Future updates will allow smooth handling of sharp angles without stopping by predicting the next path automatically.
