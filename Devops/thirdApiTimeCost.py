#!env python
#coding=utf-8

import os
import sys
import json
import re
import socket
import time
import types
import traceback
import requests

LogFile='/letv/logs/tomcat/iptv/tomcat1-httpClient.log'
LogSize=os.stat(LogFile).st_size
LogOffSet=50*1024*1024 #Byte
LogArr  = []
Domain  = {}
TimeAvgDict = {}
Stastics= {}
PostArr = []
Trigger = 1000
Now     = int(time.time())
Agent_Post_Url="http://localhost:1567/v1/push"
Date    = time.strftime("%Y-%m-%d %H:%M", time.localtime(Now - 60))

Pattern = r'%s:\d+[\|,]\b((?:http|thrift)\b:\/\/[\.\w]+).+\|(\d{3})\|(\d+)\|(\d+)\|\d$' % Date
#Match = re.compile(Pattern)

API_ARR = [
    'http://api.boss.cp21.ott.cibntv.net',
    'http://api.live.letv.com',
    'http://api.message.le.com',
    'http://api.my.cp21.ott.cibntv.net',
    'http://api.sso.cp21.ott.cibntv.net',
    'http://api.zhifu.cp21.ott.cibntv.net',
    'http://d.itv.letv.com',
    'http://data.so.cp21.ott.cibntv.net',
    'http://gc.cp21.ott.cibntv.net',
    'http://hd.my.cp21.ott.cibntv.net',
    'http://i.api.cp21.ott.cibntv.net',
    'http://i.static.itv.letv.com',
    'http://i.top.letv.com',
    'http://le.so.cp21.ott.cibntv.net',
    'http://open.api.cp21.ott.cibntv.net',
    'http://rec.cp21.ott.cibntv.net',
    'http://rec.ysbbx.com',
    'http://s.itv.letv.com',
    'http://static.api.cp21.ott.cibntv.net',
    'http://suggest.cp21.ott.cibntv.net',
    'http://v.stat.cp21.ott.cibntv.net',
    'http://yuanxian.cp21.ott.cibntv.net',
    'thrift://serving.GenericServing',
]

try:
    FH = open(LogFile,'r')
    if LogOffSet >= LogSize:
        LogOffSet = LogSize
    FH.seek(-LogOffSet,2)
    LogArr = FH.readlines()
    FH.close()
except:
    traceback.print_exc()

def ReFilte(x):
    #MatchObj = Match.match(x)
    MatchObj = re.match(Pattern,x)
    if MatchObj is not None:
        domain = MatchObj.group(1)
        Domain = {
            domain:{
                'domain': domain,
                'resp_status': MatchObj.group(2),
                'resp_size'  : MatchObj.group(3),
                'resp_time'  : MatchObj.group(4),
            }
        }
        return Domain
    #else: #debug
    #    print "not match "

List = map(ReFilte,LogArr)
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.0.0.0', 0))
        (addr, port) = s.getsockname()
        s.close()
        return addr
    except socket.error:
        return socket.gethostbyname(socket.gethostname())

def Stats(List):
    TimeAvgDict = {}
    if List:
        for i in List:
            if type(i) is dict:
                if type(i) is dict:
                    Domain_Dict = i
                    for domain in Domain_Dict.keys():
                        Api=Domain_Dict[domain]['domain']
                        Time=Domain_Dict[domain]['resp_time']

                        if TimeAvgDict.has_key(Api) is False:
                            TimeAvgDict[Api] = {}
                        if TimeAvgDict[Api].has_key('total_time') is False:
                            TimeAvgDict[Api]['total_time'] = 0
                        if TimeAvgDict[Api].has_key('total_nums') is False:
                            TimeAvgDict[Api]['total_nums'] = 0
                        if int(Time):
                            TimeAvgDict[Api]['total_time'] += int(Time)
                            TimeAvgDict[Api]['total_nums'] += 1
        return TimeAvgDict
    else:
        for Api in API_ARR:
             if TimeAvgDict.has_key(Api):
                 if TimeAvgDict[Api].haskey('total_time') is False:
                     TimeAvgDict[Api]['total_time'] = 0
                 if TimeAvgDict[Api].haskey('total_nums') is False:
                     TimeAvgDict[Api]['total_nums'] = 0
        return TimeAvgDict

# 获取统计
count = Stats(List)
Host = get_local_ip()

def TimeAvgArr(x):
    for api in API_ARR:
        if api not in x.keys():
            if x.has_key(api) is False:
                x[api] = {}
                if x[api].has_key('total_time') is False:
                    x[api]['total_time'] = 0
                if x[api].has_key('total_nums') is False:
                    x[api]['total_nums'] = 1
    for (domain,stats) in x.items():
        avg = x[domain]['total_time'] / x[domain]['total_nums']
        PostData = {
            "step"              : 60,
            "endpoint"          : Host,
            "tags"              : 'domain=' + domain,
            "timestamp"         : Now,
            "metric"            : "resp_time(ms)",
            "value"             : avg,
            "counterType"       : "GAUGE"
        }
        PostArr.append(PostData)
    return PostArr

PostTimeAvg = json.dumps(TimeAvgArr(count),indent=4)

def POST(x):
    Respone = requests.post(Agent_Post_Url,x)
    print Respone

if len(sys.argv) == 2:
    if sys.argv[1] == "--test":
        print PostTimeAvg + "\n"
else:
    POST(PostTimeAvg)
