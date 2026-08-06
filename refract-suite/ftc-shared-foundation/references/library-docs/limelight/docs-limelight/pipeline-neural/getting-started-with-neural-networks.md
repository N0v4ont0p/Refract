> Source: https://docs.limelightvision.io/docs/docs-limelight/pipeline-neural/getting-started-with-neural-networks · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). All sitemap doc pages, unfiltered.
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Getting Started with Neural Networks | Limelight Documentation

 Skip to main content

 On this page

# Getting Started with Neural Networks

With Limelight's neural network pipelines, once-impossible computer vision challenges are now trivial. Learning-based vision already plays an enormous role in bleeding-edge robots and self-driving vehicles, so we are
excited to bring this technology to FIRST students.

 info
Limelight 1, 2, and 3 all support learning-based vision with the help of Google Coral. Google Coral is a USB accelerator that must be purchased separately.

Check out 2023 World Champion 1323's use of Limelight's Neural Network pipeline:

Download pretrained neural networks from our downloads page.

In FRC, teams have always wanted to track game pieces on the field during the autonomous and teleoperated periods.
Using Limelight's "Neural Detector" pipeline, teams are able to track pieces just like any other target with zero tuning.

"Neural Classifier" pipelines, on the other hand, allow teams to add advanced sensing capabilities to their robots.
Let's say a team wanted to determine whether their robot was in possession of a Red ball, a Blue ball, or not in possession of a ball.
A Limelight pointed inside a robot could run a classifier trained to determine one of these three cases. A classifier could also count the number of objects in a hopper, determine the state of a field feature, etc.

Neural Detector and Classifier networks require the addition of a Google Coral USB accelerator. The Google Coral Accelerator is an ASIC (application specific integrated circuit)
that is purpose-built for neural network inference. You can think of the term "inference" as "execution" or "running data through the neural network and producing an output".

If you are interested in building a deeper understanding of machine learning, we recommend starting with this video from 3blue1brown

Programmers can learn more in a hands-on fashion with the following book

## Neural Detector Pipeline​

To get started, ensure your Google Coral is plugged into the USB-A port on your Limelight.

Change "Pipeline Type" to "Neural Detector" to start running inference on the built-in test model. Download pretrained neural networks from our downloads page, and upload it to begin tracking game pieces.

Change the "confidence threshold" slider to adjust the required confidence for a successful detection.

Change the crop window to easily ignore objects outside of the desired detection zone.

## Neural Classifier Pipeline​

To get started, ensure your Google Coral is plugged into the USB-A port on your Limelight.

Change "Pipeline Type" to "Neural Classifier" to start running inference on the built-in test model. You can train your own classifier models using the method documented in the "Training" section.

The "Crop" window will allow you to better control the image used for neural network inference. While classifier models are capable of incredible levels of generalization in diverse environments, you will
see greater success by minimizing the number of variables in your image.

- Neural Detector Pipeline
- Neural Classifier Pipeline