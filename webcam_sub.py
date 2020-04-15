#!/usr/bin/env python
import time
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
#TODO: import proper ROS message libraries

def callback(data):

    bridge=CvBridge()
    #convert images to opencv image
    try:
        cv_image=bridge.imgmsg_to_cv2(data, "8UC3")
    except CvBridgeError as e:
        print(e)
    #display the image
    if (not cv_image is None):
        cv2.imshow("Image",cv_image)
    if cv2.waitKey(50)==-1:
        cv2.destroyAllWindows()
    #TODO:
    # 3 desired colors (rbg values for each color)
    # filter the image with those colors (cv2.inRange(image, lowerb, upperb))
    # result in 3 filtered image
    # use Opencv connected component function to decide which color dominates (cv2.connectedComponentsWithStats())
    # Initialize ROS publisher
    # publish /turtle1/cmd_vel --> geometry_msgs/Twist.msg --> Vector3  linear; Vector3  angular

if __name__ == '__main__': 
    rospy.init_node('stream_node', anonymous=True)
    sub = rospy.Subscriber("/image_raw",Image,callback)
    rospy.spin()                                    #ctrl+c to terminate this script
