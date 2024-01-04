#import list
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy as sy
import math
import pandas as pd
from scipy.fftpack import fft
import pywt
from scipy import signal

import os
def lenpath(path):
    # 输入文件夹地址
    files = os.listdir(path)   # 读入文件夹
    num_png = len(files)
    return num_png
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
def biaozhuncha(x):
    sum=0
    for i in range(len(x)):
        sum+=(x[i])**2
    return np.sqrt(sum/len(x))
def hampel(x,k,sigma):
    print(k,len(x)-k)
    for i in range(k,len(x)-k):
        l=np.array(x[i-k:i+k+1])
        medi=np.median(l)

        norm=l.copy()
        ave=np.sum(l)/len(l)
        nor=norm-ave
        norm=biaozhuncha(nor)
        for ii in range(len(l)):
            if(abs(l[ii]-medi)>=sigma*1.4826*norm):

                l[ii]=medi
            else:

                continue
        x[i-k:i+k+1]=l
    return x
#l: list to be dealed with
#power list
def Gauss_filter(l, lp):
    if (len(lp) % 2 == 0):
        print('invalid window')
        return 0  # window length should be odd
    else:
        lt = list(l.copy())
        m = len(lp)  # window length
        for i in range(int((m - 1) / 2)):
            lt.append(l[-1])
            lt.insert(0, l[0])
        ltt = lt.copy()
        print(ltt)
        for i in range(len(l)):
            sum = np.sum(np.array(lp) * np.array(ltt[i:m + i]))
            print(sum)
            lt[int((m - 1) / 2) + i] = sum/np.sum(lp)
        return lt
#方差
#l is the list to be done
#m is the variance gate
#w is the windows length, for convenience,we order it to be a odd
# def variance(l,m,w):
#     for i in range(len(l)-w):

#main
dir_ = 'C:\\Users\\rossoneri\\Desktop\\DIFFERENT_PHASE\\wave'
file_name='csi_one_wave.txt'
dir2='C:\\Users\\rossoneri\\Desktop\\DIFFERENT_PHASE\\after_0726_fft&db4\\'
for ii in range(1):
    ii=three_bit(ii)
    dir1=dir_ + ii
    for iii in range(1):
        num=ii+'\\'
        file_l=dir1+'\\0726_'+ii+'_'+three_bit(iii)+'.txt'
        f= open(file_l)
        csi=[]
        for line in f:
            csi.append(line.strip())
        for i in range(len(csi)):

            csi[i]=float(csi[i])
            if(csi[i]<0):
                csi[i]=csi[i]+180
            else:
                continue
        plt.plot(csi)
        plt.show()
        plt.figure()
        csi=hampel(csi,int(2.5*len(csi)/30),2.3)
        plt.plot(-np.array(csi))
        plt.show()
        plt.figure()
        csi=hampel(csi,int(1/16*len(csi)/30+0.5),2.4)
        plt.plot(-np.array(csi))
        plt.show()
        plt.figure()
        csi,lll=pywt.dwt(csi, 'db2', mode='symmetric', axis=-1)
        plt.plot(-np.array(csi))
        plt.show()
        plt.figure()
        #csi=Gauss_filter(csi,[1,1.5,1])
        l1=5 / len(csi) * 30
        l2=10*l1
        print('ll',l1,l2)
        b,a=signal.butter(2,[1/12/len(csi)*30,1/1.2/len(csi)*30],'bandpass')
        csi=signal.filtfilt(b,a,csi)
        plt.plot(-np.array(csi))
        plt.title('sdai')
        plt.show()
        plt.figure()
        w=np.linspace(0,30,len(csi))
        fed=sy.fft.fft(csi)
        fed=fed/len(fed)
        a=int(0.083/(len(csi)/30)*len(csi))
        b=int(0.83/(len(csi)/30)*len(csi))
        m=abs(fed[a:b])
        plt.plot(fed)
        plt.title('fed')
        plt.show()
        plt.title('m')
        plt.plot(m)
        plt.show()
        msg=''
        for ik in range(len(m)):
            msg+=str(m[ik])+'\n'
        text_create(dir2,'after_db_fft'+str(ii)+'_'+three_bit(iii)+'.txt',msg)








