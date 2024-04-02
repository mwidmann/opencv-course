import cv2 as cv
import numpy as np

# reads and displays images
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('park', img)

# Translation
def translate(img, x, y):
  transMat = np.float32([[1,0,x], [0,1,y]])
  dimensions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMat, dimensions)

cv.imshow('translated', translate(img, 50, 50))
cv.imshow('translated-negatively', translate(img, -50, -50))

# Rotating
def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]

  if rotPoint is None:
    rotPoint = (width//2, height//2)

  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width, height)
  return cv.warpAffine(img, rotMat, dimensions)

cv.imshow('rotated', rotate(img, 45))

# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('rotated', resized)

# flipping
# 0 = vertically
# 1 = horizontally
# -1 = both
flip = cv.flip(img, -1)
cv.imshow('flipped', flip)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)