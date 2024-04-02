import cv2 as cv
import numpy as np

# reads and displays images
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# first variant -> recommended
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blurred', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# second variant
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found.')

blank = np.zeros(img.shape, dtype='uint8')
drawn_contours = cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow('Contours', drawn_contours)


cv.waitKey(0)