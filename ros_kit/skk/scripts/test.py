import roslib
#roslib.load_manifest('facedetector')
import rospy
import sys, select, termios, tty
import time
#import Image
import os
import cv2, cv, numpy
from std_msgs.msg import String
from std_msgs.msg import Bool
import sensor_msgs.msg
from dynamic_reconfigure.server import Server as DynamicReconfigureServer
#from facedetector.msg import Detection
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
class FaceDetect():
    def image_callback():
        return


    def __init__(self):
        print "test"


if __name__ == '__main__':
    rospy.init_node('facedetector')
    fd = FaceDetect()
    rospy.spin()
