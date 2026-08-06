> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/moving-to-a-target-distance.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-3/autonomous-navigation-blocks/moving-to-a-target-distance.md).

# Moving to a Target Distance

Now that you have created the constant variables needed to calculate the amount of ticks per mm moved, you can use this to set a target distance. For instance, if you would like to have the robot move forward two feet, converting from feet to millimeters and multiplying by the `COUNTS_PER_MM` will give you the amount of counts (or ticks) needed to reach that distance!

Let's create two more variables called `leftTarget`  and `rightTarget`. Add the <img src="/files/-MYfarkmXxKPyNxDquzZ" alt="" data-size="original">and <img src="/files/-MYfauhcXmBRK_CtexwM" alt="" data-size="original"> blocks within the if/then statement that will run once Play is selected.

<figure><img src="/files/NWseBlFM0EjHzozNXsDQ" alt=""><figcaption><p>Inserting our leftTarget and rightTarget variables</p></figcaption></figure>

### Converting from mm to Feet

Right now the main distance factor is `COUNTS_PER_MM` , however you may want to go a distance that is in the imperial system, such as 2 feet (or 24 inches). The target distance in this case will need to be converted to mm.&#x20;

To convert from feet to millimeters use the following formula:

$$
d\_{(mm)} = d\_{(ft)} × 304.8
$$

If you convert 2 feet to millimeters, it comes out the be 609.6 millimeters. For the purpose of this guide, lets go ahead an round this to be 610 millimeters.&#x20;

### Converting Feet to Ticks

Next, multiply 610 millimeters by the `COUNTS_PER_MM` variable to get the number of ticks needed to move the robot 2 feet. Since the intent is to have the robot move in a straight line, set both the `leftTarget` and `rightTarget`, to be equal to 610 \*  `COUNTS_PER_MM`

<figure><img src="/files/xUVlpxu3Ddle66ZarW9r" alt=""><figcaption></figcaption></figure>

Lastly, we need to change the <img src="/files/-MYGq13GHps2CyeLWbZt" alt="" data-size="original"> so that both motors are set to the appropriate target position. To do this add the <img src="/files/-MYfkdJjHrXQM9Phg8gz" alt="" data-size="original"> and <img src="/files/-MYfkhOc5yahjvtzUAq2" alt="" data-size="original"> blocks to their respective motor.&#x20;

<figure><img src="/files/CxGhmx4IpFnrqzNOMDR0" alt=""><figcaption><p>All of the blocks added to set a target distance</p></figcaption></figure>
