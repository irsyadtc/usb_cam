#!/usr/bin/env python3
#######################################################################
#
# Software License Agreement (BSD License)
#
#  Copyright (c) 2023, Irsyad Sahalan.
#  All rights reserved.
#
#######################################################################

import rospy
import requests
import cv2
import numpy as np
import imutils
import sys

from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image


def ipcam(url_, screen_):

	if (url_):
		url = url_
	else:	
		url = "http://192.168.0.174:8080/shot.jpg"
		
	image_pub = rospy.Publisher("/usb_cam/image_raw", Image, queue_size=5)
	
	bridge = CvBridge()
	
	rospy.init_node('ipcam', anonymous=True)
	rate = rospy.Rate(30) # 30hz
        
	while not rospy.is_shutdown():
		img_resp = requests.get(url)
		img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
		img = cv2.imdecode(img_arr, -1)
		#img = imutils.resize(img, width=1000, height=1800)
		grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		if (screen_ == "open"):		#display screen
			grayscale_rescale = imutils.resize(grayscale, width=1000, height=1800)
			cv2.imshow("Android_cam", grayscale_rescale)
		
		image_message = bridge.cv2_to_imgmsg(grayscale, encoding="mono8")	#convert OpenCV Matrix to ros image
		image_pub.publish(image_message)
		  
		# Press Esc key to exit
		if cv2.waitKey(1) == 27:
			break

		rate.sleep()

    
if __name__ == '__main__':
	try:
		if len(sys.argv) == 3:
			print("ip camera starts. Display open")
			ipcam(sys.argv[1], sys.argv[2])
		elif len(sys.argv) == 2:
			print("ip camera starts. Display close")
			ipcam(sys.argv[1], "null")
		else:
			print("ip camera starts. Default setting")
			ipcam("http://192.168.0.174:8080/shot.jpg", "open")
			
	except rospy.ROSInterruptException:
		pass
