#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
123456
12345
1234
123
12
1
'''

line = int(raw_input('input line number:'))
i = line + 1
while i >= 1:
    i -= 1
    j = 1
    while j <= i:
        print j,
        j += 1
    print