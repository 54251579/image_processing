import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt

def calc_gray_hist(img):
    channels = [0]
    hist_size = [256]
    hist_range = [0, 256]

    hist = cv.calcHist([img], channels, None, hist_size, hist_range)

    return hist

path = # img path
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

if img is None:
    print('img load failed')
    sys.exit()

cv.imshow('img', img)

hist = calc_gray_hist(img)

plt.bar(np.arange(len(hist.T[0])), hist.T[0])
plt.show()
cv.waitKey()
cv.destroyAllWindows()