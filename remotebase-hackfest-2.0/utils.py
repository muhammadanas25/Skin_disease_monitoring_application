import numpy as np
import cv2


def resize_img(img):
    scale_percent = 15  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def get_threshold(image):

    l = [pv for pv in image.ravel() if pv > 0]
    hist, bins = np.histogram(l, 255)
    thresh = 2

    while True:
        low_thresh = low_total = 0
        for i in range(thresh):
            low_total += hist[i]
            low_thresh += hist[i] * i

        high_thresh = high_total = 0
        for i in range(thresh + 1, 255):
            high_total += hist[i]
            high_thresh += hist[i] * i

        if low_total > 0 and high_total > 0:
            low_thresh = int(low_thresh / low_total)
            high_thresh = int(high_thresh / high_total)
            if thresh == int(round((low_thresh + high_thresh) / 2.0)):
                break

        thresh += 1
    return thresh, hist, bins


def remove_background(image, mask):
    return cv2.bitwise_and(image, mask)
