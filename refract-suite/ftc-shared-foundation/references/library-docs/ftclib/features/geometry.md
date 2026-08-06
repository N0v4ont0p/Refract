> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/features/geometry.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.geometry
---

# Geometry

FTCLib provides access to geometry classes taken from WPILib. Since we like copy-pasting straight from WPILib instead of linking to the [original material](https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/pose.html), that's what we're gonna do.

## Translation

Translation in 2 dimensions is represented by FTCLib's`Translation2d` class. This class has an x and y component, representing the point $$(x,y)$$ or the vector $$\begin{bmatrix} x\\ y \end{bmatrix}$$ on a 2-dimensional coordinate system.

You can get the distance to another `Translation2d` object by using the `getDistance(Translation2d other)`, which returns the distance to another `Translation2d` by using the Pythagorean theorem.

## Rotation

Rotation in 2 dimensions is represented by FTCLib’s `Rotation2d` class. This class has an angle component, which represents the robot’s rotation relative to an axis on a 2-dimensional coordinate system. Positive rotations are counterclockwise.

## Pose

Pose is a combination of both translation and rotation and is represented by the `Pose2d` class. It can be used to describe the pose of your robot in the field coordinate system, or the pose of objects, such as vision targets, relative to your robot in the robot coordinate system. `Pose2d` can also represent the vector $$\begin{bmatrix} x\\ y\\ \theta \end{bmatrix}$$ .

## Vector

A vector in 2 dimensions is represented by the `Vector2d` class. It holds an $$x$$ and a $$y$$ value similarly to a `Translation2d`. These components representing the point $$(x,y)$$ or as the matrix$$\begin{bmatrix} x\\ y \end{bmatrix}$$.

Unlike a `Translation2d`, there are a few different methods and features.

## Transform and Twist

FTCLib provides 2 classes, `Transform2d`, which represents a transformation to a pose, and `Twist2d` which represents a movement along an arc. `Transform2d` and `Twist2d` all have $$x$$ , $$y$$ and $$\theta$$ components.

`Transform2d` represents a **relative** transformation. It has an translation and a rotation component. Transforming a `Pose2d` by a `Transform2d` rotates the translation component of the transform by the rotation of the pose, and then adds the rotated translation component and the rotation component to the pose. In other words, `Pose2d.plus(Transform2d)` returns $$\begin{bmatrix} x_{p} \\ y_{p} \\ \theta_{p} \end{bmatrix} + \begin{bmatrix} \cos{\theta_{p}} & -\sin{\theta_{p}} & 0 \\ \sin{\theta_{p}} & \cos{\theta_{p}} & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_{t} \\ y_{t} \\ \theta_{t} \end{bmatrix}$$ .

`Twist2d` represents a change in distance along an arc. For a given arc traveled, $$x$$ is the distance traveled forward as measured from the robot's perspective throughout the movement (for a differential drive, this is the arc length), $$y$$ is the distance traveled sideways from the robot's perspective (for a differential drive, this is 0), and $$\theta$$ is the change in heading.

Both classes can be used to estimate robot location. `Twist2d` is used in some of the FTCLib odometry classes to update the robot’s pose based on movement, while `Transform2d` can be used to estimate the robot’s global position from vision data.

