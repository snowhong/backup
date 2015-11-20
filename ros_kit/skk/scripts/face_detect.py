import roslib
roslib.load_manifest('skk')
import sys
import rospy
import cv2
import time
from std_msgs.msg import Bool
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Face_Service():
	def __init__(self):
		#self.image_topic = rospy.get_param('~image_topic', '/camera/image_raw')

		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback, queue_size = 1)
		#self.face_pub = rospy.Publisher("/faces", Image, self.image_callback, queue_size = 10)

	def image_callback(self, image):
            print "test"
            try:
                cv_image = self.bridge.imgmsg_to_cv2(image, "bgr8")
                print "test"
            except CvBridgeError, e:
                print e
#               detection = self.detect_faces(cv_image, self.cv_window)
#               #if len(detection) > 0:
#               cv2.imshow("FACE", cv_image)
#               cv.waitKey(1)

#	def detect_face(self, image, draw=False):
#		#Parameters
#		_scale_Factor=1.2
#		_min_Neighbour=2
#		_min_Size=(20,20)
#	        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
#		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#		faces=faceCascade.detectMultiScale(
#				gray,
#				_scale_Factor,
#				_min_Neighboru,
#				_min_Size,
#				flags
#				)
#		print "face found".format(len(faces))
#               return faces

if __name__ == '__main__':
	rospy.init_node('face_srv')
	fd = Face_Service()
	rospy.spin()
