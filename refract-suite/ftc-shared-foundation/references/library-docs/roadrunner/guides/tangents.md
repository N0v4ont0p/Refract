> Source: https://rr.brott.dev/docs/v1-0/guides/tangents/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Tangents | Road Runner Docs

# 
 Tangents
 #

Picture a robot traveling along a path. The direction that the robot is moving
at any given point is the tangent at the point. Lines have a fixed tangent
direction; splines have a variable tangent.

By default, the heading of the robot follows the tangent. In fact, tank robots
are required to have the heading match the tangent (if you want to impress your
friends, this is a nonholonomic constraint). Mecanum robots are more flexible
and have a decoupled heading and tangent.

It’s important to separate heading and tangent in one’s mind. The tangent of
this path

 .lineToX(48.0)

is the same as this path

 .lineToXLinearHeading(48.0, Math.PI / 2)

despite the heading changing.

When using TrajectoryActionBuilder, the begin tangent of any new path segment
is chosen to match the end tangent of the last segment (this helps maintain
continuity). But the tangent can still be changed manually
using setTangent(). (The heading cannot be changed, however, because that
would require the robot to teleport instead of merely coming to a stop.)

Finally, reversing the robot is the same as setting the tangent to be 180
degrees from where it currently is. Every call to setReversed() is secretly a
call to setTangent().