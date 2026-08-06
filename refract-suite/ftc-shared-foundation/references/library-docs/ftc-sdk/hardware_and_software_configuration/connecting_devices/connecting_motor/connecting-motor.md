> Source: https://github.com/FIRST-Tech-Challenge/ftcdocs/blob/372e6b4150be6b69a687e737e7b345eaa65112e6/docs/source/hardware_and_software_configuration/connecting_devices/connecting_motor/connecting-motor.rst · Fetched: 2026-08-06 · Ref: main @ 372e6b4150be · Original format: rst, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

Connecting a Motor to the Hub
==============================

The Hub can drive up to four (4) 12V DC motors per Hub. The Hub uses a
type of electrical connector known as a 2-pin JST VH connector. Many of
the *FIRST* approved 12V DC motors are equipped with Anderson Powerpole
connectors. An adapter cable can be used to connect the Anderson
Powerpole connectors to the Hub motor port (see the
:doc:`Robot Wiring Guide </robot_building/wiring_guide/wiring-guide>`
for more information).

.. image:: images/MotorRig.jpg
   :align: center
   :alt: Simple test rig with motor mounted to some Tetrix channel

|

For the examples in this tutorial, *FIRST* recommends that the user build a
simple rig to secure the motor in place and prevent it from moving about
during the test runs. The image above shows a Tetrix motor installed in
a rig built with a Tetrix motor mount and some Tetrix C-channels. A gear
was mounted on the motor shaft to make it easier for the user to see the
rotation of the shaft.

Note that it will take an estimated 2.5 minutes to complete this task.


Connecting a 12V Motor to the Hub Instructions
----------------------------------------------

1. Connect the Anderson Powerpole end of the motor's power cable to   
the Powerpole end of the Anderson to JST VH adapter cable.            

.. image:: images/ConnectingMotorStep1.jpg
   :align: center
   :alt: Connecting the adapter cable

|

.. note:: Motors from different vendors can have different cabling requirements.
   Adjust this as needed for your motor.
   One end needs to be a JST VH two pin connector (white).

2. Connect the JST VH white connector into the motor port labeled "0" on the Hub.                                

.. image:: images/ConnectingMotorStep2.jpg
   :align: center
   :alt: Shows the JST VH white connector of the cable plugged into the Control Hub

|
