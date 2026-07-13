> Source: https://github.com/OpenFTC/EasyOpenCV/blob/master/readme.md · Fetched: 2026-07-12

# EasyOpenCV

NOTE: SDK v9.0+ is required to use this.

NOTE: an OpenRC-based SDK is NOT required to use this.

Finally, a straightforward and easy way to use OpenCV on an FTC robot! With this library, you can go from a stock SDK to running a sample OpenCV OpMode, with either an internal or external camera, in just a few minutes.

## Features at a glance

- Supports concurrent streaming from:
  - An internal camera and a webcam
  - Two webcams
  - Two internal cameras *(select devices; internal cameras must not share the same bus)*
- Supports Driver Station camera preview feature introduced in SDK v5.1
- Supports tapping on the viewport to cycle through the various stages of a pipeline (see [PipelineStageSwitchingExample](https://github.com/OpenFTC/EasyOpenCV/blob/master/examples/src/main/java/org/firstinspires/ftc/teamcode/PipelineStageSwitchingExample.java))
- Supports using webcams directly with OpenCV instead of going through a Vuforia instance
- Supports changing pipelines on-the-fly (while a streaming session is in flight)
- Supports dynamically pausing/resuming live viewport to save battery and CPU time
- Support for rotating stream based on physical camera orientation (e.g. use a webcam in portrait without having to mess with rotation yourself)

## Device compatibility

Unfortunately, due to a [known bug with OpenCV 4.x](https://github.com/opencv/opencv/issues/15389), EasyOpenCV is only compatible with devices that run Android 5.0 or higher. For FTC, this means that it is incompatible with the ZTE Speed. EasyOpenCV will work fine on all other FTC-legal devices (including the Control Hub).

## Documentation

- [Camera Initialization Overview](https://github.com/OpenFTC/EasyOpenCV/blob/master/doc/user_docs/camera_initialization_overview.md)
- [Pipelines Overview](https://github.com/OpenFTC/EasyOpenCV/blob/master/doc/user_docs/pipelines_overview.md)
- [Javadocs](https://javadoc.io/doc/org.openftc/easyopencv/latest/index.html)
- [Example programs](https://github.com/OpenFTC/EasyOpenCV/tree/master/examples/src/main/java/org/firstinspires/ftc/teamcode)

**IMPORTANT NOTE:** EasyOpenCV delivers RGBA frames, but desktop OpenCV (what you may be used to) delivers BGR frames. Beware when porting code between the two!

## Installation instructions

As of FTC SDK v8.2, EasyOpenCV is now packaged with the SDK as part of the Vision module. **No manual installation is necessary** whether you are using Android Studio or Blocks.

**PLEASE NOTE THAT THERE IS CURRENTLY A KNOWN BUG IN v9.0 and v9.0.1 OF THE FTC SDK WHICH PREVENTS IMPORTING THE `OpenCvCameraFactory` CLASS IN OBJ**

- This means you cannot use the "raw" EOCV APIs from OnBotJava (OBJ).
- As a workaround, you can port your pipeline to a `VisionProcessor` and use the Vision Portal API. There is a chapter in the LearnJava4FTC book that covers this.
- Alternatively, you can switch to using Android Studio.
- **THIS WILL BE FIXED IN A FUTURE RELEASE OF THE FTC SDK.**

## Changelog

### v1.7.3
- Updates `libjpeg-turbo` to 3.0.3
- Updates OpenCV to v4.10.0
- Show more detail about camera supported resolutions and formats when user requests unsupported configuration
- Show warning if performance could be improved by using MJPEG format

### v1.7.2
- Fix race conditions when handling exception during viewport insertion

### v1.7.1
- **IMPORTANT NOTE:** SDK v9.0 or higher is now required!
- Build against FTC SDK v9.x; remove support for Vuforia integration
  - Fixes inability to use CameraFactory in OnBotJava due to reference of Vuforia classes no longer in SDK
  - Fixes entire RC app crash due to ABI breakage when user pipeline throws an exception
- Handle exceptions in user-provided canvas annotators the same way exceptions in pipelines are handled to prevent entire RC app crash
- Use the modern stacktrace display when handling user exceptions instead of the legacy ESTOP telemetry message

### v1.7.0
- Adds new `NATIVE_VIEW` viewport renderer option, balancing the stability of `SOFTWARE` with the speedup of `GPU_ACCELERATED`
- Uses anti-aliasing when drawing the statistics overlay to make text more readable on low resolution screens
- Adds ability for user pipelines to hook into Canvas rendering of frames to the live view via `requestViewportDrawHook(object)` and `onDrawFrame(...)`
- Adds support for MJPEG streaming for webcams (requires FTC SDK v8.2, uses libjpeg-turbo)
- Fixes a deadlock when trying to switch cameras when using `OpenCvSwitchableWebcam`
- Fixes cases where mutex might not be released in internal camera v2 implementation
- Updates OpenCV-Repackaged transitive dependency to `4.7.0-A`

### v1.6.2
- Add generic `getControl()` method to OpenCvWebcam
- Fix corrupted camera frame delivery when using Camera2 API on some devices
- Prevent deadlock if pipeline tried to perform a synchronized UI thread operation and the device orientation was changed

### v1.6.1
- Fixes bug where, if using a webcam, frames were not delivered to user pipeline when calling `startStreaming()` after a previous call to `stopStreaming()` even though the stream was in fact restarted successfully (#65)
- Scales viewport statistics overlay based on pixel density so that it's not overly large on some devices

### v1.6.0
- Add support for getting WhiteBalanceControl for webcams
- Handle pipeline returning empty Mat for viewport display with an error message instead of an unclear exception
- Add SENSOR_NATIVE to camera rotation enum
- Desynchronize setPipeline() from active pipeline frame processing (fixes #58)
- Synchronize getting webcam controls with opening/closing camera
- Add support for getting the CameraCalibrationIdentity for an OpenCvWebcam
- Improve memory leak detection warning

### v1.5.3
- Dependency on OpenCV-Repackaged changed to a version that bundles the OpenCV native library with the artifact instead of requiring manual copy to external storage
- 64-bit support added
- Increases default webcam permission timeout to 5 seconds
- Removes app name resource strings which shouldn't have ever been there

### v1.5.2
- Fixes compatibility with SDK v8.0. You MUST use v1.5.2 (or later) for SDK 8.0 — previous versions will **not** work. Backwards compatibility is NOT maintained for this release.
- Fixes possible leak of framebuffer when viewport render thread was restarted

### v1.5.1
- Fixes crash with SDK v7.0 when memory leak warning was generated

### v1.5.0
- Fixes compatibility with SDK v7.0. You MUST use 1.5.0 (or later) for SDK 7.0. Backwards compatibility with SDK v6.1 is maintained.
- First release supporting OnBotJava
- **API CHANGE:** OpenCV core upgraded to OpenCV v4.5.3 (transitive dependency on `opencv-repackaged` updated to `4.5.3-B`); requires an updated native library to be copied to the device
- Failure to open the camera device is now properly handled — **API CHANGE:** `AsyncCameraOpenListener` instances must now also implement `void onError(int errorCode)`
- Change webcam opening timeout to be user-configurable (new `void setMillisecondsPermissionTimeout(int ms)`)
- Fix race condition when closing camera which could cause the camera worker thread to crash
- Fix issue with viewport where user-drawn parts of the image would not appear in the correct color unless alpha was specified
- Fix bug where Camera2 backend was broken on some devices due to reading the image timestamp after closing the Image object
- Samples moved to `org.firstinspires.ftc.teamcode` package

### v1.4.4
- Add support for Vuforia passthrough mode, allowing Vuforia and OpenCV to run simultaneously on the same camera (see `OpenCvAndVuforiaOnSameCameraExample`)

### v1.4.3
- **IMPORTANT NOTE:** SDK v6.1 or higher is now required!
- Add support for additional webcam controls introduced in SDK v6.1
- Add `saveMatToDiskFullPath()` method to pipeline class
- Add `TimestampedOpenCvPipeline` class which extends `OpenCvPipeline` and delivers capture time timestamps along with frames

### v1.4.2
- Add ability to set FocusMode to Internal camera v1 API
- General improvements to Internal camera v2 API (startStreaming() checks, mutex fixes, native C++ conversion)
- Viewport improvements: centered image, GPU-accelerated rendering mode, warn instead of throw for webcam rendering policy
- Optimized webcam frame delivery using native C++ code to avoid unnecessary `memcpy` operations
- Add (beta) API for recording pipelines to a video file
- Fix memory leak detector to trip only after settle delay

### v1.4.1
- Transitive dependency on OpenCV-Repackaged updated to 4.1.0-C
- Fixes issue which prevented webcams from initializing in v1.4.0

### v1.4.0
- Adds support for Android Camera2 API via new `OpenCvInternalCamera2` interface, with manual control over ISO, exposure, focus, white balance, and frame interval (FPS)
- Make `OpenCvCamera` interface extend `CameraStreamSource`
- Adds `setViewportRenderingPolicy()` API (`MAXIMIZE_EFFICIENCY` vs `OPTIMIZE_VIEW`)
- Add memory leak detector for pipelines
- Add `init(Mat m)` method to pipeline class, called with the first frame from the camera
- Adds pipeline utility function for saving Mats to disk (async, up to 5 concurrent)
- Adds APIs for closing/opening the camera asynchronously (recommended)
- Adds support for switchable webcams via new `OpenCvSwitchableWebcam` interface
- Fix deadlock when closing webcams; increase webcam open timeout to 2 seconds
- Adds new `OpenCvWebcam` interface with exposure/focus control via SDK UVC driver interfaces

### v1.3.2
- Resolutions >480p are now possible with webcams (at reduced framerates)
- Add exposure compensation and autoexposure lock APIs for internal camera
- Fix blank display when user pipeline returned cropped mat of type CV_8UC1 (e.g. masks)
- Print supported resolutions when user selects illegal resolution for camera

### v1.3.1
- Transitive dependency on OpenCV-Repackaged updated to 4.1.0-B, which drastically improves error handling when loading native library

### v1.3
- Add official support for multiple concurrent camera streams (also allows running Vuforia alongside EasyOpenCV)
- Add "TrackerAPI" classes (run multiple OpenCV algorithms in the same pipeline, switch rendered output by tapping the viewport)
- Add support for rendering cropped returns from user pipeline
- Optimise viewport to re-use existing framebuffer memory
- Fix issue where a submat created from the input Mat would be de-linked from the input buffer on the next frame
- Added ability to use advanced features for internal cameras: recording hint, hardware frame timing range, zoom control, flashlight control, double buffering (default)
- API change: camera instances are now created by invoking `OpenCvCameraFactory.getInstance().create...`

### v1.2
- **HOTFIX:** implement workaround for SDK bug of RenderScript failing to initialize on some devices which prevented webcam frames from being forwarded through the JNI to the Java side (issue #1)

### v1.1
- SDK v5.1 or higher now required
- Add support for stream preview on Driver Station
- Fix bug where internal camera was not correctly released
- Fix bug where a null pipeline caused a crash
- API change: user pipelines now need to `extends OpenCvPipeline` instead of `implements OpenCvPipeline`
- Add ability for user pipeline to override `onViewportTapped()` to be notified if the user taps the viewport
- Add `PipelineStageSwitchingExample` showing how to use `onViewportTapped()` to change which pipeline stage is drawn to the viewport for debugging, and how to get data from your pipeline to your OpMode

### v1.0
- Initial release
