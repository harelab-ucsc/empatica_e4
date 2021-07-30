#!/usr/bin/env python
#%% Import Dependencies
import struct
import sys
from bluepy.btle import Peripheral,DefaultDelegate
import time
from binascii import unhexlify
import rospy
from std_msgs.msg import Int32
from empatica_e4.msg import SkinTemp #how to import custom msgs
"""Questions:
2. How to import custom messages
3. have ros deal with multiple values from the hex. I, using a for loop but i doubt that is best
4. Likely need things seperated into 2 different files
5. Shouldnt have a global pub variable
6. Organizational structure for adding more notifications? (Make fxs in seperate file and import the module?)
"""
# Delegation is used for NOTIFY instead of READS
class E4Del(DefaultDelegate):
    def __init__(self,params):
        DefaultDelegate.__init__(self)
        self.temperature = 0
      
    #function is called on notification
    def handleNotification(self, cHandle, data):
       hex_handle = format(cHandle,'02X')
       d_hex = data.hex()
       
       #Test of what to do with temperature data
       if (hex_handle == '20'): #and (d_hex[-1] == '0'):
         print("Notification from Handle: 0x" + format(cHandle,'02X') + " Value: "+ (data.hex()))
         self.temperature = self.splitTemp(d_hex)
         #publish
         self.skinTemp(self.temperature)
         

    def splitTemp(self, d_temp):
      temp_unpack = struct.unpack('<hhhhhhhhhh',unhexlify(d_temp))
      return temp_unpack[0:-2]

    def skinTemp(self,temp): #change to onTemp
        rate = rospy.Rate(10) # 10hz
        #rospy.loginfo(hello_str)
        hello_str = "hello world %s" % rospy.get_time()
        for t in temp:
          pub.publish(t)
          rate.sleep()


def notificationSet(peripheral): 
  charHex = ('15','19','1D','21','2E','2A')
  for i, val in enumerate(charHex):
    hexInt = (int(val,16))
    peripheral.writeCharacteristic(hexInt, struct.pack('<bb', 0x01,0x00),withResponse=True)
  
  # General output needs to be fed the current time
  # Turn notifications on by setting bit0 in the CCC more info on:
  # https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorViewer.aspx?u=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml    
  curTime = int(time.time())
  peripheral.writeCharacteristic(0x25, struct.pack('<bl', 0x01, curTime),withResponse=True)
  print('Notifications On')

def main():
  
  if len(sys.argv) != 2:
    print("Fatal, must pass device address:", sys.argv[0], "<device address="">")
    quit()
 
  p = Peripheral(sys.argv[1]) #Connect
  print('Connected')

  p.setDelegate(E4Del(p)) #Set the Delegate to talk to
  print('Delegate Set')
  notificationSet(p) #Turn on Notifications
  time.sleep(3)
  rospy.init_node('talker', anonymous=True)
  global pub 
  pub = rospy.Publisher('SkinTemp', Int32, queue_size=10) #topic name is in quotes


  # Main loop -------- 
  while not rospy.is_shutdown():
      if p.waitForNotifications(1.0):
        continue

      print("Waiting... Waited more than one sec for notification")
      # Perhaps do something else here
      
if __name__ == '__main__':
  main()
# %%
