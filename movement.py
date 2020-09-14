import cv2 as cv

cap=cv.VideoCapture(0)
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while True:
    diff=cv.absdiff(frame1, frame2)
    gray=cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray, (5,5), 0)
    _, thresh=cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    #thresh=cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11,8)
    dilated=cv.dilate(thresh, None, iterations=3)
    contours, _ =cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for contours in contours:
        (x,y,w,h)=cv.boundingRect(contours)
        if cv.contourArea(contours)<7000:
            continue
        elif cv.contourArea(contours)>100000:
            continue
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.putText(frame1, "Status: Movement", (10,20), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
        
    #cv.drawContours(frame1, contours, -1, (0,255,0))
    
    
    
    
    cv.imshow("inter", frame1)
    cv.imshow("diff", diff)
    cv.imshow("gray", gray)
    cv.imshow("blur", blur)
    cv.imshow("thresh", thresh)
    cv.imshow("dilated", dilated)
    frame1=frame2
    ret, frame2=cap.read()
    
    if cv.waitKey(40)==27:
        break

cv.destroyAllWindows()
cap.release()
