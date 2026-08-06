> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/custom/drivetrain.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Custom Drivetrain
---

You can create your own drivetrain by extending the `Drivetrain` class. 
This allows you to implement custom drivetrain logic or different drivetrains that are not natively supported by the existing drivetrains.

### Hardware
All hardware should remain in your Drivetrain class.  
This includes motors, servos, and any other control hardware.  
This ensures that the localizer can access the necessary hardware components directly.
For example, if you are doing a coaxial swerve, you would initialize the motors and servos in the constructor of your drive class and then save them in an array or list.
Then, you can use these motors and servos in your drivetrain methods to control the robot's movement.

### Constants
It is suggested that you create a Constants class for your drivetrain.
This allows for easy configuration and modification of the localizer's parameters without changing the Drivetrain itself, although not required.
So, for a `CustomDrivetrain`, you would create a `CustomDrivetrainConstants` class.
In the `Constants` file, you would then create a `CustomDrivetrainConstants` object and pass it to your drivetrain through the constructor.

### Methods

#### calculateDrive
This abstract method is used to get the drive powers for the drivetrain. 
It returns a double array, which can be used to power the motors or servos in your drivetrain.
It specifically takes in the correctiveVector (centripetal and translational), headingVector, pathingPower, and the current heading of the robot.
This method is essential for implementing the drivetrain's movement logic, allowing you to control how the robot moves based on the pathing and heading information.

#### runDrive
This abstract method is used to run the hardware using the output of calculate drive.
This could be moving servos to positions or directions but also powering motors to a certain speed.


#### runDrive
There is an overloaded version of runDrive that takes in the correctiveVector, headingVector, pathingPower, and currentHeading.
It combines the functionality of calculateDrive and runDrive into one method.
This is useful if you want to simplify the process of calculating and running the drivetrain in one method call.

<Callout title="Note" type="info">
  You must implement the runDrive method that takes in the double array from calculateDrive, as it is abstract, while the overloaded version already calls the two methods, so it cannot be modified.
</Callout>