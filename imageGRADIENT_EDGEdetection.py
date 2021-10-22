import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/our_dataset_4.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=1)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
canny = cv2.Canny(img, 0, 118)

titles = ['ORIGINAL', 'LAPLACIAN', 'SOBELX', 'SOBELY', 'SOBELCOMBINED-XY', 'CANYY']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]
row, col = 3, 2
n = 6
for i in range(n):
    plt.subplot(row, col, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(2)
cv2.destroyAllWindows()