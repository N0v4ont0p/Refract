package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.vision.apriltag.AprilTagDetection;
import org.firstinspires.ftc.vision.apriltag.AprilTagProcessor;

public class HiveRelocalizer {
    private final AprilTagProcessor tags;
    public HiveRelocalizer(AprilTagProcessor tags) { this.tags = tags; }
    /** Reset odometry from the robot's field pose computed off the HIVE tags. */
    public double[] fieldPose() {
        for (AprilTagDetection detection : tags.getDetections()) {
            if (detection.id >= 30 && detection.id <= 45 && detection.robotPose != null) {   // BIOBUZZ HIVE tag IDs
                return new double[]{detection.robotPose.getPosition().x, detection.robotPose.getPosition().y};
            }
        }
        return null;
    }
}
