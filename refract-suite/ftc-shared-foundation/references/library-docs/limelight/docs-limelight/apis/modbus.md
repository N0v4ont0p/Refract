> Source: https://docs.limelightvision.io/docs/docs-limelight/apis/modbus · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Modbus API | Limelight Documentation

 Skip to main content

 On this page

# Modbus API

Limelight OS features a Modbus TCP server running at (ipaddress):502

- 
Integers: Integers are SIGNED and encoded using twos complement. This method is universally recognized and ensures correct sign interpretation.

- 
Floating-Point Numbers: Floats are encoded using the IEEE 754 standard. To comply with the 16-bit register limitation of the Modbus protocol, floating-point numbers are divided into two parts:

- The higher-order 16 bits are stored in the second register, and the lower-order 16 bits in the first register.

- Little-endian format ensures compatibility with the Modbus spec.

USB and Ethernet Limelights may be tested with ModbusTool

Modbus enables support for part inspection and industrial automation use-cases. To get started with Modbus, you need to do the following:

- 
Connect to your Limelight via Ethernet or USB-C and configure a pipeline.

- While all pipelines will output results over modbus, our python snapscript pipelines are extremely versatile for industrial use-cases since they support custom input output data.

- 
Give your Limelight a static IP address

- 
Attach your Limelight to a modbus network.

# Modbus Register Specification

## Input / Read-Only Registers​

RegisterKeyTypeDescription
0hbintHeartbeat value. Increases once per frame
1pipelineIndexintCurrent active pipeline index (0 .. 9).
2validTargetint1 if a valid target exists, 0 otherwise.
3resultsCountintTotal results count. Includes all fiducial detections, neural detections, etc
4IDintID / Team Number
5modbusModeintModbus Server Output Mode.
6cpuTempintCPU temperature in Celsius.
7cpuUsageintCPU usage percentage.
8ramUsageintRAM usage percentage.
9currentFPSintCurrent frames per second.
10captureLatencyintCapture latency. (milliseconds)
11targetLatencyintProcessing latency. (milliseconds)
12-15reservedint

If Output Mode is set to 0:

RegisterKeyTypeDescription
16,17txfloat32Horizontal angular offset to target in degrees
18,19tyfloat32Vertical angular offset to target in degrees
20,21txncfloat32Horizontal angular offset to target (relative to principal pixel) in degrees
22,23tyncfloat32Vertical angular offset to target (relative to principal pixel) in degrees
24,25tafloat32 (0-1)Area of the target as a percentage of the image size
26fiducialIDintCurrent AprilTag ID
27classifierClassintClass Index of current classifier pipeline output. -1 if no Classifier results
28detectorClassintClass Index of current detector pipeline output. -1 if no Detector results
29reservedint
30,31python[0]float32Custom python output array [0]
32,33python[1]float32Custom python output array [1]
34,35python[2]float32Custom python output array [2]
36,37python[3]float32Custom python output array [3]
38,39python[4]float32Custom python output array [4]
40,41python[5]float32Custom python output array [5]
42,43python[6]float32Custom python output array [6]
44,45python[7]float32Custom python output array [7]

## Holding / Write-Only Registers​

RegisterKeyTypeDescription
0unlockedintUnlocks the pipeline. Set to 1 to enable pipeline switching and custom input data
1pipeIndexintSets the pipeline index if "unlocked" is set to 1
2outputModeintSets the output mode. 0 - standard, 1 - rawtargets (WIP)
3reservedint
4reservedint
5reservedint
6reservedint
7reservedint
8pythonInput[0]intCustom python input array [0]
9pythonInput[1]intCustom python input array [1]
10pythonInput[2]intCustom python input array [2]
11pythonInput[3]intCustom python input array [3]
12pythonInput[4]intCustom python input array [4]
13pythonInput[5]intCustom python input array [5]
14pythonInput[6]intCustom python input array [6]
15pythonInput[7]intCustom python input array [7]
16,17pythonInput[8]float32Custom python input array [8]
18,19pythonInput[9]float32Custom python input array [9]
20,21pythonInput[10]float32Custom python input array [10]
22,23pythonInput[11]float32Custom python input array [11]
24,25pythonInput[12]float32Custom python input array [12]
26,27pythonInput[13]float32Custom python input array [13]
28,29pythonInput[14]float32Custom python input array [14]
30,31pythonInput[15]float32Custom python input array [15]

- Input / Read-Only Registers
- Holding / Write-Only Registers