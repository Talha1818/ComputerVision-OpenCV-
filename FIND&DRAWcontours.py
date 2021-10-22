import cv2
import numpy as np

img = cv2.imread('images/our_dataset_4.jpg',1)
img = cv2.resize(img, (512, 512))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGrayq = cv2.resize(imgGray, (512, 512))

ret, thresh = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
contours, hierchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Total Contours : ", len(contours))
# print(contours[0])

cv2.drawContours(img, contours, -1, (255,150,120), 6)
cv2.imshow('Image', img)
cv2.imshow('ImageGray', imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()