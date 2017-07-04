#coding: utf-8

import re
from time import ctime

# 通过检查每个输出行中整型字段部分的第一个整型是否和该行开头的时间戳相匹配来验证redata.txt中的数据是否完好。
with open('/tmp/email.txt','r') as f:
    for line in f.readlines():
        ss = re.search(r'(.+)::.*::(\d+)',line)
        if ss.group(1) == ctime(int(ss.group(2))):
            print '相等'

# 提取出每行中完整的电子邮件地址。

with open('/tmp/email.txt','r') as f:
    for line in f.readlines():
        ss2 = re.search(r'.*::([\w]+@[\w]+\..*)::.*',line)
        print ss2.group(1)