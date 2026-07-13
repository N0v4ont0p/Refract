> Source: https://pedropathing.com/docs/pathing/reference/drive-vector-algorithm · Fetched: 2026-07-12

# Pedro Pathing — Follower / Drive Vector Algorithm

> Source: https://pedropathing.com/docs/pathing/reference/drive-vector-algorithm · Fetched: 2026-07-12

## Drive Vector Algorithm

> **Note:**
> This algorithm runs twice, once for the robot’s forward axis and once for the lateral axis, and then combines the results into a vector. This allows the robot to handle different decelerations per axis (e.g. mecanum wheels decelerate faster laterally than forward).
> The kinematics equations are also slightly modified to account for signed distance.

#### 1. Target Velocity Calculation

First, it calculates the target velocity the robot should have to decelerate at a specified rate and stop exactly at the end of the path. This is done using the kinematics formula:

```math
v_{t} = \sqrt{-2 * a_{t} * s}
```

Where:
- $$v_{t}$$ is our target velocity
- $$a_{t}$$ is the desired deceleration (should be negative)
- $$s$$ is the distance remaining (in code, modified for signed distance).

#### 2. Error Control and Feedforward

To control velocity, a <u>PIDF controller</u> is used. The most important terms are:

- **Proportional (P)** - corrects based on error: `error * kP`
- **Feedforward (F)** - prediction for the required velocity to reach the target velocity directly: `targetVelocity * kF`
  For example: if you want to go `60 in/s`, and `kF = 0.015`, the result is `0.9 power`; for `30 in/s`, it’s `0.45 power`.

This works well when cruising at a constant velocity. But during deceleration, momentum becomes a problem. The feedforward doesn’t account for the robot’s momentum and inertia, so it might still apply power when it should be reducing power much more aggressively. The proportional term alone can't fix this because it’s reactive, not predictive.

#### 3. Accounting for Momentum (Zero Power Decay)

To fix this, Pedro Path uses the concept of zero power acceleration, the deceleration the robot naturally experiences when power is cut (basically, its momentum).

Using this value, it estimates the velocity the robot would naturally have at the end of the path if it were to coast with **no power**. That’s calculated using:
```math
v_{f} = \sqrt{v_{i}^{2} + 2 * a * s}
```

Where:
- $$v_{f}$$ is the velocity the robot would be at the end of the path if it stopped applying power to the drivetrain and just had its momentum,
- $$v_{i}$$ is the current velocity,
- $$a$$ is the zero power deceleration,
- $$s$$ is the distance remaining.

Then it calculates a value called 'zero power decay' which tells us how much velocity needs to be lost due to momentum.
```math
p_{d} = v_{i} - v_{f}
```
Where:
- $$p_{d}$$ is zero power decay,
- $$v_{i}$$ is the current velocity,
- $$v_{f}$$ is the velocity at the end of the path.

Finally, it updates the target velocity by subtracting the zero power decay from it.

```math
v_{t} = v_{t} - p_{d}
```

This lets the robot reduce its feedforward power appropriately, so it slows down predictively, not just reactively.

---

> Source: https://pedropathing.com/docs/pathing/reference/deceleration · Fetched: 2026-07-12

## Deceleration

#### Default Deceleration
This is the default deceleration method that is used if no other method is specified. This deceleration method only decelerates on the last path of a PathChain or on the last. It uses two parameters to control the deceleration behavior:

##### BrakingStrength
This controls how strong the braking is. A higher value means stronger braking, while a lower value means gentler braking. The higher the value, the more abrupt the stop will be. The lower the value, the smoother the stop will be. However, a very low value may cause the robot to overshoot the target position.
This value is a double stored in the PathConstraint class/object and can be set in a PathChain or a Path.
To set in a PathChain after a path is added: `.setBrakingStrength(double set)`
To set in a Path: `PATH.setBrakingStrength(double set)`

