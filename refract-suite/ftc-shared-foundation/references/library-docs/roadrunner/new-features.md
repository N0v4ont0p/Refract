> Source: https://rr.brott.dev/docs/v1-0/new-features/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

New Features | Road Runner Docs

# 
 New Features
 #

The biggest change is a new quickstart redesigned from the ground up to give better
calibration results in less time. It also incorporates community wisdom around control
schemes and has first-class support for dead wheel odometry.

On top of that, there are significant changes to the API of the core library. The
mathematical tools and approach remain largely the same, but they have a fresh coat of
paint. And then there a few notable features added to the library:

- 
No more PathContinuityViolationException errors! The usual builders now
produce sequences of paths or trajectories. Instead of failing on a continuity
violation, they split the path/trajectory.

- 
Motion profiles and constraints support asymmetric acceleration limits.
can now specify deceleration and acceleration limits on profile and
trajectories. The constructor of ProfileAccelerationConstraint now accepts
two values, a minimum (negative) acceleration and a maximum (positive)
acceleration.

- 
Trajectories can be canceled smoothly. A canceled trajectory brings
the robot to a stop as soon as possible while remaining on the path and
obeying the mandated constraints. See Trajectory#cancel().

- 
Unit-adjusted Ramsete in the quickstart by default. The old tank PIDVA
follower is no longer in either the quickstart or the core library. Ramsete is
ubiquitous in FRC and performs much better than its predecessor. The
defaults from
WPILib
have been incorporated, so you may not even need to tune regardless of your
units.