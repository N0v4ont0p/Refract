> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-coordinate-systems · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

3D Coordinate Systems In Detail | Limelight Documentation

 Skip to main content

 On this page

# 3D Coordinate Systems In Detail

## Limelight Camera Space​

3d Cartesian Coordinate System with (0,0,0) at the camera lens.

X+ → Pointing to the right (if you were to embody the camera)

Y+ → Pointing downward

Z+ → Pointing out of the camera

## Target Space​

3d Cartesian Coordinate System with (0,0,0) at the center of the target.

X+ → Pointing to the right of the target (If you are looking at the target)

Y+ → Pointing downward

Z+ → Pointing out of the target (orthogonal to target's plane).

## Robot Space​

3d Cartesian Coordinate System with (0,0,0) located at the center of the robot’s frame projected down to the floor.

X+ → Pointing forward (Forward Vector)

Y+ → Pointing toward the robot’s right (Right Vector)

Z+ → Pointing upward (Up Vector)

## Field Space (FTC)​

3d Cartesian Coordinate System with (0,0,0) located at the center of the field

## Field Space (FTC Diamond)​

3d Cartesian Coordinate System with (0,0,0) located at the center of the field

## Field Space (FRC) (Used by map generator)​

3d Cartesian Coordinate System with (0,0,0) located at the center of the field

X+ → Points along the long side of the field

Y+ → Points up the short side of the field

Z+ → Points towards the sky

Right-handed. Positive theta results in counterclockwise rotation from positive outside perspective

## Field Space (FRC WPIBlue) (Preferred Field Space for all FRC Teams)​

Just like the standard FRC coordinate system, but with (0,0,0) at the blue-alliance origin.

## Field Space (FRC WPIRed) (Do not use this)​

Just like the standard FRC coordinate system, but with (0,0,0) at the red-alliance origin and rotated 180 degrees.

- Limelight Camera Space
- Target Space
- Robot Space
- Field Space (FTC)
- Field Space (FTC Diamond)
- Field Space (FRC) (Used by map generator)
- Field Space (FRC WPIBlue) (Preferred Field Space for all FRC Teams)
- Field Space (FRC WPIRed) (Do not use this)