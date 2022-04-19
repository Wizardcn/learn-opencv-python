import cv2 as cv

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur: remove some of the noise that exists in an image
# use gaussian blur technique
# to increase blur -> increase the kernel size
blur_k3 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur kernel size 3', blur_k3)

blur_k7 = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur kernel size 7', blur_k7)

# Edge Cascade
# use canny edge detection
# can reduce some of these edges by blurring the image
canny = cv.Canny(blur_k7, 125, 175)
cv.imshow('Canny Edges', canny)


cv.waitKey(0)
