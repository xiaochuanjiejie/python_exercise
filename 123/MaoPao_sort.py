# -*- coding: utf-8 -*-
__author__ = 'chuan'
'''
冒泡排序
8个数字，从第一个开始两两比对，则需比对7次，那么j就需要小于8，若j从0开始，那么就小于7则等于7次。
'''

t_list = [1,3,111,67,89,145,13,2]

i = 0
#在两个while的条件小括号内，如果不使用-i，也可以冒泡排序，但是不优雅，如果不每次减i，那么就相当于while i < 8，每次都需要循环7次，那么没用意义
while i < (len(t_list) - i):
    j = 0
    while j < (len(t_list) - 1 - i):
        if t_list[j] > t_list[j+1]:
            t_list[j],t_list[j+1] = t_list[j+1],t_list[j]
        j += 1
        print t_list
    i += 1
    print '第{0}轮完成'.format(i)
print t_list