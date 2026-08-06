> Source: https://rr.brott.dev/docs/v1-0/guides/pose-mapping/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Pose Mapping | Road Runner Docs

# 
 Pose Mapping
 #

FTC teams usually develop two versions of their autonomous routines depending on
their alliance color. The op modes are often very similar with minor changes to
reverse certain coordinates and headings. To avoid having to adjust coordinates
before giving them to TrajectoryActionBuilder, teams can use pose maps.

As pose map tells the builder how to transform the poses. Say you want to apply
a reflection across the x-axis: 

 \( (x, y, \theta) \mapsto (x, -y,
-\theta) \)

. The pose map (final argument) is a pretty direct
translation:

new TrajectoryBuilder(new TrajectoryBuilderParams(eps,
 new ProfileParams(dispResolution, angResolution, eps)),
 beginPose, beginEndVel,
 baseVelConstraint, baseAccelConstraint,
 pose -> new Pose2dDual<>(
 pose.position.x, pose.position.y.unaryMinus(), pose.heading.inverse()));

When the pose map is applied to trajectory

the result is

Keep in mind that the pose map is applied after the trajectory and motion
profile is created. So if your constraints depend on the pose (e.g., they
specify a lower velocity for certain regions of the field), they will be
evaluated at the original, unmapped poses.