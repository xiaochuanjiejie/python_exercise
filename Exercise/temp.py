#-*- coding: utf-8 -*-
__author__ = 'chuan'

items = ( ( 3 , 2 ) , ( 5 , 7 ) , ( 1 , 9 ) , 0 , ( 1 ) )
print len(items)
print items[1]
print items[2][0]
print type(items[0])
print type(items[4])
new4 = tuple('%s' % items[4])
print type(new4)