#-*- coding: utf-8 -*-
__author__ = 'chuan'

scroe = int(raw_input('请输入分数：\n'))

if scroe >= 90:
    print 'A'
elif scroe >= 80 and scroe < 90:
    print 'B'
elif scroe >= 60 and scroe < 80:
    print 'C'
else:
    print '不及格，加油。'