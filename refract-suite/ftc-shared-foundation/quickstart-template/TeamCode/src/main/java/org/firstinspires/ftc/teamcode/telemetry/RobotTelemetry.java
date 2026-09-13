package org.firstinspires.ftc.teamcode.telemetry;

import org.firstinspires.ftc.robotcore.external.Telemetry;

/**
 * Telemetry scaffolding, wired in by default rather than opt-in.
 *
 * known-failure-modes.md names "no telemetry" as the root cause that makes every
 * other fault undiagnosable: a fault that only shows up once (a brownout, a
 * dropped I2C read, a stale static carrying state from the previous match) reads
 * as an unreproducible hardware flake unless something recorded state at the
 * moment it happened. This class exists so a rookie never has to remember to
 * add telemetry -- {@link org.firstinspires.ftc.teamcode.opmodes.TeamOpMode}
 * calls {@link #wrap} for every OpMode automatically.
 *
 * Competition-legal by default: telemetry goes to the Driver Station only. The
 * BIOBUZZ (2026-27) manual, R704, allows streaming robot data only through the
 * FTC Driver Station application and names FTC Dashboard and FTControl Panels as
 * prohibited streaming services. Graphing through FTC Dashboard during practice
 * lives in {@link org.firstinspires.ftc.teamcode.tuning.DashboardTelemetry}, used
 * only by tuning OpModes -- never by a competition OpMode. Re-check the ACTIVE
 * season's rule (rules.py lookup R704 --season <slug>) each season: the wording
 * of this rule changes.
 */
public final class RobotTelemetry {

    private RobotTelemetry() {
        // static utility -- not instantiable
    }

    /**
     * @param driverStationTelemetry the {@code telemetry} field the SDK hands every OpMode
     * @return the Driver Station telemetry, unchanged -- the one legal competition channel
     */
    public static Telemetry wrap(Telemetry driverStationTelemetry) {
        return driverStationTelemetry;
    }
}
