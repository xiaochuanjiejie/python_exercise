#-*- coding: utf-8 -*-
__author__ = 'chuan'
#无穷循环
#计数循环就是:i = 0 \ while i < 10
#第一种格式:1 2 3 4 6 7 8 9 10
i = 0
while True:
    i += 1
    if i > 10:
        break
    if i == 5:
        continue
    print i,
#第二种格式:1 2 3 4 6 7 8 9 10 11
i = 0
flag = True
while flag:
    i += 1
    if i > 10:
        flag = False
    if i == 5:
        continue
    print i,