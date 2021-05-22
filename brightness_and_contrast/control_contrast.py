import cv2 as cv
import numpy as np
import sys

def control(alpha):
    if alpha > 10: alpha-=10
    else: alpha -= 10
    dst = cv.convertScaleAbs(src, alpha = alpha/10+1, beta = -128 * alpha/10)
    cv.imshow('dst', dst)

path = # img path
src = cv.imread(path, cv.IMREAD_GRAYSCALE)

if src is None:
    print('img read failed')
    sys.exit()

cv.namedWindow('dst')
cv.createTrackbar('alpha', 'dst', 0, 20, control)

cv.waitKey()
cv.destroyAllWindows()