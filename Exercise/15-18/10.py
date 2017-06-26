#-*- coding: utf-8 -*-

class Foo(object):
    '''类属性'''
    jishu = 100
    my_list = []

    def testJishu(self,number):
        '''定义实例属性'''
        self.jishu = number

    def print_jishu(self):
        print 'jishu，我是实例变量:',self.jishu

mytest = Foo()
mytest.testJishu(20)
mytest.print_jishu()

mytest.jishu += 1
mytest.my_list.append('change by new object')

print mytest.jishu
print mytest.my_list
print Foo.jishu
print Foo.my_list

Foo.jishu += 1
Foo.my_list.append('change by class')

print mytest.jishu
print Foo.jishu
print Foo.my_list,mytest.my_list