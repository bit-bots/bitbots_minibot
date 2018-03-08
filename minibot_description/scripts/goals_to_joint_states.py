#!/usr/bin/env python
#  -*- coding: utf8 -*-
from math import pi

import rospy
import time
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import JointState

ns = rospy.get_param("ns", "/minibot")
joint_state_pub = rospy.Publisher("/joint_states", JointState, queue_size=10)

def cb(msg):
    state_msg = JointState()
    state_msg.name = msg.joint_names
    state_msg.position = msg.points[0].positions
    state_msg.header = msg.header
    joint_state_pub.publish(state_msg)

if __name__ == "__main__":
    rospy.init_node('goals_to_joint_states')
    # get namespace
    joint_goal_subscriber = rospy.Subscriber(ns + '/controller/command', JointTrajectory, cb,
                                           queue_size=10)
    while not rospy.is_shutdown():
        try:
            # catch exeption of moving backwarts in time, when restarting simulator
            rospy.sleep(10000000000000000)
        except rospy.exceptions.ROSTimeMovedBackwardsException:
            rospy.logwarn(
                "Simulator reset ignored.")
        except rospy.exceptions.ROSInterruptException:
            exit()
