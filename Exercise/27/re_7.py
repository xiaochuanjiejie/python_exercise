#coding: utf-8

import re

num = raw_input('input num: ')
# 匹配8/10/16进制
ss = re.search(r'^(\+|-)?((0|[1-9]\d+)|(0[0-7]*)|(0[xX][0-9a-fA-F]+))',num)
print ss.group()