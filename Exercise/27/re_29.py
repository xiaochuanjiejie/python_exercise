#coding: utf-8

import re

# 区号中可以包含圆括号或连字符，而且它们是可选的，就是说你写的正则表达式可以匹配800-555-1212、555-1212或(800)555-1212。
area = raw_input('区号: ')
ss2 = re.match(r'(\d{3}\-)?\d{3}-\d{4}|\(\d{3}\)\d{3}-\d{4}',area)
print ss2.group()