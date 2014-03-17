#coding=utf-8
'''
从结果文件 .jtl中取出所有fail 的结果
并将timestamp转换成标准日期时间格式
'''
__author__ = 'Administrator'
lines = open(r'C:\testresult\testresult_rkb_ueTrack_all.jtl').readlines()
print len(lines)
import time
flag = 0
content = '<testresult>'
count=0
for i in lines:
    count+=1
    # print count
    if flag==0 and (i.find('s="false"')>0):
        flag = 1
        ts = i.split(" ")[3][4:-1]
        # print ts
        new_ts = time.strftime('%Y-%m-%d %X',time.localtime(int(ts[:-3])))
        i = i.replace(str(ts),new_ts)
        content += i
    elif flag == 1:
        content += i
        if i.find('</httpSample>')>-1:
            flag=0
content +='</testresult>'
open('d:/failresult.xml','w').write(content)