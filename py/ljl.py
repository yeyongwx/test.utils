#coding=utf-8
'''
计算成本
'''
__author__ = 'Administrator'

line=open(r"D:\ljl.txt").readlines()
print line[0].strip().replace('drsm=',"")
drsm=int(line[0].strip().replace('drsm=',""))
drhy=int(line[1].strip().replace('drhy=',""))
drkq=int(line[2].strip().replace('drkq=',""))
drzs=int(line[3].strip().replace('drzs=',""))
cbw=int(line[4].strip().replace('cbw=',""))
cwg=int(line[5].strip().replace('cwg=',""))
crj=int(line[6].strip().replace('crj=',""))
rtk=int(line[7].strip().replace('rtk=',""))
a=drsm*64+drhy*100+drkq*100+drzs*100+cbw*128+crj*64+cwg*64+rtk*60+26100
print a
print 33000-a
print 31600-a