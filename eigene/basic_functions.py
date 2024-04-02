import cv2 as cv

# reads and displays images
img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur image
blurred = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blurred', blurred)

# edge cascade
canny = cv.Canny(blurred, 125, 175)
cv.imshow('canny edges', canny)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('dilated edges', dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded edges', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)
