#coding=utf-8
'''
准备测试用的数据文件

select DISTINCT tubi.user_key,tulr.ue_sn from t_ue_location_read tulr,t_user_basic_info tubi,t_ue_basic_info tuebi
where tuebi.ue_sn=tulr.ue_sn and tuebi.sim_id=tubi.id

'''
import urllib
__author__ = 'yeyong'
tmp_str=""
lines = open(r'C:\data\getverifycode.txt').readlines()
for line in lines:
    mobile = line.strip()
    passwd='123abc'
    tmp_str+=urllib.quote(mobile+"|"+passwd)+'\n'

#print tmp_str
tmp_str = tmp_str[:-2] #remove last '\n'
f=open('c:/data/gpsdtd_data.txt','w')
f.write(tmp_str)
f.close()