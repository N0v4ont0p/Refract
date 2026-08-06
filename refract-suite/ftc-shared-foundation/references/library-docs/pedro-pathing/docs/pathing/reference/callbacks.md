> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/reference/callbacks.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Path Callbacks
---

### Overview
In Pedro Pathing, you can define custom path callbacks to be run as the robot follows the path. This allows defining and running actions contained inside a `PathChain` object. These callbacks are reset if the chain is followed again.
Callbacks are automatically added to the **last defined path in the builder before the callback is created.** Note that when defining a callback, each Runnable can be defined using a lambda expression, and each method to add a callback can optionally take an additional `int` parameter for the maximum **number of times** the action should run (the default being 1).

### Built-In Callbacks
Pedro Pathing has a couple built-in callback types:
1. Parametric
    - Executes after a certain percentage (calculated by distance traveled) of the path is exceeded
    - These are the most recommended callback to use
    - Can be added to a chain in the `PathBuilder` using `.addParametricCallback(double percent, Runnable action)` where `percent` is the percent completion of the previous path required to run `action`
2. Temporal
    - Executes a certain amount of time after the robot begins following the path.
    - These are not really recommended as they are inconsistent, given that Pedro's follower isn't based on time and the robot won't be guaranteed to be in the same spot between trials when the action is run.
    - Can be added to a chain in the `PathBuilder` using `.addTemporalCallback(double millis, Runnable action)` such that `action` executes after the `millis` amount has passed since the robot began following this path.
3. Pose
    - Executes after the robot passes the point on a path closest to a given `Pose`
    - The user inputs a `Pose` and the follower evaluates the closest point on the path to this pose. As the robot drives along the path, if it crosses this closest point, the action is run.
    - Can be added to a chain in the `PathBuilder` using `.addPoseCallback(Pose pose, Runnable action, double guess)` where `guess` is an initial guess for the parametric t-value of the closest point on the path to the specified pose. The more accurate this guess is the better the search will go, but a guess like 0.5 should suffice regardless.

### Custom Callbacks
Callbacks can also be defined by creating a class that implements the `PathCallback` interface. The `isReady()` method should return a boolean value: true if the callback is ready to be run, and false otherwise. The `run()` method is the action to be run, while the optional `initialize()` method can be used to initialize the callback once the robot begins following the path it is attached to. Finally, the `getPathIndex()` returns the index of the `Path` in the `PathChain` that the callback should be attached to.
These callbacks can then be added using the `PathBuilder` method `.addPathCallback(PathCallback callback)`. As before, you can control the maximum number of times a callback is run when adding it to the `PathBuilder` by passing an integer after the callback.

A shortcut to defining a new `PathCallback` in the builder is the use of the following `PathBuilder` method: `.addPathCallback(CallbackCondition isReady, Runnable action)` where two lambda expressions can be passed in such that `action` is run when `isReady` returns true. The `CallbackCondition` interface is functionally the same as a `BooleanSupplier`.

### Pausing and Resuming Paths
A powerful tool that can be used in conjunction with callbacks is the `pausePathFollowing()` method. This method makes the robot stop moving in th middle of a path, which is useful for performing arm actions. After completing an action, you can call `resumePathFollowing()` for the robot to continue following the path. Note that the `breakFollowing()` method doesn't work in the same way since it resets you to the first `Path` in the PathChain and resets all the `PathCallback` objects associated with the PathChain.