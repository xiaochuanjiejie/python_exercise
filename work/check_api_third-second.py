# -*- coding: utf-8 -*-
__author__ = 'xujunchuan'

from subprocess import PIPE,Popen
import re
import sys


chat = ["10.110.50.25","10.110.50.26","10.110.60.44","10.110.60.45","10.130.208.70","10.130.91.108","10.180.219.132","10.180.91.145","10.183.91.26","10.183.91.27"]
vcm = ["10.110.50.21","10.110.50.22","10.110.60.42","10.110.60.43","10.130.208.72","10.130.91.111","10.180.219.55","10.180.244.191","10.183.91.28","10.183.91.29"]
vcs = ["10.110.50.77","10.110.60.46","10.110.60.59","10.130.211.100","10.130.91.185","10.180.244.134","10.180.244.195","10.183.91.33"]
other = ["10.110.60.47","10.110.60.48","10.110.60.49","10.130.91.120","10.180.219.70","10.180.244.133","10.183.91.31","10.183.91.32"]
action = ["10.110.60.50","10.110.60.57","10.110.60.58","10.130.91.174","10.180.226.210","10.183.91.30"]
danmu = ["10.110.50.76","10.110.60.60","10.130.91.204","10.130.208.74","10.180.91.146","10.183.91.34"]

last_minute_file = Popen('grep "00:00:" /Users/xujunchuan/Documents/info.log',shell=True, stdout=PIPE, stderr=PIPE)
stdout = last_minute_file.communicate()
file_1 = "".join(stdout)
file_2 = file_1.split('\n')
list_url_chat,list_url_vcm,list_url_vcs,list_url_other,list_url_action,list_url_danmu = [],[],[],[],[],[]
for line in file_2:
    if not line.strip():continue
    if float(line.split()[8].split(':')[1]) > 1000.0:
        ip = line.split()[3]
        url = line.split()[6].split('/')[2]
        if ip in chat:
            list_url_chat.append(url)
        elif ip in vcm:
            list_url_vcm.append(url)
        elif ip in vcs:
            list_url_vcs.append(url)
        elif ip in other:
            list_url_other.append(url)
        elif ip in action:
            list_url_action.append(url)
        elif ip in danmu:
            list_url_danmu.append(url)
        # list_url.append(url)
# list_url.sort()
# set_url = set(list_url)   (a.com,b.com)
# for item in set_url:
#     print item,list_url.count(item)

def list_name(lst):
    t_dict = globals()
    global name
    for key in t_dict:
        if type(t_dict[key]) is type(lst) and t_dict[key] == lst:
            print key
            name = key
            return name

def filtration(result):
    result.sort()
    list_name(result)
    set_result = set(result)
    for item in set_result:
        print item,result.count(item)
        a = item
        b = result.count(item)
        # with open("/tmp/123",'a') as file_res:
        #     file_res.writelines(a + '   ' + str(b) + '\n')
        with open("/tmp/" + name,'a') as file_res:
            file_res.writelines(a + '   ' + str(b) + '\n')

filtration(list_url_chat)
# filtration(list_url_vcm)
# filtration(list_url_vcs)
# filtration(list_url_other)
# filtration(list_url_action)
# filtration(list_url_danmu)