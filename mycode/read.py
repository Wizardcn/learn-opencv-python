import cv2 as cv
import numpy as np

cat_img = cv.imread('../Resources/Photos/cat.jpg')
print(cat_img.shape)
cv.imshow("Cat", cat_img)

cat2_img = cv.imread('../Resources/Photos/cat_large.jpg')
print(cat2_img.shape)
cv.imshow("Cat2", cat2_img)

cv.waitKey(0)
