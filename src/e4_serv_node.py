#!/usr/bin/env python3

import rospy
import std_msgs.msg
from core_e.e4_server_dev import *
from empatica_e4.msg import *

class ROSActions(E4DataActions):
    def __init__(self):
        super(ROSActions, self).__init__()
        #'topic name', msg type, queue_size = 10 <-standard queue size
        self.acc_pub = rospy.Publisher('acc', Acc3D, queue_size=10)
        self.gsr_pub = rospy.Publisher('gsr', GSR, queue_size=10)
        self.hr_pub = rospy.Publisher('hr_e4', Heartrate, queue_size=10)
        self.st_pub = rospy.Publisher('st', SkinTemp, queue_size=10)
        
    def onGSR(self, gsr):
        rate = rospy.Rate(10)
        msg = GSR()
        msg.header = std_msgs.msg.Header()
        msg.header.stamp = rospy.Time.now()
        msg.gsr = gsr
        self.gsr_pub.publish(msg)
        rate.sleep()
        
    def onHeartRate(self, hr):
        rate = rospy.Rate(10)
        msg = Heartrate()
        msg.header = std_msgs.msg.Header()
        msg.header.stamp = rospy.Time.now()
        msg.hr = hr
        self.hr_pub.publish(msg)
        rate.sleep()    
        
    def onSkinTemp(self, st):
        rate = rospy.Rate(10)
        msg = SkinTemp()
        msg.header = std_msgs.msg.Header()
        msg.header.stamp = rospy.Time.now()
        msg.st = st
        self.st_pub.publish(msg)
        rate.sleep()

    def onAcc3D(self, acc):
        rate = rospy.Rate(10)
        msg = Acc3D()
        msg.header = std_msgs.msg.Header()
        msg.header.stamp = rospy.Time.now()
        msg.acc_x = acc[0]
        msg.acc_y = acc[1]
        msg.acc_z = acc[2]
        self.acc_pub.publish(msg)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        rospy.init_node('e4_node', anonymous=True)
        
        actions = ROSActions()
        e4 = E4Connect(actions)
        e4.connect()
        e4.suscribe_to_data()
        e4.stream()

    except rospy.ROSInterruptException:
        pass
    
    # rospy.init_node('e4_node', anonymous=True)
    # rosargs = rospy.myargv(argv=sys.argv)
    # myargs = getArgs(rosargs)  
    # if len(sys.argv) > 1:
    #     myargs.address = str(sys.argv[2])
    # else:
    #     myargs.address = 'A4:34:F1:F1:67:8F'
        
    # actions = ROSActions()
    
    # asyncio.ensure_future(init(actions,myargs))
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_forever()
    # except KeyboardInterrupt:
    #     logger.info("Ctrl-C pressed.")
        