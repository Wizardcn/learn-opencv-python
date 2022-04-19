import cv2 as cv
from cv2 import INTER_AREA

img = cv.imread('./Resources/Photos/cat_large.jpg')


def changeResolution(capture, width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=INTER_AREA)


resized_img = rescaleFrame(img, 0.2)
cv.imshow('Cat', resized_img)
cv.waitKey(0)
