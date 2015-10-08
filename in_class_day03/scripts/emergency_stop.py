#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from neato_node.msg import Bump
from geometry_msgs.msg import Twist


def bumpcallback(msg):
    print msg
    global twist
    print twist
    
    if msg.leftFront==1 or msg.rightFront ==1:
        stop = True
    else:
        stop = False

    if stop:
        twist.linear.x = 0
        twist.linear.x = -.1
        twist.angular.x = .1
    else:
        twist.linear.x = 0.1

def main():
    global twist
    rospy.init_node('emergency_stop')
    pub = rospy.Publisher('velocity', Twist, queue_size=10) 
    sub = rospy.Subscriber('bump', Bump, bumpcallback)
    
    twist = Twist()
    twist.linear.x = .1
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass