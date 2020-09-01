import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', 0)
_, mask=cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal=np.ones((5,5), np.uint8)
dilation=cv.dilate(mask, kernal, iterations=3)
erosion= cv.erode(dilation, kernal, iterations=3)

titles=['image', 'mask', 'dilation', 'erosion']
images=[img, mask, dilation, erosion]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
