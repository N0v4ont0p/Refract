> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arm-control-onbot-java/adding-a-limit-switch.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-java/part-2/arm-control-onbot-java/adding-a-limit-switch.md).

# Adding a Limit Switch

Something to consider is the physical limitations of your arm mechanism. Just like you have limitations in how far you can move your arms, our robot's arm can only move up or down so far. However, while you have nerves to help you know when you've hit your limit, we need to add something to help prevent the robot from damaging itself or things around it.

This is where the importance of using sensors comes into play. There are a few ways we could limit our mechanism. What do you think they could be?

In this section we're going to look at how to add a limit switch to stop our robot's arm from extending too far. You might recall in our "Programming Touch Sensors" section that we discussed the touch sensor can act like an on/off switch when programmed. Essentially we're going to have the arm of our robot turn its motor off once the limit is met!

{% hint style="info" %}
This section is designed with the REV Touch Sensor or Magnetic Limit Switch in mind. There may be additional requirements for 3rd party touch sensors.

If you are using a Class Bot your robot should have a Touch Sensor mounted to the front of your robot chassis. You also have a[ Limit Switch Bumper](https://docs.revrobotics.com/15mm/ftc-starter-kit-class-bot/skv3-arm-assemblies#limit-switch-bumper-assembly) installed.
{% endhint %}

### Quick Check!

Think back to the "Programming Touch Sensors" section, where you learned how to create a basic limit switch program, similar to the one below:

{% code title="Limit Switch if/else" %}

```java
 if (test_touch.isPressed()){
    //Touch Sensor is pressed  
     arm.setPower(0);
} else {
    //Touch Sensor is not pressed 
    arm.setPower(0.2);
                        }
```

{% endcode %}

We also learned how the touch sensor operates on a `TRUE/FALSE binary`. So what is our program above asking the robot to do?&#x20;

<details>

<summary>What is our code doing?</summary>

Remember that when the touch sensor is pressed it reports as TRUE and while it is NOT pressed it is FALSE.

Right now our robot has been told the motor should be moving at 20% power when the button is not pressed. Once the button is pressed it'll set the power to 0!

</details>

### Adding Controller Control

Let's take the next step for our program by adding the ability to control our arm with a controller. To do this we can nest the `Gamepad if/else` statement within the `Limit Switch if/else` statement as seen below:

<pre class="language-java"><code class="lang-java">if(test_touch.isPressed()){
     arm.setPower(0);
       }
  else {
      if(gamepad1.dpad_up){
       arm.setPower(0.2);         
            }
     else if (gamepad1.dpad_down){
       arm.setPower(-0.2); 
            }   
<strong>     else { 
</strong>       arm.setPower(0); 
            } 
       } 
</code></pre>

{% hint style="warning" %}
While testing, double check the arm mechanism is aligned with the Touch Sensor.&#x20;

For the Class Bot V2, you may need to adjust the Touch Sensor so that the Limit Switch Bumper is connecting with it more consistently.&#x20;
{% endhint %}

{% hint style="success" %}
Save the OpMode and give it a try!
{% endhint %}

### Making Adjustments&#x20;

When you tested the above code what happened? You may have encountered a problem where once the touch sensor was pressed the arm could no longer move. This is probably not ideal so why do you think this happened?

One of the advantages of a limit switch, like the touch sensor,  is the ability to easily reset to its default state. All it takes is the pressure being released from the button, but right now all our robot knows is that if the switch is pressed it needs to turn off power!

**So how do we fix that?**&#x20;

To remedy this, an action to move the arm in the opposite direction of the limit needs to be added to the `else` statement.  Since the touch sensor serves as the lower limit for the arm, it will need to move up (or the motor in the forward direction) to back away from the touch sensor.&#x20;

To do this we can create an `if/else` statement similar to our existing gamepad `Gamepad if/else if`statement. In this instance, when the touch sensor and`DpadUp`are pressed together the arm moves away from the touch sensor. Once the touch sensor no longer reports true, the normal gamepad operations will takeover again!&#x20;

```java
if(test_touch.isPressed()){
       if(gamepad1.dpad_up){
            arm.setPower(0.2);         
                 }
       else{
            arm.setPower(0);
                 }  
       }
  else {
   if(gamepad1.dpad_up){
            arm.setPower(0.2);         
                 }
      else if (gamepad1.dpad_down){
            arm.setPower(-0.2); 
                 }   
      else { 
            arm.setPower(0); 
                 } 
       } 
```
