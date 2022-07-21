import cv2
from Human_Detection import Detector

cap = cv2.VideoCapture('demo.avi')

while True:
    ret, frame = cap.read()

    frame = Detector(frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
