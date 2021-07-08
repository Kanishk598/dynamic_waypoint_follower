#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

rospy.init_node("waypoint")

class follower:
    def __init__(self):
        self.goal = PoseStamped()
        self.goals = []
        self.odom = Odometry()
        self.sub_goal = rospy.Subscriber("/new_goal", PoseStamped, self.callback_goal)
        self.pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size = 1)
    def callback_goal(self, message):
        self.goal = message
        self.goals.append(self.goal)
    def callback_odom(self, message):
        self.odom = message

follower = follower()
rospy.spin()
print("\nNode shutdown\n")
