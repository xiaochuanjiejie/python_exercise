#coding: utf-8

import re

num = raw_input('input num: ')
print type(num)

ss = re.search(r'\d+L?',num)
print ss.group()