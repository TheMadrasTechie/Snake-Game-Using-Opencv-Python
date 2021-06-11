#Created by Sundar
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import random
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cap = cv2.VideoCapture(0)
vs = cv2.VideoWriter('sundar.avi',fourcc,20.0,(640,480))
greenLower = (50, 100, 100)
greenUpper = (70, 255, 255)
font = cv2.FONT_HERSHEY_SIMPLEX
pts_green = deque(maxlen=10)
o=0
sdd =0
x1 = 0
y1=1
w=[]
def rand_food_points(x,y):
        x=int(random.randint(10,630))
        y=int(random.randint(80,400))
        z=(x,y)
        return z 
def all_food_points():

    for x in range(0, 60):
         z= rand_food_points(0,0)
         w.append(z)
         #print(str(w[x]))
all_food_points()         
 #
z = rand_food_points(x1,y1)
# print("jrhwvbrfgjh"+str(z))
def next_food(q,val):
    w = rand_food_points(x1,y1)
    draw_circle(w,val)
def draw_circle(q,val):
        cv2.circle(frame, (q), 10,(0, 0, 0), 2)
        snake_movement(q,val) 
def snake_movement(food_values,val):
    #print(str(food_values))
    # global sdd
    # ert = int(sdd)+10
    
    mask_green = cv2.inRange(hsv, greenLower, greenUpper)
    mask_green = cv2.erode(mask_green, None, iterations=2)
    mask_green = cv2.dilate(mask_green, None, iterations=2)
    cnts_green = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts_green = cnts_green[0]# if imutils.is_cv2() else cnts_green[1]
    center = None
    if(not(cnts_green is None)):

     if len(cnts_green) > 0:
        c = max(cnts_green, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255,255), 2)
            cv2.circle(frame, center, 10, (0, 0,255), -1)
    pts_green.appendleft(center)
    for i in range(1, len(pts_green)):
        if(not(pts_green[i] is None)):
            
            #print(str(pts_green[i][0]))
            if(((food_values[0]-10)<pts_green[i][0]<(food_values[0]+10))and((food_values[1]-10)<pts_green[i][1]<(food_values[1]+10))):
               #print(str(pts_green[i][0]))
               #print("comedy")
               global sdd
               
               sdd = sdd+1

               #next_food(w,sdd)               
        if pts_green[i - 1] is None or pts_green[i] is None:
            continue
        thickness = int(np.sqrt(64 / float(i + 1)) * 5) 
        cv2.line(frame, pts_green[i - 1], pts_green[i], (0, 0,255), 20)


a=time.time()
while True:
    frame = cap.read()
    frame = frame[1]    
    
    
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    #print(str(w[sdd]))
    x1=x1+1
    #print(str(sdd))
    draw_circle(w[sdd],sdd)
    dd = cv2.flip(frame, 1)
    #print(time.time())
    cv2.putText(dd, str(sdd), (20, 20), font, 0.8, (255, 255,255), 2, cv2.LINE_AA)
    cv2.putText(dd, "Time:"+str(int(time.time()-a)), (220, 20),  font, 0.8, (255, 255,255), 2, cv2.LINE_AA)
    vs.write(dd)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
#time.sleep(5.0)
    #print(str(time.time()-a)) 
    if((time.time()-a)>28):
        cv2.putText(dd, str(sdd), (200, 400), font, 10, (255, 255,255), 10, cv2.LINE_AA)
        if((time.time()-a)>30):
           print("\n\n\n\n\n\n"+str(sdd))
           time.sleep(2.0)
           break      
    cv2.imshow("Snake", dd)       
vs.release()
cv2.destroyAllWindows()