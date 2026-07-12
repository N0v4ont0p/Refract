# Team 99902 — Getting the Mecanum TeleOp Running

You have: goBILDA Strafer chassis kit, 4 mecanum wheels, 1 REV Control Hub.

## 1. Put the file in your project

Copy `MecanumTeleOp.java` into your FtcRobotController project at:

```
TeamCode/src/main/java/org/firstinspires/ftc/teamcode/MecanumTeleOp.java
```

(If you use OnBot Java instead of Android Studio: on the Control Hub's web page,
go to OnBot Java, make a new file called `MecanumTeleOp`, and paste the contents in.)

## 2. Create the robot configuration

On the Driver Station app (or the Control Hub web interface):

1. Tap the three dots -> **Configure Robot** -> **New**.
2. Tap **Control Hub Portal** -> **Control Hub** -> **Motors**.
3. Set each port you plugged a drive motor into to **GoBILDA 5202/5203/5204 series**
   and name them exactly (capitalization matters):
   - `frontLeft`
   - `backLeft`
   - `frontRight`
   - `backRight`
4. **Save** the configuration and **activate** it.

The suggested wiring is port 0 = frontLeft, 1 = backLeft, 2 = frontRight,
3 = backRight, but any ports work as long as the names match the real motors.

## 3. First drive test (important!)

1. Put the robot **on blocks** so the wheels don't touch the ground.
2. Run the "Mecanum TeleOp (99902)" OpMode and push the left stick forward.
3. All four wheels should spin in the "robot goes forward" direction.
   If one spins backwards, open the code and flip that motor's
   `setDirection(...)` between `FORWARD` and `REVERSE`.
4. Also check your mecanum wheels are mounted correctly: viewed from the top,
   the rollers should form an **X** pattern. If strafing feels wrong or the
   robot spins when you try to strafe, a wheel is probably on the wrong corner
   (goBILDA mecanums come in left and right versions).

## 4. Controls

| Input | Action |
|---|---|
| Left stick up/down | Drive forward/backward |
| Left stick left/right | Strafe left/right |
| Right stick left/right | Turn |
| Hold right bumper | Slow mode (30% speed) |

Have fun, and good luck this season!
