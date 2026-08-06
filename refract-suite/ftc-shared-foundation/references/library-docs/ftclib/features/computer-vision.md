> Source: https://github.com/FTCLib/FTCLib-Docs/blob/e49968a8531379b5310bf9b8f9199197cf9d6b12/features/computer-vision.md · Fetched: 2026-08-06 · Ref: v2.1.0 @ e49968a85313
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
description: package com.arcrobotics.ftclib.vision
---

# Computer Vision

Computer Vision is the process of helping computers to understand the digital images such as photographs and videos provided to them. FTCLib provides examples on the object detection needed for the current season \(right now being Ultimate Goal detection\) using the [EasyOpenCV library](https://github.com/OpenFTC/EasyOpenCV).

## Installation Requirements

Since FTCLib depends on EasyOpenCV for vision, and because EasyOpenCV depends on [OpenCV-Repackaged](https://github.com/OpenFTC/OpenCV-Repackaged), you will need to copy [`libOpenCvNative.so`](https://github.com/OpenFTC/OpenCV-Repackaged/blob/master/doc/libOpenCvNative.so) from the `/doc` folder of that repo into the `FIRST` folder on the USB storage of the Robot Controller \(i.e. connect the Robot Controller to your computer with a USB cable, put it into MTP mode, and drag 'n drop the file\)

Due to 64 bits vs 32 bits conflicts, after moving the so file, please remove any instance of **arm64-v8a** in `build.common.gradle`. EasyOpenCV runs in 32 bits while some phones and the Control Hub are 64 bit.

## `UGRectRingPipeline`

The heart of the Ultimate Goal detector is the pipeline. A pipeline is just a fancy way describing the sequence of instructions given to continuously manipulate the image\(in this case, what the camera sees\). Ignoring the fancy code, the pipeline boils down to these following instructions:

### Receiving the Input

```java
public Mat processFrame(Mat input)
```

In this line, what the camera sees is being passed in and represented as a matrix.

### Manipulating the Input

```java
Imgproc.cvtColor(input, matYCrCb, Imgproc.COLOR_RGB2YCrCb);

Rect topRect = new Rect(
    (int) (matYCrCb.width() * topRectWidthPercentage),
    (int) (matYCrCb.height() * topRectHeightPercentage),
    rectangleWidth,
    rectangleHeight
);

Rect bottomRect = new Rect(
    (int) (matYCrCb.width() * bottomRectWidthPercentage),
    (int) (matYCrCb.height() * bottomRectHeightPercentage),
    rectangleWidth,
    rectangleHeight
);

//The rectangle is drawn into the mat
drawRectOnToMat(input, topRect, new Scalar(255, 0, 0));
drawRectOnToMat(input, bottomRect, new Scalar(0, 255, 0));
```

The first line will convert the input matrix color space from RGB to YCrCb. Because the way YCrCb represents color by luminance\(Y\), chroma of red\(CR\), chroma of blue\(Cb\), it keeps values consistent under different lighting. Next we draw 2 rectangles on screen with predetermined position. The top rectangle should be where the 4th ring will be, and the bottom one should be where the first one will be. Then we extract the Cb value of each predetermined area of the ring to compare.

### Finding CB Values

```java
topBlock = matYCrCb.submat(topRect);
bottomBlock = matYCrCb.submat(bottomRect);

Core.extractChannel(bottomBlock, matCbBottom, 2);
Core.extractChannel(topBlock, matCbTop, 2);

Scalar bottomMean = Core.mean(matCbBottom);
Scalar topMean = Core.mean(matCbTop);

bottomAverage = bottomMean.val[0];
topAverage = topMean.val[0];
```

Here we crop the mat to just everything inside the two rectangles. Then we find the average of the values and store them in `bottomAverage` and `topAverage`.

## Creating An Instance of `UGRectDetector`

The `UGRectDetector` is a class that will show how you would use the pipeline. For more in-depth explanation of what everything does or more functionalities, please visit [here](https://github.com/OpenFTC/EasyOpenCV/tree/master/examples/src/main/java/org/openftc/easyopencv/examples). To start, create an instance of `UGRectDetector`. The detector's constructor is overloaded. You can choose between:

```java
public UGRectDetector(HardwareMap hMap)
```

```java
public UGRectDetector(HardwareMap hMap, String webcamName)
```

* `hMap`: An instance of the hardware map
* `webcamName`: The webcam name

If you use the first constructor, the detector will set the camera to the phone's camera. If the second is used, the webcam will be used.

### Manipulating Detector Settings

You can change the orientation, width, and height of the camera for all instances \(since the camera doesn't change between runs\). You can update the settings by manipulating the static variables.

```java
// change the height and width of the camera
UGRectDetector.CAMERA_WIDTH = 320;
UGRectDetector.CAMERA_HEIGHT = 240;

// change the orientation of the camera
UGRectDetector.ORIENTATION = OpenCvCameraRotation.UPRIGHT;
```

### Setting Rectangle Positions

```java
public void setTopRectangle(double topRectHeightPercentage, double topRectWidthPercentage)
```

* `topRectHeightPercentage`: the percentage of the height of the user's input and should be a decimal under 1. It is used to calculate the first y value for the top rectangle. 
* `topRectWidthPercentage`: the percentage of the width of the user's input and should be a decimal under 1. It is used to calculate the first x value for the top rectangle.

```java
public void setBottomRectangle(double bottomRectHeightPercentage, double bottomRectWidthPercentage)
```

* `bottomRectHeightPercentage`: the percentage of the height of the user's input and should be a decimal under 1. It is used to calculate the first y value for the bottom rectangle. 
* `bottomRectWidthPercentage`: the percentage of the width of the user's input and should be a decimal under 1. It is used to calculate the first x value for the bottom rectangle.

```java
public void setRectangleSize(int rectangleWidth, int rectangleHeight)
```

* `rectangleWidth` : the width of the rectangles in terms of pixels
* `rectangleHeight` : the height of the rectangles in terms of pixels

After creating an instance of the detector and setting the rectangle positions, continuously run `DetectorInstance.getStack()` to get the number in the stack.

## `UGContourRingPipeline`

Vision Pipelines, the heart of any Ultimate Goal Detector. A pipeline is just a fancy way of saying a certain set of instructions that are applied to every inputted frame we see from the camera.

This is a Vision Pipeline utilizing Contours and an Aspect Ratio to determine the number of rings currently in the ring stack.

### Using the Detector

The contour pipeline comes with a premade detector that can be used out of the box in your opmode. The `UGContourRingDetector` is an object that runs the pipeline. You can [manipulate the pipeline settings](computer-vision.md#tuning) separately, but some of the settings of the detector get carried over to the pipeline.

To create an instance of the detector, there are different constructors, some with optional parameters.

```java
// creates a phone camera detector
detector = new UGContourRingDetector(
    hardwareMap, OpenCvInternalCamera.CameraDirection.BACK,
    telemetry, true
);

// creates a webcam detector
detector = new UGContourRingDetector(
    hardwareMap, "webcam"
);

// creates a webcam detector with telemetry debugging
detector = new UGContourRingDetector(
    hardwareMap, "webcam", telemetry, true
);
```

You can, like with the rectangle detector, manipulate the settings of the contour detector.

{% tabs %}
{% tab title="Java" %}
```java
UGContourRingDetector.PipelineConfiguration
    .setCAMERA_WIDTH(320);
UGContourRingDetector.PipelineConfiguration
    .setCAMERA_HEIGHT(240);
    
UGContourRingDetector.PipelineConfiguration
    .setHORIZON(100);
    
UGContourRingDetector.PipelineConfiguration
    .setCAMERA_ORIENTATION(OpenCvCameraRotation.UPRIGHT);
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
UGContourRingDetector.PipelineConfiguration.CAMERA_WIDTH = 320
UGContourRingDetector.PipelineConfiguration.CAMERA_HEIGHT = 240

UGContourRingDetector.PipelineConfiguration.HORIZON = 100

UGContourRingDetector.PipelineConfiguration.CAMERA_ORIENTATION = OpenCvCameraRotation.UPRIGHT
```
{% endtab %}
{% endtabs %}

To initialize the detector, simply call `init`.

```java
detector.init();
```

This initializes the pipeline with your configured settings. To retrieve the height determined by the pipeline, simply call `DetectorInstance.getHeight()`.

### Tuning

There are many values that the pipeline uses that can be changed/tuned to increase or decrease accuracy.

All configuration values are stored in a `companion object` called Config \(see [here](https://github.com/FTCLib/FTCLib/blob/master/core/vision/src/main/java/com/arcrobotics/ftclib/vision/UGContourRingPipeline.kt#L90-L110)\). In this, `companion object` there are six variables, two of which are constants and cannot be changed.

* `lowerOrange`: the value of the lower orange used in finding the mask
* `upperOrange`: the value of the upper orange used in finding the mask
* `CAMERA_WIDTH`: the width of the resolution of the camera
* `HORIZON`: the value representing the horizon, on the y-axis. used in the horizon check
* `MIN_WIDTH`: the algorithmically generated value used in the minimum width check
* `BOUND_RATIO`: the value that the aspect ratio checks to determine whether the ring stack is one and four.

{% hint style="info" %}
`HORIZON` will most likely be the value you will have to tune. Its default value may be too restrictive or it may not. This value will show up on the image as a red line. Anything above this red line will be ignored in the pipeline's calculations. Make sure that the bottom line of the ring stack's contour box is below the horizon line.

NOTE: the returned image from the pipeline will be majority black, this is to show the logic behind what the pipeline is ignoring. All contours will be drawn in green. The binding rectangle of the largest contour below the horizon will be drawn in blue.
{% endhint %}

{% hint style="warning" %}
Config is stored in a companion object, this means that every instance of the `UGContourRingPipeline` will share the same configuration.

These values and variables may change with future releases.
{% endhint %}

{% hint style="info" %}
Below is the explanation of the algorithm the Pipeline uses
{% endhint %}

### Receiving the Input

{% tabs %}
{% tab title="Java" %}
```java
public Mat processFrame(Mat input)
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
override fun processFrame(input: Mat?): Mat
```
{% endtab %}
{% endtabs %}

What the camera sees is being passed into the pipeline stored as an OpenCV `Mat` type \(short for matrix\).

### Manipulating the Input

{% hint style="info" %}
Kotlin only: `Mat?` is a nullable type of `Mat`, since the inputted frame could be null.
{% endhint %}

{% tabs %}
{% tab title="Java" %}
```java
Imgproc.cvtColor(input, mat, Imgproc.COLOR_RGB2YCrCb);
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
Imgproc.cvtColor(input, mat, Imgproc.COLOR_RGB2YCrCb)
```
{% endtab %}
{% endtabs %}

We first take this Mat and convert it to YCrCb to help with thresholding.

{% tabs %}
{% tab title="Java" %}
```java
// variable to store mask in
Mat mask = new Mat(mat.rows(), mat.cols(), CvType.CV_8UC1);
Core.inRange(mat, lowerOrange, upperOrange, mask);
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
val mask = Mat(mat.rows(), mat.cols(), CvType.CV_8UC1) // variable to store mask in
Core.inRange(mat, lowerOrange, upperOrange, mask)
```
{% endtab %}
{% endtabs %}

We then perform an inRange operation on the input Mat and store the result in a temporary variable called mask. This mask is a black and white image where all white pixels on the mask were pixels in input that are in the orange range threshold. All black pixels on the mask were pixels in the input that were not in the orange range threshold.

{% tabs %}
{% tab title="Java" %}
```java
Imgproc.GaussianBlur(mask, mask, Size(5.0, 15.0), 0.00)
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
Imgproc.GaussianBlur(mask, mask, Size(5.0, 15.0), 0.00)
```
{% endtab %}
{% endtabs %}

Next, using a GaussianBlur, we eliminate any noise between the rings on the stack. Due to how we are thresholding in the mask calculation, there may be some gaps in the stack, due to shadows or unwanted light sources.

{% hint style="info" %}
example of blurring in order to smooth images with Gaussian Blur: [here](https://docs.opencv.org/3.4/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html)
{% endhint %}

### Finding the Contours

After the GaussianBlur, this noise is eliminated as the picture becomes "blurrier". We then find all contours on the image.

{% hint style="info" %}
What is a Contour? Contours can be explained simply as a curve joining all the continuous points \(along the boundary\), having the same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

example of contours: [here](https://docs.opencv.org/3.4/df/d0d/tutorial_find_contours.html)
{% endhint %}

{% tabs %}
{% tab title="Java" %}
```java
List<MatOfPoint> contours = new ArrayList<>();
Mat hierarchy = new Mat();
Imgproc.findContours(mask, contours, hierarchy, Imgproc.RETR_TREE, Imgproc.CHAIN_APPROX_NONE);
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
val contours: List<MatOfPoint> = ArrayList()
val hierarchy = Mat()
Imgproc.findContours(mask, contours, hierarchy, Imgproc.RETR_TREE, Imgproc.CHAIN_APPROX_NONE)
```
{% endtab %}
{% endtabs %}

After finding the contours on the black and white mask, we then perform a linear search algorithm on the resulting list of contours \(stored in as MatOfPoint\). We first find the bounding rectangle of each contour and use this bounding rectangle \(not rotated\) to find the rectangle with the biggest width. We do this in order to not confuse the ring stack with other objects that may have been thought to be orange by the mask. Since the ring stack will most likely be the largest blob of orange in the view of the camera. When then do a check on the width of the widest contour. To see if it is actually a ring stack since zero is a valid option we must account for it. This check also makes sure that we don't mistake other smaller objects on the field as the ring stack, even if they are rings.

{% tabs %}
{% tab title="Java" %}
```java
int maxWidth = 0;
Rect maxRect = new Rect();
for (MatOfPoint c : contours) {
    MathOfPoint2f copy = new MatOfPoint2f(c.toArray());
    Rect rect = Imgproc.boundingRect(copy);

    int w = rect.width;
    // checking if the rectangle is below the horizon
    if (w > maxWidth && rect.y + rect.height > HORIZON) {
        maxWidth = w;
        maxRect = rect;
    }
    c.release(); // releasing the buffer of the contour, since after use, it is no longer needed
    copy.release(); // releasing the buffer of the copy of the contour, since after use, it is no longer needed
}
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
var maxWidth = 0
var maxRect = Rect()
for (c: MatOfPoint in contours) {
    val copy = MatOfPoint2f(*c.toArray())
    val rect: Rect = Imgproc.boundingRect(copy)

    val w = rect.width
    // checking if the rectangle is below the horizon
    if (w > maxWidth && rect.y + rect.height > HORIZON) {
        maxWidth = w
        maxRect = rect
    }
    c.release() // releasing the buffer of the contour, since after use, it is no longer needed
    copy.release() // releasing the buffer of the copy of the contour, since after use, it is no longer needed
}
```
{% endtab %}
{% endtabs %}

We also implemented a horizon check. Anything above the horizon is disregarded and not looked at even if it has the greatest width from all the other contours. This is to ensure that the algorithm down not detect the red goal as YCrCb color space is very unreliable when detecting the difference between red and orange.

### Calculating the Aspect Ratio

{% tabs %}
{% tab title="Java" %}
```java
double aspectRatio = maxRect.getHeight() / maxRect.getWidth();

height = maxWidth >= MIN_WIDTH ? aspectRatio > BOUND_RATIO ? FOUR : ONE : ZERO;

// equivalent
if (maxWidth >= MIN_WIDTH) {
    if (aspectRatio > BOUND_RATIO) {
        height = FOUR;
    } else {
        height = ONE;
    }
} else {
    height = ZERO;
}
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
height = if (maxWidth >= MIN_WIDTH) {
    val aspectRatio: Double = maxRect.height.toDouble() / maxRect.width.toDouble()

    /** checks if aspectRatio is greater than BOUND_RATIO 
     * to determine whether stack is ONE or FOUR
     */
    if (aspectRatio > BOUND_RATIO) 
        Height.FOUR // height variable is now FOUR
    else 
        Height.ONE // height variable is now ONE
} else {
    Height.ZERO // height variable is now ZERO
}
```
{% endtab %}
{% endtabs %}

After finding the widest contour, which is to be assumed the stack of rings, we perform an aspect ratio of the height over the width of the largest bounding rectangle.

{% hint style="info" %}
Possible Questions:

* Why not just count how tall the largest bounding rectangle is? 
  * It is because of camera resolution. Since depending on the resolution of the camera, the height of the stack in pixels would be different despite them both being 4 \(let's say for example\).
* Didn't you just say that you used a width check on the contour though? Isn't that also pixels? 
  * Yes. we did, however, unlike the height of the stack, the width of the stack is consistent. It is always one ring wide, this way we are able to algorithmically generate a minimum bounding width.
{% endhint %}

