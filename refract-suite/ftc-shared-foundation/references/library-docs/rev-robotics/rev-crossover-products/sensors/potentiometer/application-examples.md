> Source: https://docs.revrobotics.com/rev-crossover-products/sensors/potentiometer/application-examples.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-crossover-products/sensors/potentiometer/application-examples.md).

# Application Examples

## Application Information

Potentiometers are most commonly used to measure the angle of an arm type joint. There are two different ways to utilize a potentiometer when using it in conjunction with an arm. One way to use the potentiometer is to directly place it on the shaft being used to pivot the arm. However, placing the potentiometer on an adjacent shaft that connects to the pivot-point shaft, via gears or chain, allows for more design flexibility.&#x20;

Applying the concept of gear ratios (or sprocket ratios) to the potentiometer; it is possible to manipulate the accuracy/range of motion relationship. When the range of motion increases, through changes in gear ratio, accuracy decreases, and vice versa.&#x20;

This Potentiometer has a 5mm female hex socket input and can be used with any 5mm hex axle, like the ones in the REV Building System.  There are six M3 tapped holes around the input shaft on a 16mm circle which will mount to any of the REV Robotics Motion Brackets.

#### Calculating the relationship between voltage and angle&#x20;

The REV Potentiometer has a linear\* relationship between the output voltage and the angle of its shaft.

{% hint style="info" %}
\*When used in FTC applications, the Hub's analog circuitry changes the linearity of the potentiometer. Skip ahead to the FTC Applications section for more information.
{% endhint %}

Assuming a 3.3V input voltage, the degrees per volt can be graphed and calculated as follows:

<figure><img src="/files/C02ny4vZVqUdv0XUQLOx" alt=""><figcaption></figcaption></figure>

$$
\frac{270^{\circ}}{3.3V}=\frac{81.8^{\circ}}{1V}: or;\frac{0.0818^{\circ}}{1mV}
$$

Therefore, given a measured output voltage V in volts, you can easily calculate the corresponding angle θ in degrees:

$$
\theta= V\_{\textit{OUT}}\times81.8
$$

### FTC Applications&#x20;

Even though the Potentiometer is a linear taper potentiometer, the analog circuitry on the Control/Expansion Hubs can change the linearity so that the above equations are not as accurate. Therefore, it is recommended to move your robot mechanisms to specific positions of interest and record the Potentiometer voltage at those positions to use in your code.

Calculating the output voltage for a specific angle θ between 0 and 270° is still possible, but the equation is no longer linear:

$$
V\_\textit{OUT}=\frac{445.5(\theta-270)}{\theta^2-270\theta-36450}
$$

#### Configuring in the Control System&#x20;

Configure the Potentiometer as "Analog Input" as shown in the image below.&#x20;

<figure><img src="/files/aOfcTEqjVLNDdns2hzsW" alt=""><figcaption></figcaption></figure>

In this example, the Potentiometer is configured on port 0. It is touched on briefly in the[ Pinout Section ](/rev-crossover-products/sensors/magnetic-limit-switch/specs.md#pinout-and-schematic)that the Potentiometer only sends a signal to the Control Hub through the n communication channel. Because of this limitation, the Potentiometer will only work when configured port 0 and port 2.

#### Programming Applications

This program has a variable called CurrentVoltage that is used to store the current voltage. CurrentVoltage is updated using the AnalogInput block every time that the program loops. When CurrentVoltage less than the midpoint of 1.65 volts, the motor stops. When the voltage is higher than the midpoint, the motor moves. The potentiometer voltage is also displayed via telemetry.

{% tabs %}
{% tab title="Blocks" %}

<figure><img src="/files/yEq4nVN7s0mggsLwYzGs" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="OnBot Java" %}
{% hint style="info" %}
The code assumes that a Potentiometer was configured with the name “potentiometer”, and that a motor was configured with the name “test\_motor”.
{% endhint %}

```java
package org.firstinspires.ftc.teamcode;
 
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.AnalogInput;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
 
@TeleOp
public class PotentiometerTest extends LinearOpMode {
    // Define variables for our potentiometer and motor
    AnalogInput potentiometer;
    DcMotor test_motor;
 
    // Define variable for the current voltage
    double currentVoltage;
 
    @Override
    public void runOpMode() {
        // Get the potentiometer and motor from hardwareMap
        potentiometer = hardwareMap.get(AnalogInput.class, "potentiometer");
        test_motor = hardwareMap.get(DcMotor.class, "test_motor");
        
        // Loop while the Op Mode is running
        waitForStart();
        while (opModeIsActive()) {
            // Update currentVoltage from the potentiometer
            currentVoltage = potentiometer.getVoltage();
            
            // Turn the motor on or off based on the potentiometer’s position
            if (currentVoltage < 1.65) {
                test_motor.setPower(0);
            } else {
                test_motor.setPower(0.3);
            }
 
            // Show the potentiometer’s voltage in telemetry
            telemetry.addData("Potentiometer voltage", currentVoltage);
            telemetry.update();
        }
    }
}
```

{% endtab %}
{% endtabs %}
