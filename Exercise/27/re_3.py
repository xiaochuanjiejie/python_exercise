#coding: utf-8

import re

name = 'jake, Oha 12312312'
ss = re.search(r'\b\w+, \w+',name)
print ss.group()