#!/usr/bin/env python3
#%% Import Dependencies
import struct
import sys
from bluepy.btle import Peripheral,DefaultDelegate
import time
from binascii import unhexlify

"""Questions:
3. have ros deal with multiple values from the hex. I, using a for loop but i doubt that is best
-backlogging time from the most recent call
1. check sum for acc3d data - wait
2. aux msg from gsr - wait
4. heartrate?
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
  #Overwrite this class definition to do what you want when the data is received.
  def __init__(self):
    pass
  
  def onAcc3D(self, acc3D):
    print("Got Acc:" + str(acc3D))
  
  def onGSR(self, gsr):
    print("Got GSR:" + str(gsr))
    
  def onHeartRate(self, heartRate):
    print("Got Acc:" + str(heartRate))
    
  def onSkinTemp(self, SkinTemp):
    print("Got SkinTemp:" + str(SkinTemp))

class E4DataStreams(object):
  Acc3D = 0x1c
  GSR = 0x18
  HR = 0x14
  SkinTemp = 0x20
  
  def __init__(self, cHandle, data, action):
    
    self.cHandle = cHandle
    self.data = data
    self.action = action
    self.readData(self.cHandle,self.data,self.action)
    
  def readData(self,cHandle, data, action):
    #insert somekind of data check then move on to parseNotification
    self.parseNotification(cHandle, data, action)
    
  @classmethod
  def parseNotification(cls, cHandle, data, action):
    if cHandle == E4DataStreams.Acc3D:
      cls.parseAcc3D(data,action)
    elif cHandle == E4DataStreams.GSR:
      cls.parseGSR(data,action)
    elif cHandle == E4DataStreams.HR:
      cls.parseHeartRate(data,action)
    elif cHandle == E4DataStreams.SkinTemp:
      cls.parseSkinTemp(data,action)
    else:
      print('Unknown sensor type')
  
  @classmethod
  def parseAcc3D(cls, data, action):
    acc3D_unpack = struct.unpack('<hhhhhhhhhh',unhexlify(data.hex()))
    acc3d_data = acc3D_unpack[0:-1]
    action.onAcc3D(acc3d_data)
    #add check sum verification check?
    pass
  
  @classmethod
  def parseGSR(cls, data, action):
    gsr_unpack = struct.unpack('<hhhhhhhhhh',unhexlify(data.hex()))
    if gsr_unpack[-2] == 256:
      #print('Base Message')
      action.onGSR(gsr_unpack[0:-2])
    else:
      print('Aux Message')
    #check to see which notification we are given via unhex maybe publish a gsr and gsr aux on the ROS side
    #that would allow us to see them both and play with the outputs. 
    pass
  
  @classmethod
  def parseHeartRate(cls, data, action):
    pass

  @classmethod
  def parseSkinTemp(cls, data, action):
    temp_unpack = struct.unpack('<hhhhhhhhhh',unhexlify(data.hex()))
    temp_data = temp_unpack[0:-2]
    action.onSkinTemp(temp_data)
    
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