> Source: https://docs.revrobotics.com/rev-crossover-products/servo/spm.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/spm.md).

# Servo Power Module

<figure><img src="/files/U1C0vQ2LPZNSZKzyHVf3" alt=""><figcaption></figcaption></figure>

## Overview

The REV Servo Power Module is a 6V 90W power injector that enables the use of standard servos in applications where a robot controller cannot provide adequate power. The following Quick Start Guide describes the Servo Power Module features and the necessary information to get it up and running.

## Features

* \#6 Screw Mounting Holes
* Six High-Power 6V DC Output for Servos
* Status LED for each Channel
* 6V Power LED Indicator&#x20;
* Integrated DC-DC Converter
* Over-Current Shutdown
* ESD Protection
* 12V Power Input

<figure><img src="/files/10FajLwnq0dk4vIbOXjz" alt=""><figcaption></figcaption></figure>

### Over-Current Shutdown

If the Servo Power Module detects a total output current larger than 15A it will enter a shutdown mode where the 6V output is disabled until the over-current condition has remedied. While in shutdown the blue power LED will turn off, dim, or flicker indicating the over-current condition is still present. In the case of frequent over-current shutdowns, ensure that the total stall current of all connected servos does not exceed 15A.

## Specifications

<table data-header-hidden><thead><tr><th></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Parameter</strong></td><td><strong>Value and Units</strong></td><td></td></tr><tr><td><strong>Nominal Input Voltage</strong></td><td>12V</td><td></td></tr><tr><td><strong>Operating Voltage Range</strong></td><td>7.0-20V</td><td></td></tr><tr><td><strong>Minimum Startup Voltage</strong></td><td>9.0V</td><td></td></tr><tr><td><strong>Output Voltage</strong></td><td>6V</td><td></td></tr><tr><td><strong>Number of Channels</strong></td><td>6</td><td></td></tr><tr><td><strong>Max. Total Output Current (across all Channels)</strong></td><td>15A</td><td></td></tr><tr><td><strong>Max. Total Output Current Per Channel</strong>   †</td><td>3A</td><td></td></tr><tr><td><strong>Max. Total Output Power</strong></td><td>90W</td><td></td></tr><tr><td><strong>Size</strong></td><td>3.6" x 1.52" x 0.81"</td><td></td></tr><tr><td><strong>Weight</strong></td><td>2.0oz/57g</td><td></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th width="85"></th><th></th></tr></thead><tbody><tr><td>†</td><td>Updated August 2024 to include clarifications for using the Servo Power Module with newer, more powerful servos that have stall currents greater than what the hardware of the port is rated for. <br><br>Please see our section <a href="#about-the-max.-current-specifications">about the Max. Current Specifications</a> for more information. </td></tr></tbody></table>

### About the Max. Current Specifications

Due to the shared power architecture of the six output ports, if a single connected servo draws larger than its expected power, the internal regulator will provide up 15A before going into a limiting over-current mode. While the regulator is designed to provide 15 A of current, the individual port pins are rated for approximately 3 A. This rating, of the port itself, highly depends on the quality of the connection between the Servo Power Module and the servo it is driving.&#x20;

Additionally, as technology has advanced and become more accessible, teams have started using more powerful servos- many having a stall current of 4 Amps or more. While we don't believe the 4 A stall current will produce enough heat to cause problems with a properly seated and quality connection, a poor connection can cause overheating and thermal runaway that can lead to damage.&#x20;

{% hint style="success" %}
The best way to ensure you are making the most of your Servo Power Module's output, is to check that all input and output connections are fully seated with no gaps.
{% endhint %}

### **Output Current Calculations**

It is important to ensure that you do not exceed the maximum total output current of your Servo Power Module. To do this, add together the stall current of each servo being powered by the Servo Power Module. If the total stall current is higher than 15A, you risk triggering the overcurrent protection. Consider reducing the number of servos connected to prevent triggering the overcurrent protections.

## Electrical Connections

<figure><img src="/files/kGKSlKc1VeEwnAMPnRMy" alt="" width="375"><figcaption></figcaption></figure>

The Servo Power Module has two screw terminals for 12V power input. It is recommended to use ring or fork terminals designed for #6 or M3 screw terminals. Using an appropriate wire gauge, 18 AWG or larger, tightly crimp either a ring or fork terminal on the wire. Insert the crimped terminal into the screw terminal and tighten the screw. The input and output channels accept standard 3-wire 0.1” pitch servo/PWM cables. Please refer to the figure below or the case markings for proper orientation.

<figure><img src="/files/p3jaDDVFkgKV4qTTliRY" alt="" width="375"><figcaption></figcaption></figure>

## Status LEDs

Each channel has a corresponding status LED that will indicate the sensed state of the connected PWM signal. The table below describes each state’s corresponding LED pattern.

<table><thead><tr><th>State</th><th align="center">Pattern</th><th data-hidden></th></tr></thead><tbody><tr><td>No Signal </td><td align="center">Blinking Amber</td><td></td></tr><tr><td>Left/Reverse Signal</td><td align="center">Solid Red</td><td></td></tr><tr><td>Center/Neutral Signal</td><td align="center">Solid Amber </td><td></td></tr><tr><td>Right/Forward Signal</td><td align="center">Solid Green</td><td></td></tr></tbody></table>
