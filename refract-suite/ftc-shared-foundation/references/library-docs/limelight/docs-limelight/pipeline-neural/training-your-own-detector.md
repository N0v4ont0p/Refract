> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-neural/training-your-own-detector · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Training a Custom Detector Model | Limelight Documentation

 Skip to main content

 On this page

# Training a Custom Detector Model

With Roboflow and the Limelight Neural Network Trainer, you can quickly train custom detector models for Limelight.

Here's an overview of the steps you will need to take:

- Collect and annotate images of objects of interest.

- In this context, "annotation" is the process of drawing bounding boxes around objects of interest. All of this can be done within Roboflow's web interface.

- Alternatively, you may select a public dataset from Roboflow Universe

- Export the annotated dataset as a .tfrecord, upload to Google Drive, and use our free training tool at https://tools.limelightvision.io/neural-network-trainer

## 1. Building the Dataset​

The Limelight Training Notebook expects a zipped .tfrecord dataset. Roboflow can export .tfrecord archives with one click.

You can build your own dataset with Roboflow, or browse Roboflow Universe for pre-annotated datasets.

If you opt to build your own dataset, read the following:

- 
You should maximize the diversity of your dataset. The diversity of your dataset should exceed the diversity of what your Limelight will see once deployed.

- 
The quality and accuracy of your dataset are of extreme importance. Make sure your bounding boxes are accurate and follow a single convention.
For example, a partially occluded object's bounding box should only capture the visible part of the object.

- 
Use all lowercase letters for class labels

- 
Minimize the number of class labels.

- 
Utilize Roboflow's augmentations, but make sure they make sense. If you are detecting red and blue balls, for example, make sure you are not inverting or heavily modifying hue in your augmented dataset.

Once you have labeled or found a dataset, use Roboflow's "Download Dataset" button to export it as a Tensorflow TFRecord. Upload this archive to your Google Drive.

## 2. Training the Model​

To train your custom detector, navigate to the Limelight Neural Network Trainer.

### Enter a link to your dataset and configure​

In google drive, make sure your dataset .tfrecord file is shared publically or with "anyone with the link". Copy the share link, and paste it into the trainer.

If you want to quickly test your model, set steps to 4000. If you've tested your model and want to try to increase accuracy, try 20000 steps. Make sure "Limelight CPU / Google Coral" is selected if you're using Limelight 3A. If you're using Hailo 8 or Hailo 8L, select the appropriate platform from the dropdown menu.

Click the "Start Training" button. The process may take up to 5 hours. Each session runs on a dedicated NVIDIA H100 GPU.

Once training is complete, click the "Download" button.

## 3. Uploading to Limelight​

- Unzip the archive after downloading.

- FTC Teams - If you have a Limelight3A, upload the 8bit tflite model and labels.txt. You will need to change the runtime engine from "coral" to "cpu"

- FRC Teams - If you have a google coral, upload the limelight_neural_detector_coral.tflite and the labels.txt files to your Limelight.

- 1. Building the Dataset
- 2. Training the Model- Enter a link to your dataset and configure

- 3. Uploading to Limelight