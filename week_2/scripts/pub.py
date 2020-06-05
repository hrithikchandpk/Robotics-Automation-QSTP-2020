#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


if __name__ == "__main__":

    rospy.init_node("rad", anonymous = False)
    pub=rospy.Publisher('radius',Float64, queue_size=10)
    rate = rospy.Rate(15)
    rad=1.0
    while not rospy.is_shutdown(): 
        pub.publish(rad)
        rate.sleep()  
  
  
