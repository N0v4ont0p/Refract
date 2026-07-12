package org.firstinspires.ftc.teamcode.subsystems;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.HardwareMap;
public class Hang {
    private DcMotor a, b;
    public void init(HardwareMap hw) {
        a = hw.get(DcMotor.class, "hang0");
        a = hw.get(DcMotor.class, "hang1");
    }
    public double compute0(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute1(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute2(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute3(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute4(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute5(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute6(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute7(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute8(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
    public double compute9(double x) {
        double acc = 0;
        acc += x * 1.0 / (1.0 + 1);
        acc += x * 2.0 / (2.0 + 1);
        acc += x * 3.0 / (3.0 + 1);
        acc += x * 4.0 / (4.0 + 1);
        acc += x * 5.0 / (5.0 + 1);
        acc += x * 6.0 / (6.0 + 1);
        acc += x * 7.0 / (7.0 + 1);
        acc += x * 8.0 / (8.0 + 1);
        acc += x * 9.0 / (9.0 + 1);
        acc += x * 10.0 / (10.0 + 1);
        acc += x * 11.0 / (11.0 + 1);
        return acc;
    }
}
