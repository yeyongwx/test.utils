class Sampler(object):

    def __init__(self, name):
        self.name = name
        self.results = []
        self.lt_list = []
        self.ts_list = []
        self.s_list = []
        self.rc_list = []
        self.total_lt = 0

    def sort(self):
        self.lt_list.sort()

    def add_result(self, result):
        # result should be a list with given sequenced values like below:
        # [lt, ts, s , rc]
        lt, ts, s, rc = result
        lt = int(lt)
        s = str(s)
        rc = str(rc)
        self.lt_list.append(lt)
        self.ts_list.append(ts)
        self.s_list.append(s)
        self.rc_list.append(rc)
        self.total_lt += int(lt)

    def get_latency_average(self):
        return self.total_lt / len(self.lt_list)

    def sort_latency_list(self):
        self.lt_list.sort()

    def get_latency_50(self):
        total_l = len(self.lt_list)
        return self.lt_list[int((total_l - 1) * 0.5)]

    def get_latency_60(self):
        total_l = len(self.lt_list)
        return self.lt_list[int((total_l - 1) * 0.6)]

    def get_latency_70(self):
        total_l = len(self.lt_list)
        return self.lt_list[int((total_l - 1) * 0.7)]

    def get_latency_80(self):
        total_l = len(self.lt_list)
        return self.lt_list[int((total_l - 1) * 0.8)]

    def get_latency_90(self):
        total_l = len(self.lt_list)
        return self.lt_list[int((total_l - 1) * 0.9)]

    def get_latency_100(self):
        total_l = len(self.lt_list)
        return self.lt_list[(total_l - 1)]

    def get_fail_rate(self):
        from collections import Counter
        counter = Counter(self.s_list)
        if 'false' in counter.keys():
            fail = counter.get('false')  # false means failed
        else:
            fail = 0

        return "%s" % str(float(fail)/float(len(self.s_list))*100.0)

    def get_http_code(self):
        return ",".join(set(self.rc_list))

    def get_min_latency(self):
        return self.lt_list[0]

    def get_max_latency(self):
        return self.lt_list[-1]

    def get_total_samples_number(self):
        return len(self.lt_list)

    def print_self(self):
        print self.name
        print self.lt_list
        print self.rc_list
        print self.s_list
