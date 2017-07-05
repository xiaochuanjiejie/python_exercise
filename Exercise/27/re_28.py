#coding: utf-8

import re

# 区号（第一组的三个数字和它后面的连字符）是可选的，即你写的正则表达式对800-555-1212和555-1212都可匹配。
area = raw_input('区号: ')
ss = re.match(r'(\d{3}\-)?(\d{3})-(\d{4})',area)
print ss.group()