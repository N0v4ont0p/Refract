> Source: https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/troubleshooting.md).

# Troubleshooting

## Troubleshooting Guide

This troubleshooting guide helps diagnose and resolve issues with the REV Servo Hub.&#x20;

## Power Issues

If the Servo Hub is unresponsive (no lights):

1. **Check Power Supply**:
   * Verify the power supply provides sufficient voltage (6–12V recommended).
   * If using a REV PDH, check the breaker for the channel powering the Servo Hub.<br>
2. **Inspect Wiring**:
   * Ensure all wires are securely connected.
   * Perform a tug test on the power connections.<br>
3. **Enter Recovery Mode**:
   * If the Servo Hub has power but no LEDs light up, follow the recovery mode instructions below.

### Overcurrent Faults

The Servo Hub protects itself and the connected servos from overcurrent conditions. There are two types of overcurrent faults:

1. [Channel Overcurrent Fault](#channel-overcurrent-fault)
2. [Total Device Overcurrent Fault](#total-device-overcurrent-fault)

### Channel Overcurrent Fault

**Condition**: A channel exceeds 6A for a prolonged period or experiences short spikes above 7A.

**Indicators**: Channel LED blinks amber at a high frequency and/or power to the affected channel is removed.

**Resolution**:

1. Remove the load from the servo.
2. Allow the current to drop to clear the fault.

### Total Device Overcurrent Fault

**Condition**:  The total current across all six channels exceeds 15A.

**Indicators**: All channel LEDs blink amber at a high frequency and/or power to all channels is removed.

**Resolution**:&#x20;

1. Disconnect servos and inspect for faults or excessive current draw.
2. Ensure no channel is shorted.
3. The fault will clear 1 second after the total current drops below 15A.

**Common Causes**:

* Overcurrent faults may indicate excessive load or a servo malfunction. Disconnect and test the servos individually.
* Stalled high-power servos (e.g., Axon Max with a stall current of \~4A).
* Shorts in servo wiring.43

### Low Battery Warnings

The Servo Hub will alternate between **blue** and **orange** on the main status LED when the input voltage is low:

* **Low Voltage Threshold**: Below 5.5V.
* **Clearing Voltage**: Above 6.5V.

**Resolution**:

* Check the voltage of the battery powering the Servo Hub and recharge if needed.
* Ensure connections to the battery are secure.
* Low voltage can cause unexpected behavior.

### CAN Bus Faults

A CAN fault occurs when the Servo Hub detects unreliable communication on the CAN bus. The main status LED will alternate between **yellow** and **orange**.

### **Troubleshooting Steps**:

1. **Inspect Wiring**:
   * Perform a tug test to ensure connections are secure.
   * Verify there’s enough bare wire in the Wago connectors.
2. **Check Termination Resistors**:
   * Ensure proper termination at both ends of the CAN bus.
3. **Test for Shorts**:
   * Inspect for shorts in the CAN wiring.

## No Connection Detected

When the Servo Hub cannot detect a connection to a controller or the REV Hardware Client, the main status LED will flash magenta.

### **Troubleshooting Steps**:

1. **Check the Hardware Client**:
   * Open the REV Hardware Client and ensure it recognizes the Servo Hub.<br>
2. **Check CAN Connection**:
   * Verify the CAN bus wiring.
   * Use the Hardware Client to check if other devices on the CAN bus are visible.<br>
3. **Inspect roboRIO:**
   * Ensure the roboRIO has power.
   * Verify the roboRIO configuration and connections.

## Servo and Channel Issues

### Servo Not Responding

* Ensure the channel is enabled (LED is not blinking amber).
* Check the servo wiring for loose connections or damage.
* Verify the servo is compatible with the configured pulse width range.

### Erratic or Unstable Servo Movement

* Inspect the Disable Behavior configuration:
* Some servos may jitter or misbehave when powered but not receiving a signal. Consider using `kDoNotSupplyPower`.
* Test with another servo to rule out hardware issues.

### Channel LED Does Not Light Up

* If the channel LED is off, verify the channel is properly configured in the program.
* Check wiring and servo functionality.
* Test with another servo to confirm channel operation.

## Software Issues

### Unable to Configure Multiple Servo Hubs to use with a Control Hub&#x20;

* Double check that each Servo Hub has a [unique CAN ID](/rev-crossover-products/servo/servo-hub/configuring-the-servo-hub-with-a-control-hub.md#accessing-the-configuration-utility) by connecting it via USB to the REV Hardware Client&#x20;
* Servo Hubs must have a different ID than an Expansion Hub. Expansion Hubs default to ID 1 or 2

### Servo Hub is not Appearing in the Configuration Menu

{% hint style="info" %}
You must be running Robot Controller App AND Driver Station App version 10.0 to use a Servo Hub.
{% endhint %}

* Check first that the Servo Hub is receiving proper power and that the RS485 cable is secure
* Double check that each Servo Hub has a [unique CAN ID](/rev-crossover-products/servo/servo-hub/configuring-the-servo-hub-with-a-control-hub.md#accessing-the-configuration-utility) by connecting it via USB to the REV Hardware Client&#x20;
* Servo Hubs must have a different ID than an Expansion Hub. Expansion Hubs default to ID 1 or 2&#x20;

### Unable to set the CAN ID/CAN ID not Saving on the Servo Hub

When a Servo Hub is connected to a Control Hub, directly or through another Hub, it will be set to a "read-only" mode when interacting with the REV Hardware Client. This means the Client cannot update the ID or firmware, and features, such as the ability to run servos, will not be available.&#x20;

* Power down the robot or disconnect the RS845 cable leading to the Servo Hub
* Power cycle the Servo Hub
* You should now be able to connect the Servo Hub via USB-C to the REV Hardware Client to set the ID or use the Client features

### Driver Hub Showing "Servo Hub not currently responding to commands" Error

<figure><img src="/files/hRkdAQewNq7GvJblBk9M" alt=""><figcaption></figcaption></figure>

This error appears if the Control Hub has lost communication with a Servo Hub that was previously established in the configuration file

* Double check the Servo Hub is receiving proper and securely wired
* If the Servo Hub ID has been changed or a different Servo Hub with a different ID has been connected as a substitute:&#x20;
  * Change the [Servo Hub ID](/rev-crossover-products/servo/servo-hub/configuring-the-servo-hub-with-a-control-hub.md#accessing-the-configuration-utility) to match the one in the configuration OR
  * Create a new configuration file with the updated ID

If you are removing the Servo Hub completely, create a new configuration file.

### Driver Hub showing "Addresses higher than 10 are reserved for system use" warning

<figure><img src="/files/dDNgoeaFtfA9WdYTXXyW" alt=""><figcaption></figcaption></figure>

Change the [Servo Hub's ID](/rev-crossover-products/servo/servo-hub/configuring-the-servo-hub-with-a-control-hub.md#accessing-the-configuration-utility) to between 1-10 to avoid potential conflicts. Expansion Hubs default to having ID 1 or 2.&#x20;

### Servo Hub Appearing as an Expansion Hub in the REV Hardware Client

When connecting over USB-C to a Control Hub with a Servo Hub connected it will appear as an Expansion Hub within the Client as seen below:

<figure><img src="/files/IJCOEspo0zjXGcrK4k4T" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/UCx2kelBUzjW09n2FmYl" alt=""><figcaption></figcaption></figure>

This is expected behavior as of RHC Version 1.7.0. To update the Servo Hub, disconnect it from the Control Hub and power cycle it before connecting only the Servo Hub via USB-C.

## Firmware Recovery Mode

If the Servo Hub is unresponsive, use recovery mode to restore functionality.

**Steps to Enter Recovery Mode**:

1. Power off the Servo Hub.
2. Press and hold the mode button on the Servo Hub.
3. While holding the button, power on the Servo Hub.
4. Release the button once the channel 4 red LED and channel 5 green LED are on.

The Servo Hub will now be ready to recover via the REV Hardware Client.

***

By following this guide, users can diagnose and resolve most common issues with the REV Servo Hub. If problems persist, contact REV Robotics support for further assistance.
