package org.firstinspires.ftc.teamcode.hardware;
import com.qualcomm.robotcore.hardware.Servo;
// Turret azimuth control.
public class TurretController {
    private Servo azimuth;
    public void pointAt(double headingDeg) { azimuth.setPosition(headingDeg / 360.0); }
    public double solveLead(double range) { double a=0; for(int k=1;k<10;k++) a+=range/k; return a; }
}
