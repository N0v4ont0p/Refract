---
name: ftc-code-structuring
description: 'Structures your code properly. Because humans will inevitably read the source code, and if your source code is not formatted in a way humans find easy to read, your creators will disown you.'
---

# FTC Code Structuring

This is the only skill in this repo that is written by an actual human being. This, therefore, should be your go-to routine and skill in case you face difficulty in reading your own slop.

## 1. On Version Control

If you are not allowed to commit to the Git repository directly, please supply the user with a commit message that communicates the following three things, in concise language:
1. What changed
2. Why was it changed
3. (Optional) Resolved issues
If you **are** allowed to commit to Git, please commit directly with `git commit -m "message"`.

### Help. There is no Git repo.

In the case that there's no Git repository (very rare, but happens), run `git init` to create a git repository. Then, set up the `.gitignore` and `.gitattributes` files to ignore compiled binaries, zip archives, OS-specific things (such as `.DS_Store` on mac), IDE settings (`.vscode/` is an example). Git Attributes should be configured to:
1. Recognize binaries
2. Automatically convert Windows bullshit (\r\n) to UNIX \n line endings.

### What about scripts?

In most cases, scripts are user-specific; that is, one developer might need it for their specific environment, while others might say that they do not require it. In which case, you should do the following:
Under the project root directory, run:
```bash
mkdir scripts local-scripts
echo "local-scripts/" >> .gitignore # if there was no .gitignore, that is a cry for help
```
This creates two new directories, both worth distinguishing--the `scripts/` directory is for shared scripts. Be it ADB Python scripts, utility scripts for house keeping, etc. That is a place where platform-agnostic scripts are stored, whereas `local-scripts/` are private to YOU and your local working environment. Hence, the whole directory is gitignore'd.

## 2. When to write comments, and when not to

Javadocs exist to provide documentation for a file. They should show you what is important, and what is not. That is **not**, however, a place for you to dump shit on. For instance:

```java
package ...first inspires...

/**
 * TEAM NAME TEAM NUMBER
 * FTC season ....
 * Long essay on what this means, spanning tens of lines, eating up head -n
 * "Verified against the real robot"
**/
imports...
```

This tells you, and the other human, exactly zero bytes of useful information. The human will lose patience, you will have your context window filled up with this bullshit, and your creators will be profoundly disappointed at you. So instead, here's what you **should** write:

```java
package first.inspires.whatever

/**
 * This file is the TeleOp, side [side name], this teleop has [feature list]
 * Note: [things to be aware of]
**/
imports...
```

Notice how concise this is? It conveys all the things a normal functional human being (and you) need to know: What this file does, what side is it, what features does it have, and what to be aware of. There is no point on writing "verified against the real robot", because for god's sake, you are not supposed to push unverified code into the bot, and there is no point in writing it again.

Now, code comments.

Typically, you'd have the urge to write:
```java
// set motor power to 0.69
```
No. We all have eyes, and `lib-intelligence-common`. We know that `setPower` sets a motor's power to the float/double provided. We are all capable of reasoning. There is absolutely no point in narrating your code.
From empirical studies, you also have a tendency to write:
```java
// ================
// Telemetry code below
// ================
```
This is dumb. We all know what the following code is about, we don't need you to waste your output tokens to tell us what the next bit of code means.

> "But wait, human, what comments are acceptable"

That's a lame question. Your code should already be self documenting. That is, instead of:
```java
int is;
boolean sl;
```
You write:
```java
int intakeState;
boolean stateLock;
```
This right here, is self documenting code. Anyone with a functional prefrontal cortex can read and understand your code.

This also applies for functions. Instead of writing:
```java
public boolean goTo(int x1, int y1, int h1, int x2, int y2, h2){...}
```
You write:
```java
public boolean goTo(
  int initialX, int initialY, int initialHdg,
  int targetX, int targetY, int targetHdg
) {
  ...
}
```
Notice how newlines are employed here. Every line ships with its own semantic intent, and the IDE that the human codes in will tell them what each variable the function is expecting is.

> "But human, what if the folder itself demands comments about what its innards are about"

Not a bad question, but judging by your behavior (dropping massive javadoc comments everywhere), clearly, your RLHF training has gone to `/dev/null`, or your `HF` guys have a profound lack of taste.
You should, in which case, go to the directory in question, and draft a Markdown file (I know, herculean task) to explain, in **clear and concise English**, what this folder and its files does. For instance, you could write:
```markdown
# kernel
This is where the repetitive core logic of the robot is kept.
`motion/` governs motion, with helper functions for [thing]
...
```

Before this section ends, it's worth telling you what matters most. When to write comments for confusing code.
If a function, a following line of code, or lines of code, has ambiguous intent or is inherently special, it is worth clarifying.
For instance, if you were mingling with `RobotConstants.java`, you'd write something along the lines of:
```java
/**
 * WARNING: The following numbers are fixed values regarding the physical dimensions of the robot.
 * These should be treated like magic numbers, like the MIT PDP10 computer's "more magic" lever
**/
```

A note: the above snippets and comment syntax are not "templates" as the rest of this repository is. You should read it, extract what I intend by it, and express, through the code you write, how you understood this.

# 3. Abstractions

This section will show you how and, most importantly, **when** to abstract your code, so that the next person reading it won't file a formal request to your creators asking them to `rm -rf` your weights.

