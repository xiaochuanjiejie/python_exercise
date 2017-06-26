#-*- coding: utf-8 -*-
from __future__ import print_function
__author__ = 'chuan'
'''
用循环崁套的⽅方式计算连续整数之和,要求输出结果如下。如果输⼊入数5,输出连续5个 数字之和:
1 = 1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
'''
line = input('Please input num(int):')
i = 1
sum1 = 0
while i <= line:
    i += 1
    j = 1
    sum1 = 0
    while j < i:
        # print j,'+',
        sum1 = sum1 + j
        if j < (i-1):
            print(j, end="+")
        else:
            print(j,'=',sum1)
        # print '+'
        j += 1
    # print('=',sum1)
# print
# sum = 0
# count = 1
# num = raw_input("Enter an integer:")
# num = int(num)
# while(count <= num):
#     sum = sum + count
#     count = count + 1
#     print sum,",",

# sum = 0
# count = 1
# num = raw_input("input an Integer:")
# num = int(num)
# while count <=num:
#     print count,
#     sum = sum + count
#     if(count != num):
#         print "+",
#     count  = count + 1
# print "=",sum