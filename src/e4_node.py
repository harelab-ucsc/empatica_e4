#!/usr/bin/env python

import sys
import rospy
import std_msgs.msg
from e4_dev import *
from empatica_e4.msg import *


class ROSActions(E4DataActions):
    def __init__(self):
        super(ROSActions, self).__init__()
        #self.acc_pub = rospy.Publisher('acc', Acc3D, queue_size=10)
        #self.gsr_pub = rospy.Publisher('gsr', GSR, queue_size=10)
        #self.hr_pub = rospy.Publisher('heartrate', Heartrate, queue_size=10)
        self.skinTemp_pub = rospy.Publisher('skintemp', SkinTemp, queue_size=10) #topic name is in quotes
        
                
    def onSkinTemp(self, skinTemp):
        self.rate = rospy.Rate(10)
        for temp in skinTemp:
            msg = SkinTemp()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = rospy.Time.now()
            msg.temp = temp
            self.skinTemp_pub.publish(msg)
            self.rate.sleep()
            
# def skinTemp(temp):
#     pub = rospy.Publisher('SkinTemp', SkinTemp, queue_size=10) #topic name is in quotes
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         #rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         rate.sleep()

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Fatal, must pass device address:", sys.argv[0], "<device address="">")
        quit()
    
    addr = sys.argv[1]
    
    try:
        actions = ROSActions()
        
        conn = E4Connect(addr,actions)
        conn.notificationSet(conn.e4)
        
        rospy.init_node('e4_node', anonymous=True)
        
        #notifications = E4Notifications()
        
        while not rospy.is_shutdown():
            if conn.e4.waitForNotifications(1.0):
                continue
    
        conn.e4.disconnect()

    except rospy.ROSInterruptException:
        pass