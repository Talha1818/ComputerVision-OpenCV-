import cv2
import numpy as np
import matplotlib.pyplot as plt
def fun(x):
    pass

img = cv2.imread('images/CBDAR_2.png', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Threshold')
cv2.createTrackbar('th1', 'Threshold',0,255,fun)
cv2.createTrackbar('th2', 'Threshold',0,255,fun)

while True:
    img = cv2.imread('images/our_dataset_4.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (540,540))
    # img = cv2.imread('images/ima22211-fig-0003-m.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('images/SH-ROSA-TL-DAPI-271120_B03_sx_4_sy_4_w1.tif', cv2.IMREAD_GRAYSCALE)
    # using biletral filter to minimize noise from image
    # img = cv2.bilateralFilter(img, 11, 17, 17)
    th1 = cv2.getTrackbarPos('th1','Threshold')
    th2 = cv2.getTrackbarPos('th2','Threshold')
    canny = cv2.Canny(img, th1, th2, apertureSize=3)
    cv2.imshow('th1',img)
    cv2.imshow('canyy',canny)

    k = cv2.waitKey(1)
    cv2.resize(img, (900,340))
    if k == ord('q'):
        break
cv2.destroyAllWindows()