> **Note:**
> - BrakingStrength was formerly known as **Zero Power Acceleration Multiplier (ZPAM)** in earlier versions of Pedro Pathing
> - A BrakingStrength of 1 corresponds to a ZPAM of 4.

#### Global Deceleration
This allows deceleration based on a entire PathChain and not only the last path of the chain. This is especially useful if the last path in the chain is short. Note that this mode is recommended for use globally, even when path chains are only one path, because it is more optimized than the default mode. Settings like BrakingStrength still take effect here as normal.

To set in a PathChain: `.setGlobalDeceleration(double BrakingStrength)` or `.setGlobalDeceleration()`

##### BrakingStart
This controls when the braking starts. The higher the value, the earlier the braking starts. The lower the value, the later the braking starts. A very high value may cause the robot to stop too early, while a very low value may cause the robot to stop too late.

BrakingStart is recommended to be used primarily for optimization, not for mitigating overshoot.

To set in a PathChain (only used with Global Deceleration): `.setBrakingStart(double set)`

#### No Deceleration
This disables deceleration for the entire path chain, allowing full speed at the end of the path chain. Though, this may cause overshoot and inaccuracy at the end of the path chain.

To set in a PathChain: `.setNoDeceleration()`

---

> Source: https://pedropathing.com/docs/pathing/reference/overshoot · Fetched: 2026-07-12

## Mitigating Overshoot

Please read the Deceleration page before looking at this one.

If your robot is overshooting in your auto, there are a couple of things you can try:
- Lower BrakingStrength: try lowering your BrakingStrength. Subtracting by intervals of 0.25 typically works well.
- Toggle Global Deceleration mode: if your PathChain has two or more paths, this will help a lot.

---

> Source: https://pedropathing.com/docs/pathing/reference/predictive · Fetched: 2026-07-12

## Predictive Braking

**Predictive Braking** is a positional control technique that maximizes deceleration by measuring the robot’s braking behavior rather than assuming it.

### Core Idea:
Instead of relying on a manually tuned derivative term to prevent overshoot, this controller predicts how far the robot will slide if it brakes using a small negative voltage. It uses the predicted braking distance to anticipate positional error, effectively treating it as reaction time. This allows the robot to brake precisely when needed, maximizing deceleration and accuracy.

#### Key benefits:
- **Faster:** maximizes deceleration, giving more time to accelerate and less time spent slowing down (~15% faster).
- **Automatically tuned empirically:** eliminates overshoot and mis-tuning; only kP requires manual adjustment.
- **Easier proportional tuning:** with braking behavior already known and maximized, kP can be set higher and adjusted more easily.
- **Accurate, responsive, and strong:** higher kP reduces steady-state error, improves responsiveness, and provides stronger corrective and holding forces.
- **Advanced movement capabilities:** treats braking distance as reaction time, enabling instant direction changes, sharp-angle turns at full speed, and natural centripetal correction for curves.

#### Trade-offs
- **Sharper stops:** can feel less smooth as the robot slides to a stop
- **No acceleration constraints:** always uses maximum deceleration when braking

## Back-EMF Braking: Modeling and Control
Applying small reverse motor power locks the wheels using internal back-EMF, letting the robot’s momentum resist motion without drawing voltage. This achieves the theoretical maximum deceleration as the robot slides to a stop.

In reality, braking is not perfectly linear. When the wheels lock, they slide across the floor, introducing nonlinear friction that must be accounted for to maximize deceleration.

### Modeling Real-World Behavior
The controller measures real-world braking by allowing the robot to slide to a stop with a small reverse voltage.
When plotting velocity versus stopping distance, the relationship typically shows a combination of linear and quadratic terms.

- **Linear term**: braking distance roughly proportional to velocity; caused by velocity-dependent braking forces such as back-EMF voltage, viscous friction, and controller delay.
- **Quadratic term**: braking distance proportional to velocity squared; caused by constant forces such as sliding friction at high speeds.

