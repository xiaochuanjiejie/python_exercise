#-*- coding: utf-8 -*-

class Foo(object):
    __slots__ = ('x','y','c')
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.c = z

p = Foo(5,6,7)
print p.c
p.z = 100