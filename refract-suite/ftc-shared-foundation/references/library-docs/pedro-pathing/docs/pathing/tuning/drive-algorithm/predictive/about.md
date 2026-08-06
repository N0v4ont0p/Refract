> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/tuning/drive-algorithm/predictive/about.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: "What is Predictive Braking?"
---

Instead of relying on a manually tuned derivative term to prevent overshoot, this controller predicts how far the robot will slide if it brakes using a small negative voltage. It uses the predicted braking distance to anticipate positional error, effectively treating it as reaction time. This allows the robot to brake precisely when needed, maximizing deceleration and accuracy.

Learn more about Predictive Braking: http://pedropathing.com/docs/pathing/reference/predictive

# Why use Predictive Braking?

Using this method, a world-record autonomous was achieved, and many other teams' autos were also sped up by **~15%**, all while automatically tuning in a few minutes.

Predictive Braking is a new, optional algorithm for following paths that replaces the old translational and drive PIDFs.

The old PIDFs are still supported, but predictive braking is much easier to tune because the algorithm automatically tunes and maximizes the deceleration speed and accuracy of your robot.

### Predictive Braking Autonomous Example
<iframe
  width="560"
  height="315"
  src="https://www.youtube-nocookie.com/embed/CcmMqLvqVk4"
  title="Predictive Braking Autonomous Example"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>