| Speed  | Dominant effect  | Model               | Braking distance ∝ |
| ------ | ---------------- | ------------------- | ------------------ |
| High   | Sliding friction | Quadratic-dominated | (v^2)              |
| Medium | Mixed            | Linear + quadratic  | (v + v^2)          |
| Low    | Back-EMF         | Linear-dominated    | (v)                |

A combined linear–quadratic braking model applies across all speeds.
At low speeds, the linear term dominates, while at high speeds, the quadratic term dominates.

### Why not use a traditional Derivative term?
A standard PID controller struggles with high-speed braking because it assumes linear deceleration, while the robot actually slides and experiences non-linear friction effects. Using only a derivative term forces you to lower aggressiveness to prevent oscillation, which reduces both responsiveness and maximum speed. Another approach is to rely on a secondary PID based on the error, with one controller more aggressive and one less aggressive. However, this becomes complicated to tune manually and does not fully capture the robot’s real behavior. By measuring actual behavior instead of assuming it, the controller predicts slippage rather than trying to prevent it.

## Common Questions
### Does maintaining traction with the ground result in faster deceleration?
Most robots maintain significant friction with the ground when they are sliding, which leads to immediate stops.
Only if your robot is so light that it completely removes contact with the ground when braking will it potentially have faster deceleration.
99% of FTC robots are heavy enough that they maintain some contact with the ground when braking.
Consider adding weight to lighter robots to increase their friction with the ground when braking.

### Why not use full-power reversal?
Alternating between full forward (+1) and full reverse (−1) can cause voltage spikes that may burn out or reset the control hub. Instead, braking is applied with a small opposite voltage. Even a tiny voltage (e.g., −0.0001) locks the wheels like zero-power brake mode, using the motor’s momentum to stop without consuming significant energy. However, if the opposite voltage is too low, it won’t provide enough braking once the robot slows down where the motor’s momentum is no longer sufficient to brake.

---

> Source: https://pedropathing.com/docs/pathing/reference/speed-control · Fetched: 2026-07-12

## Speed Control

### Overview
Pedro Pathing has no built in movement speed or velocity limiter.
The best method currently is limiting motor powers.
There are 3 main ways you can limit the motor power that Pedro Pathing can use.

### Methods

##### Global

      This method is recomended if you never want Pedro Pathing to exceed a certain motor power.
      The global default max power is stored in the `Constants` class,
      Specificaly, the `driveConstants` variable.

> **Note:**
> This is only garunteed to work on mecanum drivetrains using the `MecanumConstants`
>

      Simply change the value in `.maxPower(1)` (0 to 1).

##### Per Path

      This method is recomended if you want to slow down a particular path.
      When following a path, you can use `follower.followPath(pathChain, maxPower, holdEnd)`.

> **Note:**
> When using the `maxPower` parameter, you must also include the `holdEnd` parameter.
> The default for this value is `true`.
>

      `maxPower` is a number from 0 to 1.

##### Multiple Paths

`follower.setMaxPower(maxPower)` will set the speed of the follower until you change it again.
`maxPower` is a number from 0 to 1.

---

> Source: https://pedropathing.com/docs/pathing/reference/optimization · Fetched: 2026-07-12

## Optimization

To optimize your robot, try these steps:

#### Drive PID Adjustments
Increasing your Drive P value can often make your robot go faster, although after a certain threshold this likely won't help.

#### Global Deceleration Mode
Toggle Global Deceleration mode in your PathChains with .setGlobalDeceleration(double brakingStrength). The lower the value you pass in, the later in your chain the robot will start decelerating. Optimize by seeing how low you can set this value without causing too much overshoot. This tends to help more on a PathChain-to-PathChain basis, instead of a single global value used everywhere.

#### Optimal Pathing
Using the visualizer, try to optimize your robot's paths. Typically, shorter paths like lines tend to perform the best speed-wise. Beyond this, try experimenting with different heading interpolations. Make good use of features like piecewise heading interpolations, as for longer paths, a blend between linear and tangential can often be optimal.

