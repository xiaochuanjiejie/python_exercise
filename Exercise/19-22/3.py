#-*- coding: utf-8 -*-

class Foo(object):
    #静态变量
    num = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Foo(5,6)
print getattr(p,'x')
print getattr(Foo,'num')
print hasattr(p,'x')
print hasattr(Foo,'num')
setattr(p,'z',8)
print getattr(p,'z')
print hasattr(p,'z')
print hasattr(Foo,'z')
delattr(p,'z')
print hasattr(p,'z')
print hasattr(Foo,'z')

print dir(p)
print vars(p)

print dir(Foo)
print vars(Foo)
# print issubclass(Foo,object)
#
# p = Foo()
# print isinstance(p,Foo)
# print isinstance(p,object)