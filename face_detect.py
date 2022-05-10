from matplotlib import scale
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/lady.jpg')
cv.imshow('Person', img)

# 1 convert BGR image to grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person in Grayscale', gray)

# face detection does not involve skin tone or the colors that are present in the image.
# These hard cascades essentially look at an object in an image and using the edges tries to determine whether it's a face or not.

# read haar_face.xml
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)


cv.imshow('Detected Faces', img)

cv.waitKey(0)
