> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/apriltag/vision_portal/visionportal_camera_controls/ptz/zoom/zoom.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Zoom
====

Virtual zoom is described with a single dimensionless value of type
integer. Similar to the interfaces described above, virtual zoom can be
managed with these methods: 

-  setZoom(int zoom) 
-  getZoom() 
-  getMinZoom() 
-  getMaxZoom()

The Logitech C920 allows zoom values ranging from 100 to 500, although
values higher than 250-280 have no further effect on the preview image.

These zoom methods are called on a PtzControl object, as described above
for exposure.