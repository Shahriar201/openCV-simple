import cv2

img = cv2.imread("lambo.jpg")
print(img.shape)

#set size of the image
imgResize = cv2.resize(img, (650, 400))

cv2.imshow("Images Size", img)
cv2.imshow("Resize Image", imgResize)
cv2.waitKey(0)