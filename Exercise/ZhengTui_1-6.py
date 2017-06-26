#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
1
12
123
1234
12345
123456
'''

line = int(raw_input('input line number:'))
i = 1
while i <= line:
    i += 1
    j = 1
    while j < i:
        print j,
        j += 1
    print