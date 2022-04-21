from random import gauss
import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# In generally, We smooth an image when it tends to have a lot of noise, and noise that's caused from camera sensors are basically problems in lighting when the image was taken.
# We can smooth out the image or reduce some of the noise by applying some blurring method.

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

cv.waitKey(0)
