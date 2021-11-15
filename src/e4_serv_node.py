#!/usr/bin/env python3

import rospy
import std_msgs.msg
from core_e.e4_server_dev import *
from empatica_e4.msg import *
import numpy as np

import pyphysio.indicators.TimeDomain as td_ind
import pyphysio.indicators.FrequencyDomain as fd_ind
import pyphysio.indicators.NonLinearDomain as nl_ind
import pyphysio.indicators.PeaksDescription as pd_ind
import pyphysio.estimators.Estimators as ph_est
from pyphysio import EvenlySignal
import pyphysio as ph

class ROSActions(E4DataActions):
    def __init__(self):
        super(ROSActions, self).__init__()
        #'topic name', msg type, queue_size = 10 <-standard queue size
        self.acc_pub = rospy.Publisher('acc', Acc3D, queue_size=10)
        # self.gsr_pub = rospy.Publisher('gsr', GSR, queue_size=10)
        self.hr_pub = rospy.Publisher('hr_e4', Heartrate, queue_size=10)
        self.st_pub = rospy.Publisher('st', SkinTemp, queue_size=10)
        self.eda_pub = rospy.Publisher('eda', EDA, queue_size=10)

        self.eda_wv = []
        self.hr = []
        self.st = []
        
        # Preserving Old function for reference
    # def onGSR(self, gsr):
    #     msg = GSR()
    #     msg.header = std_msgs.msg.Header()
    #     msg.header.stamp = rospy.Time.now()
    #     msg.gsr = gsr
    #     self.gsr_pub.publish(msg)

    def onGSR(self, gsr):
        time_stamp = gsr[0]
        data = gsr[1]
        self.eda_wv.append(data)

        # print('gsr', gsr)
        # print('length', len(self.eda_wv))

        if len(self.eda_wv) >= 120: # 120 waveforms needed for 30s of data (4Hz)

            flat_eda = self.eda_wv
            eda = EvenlySignal(values=flat_eda, sampling_freq=4, signal_type='eda')
            driver = ph.DriverEstim()(eda)
            phasic, tonic, driver_no_peak = ph.PhasicEstim(delta=0.1)(driver)

            wvf_array = std_msgs.msg.Float32MultiArray()
            wvf_array.layout.data_offset = 0 
            wvf_array.layout.dim = [std_msgs.msg.MultiArrayDimension()]
            wvf_array.layout.dim[0].label = "eda_waveform"
            wvf_array.layout.dim[0].size = len(flat_eda)
            wvf_array.layout.dim[0].stride = 1

            wvf_array.data = flat_eda

            p_wvf_array = std_msgs.msg.Float32MultiArray()
            p_wvf_array.layout.data_offset = 0 
            p_wvf_array.layout.dim = [std_msgs.msg.MultiArrayDimension()]
            p_wvf_array.layout.dim[0].label = "phaisc_waveform"
            p_wvf_array.layout.dim[0].size = len(phasic)
            p_wvf_array.layout.dim[0].stride = 1

            p_wvf_array.data = phasic

            t_wvf_array = std_msgs.msg.Float32MultiArray()
            t_wvf_array.layout.data_offset = 0 
            t_wvf_array.layout.dim = [std_msgs.msg.MultiArrayDimension()]
            t_wvf_array.layout.dim[0].label = "tonic_waveform"
            t_wvf_array.layout.dim[0].size = len(tonic)
            t_wvf_array.layout.dim[0].stride = 1

            t_wvf_array.data = tonic

            delta = 0.1

            msg = EDA()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = rospy.Time.from_sec(time_stamp)
            msg.eda_wvf = wvf_array

            # Phasic
            msg.p_wvf = p_wvf_array
            msg.p_mean = ph.Mean()(phasic)
            msg.p_std = ph.StDev()(phasic)
            msg.p_range = ph.Range()(phasic)
            msg.pks_max = ph.PeaksMax(delta=delta)(phasic)
            msg.pks_min = ph.PeaksMin(delta=delta)(phasic)
            msg.pks_mean = ph.PeaksMean(delta=delta)(phasic)
            msg.pks_n = ph.PeaksNum(delta=delta)(phasic)
            msg.dur_mean = ph.DurationMean(delta=delta)(phasic)
            msg.slopes_mean = ph.SlopeMean(delta=delta)(phasic)
            msg.p_auc = ph.AUC()(phasic)

            # Tonic
            msg.t_wvf = t_wvf_array
            msg.t_mean = ph.Mean()(tonic)
            msg.t_std = ph.StDev()(tonic)
            msg.t_range = ph.Range()(tonic)
            msg.t_auc = ph.AUC()(tonic)

            self.eda_pub.publish(msg)
            self.eda_wv.pop(0)
        
    def onHeartRate(self, hr):
        self.hr.append(hr[1])

        if len(self.hr) >= 1920:
            ppg_data = self.hr

            ppg_array = std_msgs.msg.Float32MultiArray()
            ppg_array.layout.data_offset = 0 
            ppg_array.layout.dim = [std_msgs.msg.MultiArrayDimension()]
            ppg_array.layout.dim[0].label = "ppg_waveform"
            ppg_array.layout.dim[0].size = len(ppg_data)
            ppg_array.layout.dim[0].stride = 1

            ppg_array.data = ppg_data

            msg = Heartrate()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = rospy.Time.from_sec(hr[0])
            msg.ppg_wvf = ppg_array
            msg.current_hr = hr[1]

            self.hr_pub.publish(msg) 
            self.hr.pop(0)
        
    def onSkinTemp(self, st):
        self.st.append(st[1])

        if len(self.st) >= 120:
            st_data = self.st

            st_array = std_msgs.msg.Float32MultiArray()
            st_array.layout.data_offset = 0 
            st_array.layout.dim = [std_msgs.msg.MultiArrayDimension()]
            st_array.layout.dim[0].label = "skin_temp"
            st_array.layout.dim[0].size = len(st_data)
            st_array.layout.dim[0].stride = 1

            st_array.data = st_data

            msg = SkinTemp()
            msg.header = std_msgs.msg.Header()
            msg.header.stamp = rospy.Time.from_sec(st[0])
            msg.st_data = st_array
            msg.current_st = st[1]
            msg.mean_st = np.mean(self.st)
            msg.std_st = np.std(self.st)

            self.st_pub.publish(msg)
            self.st.pop(0)

    def onAcc3D(self, acc):
        msg = Acc3D()
        msg.header = std_msgs.msg.Header()
        msg.header.stamp = rospy.Time.from_sec(acc[0])
        msg.acc_x = acc[1]
        msg.acc_y = acc[2]
        msg.acc_z = acc[3]
        self.acc_pub.publish(msg)
        
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
        