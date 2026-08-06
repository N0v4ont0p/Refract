> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltag-map-specification · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

AprilTag Map Specification | Limelight Documentation

 Skip to main content

# AprilTag Map Specification

Limelight's field-space localization feature uses .fmap files to compute a robot pose for use by WPILIB's pose estimators.
Our fmap files support maps comprised of different target sizes and different families.

You can use fmaps to define "environments" such as FRC fields, or "objects" such as objects that have several attached AprilTags.
To use an fmap, all you need to do is upload it to your Limelight using the interface or the REST upload API

The .fmap file is a JSON file containing a single "fiducial" array.
Each entry in the fiducial array has the following structure:

familyAprilTag/Fiducial family
idTag ID
sizeTag size in mm
transform4x4 Matrix Transform of the target. Row-Major, SI units.
uniqueSpecifies whether the target is unique in this map or featured multiple times

In addition, the top-level object has a "type" string specifiying the map type.

typeField type e.g. frc, ftc, ftcd (ftc diamond)

AprilTag Map for FRC 2024 Crescendo - Credit to Kevin Hjelstrom{
 "type": "frc",
 "fiducials": [
 {
 "family": "apriltag3_36h11_classic",
 "id": 1,
 "size": 165.1,
 "transform": [
 -0.5,
 -0.866025,
 0,
 6.808597,
 0.866025,
 -0.5,
 0,
 -3.859403,
 0,
 0,
 1,
 1.355852,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 2,
 "size": 165.1,
 "transform": [
 -0.5,
 -0.866025,
 0,
 7.914259,
 0.866025,
 -0.5,
 0,
 -3.221609,
 0,
 0,
 1,
 1.355852,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 3,
 "size": 165.1,
 "transform": [
 -1.0,
 0,
 0,
 8.308467,
 0,
 -1.0,
 0,
 0.877443,
 0,
 0,
 1,
 1.451102,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 4,
 "size": 165.1,
 "transform": [
 -1.0,
 0,
 0,
 8.308467,
 0,
 -1.0,
 0,
 1.442593,
 0,
 0,
 1,
 1.451102,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 5,
 "size": 165.1,
 "transform": [
 0,
 1.0,
 0,
 6.429883,
 -1.0,
 0,
 0,
 4.098925,
 0,
 0,
 1,
 1.355852,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 6,
 "size": 165.1,
 "transform": [
 0,
 1.0,
 0,
 -6.429375,
 -1.0,
 0,
 0,
 4.098925,
 0,
 0,
 1,
 1.355852,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 7,
 "size": 165.1,
 "transform": [
 1.0,
 -0.0,
 0,
 -8.308975,
 0.0,
 1.0,
 0,
 1.442593,
 0,
 0,
 1,
 1.451102,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 8,
 "size": 165.1,
 "transform": [
 1.0,
 -0.0,
 0,
 -8.308975,
 0.0,
 1.0,
 0,
 0.877443,
 0,
 0,
 1,
 1.451102,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 9,
 "size": 165.1,
 "transform": [
 0.5,
 -0.866025,
 0,
 -7.914767,
 0.866025,
 0.5,
 0,
 -3.221609,
 0,
 0,
 1,
 1.355852,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 10,
 "size": 165.1,
 "transform": [
 0.5,
 -0.866025,
 0,
 -6.809359,
 0.866025,
 0.5,
 0,
 -3.859403,
 0,
 0,
 1,
 1.355852,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 11,
 "size": 165.1,
 "transform": [
 0.5,
 0.8660254,
 0,
 3.633851,
 -0.8660254,
 0.5,
 0,
 -0.392049,
 0,
 0,
 1,
 1.3208,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 12,
 "size": 165.1,
 "transform": [
 0.5,
 -0.866025,
 0,
 3.633851,
 0.866025,
 0.5,
 0,
 0.393065,
 0,
 0,
 1,
 1.3208,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 13,
 "size": 165.1,
 "transform": [
 -1.0,
 0,
 0,
 2.949321,
 0,
 -1.0,
 0,
 -0.000127,
 0,
 0,
 1,
 1.3208,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 14,
 "size": 165.1,
 "transform": [
 1.0,
 -0.0,
 0,
 -2.950083,
 0.0,
 1.0,
 0,
 -0.000127,
 0,
 0,
 1,
 1.3208,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 15,
 "size": 165.1,
 "transform": [
 -0.5,
 -0.866025,
 0,
 -3.629533,
 0.866025,
 -0.5,
 0,
 0.393065,
 0,
 0,
 1,
 1.3208,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 },
 {
 "family": "apriltag3_36h11_classic",
 "id": 16,
 "size": 165.1,
 "transform": [
 -0.5,
 0.866025,
 0,
 -3.629533,
 -0.866025,
 -0.5,
 0,
 -0.392049,
 0,
 0,
 1,
 1.3208,
 0,
 0,
 0,
 1
 ],
 "unique": 1
 }
 ]
}