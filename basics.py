import cv2 as cv

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur: remove some of the noise that exists in an image
# Kernel size should be odd number.
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
# cv.imshow('Canny Edges', canny)

# Dilating the image
# use to increase thickness edges of image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
# use to restructure the edges of image
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize
# By default there is an interpolation that occurs in the background
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# This interpolation method is useful if you are shrinking the image to dimensions that are smaller than that of the originall dimensions.
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
