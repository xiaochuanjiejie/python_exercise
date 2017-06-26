#-*- coding: utf-8 -*-

class Foo(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def test(self):
        print 'in 父类'

class Foo2(Foo):
    def test(self):
        print self.x,self.y
        print 'in 子类'

p = Foo2(2,5)
p.test()