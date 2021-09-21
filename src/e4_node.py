#!/usr/bin/env python3

import sys
import rospy
import std_msgs.msg
from core_e.e4_dev import *
#from empatica_e4.src.e4_dev import *
from empatica_e4.msg import *

class ROSActions(E4DataActions):
    def __init__(self):
        super(ROSActions, self).__init__()
        #'topic name', msg type, queue_size = 10 <-standard queue size
        self.acc_pub = rospy.Publisher('acc', Acc3D, queue_size=10)
        self.gsr_pub = rospy.Publisher('gsr', GSR, queue_size=10)
        self.hr_pub = rospy.Publisher('heartrate', Heartrate, queue_size=10)
        self.skinTemp_pub = rospy.Publisher('skintemp', SkinTemp, queue_size=10)
        
        self.acc_time = rospy.Time.now()
        self.gsr_time = rospy.Time.now() 
        self.hr_time = rospy.Time.now() 
        self.skinTemp_time = rospy.Time.now() 
        
                
    def onAcc3D(self, acc):
        self.rate = rospy.Rate(10)
        for i in range(0,len(acc),3):
            msg = Acc3D()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = rospy.Time.now()
            msg.acc_x = acc[i]
            msg.acc_y = acc[i+1]
            msg.acc_z = acc[i+2]
            self.acc_pub.publish(msg)
            self.rate.sleep()
        
    def onGSR(self, gsr):
        self.rate = rospy.Rate(10)
        for i in range(0,len(gsr),2):
            msg = GSR()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = rospy.Time.now()
            msg.status = gsr[i]
            msg.resistance = gsr[i+1]
            self.gsr_pub.publish(msg)
            self.rate.sleep()
            
    def onHeartRate(self,heartRate):
        self.rate = rospy.Rate(10)
        
    def onSkinTemp(self, skinTemp):
        #8 msgs per bluetooth payload
        self.rate = rospy.Rate(10)
        
        tm_pts, self.skinTemp_time = self.timeParse(previous_time=self.skinTemp_time,msg_split=8)
        
        for i in range(0,len(skinTemp)):
            msg = SkinTemp()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = tm_pts[i]
            #msg.header.stamp = rospy.Time.now()
            msg.temp = skinTemp[i]
            self.skinTemp_pub.publish(msg)
            self.rate.sleep()

    @classmethod
    def timeParse(cls, previous_time, msg_split):        
        incoming_time = rospy.Time.now()
        time_step = (incoming_time-previous_time)/(msg_split-1)
        t_dur = int(time_step.nsecs)
        
        t_offset = [rospy.Duration(0,t_dur*i) for i in range(msg_split)]
        t_offset.reverse()
        t_base = [incoming_time for i in range(msg_split)]
        
        return list(map(lambda x,y: x-y, t_base,t_offset)), incoming_time
        
if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        addr = '88:6B:0F:C0:44:CE'
        #print("Fatal, must pass device address:", sys.argv[0], "<device address="">")
        #quit()
    else:
        addr = sys.argv[1]
    
    try:
        rospy.init_node('e4_node', anonymous=True)
        
        actions = ROSActions()
        
        conn = E4Connect(addr,actions)
        conn.notificationSet(conn.e4)
        
        
        #notifications = E4Notifications()
        
        while not rospy.is_shutdown():
            if conn.e4.waitForNotifications(1.0):
                continue
    
        conn.e4.disconnect()

    except rospy.ROSInterruptException:
        pass