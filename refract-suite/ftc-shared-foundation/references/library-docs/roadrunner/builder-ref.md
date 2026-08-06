> Source: https://rr.brott.dev/docs/v1-0/builder-ref/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Builder Reference | Road Runner Docs

# 
 Builder Reference
 #

## 
 Path Primitives
 #

The begin pose is the origin with a heading of 

 \( \frac{\pi}{6} \)

.

### 
 lineToX()
 #

.lineToX(48)

### 
 lineToY()
 #

.lineToY(36)

### 
 splineTo()
 #

.splineTo(new Vector2d(48, 48), Math.PI / 2)

## 
 Heading Primitives
 #

The begin pose is the origin with a heading of 
 \( \frac{\pi}{2} \)

.

### 
 Tangent Heading (default)
 #

.setTangent(0)
.splineTo(new Vector2d(48, 48), Math.PI / 2)

### 
 Constant Heading
 #

.setTangent(0)
.splineToConstantHeading(Vector2d(48, 48), Math.PI / 2)

### 
 Linear Heading
 #

.setTangent(0)
.splineToLinearHeading(Pose2d(48, 48, 0), Math.PI / 2)

### 
 Spline Heading
 #

.setTangent(0)
.splineToSplineHeading(Pose2d(48, 48, 0), Math.PI / 2)