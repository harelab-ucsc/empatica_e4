import socket
import time

class E4DataActions(object):
  #Overwrite this class definition to do what you want when the data is received.
  def __init__(self):
    pass
  
  def onAcc3D(self, acc):
    print("Got Acc: " + str(acc))
  
  def onGSR(self, gsr):
    print("Got GSR: " + str(gsr[0]) + ", " + str(gsr[1]))
    
  def onHeartRate(self, heartRate):
    print("Got HeartRate: " + str(heartRate[0]) + ", " + str(heartRate[1]))
    
  def onSkinTemp(self, skinTemp):
    print("Got SkinTemp: " + str(skinTemp[0]) + ", " + str(skinTemp[1]))
# 128.114.204.116 .31
class E4Connect(object):
    def __init__(self, action, svr_addr='192.168.1.100', svr_pt=28000, acc=True, bvp=True, gsr=True, tmp=True):
        
        self.serverAddress = svr_addr
        self.serverPort = svr_pt
        self.bufferSize = 4096

        # SELECT DATA TO STREAM
        self.acc = acc      # 3-axis acceleration
        self.bvp = bvp      # Blood Volume Pulse
        self.gsr = gsr      # Galvanic Skin Response (Electrodermal Activity)
        self.tmp = tmp      # Temperature

        self.action = action 

    def connect(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        print("Connecting to server")
        s.connect((self.serverAddress, self.serverPort))
        print("Connected to server\n")

        print("Devices available:")
        s.send("device_list\r\n".encode())
        response = s.recv(self.bufferSize).decode("utf-8")
        print(response)

        # Auto detect device ID from device list
        try:
            self.deviceID = response.split('|')[1].split()[0]
            self.id_sn_lut()
        except:
            print('CONNECTION ERROR: No available devices')
            exit()

        print("Connecting to device {}".format(self.serial_number))
        s.send(("device_connect " + self.deviceID + "\r\n").encode())
        response = s.recv(self.bufferSize)
        print(response.decode("utf-8"))

        print("Pausing data receiving")
        s.send("pause ON\r\n".encode())
        response = s.recv(self.bufferSize)
        print(response.decode("utf-8"))
        
        time.sleep(1)


    def suscribe_to_data(self):
        if self.acc:
            print("Suscribing to ACC")
            s.send(("device_subscribe " + 'acc' + " ON\r\n").encode())
            response = s.recv(self.bufferSize)
            # print(response.decode("utf-8"))
        if self.bvp:
            print("Suscribing to BVP")
            s.send(("device_subscribe " + 'bvp' + " ON\r\n").encode())
            response = s.recv(self.bufferSize)
            # print(response.decode("utf-8"))
        if self.gsr:
            print("Suscribing to GSR")
            s.send(("device_subscribe " + 'gsr' + " ON\r\n").encode())
            response = s.recv(self.bufferSize)
            # print(response.decode("utf-8"))
        if self.tmp:
            print("Suscribing to Temp")
            s.send(("device_subscribe " + 'tmp' + " ON\r\n").encode())
            response = s.recv(self.bufferSize)
            # print(response.decode("utf-8"))

        print("Resuming data receiving")
        s.send("pause OFF\r\n".encode())
        response = s.recv(self.bufferSize)
        # print(response.decode("utf-8"))

        time.sleep(1)


    def reconnect(self):
        print("Reconnecting...")
        self.connect()
        self.suscribe_to_data()
        self.stream()


    def stream(self):
        print("Streaming...")
        while True:
            try:
                response = s.recv(self.bufferSize).decode("utf-8")    
                if "connection lost to device" in response:
                    print(response.decode("utf-8"))
                    self.reconnect()
                    break
                samples = response.split("\n")
                for i in range(len(samples)-1):

                    if len(samples[i]) > 0 and samples[i][0] == "E" and samples[i][-1] == "\r":
                        try:
                            stream_type = samples[i].split()[0]
                        except Exception as e:
                            print(e)
                            print(samples[i])

                        if stream_type == "E4_Acc":
                            data = [float(samples[i].split()[1].replace(',','.')), int(samples[i].split()[2].replace(',','.')), int(samples[i].split()[3].replace(',','.')), int(samples[i].split()[4].replace(',','.'))]
                            #print(f'acc data:{data}')
                            self.action.onAcc3D(data)
                        if stream_type == "E4_Bvp":
                            time_stamp = float(samples[i].split()[1].replace(',','.'))
                            data = float(samples[i].split()[2].replace(',','.'))
                            bvp = [time_stamp, data]
                            #print(f'bvp data:{data}')
                            self.action.onHeartRate(bvp) 
                        if stream_type == "E4_Gsr":
                            time_stamp = float(samples[i].split()[1].replace(',','.'))
                            data = float(samples[i].split()[2].replace(',','.'))
                            gsr = [time_stamp, data]
                            #print(f'gsr data:{data}')
                            self.action.onGSR(gsr)
                        if stream_type == "E4_Temperature":
                            time_stamp = float(samples[i].split()[1].replace(',','.'))
                            data = float(samples[i].split()[2].replace(',','.'))
                            skinTemp = [time_stamp, data]
                            #print(f'temp data:{data}') 
                            self.action.onSkinTemp(skinTemp)
                        
                #time.sleep(1)
            except socket.timeout:
                print("Socket timeout")
                self.reconnect()
                break

    # This function maps device IDs to serial numbers
    def id_sn_lut(self):
        lut = {'0612C6':'A03D2C','809CFD':'A02F5C','CE44C0':'A0343B','broken':'A024D8'}
        self.serial_number = lut[self.deviceID]


if __name__ == '__main__':
    try:
        actions = E4DataActions()
        e4 = E4Connect(actions)
        e4.connect()
        e4.suscribe_to_data()
        
        e4.stream()
        
    except KeyboardInterrupt:
        print("Disconnecting from device")
        s.send("device_disconnect\r\n".encode())
        s.close()