import cv2 as cv
import numpy as np

# create dummy image or blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a certain colour
#                         B  G    R
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)

cv.waitKey(0)
