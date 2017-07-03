#coding: utf-8

import re

url = raw_input('input domain: ')
ss = re.match(r'^www\.[a-zA-Z0-9-]+\.(net|com|edu)$',url)
if ss:
    print ss.group()
else:
    print 'not match'