import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

"""
Coutours are basically the boundaries of objects, the line or curve that joins the continuous points along the boundary of an object
- In mathematical point of view, contours and edges are two different things
- But the most part, you can get away with thinking of contours as edges
- Contours are useful tools when you get into shape analysis and object detection and recognition
"""

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)


# The way that is used to find the contours of an image is by using the find contours method.
contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found.')

cv.waitKey(0)
