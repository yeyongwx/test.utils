#coding=utf-8
'''
gen test .jmx file from a template file
with the given parameter (the API name)
'''
__author__ = 'Administrator'
import os
import os.path

global file_location, templatefile, file_prefix

file_location = r'C:\apache-jmeter-2.10\extras'
templatefile = r'C:\apache-jmeter-2.10\extras\Test_SVR_API.template'



def genfile(api, file_location, file_prefix):
    global templatefile
    content = open(templatefile).read()
    content = content.replace('gpsdtd', api)
    file_name = "%s%s.jmx" % (file_prefix, api)
    open(os.path.join(file_location, file_name), 'w').write(content)
    print 'file generated: %s'%os.path.join(file_location,file_name)
    totalUser=400
    ramptime=totalUser/2
    loops=300
    original = r'<stringProp name="ThreadGroup.num_threads">20</stringProp>'
    threads = r'<stringProp name="ThreadGroup.num_threads">%d</stringProp>'% totalUser
    content = content.replace(original,threads)
    original = r'<stringProp name="ThreadGroup.ramp_time">10</stringProp>'
    ramptime = r'<stringProp name="ThreadGroup.ramp_time">%d</stringProp>'%ramptime
    content = content.replace(original,ramptime)
    original = r'<stringProp name="LoopController.loops">5</stringProp>'
    loops = r'<stringProp name="LoopController.loops">%d</stringProp>'%loops
    content = content.replace(original,loops)
    if api=='gpsdtd':
        content = content.replace(r'testname="所有结果_xml" enabled="true"',r'testname="所有结果_xml" enabled="false"')
    open(os.path.join(file_location,'bigdata', file_name), 'w').write(content)
    print 'file generated: %s'%os.path.join(file_location,'bigdata',file_name)


def genfiles():
    content =r'''del C:\apache-jmeter-2.10\extras\*.jtl
del C:\testresult\*.csv
del C:\testresult\*.jtl
del C:\apache-jmeter-2.10\bin\*.csv'''+"\n"
    global file_location
    file_prefix = 'Test_SVR_API_1.1_'
    # api_1_1_list = ['rk_checkAccount','rk_setPwd','rk_register','rk_getVeriCode','rk_login',
    #             'rk_ueTrack','rk_ueList','rk_ueStatus','rk_ueLocation','rk_ueInfo','rk_upCoord',
    #             'rkb_ueTrack','rkb_ueList','rkb_ueStatus']
    api_1_1_list = ['rk_checkAccount', 'rk_login',
                    'rk_ueTrack', 'rk_ueList', 'rk_ueStatus', 'rk_ueLocation', 'rk_ueInfo',
                    'rkb_ueTrack', 'rkb_ueList', 'rkb_ueStatus']

    for i in api_1_1_list:
        #content += "ant -Dtest=%s%s run\n"%(file_prefix,i)
        open(os.path.join(file_location,"%s%s.bat"%(file_prefix,i)),'w').write("ant -Dtest=%s%s run\n"%(file_prefix,i))
        content += 'call %s%s.bat\n'%(file_prefix,i)

    for api in api_1_1_list:
        genfile(api, file_location, file_prefix)

    file_prefix = 'Test_SVR_API_1.0_'
    api_list = ['lg', 'gtm', 'sl',
                'sll', 'gdh', 'gpsdtd']
    # api_list = ['getVeriCode','rg','lg','new_bs','bindnumber','bind_lastsix','unbsm',
    #             'cp','cmdtoue','gtm','sl','sll','gdh','chkapp','gpsdtd']

    for api in api_list:
        genfile(api, file_location, file_prefix)

    for i in api_list:
        open(os.path.join(file_location,"%s%s.bat"%(file_prefix,i)),'w').write("ant -Dtest=%s%s run\n"%(file_prefix,i))
        content += 'call %s%s.bat\n'%(file_prefix,i)

    content = content[:-1]
    open(r'C:\apache-jmeter-2.10\extras\testrun.bat','w').write(content)



def main():
    genfiles()


if __name__ == '__main__':
    main()
