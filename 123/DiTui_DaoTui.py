#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
倒推法：在不知道初始条件的情况下，经某种递推关系而获知问题的解，再倒过来推
阶乘：1!+2!+3!+...+n!，即：1x1!+2x1!+3x2!+4x3!+...+nx(n-1)!
'''

total = 0
j = 1
n = int(raw_input('input num:\n'))

for i in xrange(1,n+1):
    j = j * i
    total += j
print total