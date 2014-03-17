import socket
from urllib2 import urlopen
import time
import traceback

def run(server,port):
    count = 0
    while (count < 5):
        try:
            print "[%s] Connecting to server ..." % (time.strftime("%Y-%m-%d %H:%M:%S"))
            tomcaturl = 'http://%s:%s/'%(server,port)
            socket.setdefaulttimeout(5)
            data = urlopen(tomcaturl)
            a =data.read()
            if len(a)>0:
                import os
                chkfile = os.path.join('status/tomcaton.txt')
                open(chkfile,'w').write(str(a))
                print "[%s] Server connected ..." % (time.strftime("%Y-%m-%d %H:%M:%S"))
                print "%s..."%(a[:400])
                return
        except:
            # traceback.print_exc()
            count = count + 1
            print "[%s] Connection failed, the server is not online." % (time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(5)
            print "[%s] Now reconnecting..." % (time.strftime("%Y-%m-%d %H:%M:%S"))

    if count == 5:
        print "[%s] Connection to server failed 5 times, server is not online." % (time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    import sys
    argvs = sys.argv
    if len(argvs)!=3:
        server = '192.168.10.9'
        port = '80'
    else:
        server,port = argvs[1],argvs[2]
    run()




