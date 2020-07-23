import cv2

cap = cv2.VideoCapture(0)

# set window width
cap.set(3, 640)

#set window height
cap.set(4, 480)

#brightness control
cap.set(10, 100)

#loop for capture all video pixel
while True:
    success, img = cap.read()
    cv2.imshow("My Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break