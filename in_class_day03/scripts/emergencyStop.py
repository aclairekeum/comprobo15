#!usr/bin/env python

import rospy
from neato_node.msg import Bump
from geometry_msgs.msg import Twist

class emergencyStop:

	def bumpcallback(self, msg):
		if msg.Front
		
	def run(self):
		pub = rospy.Publisher('motor', Twist, queue_size=10)
		sub = rospy.Subscriber('bump', Bump, bumpcallback)

	def __init__():
		


if __name__ == '__main__':
    try:
    	node = emergencyStop()
    	node.run()
    except rospy.ROSInterruptException:
        pass
