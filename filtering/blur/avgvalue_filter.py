import sys
import cv2 as cv
import numpy as np
 
# kernel = 1/(ksize.width * ksize.height) * [[1...1]....[1...1]]

def control_ksize(ksize):
    if ksize <= 0:
        ksize=1
        
    dst = cv.blur(src, (ksize, ksize))
    cv.putText(dst, f'mean: {ksize}x{ksize}', (10, 30),cv.FONT_HERSHEY_SIMPLEX, 1, 255, 1, cv.LINE_AA)
    cv.imshow('main', np.concatenate((src, dst), axis=1))

path = # img path
src = cv.imread(path, cv.IMREAD_GRAYSCALE)

if src is None:
    print('img load failed')
    sys.exit()

cv.namedWindow('main')
cv.createTrackbar('ksize', 'main', 1, 20, control_ksize)
control_ksize(1)
cv.waitKey()
cv.destroyAllWindows()