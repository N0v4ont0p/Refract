> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/features/util.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.util;
---

# Utility Functions

FTCLib comes with many different Utility Functions:

* [Look Up Tables](https://docs.ftclib.org/ftclib/features/util#what-is-a-look-up-table)
* [Timing Functions](https://docs.ftclib.org/ftclib/features/util#timing-functions)
* [Math Utilities](https://docs.ftclib.org/ftclib/features/util#math-utilities)
* [Directional Enums](https://docs.ftclib.org/ftclib/features/util#directional-enums)

## What is a Look Up Table?

A look up table or LUT for short is used to store values and be able to quickly recall them.

The FTCLib provides 2 different variations of look up tables. In this year's game they can be used to store different set and tested velocities or angles. You can either retrieve the closest reference or you can interpolate through them.

## LUT \(Look Up Table\)

Provides a way to store values in a table to quickly retrieve them. For example, this might be used to store different speeds or angles based on certain distances. This class allows you to find the closest entry to the input.

For example if you enter:

| Input | Output |
| :---: | :---: |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |

When you request 1.1, it will return 1.

### Example Usage:

```java
import com.arcrobotics.ftclib.util.LUT;

LUT<Double, Double> speeds = new LUT<Double, Double>()
{{
    add(5.0, 1.0);
    add(4.0, 0.9);
    add(3.0, 0.75);
    add(2.0, 0.5);
    add(1.0, 0.2);
}};

double distance = odometry.getPose().getTranslation().getDistance(new Translation2d(5, 10));
shooter.set(speeds.getClosest(distance));
```

## InterpLUT \(Interpolated Look Up Table\)

Provides a way to fill in the gaps in the data. Similarly to the LUT above, this allows you to add data points and retrieve a data point given an output. The difference between a normal LUT and InterpLUT is that the interpolated LUT uses math to fill in all the gaps. Effectively generating filler data based on the data around it.

### Example Usage:

```java
import com.arcrobotics.ftclib.util.InterpLUT;

//Init the Look up table
InterpLUT lut = new InterpLUT();

//Adding each val with a key
lut.add(1.1, 0.2);
lut.add(2.7, .5);
lut.add(3.6, 0.75);
lut.add(4.1, 0.9);
lut.add(5, 1);
//generating final equation
lut.createLUT();

double distance = odometry.getPose().getTranslation().getDistance(new Translation2d(5, 10));
shooter.set(lut.get(distance));

//getting the velo required and passing it to the shooter.
```

## Timing Functions

FTCLib Comes with multiple timers and Timing Functions. They let you set the length, unit, can act as a stopwatch or even return the loop time.

### Timer

A timer can be created with a length or length and Time Unit. The various functions nested within the Timer object are:

| Function | Return Type | Description |
| :--- | :--- | :--- |
| `timer.start()` | Void | Starts the Timer |
| `timer.pause()` | Void | Pauses the Timer |
| `timer.resume()` | Void | Resumes the Timer |
| `timer.elapsedTime()` | long | Returns the Passed Time |
| `timer.remainingTime()` | long | Returns Time Left |
| `timer.done()` | Boolean | Returns if the Timer is Completed |
| `timer.isTimerOn()` | Boolean | Returns if the Timer is Active |

## Math Utilities

FTCLib currently adds 1 math utility, clamp. It lets you restrict a value to a certain max and min and is usable in double and int.

**Example Usage:**

Double Method:

```java
import com.arcrobotics.ftclib.util;

double ValueToClamp;
double LowestPossibleValue;
double HighestPossibleValue;

double OutputVal = clamp(ValueToClamp,
                         LowestPossibleValue,
                         HighestPossibleValue);
```

Int Method:

```java
import com.arcrobotics.ftclib.util;

int ValueToClamp;
int LowestPossibleValue;
int HighestPossibleValue;

int OutputVal = clamp(ValueToClamp,
                         LowestPossibleValue,
                         HighestPossibleValue);
```

## Directional Enums

FTCLib comes with multiple directional enums for all your directional needs! You can use these for any autonomous or TeleOP States or anything you want!

| Direction | Index |
| :--- | :--- |
| LEFT | 0 |
| RIGHT | 1 |
| UP | 2 |
| DOWN | 3 |
| FORWARD | 4 |
| BACKWARDS | 5 |

You can find some examples in the [sample folder](https://github.com/FTCLib/FTCLib/tree/v1.1.2/examples/src/main/java/com/example/ftclibexamples).

