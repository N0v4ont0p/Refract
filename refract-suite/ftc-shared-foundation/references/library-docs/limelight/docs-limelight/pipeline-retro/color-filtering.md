> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-retro/color-filtering · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Color Thresholding | Limelight Documentation

 Skip to main content

 On this page

# Color Thresholding

Thresholding is a critical component of most vision tracking algorithms. It is the act of taking an image, and throwing away any pixels that aren't within a specific color range. The result of thresholding is generally a one-dimensional binary image in which every pixel is either "on" or "off. In color blob / retroreflective pipelines, this is the most critical step.

### Video Feed (Located beneath stream)​

Controls which image is streamed from the mjpeg server. You should switch to the "threshold" image if you need to tune your HSV thresholding.

### Thresholding Wands​

Wands enable users to click on Limelights's video stream to perform automatic HSV thresholding.

- The "Eyedropper" wand centers HSV parameters around the selected pixel

- The "Add" wand adjusts HSV parameters to include the selected pixel

- The "Subtract" wand adjust HSV parameters to ignore the selected pixel

### Hue​

Describes a "pure" color. A Hue of "0" describes pure red, and a hue of 1/3 (59 on the slider) describes pure green. Hue is useful because it doesn't change as a pixel "brightens" or "darkens". This is the most important parameter to tune. If you make your hue range as small as possible, you will have little if any trouble transitioning to an actual FRC field.

### Saturation​

Describes the extent to which a color is "pure". Another way to think of this is how washed-out a color appears, that is, how much "white" is in a color. Low saturation means a color is almost white, and high saturation means a color is almost "pure".

### Value​

Describes the darkness of a color, or how much "black" is in a color. A low value corresponds to a near-black color. You should absolutely increase the minimum value from zero, so that black pixels are not passed through the processing pipeline.

### Erosion and Dilation​

Erosion slightly erodes the result of an HSV threshold. This is useful if many objects are passing through a tuned HSV threshold. Dilation slightly inflates the result of an HSV threshold. Use this to patch holes in thresholding results.

### Hue Inversion​

Use hue inversion to track red targets, as red exists at both the beginning and the end of the hue range.

- Video Feed (Located beneath stream)
- Thresholding Wands
- Hue
- Saturation
- Value
- Erosion and Dilation
- Hue Inversion