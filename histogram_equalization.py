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

def equalizatoin(src):
    dst = cv.equalizeHist(src)

    src_hist = calc_gray_hist(src)
    dst_hist = calc_gray_hist(dst)

    plt.subplot(221).axis('off')
    plt.title('src')
    plt.imshow(src, cmap=plt.cm.gray)
    plt.subplot(222).axis('off')
    plt.title('dst')
    plt.imshow(dst, cmap=plt.cm.gray)
    plt.subplot(223)
    plt.title('src historgram')
    plt.bar(np.arange(len(src_hist.T[0])), src_hist.T[0])
    plt.subplot(224)
    plt.title('dst historgram')
    plt.bar(np.arange(len(dst_hist.T[0])), dst_hist.T[0])

    plt.show()

path = 'img/ch.png'
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

if img is None:
    print('img load failed')
    sys.exit()

equalizatoin(img)

cv.waitKey()
cv.destroyAllWindows()