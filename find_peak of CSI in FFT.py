import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy as sy
import math
import pandas as pd
from scipy.fftpack import fft
import pywt


def three_bit(x):
    if(x<10):
        return '00'+str(x)
    if(x>=10 and x<100):
        return '0'+str(x)
    else:
        return str(x)
def text_create(dir_,name,msg):
    path=dir_+name+'.txt'
    file=open(path,'w')
    file.write(msg)
    file.close()

def peak(a):
    return a.index(max(a))

dir_='C:\\Users\\rossoneri\\Desktop\\DIFFERENT_PHASE\\after_0726_fft&db4\\'
for i in range(1):
    i=three_bit(i)
    for ii in range(50):
        name=dir_+'after_db_fft'+i+'_'+three_bit(ii)+'.txt.txt'
        f=open(name)
        fl=[]
        for line in f:
            fl.append(line.strip())
        for ii in range(len(fl)):
            fl[ii]=float(fl[ii])
        plt.plot(fl)
        plt.show()
        ltot=len(fl)/0.45
        print(peak(fl))
        Hz=50*(peak(fl)/len(fl))+5*(1-peak(fl)/len(fl))
        print(Hz)



















