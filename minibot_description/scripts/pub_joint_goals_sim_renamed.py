#!/usr/bin/env python
#  -*- coding: utf8 -*-
from math import pi

import rospy
import time
from std_msgs.msg import Float64MultiArray


def send_zero_position():
    rospy.loginfo("publishing 0 goals for joints")
    msg = Float64MultiArray()
    msg.data = [0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    joint_goal_publisher.publish(msg)


if __name__ == "__main__":
    rospy.init_node('pub_joint_goals_sim')
    # get namespace
    ns = rospy.get_param("ns", "/minibot")
    joint_goal_publisher = rospy.Publisher(ns + '/controller/command', Float64MultiArray,
                                           queue_size=10)
    rospy.sleep(1)
    send_zero_position()
    while not rospy.is_shutdown():
        try:
            # catch exeption of moving backwarts in time, when restarting simulator
            rospy.sleep(10000000000000000)
        except rospy.exceptions.ROSTimeMovedBackwardsException:
            rospy.logwarn(
                "Simulator reset. I will do position reset to zero")
            send_zero_position()
        except rospy.exceptions.ROSInterruptException:
            exit()
