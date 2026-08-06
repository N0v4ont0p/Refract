> Source: https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/programming-arcade-drive.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/hello-robot-blocks/part-2/arcade-style-teleop-blocks/programming-arcade-drive.md).

# Programming Arcade Drive

### Programming Arcade Drive

From the **math** menu grab the <img src="/files/-MW0x3wm9ShSr87RKGmE" alt="" data-size="original">and <img src="/files/-MW0xADWQomF1x9ui--7" alt="" data-size="original"> blocks and add them to the respective motor in the <img src="/files/-MVwRA9auYOOqnGmzAX7" alt="" data-size="original"> block.&#x20;

<figure><img src="/files/Rfvw7gvYqBg3DaM3bPug" alt="" width="435"><figcaption></figcaption></figure>

Next add the <img src="/files/-MW1GN0AKTXtbG-4RSvt" alt="" data-size="original"> and <img src="/files/-MW1GPqHF3_v0S-vEmE3" alt="" data-size="original"> variables to the formula blocks. &#x20;

<figure><img src="/files/d2uqbKtzRPSTyNZqvDkV" alt=""><figcaption></figcaption></figure>

From there the robot will handle the rest as the program runs! Each time our loop cycles, the robot will check the position of our joysticks and quickly adjust the motor power based on its calculations.&#x20;

Save your OpMode and give it a try!

### Full Program

<figure><img src="/files/oiVStvKYLLCLpGkjeqvT" alt=""><figcaption></figcaption></figure>
