'''
merge all jmeter result file into one report file
'''
import os,os.path

__author__ = 'Administrator'
path = r'C:\tmp'
content = ''
for i in os.listdir(path):
    file_name = os.path.join(path,i)
    content += open(file_name).read().strip()+"\n"
open(os.path.join(path,'result_all.csv'),'w').write(content)