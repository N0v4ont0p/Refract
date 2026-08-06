> Source: https://rr.brott.dev/docs/v1-0/guides/cancellation/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Cancellation | Road Runner Docs

# 
 Cancellation
 #

Sometimes you may want to a stop a trajectory when it’s already running. For
example, if you’re executing an intake trajectory in autonomous, you may want to
stop once sensors detect that a game element was taken in.

Cancellation comes in two forms, abrupt and smooth. The former has the advantage
of speed over the latter, though rapid acceleration may cause wheel slip and
impede following performance.

## 
 Abrupt Cancellation
 #

Abrupt cancellation is easy to implement. Simply switch from executing a
trajectory to stopping the motors or executing a new trajectory.

public class CancelableFollowTrajectoryAction implements Action {
 private final FollowTrajectoryAction action;
 private boolean cancelled = false;

 public CancelableFollowTrajectoryAction(TimeTrajectory t) {
 action = new FollowTrajectoryAction(t);
 }

 @Override
 public boolean run(@NonNull TelemetryPacket telemetryPacket) {
 if (cancelled) {
 setDrivePowers(new PoseVelocity2d(new Vector2d(0, 0), 0));
 return false;
 }

 return action.run(telemetryPacket);
 }

 public void cancelAbruptly() {
 cancelled = true;
 }
}

Then this cancelable action should be executed concurrently with logic that
decides when to cancel. We’ll take inspiration from teleop
actions and write our own runBlocking() loop.

public class CancelableActionOpMode extends LinearOpMode {
 @Override
 public void runOpMode() throws InterruptedException {
 FtcDashboard dash = FtcDashboard.getInstance();

 CancelableFollowTrajectoryAction cancelableAction = new CancelableFollowTrajectoryAction(traj);
 while (opModeIsActive()) {
 TelemetryPacket packet = new TelemetryPacket();
 cancelableAction.preview(packet.fieldOverlay());
 if (!cancelableAction.run(packet)) {
 break;
 }

 if (gamepad1.a) {
 cancelableAction.cancelAbruptly();
 }

 dash.sendTelemetryPacket(packet);
 }
 }
}

It’s a little silly to call cancelAbruptly() when we could just break;
directly here, but this pattern can be used in more complex scenarios where
the cancelable action can also be nested inside another action. In this case,
when the trajectory action is cancelled, it won’t poison the rest of the sequential
action. The sequence will skip forward to the next action (sleep in this case)
and continue like normal.

public class CancelableActionOpMode extends LinearOpMode {
 @Override
 public void runOpMode() throws InterruptedException {
 FtcDashboard dash = FtcDashboard.getInstance();

 CancelableFollowTrajectoryAction cancelableAction = new CancelableFollowTrajectoryAction(traj);
 while (opModeIsActive()) {
 TelemetryPacket packet = new TelemetryPacket();
 cancelableAction.preview(packet.fieldOverlay());
 if (!cancelableAction.run(packet)) {
 break;
 }

 if (gamepad1.a) {
 cancelableAction.cancelAbruptly();
 }

 dash.sendTelemetryPacket(packet);
 }
 }
}

Nothing in the implementation really depends on action being a
FollowTrajectoryAction. We can generalize the pattern into a FailoverAction
that runs a main action until instructed to fall back to a secondary action.

public class FailoverAction implements Action {
 private final Action mainAction;
 private final Action failoverAction;
 private boolean failedOver = false;

 public FailoverAction(Action mainAction, Action failoverAction) {
 this.mainAction = mainAction;
 this.failoverAction = failoverAction;
 }

 @Override
 public boolean run(@NonNull TelemetryPacket telemetryPacket) {
 if (failedOver) {
 return failoverAction.run(telemetryPacket);
 }

 return mainAction.run(telemetryPacket);
 }

 public void failover() {
 failedOver = true;
 }
}

The cancellable trajectory action from above can now be represented as

Action a = new FailoverAction(
 new FollowTrajectoryAction(traj),
 new InstantAction(() -> setDrivePowers(new PoseVelocity2d(new Vector2d(0, 0), 0)))
);

You can also put NullAction in the failover slot to do nothing on
failover().

## 
 Smooth Cancellation
 #

Smooth cancellation can be implemented with a failover action that switches to a
stopping trajectory on cancellation. Stopping trajectories can be generated from
any normal Trajectory by calling cancel() with how far the robot is along
the trajectory.

 Will add more details here in the future. See
road-runner-quickstart#310
in the meantime.