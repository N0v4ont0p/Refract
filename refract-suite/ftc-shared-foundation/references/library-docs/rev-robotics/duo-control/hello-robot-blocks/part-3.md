> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3.md).

# Part 3: Autonomous and Encoders

We've tackled the basics. We have a robot able to drive around. What could be next?&#x20;

Right now our robot is largely dependent on inputs from us as the driver from the gamepad. We've helped it learn to sense a little bit using the touch sensor, but there is still more we can do.&#x20;

During **Part 3** we will be learning how to help our robot navigate the world around it autonomously in different ways. To start we will look at how to use a timer for the robot to keep track of how long it should do something. From there, we will move on to using the built in encoders of the HD Hex and Core Hex Motors.&#x20;

Encoders are a form of sensor that help collect data for the motor. Some encoders count the number of completed rotations. Others are able to track the exact position of a motor, similar to a servo. The use of encoders brings the need for more math and complex programming, however it will allow your robot to navigate more efficiently.&#x20;

## Quick Links

|                                                        ElapsedTime                                                        |                                                                          Drivetrain Encoders                                                                          |                                                                          Arm Encoders                                                                         |
| :-----------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                             [Overview](/duo-control/hello-robot-blocks/part-3/elapsed-time.md)                            |                                           [Overview](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks.md)                                          |                                     [Overview](/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks.md)                                    |
|               [ElapsedTime Set Up](/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-setup.md)              |        [Converting Encoder Ticks to a Distance](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/converting-encoder-ticks-to-a-distance.md)        |      [Estimating the Position of the Arm](/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/estimating-the-position-of-the-arm.md)      |
|               [ElapsedTime Logic](/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-logic.md)               |                   [Moving to a Target Distance](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/moving-to-a-target-distance.md)                   |             [Calculating Target Position](/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/calculating-target-position.md)             |
| [ElapsedTime - Multiple Movements](/duo-control/hello-robot-blocks/part-3/elapsed-time/elapsedtime-multiple-movements.md) |                              [Setting Velocity](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/setting-velocity.md)                              | [Using Limits to Control Range of Motion](/duo-control/hello-robot-blocks/part-3/arm-control-with-encoders-blocks/using-limits-to-control-range-of-motion.md) |
|                                                                                                                           | [Turning the Drivetrain Using RUN\_TO\_POSITION](/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/turning-the-drivetrain-using-run_to_position.md) |                                                                                                                                                               |
