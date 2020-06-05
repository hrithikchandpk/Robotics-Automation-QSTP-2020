#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math
global count
def excel_time(time):
    return  time.secs 

def publ(pub,r):
    count=0
    t= rospy.get_rostime()
    p=excel_time(t)
    vel=Twist()
    vel.linear.y=0.0
    vel.linear.x=0.20   
    vel.angular.x=0.0
    vel.angular.y=0.0
    print (r,p)
    
    if (p-r)>6.28:
        count=1

    if count==0:
        vel.angular.z=1


    elif count==1:
        vel.angular.z=-1

                  
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
    
    
