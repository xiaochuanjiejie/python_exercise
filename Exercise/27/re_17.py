#coding: utf-8

import re

week = {}.fromkeys(('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'),0)
pattern = '(' + '|'.join(week.keys()) + ')'
print pattern

with open('/tmp/email.txt','r') as f:
    for line in f.readlines():
        ss = re.match(pattern,line)
        if ss is not None:
            week[ss.group()] += 1

print week