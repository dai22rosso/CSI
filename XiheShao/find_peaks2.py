# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:40:44 2023

@author: Ivan
"""

import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Sample dataset (replace this with your actual data)
result=pd.DataFrame()
for x in range (10):
    for y in range (10):
        file_index=str(x)+str(y)
        inputdata=pd.read_csv(r"tdx_wave_0725\wave_csv_0"+file_index+"\wave.csv")
        data1=inputdata['wave']
        data=np.array(data1.values.tolist())
        temp_dataframe=pd.DataFrame()
        # Find peaks in the dataset
        for a in [10]:
            for b in [15,20,25]:
                for c in [len(data)/100,len(data)/90,len(data)/80,len(data)/70,len(data)/60]:
                    
                    peaks, _ = find_peaks(data,\
                                          distance=a, prominence=b, width=c)
              
                    # Plot the dataset with the identified peaks
                    # plt.plot(data)
                    # plt.plot(peaks, data[peaks], "ro", label="Peaks")
                    # plt.xlabel("Data Point Index")
                    # plt.ylabel("Value")
                    # plt.legend()
                    # plt.show()
            
                    # Count the number of peaks
                    num_peaks = len(peaks)
                    total_time = len (data)
                    
                    #start record from the second peak and end at second last.
                    effective_time = peaks[len(peaks)-2]-peaks[1] 
                    effective_period=num_peaks-2-1
                    
                    #estimated number of period
                    peaks_est=effective_period/effective_time*total_time 
                    
                    
                    column= "d"+str(a)+"p"+str(b)+"w"+str(c)
                    temp_dataframe=pd.concat([temp_dataframe,pd.DataFrame\
                                      ({column:[peaks_est]})], \
                                     ignore_index=False, axis=1)
                    #print(effective_time)
                    #print(f"Number of peaks: {num_peaks}""\n""est peaks in 30s:",peaks_est)
        #combine each row
        result=pd.concat([result,temp_dataframe], ignore_index=True)
        
#output csv file
result.to_csv("est_peaks.csv")
