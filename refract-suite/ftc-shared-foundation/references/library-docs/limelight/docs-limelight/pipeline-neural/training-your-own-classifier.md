> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-neural/training-your-own-classifier · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Training a Custom Classifier Model | Limelight Documentation

 Skip to main content

 On this page

# Training a Custom Classifier Model

Google's Teachable Machine is a browser-based tool that allows users to create classifier models without any code or advanced understanding of machine learning.

## Data Collection​

Gather images for each class you want to recognize.
Ensure that you have a balanced dataset (a roughly equal number of images for each class).
Ensure you have diversity in camera angle, lighting, backgrounds, object characteristics, etc.

## Training with Teachable Machine​

Go to the Teachable Machine website: teachable machine

- Click on the “Get Started” button.

- Select the “Image Project” to create an image classifier.

- Select "Standard image model"

- For each class:

- Click on the 'Add Class' button.

- Upload the images pertaining to that class.

- After adding all classes, click on the “Train Model” button.

- Once training is complete, you can test the model right in the browser.

- Click the "Export Model" Button

- Navigate to the "Tensorflow Lite" tab

- Select "EdgeTPU" if you have a Limelight Google Coral

- Select "Quantized" if you are using a Limelight 3A for FTC or you are using CPU Neural Network functionality.

- Download the model.

- Data Collection
- Training with Teachable Machine