> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-retro/contour-filtering-and-sorting · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Contour Filtering and Sorting | Limelight Documentation

 Skip to main content

 On this page

# Contour Filtering and Sorting

After color thresholding, Limelight generates a list of contours. After that, each contour is wrapped in a tightest-fit bounding rectangle, an "unrotated" rectangle, and a "convex hull". These are passed through a series of filters to determine the "best" contour. If multiple contours pass through all filters, Limelight chooses the best contour using the "Sort Mode" Control.

### Sort Modes​

Controls how contours are sorted after they are passed through all other filters.

In 2019, the "closest" sort mode was added. This mode will select the target that is closest to the configurable crosshair.

### Target Area​

Controls the range of acceptable bounding-rectangle areas, as percentages of the screen. You can increase the minimum area to help filter-out stadium lights, and decrease the maximum value to help filter-out things like large displays near the field.

The area slider is not linearly scaled, but quarticly scaled. This is done to provide extra precision near the lower-end of area values, where many FRC targets lie. The area of a square scales quadratically with its side length, but x^4 scaling provides even greater precision where it is needed.

### Target Fullness​

Fullness is the percentage of "on" pixels in the chosen contour's bounding rectangle. A solid rectangle target will have a near-1.0 fullness, while a U-shaped target will have a low fullness.

### Target Aspect Ratio​

Aspect ratio is defined by the width of the bounding rectangle of the chosen contour divided by its height. A low aspect ratio describes a "tall" rectangle, while a high aspect ratio describes a "wide" rectangle.

The aspect ratio slider is also quadratically scaled.

### Direction Filter​

Rejects contours on the basis of their orientation.

### Smart Speckle Rejection​

Rejects relatively small (as opposed to absolutely small w/ the area filter) contours that have passed through all other filters. This is essential if a target must remain trackable from short-range and long-range.
This feature was introduced in the 2019 season to reject Limelight's LED reflections when robots were very close to targets.

### Target Grouping​

Controls target "grouping". Set to dual mode to look for "targets" that consist of two shapes, or tri mode to look for targets that consist of three shapes.

Smart Target Grouping can group a variable number of targets and reject outliers. It was added in 2022 to help track the upper hub target.

### Intersection Filter (Dual Targets Only)​

Rejects groups of contours based on how they would intersect if extended to infinity.

### Smart Target Grouping​

Automatically group targets that pass all individual target filters.

- Will dynamically group any number of targets between -group size slider minimum- and -group size slider maximum-

### Outlier Rejection​

- While group targets are more challenging than normal targets, they provide more information and opportunities for filtering. If you know that a goal is comprised of multiple targets that are close to each other, you can actually reject outlier targets that stand on their own.

- You should rely almost entirely on good target filtering, and only use outlier rejection if you see or expect spurious outliers in your camera stream. If you have poor standard target filtering, outlier detection could begin to work against you!

## Output​

This tab controls what happens during the last stage of the vision pipeline

### Targeting Region​

Controls the point of interest of the chosen contour's bounding rectangle. By default, the tracking parameters tx and ty represent the offsets from your crosshair to the center of the chosen rectangle. You can use another option if a target changes in size, or is comprised of two targets that sometimes blend together.

### Send Raw Corners?​

Set this control to "yes" to include corner locations in JSON, NetworkTables, and API results. Tune the number of corners submitted by adjusting the "Contour Simplification" value in the "Contour Filtering" page.

### Send JSON over NT?​

Set this control to "yes" to submit JSON over NetworkTables.

### Crosshair Calibration​

Controls the "origin" of your targeting values. Let's say a shooter on your robot needs to be calibrated such that it always points a bit left-of-center. You can line up your robot, click "calibrate," and all of your targeting values will be sent relative to your new crosshair. See the calibration page for more details!

## 3D​

Experiment with PnP point-based pose estimation here.

### Compute 3D​

Controls whether pose estimation is enabled. You must enable the 960x720 high-res mode for this to work.

### Force Convex​

Use this option to select only the "outermost" corners of a target for SolvePnP.

### Contour Simplification​

Use this option to remove small, noisy edges from the target.

### Acceptable Error​

Limelight will only return a target if it passes a reprojection test with a certain score in pixels.

### Goal Z-Offset​

Automatically the 3D Depth value of your target (Z-Axis).

- Sort Modes
- Target Area
- Target Fullness
- Target Aspect Ratio
- Direction Filter
- Smart Speckle Rejection
- Target Grouping
- Intersection Filter (Dual Targets Only)
- Smart Target Grouping
- Outlier Rejection
- Output- Targeting Region
- Send Raw Corners?
- Send JSON over NT?
- Crosshair Calibration

- 3D- Compute 3D
- Force Convex
- Contour Simplification
- Acceptable Error
- Goal Z-Offset