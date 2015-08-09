# -*- coding: UTF-8 -*-
__author__ = 'chuan'

#共享引用下对列表(可变对象)的修改是会对引用对象产生影响的

from module_small import x,y
print x
x = 0
y[0] = 'modify'
print x
print y

print '###'

import module_small
print module_small.x
module_small.x = 123
print module_small.x
print module_small.y
