> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/exposure/auto_exposure/auto-exposure.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

AE Priority
=============

Auto-Exposure Priority is a setting within the ExposureControl
interface. It’s listed here at the end, not likely to be needed in 
since it it operates in very low lighting.

What does it do? Imagine that the webcam is operating at its default
frame rate, for example 30 frames per second (fps). *Note that frame
rate is not covered in this basic tutorial.*

If the webcam’s built-in auto-exposure detects that the image is very
dark, AE Priority **allows the frame rate to decrease**. This slowdown,
or ‘undershoot’, allows more light per frame, which can ‘brighten’ the
image.

Its methods are: 

-  setAePriority(boolean priority) 
-  getAePriority()

These AE Priority methods are called on an ExposureControl object, as
described above.

.. figure:: images/500-AE-Priority.png
   :align: center

   Two examples of AE Priority


Here are two pairs of previews, each with AE Priority off and on. In
both pairs, the ambient light level is very low. These results are from
a Logitech C270 webcam.

The Exposure=0 recognition here was made before reducing exposure and
gain. When testing ‘instant’ results, AE Priority could improve the
chance of recognition.

Again, this effect is triggered only in very low lighting, not expected in
competition. If the building loses all power, Duck recognition becomes… less
essential.