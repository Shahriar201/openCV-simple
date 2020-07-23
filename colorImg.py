import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
#print(img)

#Color the image of small part
#img[200:300, 100:300] = 255, 0, 0

#Draw a line shape
cv2.line(img, (0,0), (img.shape[0], img.shape[0]), (0, 255, 0), 3)

#Draw a rectangle shape
cv2.rectangle(img,(0,0), (250, 350), (0, 0, 255), 2)

#Circle
cv2.circle(img, (400, 100), 50, (255, 255, 0), 7)

#Write text on the images
cv2.putText(img, "Welcome", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 0), 1)

cv2.imshow("Images", img)
cv2.waitKey(0)

