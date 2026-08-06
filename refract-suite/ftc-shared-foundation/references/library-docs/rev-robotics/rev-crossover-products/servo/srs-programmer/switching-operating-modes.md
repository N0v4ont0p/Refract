> Source: https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/srs-programmer/switching-operating-modes.md).

# Switching Operating Modes

Out of the box, the SRS operates as a 270° servo. However, the [REV SRS Programmer](/rev-crossover-products/servo/srs-programmer.md) can reconfigure the SRS to set angular limits or switch it into a continuous rotation mode. The SRS Programmer has several operating modes for configuring and testing the [REV Smart Robot Servo](/rev-crossover-products/servo/srs-programmer.md). The following sections describe each operating mode in detail.

## Switching Operation Modes

### Default Operation&#x20;

The default range for the SRS is 270°. This range is mapped to an input pulse range of 500μs to 2500μs with 1500μs as the center point. The image below describes the pulse-to-angle relationship.

<figure><img src="/files/XaFThCzlVy1K64MW3G22" alt=""><figcaption></figcaption></figure>

### Continuous Rotation&#x20;

The SRS can be configured with the SRS Programmer to operate in a continuous rotation mode. In this mode, the same input pulse range is mapped to direction and speed. The table below lists the pulse mapping for direction and speed.

<figure><img src="/files/783QDQErMOiVlysfzT9r" alt=""><figcaption></figcaption></figure>

### Switching Modes

Follow the steps below to switch a REV Smart Robot Servo between Continuous Mode and Servo Mode. The figure below shows the process to select Continuous Mode.

<figure><img src="/files/EBSBSzMJIBgvgKV4TOG3" alt=""><figcaption></figcaption></figure>

1. Connect the SRS to the programmer.
2. Turn on the programmer.
3. Slide the mode switch to the desired mode: C - Continuous, S - Servo.
4. Press and release the PROGRAM button once.
5. The PROGRAM LED should blink and then stay solid indicating success.

## Angular Limits&#x20;

The SRS can be easily configured with the SRS Programmer to limit right and left motion at two user-defined angles. Input pulses that occur past the limits will be ignored and the SRS will hold the limit angle. Any two angles can be set as limits as long as the left limit is left of the center dead band and the right limit is to the right of the center dead band. The table below shows the valid regions for left and right limits.

<figure><img src="/files/hx9NrKuRppvmYrlcg1EA" alt=""><figcaption></figcaption></figure>

Once valid limits are programmed, the SRS will ignore any pulses that exceed the limits and hold the limit angle. For example, the image below exhibits what would happen a left limit of -30° and a right limit of +60° was set.

<figure><img src="/files/E0np4jCLUCRM49gQXlgs" alt=""><figcaption></figcaption></figure>

### Setting Angular Limits&#x20;

Follow the steps below to set the angular limits for the Servo Mode. The figure below shows an example of setting a left and right limits at -54° and +81° respectively.

![](https://lh6.googleusercontent.com/yu5tUI3NEQlaA8nm237DzEhpCKl7SZXJ_BmKHp0iZNgbybnyRjp2KW8q4NQ0SbtDhCwIbZnGk2KX2Et0jKxX3rbvXfVzQ3OhD0Mg_BBHk7wu0FNE133EVthtRjyfJlsAhw)

Start with the SRS already configured in Servo Mode, see section [Switching Modes](#switching-operation-modes) for instructions.

1. Connect the SRS to the programmer.
2. Turn on the programmer.
3. Slide the mode switch to S position.
4. This step is optional, but recommended to make it easier to see the valid limit ranges. Please refer to the SRS User's Manual for more information about the valid limit ranges.
   1. Press and release the TEST button twice to enter Manual Test Mode (see [Test Modes](#test-modes) for more information).
   2. Press the PROGRAM button to center the servo at 0°.
   3. Press and release the TEST button once to leave the test mode.
5. Manually rotate the servo to the desired left limit position.
6. Press and release the LEFT button. The LEFT LED will illuminate if the position is valid.
7. Manually rotate the servo to the desired right limit position.
8. Press and release the RIGHT button. The RIGHT LED will illuminate if the position is valid.
9. After both limits are set, press and release the PROGRAM button. The PROGRAM LED should blink and then stay solid indicating success.

## Resetting to Default&#x20;

Follow the steps below to reset the Smart Robot Servo to its default mode and limits. The figure below shows the process to reset to defaults.

<figure><img src="/files/IEsWD9ZZY18pN6CCMhZA" alt=""><figcaption></figcaption></figure>

1. Connect SRS to the programmer.
2. Turn on the programmer.
3. Slide the mode switch to S position.
4. Press and hold the PROGRAM button for at least 5 seconds.
5. The LEDs will blink and then the PROGRAM LED will stay solid indicating success.

## Test Modes

In either Continuous or Servo Modes, pressing and releasing the TEST button cycles through the two test modes:

* 1st press - Automatic Sweep Mode
* 2nd press - Manual Test Mode
* 3rd press - Return to default state

The section below will cover the two different test modes.

{% tabs %}
{% tab title="Automatic Sweep Mode" %}
In Automatic Sweep Mode, the SRS Programmer will automatically sweep the SRS through motions appropriate for its configuration. the table below describes the behavior based on the configured mode.

| **Servo and Programmer Mode** | **Behavior**                 |
| ----------------------------- | ---------------------------- |
| **Continuous Mode (C)**       | Sweeping direction and speed |
| **Servo Mode (S)**            | Sweeping between limits      |
| {% endtab %}                  |                              |

{% tab title="Manual Test Mode" %}
In Manual Test Mode the LEFT, PROGRAM, and RIGHT buttons control the movement of the SRS. The table below describes how the SRS will behave based on the configured mode.

<figure><img src="/files/pxHLDS0sExxlbQZ1bNva" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Power-off Reminder

If the SRS Programmer is left on for an extended period of inactivity, it will blink every LED as a reminder to shut off power.

## How to Video

{% embed url="<https://youtu.be/PJjFdsnw0uY?feature=shared>" %}
