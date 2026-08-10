> AUTHORED BY REFRACT — not fetched from upstream. Written: 2026-08-07.
> This is not a copy of Pedro's documentation. It exists because Pedro's own bundled doc set
> (checked directly, both `examples.md` and `docs/pathing/examples/teleop.md`, plus a grep for
> `offsetHeading` across all 63 files this corpus stores) covers `setTeleOpDrive`'s `isRobotCentric`
> parameter with exactly one line — a code comment reading `// Robot Centric` next to the literal
> `true` — and never once shows or explains the 5-argument `offsetHeading` overload. Nothing here
> contradicts Pedro's docs; it fills a gap they leave, verified by direct search before writing this
> rather than assumed. Written after a real integration where the one-line comment's implication
> ("false means field-centric") was correctly read but the actual runtime semantics were the inverse
> of what that reading suggests, and it took reading `Follower.setTeleOpDrive`'s real source, not
> the doc, to see why.

# Field-centric ("headless") teleop drive — the mechanism Pedro's one-line comment doesn't explain

Pedro's bundled examples show `setTeleOpDrive`'s fourth argument as a bare `true // Robot Centric`,
with a comment above it noting "make the last parameter false for field-centric." That's correct as
far as it goes. It doesn't explain what the parameter actually does, why the direction of that
implication surprises people, or that a 5th parameter exists for the piece a field-centric drive
still needs and the docs never show.

## The two frames in play

Every holonomic robot has two coordinate systems active at once:

- **Robot frame** — rotates with the chassis. "Forward" always means "toward the robot's own nose,"
  regardless of which way the robot is currently facing on the field.
- **Field frame** — fixed. "Forward" always means the same physical direction on the floor,
  regardless of how the robot is rotated.

**Robot-centric drive** feeds the joystick vector straight into the robot frame: push the stick up,
the robot's nose goes that way — always, but "that way" changes as the robot spins, so the driver
has to mentally track the robot's current heading to predict what "forward" will do next.

**Field-centric drive** removes that dependency: push the stick up, the robot always travels the
same field direction, regardless of which way its chassis happens to be pointed at that instant.

## What `isRobotCentric` actually does, and why the comment reads backwards from intuition

`Follower.setTeleOpDrive(forward, strafe, turn, isRobotCentric, offsetHeading)` builds the drive
vector from the stick inputs, then:

1. If `isRobotCentric` is true, the vector is **rotated by the robot's current heading**.
2. The vector is then rotated once more by `offsetHeading` (see below).

The vector is consumed downstream **in the field frame by default**. Rotating it by the robot's
heading is the step that makes it robot-relative — so `isRobotCentric = true` is the robot-centric
case, and `isRobotCentric = false` skips that rotation and leaves the vector in field terms, which
*is* field-centric behavior. That matches the doc's own comment. What the comment doesn't say is
*why* it reads backwards from a first guess: naming the flag `isRobotCentric` invites reading `true`
as "yes, do the field-centric thing to it," when `true` is what turns the field-centric skip *off*.
A team porting or writing this from the comment alone can pass the flag with the *value* correct and
the *reasoning* inverted, and not notice until the controls feel wrong in a specific, confusing way
(see the failure mode below).

`turn` is unaffected by any of this either way — Pedro builds the rotation/turn vector separately
from the translation vector, so nothing here changes how the robot spins.

## The parameter the bundled examples never show: `offsetHeading`

Field-centric alone is not enough, because "field forward" as the library's own coordinate frame
defines it has no relationship to where a driver is physically standing at a given field position.
The 5-argument overload's final parameter, `offsetHeading`, is a one-time rotation applied to the
drive vector to align the library's field frame with wherever "forward" needs to mean for that
specific driver-station setup. It is genuinely necessary for a usable field-centric drive and does
not appear anywhere in this corpus's bundled Pedro examples — both the flat `examples.md` and the
mirrored `docs/pathing/examples/teleop.md` show only the 4-argument robot-centric call.

**Use this parameter — don't hand-roll the same rotation separately.** Verified directly against
`VectorCalculator.setTeleOpMovementVectors`: the drive vector is rotated by the robot's heading only
if `isRobotCentric`, and is then **always** rotated once more by `offsetHeading`, regardless of that
flag. A team that doesn't know this parameter exists and instead applies its own alignment rotation
to the stick input before calling the 4-argument overload is doing the same math by hand, outside
the library, with no reason to — and a much easier place to introduce a sign or units mistake than
inside a single, already-tested library parameter.

## The failure mode this produces

The flag's inverted-reading risk and the missing `offsetHeading` documentation compound: a team that
reasons "I want field-centric, so I should pass `false`... wait, but the comment says `true` means
Robot Centric, so field-centric must be the opposite" can get the boolean right while still having
no idea an alignment offset is needed at all — and the resulting drive is field-centric but rotated
to the wrong "forward," which presents as **"the controls are simply inverted,"** not as a frame or
alignment problem. That symptom sends debugging effort toward the joystick-reading code, which is
fine, rather than toward the frame math, which is where the actual issue lives.

## What field-centric drive costs that robot-centric drive doesn't

Robot-centric drive works even with a garbage pose estimate — it never consults heading at all.
Field-centric drive is only as good as the heading feed it's built on: a wrong or stale pose at the
moment `setTeleOpDrive` is called makes every drive direction wrong, not just aim. This is the
direct tradeoff for the intuitive-controls benefit, and it's worth stating plainly since nothing in
the 4-argument robot-centric examples this corpus bundles would surface it.

## How to actually verify a field-centric setup, rather than trust it by eye

Replay the vector math directly against several different robot headings and confirm the output
direction stays identical regardless of chassis rotation. Reading the boolean and the offset value
and reasoning about what they "should" do is exactly the mode of check that produced the inverted-
controls failure above — the fix that actually confirmed correctness was running the real
`rotateVector`/heading-transform logic against test headings, not re-reading the call site.
