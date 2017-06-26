# -*- coding: UTF-8 -*-
__author__ = 'chuan'
'''
将列表内的元素，排序
选择排序：将剩下的每一个元素和没有比过的做比较，如小则交换
方法很多，比如list的
'''

t_list = [7,9,3,16,1,18,21,56,90,101,13]
len1 = len(t_list)

for i in xrange(len1):
    small = i
    for j in xrange(i+1,len1):
        if t_list[j] < t_list[small]:
            small = j
    if small != i:
        t_list[i],t_list[small] = t_list[small],t_list[i]
print t_list