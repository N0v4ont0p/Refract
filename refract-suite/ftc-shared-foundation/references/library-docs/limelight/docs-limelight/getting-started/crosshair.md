> Source: https://docs.limelightvision.io/docs/docs-limelight/getting-started/crosshair · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Crosshair Calibration | Limelight Documentation

 Skip to main content

 On this page

# Crosshair Calibration

Limelight’s crosshairs simplify offset calibration. Rather than storing angular offsets in code, you can align your robot to a target, and click "calibrate".

Calibrating a crosshair moves the “zero” of your targeting data. This is very useful if your Limelight isn’t perfectly centered on your robot.

## Single Crosshair Mode​

Line-up your robot at its ideal scoring location+rotation, and click “calibrate”. Now a tx and ty of “zero” equate to a perfectly aligned robot. If your robot needs to be recalibrated for a new field, simply take a practice match to find the perfect alignment for your robot, and click “calibrate” during your match.

## Dual Crosshair Mode​

Imagine a robot with an off-axis camera or shooter that needs to shoot gameobjects into a goal from many positions on the field. As the robot approaches the goal, its crosshair must adjust in real-time to compensate. Dual crosshair mode is built for this functionality. Line-up your robot at its closest scoring position+rotation, and calibrate crosshair “A”. Line-up your robot at its farthest scoring position+rotation, and calibrate crosshair “B”. When you calibrate in dual-crosshair mode, crosshairs also store an area value. You will notice that as your robot moves between its min and max scoring distances, the crosshair moves between crosshair “A” and crosshair “B”. This is done by checking the area of the target, and comparing it to the two target areas seen during calibration.

- Single Crosshair Mode
- Dual Crosshair Mode