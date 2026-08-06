> Source: https://docs.revrobotics.com/rev-crossover-products/blinkin/ion.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/blinkin/ion.md).

# REV ION Application Examples

### Wiring with the *FIRST* Robotics Competition Control System

The BLINKIN LED Driver comes with the 36” PWM Cable (REV-11-1130), that can be used to connect the BLINKIN to the NI roboRIO’s PWM ports for communication. To power the BLINKIN you need an XT30 Cable with one male connector and bare wire on the opposing end. Plug the male connector into the BLINKIN and the bare wire ends into the appropriate Power Distribution Hub channel.

The BLINKIN is capable of driving either a 5V Addressable LED Strip (REV-11-1198) or a 12V RGB LED Strip (REV-11-1197). The image below shows how both types of LED strips connect to the BLINKIN using the BLINKIN LED Cable Adapter (REV-11-1105).

{% hint style="info" %}
Always be sure to read the relevant rules and use appropriate gauge wiring before using anything on your competition robot.
{% endhint %}

![](/files/ldDDZnKJ5zDvOKJDDoh3)

After wiring your Blinkin into your robot, follow the [setup instructions ](/rev-crossover-products/blinkin/gs.md#setup-and-configuration)and follow the instructions on [PWM control ](/rev-crossover-products/blinkin/gs.md#pwm-control)as desired.

### *FIRST* Robotics Competition Programming Example

In the FRC Control System, motor outputs range varies depending on which type of motor controller is initialized. The output pulse range is scaled from the user requested output power of -1 to 1 to the range defined for each type of Motor controller.

| <p><strong>WPI Motor Control</strong></p><p><strong>Open Type</strong></p> | <p><strong>Minimum Pulse</strong></p><p><strong>Width Output (us)</strong></p> | <p><strong>Maximum Pulse</strong></p><p><strong>Width Output (us)</strong></p> |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| SPARK                                                                      | 1000                                                                           | 2000                                                                           |
| SRX                                                                        | 997                                                                            | 2004                                                                           |
| Talon SR                                                                   | 989                                                                            | 2037                                                                           |
| Jaguar                                                                     | 697                                                                            | 2322                                                                           |

The SPARK motor controller type output directly matches the input to the Blinkin, which makes the math to convert the -1 to 1 code range to the 1000-2000us Blinkin input range the simplest. Other control types, including servo, from the roboRIO can also be used, but the user will need to scale input range correctly to ensure they are sending only a valid PWM range and that they can select the desired LED pattern.

As an example, referencing the [Excerpt from the LED Pattern Tables](#excerpt-from-the-led-pattern-tables) includes an excerpt from the [LED Pattern Tables](/rev-crossover-products/blinkin/gs/patterns.md), and includes the correct SPARK motor output value for each pattern. The table below lists motor control values associated with specific patterns:

#### Example Spark Control Values based on the LED Pattern Table&#x20;

| **LED Color/Pattern**                        | **Motor Output Value** |
| -------------------------------------------- | ---------------------- |
| Ocean Colored Rainbow                        | -0.95                  |
| Larson Scanner (Similar to a Cylon)          | -0.35                  |
| Fast Heartbeat in User Selected Team Color 1 | 0.07                   |
| Solid Blue                                   | 0.87                   |

#### Excerpt from the LED Pattern Tables&#x20;

| <p><strong>Pulse Width</strong></p><p><strong>(us)</strong></p> | <p><strong>roboRIO SPARK</strong></p><p><strong>Value</strong></p> | **Pattern Type**      | Pattern/Palette            |
| --------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------- | -------------------------- |
| 1005                                                            | -0.99                                                              | Fixed Palette Pattern | Rainbow, Rainbow Palette   |
| 1015                                                            | -0.97                                                              | Fixed Palette Pattern | Rainbow, Party Palette     |
| 1025                                                            | -0.95                                                              | Fixed Palette Pattern | Rainbow, Ocean Palette     |
|                                                                 |                                                                    | **...**               |                            |
| 1325                                                            | -0.35                                                              | Fixed Palette Pattern | Larson Scanner, Red        |
|                                                                 |                                                                    | **...**               |                            |
| 1515                                                            | 0.03                                                               | Color 1 Pattern       | Heartbeat Slow             |
| 1525                                                            | 0.05                                                               | Color 1 Pattern       | Heartbeat Medium           |
| 1535                                                            | 0.07                                                               | Color 1 Pattern       | Heartbeat Fast             |
|                                                                 |                                                                    | **...**               |                            |
| 1765                                                            | 0.53                                                               | Color 1 and 2 Pattern | Color Waves, Color 1 and 2 |
|                                                                 |                                                                    |                       |                            |
| 1935                                                            | 0.87                                                               | Solid Colors          | Blue                       |
| 1945                                                            | 0.89                                                               | Solid Colors          | Blue Violet                |
| 1955                                                            | 0.91                                                               | Solid Colors          | Violet                     |

## Competition Robotics Application Ideas

Adding LEDs to your robot (or other project) can do more than just make them look cool, you can use LEDs to provide critical visual feedback. Here are some examples:

* Program a controller button to change the LED output pattern (e.g. 85 – Solid Yellow) and the drive can use the LEDs to communicate to the human player at a portal station across the field that the robot is ready to receive a game object.
* If the driver has poor visibility to see if the robot has acquired a game object, add a sensor to the intake and the LED strip can be programmed to automatically display a new pattern when the object is acquired. The driver never has to take their eyes off the robot to check the dashboard because the robot will clearly display its status.
* Using the match time value available in software, the LEDs can be changes to a time warning pattern (e.g. – Solid Red) with X seconds left in a match.
* The robot can display a different pattern when enabled vs disabled which provides a more visible indicator of the state of the robot than the RSL.
