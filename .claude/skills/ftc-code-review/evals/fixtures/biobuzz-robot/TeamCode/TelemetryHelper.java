package org.firstinspires.ftc.teamcode;

import com.acmerobotics.dashboard.FtcDashboard;
import com.acmerobotics.dashboard.telemetry.MultipleTelemetry;
import org.firstinspires.ftc.robotcore.external.Telemetry;

public class TelemetryHelper {
    public static Telemetry wrap(Telemetry ds) {
        return new MultipleTelemetry(ds, FtcDashboard.getInstance().getTelemetry());
    }
}
