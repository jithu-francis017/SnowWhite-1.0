import cv2
import numpy as np


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test_image.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw 3D transparent boxes around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.line(img, (x, y), (x+w//4, y-h//4), (255, 0, 0), 2)
    cv2.line(img, (x+w, y), (x+3*w//4, y-h//4), (255, 0, 0), 2)
    cv2.line(img, (x, y), (x, y-h//4), (255, 0, 0), 2)
    cv2.line(img, (x+w, y), (x+w, y-h//4), (255, 0, 0), 2)
    cv2.line(img, (x, y-h//4), (x+w//4, y-3*h//4), (255, 0, 0), 2)
    cv2.line(img, (x+w//4, y-3*h//4), (x+3*w//4, y-3*h//4), (255, 0, 0), 2)
    cv2.line(img, (x+w, y-h//4), (x+3*w//4, y-3*h//4), (255, 0, 0), 2)
    pts = np.array([[x, y], [x+w, y], [x+w, y-h], [x, y-h]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts],(255,255,255))

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
