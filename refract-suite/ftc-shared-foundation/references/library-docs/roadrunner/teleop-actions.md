> Source: https://rr.brott.dev/docs/v1-0/guides/teleop-actions/ · Fetched: 2026-07-17
> Completeness-audit addition: RoadRunner's real v1.0 docs have ~19 pages total; only 4 were
> stored before this pass (installation, core-concepts, trajectories, tuning). This is the
> single highest-value gap for a code-generation use case — running an Action outside a blocking
> autonomous context, i.e. during TeleOp. Remaining known gaps (new-features, migration, api-docs,
> builder-ref, log-files, modules, and the other 9 guide pages — cancellation, extra-correction,
> path-following, pose-mapping, variable-constraints, continuity, ftclib-commands, tangents,
> centerstage-auto) are logged, not silently dropped.

# RoadRunner — Running Actions from TeleOp

`Actions.runBlocking()` — the standard way to run an Action during autonomous — blocks until the
action completes, which doesn't fit a TeleOp loop that also needs to keep reading gamepad input
every cycle. `runBlocking()`'s own real mechanism is just: call `run()` on the action repeatedly
until it returns `false`, plus manage FTC Dashboard telemetry/preview. TeleOp replicates that same
mechanism manually, non-blocking:

```java
public class TeleopWithActions extends OpMode {
    private FtcDashboard dash = FtcDashboard.getInstance();
    private List<Action> runningActions = new ArrayList<>();

    @Override public void init() {}

    @Override public void loop() {
        TelemetryPacket packet = new TelemetryPacket();

        // ... update based on gamepad input ...

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
```

Queue a new action onto the running list from a gamepad edge, e.g.:

```java
if (gamepad1.a) {
    runningActions.add(new SequentialAction(
            new SleepAction(0.5),
            new InstantAction(() -> servo.setPosition(0.5))
    ));
}
```

`InstantAction` wraps a one-shot `Runnable` so the lambda doesn't need to `return false;` itself.
