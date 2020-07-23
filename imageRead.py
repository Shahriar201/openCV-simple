import cv2

print("Imported Package")

img = cv2.imread("lana.png")

cv2.imshow('First Images', img)
cv2.waitKey(0)
