#!/usr/bin/env python
#  -*- coding: utf8 -*-
from math import pi

import rospy
import time
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


def send_zero_position():
    rospy.loginfo("publishing 0 goals for joints")
    msg = JointTrajectoryPoint()
    msg.positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    msg.time_from_start.nsecs = 10000000
    traj_msg = JointTrajectory()
    # make an array with String objects (ros message type)
    traj_msg.joint_names = ['HeadPan', 'HeadTilt', 'LShoulderPitch', 'LShoulderRoll', 'LElbow', 'RShoulderPitch',
                            'RShoulderRoll', 'RElbow', 'LHipYaw', 'LHipRoll', 'LHipPitch', 'LKnee', 'LAnklePitch',
                            'LAnkleRoll', 'RHipYaw', 'RHipRoll', 'RHipPitch', 'RKnee', 'RAnklePitch', 'RAnkleRoll']
    traj_msg.points = []
    traj_msg.points.append(msg)
    traj_msg.header.stamp = rospy.Time.now()

    joint_goal_publisher.publish(traj_msg)


if __name__ == "__main__":
    rospy.init_node('pub_joint_goals_sim')
    joint_goal_publisher = rospy.Publisher('/minibot/controller/command', JointTrajectory,
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
