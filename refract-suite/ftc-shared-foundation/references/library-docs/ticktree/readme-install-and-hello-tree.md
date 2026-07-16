> Source: https://github.com/N0v4ont0p/Ticktree/blob/998011a2039942df2ec0e2cb063d454084b9cd1e/README.md · Fetched: 2026-07-16
> Note: fetched at HEAD (998011a), not the v0.1.0 release tag — TickTree is pre-alpha and actively changing; per G5's own staleness discipline, re-fetch and re-stamp before trusting this against a materially newer commit.

[![Release](https://jitpack.io/v/N0v4ont0p/Ticktree.svg)](https://jitpack.io/#N0v4ont0p/Ticktree)
[![CI](https://github.com/N0v4ont0p/Ticktree/actions/workflows/ci.yml/badge.svg)](https://github.com/N0v4ont0p/Ticktree/actions/workflows/ci.yml)

# TickTree

**A behavior-tree decision-making engine for FIRST Tech Challenge (FTC) robotics, in Java.**

TickTree answers the question FTC's existing tooling leaves to ad-hoc student code: *given the
current state of the match, the robot, and the field — which behavior should the robot run right
now, and how does it get preempted the instant that stops being true?* It is a reactive
arbitration layer that sits **above** motion/path libraries (Road Runner, Pedro Pathing) and
command frameworks (FTCLib, SolversLib) — orthogonal to all of them, not a replacement for any.

> **Status: pre-alpha — API unstable.** The engine (core) and FTC bridge are implemented,
> tested off-robot, and published on JitPack (`v0.1.0`), but 1.0 has not shipped and the API may
> still change between 0.x releases. Design detail: [PLAN.md](PLAN.md).

> **Generating FTC code with Claude Code?** [Refract](https://github.com/N0v4ont0p/Refract) is a
> companion plugin that grounds generation in real hardware specs, real library docs, and the
> actual rules corpus instead of guessing. Mention TickTree when its `ftc-team-config` skill asks
> about your software stack, and generated subsystem code can be wired as TickTree leaves instead
> of ad hoc control flow.

## Contents

- [Modules](#modules)
- [Install](#install-30-seconds)
- [Hello, tree](#hello-tree)
- [Documentation](#documentation)
- [Zero-allocation tick](#zero-allocation-tick)
- [Building from source](#building-from-source)
- [License](#license)

## Modules

| Module | Description |
|---|---|
| `ticktree-core` | The pure-Java behavior-tree engine. **Zero** Android/FTC-SDK dependency; fully unit-testable off-robot with JUnit 5. |
| `ticktree-ftc`  | The FTC bridge — neutral functional adapters mapping FTCLib **and** SolversLib `Command`s onto TickTree nodes, plus an `OpModeTreeRunner`. FTC dependencies are `compileOnly`, so neither library is forced on you. |

## Install (30 seconds)

Add JitPack, then TickTree, then **make sure your command library is also on the classpath** (see
the warning below):

```groovy
repositories {
    maven { url = 'https://jitpack.io' }
}
```

**SolversLib teams** (recommended — SolversLib is the actively-maintained fork):

```groovy
repositories {
    maven { url = 'https://repo.dairy.foundation/releases' }   // SolversLib
}
dependencies {
    implementation 'com.github.N0v4ont0p.Ticktree:ticktree-core:v0.1.0'
    implementation 'com.github.N0v4ont0p.Ticktree:ticktree-ftc:v0.1.0'
    implementation 'org.solverslib:core:0.3.4'   // ← YOU must add this yourself (see below)
}
```

**FTCLib teams** (equally supported):

```groovy
dependencies {
    implementation 'com.github.N0v4ont0p.Ticktree:ticktree-core:v0.1.0'
    implementation 'com.github.N0v4ont0p.Ticktree:ticktree-ftc:v0.1.0'
    implementation 'org.ftclib.ftclib:core:2.1.1'   // ← YOU must add this yourself (see below)
}
```

> ### ⚠️ You must supply FTCLib or SolversLib yourself
> TickTree depends on FTCLib and SolversLib as **`compileOnly`** — on purpose, so it never forces
> one library on a team that uses the other. **`compileOnly` dependencies are NOT transitive**, so
> adding `ticktree-ftc` does **not** pull FTCLib/SolversLib in for you. If you see
> `NoClassDefFoundError: com/arcrobotics/...` or `com/seattlesolvers/...` at runtime, it's because
> the command library line above is missing. Add the one your team already uses. (Most teams
> already have it — this line is usually already in your `build.gradle`.)

## Hello, tree

A tiny TeleOp behavior: auto-score while the driver isn't overriding, otherwise hand control back
to the driver.

```java
import static io.github.n0v4ont0p.ticktree.TickTree.*;
import static io.github.n0v4ont0p.ticktree.Status.*;
import io.github.n0v4ont0p.ticktree.*;   // BehaviorTree, Blackboard, ...

public class MyTeleOp extends OpMode {
    private BehaviorTree tree;

    @Override public void init() {
        Blackboard bb = new Blackboard();
        tree = TickTree.tree("teleop").root(
            reactiveSelector(                                     // re-evaluated every loop; higher branch wins
                guard(() -> !gamepad1.a,                          // while the driver is NOT overriding...
                    sequence(
                        action("alignToGoal", () -> aligned() ? SUCCESS : RUNNING),
                        action("score",       () -> { shooter.fire(); return SUCCESS; })
                    )),
                action("driverControl", () -> { drive.arcade(gamepad1); return RUNNING; })   // fallback
            )
        ).build(bb);
    }

    @Override public void loop() { tree.tick(); }   // tick once per loop
    @Override public void stop() { tree.halt(); }   // stop actuators when the OpMode ends
}
```

For a `LinearOpMode`, use the runner instead of a manual loop — it halts the tree on any exit
(including interruption):

```java
waitForStart();
OpModeTreeRunner.runLinear(tree, this::opModeIsActive);   // ticks until stop; halts on exit
```

## Documentation

Full docs live in [`docs/`](docs/) (mkdocs-material):

- **[Getting started](docs/getting-started.md)** — zero to a ticking tree in ~10 minutes.
- **[Core concepts](docs/core-concepts.md)** — tick/Status, composites vs decorators vs leaves,
  memory vs reactive, the blackboard, halt/preemption.
- **[Node reference](docs/node-reference.md)** — every node type, with semantics and examples.
- **[Cookbook](docs/cookbook.md)** — complete recipes: priority arbitration, conditional
  autonomous, wrapping a path follower, retry/timeout fallbacks, and more.
- **[Testing your tree](docs/testing-your-tree.md)** — unit-test your match strategy off-robot,
  no hardware required.
- **[Migrating from an if/else or FSM](docs/migration.md)** — a worked conversion example.

## Zero-allocation tick

TickTree guarantees **zero heap allocation on the steady-state tick path**: after you build a tree
once, calling `tree.tick()` with no `TreeVisitor` attached allocates nothing — across the full node
catalog (composites, decorators, guards, blackboard reads/writes). This matters on the REV Control
Hub (1 GB RAM, Android 7.1), where per-tick allocation causes GC jitter that shows up as loop-time
spikes. Verified by an allocation harness measuring a full-catalog tree over 200,000 ticks (0 bytes).

It deliberately does **not** cover: building the tree (`build()` / node construction allocates once,
off the hot path) and `TreeVisitor` calls (`activePath()` / `snapshot()` build strings/objects — only
when you actually invoke them). Your own action/condition bodies are your responsibility (e.g. don't
box primitives per tick).

## Building from source

```bash
./gradlew build
```

Requires JDK 17+ (emits Java 8 bytecode). `ticktree-core` needs only a JDK; `ticktree-ftc` is an
Android library module and additionally requires the Android SDK.

## License

[MIT](LICENSE) © 2026 George Hu
