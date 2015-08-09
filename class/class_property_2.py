# -*- coding: UTF-8 -*-
__author__ = 'chuan'

class Student:
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        self.age = 2015 - self.birth
        return self.age

s = Student()
s.birth = 2001
print s.birth
print s.age


# #若不使用property方式的原始方法
# class pr:
#     def __str__(self):
#         return '[Person: %s]' % (self.age)
# class Student(pr):
#     def get_birth(self):
#         return self.birth
#     def set_birth(self,value):
#         self.birth = value
#     def age(self):
#         self.age = 2015 - self.birth
#         return self.age
#         # print self.age
#
# s = Student()
# s.set_birth(2001)
# s.get_birth()
# #若没有下面这行，那么print s则会产生：[Person: <bound method Student.age of <__main__.Student instance at 0x00000000020D5B48>>]
# s.age()
# print s