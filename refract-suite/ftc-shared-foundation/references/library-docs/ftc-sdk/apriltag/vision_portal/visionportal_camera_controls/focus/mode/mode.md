> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/focus/mode/mode.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Focus Control Mode
------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode`

A webcam may operate in one of various focus modes. To directly control
the focus length, set the webcam to Fixed mode.

The SDK supports these values of FocusControl.Mode: 

-  `Auto` 
-  `ContinuousAuto` 
-  `Fixed` 
-  `Infinity` 
-  `Macro` 
-  `Unknown`

Mode is managed with these FocusControl methods: 

-  setMode(ExposureControl.Mode._mode_) 
-  getMode()

The Logitech C920 webcam offers two modes: ContinuousAuto and Fixed,
which does respond to FocusControl methods. The Logitech C270 (older
model) offers only Fixed mode, but does not allow programmed control.

Full details are described in the `FocusControl
Javadoc <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/hardware/camera/controls/FocusControl.html>`__.