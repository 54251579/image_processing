import sys
import cv2 as cv
import numpy as np

def change(pos):
    pass

path = 'img/Lenna.png'
src = cv.imread(path, cv.IMREAD_GRAYSCALE)

if src is None:
    print('img load failed')
    sys.exit()

cv.namedWindow('main')
cv.createTrackbar('sigma', 'main', 1, 100, change)
cv.createTrackbar('alpha', 'main', 1, 100, change)
while True:
    sigma = cv.getTrackbarPos('sigma', 'main')
    if sigma <= 0: sigma = 1
    alpha = cv.getTrackbarPos('alpha', 'main')/100

    blurred = cv.GaussianBlur(src, (0, 0), sigma)

    dst = cv.addWeighted(src, 1+alpha, blurred, -alpha, 0)

    cv.putText(dst, f'sigma: {sigma}', (10, 30),cv.FONT_HERSHEY_SIMPLEX, 1, 255, 1, cv.LINE_AA)
    cv.putText(dst, f'alpha: {alpha}', (10, 60),cv.FONT_HERSHEY_SIMPLEX, 1, 255, 1, cv.LINE_AA)
    cv.imshow('main', np.concatenate((src, dst), axis=1))
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()