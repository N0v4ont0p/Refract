> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/custom/curve.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Custom Curve
---

The Pedro Pathing follower is capable of following custom curves external to the library-provided ones. 
You can create your own curve by extending the abstract class `CustomCurve`.
Custom Curves **must** be twice differentiable, parameterized on the interval [0,1], and non-degenerate (meaning the curve must never satisfy $$x'(t) = y'(t) = 0$$ for $$t \in [0,1]$$).
There is an optional `initialization()` method that can be overridden to do something on the creation of the curve.
For example, the BezierCurve class stores the end tangent at this time.

Here is a simple example of a LinearSpline:

```java
import com.pedropathing.geometry.CustomCurve;
import com.pedropathing.geometry.Pose;
import com.pedropathing.math.Vector;
import com.pedropathing.paths.PathConstraints;
import java.util.Arrays;

public class LinearSpline extends CustomCurve {
    private Pose startPose;
    private Pose endPose;
    private Pose diffPose;

    public LinearSpline(Pose startPoint, Pose endPoint) {
        super(startPoint, endPoint);
    }

    public LinearSpline(FuturePose startPoint, FuturePose endPoint) {
        super(startPoint, endPoint);
    }

    public LinearSpline(Pose startPoint, Pose endPoint, PathConstraints constraints) {
        super(Arrays.asList(startPoint, endPoint), constraints);
    }

    @Override
    public String pathType() {
        return "Linear Spline";
    }

    @Override
    public LinearSpline getReversed() {
        LinearSpline curve = new LinearSpline(getControlPoints().get(1), getControlPoints().get(0), this.getPathConstraints());
        curve.initialize();
        return curve;
    }

    @Override
    public Vector getDerivative(double t) {
        return diffPose.getAsVector();
    }

    @Override
    public Pose getPose(double t) {
        if (startPose == null) init();

        double x = t * diffPose.getX() + startPose.getX();
        double y = t * diffPose.getY() + startPose.getY();

        return new Pose(x, y);
    }

    public void init() {
        startPose = getControlPoints().get(0);
        endPose = getControlPoints().get(1);
        diffPose = endPose.minus(startPose);
    }

    @Override
    public Vector getSecondDerivative(double t) {
        return new Vector();
    }
}
```
