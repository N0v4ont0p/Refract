> Source: https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-aiming-and-ranging · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Aiming and Ranging Simultaneously | Limelight Documentation

 Skip to main content

# Aiming and Ranging Simultaneously

This example combines aiming and range adjustment into one method.
https://thumbs.gfycat.com/UncommonIncomparableDassierat-size_restricted.gif
This example uses code from the aiming and range adjustment examples and puts everything together into one simple function. Using this, you can get your robot “close” and then use code to automatically aim and drive to the correct distance.

float KpAim = -0.1f;
float KpDistance = -0.1f;
float min_aim_command = 0.05f;

std::shared_ptr<NetworkTable> table = NetworkTable::GetTable("limelight");
float tx = table->GetNumber("tx");
float ty = table->GetNumber("ty");

if (joystick->GetRawButton(9))
{
 float heading_error = -tx;
 float distance_error = -ty;
 float steering_adjust = 0.0f;

 if (tx > 1.0)
 {
 steering_adjust = KpAim*heading_error - min_aim_command;
 }
 else if (tx < -1.0)
 {
 steering_adjust = KpAim*heading_error + min_aim_command;
 }

 float distance_adjust = KpDistance * distance_error;

 left_command += steering_adjust + distance_adjust;
 right_command -= steering_adjust + distance_adjust;
}