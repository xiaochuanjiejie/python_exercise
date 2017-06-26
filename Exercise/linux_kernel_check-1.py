# -*- coding: utf-8 -*-
__author__ = 'xujunchuan'

from subprocess import PIPE,Popen
import re
import time
import os
import json
import time
import socket
import requests
import sys
import getopt
import urllib,httplib

#basic falcon info
conf = '/users/xujunchuan/documents/cfg.json'
# conf = '/usr/local/lemonitor/falcon-agent/cfg.json'
agentposturl = 'http://localhost:1567/v1/push'
tmplist = []
info_res = {}

#file info
TIMEFORMAT='%H:%M:'
before_time = time.time() - 60
file_time = time.strftime(TIMEFORMAT,time.localtime(before_time))
file_path = '/users/xujunchuan/documents/messages'
# file_path = '/var/log/messages'
filter_str = ['kernel:','Out of memory']

def simplemetric(endpoint,metric,ts,step,value,countertype,tags):
    data = {
        "endpoint": endpoint,
        "metric": metric,
        "timestamp": ts,
        "step": step,
        "value": value,
        "countertype": countertype,
        "tags": tags
    }
    return data

def basicinfo(conf):
    with open(conf) as mid:
        source = json.load(mid)
        info_res['hostname'] = source["hostname"]
    return info_res

#取IP
basicinfo(conf)
print info_res['hostname'],type(info_res['hostname'])
ip = str(info_res['hostname'])
print type(ip),'ip.....'

last_minute_file = Popen('grep "20:17:" %s' % file_path,shell=True, stdout=PIPE, stderr=PIPE)
# last_minute_file = Popen('grep "%s" %s' % (file_time,file_path),shell=True, stdout=PIPE, stderr=PIPE)
stdout = last_minute_file.communicate()
file_str = "".join(stdout)
file_list = file_str.split('\n')
print file_list
#去掉空值
file_list.remove('')

for line in file_list:
    for filter in filter_str:
        index = line.find('%s' % filter)
        if index > 0:
            tmplist.append({'ip=%s %s %s' % (ip,line.split('%s' % filter)[0],filter):line.split('%s' % filter)[1]})
        else:
            print 'Invalid Line...'

#post parameter
for parameter in tmplist:
    filetmp = urllib.urlencode(parameter)
    print type(filetmp),'***'
    params = urllib.urlencode({'name': 'le.com', 'age': '5'})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    httpClient = httplib.HTTPConnection('weixin-aoc.lecloud.com', 3000, timeout=10)
    httpClient.request('POST', '/openwx/send_group_message?displayname=应用运维告警接收群&content=%s' % filetmp, params, headers)
    response = httpClient.getresponse()
    print response.status
    print response.reason