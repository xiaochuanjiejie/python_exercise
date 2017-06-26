#-*- coding: utf-8 -*-
__author__ = 'chuan'
'''
解释"is "和"= ="之间的差异, 例说明,对is 返回为假,= = 返回为真。
答：
Python中的对象包含三要素：id、type、value
其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值
is判断的是a对象是否就是b对象，是通过id来判断的
==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
'''

a = 1
b = 1.0

if a is b:
    print 'a:%s 和 b:%s (is)ID相等' % (id(a),id(b))
else:
    print 'a:%s 和 b:%s (is)ID不等' % (id(a),id(b))

if a == b:
    print 'a:%s 和 b:%s VALUE相等' % (a,b)
else:
    print 'a:%s 和 b:%s VALUE不等' % (a,b)