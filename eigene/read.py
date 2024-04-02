import cv2 as cv

# reads and displays images
# img = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow('cat', img)
# cv.waitKey(0)

# reads and displays videos
# numbers instead of a path to a video could be used to reference a camera built
# into the system. 0 for the standard webcam f.e.
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    # shows every frame of the video frame by frame
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break;

capture.release()
cv.destroyAllWindows()
