> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/build-tips-and-tricks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/into-the-deep-2024-25/build-tips-and-tricks.md).

# Build Tips & Tricks

{% embed url="<https://www.youtube.com/watch?v=hIvENLdEs3Y>" %}

## Compatibility with Starter Kit V3

The 2024-25 REV DUO Starter Bot is designed to be built with the FTC Starter Kit V3.1, however there are only a few parts missing from the Starter Kit V3. Below is the list of parts you will need to add to your Starter V3 to make it compatible with the 2024-25 REV DUO Starter Bot.&#x20;

| Part number       | Description                                                                                             | Quantity |
| ----------------- | ------------------------------------------------------------------------------------------------------- | -------- |
| REV-41-1124-PK100 | [M3 x 20mm Hex Cap Screws - 100 Pack](https://www.revrobotics.com/M3-Hex-Cap-Screws/)                   | 1        |
| REV-41-1600       | [UltraPlanetary Gearbox Kit & HD Hex Motor](https://www.revrobotics.com/rev-41-1600/)                   | 1        |
| REV-41-1491-PK4   | [M3 Standoff - 30mm - 4 Pack](https://www.revrobotics.com/M3-Standoffs/)                                | 2        |
| REV-41-1493-PK4   | [M3 Standoff - 45mm - 4 Pack](https://www.revrobotics.com/M3-Standoffs/)                                | 1        |
| REV-41-2702-PK4   | [Flap Wheel - 5mm Hex Bore - Medium (Dark Gray) - 4 Pack](https://www.revrobotics.com/duo-flap-wheels/) | 2        |

## Pre-Loading Brackets

There are many brackets used in the 2024-25 REV DUO Starter Bot, pre-loading these brackets with the appropriate screws and nuts make these steps easier. Pre-Loading is discussed in the [Channel Drivetrain build guide](/duo-build/channel-drivetrain-build-guide.md). When pre-loading remember that the head of the Hex Cap screw should face the extrusion.&#x20;

<figure><img src="/files/6CoRRhU9zw8RfM0SE5Ou" alt="" width="375"><figcaption></figcaption></figure>

## UltraPlanetary Overtightening&#x20;

When you [assemble your UltraPlanetary](/rev-crossover-products/ultraplanetary/assembly-instructions.md) take care not to over-tighten the gearbox housing screws. Hand tight is enough to keep the gearbox assembled. If you overtighten the gears might bind leading to poor performance and possibly damage.&#x20;

<figure><img src="/files/K0mdrKaZXbJWTp3wbzPR" alt=""><figcaption></figcaption></figure>

## Making the Chain and Master Links

Roller chain is typically connected into a continuous loop. This can be done using a Chain Tool to press the pins in and out of the desired outer link as described in the build guide. An alternate way to make the chain is using a common roller chain accessory called a [Master Link](/duo-build/motion/sprockets-and-chain/chain-tool.md#master-links), or quick-release link. Two of these master links come in your FTC Starter Kit V3.1. Master links allow for easy chain assembly/disassembly without any special chain tools. Master links can typically be reused many times, but can become bent with multiple uses. At the point that master links become bent they should be discarded.

<figure><img src="/files/Mu13dN4fQfEDIHR1b4b7" alt=""><figcaption></figcaption></figure>

## Squaring Your Assembly

When assembling your Starter Bot, it is important to square up your shafts and extrusion. This will ensure your robot operates smoothly and effectively. To check if your assembly is square you can use a Square tool or if that is not available you can use something with a known 90 degree angle such as a sheet of paper.&#x20;

<figure><img src="/files/0uAtwzxcCEL2xKDz3qgd" alt="" width="339"><figcaption></figcaption></figure>

## Initializing Your Robot

The preset positions, such as "Intake" and "Low Basket," in the default Starter Bot code work using the built-in encoders of the motors. To ensure the robot moves to the correct position for these presets, make sure the robot is powered on while in its initialization orientation.&#x20;

This orientation is pictured below: arm down and the wrist folded up.&#x20;

<figure><img src="/files/CFSXs4NsWTmfNQLqLtbm" alt="" width="371"><figcaption></figcaption></figure>

## Programing Your Smart Robot Servo

The 2024-25 REV DUO Starter Bot uses two Smart Robot Servos. The Intake servo needs to be programed in Continuous Rotation mode and the Claw servo needs to be programed in Default Operation with angular limits set. Use the [SRS Programmer (REV-31-1108)](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer) to [switch the operating modes.](/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md#continuous-rotation)&#x20;

{% embed url="<https://youtu.be/PJjFdsnw0uY?feature=shared>" %}

## Wire Management&#x20;

One of the most important steps for a reliable and safe robot is wire management. Wire management involves bundling and routing wires along a defined path to the electrical parts, such as servos and motors. Wires can bundled with zip ties, wrapped in tape, tucked into extrusion, and routed away from moving parts of your robot.&#x20;

#### Pinch Points

There are points on the robot that can catch an unconstrainted wire and pinch it causing it to be damaged or disconnected. This is most noticeable with the gears on the arm and the servo wires, however, the arm still needs to move we can not completely constrain the wires.&#x20;

<figure><img src="/files/cTiCoHqdaC5MNyEShwZF" alt="" width="375"><figcaption></figcaption></figure>

We recommend using a length of extra wire to form a "service loop", like the one shown above. This loop keeps wires bundled together, and provides a predictable path of movement as your arm pivots.&#x20;

<figure><img src="/files/k1Q7yKKgCWF18EY0gBOl" alt="" width="375"><figcaption></figcaption></figure>

#### Strain Relief &#x20;

Minimizing stress on a wire connection, which is often a two-part connector on FTC Robots, is a great method to avoid wiring getting pulled loose within your control system! Proper strain relief ensures that the wires are not causing unnecessary stress on the connectors and that the connection remains snug.&#x20;

To add strain relief to your wiring, secure the wire about one or two inches from the connector and leave a bit of slack on the connector side. This helps avoid unintentional tension that could damage the connector and allows for easy disconnection when needed for testing or replacing modules.&#x20;

<figure><img src="/files/ywsPnbsXoGTZ8TycdxDQ" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
Be careful to not leave too much or too little slack on either end of the connection

* Too little slack can cause the wires to pull apart&#x20;
* Too much slack can become an entanglement risk
  {% endhint %}

#### Smart Tug

A "Smart Tug" is a test where you test your wiring by tugging on a wire with a reasonable amount of force to see if it comes undone. The Smart Tug simulates many common scenarios, including a wire getting caught on a field element, actuator, or another robot. It is a good practice to do this test any time you connect a wire to ensure it is fully seated in the connector and secure.&#x20;

{% hint style="success" %}
If you perform a Smart Tug on your wire and it becomes disconnected, you can use one of the above methods to secure the wire!
{% endhint %}

## Starter Bot Programming TeleOp without Initialization

The provided program template for the 2024-25 Starter Bot has the robot move to initialization at the start of the program. However, in some situations the arm and wrist motor may never hit the designated starting position leading to oscillating movements, or the Control Hub may have been powered on in the wrong positions, which determines these motors' zeroes, leading to unexpected movement.&#x20;

Below is a version of the TeleOp program that changes this initialization so the robot no longer moves until receiving input from the gamepad. This version is only available for the basic Blocks template and not for any upgrades. Read through the short guide below to learn more about the changes!

### Download of Starter Bot Program without Initialization

{% file src="/files/jVnKRaYQFrLee395HLa9" %}

### Robot Start Up Position

When the program begins, the robot will first STOP\_AND\_RESET\_ENCODER for the arm's HD Hex Motor and wrist's Core Hex Motor. Whatever position the arm and wrist are in will become the "zero" the presets are based around.&#x20;

<figure><img src="/files/JBnpjylrVcxFyMHWNDrb" alt=""><figcaption><p>STATE_MACHINE with INIT change</p></figcaption></figure>

Because of this, the arm and wrist should still start in a similar position as we recommended on the [default program](#initializing-your-robot), which is ideal for a competition set up as well. Your team should consider marking or labeling your robot in some way to know always where the arm should be reset between runs of the program.&#x20;

### Left Bumper Reset

When pressing the left bumper on the gamepad, the arm and wrist will return to their start up position. To prevent this from also resetting the encoder, a new variable called ZEROING has been added to our STATE\_MACHINE as seen below:

<figure><img src="/files/mz1bpyW1rHnSBaP6lCe9" alt=""><figcaption><p>ZEROING position</p></figcaption></figure>

The call for the left bumper now looks like below:

<figure><img src="/files/0ESDtSLSppQ3A66us2pp" alt=""><figcaption><p>When LeftBumper is pressed the arm and wrist move to ZEROING</p></figcaption></figure>

### Adjusting the STATE\_MACHINE

Due to variations in the robot's structure and how team's decide to position it for start up, you will likely need to make some adjustments to your arm and wrist values within the STATE\_MACHINE to fit your team's needs for the presets.

<figure><img src="/files/1cfQ6y1rdCtlCOngEE80" alt=""><figcaption><p>Updated STATE_MACHINE</p></figcaption></figure>

Some changes to the targetArm position have already been included, but we recommend using the telemetry readout on your Driver Hub to refine your movements!&#x20;

**Remember if you change where you start your arm and wrist the zero for the motors will change**. A breakdown of the [positions can be found here as part of the main tutorial](/ftc-kickoff-concepts/into-the-deep-2024-25/programming-teleop/programming-initialization.md#establishing-variables).&#x20;
