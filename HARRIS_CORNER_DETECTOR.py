import cv2
import numpy as np

# img = cv2.imread('images/chessboard.png', 1)
img = cv2.imread('images/our_dataset_4.jpg', 1)
# img = cv2.imread('images/left09.jpg', 1)
img = cv2.resize(img, (512, 512))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
img [dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()