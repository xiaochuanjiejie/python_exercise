#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
     1
    21
   321
  4321
 54321
654321
'''

line = int(raw_input('input line number:'))
# i = 7
# while i >= 1:
a = 1
while a < (line + 1):
    i = 7
    j = 1
    while j < i:
        value = i - j
        j += 1
        if value > a:
            print ' ',
        else:
            print value,
    a += 1
    print '\n'