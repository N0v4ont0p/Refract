**No, not if the robot itself is 19 inches wide. A 19" wide robot fails the starting size rule.** One exception is below and could change the answer.

**The rule this season is R102, not R101.** In the BIOBUZZ Competition Manual (V1), R101 is the rule that your team must build its own robot. The starting size rule moved to R102 (last season in DECODE it was R101, so you remembered right). R102 says the starting configuration is limited to an 18-inch cube. When the match starts, every part of the robot must be still and fit inside an 18 in. (45.70 cm) wide × 18 in. long × 18 in. high box.

19" is 1" too wide. G304.F also says the robot must be set up in that starting configuration. If it isn't, the match won't start until you fix it. If you can't fix it quickly, the robot is DISABLED or taken off the field. Before that happens, you'd fail the sizing check at inspection.

**The exception:** R102 says pre-loaded scoring elements may stick out past the 18" limit. This season each robot starts touching 4 POLLEN pre-loads (G304.G). If the extra inch is only POLLEN sticking out, and the robot's frame and mechanisms fit in 18", you pass.

**Ways to fix it if the robot really is 19":**
- **Fold or tuck things in.** R103 lets the robot hold a smaller shape either mechanically while powered off, or with an init OpMode that holds servos and motors in place. The robot must support itself and can't push on the sides or top of the sizing tool. You may wait several minutes before a match, so don't leave motors stalled against a hard stop.
- **Expand after the start.** R105 lets the robot grow once the match starts, up to 18 × 24 × 29 in. (29 in. is height). The limit must be enforced by the mechanism itself, not by software. So being 19" wide during the match is fine if that width falls in the 24" direction, as long as you start at 18".

Also check for Team Updates. This is the V1 manual, and Team Updates can change rules.

**Questions I'd ask you:**
1. **What makes it 19": the frame and mechanisms, or the POLLEN pre-loads?** If only POLLEN, you're legal and nothing changes. If it's the robot, you need a fix.
2. **What sticks out: something that could fold (intake, arm, bumper) or the drivetrain frame?** If it folds, add a latch or an init OpMode hold (R103). If it's the frame, you need to take an inch out of the chassis.
3. **Did you measure with every mechanism in its starting position, and in every interchangeable setup you plan to run?** R102 says you should be ready to show you pass in every setup. If you measured while something was loose or powered off in a different pose, measure again in the real starting pose.
4. **Once expanded, does the robot fit 18 × 24 × 29 in., limited by the mechanism itself?** If not, you also need a mechanical stop to pass R105.

Sources:
- [2026-2027 BIOBUZZ Competition Manual V1](https://ftc-resources.firstinspires.org/ftc/game/manual) (R101, R102, R103, R105, G304)
- [BIOBUZZ Game & Season, FIRST](https://www.firstinspires.org/programs/ftc/game-and-season)
- [DECODE Competition Manual, Section 12 (last season's R101)](https://ftc-resources.firstinspires.org/ftc/archive/2025/game/manual-12)