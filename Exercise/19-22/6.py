#-*- coding: utf-8 -*-

class Foo(object):
    def __init__(self,x):
        self.x = x
    def __getattr__(self, item):
        if item == 'age':
            return 35
        else:
            raise AttributeError,item

p = Foo(5)
#实例p有x属性，不受重构的getattr方法的影响
print p.x
print getattr(p,'x')
#对于实例没有的属性，则需走重构的getattr方法
print p.age