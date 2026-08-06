> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-3d · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

3D AprilTags | Limelight Documentation

 Skip to main content

 On this page

# 3D AprilTags

There are three levels of 3D AprilTag tracking in Limelight OS:

- Point of interest tracking (Easy to use, requires zero code changes, compatible with "tx" and "ty")

- Full 3D Tracking

- Robot Localization

## Point-of-Interest Tracking​

Point-of-Interest tracking allows you to define a 3D point of interest relative to an AprilTag.

Let's say you are trying to target a field feature that is 6 inches to the left and 2 inches behind an AprilTag. You can simply define that point of interest
in the web interface (in meters), and then track this 3D point using tx and ty as if it existed as a real-world target.

## Full 3D Tracking​

In the "visualizer" section of the "Advanced" tab,
you will find several visualizers that will help you understand the purpose of each of the available transforms. In general,
the most useful transforms will be "Camera Transform in Target Space", "Robot Transform in Target Space", and "Robot Transform in Field Space". See the coordinate system doc for more details.

Note the limelight pose (robotspace) adjustments in this demonstration:

- Point-of-Interest Tracking
- Full 3D Tracking