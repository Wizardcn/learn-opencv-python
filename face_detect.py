from matplotlib import scale
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/group 1.jpg')
cv.imshow('Group of people', img)

# 1 convert BGR image to grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Persons in Grayscale', gray)

# face detection does not involve skin tone or the colors that are present in the image.
# These hard cascades essentially look at an object in an image and using the edges tries to determine whether it's a face or not.

# read haar_face.xml
haar_cascade = cv.CascadeClassifier('haar_face.xml')


img1 = img.copy()
minNeighbors = 3
faces_rect1 = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=minNeighbors)

print(f'Number of faces found = {len(faces_rect1)}')
for (x, y, w, h) in faces_rect1:
    cv.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow(f'Detected Faces with minimum neighbors = {minNeighbors}', img1)

# Haar cascades are really sensitive to noise in an image
# The way we can minimize the sensitivity to noise is essentially modifying the scale factor in minimum neighbors

img2 = img.copy()
minNeighbors = 6
faces_rect2 = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=minNeighbors)

print(f'Number of faces found = {len(faces_rect2)}')
for (x, y, w, h) in faces_rect2:
    cv.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)


cv.imshow(f'Detected Faces with minimum neighbors = {minNeighbors}', img2)

cv.waitKey(0)
