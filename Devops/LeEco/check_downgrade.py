#!env python
#-*- coding: utf-8 -*-

import os
import json
import time
import requests

# basic falcon info
step = 60
outdata = []
info_res = {}
agentPostUrl = 'http://localhost:1567/v1/push'
conf = '/usr/local/LeMonitor/falcon-agent/cfg.json'
# 定义json格式
def simpleMetric(endpoint,metric,ts,step,value,counterType,tags):
    data = {
        "endpoint": endpoint,
        "metric": metric,
        "timestamp": ts,
        "step": step,
        "value": value,
        "counterType": counterType,
        "tags": tags
    }
    return data
# 读取falcon基础信息
def basicinfo(conf):
    with open(conf) as mid:
        source = json.load(mid)
        info_res['hostname'] = source["hostname"]
    return info_res
def POST(x):
    Respone = requests.post(agentPostUrl,x)
    #print Respone

# 取IP
basicinfo(conf)
ip = str(info_res['hostname'])
ts = int(time.time())
with open('/dev/shm/downgrade_conf.json') as f:
	result = json.load(f)
	for (k,v) in result.items():
		tags = 'name=' + k
		value = v
		counterType = 'GAUGE'
		metric = 'downgrade'
		outdata.append(simpleMetric(ip,metric,ts,step,value,counterType,tags))
outjson = json.dumps(outdata,indent=2)
#print outjson

if __name__ == '__main__':
	POST(outjson)
