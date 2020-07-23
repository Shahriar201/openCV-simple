import cv2
import numpy as np

img = cv2.imread("lana.png")

kernel = np.ones((5,5), np.uint8)

#convert gray schale color
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur color
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

#edges detector of the images
imgCanny = cv2.Canny(img, 150, 200)

#Dialation of the canny images
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

#More thikness using errod images
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Gray Images", imgGray)

cv2.imshow("Blur Images", imgBlur)

cv2.imshow("Canny Images", imgCanny)

cv2.imshow("Dialation Images", imgDialation)

cv2.imshow("Eroded Images", imgEroded)

cv2.waitKey(0)