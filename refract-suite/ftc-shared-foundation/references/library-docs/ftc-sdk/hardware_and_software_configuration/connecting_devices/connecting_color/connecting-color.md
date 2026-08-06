> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/hardware_and_software_configuration/connecting_devices/connecting_color/connecting-color.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Connecting a Color-Distance Sensor to the Hub
=============================================

The Hub has 4 independent I2C buses. Each bus has its own port on the
Hub. We will connect a REV Robotics Color-Distance sensor to the I2C bus
#0 on the Hub.

Note that it will take an estimated 2.5 minutes to complete this task.


Connecting a Color-Distance Sensor to the Hub Instructions
----------------------------------------------------------

1. Connect one end of the 4-pin JST PH cable to the REV Robotics  
Color-Distance sensor.                                                

.. image:: images/ColorSensorStep1.jpg
   :align: center

|

2. Plug the other end of the 4-pin JST PH cable to the I2C port       
labeled "0" on the Hub.                                               

.. image:: images/ColorSensorStep2.jpg
   :align: center

|