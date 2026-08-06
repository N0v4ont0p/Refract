> Source: https://rr.brott.dev/docs/v1-0/migration/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Migrating from 0.5.x | Road Runner Docs

# 
 Migrating from 0.5.x
 #

This document assesses the 1.0.0 API changes that will most affect teams using the
library.

## 
 Packages
 #

Previously, classes were scattered across many subpackages of
com.acmerobotics.roadrunner. Now everything can be found in the root package.

## 
 Trajectory Builder
 #

Most of the methods are the same and should feel familiar. The most notable change
is splitting lineTo() into two methods, lineToX() and lineToY(). Line directions
will now automatically match the path tangent for continuity unless setTangent() is
called. Wherever possible, the trajectory builder encourages continuity.

## 
 Trajectory Sequences
 #

Trajectory sequences have been extended intoa a full actions system. Each action
describes a task that executes in a bunch of small steps. For example, following
a trajectory is an action made up of “read encoders, compute deviation from the
trajectory, set motor powers, read encoders, compute deviation …”. The
TrajectoryActionBuilder class takes the place of TrajectorySequenceBuilder
in making it easy to combine following trajectories with moving servos, setting
motor powers, and any other behaviors you might want.

Markers are included in the new system. Here’s an example:

builder
.lineToX(-12)
.afterDisp(5, dispMarker)
.splineTo(Vector2d(-24, -12), -Math.PI / 2)
.turn(Math.PI / 2)
.afterTime(0.5, tempMarker)
.turn(Math.PI / 2)
.setReversed(true)
.splineTo(Vector2d(-36, 0), Math.PI)

The action dispMarker triggers 5 units after the end of the first line and
is similar to a displacement marker. The action tempMarker triggers half of a second
after the first turn begins and is similar to a temporal marker.

## 
 PID Controller
 #

Some old classes didn’t make the cut for the new code. Among this group is PIDFController,
which you can find here in Java.
All of the other old files are still available on GitHub, and you can copy them into your codebase if you need to.
Nothing is gone completely.