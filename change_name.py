import os


# -*- coding: utf-8 -*-
import os
#设定文件路径
# -*- coding:utf-8 -*-
import os


# 获取文件的扩展名
def get_file_extension(filename):
    arr = os.listdir(filename)
    print(arr)
    return arr
def three_bit(x):
    if(x<10):
        return '00'+str(x)
    if(x>=10 and x<100):
        return '0'+str(x)
    else:
        return str(x)

for i in range(200):
    filename='./wave2process/ddy_wave/wave_csv_'+three_bit(i)
    x=get_file_extension(filename)
    if(x[0][len(x[0])-3:len(x[0])]=='npz'):
        os.rename(filename+'/'+x[0],filename+'/'+'rx.npz')
        os.rename(filename+'/'+x[1],filename+'/'+'wave.csv')
    if(x[0][len(x[0])-3:len(x[0])]=='csv'):
        os.rename(filename+'/'+x[0],filename+'/'+'wave.csv')
        os.rename(filename+'/'+x[1],filename+'/'+'rx.npz')



# path = '文件夹所在路径'
# # 路径下的所有文件夹列表folderlist
# folderlist = os.listdir(path)
# # 对于每个文件夹内的文件
# for folder in folderlist:
#     inner_path = os.path.join(path, folder)
#     filelist = os.listdir(inner_path)
#     # 对于每个文件，分别修改文件名为所在文件夹的名称
#     for item in filelist:
#         os.rename(inner_path + '\\' + item, inner_path + '\\' + str(folder) + get_file_extension(item))



