import cv2 as cv
import numpy as np

# Use Affine Transformaions technique
# https://neutrium.net/mathematics/basics-of-affine-transformation/


def main():
    img = cv.imread('./Resources/Photos/park.jpg')
    # cv.imshow('Park', img)

    # translated = translate(img, 100, 100)
    # cv.imshow('Translated', translated)

    rotated = rotate(img, 45)
    cv.imshow('Rotated', rotated)

    cv.waitKey(0)


def translate(img, x, y):
    '''
        Translation: is basically shifting an image along the x and y axis up, down, left, right
        - -x --> left
        - -y --> up
        - x --> right
        - y --> down
    '''
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


def rotate(img, angle, rotPoint=None):
    """
        Specify any rotation point that you'd like to rotate the image around 
    """
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


if __name__ == "__main__":
    main()
