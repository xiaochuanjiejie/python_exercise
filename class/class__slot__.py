# -*- coding: UTF-8 -*-
__author__ = 'chuan'
#手动为实例添加属性，绑定方法.动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
class Student:
    pass

s1 = Student()
s1.name = 'bob'
print s1.name

def set_age(self,age):
    self.age = age
    return self.age

from types import MethodType
s1.set_age = MethodType(set_age,s1,Student)
print s1.set_age(21)
#但对于未绑定方法的实例，不起作用
#s2 = Student()
#s2.name = 'jake'
#print s2.set_age(22)
#为了给所有实例都绑定方法，可以给class绑定方法
Student.set_age = MethodType(set_age,None,Student)
s3 = Student()
print s3.set_age(23)

#使用__slots__限制class属性（仅在3.x版本有效）
class Student1:
    __slots__ = ('name','score')
s4 = Student1()
s4.name  = 'bob'
s4.score = '34'
s4.age   = 21
print s4.name,s4.score,s4.age
