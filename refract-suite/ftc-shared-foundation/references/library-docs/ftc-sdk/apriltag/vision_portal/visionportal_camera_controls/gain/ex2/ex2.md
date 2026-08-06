> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/gain/ex2/ex2.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Example 2: Gain’s effect on recognition
---------------------------------------

Now we adjust only gain. We set Exposure to a fixed value of 15,
selected because it was a poor performer in Example 1. **Can gain
help?**

.. figure:: images/300-Exp15Gain000-to-035.png
   :align: center

   Exp 15, Gain 000 -> 035

.. figure:: images/310-Exp15Gain040-to-060.png
   :align: center

   Exp 15, Gain 040 -> 060

.. figure:: images/330-Exp15Gain070-to-100.png
   :align: center

   Exp 15, Gain 070 -> 100


Five fresh readings were taken at each gain setting.

.. figure:: images/350-chart-exposure=15.png
   :align: center

   Five readings at each gain level

Higher gain does improve recognition, then performance declines. Then at
higher levels, the processor begins to “see” the wrong object entirely. The
gain effect was similar to the exposure effect.

These two charts suggest that vision processing results are affected by, and
can perhaps be optimized by, setting specific values for exposure and gain.
A team should compare this with the default or automatic performance of
their robot and webcam, in the full range of expected match conditions.