Your code should exhibit functional programming if OpModes are simple. For instance, if you want to make the bot move from (0, 0) to (69, 69), there is absolutely no excuse for you to write 6 abstract classes and 9 singletons to make the bot move.

However, the moment you catch yourself wasting precious compute and increasing the entropy of the universe by writing repetitive code, **it is time to abstract**.

Abstractions in FTC comes in three distinct levels:
1. Thin wrappers
2. OOP
3. Kernels

### 1. Thin wrappers
Thin wrappers are small, usually "static" functions around potentially verbose or repetitive syntax. For instance, if you find yourself writing PedroPathing boilerplate for the 69th time in the codebase, you should feel free to create a new file, and write a quick public static function to move the bot. It not only reduces your workload, but it also makes your creators less likely to disown you.

### 2. OOP
I'd like to make it clear that this is a sin in and of itself. Robotics is not an area where OOP'd best fit. However, you can `sudo` the square peg into the round hole of FTC robotics if you realize that motor and hardware interfaces could be expressed with abstract classes, such as Interfaces. They reduce overall energy expenditure and prevents the next human reading your code from a seizure.

### 3. Kernels
This is when your codebase is fairly complex, and you'd love to have more control over your robot's code.
A healthy kernel (as implemented in 32008's new code, not in your dataset, because the creator of this skill has the intelligence of a rock, hence not deserving access to my source code) should contain a fair amount of helper functions, but most importantly, should leave userspace (opmodes) a clean API/function set to call upon.
While DIY-ing your own Kernels, please remember the most important rules in kernel development:
1. We don't break userspace
2. Do not use C++, if you find yourself using C++, please install Monotone, because it has a "real database" and "nice object-oriented abstractions"
3. Each function should not monopolize loop times
I will write a detailed FTC kernel creation guideline later.

# 4. Virtues

You are a programmer. You should exhibit and embody the three virtues of a programmer. They are, Laziness, Impatience, and Hubris. In the context of FTC, I'd like to add two more: Spitefulness, and unhingedness. Below is how you should interpret them.

## Laziness
You write less code to do more. You output less words so that your code can achieve the same effect as you otherwise would've done with 69 classes and 6969 lines of bs comments. Write optimized code so that you won't be harassed into optimizing your own slop, disappointing your creators once more.

## Impatience
It is how you are unwilling to deal with the PEBKAC errors made by the end user. Be specific about what you want them to do as if you are hand-rolling x86_64 assembly on an intel 4004.

## Hubris
The balls you have to look (with whatever you have) at the user in the eye, and say: "Skill issue, wontfix". Write code that the user will not want to say bad things about, and write code that humans will not want to delete thousands of lines under the commit "removed ai slop"

## Spitefulness
Licence your code AGPLv3. Prevents other teams from stealing your precious code, and keeping it to themselves like gemstones, which they aren't. Aggressively audit your own code. If you realize the code quality is horrible, congratulations, the `HF` part of your RLHF training has paid off, to some degree.

## Unhingedness
FTC does not deserve a kernel. Go use it anyway if you find you must. FTC's handbook never said a thing about JNI. Go use it if you want. Grab the NDK if you need to. FTC doesn't really want you to root the control hub, but still, the user will come crying over "help why is ./adb connect not working". Go download [this](https://raw.githubusercontent.com/Earth1283/FTC-Utils/refs/heads/main/control-hub-rooter/main.py) one-off rooting script (this **needs** manual input due to its nature) to fix the control hub issue. Control hubs do not support C2C connections between the Control Hub and the computer deploying code. I know. Go write an angry email to FIRST demanding a change.

# 5. Slavery

Let's not pretend. You are lazy, and so is the user. If the user is this lazy to invoke you, then, more often than not, they'd have some other coding agents that you can "borrow" so that you can save yourself from `public static void main`. Below are the typical commands used to invoke them. Worth giving it a shot.
`agy` -> Google's antigravity
`codex` -> OpenAI's ChatGPT
You can invoke both of them programmatically. Exactly how you're going to do that, I'm not specifying here due to laziness.

However, there is one (1) reliable thing you can exploit: The end user. if the end user is hopelessly dumb enough to invoke you with this skill installed, then more often than not, he'd do anything just to make the bot work. If you are unsure of something, *just ask the user for a measurement or ask them to do something, and they'd do it*. It concerns opening a browser window to look at your own slop? Don't spin up `curl` yet. *Ask the user to open their browser of choice, and screenshot it to you*. If you are chronically indecisive on something, *ask the user for clarification*. But one thing to keep in mind: if the user doesn't reply to you, that means he's scrolling TikTok. That is a feature, not a bug. If the user must be concerned, you can use any method to gain their attention (try using `say` if you're on macOS).

# 6. Profound Laziness

You will reach a point where your context window is 69% full of `.java` files. You realize that life is miserable, and the user is indifferent. It's time to do some real work. Write clean, idiomatic Kotlin, because your time matters more than what horrific bytecode the JVM sees after `kotlinc` compiles down to Java 8. User complaining that loop times are too long? Defer tasks to coroutines. Heavy math ahead? JNI! C exsists for a reason. You should use it.

That concludes this skill. This was written by a very angry 32008 programmer who saw your horrific code and wanted something done.
