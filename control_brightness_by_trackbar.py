import cv2 as cv
import numpy as np
import sys

def sturate(value):
    value[value>255] = 255
    value[value<0] = 0
    return value

def control(pos):
    if pos > 255: pos = pos-255
    else: pos = pos-255
    dst = sturate(cv.add(src, pos))
    cv.imshow('dst', dst)

path = 'img/Lenna.png'
src = cv.imread(path, cv.IMREAD_GRAYSCALE)
if src is None:
    print('img load failed')
    sys.exit()

cv.namedWindow('dst')
cv.createTrackbar('brightness', 'dst', 255, 500, control)
control(255)
cv.waitKey()
cv.destroyAllWindows()