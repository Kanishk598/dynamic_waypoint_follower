# Dynamic Waypoint Follower

![Video demonstration](https://youtu.be/rmQ4tR-wsTM)

[![Video Demonstration](https://raw.githubusercontent.com/kanishkanarch/dynamic_waypoint_follower/master/Video_demo.png)](https://www.youtube.com/watch?v=rmQ4tR-wsTM)

This package is made to compensate for the following problems in ![Follow Waypoints](http://wiki.ros.org/follow_waypoints) ROS package:

1. Robot has to be told to start moving explicitly, to the given waypoints.
2. When the robot starts moving to the given waypoints, new waypoints can't be added in the list in real-time.

### Usage:

1. Start turtlebot's navigation stack
2. In RVIZ, open the config file mentioned in this repository
3. `rosrun dynamic_waypoint_follower dynamic_follow_waypoint.py`

Enjoy!
