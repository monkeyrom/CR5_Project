import rospy
import sys
import cv2
import numpy

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

face_cascade = cv2.CascadeClassifier("/home/rai/catkin_ws/src/CR5_Project/opencv/data/haarcascades/haarcascade_frontalface_default.xml")

def process_image(msg):
    bridge = CvBridge()

    img = bridge.imgmsg_to_cv2(msg, "bgr8")
    frame = cv2.resize(img,(640,360))
    #cv2.imshow("image",img)
    colorfilter(frame)
    face_detect(frame)
    # Node rate in millisec
    cv2.waitKey(10)

def colorfilter(img):
    lower = numpy.array([20,40,40])
    upper = numpy.array([124,255,333])

    mask = cv2.inRange(img,lower,upper)

    cv2.imshow("ColorFliter",mask)

def face_detect(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    scaleFactor = 1.1
    minNeighbor = 5
    face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbor)
    for (x,y,w,h) in face_detect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
    cv2.imshow("Detect",img)

if __name__ == '__main__':

    while not rospy.is_shutdown():
        rospy.init_node('image_sub')

        rospy.loginfo('Image_sub node started')

        # Subscribers
        rospy.Subscriber("/camera/color/image_raw", Image, process_image)
        rospy.loginfo("Subscribed to /camera/color/image_raw")
        
        rospy.spin()