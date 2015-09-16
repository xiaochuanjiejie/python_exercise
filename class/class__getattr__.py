# -*- coding: UTF-8 -*-
__author__ = 'chuan'

#类的方法和属性不存在，默认返回普通用法
class Student:
    def __init__(self):
        self.name = 'bob'
    # def __getattr__(self, attr):
    #     if attr == 'score':
    #         return 99
    # def
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# s = Student('bo1b')
s = Student()
print s.age(),s.name
# print s.score()

#类的方法和属性不存在，默认返回的迭代用法
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, attr):
        print self._path    #加此行可看到“status.user.timeline.list”是逐词往类送参的
        return Chain('%s/%s' % (self._path, attr))
    def __str__(self):
        return self._path
s = Chain()
print s.status.user.timeline.list