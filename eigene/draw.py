import cv2 as cv
import numpy as np

# creates a blank image 500x500 px
blank = np.zeros((500, 500, 3), dtype='uint8')

# img = cv.imread('../Resources/Photos/cat.jpg')

# 1. paint the image a certain color
blank[:] = 0,255,0
# paint only a part of the image
blank[200:300, 300:400] = 0,0,255

# 2. Draw a Rectangle
cv.rectangle(blank, (10,10), (250, 250), (255,0,0), thickness=2)
# for filling
cv.rectangle(blank, (50,50), (150, 150), (255,255,255), thickness=cv.FILLED)

# 3. Draw a circle
# the operator // does a math.floor
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 50, (128,128,128), thickness=3)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,0,0), thickness=3)

# 5. Write text
cv.putText(blank, 'Hello, World', (50, 225), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0,0,0), thickness=2)

cv.imshow('Blank', blank)

cv.waitKey(0)