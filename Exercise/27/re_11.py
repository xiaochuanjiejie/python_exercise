#coding: utf-8

import re

email = raw_input('input email: ')
ss = re.search(r'[\w-]+@[a-zA-Z\d]+\.(com|net)',email)
print ss.group()