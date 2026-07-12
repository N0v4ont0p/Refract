package org.firstinspires.ftc.teamcode.subsystems;
import com.seattlesolvers.solverslib.command.SubsystemBase;
import com.qualcomm.robotcore.hardware.DcMotorEx;
public class Shooter extends SubsystemBase {
    private DcMotorEx fly;
    public void spinUp(double rpm) { fly.setVelocity(rpm); }
    public double ff(double d) { double a=0; for(int k=1;k<15;k++) a+=d*k/(k+0.5); return a; }
}
