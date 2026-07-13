> Source: https://ftc-docs.firstinspires.org/en/latest/control_hard_compon/rc_components/sensors/sensors.html · Fetched: 2026-07-12

# Sensors

Listed below are examples of common robot sensors. While the _FIRST_ Tech Challenge SDK supports many sensors, not all are natively supported.

## Distance Sensor (Ultrasonic)

**Example: MaxBotix I2C Ultrasonic Sensor (MB1242)**

An Ultrasonic Distance Sensor measures the distance between an object and the sensor by sending out a sound wave and measuring the time it takes for the wave to travel to the object and back. Using this time and the speed of sound, the distance can be calculated.

## Distance Sensor (Optical)

**Example: REV 2m Distance Sensor (REV-31-1505)**

An Optical Time of Flight (ToF) Sensor measures the distance between an object and the sensor by sending out a light beam and measuring the time it takes for the beam to travel to the object and back. Using this time and the known speed of light, the distance can be calculated. The way an object interacts with light can change measurement accuracy — transparent objects like field panels will often give inaccurate readings.

## Color Sensor

**Examples: REV Color Sensor (REV-31-1557), Modern Robotics Color Sensor (MR 45-2018)**

"A color sensor is usually a digital output device that is able to measure the color of an object." Most color sensors require the object to be relatively close to the sensor.

## Touch Sensor

**Example: REV Touch Sensor (REV-31-1425)**

"A touch sensor is a digital output device that detects the activation of a button." Commonly used as a limit switch to limit the range of motion of a mechanism. Typically uses the digital port.

## Magnetic Limit Switch

**Example: REV Magnetic Limit Switch (REV-31-1462)**

"A Magnetic Limit Switch is used to detect the presence of a magnet in near proximity." Commonly used to limit the range of movement of a mechanism that would otherwise cause damage, by placing a magnet on the mechanism to trigger the switch. As a digital device it only outputs a boolean, not a range.

## IMU

**Examples: Navigation Sensor (navX2-Micro), BNO055**

"An Inertial Measurement Unit (IMU) is a sensor that is a combination of a Gyroscope, Accelerometer, and Magnetometer."
- A Gyroscope reports the angular orientation of an object in 3 dimensions.
- An Accelerometer reports the acceleration of an object in 3 dimensions.
- A Magnetometer measures the strength of magnetic fields in 3 axes and can be used as a compass.

## Potentiometer

**Examples: REV Potentiometer (REV-31-1155), 50k Ohm Potentiometer (BBG-770)**

"A Potentiometer is a device that changes the output voltage based upon the degree to which the adjuster is turned." Often used to measure the absolute orientation of an axle. Typically attached via the analog port of the REV Hub.

## Sensor Compatibility

The compatibility chart on the source page indicates sensor types, compatibility status, and any adapters needed for use with FTC systems:
- Most I2C sensors are compatible with adapters.
- Quad Encoder motors are generally compatible; REV Robotics HD Hex and Core Hex Motors are directly compatible without custom adapters.
- Digital sensors like the Modern Robotics Limit Switch are compatible but may require custom wiring harnesses.
- Some analog sensors (Rate Gyro, Optical Distance Sensor, Light Sensor, Magnetic Sensor) are not officially supported.

## Additional Resources (referenced, not detailed on this page)

- Analog Port Overview
- Digital Port Overview
- I2C Port Overview
