import cv2 as cv

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

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
print(cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


cv.waitKey(0)
