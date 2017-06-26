#-*- coding: utf-8 -*-

class FindIp(object):
    def __init__(self,path):
        self.txt = path
    def chou_sogou_ip(self):
        file1 = open(self.txt,'r')
        iplist = []
        for line in file1:
            ss = line.find('"Sogou web spider/4.0')
            if ss > 0:
                iplist.append(line[:ss].strip())
        file1.close()
        return iplist

p = FindIp('/tmp/ip.txt')
s = p.chou_sogou_ip()
print list(set(s))