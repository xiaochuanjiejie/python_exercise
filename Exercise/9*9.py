#-*- coding: utf-8 -*-
# from __future__ import print_function
__author__ = 'chuan'
'''
9 x 9乘法表
'''

a = '1  2  3  4  5  6  7  8  9'
print a
print '-' * len(a)
for i in xrange(1,10):
    # print i,'|'
    for j in xrange(1,10):
        # print i * j,
        value = i * j
        if value == i:
            print i,'|',value,
        else:
            print value,
    print '\n'