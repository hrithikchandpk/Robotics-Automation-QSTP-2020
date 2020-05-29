#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math
global count
def excel_time(time):
    return  time.secs / (24.0*60.0*60.0)

def publ(pub,r):
    
    t= rospy.get_rostime()
    p=excel_time(t)
    vel=Twist()
    
    vel.linear.z=0
    vel.angular.x=0
    vel.angular.y=0
    vel.angular.z=-1
    if p-r<7:
        count=0

    if p-r %6.28==0.0 and count==0:
        count=1
    elif p-r %6.28==0.0 and count==1:
        count=0    
    if  count==0:
        vel.linear.x=1*math.cos(p-r)
        vel.linear.y=1*math.sin(p-r)
        vel.angular.z=1
    elif count==1:
        vel.linear.x=1*math.cos(p-r)
        vel.linear.y=1*math.sin(r-p)
        
    pub.publish(vel) 
       
       

if __name__ == "__main__":

    rospy.init_node("angvel_client2", anonymous = False)
    pub=rospy.Publisher('cmd_vel',Twist, queue_size=10)
    intime= t= rospy.get_rostime()
    r=excel_time(intime)#gives initial time
  
    rate = rospy.Rate(15)
    while not rospy.is_shutdown(): 
        publ(pub,r)
        rate.sleep()  
    
