import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
points = [(0,0)]

def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        

while(True):
    ret, frame = cap.read()
    cv2.setMouseCallback('frame', click_event)
    if len(points)>=6:
        cv2.line(frame,points[-1], points[-2], (255,0,0), 5)
        cv2.line(frame,points[-2], points[-3], (255,0,0), 5)
        cv2.line(frame,points[-3], points[-4], (255,0,0), 5)
        cv2.line(frame,points[-4], points[-5], (255,0,0), 5)
    cv2.imshow('frame', frame)
    print(points)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
