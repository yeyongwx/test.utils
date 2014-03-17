#coding=utf-8
'''
准备测试用的数据文件
'''

__author__ = 'yeyong'
tmp_str=""
lines = open('c:/data/tmp.txt').readlines()
for line in lines:
    sn,userkey = line.strip().split("\t")
    sn = sn.strip()
    userkey = userkey.strip()
    tmp_str+=userkey+"%7C"+sn+"%7C"+sn+'\n'
#print tmp_str
f=open('c:/data/sll_data.txt','w')
f.write(tmp_str)
f.close()