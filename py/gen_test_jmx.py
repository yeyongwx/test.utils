'''
gen test .jmx file from a template file
with the given parameter (the API name)
'''
__author__ = 'Administrator'
import os, os.path

global file_location,templatefile,file_prefix

file_location=r'C:\apache-jmeter-2.10\extras'
templatefile=r'C:\apache-jmeter-2.10\extras\Test_SVR_API_1.0_gpsdtd.jmx'
file_prefix='Test_SVR_API_1.0_'

def genfile(api, file_location):
    global templatefile
    content = open(templatefile).read()
    content = content.replace('gpsdtd',api)
    file_name="%s%s.jmx"%(file_prefix,api)
    open(os.path.join(file_location,file_name),'w').write(content)

def genfiles():
    global file_location
    api_list = ['getVeriCode','rg','lg','new_bs','bindnumber','bind_lastsix','unbsm',
                'cp','cmdtoue','gtm','sl','sll','gdh','chkapp']
    for api in api_list:
        genfile(api,file_location)

def main():
    genfiles()

if __name__=='__main__':
    main()
