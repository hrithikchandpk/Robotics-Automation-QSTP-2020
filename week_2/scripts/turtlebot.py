#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from week_2.srv import angvel, angvelRequest,angvelResponse
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import math


def angve(a, pub):

    try:
        

        rospy.wait_for_service('compute_ang_vel')
        compute_ang = rospy.ServiceProxy('compute_ang_vel', angvel)
        b=compute_ang(a)
        vel = Twist()
        vel.linear.x = 1.0
        vel.linear.y = 0.0
        vel.linear.z = 0.0
        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = b.angvel1
        pub.publish(vel)
    except rospy.ServiceException, e:

        print 'Service call failed: %s' % e


if __name__ == '__main__':

    rospy.init_node('angvel_client', anonymous=False)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('radius', Float64, angve, pub)
    rospy.spin()

