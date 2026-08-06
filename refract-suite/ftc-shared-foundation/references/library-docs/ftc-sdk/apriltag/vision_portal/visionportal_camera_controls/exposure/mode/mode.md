> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/exposure/mode/mode.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Exposure Control Mode
---------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls`


A webcam may operate in one of various exposure modes.

Many common webcams offer only some of these modes. To directly
control the exposure, set the webcam to Manual mode.

The SDK supports these values of ExposureControl.Mode: 

- `AperturePriority`
- `Auto` 
- `ContinuousAuto`
- `Manual` 
- `ShutterPriority` 
- `Unknown`

Mode is managed with these ExposureControl methods: 

- setMode(ExposureControl.Mode._mode_) 
- getMode()

The Logitech C920 and C270 models offer two exposure modes:
AperturePriority and Manual.