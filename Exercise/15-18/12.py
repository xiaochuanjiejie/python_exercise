#-*- coding: utf-8 -*-

class Foo(object):

    '''实例方法'''
    def test(self):
        print 'in test()'

    '''静态方法对比，静态方法除可被实例调用外还可被类调用，普通的实例方法是不可被类调用的。另，静态方法括号跟的参数是直接显示'''
    def foo1(self,x):
        print 'in foo()' + x
    @staticmethod
    def foo_static(x):
        print 'in foo_static()' + x
    # foo_static = staticmethod(foo_static)     //等同于方法前加@staticmethod

    '''类方法，第一个参数类似实例方法的self，是不显示的'''
    @classmethod
    def foo_class(clss):
        print 'in foo_class()'
        print clss
    # foo_class = classmethod(foo_class)        //等同于方法前加@classmethod

p = Foo()
p.test()
p.foo1('实例使用方法')
p.foo_static('实例调用')
Foo.foo_static('类调用')
p.foo_class()
Foo.foo_class()