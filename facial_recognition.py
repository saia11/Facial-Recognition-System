import face_recognition
import argparse
import pickle
import cv2
import numpy

# Load command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True, help="path to encodings")
ap.add_argument("-i", "--image", required=True, help="path to image for detection")
ap.add_argument("-d", "--detection-method", type=str, default="cnn", help="detection method, either hog or cnn")
args = vars(ap.parse_args())

# Get encoding data
print("[INFO] loading encodings...")
encodingData = pickle.loads((open(args["encodings"], "rb")).read())

# Read input image to detect and convert to RGB
imageBGR = cv2.imread(args["image"])
imageRGB = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)

# Detect boundary boxes of input image and encode 128 vectors
print("[INFO] recognizing faces...")
inputImageBoxes = face_recognition.face_locations(imageRGB, model=args["detection_method"])
inputImageEncodings = face_recognition.face_encodings(imageRGB, inputImageBoxes)

names = []

# Attempt to match an encoding from input image to known encodings and get most likely name
for encoding in inputImageEncodings:
    matches = face_recognition.compare_faces(encodingData["encodings"], encoding)
    name = "Unknown"
    print(matches)

    if True in matches:
        matchedIndexes = [i for (i, b) in enumerate(matches) if b]
        counts = {}

        for i in matchedIndexes:
            name = encodingData["names"][i]
            counts[name] = counts.get(name, 0) + 1

        name = max(counts, key=counts.get)
    names.append(name)

for ((top, right, bottom, left), name) in zip(inputImageBoxes, names):
    cv2.rectangle(imageBGR, (left, top), (right, bottom), (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(imageBGR, name, (left, y), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 255, 0), 2)

cv2.imshow("Image", imageBGR)
cv2.waitKey(0)
