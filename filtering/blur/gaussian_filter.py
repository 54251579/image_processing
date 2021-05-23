import sys
import cv2 as cv
import numpy as np

def control_sigma(sigma):
    if sigma <= 0:
        sigma=1  
    dst = cv.GaussianBlur(src, (0, 0), sigma)
    cv.putText(dst, f'sigma: {sigma}', (10, 30),cv.FONT_HERSHEY_SIMPLEX, 1, 255, 1, cv.LINE_AA)
    cv.imshow('main', np.concatenate((src, dst), axis=1))

path = # img path
src = cv.imread(path, cv.IMREAD_GRAYSCALE)

if src is None:
    print('img load failed')
    sys.exit()

cv.namedWindow('main')
cv.createTrackbar('sigma', 'main', 1, 20, control_sigma)
control_sigma(1)
cv.waitKey()
cv.destroyAllWindows()