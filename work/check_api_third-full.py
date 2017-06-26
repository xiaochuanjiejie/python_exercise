# -*- coding: utf-8 -*-
__author__ = 'xujunchuan'

from subprocess import PIPE,Popen
import re

# last_minute_file = Popen('grep "$(date -d "-1 minutes" +"%H:%M:")" /data/behavior/hd/http/2016/06/01/info.log',shell=True, stdout=PIPE, stderr=PIPE)
last_minute_file = Popen('grep "00:00:" /Users/xujunchuan/Documents/info.log',shell=True, stdout=PIPE, stderr=PIPE)
stdout = last_minute_file.communicate()
# print type(stdout)    //tuple
file_1 = "".join(stdout)
# print type(file_1)        //str
file_2 = file_1.split('\n')
# print type(file_2),file_2[0]                  # //list
# print file_2[0].split()[6].split('/')[2]      # //domain
list_url = []
for line in file_2:
    if not line.strip():continue
    if float(line.split()[8].split(':')[1]) > 1000.0:
        # print line.split()[3],line.split()[6].split('/')[2],line.split()[8].split(':')[1]
        # print line.split()[3],line.split()[6].split('/')[2]
        ip = line.split()[3]
        url = line.split()[6].split('/')[2]
        ip_url = str(ip)+url
        list_url.append(ip_url)
list_url.sort()
set_ip_url = set(list_url)
for item in set_ip_url:
    print "the %s has found %d" % (item,list_url.count(item))
# print list(set(list_url))    //去重