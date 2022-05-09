from cv2 import threshold
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# convert BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Simple Thesholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thesholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Thesholded', thresh_inv)

cv.waitKey(0)
