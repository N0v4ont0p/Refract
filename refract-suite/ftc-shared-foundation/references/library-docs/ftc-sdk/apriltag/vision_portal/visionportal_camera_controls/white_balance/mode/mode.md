> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/white_balance/mode/mode.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

White Balance Control Mode
--------------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode`

This interface supports 3 values of WhiteBalanceControl.Mode:

-  AUTO
-  MANUAL
-  UNKNOWN

To directly control the color balance temperature, set the webcam to
Manual mode. Mode is managed with these WhiteBalanceControl methods:

-  setMode(WhiteBalanceControl.Mode.MODE)
-  getMode()

The Logitech C920 defaults to Auto mode for white balance control, and
even reverts to Auto in a fresh session, after being set to Manual in a
previous session. For other CameraControl settings, some webcams revert
to a default value and some preserve their last commanded value.