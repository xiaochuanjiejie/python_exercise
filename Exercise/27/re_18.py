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
        print 'Email: %s' % ss2.group(1)

# 只提取时间戳中的月份
with open('/tmp/email.txt','r') as f:
    for line in f.readlines():
        ss3 = re.search(r'\w+\s(\w+)\s.*',line)
        print '月份: %s' % ss3.group(1)

# 只提取时间戳中的年份
with open('/tmp/email.txt','r') as f:
    for line in f.readlines():
        ss4 = re.search(r'.*\s(\d{4}).*',line)
        print '年份: %s' % ss4.group(1)

# 只提取时间戳中的时间
with open('/tmp/email.txt','r') as f:
    for line in f.readlines():
        ss5 = re.search(r'.+(\d\d:\d\d:\d\d)',line)
        ss6 = re.search(r'.+::(\w+)@(.+)::',line)
        print '小时分秒: %s' % ss5.group(1)
        print '登录名: %s;域名: %s' % (ss6.group(1),ss6.group(2))

