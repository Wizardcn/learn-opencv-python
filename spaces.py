import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

"""
    How to switch between color spaces in opencv
    
    Color Spaces: a system of representing an array of pixel colors
    - RGB is a kind of space, grayscale is color space.
    - HSV, and many more.
"""

# BGR to Grayscale
# Grayscale images show the distribution of pixel intensities at particular locations of the images.
# cv.COLOR_BGR2GRAY = 6
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# BGR to HSV
# HSV is called Hue Saturation Value and is kind of based on how humans think and conceive of color.
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR isn't the current system that we use to represent colors outside of opencv.
# Outside of opencv, we use the RGB format, which id kind of like the inverse of BGR.

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()
# matplotlib: plt.imshow() will not inverse input image.
# opencv: cv.imshow() will assume input image is BGR space and inverse to RGB to display on the screen.

# cannot convert grayscale image to HSV directly
# the way you can do that convert the grayscale image to BGR and then convert the BGR image to HSV
# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)


cv.waitKey(0)
