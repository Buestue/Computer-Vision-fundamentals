import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)


while(True):
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     lr = cv.pyrDown(frame)
#     lr2 = cv.pyrDown(lr)
#     up = cv.pyrUp(lr2)
#     up2 = cv.pyrUp(up)

    for i in range(2):
        frame=cv.pyrDown(frame)
    for i in range(2):
        frame=cv.pyrUp(frame)
    
        

    cv.imshow('frame', frame)
    
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
