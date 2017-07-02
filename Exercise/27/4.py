#coding: utf-8

import re

result_list = []

with open('/Users/zj/Desktop/ip.txt') as f1:
    for line in f1.readlines():
        ss = re.findall('(.*)"Sogou web spider',line)
        print ss
        break
        if ss:
            result_list.append(ss[0].strip())
print set(result_list)