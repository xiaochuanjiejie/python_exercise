# -*- coding: UTF-8 -*-
__author__ = 'chuan'

class Student:
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integar!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

s = Student()
#实际转化为s.set_score(60)
s.score = 60
#实际转化为s.get_score()
print s.score