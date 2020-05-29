#!/usr/bin/env python

import rospy
from week_2.srv import angvel,angvelRequest,angvelResponse
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def angvel_client(x,pub):
    compute_ang_vel= rospy.ServiceProxy('compute_ang_vel', angvel)
    vel=Twist()
    vel.linear.x=1
    vel.linear.y=0
    vel.linear.z=0
    vel.angular.x=0
    vel.angular.y=0
    vel.angular.z= compute_ang_vel(x)
    pub.publish(vel) 
       
       

if __name__ == "__main__":

    rospy.init_node("angvel_client2", anonymous = False)
    pub=rospy.Publisher('cmd_vel',Twist, queue_size=10)
    rospy.Subscriber('radius',Float64,angvel_client,pub)
    rospy.spin()
