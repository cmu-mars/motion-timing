#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu

def callback(msg):
#       print msg
        rospy.loginfo("%f"%(msg.twist.twist.linear.x))

def sensorListener():
        rospy.init_node('sensorListener', anonymous=True)
        rospy.Subscriber("/odom", Odometry, callback)
        rospy.spin()

if __name__ == '__main__':
        sensorListener()

