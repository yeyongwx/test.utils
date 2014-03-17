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
import time

def addtodic(time, latency):
    global data_dic
    if data_dic.has_key(time):
        data_dic[time].append(latency)
    else:
        tmpl = [latency]
        data_dic[time] = tmpl

def parsedata():
    content = ''
    global data_dic,max
    max=0
    interval = 10
    #因为是规范数据，不用正则
    datafile = r'C:\testresult\bak_400_60_80\testresult_correct.txt'
    lines = open(datafile).readlines()
    for line in lines:
        stime = line.strip().split(',')[0]
        sstime = stime[:-3]
        sstime = time.strftime('%Y-%m-%d %X',time.localtime(int(sstime)))
        line = line.replace(stime,sstime)
        content += line
    open('c:/test.txt','w').write(content)




if __name__=="__main__":
    parsedata()
