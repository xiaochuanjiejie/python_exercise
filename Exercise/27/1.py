#coding: utf-8

import re

# search
str = 'purple alice-b@google.com monkey dishwasher'
ss = re.search(r'([\w.-]+)@([\w.-]+)',str)
print ss.group()
print '---'
print ss.group(0)
print ss.group(1)
print ss.group(2)


# findall
str = 'purple alice-b@google.com monkey dishwasher xiaochuanjiejie@163.com'
ss1 = re.findall(r'([\w.-]+)@([\w.-]+)',str)
print ss1