#-*- coding:utf-8 -*-
__author__ = 'chuan'

'''
切大饼：
一刀=1+1=2
两刀=1+1+2=4
三刀=1+1+2+3=7
四刀=1+1+2+3+4=11
结论：p(n) = p(n-1) + n
求切100刀，能分出多少块
'''

qie_list = [0] * 100
qie_list[0] = 1
for i in xrange(1,100):
    qie_list[i] = qie_list[i-1] + i
print '切100刀可以切出：%s' % qie_list[99]