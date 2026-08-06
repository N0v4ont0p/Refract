> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/docs/getting-started.md · Fetched: 2026-08-06 · Ref: main @ 998011a20399
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

# Getting started

Zero to a ticking behavior tree in about ten minutes. No prior behavior-tree experience assumed.

!!! tip "Generating robot code with Claude Code?"
    [Refract](https://github.com/N0v4ont0p/Refract) is a companion plugin that grounds FTC code
    generation in real hardware specs and library docs instead of guessing. When its
    `ftc-team-config` skill asks about your software stack, mention TickTree alongside
    FTCLib/SolversLib/raw LinearOpMode so generated subsystem code gets wired as TickTree leaves
    rather than raw command bindings — there's no formal TickTree option in its config schema yet,
    but its skills pick up context from what you tell them.

!!! note "A note on FTCLib vs SolversLib"
    TickTree supports **both** FTCLib and SolversLib equally. These docs lead with **SolversLib**
    simply because it's the actively-maintained fork (FTCLib core hasn't published since ~2022); the
    FTCLib snippets right below it are exactly as supported. Use whichever your team already has.

## 1. Install

Add JitPack, then TickTree, then **your command library** (this last part trips people up — see the
warning).

```groovy
// project build.gradle
repositories {
    maven { url = 'https://jitpack.io' }
}
```

=== "SolversLib"

    ```groovy
    repositories {
        maven { url = 'https://repo.dairy.foundation/releases' }
    }
    dependencies {
        implementation 'com.github.N0v4ont0p.Ticktree:ticktree-core:v0.1.0'
        implementation 'com.github.N0v4ont0p.Ticktree:ticktree-ftc:v0.1.0'
        implementation 'org.solverslib:core:0.3.4'   // you supply this — see warning
    }
    ```

=== "FTCLib"

    ```groovy
    dependencies {
        implementation 'com.github.N0v4ont0p.Ticktree:ticktree-core:v0.1.0'
        implementation 'com.github.N0v4ont0p.Ticktree:ticktree-ftc:v0.1.0'
        implementation 'org.ftclib.ftclib:core:2.1.1'   // you supply this — see warning
    }
    ```

!!! warning "You must add FTCLib / SolversLib yourself"
    TickTree depends on FTCLib/SolversLib as **`compileOnly`** so it never forces one on a team that
    uses the other. `compileOnly` dependencies **do not transitively install** — so adding
    `ticktree-ftc` will *not* pull the command library in for you. If you hit a runtime
    `NoClassDefFoundError` mentioning `com/arcrobotics/...` or `com/seattlesolvers/...`, that line is
    missing. Most teams already have it in their `build.gradle`.

## 2. Two nodes you need to know

A behavior tree is made of **nodes**. The two you'll use most are *composites* — nodes that combine
children:

- **`sequence(a, b, c)`** — runs children **in order, requiring all to succeed** (logical AND).
  Stops early and fails if any child fails. Think: "do a, *then* b, *then* c."
- **`selector(a, b, c)`** — tries children **in order until one succeeds** (logical OR). Think:
  "try a; if it can't, try b; else c." Its reactive cousin **`reactiveSelector`** re-checks from the
  top every tick, so a higher-priority child can take over the moment it becomes viable — this is
  how preemption works.

Every node, each tick, returns one of three statuses: **`SUCCESS`**, **`FAILURE`**, or
**`RUNNING`** (still working, ask again next loop). That's the whole vocabulary.

## 3. Build a tree

```java
import static io.github.n0v4ont0p.ticktree.TickTree.*;
import static io.github.n0v4ont0p.ticktree.Status.*;
import io.github.n0v4ont0p.ticktree.*;   // Blackboard, BehaviorTree, ...

Blackboard bb = new Blackboard();

BehaviorTree tree = TickTree.tree("teleop").root(
    reactiveSelector(                                   // priority order, re-checked every loop
        // Highest priority: while the driver holds A, hand control back to them.
        guard(() -> gamepad1.a,
            action("driverControl", () -> { drive.arcade(gamepad1); return RUNNING; })),
        // Otherwise: auto-align then score.
        sequence(
            action("alignToGoal", () -> aligned() ? SUCCESS : RUNNING),
            action("score",       () -> { shooter.fire(); return SUCCESS; })
        )
    )
).build(bb);
```

- `action("name", () -> ...)` is a leaf that does work and returns a `Status`. `RUNNING` means
  "still going" — return it across as many loops as the work takes.
- `guard(condition, child)` runs `child` only while `condition` is true; the instant it goes false,
  the child is **halted** (its actuators stopped) and the guard fails — so the branch below takes
  over cleanly.

## 4. Wire it into your OpMode

Build the tree **once** in `init()`, tick it every `loop()`, and halt it in `stop()`.

=== "Iterative OpMode"

    ```java
    public class MyTeleOp extends OpMode {
        private BehaviorTree tree;

        @Override public void init() {
            tree = /* build as above */;
        }
        @Override public void loop() {
            tree.tick();                                  // one tick per loop
            TreeTelemetry.addActivePath(telemetry, "Tree", tree);
            telemetry.update();
        }
        @Override public void stop() {
            tree.halt();                                  // stop actuators when the OpMode ends
        }
    }
    ```

=== "LinearOpMode"

    ```java
    public class MyAuto extends LinearOpMode {
        @Override public void runOpMode() throws InterruptedException {
            BehaviorTree tree = /* build as above */;
            waitForStart();
            OpModeTreeRunner.runLinear(tree, this::opModeIsActive);   // ticks until stop; halts on exit
        }
    }
    ```
    `runLinear` loops for you and **guarantees `halt()` on any exit** — normal stop or thread
    interruption — so actuators always stop.

## 5. Confirm it's working

`TreeTelemetry.addActivePath(...)` writes the **active path** to the Driver Station each loop — the
live chain of nodes from the tree down to whatever leaf is currently running, plus its status:

```
Tree : teleop ▸ driverControl [RUNNING]     ← while holding A
Tree : teleop ▸ alignToGoal [RUNNING]       ← after releasing A, aligning
Tree : teleop ▸ score [SUCCESS]             ← aligned, fired
```

If the path jumps to `driverControl` the instant you press A and back to the auto-score branch when
you release it, preemption is working. That's a ticking, reacting behavior tree.

## Next

- **[Core concepts](core-concepts.md)** — memory vs reactive (important!), the blackboard, and why
  halt matters.
- **[Node reference](node-reference.md)** — the full catalog.
