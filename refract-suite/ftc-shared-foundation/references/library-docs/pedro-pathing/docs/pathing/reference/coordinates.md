> SEASON SCOPE (added by Refract, 2026-09-13): the field images labelled "Decode" and the paragraph
> converting FTC coordinates "for the Decode game" via `InvertedFTCCoordinates` ("inverted for
> decode") below are DECODE (2025-26)-specific. Pedro's own coordinate system (0-144, CCW-positive
> heading) is generic. It does not describe BIOBUZZ (2026-27). For BIOBUZZ facts read
> `ftc-shared-foundation/season-extensions/biobuzz-2026-27.yaml`. No BIOBUZZ field-axis definition has
> been published on ftc-docs as of 2026-09-13; the BIOBUZZ manual (§9.5) only says the red ALLIANCE
> AREA is on the left from the audience. Do not infer BIOBUZZ axes or pick a coordinate conversion
> from the DECODE material.

> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/coordinates.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Coordinates
---

Pedro Pathing uses a right-hand coordinate system, which is nonstandard to the FTC SDK Standard.

<img
  className="inline-block dark:hidden"
  src="/docs/fieldcoordinates-light.png"
  alt="Pedro Pathing Decode FTC Coordinate System"
/>

<img
  className="hidden dark:inline-block"
  src="/docs/fieldcoordinates-dark.png"
  alt="Pedro Pathing Decode FTC Coordinate System"
/>

As shown, as a robot moves to the right in the image below, x increases. As a robot moves up on the field image, y increases.  

A robot facing towards the right side of the image is at a heading of 0 radians (0 degrees), facing up is $\frac{\pi}{2}$ radians (90 degrees), facing left is $\pi$ radians (180 degrees), and facing down is $\frac{3\pi}{2}$ radians (270 degrees).
Thus, counterclockwise rotation is positive rotation, similar to a unit circle.

To convert FTC Coordinates for the Decode game into Pedro's coordinates, first declare a Pose in FTC coordinates (inverted for decode). Let's say you have Pose2D (a class in the FTC SDK) `ftcPose2d` with your coordinates from a camera. You can use 
`Pose ftcStandard = PoseConverter.pose2DToPose(ftcPose2d, InvertedFTCCoordinates.INSTANCE);` to convert this to Pedro's `Pose` class. Then, you need to convert to Pedro coordinates using 
`ftcStandard.getAsCoordinateSystem(PedroCoordinates.INSTANCE);`

