package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.HardwareMap;

public class LauncherSubsystem {
    private final DcMotorEx flywheel;
    public LauncherSubsystem(HardwareMap hw) { flywheel = hw.get(DcMotorEx.class, "launcher"); }
    public void setVelocity(double ticksPerSecond) { flywheel.setVelocity(ticksPerSecond); }
}
