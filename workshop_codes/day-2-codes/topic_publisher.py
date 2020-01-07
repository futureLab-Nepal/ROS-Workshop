#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
rate = rospy.Rate(2)

cmd_vel = Twist()
cmd_vel.linear.x=0.2
cmd_vel.angular.z = 1.0
count = 0

while not rospy.is_shutdown():
    pub.publish(cmd_vel)
    rate.sleep()

    
