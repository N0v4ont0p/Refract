> Source: https://rr.brott.dev/docs/v1-0/guides/teleop-actions/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Teleop Actions | Road Runner Docs

# 
 Teleop Actions
 #

Most sample code in the docs involving actions use Actions.runBlocking() to
run them. runBlocking() is a great fit for most autonomous programs, though
it’s hard to integrate into teleop where there’s already a loop monitoring the
gamepads.

Let’s see what’s going on inside the function and see how we can repurpose it.

public static void runBlocking(Action action) {
 FtcDashboard dash = FtcDashboard.getInstance();
 Canvas previewCanvas = new Canvas();
 action.preview(previewCanvas);

 boolean running = true;
 while (running && !Thread.currentThread().isInterrupted()) {
 TelemetryPacket packet = new TelemetryPacket();
 packet.fieldOverlay().getOperations().addAll(previewCanvas.getOperations());

 running = action.run(packet);

 dash.sendTelemetryPacket(packet);
 }
}

At its core, runBlocking() is calling run() on the specified action until it
returns false. The rest is to give feedback on the actions execution in FTC
Dashboard. We can replicate this
in teleop.

public class TeleopWithActions extends OpMode {
 private FtcDashboard dash = FtcDashboard.getInstance();
 private List<Action> runningActions = new ArrayList<>();

 @Override
 public void init() {
 }

 @Override
 public void loop() {
 TelemetryPacket packet = new TelemetryPacket();

 // updated based on gamepads

 // update running actions
 List<Action> newActions = new ArrayList<>();
 for (Action action : runningActions) {
 action.preview(packet.fieldOverlay());
 if (action.run(packet)) {
 newActions.add(action);
 }
 }
 runningActions = newActions;

 dash.sendTelemetryPacket(packet);
 }
}

Actions can be queued up by adding them to the list.

if (gamepad1.a) {
 runningActions.add(new SequentialAction(
 new SleepAction(0.5),
 new InstantAction(() -> servo.setPosition(0.5))
 ));
}

Notice also how InstantAction saves us from writing return false; in the lambda.