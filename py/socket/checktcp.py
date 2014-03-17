__author__ = 'Administrator'

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def checkserver(sock):
    import time
    time.sleep(1)
    print '[%s] Sending a T1 to server and waiting for response...'%(time.strftime("%Y-%m-%d %H:%M:%S"))
    sock.send('[2012-03-01 10:44:38,0,W1,000872209,T1,15061528443,15801090383,123456,11,460023615223538,355889008722099,TBIT]')
    resp = sock.recv(1024)
    sock.close()
    import os
    chkfile = os.path.join('tcpserveron.txt')
    count = 0
    if str(resp).find('S1')>0:
        open(chkfile,'w').write(resp)
        print "[%s] Got a S1 response from server. Server is online now."%(time.strftime("%Y-%m-%d %H:%M:%S"))
        exit()
    else:
        count = count +1
        print "[%s] S1 not received, sleep for 5 seconds then reconnect..."%(time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(5)

import sys

argvs = sys.argv
if len(argvs)!=3:
    server = '192.168.10.9'
    port = '8086'
else:
    server,port = argvs[1],argvs[2]

import time
count = 0
while (count < 5):
    try:
        print "[%s] Connecting to server %s:%s..."%(time.strftime("%Y-%m-%d %H:%M:%S"),server,port)
        sock.connect((server,int(port)))
        print "[%s] Server connected ..."%(time.strftime("%Y-%m-%d %H:%M:%S"))
        break
    except:
        count = count +1
        print "[%s] Connection failed, the server is not online."%(time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(5)

if count ==5:
    print "[%s] Connection to server failed 5 times, server is not online."%(time.strftime("%Y-%m-%d %H:%M:%S"))
    exit()
checkserver(sock)
print "[%s] S1 not received , the server is not online."%(time.strftime("%Y-%m-%d %H:%M:%S"))


