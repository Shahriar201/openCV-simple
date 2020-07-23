import cv2

img = cv2.imread("lambo.jpg")

#Cropped Images
imgCropped = img[0:300, 200:500]

cv2.imshow("Cropped Images", imgCropped)
cv2.waitKey(0)