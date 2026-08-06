> Source: https://rr.brott.dev/docs/v1-0/guides/continuity/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Continuity | Road Runner Docs

# 
 Continuity
 #

The TrajectoryActionBuilder tries as best it can to make smooth paths without
kinks or changes of direction. Smooth paths are preferred because they can be
followed without stopping.

To make the notion of smoothness more precise, the TAB checks the continuity of
a few different values. It assumes that each individual line and spline segments
are continuous and checks that these values match at every junction.

Some violations are obvious. Take these two perpendicular line segments:

 .lineToX(24.0)
 .setTangent(Math.PI / 2)
 .lineToY(24.0)

There is no way for a robot to immediately change direction like that and so it
must come to a stop at that point. This is an example of a tangent
discontinuity.

Continuity is also relevant for the heading of the robot. A robot can’t
instantaneously go from spinning to maintaining a fixed heading:

 .lineToXLinearHeading(24.0, Math.PI / 2)
 .lineToX(48.0)

Similarly, a robot can’t go from spinning at one speed to spinning at another
speed:

 .lineToXLinearHeading(24.0, Math.PI / 2)
 .lineToXLinearHeading(48.0, 3 * Math.PI / 4)

Why do the two segments have different speeds? It has to do with the length of
each path segment and difference between the begin and end heading.

One way to get around this issue is to make one of them a spline heading. The
spline heading is more flexible than linear heading but has the downside of
being less preictable. You can put it at the beginning:

 .lineToXSplineHeading(24.0, Math.PI / 2)
 .lineToXLinearHeading(48.0, 3 * Math.PI / 4)

Or at the end:

 .lineToXLinearHeading(24.0, Math.PI / 2)
 .lineToXSplineHeading(48.0, 3 * Math.PI / 4)