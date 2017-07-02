#coding: utf-8

import re

# 替换
str1 = 'sss b jk b kkiib jkiils'
str2 = 'purple alice-b@google.com monkey dishwasher xiaochuanjiejie@163.com'

ss1 = re.sub(r'b\s*',r'B',str1)     #\s代表空格
print ss1
ss2 = re.sub(r'([\w.-]+)@([\w.-]+)',r'\1@126.com',str2)
print ss2

# 分割split
ss3 = re.split(r'b\s*',str1)
print ss3

# 或
str3 = 'sss b jk b kkiib jkiilsb820'
ss4 = re.findall(r'b\d+|b\s*\w',str3)
print ss4