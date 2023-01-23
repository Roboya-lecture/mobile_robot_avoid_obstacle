#!/usr/bin/env python
import rospy
from msg_tutorials.msg import MsgTutorial


def callback(data):
  rospy.loginfo("Company : %s, Data : %d" % (data.name, data.data))

def listener():
  rospy.init_node('custom_listener', anonymous=True)
  rospy.Subscriber("custom_msg", MsgTutorial, callback)
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()