#coding: utf-8

import re
'''
9.322e-36j
.876j
1.23e-1j
'''
num = raw_input('inpu 复数: ')
print type(num)
# ss = re.search(r'^-?\d+\.?(\d+([eE]?[+-]?\d+)?)?j',num)
ss = re.search(r'[-|d]?\.?(\d+([eE]?[+-]?\d+)?)?j',num)
print ss.group()