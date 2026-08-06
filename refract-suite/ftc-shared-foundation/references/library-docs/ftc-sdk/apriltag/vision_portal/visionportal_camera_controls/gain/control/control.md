> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/gain/control/control.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Gain Control
------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls`

Gain is a digital camera setting that controls the amplification of the
signal from the webcam sensor. This amplifies the whole signal,
including any associated background noise.

Gain **must** be managed together with exposure. Autoexposure mode manages
both, so gain can be adjusted only if ExposureControl Mode is set to
``Manual`` (not the default).

Raising exposure and keeping gain low, can provide a bright image and low
noise. On the other
hand, longer exposure can cause motion blur, which may affect target
tracking performance. In some cases, reducing exposure duration and
increasing gain may provide a sharper image, although with more noise.

The interface GainControl uses a single value to control gain. It’s
used for amplification, and thus has no units – it’s just a number of
type integer. Its methods are: 

- setGain(int gain) 
- getGain()

As with exposure, the webcam may support minimum and maximum allowed
values of gain. These can be retrieved with: 

- getMinGain() 
- getMaxGain()

There are no ``set()`` methods for min and max gain; these are
hard-coded in the webcam’s firmware. Note that firmware settings may
vary among different versions of the same webcam model.

These and other gain methods are called on a GainControl object, as
described above for exposure.