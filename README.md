# Facial-Recognition-System

This project implements a facial recognition system using Python, designed to detect and recognize faces in images efficiently and accurately. The system combines OpenCV for image handling and preprocessing with the face_recognition library for face detection and feature encoding.

Overview

The system works as follows:

Image Acquisition & Preprocessing:
OpenCV is used to read images and prepare them for facial analysis. Preprocessing ensures that faces are detected reliably under varying lighting conditions and image qualities.

Face Detection & Encoding:
Using the face_recognition library, the system locates faces within an image and encodes each detected face into a 128-dimensional feature vector. This encoding captures the unique facial characteristics of each individual.

Face Matching:
Unknown face encodings are compared against a database of known face encodings. The comparison uses Euclidean distance to measure similarity between feature vectors. A tolerance parameter is applied to determine if a detected face matches a known individual. This allows the system to accurately recognize or verify identities.

Result Output:
Boxes outline faces in input image displaying the name of the unknown detected face.

Future features:
Deep learning image dataset
Video processing (currently only support image processing)
