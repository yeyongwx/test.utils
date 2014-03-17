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

def addtodic(data_dic,time, latency):
    if data_dic.has_key(time):
        data_dic[time].append(latency)
    else:
        tmpl = [latency]
        data_dic[time] = tmpl

def getbasetimestamp():
    #应当考虑下有可能第一行的值并不是最小的值的问题
    datafile = r'C:\testresult\testresult_correct.txt'
    lines = open(datafile).readlines()
    #得到base time 以统计其后的请求返回时间与初始时间的差距
    line0 = lines[0]
    time = line0.strip().split(',')[0]
    basetimestamp = int(time[:-3])
    return basetimestamp

def parsedata(datafile):
    global interval, max
    data_dic={}
    max=0
    basetimestamp = getbasetimestamp()
    lines = open(datafile).readlines()
    for line in lines:
        if line.strip()=='': continue
        tmpl = line.strip().split(',')
        time = tmpl[0]
        time = time[:-3]
        time = (int(time) - basetimestamp)/interval + 1
        if time>max: max=time
        latency = int(tmpl[1])
        addtodic(data_dic,time, latency)
    return data_dic


def genchart(datafile1, datafile2, outputpng):
    global interval
    from pychartdir import *
    global max
    success_dic = parsedata(datafile1)
    fail_dic = parsedata(datafile2)
    data0=[]
    data1=[]
    label=[]
    for j in range(1,max+1):
        label.append(str(j))
        if success_dic.has_key(j):
            data0.append(len(success_dic[j]))
        else:
            data0.append(0)

        if fail_dic.has_key(j):
            data1.append(len(fail_dic[j]))
        else:
            data1.append(0)
    c = XYChart(1000,1000)
    # Add a title to the chart using 10 pt Arial font
    c.addTitle("         finished requests every %s seconds"%interval, "", 10)
    c.setPlotArea(30,20,900,900,0xffffc0, 0xffffe0)
    c.addLegend(55, 18, 0, "", 8).setBackground(Transparent)
    c.yAxis().setTitle("requests per %s seconds"%interval)
    c.yAxis().setTopMargin(20)

    layer = c.addBarLayer2(Side, 3)
    layer.addDataSet(data1,0x80ff80 , "Success Requests")
    layer.addDataSet(data0, 0xff8080, "Fail Requests")
    c.xAxis().setLabels(label)
    c.makeChart(outputpng)



if __name__=="__main__":
    global interval
    interval=10
    datafile1 = r'C:\testresult\testresult_correct.txt'
    datafile2 = r'C:\testresult\testresult_tree.txt'
    outputpng = r"C:\testresult\testresult_merge.png"
    genchart(datafile1,datafile2,outputpng)
