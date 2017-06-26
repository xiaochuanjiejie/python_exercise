#-*- coding: utf-8 -*-
__author__ = 'chuan'

while True:
    for x in range(6):
        y = 2 * x + 1
        print y
        if y>9 :
            break

'''
x等于4时，y==9仍继续执行for循环；x等于5，y==11则退出for循环；进入while True，仍旧循环至x等于5再次退出。
'''