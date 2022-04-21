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

# Median Blur
# In generally, Median blur tends to be more effective in reducing noise in an image as compared to averaging and even gaussian blur
# , and pretty good at removingsome salt and peper noise that may exist in the image.
# In general. people tend to use this image in advanced computer vision project that tend to depand on the reduction of substantial amount of noise.
median_k3 = cv.medianBlur(img, 3)
cv.imshow('Median Blur ksize=3', median_k3)

median_k7 = cv.medianBlur(img, 7)
cv.imshow('Median Blur ksize=7', median_k7)

# Bilateral Blur
# Bilateral Blur is the most effective, and sometimes used in a lot of advanced computer vision projects.
# because of how it blurs. bilateral blurring applies blurring but retains the edges in the image. So you have a blurred
# image, but you get to retain the edges as well.
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
