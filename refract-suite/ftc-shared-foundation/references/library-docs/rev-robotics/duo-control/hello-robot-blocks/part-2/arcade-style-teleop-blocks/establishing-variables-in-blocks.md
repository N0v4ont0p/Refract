> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/establishing-variables-in-blocks.md).

# Establishing Variables in Blocks

## Creating X and Y Variables

You may not expect it, but there is a little bit of math that needs to be done to get our robot moving smoothly. But before we dive too deeply into that let's start with the basics of movement we'll need.

To start, create two variables x and y . This can be done within the Variable menu on the lefthand side.

<figure><img src="/files/d26xLt9TmyNpl8B2aRHp" alt=""><figcaption></figcaption></figure>

Once created, add the <img src="/files/-MVS6vr4fOLI02xyBjhL" alt="" data-size="original">and<img src="/files/-MVS14nu9_ZE4QKp6Yn5" alt="" data-size="original">blocks to the while loop above your existing power block.

<figure><img src="/files/cEjJAOPARN4GQHecoLIW" alt=""><figcaption></figcaption></figure>

Our y variable will be assigned as <img src="/files/-MVY90hzKehu4L9uGscf" alt="" data-size="original">, which is the y-axis of the right joystick. Remember just like in[ Part 1: Programming a Motor with a Gamepad](/duo-control/hello-robot-blocks/part-1/programming-motors/programming-a-motor-with-a-gamepad.md) the y-axis will need to be inversed using the ![](/files/F4RyoOkkSdFrDFahXg6V) block available from the Math menu.

Next assign x as the <img src="/files/-MVY92VNjdfeFbgTDbty" alt="" data-size="original">, which is the x-axis of the right gamepad joystick. The x-axis of the joystick does not need to be inverted.&#x20;

<figure><img src="/files/VugsszcR1TNxSUxXRLht" alt=""><figcaption></figcaption></figure>

The <img src="/files/-MVYECjmC5fNog4tq9u5" alt="" data-size="original"> and <img src="/files/-MVYEFfkG_JRA7Cf0cUT" alt="" data-size="original"> block sets assign values from the gamepad joystick to x and y. Depending on the orientation of the joystick, these valuables will receive some value between -1 and 1.&#x20;

For a quick reference let's take a look at what number each variable would be assigned at their far ends:

|                          Joystick Direction                         | $$x$$ | $$y$$ |
| :-----------------------------------------------------------------: | :---: | :---: |
| <img src="/files/-Mefhx7EWkkmadU6LW8V" alt="" data-size="original"> |   0   |   1   |
| <img src="/files/-MefhzwimOC2m68IoDSE" alt="" data-size="original"> |   0   |   -1  |
| <img src="/files/-Mefi1rcj_EIfo6ZRW2u" alt="" data-size="original"> |   -1  |   0   |
| <img src="/files/-Mefi4IQJxLAupAhBq8Y" alt="" data-size="original"> |   1   |   0   |

### What is a Variable?

Right now we have x and y assigned values based on our joystick's movement, but what does that mean? Why is that useful?

Maybe you have seen in a math class before something like this:

$$
a + 8 = 15
$$

In this case, **a** is our variable that has been assigned some value. For this example, we can determine that value is 7. But what does that mean in programming?&#x20;

Variables used in programming follow this same principle. We can define a variable within our code to hold a set value or a value that changes, such as we are doing here. Then whenever that variable is referenced the robot will read it as that assigned value!

So using our example above if I had:

$$
a + 10 = ?
$$

My robot would know my variable of **a** is equal to 7 and therefore calculate the answer as 17 for me!

### When or Why do we use Variables?

Consider for a moment, why should we use a variable when we could just use the number on its own?&#x20;

We'll be using variables in greater detail in later sections, but even for our drive code you will be able to see the use of variables helps keep our program clean and easier to follow.&#x20;

By using setting our ![](/files/m709m4TBmp15BAAOutqz)variable at the beginning of our code we can inverse it without needing to do so every time we may reference the joystick's y-axis. Within a longer program, having our variables defined at the start would allow us to quickly change a value without having to hunt down or double check that every possible instance in the code has been updated to reflect this change. Instead we are able to change it once and continue testing!
