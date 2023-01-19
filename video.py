import cv2 as cv
import sys
import numpy as np

cap  = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'MP4V')
out = cv.VideoWriter('out.mp4', fourcc, 20.0, (640,  480))

font = cv.FONT_HERSHEY_SIMPLEX


if not cap.isOpened():
    print("Can not open camara")
    exit()
else:
    print("Camara is turing on .")
while True:
    ret, frame = cap.read()
    
    cv.putText(frame, "Recording...", (10, 50),
               font, 2, (235, 16, 16), 2, cv.LINE_AA)
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
out.release()
cv.destroyAllWindows()
