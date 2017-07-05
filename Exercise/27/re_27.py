#coding: utf-8

import re

with open('/tmp/email.txt','r') as f1:
    for line in f1.readlines():
        ss = re.match(r'.+\s(\w+)\s+(\d+).*(\d{4})::',line)
        if ss is not None:
            print '年-月-日: %s-%s-%s' % (ss.group(3),ss.group(1),ss.group(2))