import cv2 as cv
import numpy as np
import sys

path = # img path
src = cv.imread(path, cv.IMREAD_GRAYSCALE)

if src is None:
    print('img load failed')
    sys.exit()

emboss = np.array([
    [-1,-1,0],
    [-1,0,1],
    [0,1,1]
], dtype=np.float32)

dst = cv.filter2D(src, -1, emboss, delta=128)
cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey()
cv.destroyAllWindows()