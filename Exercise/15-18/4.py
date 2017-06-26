#-*- coding: utf-8 -*-

class Foo(object):
    """定义一个类，说明属性相关的事"""
    x = 100     #静态变量
    def print_x(self):
        print Foo.x

print Foo.x
Foo.x += 1
print Foo.x

p = Foo()
p.print_x()

print dir(Foo)
print Foo.__dict__
print Foo.__doc__
print Foo.__name__
print Foo.__module__
print Foo.__bases__
print Foo.__class__