import numpy as np
import cv2

cap = cv2.VideoCapture('../output/output.avi')

if cap.isOpened():
    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
else:
    print("can't open camera")

cap.release()
cv2.destroyAllWindows()