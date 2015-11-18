import cv2
import rospy
import roslib
import time
from std_msgs.msg import Bool
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class Face_Service():
	def __init__(self):
		#self.image_topic = rospy.get_param('~image_topic', '/camera/image_raw')

		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback, queue_size = 1)
		self.face_pub = rospy.Publisher("/faces", Image, self.image_callback, queue_size = 10)
		self.enabled = True #rospy.get_param('~enabled', True)
                self.cv_window = True #rospy.get_param('~show_cv_window', True)

	def image_callback(self, image):
		if not self.enabled:
			return
		try:
                    cv_image = self.bridge.imgmsg_to_cv2(image, "bgr8")
                    detection = self.detect_faces(cv_image, self.cv_window)
                    #if len(detection) > 0:
                    if self.cv_window:
                        cv2.imshow(CV_WINDOW_TITLE, cv_image)
                        cv.waitKey(1)
                except CvBridgeError, e:
                    print e

	def status_callback(self, status):
                if self.enabled:
                    rospy.loginfo("Face detection enabled")
                else:
                    rospy.loginfo("Face detection disabled")

	def detect_face(self, image, draw=False):
		#Parameters
		_scale_Factor=1.2
		_min_Neighbour=2
		_min_Size=(20,20)
	        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faces=faceCascade.detectMultiScale(
				gray,
				_scale_Factor,
				_min_Neighboru,
				_min_Size,
				flags
				)
		print "face found".format(len(faces))
                return 

if __name__ == '__main__':
	rospy.init_node('face_srv')
	fd = Face_Service
	rospy.spin()
