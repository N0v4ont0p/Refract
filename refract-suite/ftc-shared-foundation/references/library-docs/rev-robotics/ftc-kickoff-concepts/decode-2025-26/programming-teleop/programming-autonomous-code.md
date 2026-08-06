> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-code.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-code.md).

# Programming - Autonomous Code

Once our OpMode is selected, we're ready to actually hit play and let the robot run! For this example, the [TeleOp portion of the code ](/ftc-kickoff-concepts/decode-2025-26/programming-teleop.md)has remained the same so we won't repeat looking at it here.&#x20;

Instead let's break down our autonomous code options. For both Blue and Red Alliance versions of the code, the robot is intended to start against the goal while touching the launch line. It will automatically fire the pre-loaded balls for 10 seconds before backing up from the goal, turning, and driving straight back off the line.&#x20;

<figure><img src="/files/ZeR0EcIlXPS1cM1agBMy" alt=""><figcaption><p>Auto Blue Alliance</p></figcaption></figure>

<figure><img src="/files/dxE8b2k9k3DDlgQSma46" alt=""><figcaption><p>Auto Red Alliance</p></figcaption></figure>

The two versions of the code are nearly identical with the difference being which direction the robot needs to turn before backing up.&#x20;

<div><figure><img src="/files/bkAdyckkL23F2QpodMEt" alt="" width="299"><figcaption><p>Turn Blue</p></figcaption></figure> <figure><img src="/files/0bi89xLT4bkPn9AeN65J" alt=""><figcaption><p>Turn Red</p></figcaption></figure></div>

Let's take a closer look at how our auto code works.

## Running Auto

### Launching Balls

<figure><img src="/files/80ytRA5L3OGFYdiJ94WK" alt=""><figcaption><p>Code for launching balls for 10 seconds</p></figcaption></figure>

Our entire auto is contained to an if/else statement checking if opModeIsActive is true, meaning the "play" button has been pressed on the Driver Hub. Once this occurs, it'll read out that the OpMode is running.&#x20;

To start launching balls into the target, the associated timer will first be reset. Elapsedtimers begin counting at their creation so it is important to reset them when they're actually going to be used to get a correct time.&#x20;

With the timer running, the "bankShotAuto", the same used in TeleOp, will begin running for 10 seconds. This time can be adjusted, but was set to 10 seconds in the example as a safe window for teams to begin testing with and observing how their robot acts.&#x20;

<figure><img src="/files/tiz0jyALsPeZkBVEgzJ1" alt=""><figcaption><p>10 second timer for launching in autonomous</p></figcaption></figure>

{% hint style="info" %}
When using a "whileLoop" in Blocks a call of if the "opModeIsActive" is required for the loop to properly run.
{% endhint %}

A telemetry readout to the Driver Hub will show how much time has passed according to the "autoLaunchTimer" to aid with making adjustments.

<figure><img src="/files/LHatReFkJdxAGoHrtJnN" alt=""><figcaption><p>Telemetry readout for the launcher timer</p></figcaption></figure>

Once our timer is up, all our actuators will be set back to 0 power or velocity.

<figure><img src="/files/6iRt0wtU9Z3AaIChpiGl" alt=""><figcaption><p>Setting actuators back to 0</p></figcaption></figure>

### Driving in Auto

There are two parts to our program for the robot driving in autonomous. In our if/else statement, we have a portion of the "autoDrive" function taking in inputs to calculate the robot's movements. Let's looking at the function itself first.

<figure><img src="/files/bpYQyBZzLwcHI9zQZcbp" alt=""><figcaption><p>Full autoDrive code</p></figcaption></figure>

Here our elapsed timer will reset to be ready for use with the robot's movements. Then the drivetrain motors are given a target position. This target position is calculated using the current position of the motor, the inputted distance in inches from the main function, and our conversion set up during initialization.&#x20;

<figure><img src="/files/Isd0PLdHEas9sMrWDBf8" alt=""><figcaption><p>Calculating drivetrain movements using the motors' encoders</p></figcaption></figure>

Next, we're change our motors to "RUN\_TO\_POSITION" mode for this autonomous. The power to be provided is set by the "speed" given in the main function.&#x20;

<figure><img src="/files/tkgwMgCovT7pHL8Vmjeo" alt=""><figcaption><p>Updating the mode and power for the drivetrain motors</p></figcaption></figure>

With all that information gathered, our robot will now moved the specified direction and distance stopping when either the motors halt or the timer runs out. Using "call idle" allows our program to progress between the two functions.&#x20;

<figure><img src="/files/SoHvVlciW3zrGFt30YLg" alt=""><figcaption><p>Checking that the motors are active and the timer has not run out</p></figcaption></figure>

Once our movement is complete, our drivetrain motors are set to turn to 0 power and reset back to "RUN\_WITHOUT\_ENCODER" in preparation for TeleOp.

<figure><img src="/files/ZfqHCr5pj4ewBOjeBIn8" alt=""><figcaption><p>Updating the mode and power for the draintrain motors after running</p></figcaption></figure>

Now let's look at the remainder of our main function of "doAuto".

<figure><img src="/files/Ag2N1VbV5fScRtDZ0Xsi" alt=""><figcaption><p>Movements of the robot in autonomous</p></figcaption></figure>

For each portion of movement we have inputted:

* **speed**- The set power for the motors&#x20;
* **leftDistanceInch/rightDistanceInch**- The target distance we want our robot to move to be calculated with our equation. This will be different for each motor when the robot is turning.
* **timeout\_ms**- this is the maximum time the elapsedtimer can count up to in milliseconds.&#x20;

Let's take a look at each step of the robot's movement

#### Back Up

The robot will first back away from the goal, at half power, roughly 12 inches. If something happens where the robot cannot complete this, such as colliding with another robot, this step will timeout after 5 seconds.

<figure><img src="/files/R8bvth2o5DF8gPrJROTj" alt=""><figcaption><p>Code for the robot backing up</p></figcaption></figure>

#### Turn

Next the robot will turn at half power about 6 inches making a 90 degree angle. If something happens where the robot cannot complete this, such as colliding with another robot, this step will timeout after 5 seconds.

<figure><img src="/files/vi0Um5vGpPsEfOkUzLJR" alt=""><figcaption><p>Code for the robot turning</p></figcaption></figure>

#### Drive Off Line

Finally the robot will back up at full power 50 inches to be off the line. This is much further than needed to be off the line so we encourage teams to adjust this value to get the robot positioned where they prefer.&#x20;

If something happens where the robot cannot complete this, such as colliding with another robot, this step will timeout after 5 seconds.

<figure><img src="/files/MR3sIXt1NCPQoGsC7MO0" alt=""><figcaption><p>Code for the robot driving off the line</p></figcaption></figure>

Once the robot has finished moving, the code will stop and return to the initialization option.&#x20;
