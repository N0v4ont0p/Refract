> Source: https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/android_studio/creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio).html · Fetched: 2026-07-12
> Source: https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/onbot_java/creating_op_modes/Creating-and-Running-an-Op-Mode-(OnBot-Java).html · Fetched: 2026-07-12

# OpMode Basics (Creating and Running an OpMode)

## What's an OpMode?

During _FIRST_ Tech Challenge matches, robots perform tasks to score points. Teams write programs called "OpModes (operational modes)" to specify robot behavior. These run on the Robot Controller after selection on the Driver Station. An OpMode functions as "a list of tasks for the Robot Controller to perform." For `LinearOpMode` types, the controller processes tasks sequentially.

## TeamCode Module (Android Studio)

The Android Studio project includes a module named `TeamCode` used to build a custom Robot Controller app. Place custom classes and OpModes in the `org.firstinspires.ftc.teamcode` package within the TeamCode module — this package is reserved for custom code.

Javadoc reference: https://javadoc.io/doc/org.firstinspires.ftc

Enable Android Studio's auto-import feature (Editor → General → Auto Import, check "Add unambiguous imports on the fly") to save time during OpMode development.

Sample OpModes are located in the FtcRobotController module under `org.firstinspires.ftc.robotcontroller.external.samples`. To use a sample, copy it to `org.firstinspires.ftc.teamcode` and change `@Disabled` to `//@Disabled`.

## The OnBot Java Programming Tool

OnBot Java is "a user-friendly programming tool that is served up by the Robot Controller phone." Users write Java op modes that compile quickly on the Robot Controller and load dynamically at runtime. Access it via a JavaScript-enabled browser connected to the Robot Controller's Program & Manage wireless network (works on Windows, Mac, Chromebook, iPad).

To create a new file in OnBot Java: press "+" in the project browser, name the file, choose the "BlankLinearOpMode" sample, check "TeleOp" and "Setup Code for Configured Hardware", then press OK.

## Basic OpMode Structure

```java
@TeleOp
public class MyFIRSTJavaOpMode extends LinearOpMode {
    private Gyroscope imu;
    private DcMotor motorTest;
    private DigitalChannel digitalTouch;
    private DistanceSensor sensorColorRange;
    private Servo servoTest;

    @Override
    public void runOpMode() {
        imu = hardwareMap.get(Gyroscope.class, "imu");
        motorTest = hardwareMap.get(DcMotor.class, "motorTest");
        digitalTouch = hardwareMap.get(DigitalChannel.class, "digitalTouch");
        sensorColorRange = hardwareMap.get(DistanceSensor.class, "sensorColorRange");
        servoTest = hardwareMap.get(Servo.class, "servoTest");

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        // Wait for the game to start (driver presses PLAY)
        waitForStart();

        // run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            telemetry.addData("Status", "Running");
            telemetry.update();
        }
    }
}
```

### Key components

- **Annotation** — `@TeleOp` marks the OpMode as driver-controlled; use `@Autonomous` for autonomous OpModes.
- **Class definition** — "An op mode is defined as a Java class." A linear OpMode extends `LinearOpMode`, inheriting the necessary functionality.
- **Member variables** — private fields hold references to configured devices detected in the configuration file.
- **`runOpMode()`** — every `LinearOpMode` must implement this method; it is called when a user selects and runs the OpMode.
- **Hardware access** — device references are retrieved via `hardwareMap`:
  ```java
  motorTest = hardwareMap.get(DcMotor.class, "motorTest");
  ```
  "The name that you specify as the second argument of the HardwareMap.get method must match the name used to define the device in your configuration file." The match is case-sensitive; a mismatch throws an exception.
- **Initialization / waiting** — `telemetry.addData()` / `telemetry.update()` send messages to the Driver Station. "All linear op modes should have a waitForStart statement to ensure that the robot will not begin executing the op mode until the driver pushes the start button."
- **Main loop** — after start, the OpMode enters a `while (opModeIsActive())` loop, iterating until the driver presses stop.

## Building and Running

**Android Studio:** Connect the Robot Controller phone via USB with debugging enabled, or connect a Control Hub via its USB Type-C port (not Mini) with a charged 12V battery. Click the green Run button next to `TeamCode`. If the official Robot Controller app was previously installed from Google Play, Android Studio will request permission to uninstall and replace it. For Control Hubs (no screen), verify success via the Driver Station connection.

**OnBot Java:** The editor auto-saves `.java` files, but changes must be built before they run — press the Build button (wrench icon); a successful build prints "Build succeeded!" in the message pane. Common build errors:
- **Illegal start of expression** — missing or incorrect method arguments.
- **Cannot find symbol** — undefined classes or variables (case-sensitive).

"Whenever you rebuild an op mode, you must stop the current op mode run and then restart it before the changes that you just built take effect."

**Running (both tools):** On the Driver Station, select the OpMode from the TeleOp dropdown, press INIT (executes statements up to `waitForStart()`), then press START (triangle) to begin and STOP (square) to end.

## Adding Gamepad Control

```java
double tgtPower = 0;
while (opModeIsActive()) {
    tgtPower = -this.gamepad1.left_stick_y;
    motorTest.setPower(tgtPower);
    telemetry.addData("Target Power", tgtPower);
    telemetry.addData("Motor Power", motorTest.getPower());
    telemetry.addData("Status", "Running");
    telemetry.update();
}
```

`gamepad1` represents the state of gamepad #1 in the operator console. For an F310 gamepad, the joystick Y-axis ranges from -1 (top) to +1 (bottom); negating the value means pushing the stick forward produces positive motor power.

To use a gamepad: connect a Logitech F310 (or approved gamepad) to the Driver Station — direct USB-A on a Driver Hub, or a Micro USB OTG adapter on a phone. Press Start+A to designate it as User #1 (Start+B for User #2; PS4 pads use Options+Cross or Options+Circle). A gamepad icon appears above "User 1" on the Driver Station screen, highlighting green during activity.
