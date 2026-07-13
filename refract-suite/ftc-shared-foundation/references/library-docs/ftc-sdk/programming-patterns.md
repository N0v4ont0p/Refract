> Source: https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pid_coefficients/pid-coefficients.html · Fetched: 2026-07-12
> Source: https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pidf_coefficients/pidf-coefficients.html · Fetched: 2026-07-12

# Programming Patterns: PID / PIDF Motor Control

The REV Robotics Control Hub and Expansion Hub let you change the PID/PIDF coefficients used for closed-loop motor control. Coefficients are specific to each motor channel and `RunMode`.

**Persistence limitation:** "Changes made to the PID[F] coefficients do not persist if you power cycle the REV Robotics Control Hub or REV Robotics Expansion Hub." To preserve changes across power cycles, store the state information on the Control Hub or Android device and re-apply it at OpMode init.

**SDK note:** As of SDK 7.0, the former PID-only methods remain available but are deprecated in favor of the PIDF implementations.

## Method 1: Using `DcMotorEx`

The extended `DcMotorEx` class provides `getPIDFCoefficients()` / `setPIDFCoefficients()` (and the older `getPIDCoefficients()` / `setPIDCoefficients()`), unavailable on the plain `DcMotor` class.

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.PIDFCoefficients;

@Autonomous(name="Concept: Change PIDF", group = "Concept")
public class ConceptChangePIDF extends LinearOpMode {

    DcMotorEx motorExLeft;

    public static final double NEW_P = 2.5;
    public static final double NEW_I = 0.1;
    public static final double NEW_D = 0.2;
    public static final double NEW_F = 0.5;

    public void runOpMode() {
        motorExLeft = (DcMotorEx)hardwareMap.get(DcMotor.class, "left_drive");

        waitForStart();

        PIDFCoefficients pidfOrig = motorExLeft.getPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

        PIDFCoefficients pidfNew = new PIDFCoefficients(NEW_P, NEW_I, NEW_D, NEW_F);
        motorExLeft.setPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER, pidfNew);

        PIDFCoefficients pidfModified = motorExLeft.getPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

        while(opModeIsActive()) {
            telemetry.addData("Runtime (sec)", "%.01f", getRuntime());
            telemetry.addData("P,I,D,F (orig)", "%.04f, %.04f, %.04f, %.04f",
                    pidfOrig.p, pidfOrig.i, pidfOrig.d, pidfOrig.f);
            telemetry.addData("P,I,D,F (modified)", "%.04f, %.04f, %.04f, %.04f",
                    pidfModified.p, pidfModified.i, pidfModified.d, pidfModified.f);
            telemetry.update();
        }
    }
}
```

Steps: cast the motor to `DcMotorEx` → read current coefficients via `getPIDFCoefficients()` → build a new `PIDFCoefficients` object → apply via `setPIDFCoefficients()` → verify by re-reading.

## Method 2: Using `DcMotorControllerEx`

"The actual change of the PIDF coefficients occurs on the motor controller that is controlling the selected motor." This method adjusts coefficients directly through the controller rather than the motor object.

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorControllerEx;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.PIDFCoefficients;

@Autonomous(name="Concept: Change PIDF Controller", group = "Concept")
public class ConceptChangePIDFController extends LinearOpMode {

    DcMotor motorLeft;

    public static final double NEW_P = 2.5;
    public static final double NEW_I = 0.1;
    public static final double NEW_D = 0.2;
    public static final double NEW_F = 0.5;

    public void runOpMode() {
        motorLeft = hardwareMap.get(DcMotor.class, "left_drive");

        waitForStart();

        DcMotorControllerEx motorControllerEx = (DcMotorControllerEx)motorLeft.getController();

        int motorIndex = ((DcMotorEx)motorLeft).getPortNumber();

        PIDFCoefficients pidfOrig = motorControllerEx.getPIDFCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER);

        PIDFCoefficients pidfNew = new PIDFCoefficients(NEW_P, NEW_I, NEW_D, NEW_F);
        motorControllerEx.setPIDFCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER, pidfNew);

        PIDFCoefficients pidfModified = motorControllerEx.getPIDFCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER);

        while(opModeIsActive()) {
            telemetry.addData("Runtime (sec)", "%.01f", getRuntime());
            telemetry.addData("P,I,D,F (orig)", "%.04f, %.04f, %.04f, %.04f",
                    pidfOrig.p, pidfOrig.i, pidfOrig.d, pidfOrig.f);
            telemetry.addData("P,I,D,F (modified)", "%.04f, %.04f, %.04f, %.04f",
                    pidfModified.p, pidfModified.i, pidfModified.d, pidfModified.f);
            telemetry.update();
        }
    }
}
```

Steps: get a reference to the motor's controller as `DcMotorControllerEx` → get the motor's port number via `((DcMotorEx)motor).getPortNumber()` → call the controller-level `getPIDFCoefficients(motorIndex, runMode)` / `setPIDFCoefficients(motorIndex, runMode, coeffs)` → verify by re-reading.

Both approaches target the same underlying motor-controller mechanism; choose based on whether your code already holds a `DcMotorEx` reference or needs to go through the controller.
