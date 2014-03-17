#coding=utf-8
'''
数据样例:
1392259944182,227,get_CUR_LOC,200,OK,Mix threadGroup 1-1,text,true,519,227
1392259944377,126,get_CUR_LOC,200,OK,Mix threadGroup 1-2,text,true,518,126
1392259944411,162,get_CUR_LOC,200,OK,Mix threadGroup 1-1,text,true,519,162
1392259944511,172,get_CUR_LOC,200,OK,Mix threadGroup 1-2,text,true,518,172
'''
__author__ = 'Administrator'
global data_dic,max

def addtodic(time, latency):
    global data_dic
    if data_dic.has_key(time):
        data_dic[time].append(latency)
    else:
        tmpl = [latency]
        data_dic[time] = tmpl

def getbasetimestamp():
    datafile = r'C:\testresult\testresult_correct.txt'
    lines = open(datafile).readlines()
    #得到base time 以统计其后的请求返回时间与初始时间的差距
    line0 = lines[0]
    time = line0.strip().split(',')[0]
    basetimestamp = int(time[:-3])
    return basetimestamp

def parsedata(datafile,outputpng):
    global data_dic,max
    max=0
    interval = 10
    #因为是规范数据，不用正则
    #得到base time 以统计其后的请求返回时间与初始时间的差距
    basetimestamp = getbasetimestamp()
    data_dic = {}
    lines = open(datafile).readlines()
    for line in lines:
        if line.strip()=='': continue
        tmpl = line.strip().split(',')
        time = tmpl[0]
        time = time[:-3]
        time = (int(time) - basetimestamp)/interval + 1
        if time>max: max=time
        latency = int(tmpl[1])
        addtodic(time, latency)
    printdatadic(outputpng)

def printdatadic(outputpng):
    from pychartdir import *
    global data_dic,max
    # X_time=[]
    # Y_count=[]
    # tmp_dic={}
    # for i in data_dic.keys():
    #     X_time.append(i)
    #     Y_count.append(len(data_dic[i]))
    #     tmp_dic[i]=len(data_dic[i])
    data=[]
    label=[]
    print max
    for j in range(1,max+1):
        label.append(str(j))
        if data_dic.has_key(j):
            data.append(len(data_dic[j]))
        else:
            data.append(0)
        print label[j-1],data[j-1]
    c = XYChart(1000,1000)
    c.setPlotArea(30,20,900,900)
    c.addBarLayer(data)
    c.xAxis().setLabels(label)
    c.makeChart(outputpng)

if __name__=="__main__":
    datafile = r'C:\testresult\testresult_correct.txt'
    outputpng = r"C:\testresult\testresult_correct.simplebar.png"
    parsedata(datafile,outputpng)
    datafile = r'C:\testresult\testresult_tree.txt'
    outputpng = r"C:\testresult\testresult_fail.simplebar.png"
    parsedata(datafile,outputpng)
