import numpy as np
import cv2
import cv2 as cv

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
capture = cv.VideoCapture(
    './Resources/Videos/dog.mp4')

# Read until video is completed
while True:
    # Capture frame-by-frame
    isTrue, frame = capture.read()
    if isTrue == False:
        print('cannot read frame')

    # Display the resulting frame
    cv.imshow('Video', frame)

    # Press D on keyboard to  exit
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# When everything done, release the video capture object
capture.release()

# Closes all the frames
cv.destroyAllWindows()
