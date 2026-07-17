> Source: https://docs.revrobotics.com/duo-control/hello-robot-java/part-3/autonomous-navigation-onbot · Fetched: 2026-07-17
> Completeness-audit addition: REV's real docs sitemap has 158 pages; the 5 files already stored
> here are deliberate consolidated syntheses covering the Java-programming and hardware-setup
> tracks (confirmed by checking their own source citations, which each already cite a whole
> subsection). The ~94-page Blocks-programming curriculum is a different curriculum entirely
> (visual programming, not Java) — legitimately out of scope for Refract, not a gap. This
> RUN_TO_POSITION encoder-autonomous page was the one real, concrete gap in the Java track:
> directly relevant to autonomous movement code generation and not covered by the existing
> summaries' stated scope. Driver Hub-specific pages (a separate REV product) remain a known,
> lower-priority gap.

# REV — Encoder-Based Autonomous Movement (OnBot Java)

Moving to a target position via encoders, rather than elapsed-time timing, eliminates the drift
elapsed-time methods accumulate.

## Setup

```java
leftmotor = hardwareMap.get(DcMotor.class, "leftmotor");
rightmotor = hardwareMap.get(DcMotor.class, "rightmotor");
```

For a mirrored drivetrain (motors facing opposite directions), reverse one side:

```java
rightmotor.setDirection(DcMotor.Direction.REVERSE);
```

## `RUN_TO_POSITION`, three steps in order

1. **Target position** (encoder ticks): `leftmotor.setTargetPosition(1000);`
2. **Run mode**: `leftmotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);`
3. **Power** (this is what actually makes the motor move once in this mode):
   `leftmotor.setPower(0.8);`

## Resetting encoders before a run

Reset *before* `waitForStart()`, not after:

```java
leftmotor.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
```

## Waiting for the move to finish

```java
while (opModeIsActive() && (leftmotor.isBusy() && rightmotor.isBusy())) {}
```

Use `||` instead of `&&` if you only need to wait for either motor (e.g. one side reaches target
first is acceptable) rather than both.
