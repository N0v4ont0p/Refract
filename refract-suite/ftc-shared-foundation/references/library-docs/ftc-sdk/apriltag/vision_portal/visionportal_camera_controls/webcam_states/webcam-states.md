> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/webcam_states/webcam-states.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Webcam States
-------------

Camera controls cannot be used until the webcam has reached the state
``CAMERA_DEVICE_READY``.

The VisionPortal reports these camera states:

- OPENING_CAMERA_DEVICE
- CAMERA_DEVICE_READY
- STARTING_STREAM
- STREAMING
- STOPPING_STREAM
- CLOSING_CAMERA_DEVICE
- CAMERA_DEVICE_CLOSED
- ERROR

These **enums** are listed in sequence, as if opening a camera (fresh
build), then starting or resuming streaming, then stopping streaming,
then closing the camera.

Notes and Guidelines for Enums
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``OPENING_CAMERA_DEVICE`` - no vision processing is happening

- ``CAMERA_DEVICE_READY`` - Camera is open. No processing is happening,
  including background processing from EOCV (i.e. pulling frames and
  performing color conversion). Ready to call ``resumeStreaming()``

- ``STARTING_STREAM`` - no processing is happening

- ``STREAMING`` - Frames are available for processing (AprilTag detections
  and/or Color Processing results) and preview (RC preview and DS Camera Stream)

- ``STOPPING_STREAM`` - processing may or may not be happening. This
  status is followed by ``CAMERA_DEVICE_READY``.

- ``CLOSING_CAMERA_DEVICE`` - no processing is happening

- ``CAMERA_DEVICE_CLOSED`` - nothing is running, USB comms are closed.
  Once closed, don't open camera again during this OpMode.
