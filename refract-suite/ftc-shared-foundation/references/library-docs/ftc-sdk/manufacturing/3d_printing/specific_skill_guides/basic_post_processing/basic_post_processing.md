> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/manufacturing/3d_printing/specific_skill_guides/basic_post_processing/basic_post_processing.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Basic Post-Processing
=====================

Support Removal
---------------

Support material removal is a basic form of post processing where, as the name suggests, you remove support material from your print.
This can typically be done easily with either just your fingers or a pair of pliers/flush cutters, however, sometimes removing
support from small features or holes can be difficult. This is why it's recommended to design away from using supports, and if
you must use them, to set up your slicing settings properly in order to make them easy to remove.

.. image:: images/supportremoval.png
  :align: center
  :width: 55%
  :alt: The process of support removal.

|

Drilling Out Holes
------------------

Drilling out printed holes are typically used in order to widen screw holes to achieve a loose fit. This can be done with any
drill and properly sized drill bit, however take your time while drilling to ensure that the drill bit is lined up properly to
guarantee that drilled holes are straight.

Brim Removal
------------

Brims are used to have more surface area for your print to contact the build plate. To remove them, you typically just use your
fingers, however, if your Z-Offset is too low, it may be easier to use a deburring tool to remove the inner layer lines of the brim.