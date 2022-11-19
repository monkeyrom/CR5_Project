import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
pic = cv2.imread("/home/rai/catkin_ws/src/CR5_Project/src/image/Robot.jpg")
face_cascade = cv2.CascadeClassifier("/home/rai/catkin_ws/src/CR5_Project/opencv/data/haarcascades/haarcascade_frontalface_default.xml")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y)
        cv2.putText(frame,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.imshow("Output",frame)

def colorfilter(img):
    lower = numpy.array([20,40,40])
    upper = numpy.array([124,255,333])

    mask = cv2.inRange(img,lower,upper)

    cv2.imshow("ColorFliter",mask)

def face_detect(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    scaleFactor = 1.1
    minNeighbor = 3
    face_detect = face_cascade.detectMultiScale(gray_img)
    for (x,y,w,h) in face_detect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
    
    cv2.imshow("Detect",img)

while(True):
    check , frame = cap.read()
    #frame = cv2.resize(frame,(640,480))
    #cv2.imshow("Output",frame)
    #cv2.setMouseCallback("Output",clickPosition)
    #colorfilter(frame)
    face_detect(frame)

    # ใช้ matplotlib โชว์ 
    #pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    #plt.imshow(pic)
    #plt.show()

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()