package org.firstinspires.ftc.teamcode.tuning;

import com.acmerobotics.dashboard.FtcDashboard;
import com.acmerobotics.dashboard.telemetry.MultipleTelemetry;

import org.firstinspires.ftc.robotcore.external.Telemetry;

/**
 * PRACTICE / TUNING ONLY. Fans telemetry out to both the Driver Station and FTC
 * Dashboard's graphing UI (FTC Dashboard's own {@link MultipleTelemetry}).
 *
 * Never call this from a competition OpMode: BIOBUZZ (2026-27) R704 prohibits
 * third-party streaming such as FTC Dashboard during events. The ftc-dashboard
 * docs' competition page also says to use the "Disable Dashboard" menu item or op
 * mode during gameplay. Keeping every Dashboard streaming call in this package is
 * what lets a reviewer (and ftc-code-review's config_lint season constraint)
 * confirm competition code is clean by looking in one place.
 */
public final class DashboardTelemetry {

    private DashboardTelemetry() {
        // static utility -- not instantiable
    }

    public static Telemetry wrap(Telemetry driverStationTelemetry) {
        return new MultipleTelemetry(driverStationTelemetry, FtcDashboard.getInstance().getTelemetry());
    }
}
