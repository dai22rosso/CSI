# -*- coding: utf-8 -*-
import xlsxwriter as xw
import os
import numpy
def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['number','cal_BPM', 'CSI_DATA', 'ERROR']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]['num'],data[j]["BPM"], data[j]["CSI"], data[j]["error"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表
def xw_toExcel_2(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['number','pp1', 'pp2', 'fff1','fff2','error']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]['num'],data[j]["pp1"], data[j]["pp2"], data[j]["fff1"],data[j]["fff2"],data[j]["error"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表
def get_three(file):
    f=open(file)
    data=f.readlines()
    f.close()
    return data
def three_bit(x):
    if(x<10):
        return '00'+str(x)
    if(x>=10 and x<100):
        return '0'+str(x)
    else:
        return str(x)
def get_file_extension(filename):
    arr = os.listdir(filename)
    return arr
def test_if_there_is(file_path,pp1,pp2,fff1,fff2):
    x = get_file_extension(file_path)
    s=0
    for i in range(len(x)):
        if x[i]=='compared_p1_'+str(pp1)+'_p2_'+str(pp2)+'_q1_'+str(fff1)+'_q2_'+str(fff2)+'.txt':
            s=s+1
        else:
            pass
    return s
# "-------------数据用例-------------"
# for pp1 in range(80,140,5):
pp1=150
fff1=100
take_Data=[]
for pp2 in range(30,40,5):
        # for fff1 in range(60,160,10):
    for fff2 in range(170,180,10):
        testData = [
        ]
        error_l=[]
        for sdir in range(138):
            dir = './wave2process/tdx_wave_0726/wave_csv_'+three_bit(sdir)
            if(test_if_there_is(dir,pp1,pp2,fff1,fff2)==0):
                continue
            else:
                dir=dir+'/compared_p1_'+str(pp1)+'_p2_'+str(pp2)+'_q1_'+str(fff1)+'_q2_'+str(fff2)+'.txt'
                Data=get_three(dir)
                if(len(Data)>=6):
                    error_l.append(float(Data[5]))
                    testData.append({'num':float(sdir),'BPM':float(Data[1]),'CSI':float(Data[3]),'error':float(Data[5])})
        print(error_l)
        take_Data.append({'num':float(sdir),'pp1':float(pp1),'pp2':float(pp2),'fff1':float(fff1),'fff2':float(fff2),'error':float(numpy.average(error_l))})


        fileName = './math_method_'+'compared_p1_'+str(pp1)+'_p2_'+str(pp2)+'_q1_'+str(fff1)+'_q2_'+str(fff2)+'.xlsx'
        xw_toExcel(testData, fileName)
        fileName2 = './math_method_' + 'compared_150_100_3.xlsx'
        xw_toExcel_2(take_Data,fileName2)
