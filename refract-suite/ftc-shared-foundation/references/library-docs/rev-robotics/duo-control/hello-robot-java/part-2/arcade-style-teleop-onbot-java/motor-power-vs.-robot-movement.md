> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java/motor-power-vs.-robot-movement.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arcade-style-teleop-onbot-java/motor-power-vs.-robot-movement.md).

# Motor Power vs. Robot Movement

At the moment, our motors are set to power on to a full forward at the start of our program. For reference, the image below shows the full scale of movement between forward and reverse:

<figure><img src="/files/CLdzRzt6L2wxXFQIwDzn" alt=""><figcaption></figcaption></figure>

Let's take this information and think back to when we first[ programmed a motor](/duo-control/hello-robot-blocks/part-1/programming-motors/programming-a-motor-with-a-gamepad.md) to move with our gamepad. During that section our motor was able to rotate at different power levels depending on how far and in which direction our joystick moved. However, do you recall the problem we had with this set up?

While using our previous code our motor only spun when the joystick was moved along the y-axis. Moving to the left or right did not ask the motor to power on, but it would begin to stutter some at the diagonals.&#x20;

This is where adding some math to our code comes into play. Remember on an arcade drive both motors are being controlled by a single joystick. We need our robot to be able to calculate for both motors how much they should power on and in which direction. Thankfully, once we have it all set up our robot will be able to handle the calculations itself as the program runs!

By the end, we should be able to create situations like the following charts where the motors respond to create different forms of motion:

<figure><img src="/files/AHyebx9FYvG4LuAQzBoQ" alt=""><figcaption></figcaption></figure>

### Quick Check!

How our robot moves is dependent on how much power each motor is receiving. Before continuing, we can explore with our current program how the robot reacts when changing the values assigned to our motors.

* What happens when we set the power of the rightmotor to 0.3 and leftmotor to 1?
* What happens when we set the power of the leftmotor to 0.5 and rightmotor to 1?
* What happens when we set the power of the leftmotor to -0.4 and rightmotor to 0.4?

After testing different combinations, let's look at a quick breakdown of how power between the motors effects movement:

| Power Comparison                   | Robot Movement              |
| ---------------------------------- | --------------------------- |
| rightMotor power = leftMotor power | Straight Forward or Reverse |
| rightMotor power > leftMotor power | Left Turn                   |
| rightMotor power < leftMotor power | Right Turn                  |

### Determining Power with the Joysticks

Rather than setting a static numerical value for our motors, the variables we've set will help our robot to translate the motion of the joysticks into a power level. &#x20;

For our arcade drive, the goal is for our joystick inputs to calculate to the following motor outputs:

<table data-header-hidden><thead><tr><th width="223">Joystick Direction</th><th>(  ,  )</th><th width="124">rightmotor</th><th>leftmotor</th><th></th></tr></thead><tbody><tr><td>Joystick Direction</td><td>( <span class="math">x</span> , <span class="math">y</span> )</td><td>rightmotor</td><td>leftmotor</td><td>Movement</td></tr><tr><td><img src="/files/-Mefhx7EWkkmadU6LW8V" alt="" data-size="original"></td><td>(0,1)</td><td>1</td><td>1</td><td>Forward</td></tr><tr><td><img src="/files/-MefhzwimOC2m68IoDSE" alt="" data-size="original"> </td><td>(0,-1)</td><td>-1</td><td>-1</td><td>Reverse</td></tr><tr><td><img src="/files/-Mefi1rcj_EIfo6ZRW2u" alt="" data-size="original"> </td><td>(-1,0)</td><td>1</td><td>-1</td><td>Turn left</td></tr><tr><td><img src="/files/-Mefi4IQJxLAupAhBq8Y" alt="" data-size="original"> </td><td>(1,0)</td><td>-1</td><td>1</td><td>Turn right</td></tr></tbody></table>

To get the outputs expressed in the table above, the gamepad values must be assigned to each motor in a meaningful way. To do so we are going to set up two equations in our code using the variables we have already established:

$$
rightmotor = y-x \\
leftmotor = y+x
$$
