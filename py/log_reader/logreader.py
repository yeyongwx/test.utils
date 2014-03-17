__author__ = 'Administrator'
'''
use cmd:
        grep -c -n -i -e 'error' -e 'exception' nohup.out
will get the number of matched lines

use cmd
       grep -C 10 -n -i -e 'error' -e 'exception' nohup.out

'''

def parse(logfile):
    i=0
    with open(logfile) as fp:
        for line in fp:
            i=i+1
            readline(line,i)

def readline(line,i):
    global lines
    tmpline = line.lower()
    # print tmpline
    if ((tmpline.find('error')>-1)|(tmpline.find('exception')>-1)):
        lines.append(('%s %s')%(str(i).ljust(10),line))

def getnumber(countfile,total_errors):
    #need try catch here
    try:
        old_count = int(open(countfile).read().strip())
        open(countfile,'w').write(str(total_errors))
        return total_errors-old_count
    except Exception, e:
        print e
        try:
            open(countfile,'w').write(str(total_errors))
            return total_errors
        except Exception,e:
            print e.message



if __name__=="__main__":
    import time
    import sys
    argv = sys.argv
    global lines
    lines=[]
    old_time = time.time()
    logfile= r'D:\tmp\nohup.out'
    resultfile=r'd:\tmp\log_result.txt'
    countfile = r'd:\tmp\logcount.txt'
    if len(argv)==4:
        logfile=sys.argv[1]
        resultfile=sys.argv[2]
        countfile=sys.argv[3]
    parse(logfile)

    total_errors = len(lines)
    new_count = getnumber(countfile,total_errors)

    if new_count==0:
        new_error_lines=[]
    else:
        new_error_lines = lines[-new_count:]
    content = ''
    for i in new_error_lines:
        content = content+'\n'+i.strip()
    open(resultfile,'w').write(content)

    now=time.time()
    print 'Total processed: %s'%(now-old_time)
    print 'Total results: %s'%len(lines)
    print 'New errors: %s'%(str(new_count))
