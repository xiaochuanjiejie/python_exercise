# -*- coding: UTF-8 -*-
__author__ = 'chuan'

a = []
a = tuple(input('输入三个整数： '))
x = a[0]
y = a[1]
z = a[2]
print 'x_value is %s,y_value is %s,z_value is %s' % (x,y,z)
if x > y:
    if x > z:
        if y > z:
            print 'x>y>z'
        else:
            print 'x>z>y'
    else:
        print 'z>x>y'
else:
    if x > z:
        print 'y>x>z'
    else:
        if y > z:
            print 'y>z>x'
        else:
            print 'z>y>x'