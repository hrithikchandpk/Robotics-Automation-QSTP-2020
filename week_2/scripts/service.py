#!/usr/bin/python
# -*- coding: utf-8 -*-

from week_2.srv import angvel, angvelRequest, angvelResponse
import rospy


def process_service_request(req):
    resp = angvelResponse()
    resp.angvel = 1 / req.radius
    return resp


def av_server():
    rospy.init_node('angvel_server', anonymous=False)
    service = rospy.Service('compute_ang_vel', angvel,
                            process_service_request)
    rospy.loginfo('server available.')
    rospy.spin()


if __name__ == '__main__':
    av_server()
