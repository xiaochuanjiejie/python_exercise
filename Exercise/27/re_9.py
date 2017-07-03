#coding: utf-8

import re

num = raw_input('input num: ')
ss = re.search(r'\d+\.\d*',num)
print ss.group()