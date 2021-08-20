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
        self.latch = 0
        self.sub_goal = rospy.Subscriber("/new_goal", PoseStamped, self.callback_goal)
        self.sub_odom = rospy.Subscriber("/odom", Odometry, self.callback_odom)
        self.pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size = 1)
    def callback_goal(self, message):
        self.goal = message
        self.goals.append(self.goal)
    def callback_odom(self, message):
        self.odom = message
        print("Number of goals in the list: " + str(len(self.goals)))
        if (len(self.goals) != 0):
            dist = ((self.goals[0].pose.position.x - self.odom.pose.pose.position.x)**2 + (self.goals[0].pose.position.y - self.odom.pose.pose.position.y)**2)**(1/2)
            if (dist > 0.5 and self.latch == 0):
                self.pub_goal.publish(self.goals[0])
                self.latch = 1
                print("Published a goal")
            elif (self.latch==1):
                if(dist <=0.5):
                    del(self.goals[0])
                    self.latch = 0
                    print("Deleted a goal")

follower = follower()
rospy.spin()
print("\nNode shutdown\n")
