# Facial Recognition System

A lightweight facial recognition project in **Python** that detects faces in images and recognizes them against a set of known identities. It uses:

- **OpenCV** for image I/O and drawing bounding boxes / labels  
- **face_recognition** (dlib-based) for face detection and 128‑D face encodings

> **Note:** This project currently supports **image** recognition. Video/webcam support is listed under future work.

---

## Features

- Detect one or more faces in an input image
- Encode known faces into reusable embeddings
- Match unknown faces to known identities using a configurable tolerance
- Choose between detection models:
  - **CNN** (more accurate, slower, may require more resources)
  - **HOG** (faster, less accurate)

---

## Project Structure

A typical layout looks like this:

```
Facial-Recognition-System/
├─ dataset/
│  ├─ Alice/
│  │  ├─ img1.jpg
│  │  └─ img2.png
│  └─ Bob/
│     └─ bob_01.jpg
├─ encodings/               # (recommended) where you save computed encodings
├─ facial_recognition.py
├─ encode_dataset.py        # (if you have a separate script; see "Encoding Known Faces")
└─ README.md
```

Your **known faces** should be organized as:

```
dataset/<person_name>/<image_files>
```

The folder name is treated as the label (the person’s name).

---

## Requirements

- Python **3.9+** recommended
- A working C/C++ build toolchain is helpful on some platforms (for `dlib`)

Python packages:
- `opencv-python`
- `face_recognition` (includes `dlib` dependency)

---

## Setup

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd Facial-Recognition-System
```

### 2) Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
python -m pip install --upgrade pip
pip install opencv-python face_recognition
```

> If `dlib` fails to install, see **Troubleshooting** below.

---

## Prepare Your Dataset

1. Create a `dataset/` folder at the project root (if it doesn’t exist).
2. Add one folder per person.
3. Put multiple clear images of that person inside the folder.

Example:

```
dataset/
├─ Alice/
│  ├─ alice1.jpg
│  ├─ alice2.jpg
└─ Bob/
   ├─ bob1.jpg
```

Tips:
- Use front-facing images when possible.
- Include slight variations (lighting, angle) to improve matching.

---

## Encoding Known Faces

You need to compute face encodings for your known dataset once (or whenever you change the dataset).  
How you do this depends on your scripts. Common patterns are:

### Option A: If you have a separate encoding script (recommended)
Run something like:

```bash
python encode_dataset.py --dataset dataset --output encodings/known_encodings.pkl
```

### Option B: If `facial_recognition.py` supports an “encode” mode
Run:

```bash
python facial_recognition.py --dataset dataset --save-encodings encodings/known_encodings.pkl
```

If your repository only has one script, consider adding a small `encode_dataset.py` so users can generate encodings without running recognition each time.

---

## Run Recognition on an Image

Run recognition using your saved encodings and a target image:

```bash
python facial_recognition.py --encodings encodings/known_encodings.pkl --image path/to/input.jpg --model hog
```

### Common flags (typical)
Your exact CLI arguments may differ depending on your implementation, but these are common:

- `--image`: path to the input image
- `--encodings`: path to saved encodings (e.g., `.pkl`)
- `--dataset`: path to dataset folder (only needed for encoding)
- `--model`: `hog` or `cnn`
- `--tolerance`: float threshold (lower = stricter matching)

**Tolerance guidance:**
- `0.6` is a common default used in many face_recognition examples.
- Lower (e.g., `0.5`) reduces false positives but may increase “Unknown” results.
- Higher (e.g., `0.65`) increases matches but can increase misidentifications.

---

## Output

The program will produce an output image (or display a window, depending on your code) with:

- Bounding boxes drawn around detected faces
- A label (matched name or **Unknown**) rendered near each box

---

## Troubleshooting

### `dlib` installation issues
`face_recognition` depends on `dlib`, which can be the main source of installation problems.

- Ensure you’re using a supported Python version (3.9+ recommended).
- Upgrade pip/setuptools/wheel:

```bash
python -m pip install --upgrade pip setuptools wheel
```

- On some systems, installing build tools (e.g., CMake / compiler toolchain) may be required.

If you want this README to be extremely beginner-friendly, consider adding OS-specific instructions (Windows/macOS/Linux) once you confirm your target audience.

---

## Future Improvements

- Video/webcam processing
- More robust dataset tooling (auto-cleaning, face quality checks)
- Deep learning-based recognition pipeline and/or training workflow

---

## License

Add a license file (e.g., MIT) if you plan to share this publicly.

---

## Acknowledgements

- OpenCV
- face_recognition (dlib-based face recognition utilities)
