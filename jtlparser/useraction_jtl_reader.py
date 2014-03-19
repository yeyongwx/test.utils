#coding = utf-8
"""
this script is used to generate the general report from the result jtl file
"""
from xml.sax import *
import time
from Sampler import Sampler
from jtlsaxparser import UserDecodeHandler


def run(basedir, targetfile):
    import os
    parser = make_parser()
    handler = UserDecodeHandler()
    parser.setContentHandler(handler)
    start = time.time()
    parser.parse(os.path.join(basedir, targetfile))
    end = time.time()
    print end - start

    print "Total records: %s" % str(len(handler.results))
    obj_dic = {}
    for item in handler.results:
        latency = item['lt']
        ts = item['ts']
        result = item['s']
        rc = item['rc']
        request_name = item['lb']
        if not(request_name in obj_dic.keys()):
            obj_dic[request_name] = Sampler(request_name)
        obj_dic[request_name].add_result([latency, ts, result, rc])

    print time.time() - end

    content = ""
    for obj_name in obj_dic.keys():
        sampler = obj_dic[obj_name]

        sampler.sort()
        content += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" \
                   "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (obj_name,
                                                                                     sampler.get_total_samples_number(),
                                                                                     sampler.get_latency_average(),
                                                                                     sampler.get_latency_50(),
                                                                                     sampler.get_latency_60(),
                                                                                     sampler.get_latency_70(),
                                                                                     sampler.get_latency_80(),
                                                                                     sampler.get_latency_90(),
                                                                                     sampler.get_latency_100(),
                                                                                     sampler.get_min_latency(),
                                                                                     sampler.get_max_latency(),
                                                                                     sampler.get_http_code(),
                                                                                     sampler.get_fail_rate())

    header = "<tr><th>URI</th><th>Samples</th><th>Average(ms)</th><th>50% Line</th><th>60% Line</th>" \
             "<th>70% Line</th><th>80% Line</th><th>90% Line</th><th>100% Line</th><th>Min(ms)</th>" \
             "<th>Max(ms)</th><th>HTTP Code</th><th>Errors(%)</th></tr>"
    html_content = '<table cellspacing="0" cellpadding="0" border="1">%s%s</table>' % (header, content)

    open('d:/tmp/index.html', 'w').write(html_content)

if __name__ == "__main__":
    start = time.time()
    basedir = r'D:\tmp\231446_20140317'
    targetfile = r'212_useraction.jtl'
    run(basedir, targetfile)
    end = time.time()
    print 'Total process time: ', (end - start)