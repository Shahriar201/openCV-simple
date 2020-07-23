import cv2

import numpy as np

img = cv2.imread("girl.png")

#Duplicate images on horizontal
imgHor = np.hstack((img, img))

#Duplicate images on vertical
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal Images", imgHor)
cv2.imshow("Vertical Images", imgVer)
cv2.waitKey(0)