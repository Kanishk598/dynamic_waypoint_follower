#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import math

rospy.init_node("waypoint")

class follower:
    def __init__(self):
        self.goal = PoseStamped()
        self.goals = []
        self.odom = Odometry()
        self.dist = 0
        self.latch = 0
        self.sub_goal = rospy.Subscriber("/new_goal", PoseStamped, self.callback_goal)
        self.sub_odom = rospy.Subscriber("/odom", Odometry, self.callback_odom)
        self.pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size = 1)
    def callback_goal(self, message):
        self.goal = message
        self.goals.append(self.goal)
    def callback_odom(self, message):
        self.odom = message
        if (len(self.goals) != 0):
            self.dist = math.sqrt((self.goals[0].pose.position.x - self.odom.pose.pose.position.x)**2 + (self.goals[0].pose.position.y - self.odom.pose.pose.position.y)**2)
            if (self.dist > 0.1 and self.latch == 0):
                self.pub_goal.publish(self.goals[0])
                self.latch = 1
            else:
                if self.dist <= 0.5:
                    del(self.goals[0])
                    self.latch = 0

follower = follower()
rospy.spin()
print("\nNode shutdown\n")
