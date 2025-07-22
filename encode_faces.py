from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# These are for command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True, help="input directory to faces and images")
ap.add_argument("-e", "--encodings", required=True, help="path to db or facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn", help="facial detection method: either hog or cnn")

# Parse args and put them into a dict format
args = vars(ap.parse_args())

# Extract and list all the images in dataset
imagePaths = list(paths.list_images(args["dataset"]))

knownEncodings = []
knownNames = []

for (index, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(index + 1, len(imagePaths)))
    # Extract name of person
    name = imagePath.split(os.path.sep)[-2] # Assuming the path is dataset/name/image

    # Extract image and convert it from BGR to RGB so dlib can read it
    imageBGR = cv2.imread(imagePath)
    imageRGB = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(imageRGB, model=args["detection_method"]) # Creates bounds on faces

    encodings = face_recognition.face_encodings(imageRGB, boxes)

    for encoding in encodings:
        knownEncodings.append(encodings)
        knownNames.append(name)

# Need to store encodings in an encoding file

data = {"encodings" : knownEncodings, "names" : knownNames}

f = open(args["encodings"], "wb")

f.write(pickle.dumps(data))
f.close()
