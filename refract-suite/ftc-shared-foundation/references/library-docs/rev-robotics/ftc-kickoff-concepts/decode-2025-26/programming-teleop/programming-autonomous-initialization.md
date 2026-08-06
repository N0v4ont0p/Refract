> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-initialization.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-autonomous-initialization.md).

# Programming - Autonomous Initialization

The autonomous version of the sample program includes the option for both a Blue and Red Alliance Auto, along with TeleOp, all in one code.&#x20;

#### Why combine everything into one program?&#x20;

Combining the Auto codes and TeleOp all together does make the Blocks program appear chunky and intimidating at first glance. However, the goal is for this to prevent issues with updates not being reflected across multiple programs.&#x20;

For example, say your team decides to make changes to the flywheel that leads to changes in what one of the target velocities should be set to. This change is then updated in TeleOp, perhaps the program the team runs most often, but neither of the auto options. This can lead to frustration and confusion later.

But since everything is combined here, when that one variable is update, it now is automatically reflect in all three options!&#x20;

Let's take a look first at how we select which OpMode should run when we press "play" on the Driver Hub.

## Initialization with Auto

<figure><img src="/files/qdQPQmtBYU5I8WTQYcHh" alt=""><figcaption><p>Initilization for the autonomous program</p></figcaption></figure>

First, you may notice compared to our "default" code that the variables and motor modes are gone. These have been combined into a function, "initRobot", for clarity. We'll look at that function more closely below.&#x20;

Next, rather than checking if our opModeIsActive as we usually do we are instead checking that the program has only been initialized. In this time frame is when we can select which OpMode will run.&#x20;

<figure><img src="/files/oEovO93JFKzOPmJ0DjCu" alt=""><figcaption><p>Code for switching between OpModes using the gamepad</p></figcaption></figure>

Our "operationSelected" variable will ultimately set which OpMode will run after receiving input from the function "selectOperation". By default, it is set to run TeleOp if the PS/Home button is never pressed.&#x20;

The "selectOperation" function will output the end state to change this variable. The PS/Home button on the gamepad will progress the if/else statement used for determining this state. We'll break this down further below!

<figure><img src="/files/wlKALCbXPmzJtsF8TCwh" alt=""><figcaption><p>Function block for inputting operationSelected and gamepad inputs</p></figcaption></figure>

After "waitForStart" is called, the robot will execute the appropriate function containing the Auto Blue, Auto Red, or TeleOp code based on what was selected.

<figure><img src="/files/ZJbsWl17SiCHKcTGvswn" alt=""><figcaption><p>If/else statement for determining which mode will run</p></figcaption></figure>

### Initializing Variables and Settings

<figure><img src="/files/t7ArgPUdoTRU7wKq9RhF" alt=""><figcaption><p>Setting up actuator settings and initializing variables</p></figcaption></figure>

Let's focus on the new variables added in this version of the code. To learn about the motor settings and existing variables check out [Programming - Initialization](/ftc-kickoff-concepts/decode-2025-26/programming-teleop/programming-initialization.md#motor-and-servo-settings).&#x20;

First, we need to set up the variables used while selecting our state to mean something. In this case, rather than the variables being set to a number, we will set them to a name.&#x20;

<figure><img src="/files/q5QF7XsnhuWpQg3sHWvj" alt=""><figcaption><p>Defining the text based variables</p></figcaption></figure>

Additionally, we need our "operationSelected" to have a default program to run.&#x20;

<figure><img src="/files/ICASs0qBeGqzmKfT9G8Q" alt=""><figcaption><p>Defaulting operationSelected to "TeleOp"</p></figcaption></figure>

{% hint style="info" %}
When making edits to this program, please note that the order the variables are defined MATTERS. If "operationSelected" is defined before the Auto/TeleOp variables are set to a name it will return an error.
{% endhint %}

For autonomous we'll be using elapsed timers and encoders. Because of this we need to set up some needed information to be referenced later, starting with our timers.&#x20;

* autoLaunchTimer - controls how long the robot will launch balls during autonomous
* autoDriveTimer - controls how long the robot can drive when backing away from the launch line

<figure><img src="/files/yjJP40V7ERbWYvfBTyey" alt=""><figcaption><p>Setting up timers for autonomous</p></figcaption></figure>

For drivetrain encoders, we can go ahead and do our math here needed to convert wheel size into appropriate ticks.&#x20;

<figure><img src="/files/YjYC0c6Hevj3zz77CSEa" alt=""><figcaption><p>Completing the math needed for using encoders in auto</p></figcaption></figure>

{% hint style="info" %}
Interested in learning more about programming with encoders or elapsed timers? Check out [Hello Robot!](/duo-control/hello-robot-blocks/part-3.md)
{% endhint %}

### selectOperation Function

<figure><img src="/files/dPsDiUrGimyLqX7IMsk8" alt=""><figcaption><p>Full code for cycling between options using the gamepad</p></figcaption></figure>

Unlike functions we've used previously, the "selectOperation" function is set up to take in an input then return an output after being completed. In this instance, "state" and "cycleNext" are being inputted then the output will be the variable "state".&#x20;

Keep in mind the function will repeatedly run while the specified condition is true, in this case so long as the program is set to initialization. Therefore state will be an input and output between each cycle.

Functions such as this are created in Blocks by clicking the gear icon and adding desired inputs.

<figure><img src="/files/U81F39HksW43a90GhbbT" alt=""><figcaption><p>How to create a function that uses inputs</p></figcaption></figure>

#### Cycling OpModes

<figure><img src="/files/am7glurtGN2q78kBKwfl" alt=""><figcaption><p>If/else for cycling between auto blue, auto red, and teleOp OpModes</p></figcaption></figure>

As mentioned above, our cycleNext is tied to our PS/Home button and if it was pressed (not being held). Each time it is pressed, "state" will progress one step in our if/else statement moving through each option.

In short, our if/else is checking what "state" is currently set to then proceeding to the next option if the button is pressed again. In the event the input is not received properly, a warning will be returned instead as our final "else".&#x20;

#### Telemetry Outputs

<figure><img src="/files/MEq9VmNOaHD6qC7P3Wwt" alt=""><figcaption><p>Telemetry readout to the Driver Hub for what is selected</p></figcaption></figure>

Based on which "state" or OpMode has been selected, the Driver Hub will showcase different telemetry reads. First is the telemetry to provide the directions for cycling OpModes and the current selection.&#x20;

<figure><img src="/files/PUDrkNaPDGAriPppBRcS" alt=""><figcaption><p>Directions for how to cycle options</p></figcaption></figure>

If an autonomouse mode has been selected, then the Driver Hub will read out a prompt to turn on the "Auto timer" built into the Driver Station App for autonomous. This will prevent the robot from continuing to run after the 30 second auto period.

<figure><img src="/files/wP0zKqpw8W09HepEaN05" alt=""><figcaption><p>Reminder to turn on the auto timer</p></figcaption></figure>

Lastly is another instruction for starting the program when ready. You'll see at the bottom of our function the return of "state" to be used.

<figure><img src="/files/krT7ix6elUuOf4PjWVTx" alt=""><figcaption><p>Directions for starting the program</p></figcaption></figure>
