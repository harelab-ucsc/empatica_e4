#!/usr/bin/env python
#%% Import Dependencies
import struct
import sys
from bluepy.btle import Peripheral,DefaultDelegate
import time
from binascii import unhexlify
#import rospy
#from std_msgs.msg import Int32
#from empatica_e4.msg import SkinTemp #how to import custom msgs
"""Questions:
3. have ros deal with multiple values from the hex. I, using a for loop but i doubt that is best
4. Likely need things seperated into 2 different files
5. Shouldnt have a global pub variable
6. Organizational structure for adding more notifications? (Make fxs in seperate file and import the module?)
"""
class E4Connect(object):
  def __init__(self, addr, action):
    self.e4 = Peripheral(addr)
    self.action = action
    print('Connected')
    self.e4.setDelegate(E4Del(self.e4,self.action)) #Set the Delegate to talk to
    print('Delegate Set')
  #connect peripheral function (in init?)
  # set delegate function
  def notificationSet(self,peripheral): 
    charHex = ('15','19','1D','21','2E','2A')
    for i, val in enumerate(charHex):
      hexInt = (int(val,16))
      peripheral.writeCharacteristic(hexInt, struct.pack('<bb', 0x01,0x00),withResponse=True)

    # General output needs to be fed the current time
    # Turn notifications on by setting bit0 in the CCC more info on:
    # https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorViewer.aspx?u=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml    
    curTime = int(time.time())
    peripheral.writeCharacteristic(0x25, struct.pack('<bl', 0x01, curTime),withResponse=True)
    time.sleep(3) #delay gives time for data to start streaming once notifications are turned on
    print('Notifications On')
  
class E4DataActions(object):
  #Rewrite over this in a class instance to do what you want when the data is received.
  def __init__(self):
    pass
  
  def onSkinTemp(self, SkinTemp):
    print("Got SkinTemp:" + str(SkinTemp))

class E4DataStreams(object):
  SkinTemp = 0x14
  def __init__(self, cHandle, data, action):
    
    self.cHandle = cHandle
    self.data = data
    self.action = action
    self.readData(self.cHandle,self.data,self.action)
    
  def readData(self,cHandle, data, actions):
    #somekind of data check then move on to parseNotification
    self.parseNotification(cHandle, data, actions)
    
  @classmethod
  def parseNotification(cls, cHandle, data, actions):
    if cHandle == E4DataStreams.SkinTemp:
      cls.parseSkinTemp(data,actions)
    else:
      print('Unknown sensor type')
    
  @classmethod
  def parseSkinTemp(cls, data, actions):
    temp_unpack = struct.unpack('<hhhhhhhhhh',unhexlify(data.hex()))
    temp_data = temp_unpack[0:-2]
    actions.onSkinTemp(temp_data)
    
class E4Del(DefaultDelegate):
    def __init__(self,parent,action):
        DefaultDelegate.__init__(parent)
        self.action = action
      
    #function is called on notification
    def handleNotification(self, cHandle, data):
      streams = E4DataStreams(cHandle, data, self.action)

def main():
  
  if len(sys.argv) != 2:
    print("Fatal, must pass device address:", sys.argv[0], "<device address="">")
    quit()
  actions = E4DataActions()
  conn = E4Connect(sys.argv[1], actions) #connect device

  conn.notificationSet(conn.e4) #Turn on Notifications

  while True:
    
      if conn.e4.waitForNotifications(1.0):
        continue

      print("Waiting... Waited more than one sec for notification")
      
if __name__ == '__main__':
  main()