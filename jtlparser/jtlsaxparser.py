from xml.sax import *

class UserDecodeHandler(ContentHandler):
    latency = None
    ts = None
    ts_new = None
    s = None
    lb = None
    responsedata = None
    url = None
    results = None
    result = {}
    temp = None
    currenttag = None

    def startDocument(self):
        print "start xml document"

    def endDocument(self):
        print "end xml document"

    def startElement(self, name, attrs):
        if name == "testResults":
            self.results = []
        elif name == "httpSample":
            self.result = {}
            self.result['lt'] = attrs['lt']
            self.result['ts'] = attrs['ts']
            self.result['s'] = attrs["s"]
            self.result['lb'] = attrs['lb']
            self.result['rc'] = attrs['rc']
        self.currenttag = name
        self.temp = ''

    def endElement(self, name):
        if name == "httpSample":
            self.results.append(self.result)
        self.temp = ''
        self.currenttag = None

    def characters(self, content):
        self.temp += content
