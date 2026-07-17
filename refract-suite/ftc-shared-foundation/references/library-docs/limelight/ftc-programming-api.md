> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/ftc-programming · Fetched: 2026-07-17
> Completeness-audit addition: this is the single FTC-specific Java/Blockly programming page in
> Limelight's docs — absent from this corpus before this pass, not stale, never fetched. The
> broader completeness sweep found ~48 real pages in Limelight's docs sitemap total (getting-started
> per hardware model, other API references, pipeline-specific pages, tutorials, changelogs); this
> page was the single highest-value gap given Refract's actual scope (FTC Java code generation).
> The rest remain a known, lower-priority gap — logged, not silently dropped.

# FTC Java & Blockly Programming Guide for Limelight

## Setup

Import the needed classes and configure the `Limelight3A` in `init()`: set a poll rate (e.g.
100 Hz) and call `start()` to begin vision processing.

## Pipelines

Swap between up to 10 pre-configured pipelines with `pipelineSwitch()` — completes within
milliseconds, does not block the OpMode loop.

## Reading results

Results come through an `LLResult` object. Always validate before use:

```java
if (result != null && result.isValid()) { ... }
```

Basic targeting data: `getTx()`, `getTy()`, `getTa()`.

**Specialized result types**, depending on the active pipeline: color (position + area of a
colored target), fiducial/AprilTag (marker ID + relative pose), barcode (QR/barcode decode),
classifier (neural-net classification), detector (object location + confidence).

## Localization

- **MegaTag 1**: robot position from AprilTag detection alone.
- **MegaTag 2**: MegaTag 1 fused with IMU orientation data, for higher accuracy.

Both require "Full 3D" mode enabled and the camera calibrated relative to the robot's own center —
an uncalibrated offset feeds a wrong pose silently, not an error.

## Utility

- `getStaleness()` — check result-timestamp freshness before trusting a value.
- Snapshot capture during autonomous, for offline pipeline tuning/analysis after a run.
- Python integration: `updatePythonInputs()`/`getPythonOutputs()` for bidirectional communication
  with a custom SnapScript pipeline.

## Further reference

[Javadoc](https://javadoc.io/doc/org.firstinspires.ftc/Hardware/latest/com/qualcomm/hardware/limelightvision/package-summary.html) ·
[Official FTC examples](https://github.com/LimelightVision/limelight-examples)
