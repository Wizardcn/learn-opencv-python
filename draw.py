import cv2 as cv
import numpy as np

# create dummy image or blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# 2. Draw a Rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2,
          blank.shape[0]//2), 40, (0, 0, 255), thickness=3)

# 4. Draw a line
cv.line(blank, (10, 100), (blank.shape[1]//2,
        blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)
cv.waitKey(0)
