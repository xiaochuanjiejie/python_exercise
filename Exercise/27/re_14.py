#coding: utf-8

import re

month = raw_input('输入月份:')
ss = re.search(r'^(0|1)?[0-9]?',month)
print ss.group()