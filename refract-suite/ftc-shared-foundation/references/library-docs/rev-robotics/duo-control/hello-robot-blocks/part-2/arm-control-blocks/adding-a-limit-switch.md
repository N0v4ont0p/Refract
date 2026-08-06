> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arm-control-blocks/adding-a-limit-switch.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arm-control-blocks/adding-a-limit-switch.md).

# Adding a Limit Switch

Something to consider is the physical limitations of your arm mechanism. Just like you have limitations in how far you can move your arms, our robot's arm can only move up or down so far. However, while you have nerves to help you know when you've hit your limit, we need to add something to help prevent the robot from damaging itself or things around it.

This is where the importance of using sensors comes into play. There are a few ways we could limit our mechanism. What do you think they could be?

In this section we're going to look at how to add a limit switch to stop our robot's arm from extending too far. You might recall in our "Programming Touch Sensors" section that we discussed the touch sensor can act like an on/off switch when programmed. Essentially we're going to have the arm of our robot turn its motor off once the limit is met!

{% hint style="info" %}
This section is designed with the REV Touch Sensor or Magnetic Limit Switch in mind. There may be additional requirements for 3rd party touch sensors.

If you are using a Class Bot your robot should have a Touch Sensor mounted to the front of your robot chassis. You also have a[ Limit Switch Bumper](https://docs.revrobotics.com/15mm/ftc-starter-kit-class-bot/skv3-arm-assemblies#limit-switch-bumper-assembly) installed.
{% endhint %}

For the moment, let's grab the <img src="/files/-Ma5a_1yFPykLjStaOFu" alt="" data-size="original"> statement made in the previous section to be set off to the side for later use.

<figure><img src="/files/xzDcvCDCxBIQuy8TcLeP" alt=""><figcaption></figcaption></figure>

### Quick Check!

Think back to the "Programming Touch Sensors" section, where you learned how to create a basic limit switch program, similar to the one below:

<figure><img src="/files/PJNfiIZLSThi1Htp1x3s" alt=""><figcaption></figcaption></figure>

We also learned how the touch sensor operates on a `TRUE/FALSE binary`. So what is our program above asking the robot to do?&#x20;

<details>

<summary>What is our code doing?</summary>

Remember that when the touch sensor is pressed it reports as TRUE and while it is NOT pressed it is FALSE.

Right now our robot has been told the motor should be moving at 20% power when the button is not pressed. Once the button is pressed it'll set the power to 0!

</details>

### Adding Controller Control

Add the <img src="/files/-Ma5a_1yFPykLjStaOFu" alt="" data-size="original"> block set back to the code in the else port of the <img src="/files/rGAYsd7qqpCswTEuexAa" alt="" data-size="original"> block.&#x20;

<figure><img src="/files/79rXMuD8WcjfJS9j4zDl" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
While testing, double check the arm mechanism is aligned with the Touch Sensor.&#x20;

For the Class Bot V2, you may need to adjust the Touch Sensor so that the Limit Switch Bumper is connecting with it more consistently.&#x20;
{% endhint %}

{% hint style="success" %}
Save the op mode and give it a try!
{% endhint %}

### Making Adjustments

When you tested the above code what happened? You may have encountered a problem where once the touch sensor was pressed the arm could no longer move. This is probably not ideal so why do you think this happened?

One of the advantages of a limit switch, like the touch sensor,  is the ability to easily reset to its default state. All it takes is the pressure being released from the button, but right now all our robot knows is that if the switch is pressed it needs to turn off power!

**So how do we fix that?**&#x20;

To remedy this, an action to move the arm in the opposite direction of the limit needs to be added to the **do** statement.  Since the touch sensor serves as the lower limit for the arm, it will need to move up (or the motor in the forward direction) to back away from the touch sensor.&#x20;

To do this we can create an `if/else` statement similar to our existing gamepad `Gamepad if/else if`statement. In this instance, when the touch sensor and`DpadUp`are pressed together the arm moves away from the touch sensor. Once the touch sensor no longer reports true, the normal gamepad operations will takeover again!&#x20;

<figure><img src="/files/5hQSi6FOyYuFPjm0cvso" alt=""><figcaption></figcaption></figure>

Now we can snap this into our do statement to complete our code:

<figure><img src="/files/kl1e2tMlZuuzrfkSTejB" alt=""><figcaption></figcaption></figure>
