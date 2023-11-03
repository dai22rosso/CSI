# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 17:25:26 2023

@author: xihes2
"""
import pandas as pd
import math
from scipy import signal
import numpy as np
import os

# Functions
def three_bit(x):
    if(x<10):
        return '00'+str(x)
    if(x>=10 and x<100):
        return '0'+str(x)
    else:
        return str(x)
    
# Main
for No in range (0,140):
    # make new folder
    os.mkdir("./wave"+three_bit(No))
    
    dir_ = './tdx_wave_0726/wave_csv_'+three_bit(No)+'/'
    datas = np.load(dir_+'rx.npz')
    print(datas.files)
    Timestamp = datas['Timestamp']
    SubcarrierIndex = datas['SubcarrierIndex']
    Csi = datas['Csi']
    RSSI = datas['RSSI']
    noiseFloor = datas['noiseFloor']
    Num_Tx = int(datas['Num_Tx'])
    Num_Rx = int(datas['Num_Rx'])
    centerFrequency = int(datas['centerFrequency'])
    channelBandWidth = int(datas['channelBandWidth'])
    Mag = np.abs(Csi)
    Phase = np.angle(Csi, deg=True)
    Num_Ts = Timestamp.size
    Num_Sc = SubcarrierIndex.size
    Seconds = Timestamp - Timestamp[0]
    
    # calculate differental phase
    diff_Phase = np.zeros([Num_Ts, Num_Tx, Num_Sc])
    for txid in range(Num_Tx):
        
        diff_Phase[:,txid,:] = Phase[:,txid,1,:] - Phase[:,txid,0,:]
        diff_Phase_ori = diff_Phase.copy()
        for scid in range(Num_Sc):
            temp = diff_Phase[:,txid, scid].copy()
            while np.mean(temp)-np.min(temp)>180:
                n_t_360 = np.where(temp<np.mean(temp)-180)[0]
                diff_Phase[n_t_360,txid, scid] += 360
                temp = diff_Phase[:, txid, scid].copy()
            while np.max(temp)-np.mean(temp)>180:
                n_t_360 = np.where(temp>np.mean(temp)+180)[0]
                diff_Phase[n_t_360,txid, scid] -= 360
                temp = diff_Phase[:,txid, scid].copy()
            ratio_lowlier = np.sum(temp<-180)/temp.size
            ratio_uplier = np.sum(temp>180)/temp.size
            if ratio_lowlier > 0.5:
                diff_Phase[:,txid, scid] += 360
            if ratio_uplier > 0.5:
                diff_Phase[:,txid, scid] -= 360
                
            subcarrier_diff_phase=diff_Phase[:,txid,scid]
            txt_name='0726wave_'+three_bit(No)+"_"+three_bit(scid)+".txt"
    
            np.savetxt(("./wave"+three_bit(No)+"/"+txt_name, subcarrier_diff_phase, fmt='%.8f')
