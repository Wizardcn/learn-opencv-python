import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')

# cv.imshow('Park', img)

# Translation: is basically shifting an image along the x and y axis up, down, left, right
# Use Affine Transformaions technique
# https://neutrium.net/mathematics/basics-of-affine-transformation/


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

cv.waitKey(0)
