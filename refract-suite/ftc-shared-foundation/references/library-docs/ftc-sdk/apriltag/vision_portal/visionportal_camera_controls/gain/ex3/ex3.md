> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/gain/ex3/ex3.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Example 3: An odd preview
-------------------------

.. figure:: images/400-Duck-in-Dark.png
   :align: center

   Was this recognition really made in the dark?


How can this be? Answer: this image was not an ‘instant’ result.
Exposure was reduced very low, **after** the object had been recognized.

Vision processors can be much better at **tracking** a currently-identified
object through translation, rotation, partial blockage, and even extreme
changes in exposure, than at making that first recognition. A preview that
looks far too dark to work with may still be good enough to hold a lock the
processor already has.