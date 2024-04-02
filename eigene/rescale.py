import cv2 as cv

def changeRes(width, height):
   # only works for live video!
   capture.set(3, width)
   capture.set(4, height)

def rescaleFrame(frame, scale=0.75):
  # will work for images, videos and live video
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def rescaleProportionally(frame, new_width=700):
   width = frame.shape[1]
   height = frame.shape[0]
   factor = width / height

   dimensions = (new_width, int(new_width / factor))
   return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# scaling images
# img = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', rescaleFrame(img))
# cv.waitKey(0)

# scaling videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
# capture = cv.VideoCapture(0) # not working in wsl
while True:
    isTrue, frame = capture.read()

    frame_rescaled = rescaleProportionally(frame, new_width=320)
    # shows every frame of the video frame by frame
    cv.imshow('video', frame_rescaled)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break;

capture.release()
cv.destroyAllWindows()