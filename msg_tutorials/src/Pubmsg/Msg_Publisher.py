#!/usr/bin/env python
import rospy
from msg_tutorials.msg import MsgTutorial
 
def talker():
    pub = rospy.Publisher('custom_msg', MsgTutorial)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = MsgTutorial()
    msg.name = "roboya"
    msg.data = 4
  
    while not rospy.is_shutdown():
      rospy.loginfo(msg)
      pub.publish(msg)
      r.sleep()