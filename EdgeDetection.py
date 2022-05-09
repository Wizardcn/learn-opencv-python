from cv2 import CV_64F, threshold
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

cv.waitKey(0)
