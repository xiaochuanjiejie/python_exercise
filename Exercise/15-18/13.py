#-*- coding: utf-8 -*-

class Foo(object):
    pass

class Foo2(Foo):
    pass

print issubclass(Foo2,Foo)      //判断Foo2是否为Foo的子类