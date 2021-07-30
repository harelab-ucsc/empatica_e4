#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from e4.msg import SkinTemp

def skinTemp(temp):
    pub = rospy.Publisher('SkinTemp', SkinTemp, queue_size=10) #topic name is in quotes
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        skinTemp(temperature)
    except rospy.ROSInterruptException:
        pass