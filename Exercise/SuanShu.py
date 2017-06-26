#-*- coding: utf-8 -*-
__author__ = 'chuan'
'''
1*8+1=9
12 * 8 + 2 = 98
123 * 8 + 3 = 987
1234 * 8 + 4 = 9876
12345 * 8 + 5 = 98765
123456 * 8 + 6 = 987654
1234567 * 8 + 7 = 9876543
12345678 * 8 + 8 = 98765432
123456789 * 8 + 9 = 987654321
'''

line = 1
num1 = [0] * 10
num1[0] = 0
while line < 10:
# for line in xrange(1,10):
    num1[line] = 10 * num1[line - 1] + (line - 1) + 1
    # print num1[line]
    value = num1[line] * 8 + line
    print '%s * 8 + %s = %s' % (num1[line],line,value)
    line += 1