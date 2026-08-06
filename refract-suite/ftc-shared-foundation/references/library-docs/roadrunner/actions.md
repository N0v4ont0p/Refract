> Source: https://rr.brott.dev/docs/v1-0/actions/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Actions | Road Runner Docs

# 
 Actions
 #

Actions help you define simple behaviors that are easy to combine into large
routines. By breaking down autonomous programs you make them easier to
understandand and modify. And then the base actions can be reused in new
autonomous programs so you never need to start from scratch. But most
importantly of all your code will play nice with the Road Runner Quickstart.
Let’s see how this all works!

 Actions are very similar to commands as implemented in libraries like
WPILib
and
FTCLib. Road
Runner uses a different name for this pattern to distinguish its particular
design from these peer libraries. The ideas have also been explored
extensively outside the FIRST realm. Check out cooperative multitasking and
coroutines if you’re interested.

## 
 Overview
 #

Each subsystem of a robot has certain basic behaviors. For a drivetrain,
these may include following a trajectory, moving toward a point, and turning in place;
for a shooter you may have spinning up, firing a ball, and loading from the
magazine. These are the smallest units of action that accomplish something
meaningful. But they range under hood from simply setting a motor power to
tracking a smooth path with a sophisticated controller.

In code we’ll represent the subsystems with classes and the actions with methods
that return Action:

public class Drive {
 public Action followTrajectory(Trajectory t) {
 return new TodoAction();
 }

 public Action turn(double angle) {
 return new TodoAction();
 }

 public Action moveToPoint(double x, double y) {
 return new TodoAction();
 }
}

public class Shooter {
 public Action spinUp() {
 return new TodoAction();
 }

 public Action fireBall() {
 return new TodoAction();
 }

 public Action loadBall() {
 return new TodoAction();
 }
}

Now to run an action, just call runBlocking():

Drive drive = new Drive();
Actions.runBlocking(drive.moveToPoint(10, 20));

Despite the name “blocking,” this method can still be interrupted by pressing
the stop button. This feature comes for free with actions and is much more
reliable than carefully checking for interruption at every phase in your op
mode.

 But actions are no panacea for programming folly. It’s perfectly possible to
write custom actions cannot be interrupted, usually with a misplaced
Thread.sleep() or while loop. Take care in composing your own actions and
interrupt your op modes regularly to catch any issues in advance of competition.

Then with basic actions in place, you can combine them together into a complex
action. Sequential actions run a list of actions one at a time in order, while
parallel actions run a list of actions simultaneously until each has finished.

Here’s a rudimentary routine that executes the following steps:

- Turn 90 degrees in place.

- While following shootingTraj, spin up the shooter and fire a ball.

Actions.runBlocking(new SequentialAction(
 drive.turn(Math.PI / 2),
 new ParallelAction(
 drive.followTrajectory(shootingTraj),
 new SequentialAction(
 shooter.spinUp(),
 shooter.fireBall()
 )
 )
));

That’s all there is to it!

## 
 Built-in Actions
 #

The quickstart comes with a small set of actions to start from.

- SleepAction: sleep for a duration

- SequentialAction: execute a bunch of actions one after the other

- ParallelAction: execute a bunch of actions at the same time

- FollowTrajectoryAction: follow a trajectory (separate tank and mecanum versions)

- TurnAction: turn in place (separate tank and mecanum versions)

## 
 Custom Actions
 #

At their core, actions are long-running segments of code that execute in many
little steps. This property allows us to run two actions A and B in parallel
without using multiple threads. By executing “step A”, “step B”, “step A”, …
in alternating fashion, actions A and B appear to proceed concurrently. But the
illusion is easily ruined if “step A” takes a long time and starves B of the
chance to run.

To create a custom action, make a class that implements Action and with the
following two methods:

- public boolean run(TelemetryPacket packet): Code to run repeatedly while the
method returns true. Any data added to packet will be sent to FTC
Dashboard—see its telemetry
documentation
for details.

Calls to run() should complete quickly. Delays longer than 100ms will begin to
noticeably impinge on other actions.

Let’s look at a simple shooter spin-up action.

public class Shooter {
 private DcMotorEx motor;

 public Shooter(HardwareMap hardwareMap) {
 motor = hardwareMap.get(DcMotorEx.class, "shooterMotor");
 }

 public class SpinUp implements Action {
 private boolean initialized = false;

 @Override
 public boolean run(@NonNull TelemetryPacket packet) {
 if (!initialized) {
 motor.setPower(0.8);
 initialized = true;
 }

 double vel = motor.getVelocity();
 packet.put("shooterVelocity", vel);
 return vel < 10_000.0;
 }
 }

 public Action spinUp() {
 return new SpinUp();
 }
}

public class ShooterOpMode extends LinearOpMode {
 @Override
 public void runOpMode() throws InterruptedException {
 Shooter shooter = new Shooter(hardwareMap);

 waitForStart();

 Actions.runBlocking(shooter.spinUp());
 }
}

Checking the velocity and adding it to telemetry doesn’t take much time even
though the shooter may need seconds to reach the right speed.

Also if you only use the class SpinUp inside spinUp() you can move the class
inside the method.

class Shooter {
 private DcMotorEx motor;

 public Shooter(HardwareMap hardwareMap) {
 motor = hardwareMap.get(DcMotorEx.class, "shooterMotor");
 }

 public Action spinUp() {
 return new Action() {
 private boolean initialized = false;

 @Override
 public boolean run(@NonNull TelemetryPacket packet) {
 if (!initialized) {
 motor.setPower(0.8);
 initialized = true;
 }

 double vel = motor.getVelocity();
 packet.put("shooterVelocity", vel);
 return vel < 10_000.0;
 }
 };
 }
}