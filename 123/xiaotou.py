#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
 a 说: "我不是小偷。"
 b 说: " c 是小偷。"
 c说: "小偷肯定是 d 。"
 d 说: " c 在胡说 "
 求谁是小偷。
 思路：将四个人说的话都逻辑表达式化，然后穷举法，类似于百鸡题
'''

for xiaotou in ['a','b','c','d']:
    sum = (xiaotou != 'a') + (xiaotou == 'c') + (xiaotou == 'd') + (xiaotou != 'd')
    if sum == 3:
        print '小偷是: %s' % xiaotou