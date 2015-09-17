#!/usr/bin/env python

""" This ROS node uses proportional control to guide a robot to a specified
    distance from the obstacle immediately in front of it """

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class WallApproach(object):
    """ A ROS node that implements a proportional controller to approach an obstacle
        immediately in front of the robot """
    def __init__(self):
        """ Initialize a node with the specified target distance
            from the forward obstacle """
        rospy.init_node('wall_approach')
        init_speed = 0
        
        self.twist = Twist()
        self.twist.linear.x = init_speed
        self.target_distance = rospy.get_param('~target_distance')
        self.actual_distance = 0
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) 
        rospy.Subscriber('/scan', LaserScan, self.callbackScan)
        
    def callbackScan(self, data):
        if not data.ranges[0]==0:
            self.actual_distance = data.ranges[0]
        

    def run(self):
        """ Our main 5Hz run loop """

        r = rospy.Rate(5)
        while not rospy.is_shutdown():
            self.twist.linear.x = (self.actual_distance-self.target_distance)
            print (self.actual_distance)
            self.pub.publish(self.twist)
            r.sleep()

if __name__ == '__main__':
    node = WallApproach()

    node.run()