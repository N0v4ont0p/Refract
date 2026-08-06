> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/vision/computer-vision.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.vision
---

# Setting Up Vision

Computer Vision is the process of helping computers to understand the digital images such as photographs and videos provided to them. FTCLib provides examples on the object detection needed for the current season \(right now being Ultimate Goal detection\) using the [EasyOpenCV library](https://github.com/OpenFTC/EasyOpenCV).

## Installation Requirements

Since FTCLib depends on EasyOpenCV for vision, and because EasyOpenCV depends on [OpenCV-Repackaged](https://github.com/OpenFTC/OpenCV-Repackaged), you will need to copy [libOpenCvAndroid453.so](https://github.com/OpenFTC/OpenCV-Repackaged/tree/9a4d3d4bc001feffb3767842fa2de0c38a98883a/doc/native_libs/armeabi-v7a) into the `FIRST` folder of the Robot Controller (i.e. connect the Robot Controller to your computer with a USB cable, put it into MTP mode, and drag 'n drop the file)

Due to 64 bits vs 32 bits conflicts, after moving the so file, please remove any instance of **arm64-v8a** in `build.common.gradle`. EasyOpenCV runs in 32 bits while some phones and the Control Hub are 64 bit. For more details, please refer to the [installation page](https://docs.ftclib.org/ftclib/installation). 

Due to breaking changes in SDK version 7.0, EasyOpenCV version 1.5.0 is required to maintain compatibility. Because 7.0 will be the minimum SDK requirement in competition, the FTCLib team will not support SDK below version 7.0.  

