import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

# yellow_lower = np.array([22, 93, 0])
# yellow_upper = np.array([45, 255, 255])
sensitivity = 15
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])

prev_y=0
while True:
    ret, frame = cap.read()
    vflip=cv2.flip(frame,1)
    #gray=cv3.cvtColor(vflip, cv3.COLOR_BGR2GRAY)
    hsv= cv2.cvtColor(vflip, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area= cv2.contourArea(c)
        if area > 300:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),10)
            if y < prev_y:
                pyautogui.press('space')
            prev_y=y
    
    cv2.imshow('My Cam', vflip)
    #cv2.imshow('Masked',mask)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()    
cv2.destroyAllWindows()