import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

b, g, r = cv.split(img)
# in each color channels are depicted and displayed as grayscale images that show the distribution of pixel intensities.
# regions where it's lighter showed that there is a far more concentration of those pixel value
# regions where it's darker represened a little or even no pixels in that region.

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
